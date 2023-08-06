"""
Discrete variable module
"""

import numpy as np

from .variable import Variable

CATEGORIES_PREFIX: str = "Cat"


class NominalVariable(Variable):
    """
    A nominal variable defined by a distribution
    """

    def __init__(self,
                 label: str,
                 categories_count: int,
                 missing_values_fraction: float = 0) -> None:
        super().__init__(label, missing_values_fraction)
        self.__values = []
        self.__categories = self.__init_categories_options(categories_count)

    @property
    def categories(self) -> list:
        """Get categories

        Returns:
            np.ndarray: categories
        """
        return self.__categories

    def simulate_values(self, size: int) -> np.ndarray[str]:
        self.__values = np.random.choice(self.__categories, size)
        return self.__values

    def __init_categories_options(self, categories_count) -> list:
        categories = np.arange(
            1, categories_count+1).astype(str)
        return [CATEGORIES_PREFIX +
                category for category in categories]
