import os
import random
import string
from dataclasses import dataclass, field
from typing import Optional

import randomname


BASE_NAME_FOR_WANDB = "BASE_NAME_FOR_WANDB"
TRAINING_JOB_NAME = "TRAINING_JOB_NAME"  # defined by sagemaker


@dataclass
class WeightsAndBiasesConfig:
    entity: Optional[str] = None
    group: Optional[str] = None
    name: Optional[str] = None
    id: str = field(default_factory=lambda: "".join(random.choices(string.ascii_lowercase + string.digits, k=8)))

    def is_main(self) -> bool:
        assert self.name is not None
        return self.name.endswith("__main")

    @classmethod
    def create_main_config(cls, create_group: bool, entity: Optional[str] = "globality") -> "WeightsAndBiasesConfig":
        """ Create a config for the main process wandb run (which may be the only run). """
        group, name = None, None
        # Use a base_name taken from `BASE_NAME_FOR_WANDB` if it exists, else `TRAINING_JOB_NAME`,
        # else a random name. This is used as the group name and as the prefix of the run name.
        if BASE_NAME_FOR_WANDB in os.environ:
            base_name = os.environ[BASE_NAME_FOR_WANDB]
        elif TRAINING_JOB_NAME in os.environ:
            base_name = os.environ[TRAINING_JOB_NAME]
        else:
            base_name = randomname.get_name()
        name = f"{base_name}__main"
        if create_group:
            group = base_name
        return cls(entity=entity, group=group, name=name)
