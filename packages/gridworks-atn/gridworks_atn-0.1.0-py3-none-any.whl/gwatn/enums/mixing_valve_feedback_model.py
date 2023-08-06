from enum import auto
from typing import List

from fastapi_utils.enums import StrEnum


class MixingValveFeedbackModel(StrEnum):
    """
    Control mechanism for a mixing valve, used by Spaceheat SCADAs

    Choices and descriptions:

      * ConstantSwt: Constant Source Water Temp
      * NaiveVariableSwt: Variable Source Water Temp, naive assumptions about distribution system capabilities
      * CautiousVariableSwt: Variable Source Water Temp, conservative assumptions about distribution system capabilities
    """

    ConstantSwt = auto()
    NaiveVariableSwt = auto()
    CautiousVariableSwt = auto()

    @classmethod
    def default(cls) -> "MixingValveFeedbackModel":
        """
        Returns default value ConstantSwt
        """
        return cls.ConstantSwt

    @classmethod
    def values(cls) -> List[str]:
        """
        Returns enum choices
        """
        return [elt.value for elt in cls]
