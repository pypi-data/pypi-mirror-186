from .tsc_evaluation_method_base import TSCBaseEvaluationMethod
from ..prediction_models.tsc_prediction_model_base import TSCBasePredictionModel
from ....util.dataset import Dataset
from ....util.plotting import do_cm
from ....util.utils import create_window_slices


class LegacyIdentificationOnly(TSCBaseEvaluationMethod):

    def __init__(self, output_dir: str = "evaluation_identification_legacy", perform_windowslicing: bool = False,
                 window_stride: int = None, window_size: int = None, shuffle_window_slices: bool = False):
        super().__init__(output_dir)
        self.perform_windowslicing = perform_windowslicing
        self.window_stride = window_stride
        self.window_size = window_size
        self.shuffle_window_slices = shuffle_window_slices

    def evaluate(self, dataset: Dataset, prediction_model: TSCBasePredictionModel, **kwargs):
        _, _, _, y_test = dataset.view_one_hot_encoded_labels()
        if self.perform_windowslicing:
            x_test, y_test, _ = create_window_slices(dataset.testset_enrollment_data,
                                                     y_test,
                                                     self.window_stride,
                                                     self.window_size,
                                                     shuffle=self.shuffle_window_slices)

            do_cm(x_test, y_test, prediction_model, self.output_dir)
            do_cm(x_test, y_test, prediction_model, self.output_dir, perform_per_sample_majority_vote=True)
        else:  # no window slicing here
            x_test = dataset.testset_enrollment_data
            do_cm(x_test, y_test, prediction_model, self.output_dir)
