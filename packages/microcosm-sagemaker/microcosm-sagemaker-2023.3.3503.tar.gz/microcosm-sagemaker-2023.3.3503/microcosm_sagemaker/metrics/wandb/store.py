import random
import string
from logging import Logger
from typing import Optional

from microcosm.api import binding, defaults
from microcosm_logging.decorators import logger

from microcosm_sagemaker.decorators import metrics_observer
from microcosm_sagemaker.metrics.wandb.wandb_config import WeightsAndBiasesConfig


try:
    import wandb
    from wandb.errors import CommError
except ImportError:
    pass


@metrics_observer()
@logger
@binding("weights_and_biases")
@defaults(
    enable=None,
)
class WeightsAndBiases:
    logger: Logger

    def __init__(self, graph):
        self.graph = graph
        self.enable = (
            # If it is not explicitly enabled or disabled, enable if not testing.
            graph.config.weights_and_biases.enable or not graph.metadata.testing
        )
        if self.enable:
            try:
                wandb
            except NameError:
                self.logger.warning("wandb is enabled but not installed!!!")
                self.enable = False
        self.project_name = graph.metadata.name.replace("_", "-")
        self.bundle_and_dependencies_config_extractor = self.graph.bundle_and_dependencies_config_extractor
        self.active_bundle = getattr(graph, graph.config.active_bundle)
        self.wandb_run = None

        # Settings used by init to configure the wandb run. These need to be set before the call to
        # init() if non-default values are needed. A true value in `from_server` is used for joining an
        # existing (completed) run, typically from a different machine.
        self.run_config: Optional[WeightsAndBiasesConfig] = None
        self.from_server: bool = False

    def set_from_server_config(self):
        """ Configure the loading of a wandb run from wandb server data (for use when pushing
        new data to a previously completed run (potentially from a different machine)."""
        if self.wandb_run is not None:
            self.logger.warning(
                "wandb run already exists! changes to use wandb server config won't take effect!"
            )
        self.from_server = True
        run_path = self.graph.config.wandb.run_path
        entity, project, id_ = run_path.split("/")
        if project != self.project_name:
            raise ValueError(
                f"wandb project implied by run_path {run_path} is different than expected {self.project_name}!"
            )
        self.run_config = WeightsAndBiasesConfig(
            entity=entity,
            id=id_,
        )
        run_path = f"{self.run_config.entity}/{self.project_name}/{self.run_config.id}"
        self.logger.info(f"wandb server config: run_path = {run_path}")

    def init(self) -> None:
        """ Initialize wandb run. """

        # Only initialize wandb if it is enabled
        if not self.enable:
            return

        self.wandb_run = wandb.run

        # Only initialize/load wandb if it is not already created/loaded
        if self.wandb_run is not None:
            self.logger.info(f"wandb run {self.wandb_run.name}/{self.wandb_run.id} already exists!")
            return

        if not self.from_server:
            # Create a new wandb run. If `run_config` is None, we assume this is for the main process
            # (for spawned processes, it should be set prior to calling `init`).
            if self.run_config is None:
                self.run_config = WeightsAndBiasesConfig.create_main_config(create_group=True)
            assert self.run_config is not None
            self.wandb_run = wandb.init(
                project=self.project_name,
                config=self.bundle_and_dependencies_config_extractor(self.active_bundle),
                **self.run_config.__dict__
            )
            if self.wandb_run is None:
                raise Exception(f"Could not create wandb run (run_config: {self.run_config})!?!")
            self.logger.info(f"A new `weights & biases` run was created: {self.wandb_run.path}")
            if self.run_config.is_main():
                # Injecting the wandb run path into the config
                self.graph.config.wandb.run_path = self.wandb_run.path
                # Adding the link to the Weights & Biases run to the landing page
                landing_convention_links = self.graph.config.landing_convention.get("links", {})
                landing_convention_links.update({"Weights & Biases": self.wandb_run.get_url()})
                self.graph.config.landing_convention.update({"links": landing_convention_links})
        else:
            # Join an existing run, typically from a different machine. Useful for associating data
            # with the wandb run after training is completed.
            if self.run_config is None:
                raise ValueError("run_config must be defined if from_server is true!")
            run_path = f"{self.run_config.entity}/{self.project_name}/{self.run_config.id}"
            try:
                self.wandb_run = wandb.Api().run(path=run_path)
                self.logger.info(f"The existing Weights & Biases run was loaded: {run_path}")
            except CommError:
                # If the previous run cannot be found:
                #   - Start a new run instead
                #   - Add a note to the new run that this run is related to a previous run
                self.logger.warning(f"Could not find run: {run_path}")
                new_id = f"{self.run_config.id}_{''.join(random.choices(string.ascii_lowercase + string.digits, k=4))}"
                self.wandb_run = wandb.init(
                    project=self.project_name,
                    name=self.run_config.name,
                    entity=self.run_config.entity,
                    group=self.run_config.group or None,
                    id=new_id,
                    notes=f"Related to previous run: {run_path}"
                )

    def log_timeseries(self, **kwargs):
        step = kwargs.pop("step", None)
        self.wandb_run.log(kwargs, step=step)
        return None

    def log_static(self, **kwargs):
        self.wandb_run.summary.update(kwargs)
        return None
