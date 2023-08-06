from microcosm_logging.decorators import logger

from microcosm_sagemaker.distributed_cluster import is_worker_process


@logger
class ExperimentMetrics:
    """
    This registry is a place to register functions that log metrics.
    The `log_static` and `log_timeseries` methods are used to store single-value
    and multiple-value metrics, respectively.

    """
    def __init__(self, graph):
        self.graph = graph
        self.testing = graph.metadata.testing
        self.is_worker_process = is_worker_process()
        self.metric_observers = []

    def register(self, observer):
        if not self.testing and not self.is_worker_process:
            self.metric_observers.append(observer)

    def init(self):
        """
        Calls the init method on all of the registered metric observers.

        """
        for metric_observer in self.metric_observers:
            metric_observer.init()

    def log_timeseries(self, **kwargs):
        if not self.testing and not self.is_worker_process:
            for metric_observer in self.metric_observers:
                response = metric_observer.log_timeseries(**kwargs)
                if response:
                    self.logger.info(response)

    def log_static(self, **kwargs):
        if not self.testing and not self.is_worker_process:
            for metric_observer in self.metric_observers:
                response = metric_observer.log_static(**kwargs)
                if response:
                    self.logger.info(response)
