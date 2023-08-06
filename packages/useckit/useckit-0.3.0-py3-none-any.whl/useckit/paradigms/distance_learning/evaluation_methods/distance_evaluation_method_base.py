from abc import abstractmethod, ABC

import numpy as np

from ..prediction_models.distance_prediction_model_base import DistanceBasePredictionModel
from ..._paradigm_base import EvaluationMethodBase
from ....util.dataset import Dataset


class BaseThresholdingMethod(ABC):

    @abstractmethod
    def compute_threshold(self, enrollment_data: np.ndarray, enrollment_labels: np.ndarray) -> float:
        pass


class DistanceBaseEvaluationMethod(EvaluationMethodBase):

    @abstractmethod
    def evaluate(self, dataset: Dataset, prediction_model: DistanceBasePredictionModel, **kwargs):
        pass
