"""
Continous variable module
"""

from typing import Callable, Tuple
import numpy as np
from scipy.stats import rv_continuous, norm
from scipy.stats._distn_infrastructure import rv_continuous_frozen

from .variable import Variable

ContinousDistribution = (
    rv_continuous |
    Tuple[Callable[[np.number, np.number, int], np.ndarray], np.number, np.number]
)


class ContinousVariable(Variable):
    """
    A continous variable defined by a distribution
    """

    def __init__(self,
                 label: str,
                 distribution: ContinousDistribution = norm(),
                 missing_values_fraction: float = 0) -> None:
        super().__init__(label, missing_values_fraction)
        self.__values = []
        self.__distribution = distribution

    def simulate_values(self, size: int) -> np.ndarray:
        distribution_type = type(self.__distribution)

        if distribution_type is rv_continuous_frozen:
            self.__values = self.__distribution.rvs(size=size)
        else:
            dist_fn, start, stop = self.__distribution
            self.__values = dist_fn(start, stop, size)

        return self.__values
