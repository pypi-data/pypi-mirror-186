from abc import abstractmethod

from ..prediction_models.tsc_prediction_model_base import TSCBasePredictionModel
from ..._paradigm_base import EvaluationMethodBase
from ....util.dataset import Dataset


class TSCBaseEvaluationMethod(EvaluationMethodBase):

    @abstractmethod
    def evaluate(self, dataset: Dataset, prediction_model: TSCBasePredictionModel, **kwargs):
        pass
