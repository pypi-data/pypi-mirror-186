"""Variable abstract class module"""

from abc import ABC, abstractmethod
import numpy as np

from datacooker.utils import is_valid_fraction
from datacooker.variables.error_messages import invalid_missing_values_fraction_msg


class Variable(ABC):
    """Variable base abstract class"""

    def __init__(self, label: str, missing_values_fraction: float) -> None:
        self.__label: str = label

        if is_valid_fraction(missing_values_fraction):
            self.__missing_values_fraction: float = missing_values_fraction
        else:
            msg: str = invalid_missing_values_fraction_msg(
                missing_values_fraction, label)
            raise ValueError(msg)

    @property
    def label(self) -> str:
        """
        Returns variable label

        Returns:
            str: variable label
        """
        return self.__label

    @property
    def missing_values_fraction(self) -> float:
        """
        Returns fraction of missing values

        Returns:
            float: fraction of missing variables
        """
        return self.__missing_values_fraction

    @abstractmethod
    def simulate_values(self, size: int) -> np.ndarray:
        """
        Runs simulation to generate values for the variable

        Args:
            size (int): number of entries (array length)

        Returns:
            np.ndarray: values in ndarray format
        """
