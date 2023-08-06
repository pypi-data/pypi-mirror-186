"""
LogitRecipe module
"""

import numpy as np
from .recipe import Recipe


class LogitRecipe(Recipe):
    """
    Recipe for cooking a dataset that may be modeled by a logistic regression
    """

    def _apply_model(self, error_values) -> np.ndarray:
        z_values = self._model(self._data, error_values)
        prob = 1 / (1 + np.exp(-z_values))
        return np.random.binomial(1, prob)
