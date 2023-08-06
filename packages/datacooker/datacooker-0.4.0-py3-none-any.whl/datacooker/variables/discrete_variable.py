"""
Discrete variable module
"""

import numpy as np
from scipy.stats import rv_discrete, poisson

from .variable import Variable

DiscreteDistribution = rv_discrete | list | np.ndarray


class DiscreteVariable(Variable):
    """
    A discrete variable defined by a distribution
    """

    def __init__(self,
                 label: str,
                 distribution: DiscreteDistribution = poisson(1),
                 missing_values_fraction: float = 0) -> None:
        super().__init__(label, missing_values_fraction)
        self.__values = []
        self.__distribtuion: DiscreteDistribution = distribution

    def simulate_values(self, size: int) -> np.ndarray:
        distribution_type = type(self.__distribtuion)

        if distribution_type is list or distribution_type is np.ndarray:
            self.__values = np.random.choice(self.__distribtuion, size)
        else:
            self.__values = self.__distribtuion.rvs(size=size)

        return self.__values
