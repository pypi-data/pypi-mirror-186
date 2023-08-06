import json
from logging import getLogger
from pathlib import Path
from typing import Optional

import click
from microcosm.loaders import load_from_dict

from microcosm_sagemaker.app_hooks import create_train_app
from microcosm_sagemaker.artifact import BundleOutputArtifact, RootInputArtifact
from microcosm_sagemaker.bundle_traversal import BundleAndDependenciesLoader
from microcosm_sagemaker.constants import ARTIFACT_CONFIGURATION_PATH
from microcosm_sagemaker.distributed_cluster import is_worker_process
from microcosm_sagemaker.input_data import InputData
from microcosm_sagemaker.metrics.wandb.wandb_config import WeightsAndBiasesConfig


def train_one_bundle(
    bundle_name: str,
    input_data_path: Path,
    artifact_path: Path,
    testing: bool,
    wandb_entity: Optional[str],
    wandb_group: Optional[str],
):
    configuration_path = artifact_path / ARTIFACT_CONFIGURATION_PATH
    if not configuration_path.exists():
        raise ValueError(
            f"train_one_bundle-{bundle_name}: Could not find config file {configuration_path}!"
        )
    with open(configuration_path, "r") as fp:
        extra_loader = load_from_dict(json.load(fp))
    graph = create_train_app(
        extra_loader=extra_loader,
        testing=testing,
    )

    logger = getLogger(f"train_one_bundle-{bundle_name}")
    logger.info(f"configuration_path = {configuration_path}...")

    # Configure wandb if needed. This needs to happen before the call to
    # `graph.training_initializers.init()` which launches the wandb run itself.
    wandb_ = graph.get("wandb")
    if wandb_ is not None and wandb_.enable:
        if wandb_entity is None or wandb_group is None:
            wandb_entity = wandb_entity or "missing"
            wandb_group = wandb_group or "missing"
            raise ValueError(
                f"train_one_bundle-{bundle_name}: wandb is enabled but missing required wandb configuration:"
                f" wandb_entity: {wandb_entity}; wandb_group: {wandb_group}!"
            )
        wandb_name = f"{wandb_group}__{bundle_name}"
        if wandb_name.endswith("_bundle"):
            wandb_name = wandb_name[:-len("_bundle")]
        wandb_.run_config = WeightsAndBiasesConfig(
            entity=wandb_entity, group=wandb_group, name=wandb_name
        )

    graph.training_initializers.init()
    graph.experiment_metrics.init()

    if wandb_ and wandb_.wandb_run:
        logger.info(
            f"initialized experiment metrics... wandb run name: {wandb_.wandb_run.name}"
        )
    elif not testing:
        logger.warning(
            "initialized experiment metrics... no wandb run (testing is false)!"
        )

    try:
        bundle = graph[bundle_name]
    except Exception:
        raise ValueError(f"Could not find bundle {bundle_name} in graph!")

    logger.info("found bundle... about to load dependencies...")
    loader = BundleAndDependenciesLoader(graph)
    loader(bundle=bundle, root_input_artifact=RootInputArtifact(artifact_path), dependencies_only=True)
    logger.info("found bundle... about to start training...")
    bundle.fit(input_data=InputData(input_data_path))
    if not is_worker_process():
        logger.info("done training...")
        out_folder = artifact_path / bundle_name
        bundle.save(BundleOutputArtifact(out_folder))
        logger.info(f"saved artifact to {out_folder}...")


@click.command()
@click.option("--bundle-name", required=True)
@click.option("--input-data-path", required=True)
@click.option("--artifact-path", required=True)
@click.option("--testing/--no-testing", default=False)
@click.option("--wandb-entity", default=None)
@click.option("--wandb-group", default=None)
def main(
    bundle_name: str,
    input_data_path: str,
    artifact_path: str,
    testing: bool,
    wandb_entity: Optional[str],
    wandb_group: Optional[str]
):
    try:
        train_one_bundle(
            bundle_name=bundle_name,
            input_data_path=Path(input_data_path),
            artifact_path=Path(artifact_path),
            testing=testing,
            wandb_entity=wandb_entity,
            wandb_group=wandb_group,
        )
    except Exception as ex:
        getLogger(f"train_one_bundle-{bundle_name}").exception(ex)
        raise ex


if __name__ == '__main__':
    main()
