from random import seed

from microcosm.api import defaults
from microcosm.config.validation import typed

from microcosm_sagemaker.decorators import training_initializer


@defaults(
    seed=typed(int, 42),
)
@training_initializer()
class Random:
    def __init__(self, graph):
        self.seed = graph.config.random.seed

    def init(self):
        # Seed python random
        seed(self.seed)

        # Seed numpy if installed
        try:
            import numpy as np
            np.random.seed(self.seed)
        except ImportError:
            pass

        # Seed torch if installed
        try:
            from torch import manual_seed
            manual_seed(self.seed)
        except ImportError:
            pass

        # make torch operations deterministic, esp. LSTM/GRU
        # see https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html#torch.nn.LSTM
        # and https://pytorch.org/docs/stable/notes/randomness.html
        try:
            from torch import use_deterministic_algorithms
            use_deterministic_algorithms(True)
            import os
            os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
        # use_deterministic_algorithms added since Pytorch 1.8.0
        except ImportError:
            pass

        # Seed tensorflow if installed
        try:
            from tf.random import set_random_seed
            set_random_seed(self.seed)
        except ImportError:
            pass
