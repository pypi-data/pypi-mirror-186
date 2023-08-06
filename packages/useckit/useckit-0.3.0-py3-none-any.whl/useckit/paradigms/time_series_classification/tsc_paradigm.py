from .evaluation_methods.identification import IdentificationOnly
from .evaluation_methods.tsc_evaluation_method_base import TSCBaseEvaluationMethod
from .prediction_models.classification_keras_prediction_model import ClassificationKerasPredictionModel
from .prediction_models.tsc_prediction_model_base import TSCBasePredictionModel
from .._paradigm_base import ParadigmBase, PredictionModelBase
from ...util.dataset import Dataset


class TSCParadigm(ParadigmBase):

    def __init__(self, name: str = None,
                 output_dir: str = None,
                 prediction_model: TSCBasePredictionModel = None,
                 evaluation_methods: [TSCBaseEvaluationMethod] = None,
                 seed=42,
                 verbose=True,
                 disable_normalization_check=False,
                 class_weights=None
                 ):
        # This looks really stupid, but if the default value is initiated in the method head, not in the call to the
        # super constructor as blow, python will only instantiate one object for all calls to this method, hence
        # causing different paradigms to share the same instances of prediction model or evaluation method.
        # For more information see:
        # https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
        super().__init__(
            prediction_model=ClassificationKerasPredictionModel() if prediction_model is None else prediction_model,
            name=name, output_dir=output_dir,
            evaluation_methods=
            [IdentificationOnly()] if evaluation_methods is None else evaluation_methods,
            seed=seed,
            verbose=verbose)
        self.disable_normalization_check = disable_normalization_check
        self.seed = seed
        self.prediction_model = prediction_model

        if class_weights is not None:
            assert isinstance(class_weights, dict), 'class_weights must be a dict. See: https://bit.ly/3ljOI9c'
        self.class_weights = class_weights

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
