import numpy as np

from ._fixed_false_negative_thresholding_method import FixedFalseNegativeThresholdingMethod
from .anomaly_evaluation_method_base import AnomalyBaseEvaluationMethod, BaseThresholdingMethod
from ..prediction_models.anomaly_prediction_model_base import AnomalyBasePredictionModel
from ....evaluation.verification import VerificationModel, perform_verification_evaluation
from ....util.dataset import Dataset


class AnomalyVerificationModel(VerificationModel):

    def __init__(self,
                 anomaly_prediction_model: AnomalyBasePredictionModel,
                 rejection_thresholds_per_trained_user: [float]):
        self.anomaly_prediction_model = anomaly_prediction_model
        self.rejection_thresholds_per_trained_user = rejection_thresholds_per_trained_user

    def verify(self, samples: np.ndarray, identity_claims: np.ndarray) -> np.ndarray:
        preds = self.anomaly_prediction_model.predict(samples)
        preds = preds.transpose()  # 0-axis = samples, 1-axis = the predictions of the different models for the sample
        result = np.zeros(shape=identity_claims.shape)
        for i in range(len(identity_claims)):
            reject = preds[i][identity_claims[i]] >= self.rejection_thresholds_per_trained_user[identity_claims[i]]
            if reject:
                result[i] = 0
            else:
                result[i] = 1
        return result == 1  # dirty transform to bool array


class Verification(AnomalyBaseEvaluationMethod):

    def __init__(self,
                 output_dir: str = "evaluation_verification",
                 threshold_method: BaseThresholdingMethod = None):
        super().__init__(output_dir)
        self.threshold_method = threshold_method

    def evaluate(self, dataset: Dataset, prediction_model: AnomalyBasePredictionModel, **kwargs):
        if self.threshold_method is None:
            self.threshold_method = FixedFalseNegativeThresholdingMethod(prediction_model, self.output_dir)
        thresholds = self.threshold_method.compute_thresholds(dataset.testset_enrollment_data,
                                                              dataset.testset_enrollment_labels)
        verification_model = AnomalyVerificationModel(prediction_model, thresholds)
        perform_verification_evaluation(verification_model, dataset, self.output_dir)
