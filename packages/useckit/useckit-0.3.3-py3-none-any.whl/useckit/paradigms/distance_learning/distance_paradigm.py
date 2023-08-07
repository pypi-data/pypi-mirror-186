from useckit.util.dataset import Dataset
from .evaluation_methods.distance_evaluation_method_base import DistanceBaseEvaluationMethod
from .evaluation_methods.identification import IdentificationOnly
from .prediction_models.distance_prediction_model_base import DistanceBasePredictionModel
from useckit.paradigms.distance_learning.prediction_models.contrastive_loss.contrastive_keras_prediction_model import ContrastiveKerasPredictionModel
from .._paradigm_base import ParadigmBase, PredictionModelBase


class DistanceMetricParadigm(ParadigmBase):

    def __init__(self, name: str = None,
                 output_dir: str = None,
                 prediction_model: DistanceBasePredictionModel = None,
                 evaluation_methods: [DistanceBaseEvaluationMethod] = None,
                 verbose: bool = True,
                 seed=42):
        # This looks really stupid, but if the default value is initiated in the method head, not in the call to the
        # super constructor as blow, python will only instantiate one object for all calls to this method, hence
        # causing different paradigms to share the same instances of prediction model or evaluation method.
        # For more information see:
        # https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
        super().__init__(
            prediction_model=ContrastiveKerasPredictionModel() if prediction_model is None else prediction_model,
            name=name,
            output_dir=output_dir,
            evaluation_methods=
            [IdentificationOnly()] if evaluation_methods is None else evaluation_methods,
            verbose=verbose, seed=seed)

    def restore_prediction_model_trainables(self,
                                            saved_weights_path_like: str,
                                            dataset: Dataset) -> PredictionModelBase:
        if dataset is None:
            raise ValueError(
                "The dataset argument may not be None, as the method uses it to infer the size of the " +
                "restored model's first layer. " +
                "Note that the total amount of unique labels within dataset needs to match the total amount of " +
                "labels in the dataset that the model was trained on.")
        self.prediction_model.restore_model_trainables(saved_weights_path_like, dataset=dataset)
        return self.prediction_model
