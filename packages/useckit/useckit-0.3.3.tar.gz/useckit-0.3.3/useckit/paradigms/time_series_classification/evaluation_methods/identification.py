import numpy as np

from .tsc_evaluation_method_base import TSCBaseEvaluationMethod
from ..prediction_models.tsc_prediction_model_base import TSCBasePredictionModel
from ....evaluation.identification import IdentificationModel, perform_identification_evaluation
from ....util.dataset import Dataset


class TSCIdentificationModel(IdentificationModel):

    def __init__(self, dataset: Dataset, prediction_model: TSCBasePredictionModel):
        self.dataset = dataset
        self.prediction_model = prediction_model

    def identify(self, samples: np.ndarray) -> int:
        x_train, x_val, y_train, y_val, y_true, input_shape, nb_classes = \
            self.prediction_model.convert_dataset_to_legacy_values(self.dataset)
        x_test = samples
        y_pred = self.prediction_model.predict(x_test, y_true, x_train, y_train, y_val, return_df_metrics=False)
        return self.dataset.reverse_label_transform(y_pred)


class IdentificationOnly(TSCBaseEvaluationMethod):

    def __init__(self, output_dir: str = "evaluation_identification"):
        super().__init__(output_dir)

    def evaluate(self, dataset: Dataset, prediction_model: TSCBasePredictionModel, **kwargs):
        perform_identification_evaluation(TSCIdentificationModel(dataset, prediction_model), dataset,
                                          self.output_dir)
