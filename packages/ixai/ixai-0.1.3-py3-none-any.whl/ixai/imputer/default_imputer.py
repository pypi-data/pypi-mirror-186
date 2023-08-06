from typing import Callable

from .base import BaseImputer


class DefaultImputer(BaseImputer):
    def __init__(self, model_function: Callable, values: dict):
        self.values = values
        super().__init__(
            model_function=model_function
        )

    def impute(self, feature_subset: list, x_i: dict, n_samples: int = 1):
        sampled_values = {feature: self.values[feature] for feature in feature_subset}
        prediction = self.model_function({**x_i, **sampled_values})
        prediction = [prediction for _ in range(n_samples)]
        return prediction
