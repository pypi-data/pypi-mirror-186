from .evaluation_methods.anomaly_evaluation_method_base import AnomalyBaseEvaluationMethod
from .evaluation_methods.identification import IdentificationOnly
from .prediction_models.anomaly_prediction_model_base import AnomalyBasePredictionModel
from .prediction_models.auto_encoder_keras_prediction_model import AutoEncoderKerasPredictionModel
from .._paradigm_base import ParadigmBase, PredictionModelBase
from ...util.dataset import Dataset


class AnomalyParadigm(ParadigmBase):

    def __init__(self, name: str = None,
                 output_dir: str = None,
                 prediction_model: AnomalyBasePredictionModel = None,
                 evaluation_methods: [AnomalyBaseEvaluationMethod] = None,
                 verbose: bool = True,
                 seed=42,
                 ):
        # This looks really stupid, but if the default value is initiated in the method head, not in the call to the
        # super constructor as blow, python will only instantiate one object for all calls to this method, hence
        # causing different paradigms to share the same instances of prediction model or evaluation method.
        # For more information see:
        # https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
        super().__init__(prediction_model=AutoEncoderKerasPredictionModel() if prediction_model is None else prediction_model,
                         name=name,
                         output_dir=output_dir,
                         evaluation_methods=
                         [IdentificationOnly()] if evaluation_methods is None else evaluation_methods,
                         verbose=verbose,
                         seed=seed)

    def restore_prediction_model_trainables(self,
                                            anomaly_paradigm_prediction_model_directory_path_like: str,
                                            dataset: Dataset,
                                            individual_models_file_name_path_like: str = 'best_model.hdf5') \
            -> PredictionModelBase:
        self.prediction_model.restore_model_trainables(anomaly_paradigm_prediction_model_directory_path_like,
                                                       dataset=dataset,
                                                       path_like_individual_models_file_name=
                                                       individual_models_file_name_path_like)
        return self.prediction_model
