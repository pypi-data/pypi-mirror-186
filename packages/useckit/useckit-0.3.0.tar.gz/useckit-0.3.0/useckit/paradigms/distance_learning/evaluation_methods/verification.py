import numpy as np

from ._equal_error_thresholding_method import EqualErrorThresholding
from .distance_evaluation_method_base import DistanceBaseEvaluationMethod, BaseThresholdingMethod
from ..prediction_models.distance_prediction_model_base import DistanceBasePredictionModel
from ....evaluation.verification import VerificationModel, perform_verification_evaluation
from ....util.dataset import Dataset
from ....util.utils import contrastive_make_pairs


class DistanceVerificationModel(VerificationModel):

    def __init__(self,
                 distance_metric: DistanceBasePredictionModel,
                 enrollment_samples: np.ndarray,
                 enrollment_labels: np.ndarray,
                 rejection_threshold: float):
        self.distance_metric = distance_metric
        self.enrollment_samples = enrollment_samples
        self.enrollment_labels = enrollment_labels
        self.rejection_threshold = rejection_threshold

    def verify(self, samples: np.ndarray, identity_claims: np.ndarray) -> bool:
        result = np.zeros(shape=(len(samples),))
        for index, sample in enumerate(samples):
            i_claim = identity_claims[index]  # identity belonging to the one sample
            i_enrollment_samples = self.enrollment_samples[self.enrollment_labels == i_claim]  # all enrollment
            # samples of the claimed identity
            if len(i_enrollment_samples) <= 0:
                raise ValueError(f"Claimed identity {identity_claims[index]} was not part of the enrolled "
                                 f"identities {self.enrollment_labels}!")

            sample_broadcast = np.broadcast_to(sample, shape=i_enrollment_samples.shape)
            distances_to_enrollment = self.distance_metric.predict(sample_broadcast, i_enrollment_samples)

            for d in distances_to_enrollment:
                if d <= self.rejection_threshold:  # else the result remains as zero
                    result[index] = 1
                    break
        return result == 1  # dirty transform to bool array


class Verification(DistanceBaseEvaluationMethod):

    def __init__(self,
                 output_dir: str = "evaluation_verification",
                 threshold_method: BaseThresholdingMethod = None):
        super().__init__(output_dir)
        self.threshold_method = threshold_method

    def evaluate(self, dataset: Dataset, prediction_model: DistanceBasePredictionModel, **kwargs):
        if self.threshold_method is None:
            self.threshold_method = EqualErrorThresholding(prediction_model, contrastive_make_pairs, self.output_dir)

        threshold = self.threshold_method.compute_threshold(dataset.testset_enrollment_data,
                                                            dataset.testset_enrollment_labels)
        verification_model = DistanceVerificationModel(prediction_model,
                                                       dataset.testset_enrollment_data,
                                                       dataset.testset_enrollment_labels,
                                                       threshold)
        perform_verification_evaluation(verification_model, dataset, self.output_dir)
