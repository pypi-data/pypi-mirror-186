from typing import Callable, Tuple

import numpy as np

from ._equal_error_thresholding_method import EqualErrorThresholding
from .distance_evaluation_method_base import DistanceBaseEvaluationMethod
from ..prediction_models.distance_prediction_model_base import DistanceBasePredictionModel
from ....util.dataset import Dataset
from ....util.utils import contrastive_make_pairs


class PairwiseAccuracy(DistanceBaseEvaluationMethod):

    def __init__(self,
                 output_dir: str = "evaluation_pairwise",
                 pair_function: Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]] =
                 contrastive_make_pairs):
        super().__init__(output_dir)
        self.pair_function = pair_function

    def evaluate(self, dataset: Dataset, prediction_model: DistanceBasePredictionModel, **kwargs):
        thresholding_method = EqualErrorThresholding(prediction_model, self.pair_function, self.output_dir)
        thresholding_method.compute_threshold(dataset.testset_matching_data, dataset.testset_matching_labels)
