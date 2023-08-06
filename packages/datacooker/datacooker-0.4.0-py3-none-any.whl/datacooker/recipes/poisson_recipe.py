"""
PoissonRecipe module
"""

import numpy as np
from .recipe import Recipe


class PoissonRecipe(Recipe):
    """
    Recipe for cooking a dataset that may be modeled by a GLM using Poisson family
    """

    def _apply_model(self, error_values):
        z_values = self._model(self._data, error_values)
        lambda_param = np.exp(z_values)
        return np.random.poisson(lambda_param)
