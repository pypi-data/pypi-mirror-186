import subprocess
import sys
from functools import partial
from logging import getLogger
from pathlib import Path

from microcosm.api import defaults
from microcosm.object_graph import ObjectGraph

from microcosm_sagemaker.artifact import BundleInputArtifact, RootInputArtifact, RootOutputArtifact
from microcosm_sagemaker.bundle import Bundle
from microcosm_sagemaker.bundle_orchestrator import BundleOrchestrator
from microcosm_sagemaker.dependency_traverser import traverse_component_and_dependencies
from microcosm_sagemaker.distributed_cluster import is_ddp_like_cluster_defined, is_worker_process
from microcosm_sagemaker.input_data import InputData


@defaults(
    bundle_orchestrator="single_threaded_bundle_orchestrator",
)
class BundleAndDependenciesLoader:
    def __init__(self, graph: ObjectGraph):
        config = graph.config.bundle_and_dependencies_loader
        self.bundle_orchestrator: BundleOrchestrator = getattr(graph, config.bundle_orchestrator)
        self.graph = graph

    def __call__(
        self,
        bundle: Bundle,
        root_input_artifact: RootInputArtifact,
        dependencies_only: bool = False,
    ):
        def load(bundle):
            name = _get_component_name(self.graph, bundle)
            bundle.load(root_input_artifact / name)

        self.bundle_orchestrator(
            bundle=bundle,
            bundle_handler=load,
            dependencies_only=dependencies_only,
        )


def _spawn_fit_and_save_bundle(
    graph: ObjectGraph,
    bundle_name: str,
    input_data_path: Path,
    artifact_path: Path,
) -> None:
    bundle = graph[bundle_name]
    logger = getLogger("spawn_fit_and_save_bundle")

    RootOutputArtifact(artifact_path).save_config(graph.config)

    script_path = Path(__file__).parent / "commands/train_one_bundle.py"
    # sys.executable is used instead of "python" since "python" may not refer to the correct
    # python for the virtual env.
    args = [
        sys.executable,
        str(script_path.absolute()),
        "--bundle-name",
        bundle_name,
        "--input-data-path",
        str(input_data_path.absolute()),
        "--artifact-path",
        str(artifact_path.absolute()),
        "--testing" if graph.metadata.testing else "--no-testing",
    ]
    # If using wandb, we need to add some arguments needed to configure the wandb run for the
    # new process.
    wandb_ = graph.get("wandb")
    if wandb_ is not None and wandb_.run_config is not None:
        run_config = graph.wandb.run_config
        assert run_config.entity is not None and run_config.group is not None
        args += [
            "--wandb-entity",
            run_config.entity,
            "--wandb-group",
            run_config.group,
        ]

    logger.info(f"launching spawned process to train bundle {bundle_name} with args {args}...")
    completed_process = subprocess.run(args)
    completed_process.check_returncode()
    logger.info(f"spawned process to train bundle {bundle_name} completed successfully...")
    bundle.load(BundleInputArtifact(artifact_path / bundle_name))
    logger.info(f"loaded recently trained bundle {bundle_name} in the main process...")


def fit_and_save_bundle(
    graph: ObjectGraph,
    input_data: InputData,
    root_output_artifact: RootOutputArtifact,
    bundle: Bundle,
) -> None:
    bundle_name = _get_component_name(graph, bundle)

    nested_output_artifact = root_output_artifact / bundle_name
    if not is_worker_process():
        nested_output_artifact.init()

    if bundle.spawn_to_fit:
        if is_ddp_like_cluster_defined():
            raise Exception(
                "Cannot spawn new fit process if the main process has already used DDP-style training!"
            )
        _spawn_fit_and_save_bundle(
            graph=graph,
            bundle_name=bundle_name,
            input_data_path=input_data.path,
            artifact_path=root_output_artifact.path,
        )
    else:
        # We call the training_initializers.init() before any bundle.fit()
        # That makes each bundle's training reproducible, regardless of its order in the training queue.
        graph.training_initializers.init()

        bundle.fit(input_data)
        if not is_worker_process():
            bundle.save(nested_output_artifact)


@defaults(
    bundle_orchestrator="single_threaded_bundle_orchestrator",
)
class BundleAndDependenciesTrainer:
    def __init__(self, graph: ObjectGraph):
        config = graph.config.bundle_and_dependencies_trainer
        self.bundle_orchestrator: BundleOrchestrator = getattr(graph, config.bundle_orchestrator)
        self.graph = graph

    def __call__(
        self,
        bundle: Bundle,
        input_data: InputData,
        root_output_artifact: RootOutputArtifact,
        dependencies_only: bool = False,
    ):
        train = partial(
            fit_and_save_bundle,
            self.graph,
            input_data,
            root_output_artifact,
        )

        self.bundle_orchestrator(
            bundle=bundle,
            bundle_handler=train,
            dependencies_only=dependencies_only,
        )


class BundleAndDependenciesConfigExtractor:
    def __init__(self, graph: ObjectGraph):
        self.config = graph.config
        self.graph = graph

    def __call__(self, bundle: Bundle):
        """
        Returns the config from the `bundle`, as well as all of its dependents.

        """
        config = {}

        for bundle_to_handle in traverse_component_and_dependencies(bundle):
            bundle_name = _get_component_name(self.graph, bundle_to_handle)
            bundle_config = getattr(self.config, bundle_name, {})
            config.update(
                {bundle_name: bundle_config}
            )

        return config


def _get_component_name(graph, component):
    return next(
        key
        for key, possible_component in graph.items()
        if possible_component == component
    )
