from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class EmitterPumpFeedbackModel(StrEnum):
    """


    Choices and descriptions:

      * ConstantDeltaT:
      * ConstantGpm:
    """

    ConstantDeltaT = auto()
    ConstantGpm = auto()

    @classmethod
    def default(cls) -> "EmitterPumpFeedbackModel":
        """
        Returns default value ConstantDeltaT
        """
        return cls.ConstantDeltaT

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
