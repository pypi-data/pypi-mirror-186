import numpy as np

from ._equal_error_thresholding_method import EqualErrorThresholding
from .distance_evaluation_method_base import DistanceBaseEvaluationMethod, BaseThresholdingMethod
from ..prediction_models.distance_prediction_model_base import DistanceBasePredictionModel
from ....evaluation.identification_with_reject import IdentificationOrRejectModel, \
    perform_identification_or_reject_evaluation
from ....util.dataset import Dataset
from ....util.utils import contrastive_make_pairs


class DistanceIdentificationOrRejectModel(IdentificationOrRejectModel):

    def __init__(self,
                 distance_metric: DistanceBasePredictionModel,
                 enrollment_samples: np.ndarray,
                 enrollment_labels: np.ndarray,
                 rejection_threshold: float,
                 dataset: Dataset):
        self.distance_metric = distance_metric
        self.enrollment_samples = enrollment_samples
        self.enrollment_labels = enrollment_labels
        self.rejection_threshold = rejection_threshold
        self.dataset = dataset

    def identify_or_reject(self, samples: np.ndarray):
        result = np.zeros(shape=(len(samples),), dtype=int)
        for index, sample in enumerate(samples):
            sample_broadcast = np.broadcast_to(sample, shape=self.enrollment_samples.shape)
            distances_to_enrollment = self.distance_metric.predict(sample_broadcast, self.enrollment_samples)
            min_dist_index = np.argmin(distances_to_enrollment)
            if distances_to_enrollment[min_dist_index] >= self.rejection_threshold:
                result[index] = -1
            else:
                result[index] = self.enrollment_labels[min_dist_index]
        return self.dataset.reverse_label_transform(result)


class IdentificationWithReject(DistanceBaseEvaluationMethod):

    def __init__(self,
                 output_dir: str = "evaluation_identification_with_reject",
                 threshold_method: BaseThresholdingMethod = None):
        super().__init__(output_dir)
        self.threshold_method = threshold_method

    def evaluate(self, dataset: Dataset, prediction_model: DistanceBasePredictionModel, **kwargs):
        if self.threshold_method is None:
            self.threshold_method = EqualErrorThresholding(prediction_model, contrastive_make_pairs, self.output_dir)

        threshold = self.threshold_method.compute_threshold(dataset.testset_enrollment_data,
                                                            dataset.testset_enrollment_labels)
        ident_or_reject_model = DistanceIdentificationOrRejectModel(prediction_model,
                                                                    dataset.testset_enrollment_data,
                                                                    dataset.testset_enrollment_labels,
                                                                    threshold,
                                                                    dataset)
        perform_identification_or_reject_evaluation(ident_or_reject_model, dataset, self.output_dir)
