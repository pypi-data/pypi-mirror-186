from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class AtnSpaceheatStrategyName(StrEnum):
    """


    Choices and descriptions:

      * NoActor:
      * SupervisorA:
      * HeatPumpWithBoostStore:
    """

    NoActor = auto()
    SupervisorA = auto()
    HeatPumpWithBoostStore = auto()

    @classmethod
    def default(cls) -> "AtnSpaceheatStrategyName":
        """
        Returns default value NoActor
        """
        return cls.NoActor

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
