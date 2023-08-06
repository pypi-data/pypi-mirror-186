import numpy as np

from .anomaly_evaluation_method_base import AnomalyBaseEvaluationMethod
from ..prediction_models.anomaly_prediction_model_base import AnomalyBasePredictionModel
from ....evaluation.identification import IdentificationModel, perform_identification_evaluation
from ....util.dataset import Dataset


class AnomalyIdentificationModel(IdentificationModel):

    def __init__(self,
                 anomaly_prediction_model: AnomalyBasePredictionModel,
                 dataset: Dataset):
        self.anomaly_prediction_model = anomaly_prediction_model
        self.dataset = dataset

    def identify(self, samples: np.ndarray) -> np.ndarray:
        preds = self.anomaly_prediction_model.predict(samples)
        preds = preds.transpose()  # 0-axis = samples, 1-axis = the predictions of the different models for the sample
        preds = np.argmin(preds, axis=1)  # reduce to the indices of the model with the minimum prediction
        return self.dataset.reverse_label_transform(preds)


class IdentificationOnly(AnomalyBaseEvaluationMethod):

    def __init__(self,
                 output_dir: str = "evaluation_identification"):
        super().__init__(output_dir)

    def evaluate(self, dataset: Dataset, prediction_model: AnomalyBasePredictionModel, **kwargs):
        identification_model = AnomalyIdentificationModel(prediction_model, dataset)
        perform_identification_evaluation(identification_model, dataset, self.output_dir)
