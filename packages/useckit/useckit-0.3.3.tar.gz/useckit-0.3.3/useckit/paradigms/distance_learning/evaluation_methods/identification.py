import numpy as np

from .distance_evaluation_method_base import DistanceBaseEvaluationMethod
from ..prediction_models.distance_prediction_model_base import DistanceBasePredictionModel
from ....evaluation.identification import IdentificationModel, perform_identification_evaluation
from ....util.dataset import Dataset


class DistanceIdentificationModel(IdentificationModel):

    def __init__(self,
                 distance_metric: DistanceBasePredictionModel,
                 enrollment_samples: np.ndarray,
                 enrollment_labels: np.ndarray,
                 dataset: Dataset):
        self.distance_metric = distance_metric
        self.enrollment_samples = enrollment_samples
        self.enrollment_labels = enrollment_labels
        self.dataset = dataset

    def identify(self, samples: np.ndarray):
        result = np.zeros(shape=(len(samples),), dtype=int)
        for index, sample in enumerate(samples):
            sample_broadcast = np.broadcast_to(sample, shape=self.enrollment_samples.shape)
            distances_to_enrollment = self.distance_metric.predict(sample_broadcast, self.enrollment_samples)
            min_dist_index = np.argmin(distances_to_enrollment)
            result[index] = self.enrollment_labels[min_dist_index]
        return self.dataset.reverse_label_transform(result)


class IdentificationOnly(DistanceBaseEvaluationMethod):

    def __init__(self,
                 output_dir: str = "evaluation_identification"):
        super().__init__(output_dir)

    def evaluate(self, dataset: Dataset, prediction_model: DistanceBasePredictionModel, **kwargs):
        perform_identification_evaluation(DistanceIdentificationModel(prediction_model,
                                                                      dataset.testset_enrollment_data,    # FIXME
                                                                      dataset.testset_enrollment_labels,  # FIXME
                                                                      dataset),
                                          dataset,
                                          self.output_dir)
