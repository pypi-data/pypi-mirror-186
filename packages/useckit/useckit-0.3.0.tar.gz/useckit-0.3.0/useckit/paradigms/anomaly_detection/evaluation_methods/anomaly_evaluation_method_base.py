from abc import abstractmethod, ABC

import numpy as np

from ..prediction_models.anomaly_prediction_model_base import AnomalyBasePredictionModel
from ..._paradigm_base import EvaluationMethodBase
from ....util.dataset import Dataset


class BaseThresholdingMethod(ABC):

    # One threshold for each user the anomaly model was trained on
    @abstractmethod
    def compute_thresholds(self, enrollment_data: np.ndarray, enrollment_labels: np.ndarray) -> [float]:
        pass


class AnomalyBaseEvaluationMethod(EvaluationMethodBase):

    @abstractmethod
    def evaluate(self, dataset: Dataset, prediction_model: AnomalyBasePredictionModel, **kwargs):
        pass
