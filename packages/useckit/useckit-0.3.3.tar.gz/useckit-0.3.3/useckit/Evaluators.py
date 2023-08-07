from abc import ABC, abstractmethod

from useckit.paradigms.distance_learning.prediction_models.contrastive_loss.contrastive_keras_prediction_model import \
    ContrastiveKerasPredictionModel
from useckit.paradigms.distance_learning.prediction_models.online_triplet_loss.online_triplet_keras_prediction_model import \
    OnlineTripletKerasPredictionModel
from useckit.paradigms.time_series_classification.tsc_paradigm import TSCParadigm
from useckit.paradigms.time_series_classification.prediction_models.classification_keras_prediction_model \
    import ClassificationKerasPredictionModel
from useckit.paradigms.time_series_classification.prediction_models.keras_model_descriptions import \
    dl4tsc_mlp, dl4tsc_fcn, dl4tsc_resnet, dl4tsc_encoder, dl4tsc_cnn_padding_valid, dl4tsc_cnn_padding_same
from useckit.paradigms.time_series_classification.prediction_models.mcnn import dl4tsc_mcnn
from useckit.paradigms.time_series_classification.prediction_models.tlenet import dl4tsc_tlenet
from useckit.paradigms.time_series_classification.prediction_models.twiesn import dl4tsc_twiesn
from useckit.paradigms.time_series_classification.prediction_models.inception import dl4tsc_inception
from useckit.paradigms.time_series_classification.prediction_models.mcdcnn import dl4tsc_mcdcnn
from useckit.util.dataset import Dataset


class Evaluator(ABC):
    def __init__(self, dataset: Dataset, epochs: int = None, verbose: bool = False):
        if isinstance(dataset, Dataset):
            self.dataset = dataset
        else:
            raise ValueError("Provided dataset must have type 'Dataset'.")
        self.epochs = epochs
        self.verbose = verbose

    @abstractmethod
    def evaluate(self):
        pass


class AutoEvaluator(Evaluator):
    def __init__(self, dataset: Dataset, epochs: int = None, verbose: bool = False):
        super().__init__(dataset, epochs=epochs, verbose=verbose)
        self.tsc_evaluator = TSCEvaluator(dataset, epochs=epochs, verbose=verbose)
        self.distance_learning_evaluator = DistanceLearningEvaluator(dataset, epochs=epochs, verbose=verbose)
        self.anomaly_detection_evaluator = AnomalyDetectionEvaluator(dataset, epochs=epochs, verbose=verbose)

    def evaluate(self):
        self.tsc_evaluator.evaluate()
        self.distance_learning_evaluator.evaluate()
        self.anomaly_detection_evaluator.evaluate()


class TSCEvaluator(Evaluator):
    def __init__(self, dataset: Dataset, epochs: int = None, verbose: bool = False,
                 enable_mlp: bool = True,
                 enable_fcn: bool = True,
                 enable_resnet: bool = True,
                 enable_encoder: bool = True,
                 enable_cnn_valid: bool = True,
                 enable_cnn_same: bool = True,
                 enable_mcnn: bool = True,
                 enable_tlenet: bool = True,
                 enable_twiesn: bool = True,
                 enable_inception: bool = True,
                 enable_mcdcnn: bool = True):
        super().__init__(dataset, epochs=epochs, verbose=verbose)
        self.enable_mlp = enable_mlp
        self.enable_fcn = enable_fcn
        self.enable_resnet = enable_resnet
        self.enable_encoder = enable_encoder
        self.enable_cnn_valid = enable_cnn_valid
        self.enable_cnn_same = enable_cnn_same
        self.enable_mcnn = enable_mcnn
        self.enable_tlenet = enable_tlenet
        self.enable_twiesn = enable_twiesn
        self.enable_inception = enable_inception
        self.enable_mcdcnn = enable_mcdcnn

    def evaluate(self):
        if self.enable_mlp:
            TSCParadigm(
                prediction_model=ClassificationKerasPredictionModel(verbose=self.verbose, nb_epochs=self.epochs,
                                                                    model_description=dl4tsc_mlp),
                verbose=True).evaluate(self.dataset)

        if self.enable_fcn:
            TSCParadigm(
                prediction_model=ClassificationKerasPredictionModel(verbose=self.verbose, nb_epochs=self.epochs,
                                                                    model_description=dl4tsc_fcn),
                verbose=True).evaluate(self.dataset)

        if self.enable_resnet:
            TSCParadigm(
                prediction_model=ClassificationKerasPredictionModel(verbose=self.verbose, nb_epochs=self.epochs,
                                                                    model_description=dl4tsc_resnet),
                verbose=True).evaluate(self.dataset)

        if self.enable_encoder:
            TSCParadigm(
                prediction_model=ClassificationKerasPredictionModel(verbose=self.verbose, nb_epochs=self.epochs,
                                                                    model_description=dl4tsc_encoder),
                verbose=True).evaluate(self.dataset)

        if self.enable_cnn_valid:
            TSCParadigm(
                prediction_model=ClassificationKerasPredictionModel(verbose=self.verbose, nb_epochs=self.epochs,
                                                                    model_description=dl4tsc_cnn_padding_valid),
                verbose=True).evaluate(self.dataset)

        if self.enable_cnn_same:
            TSCParadigm(
                prediction_model=ClassificationKerasPredictionModel(verbose=self.verbose, nb_epochs=self.epochs,
                                                                    model_description=dl4tsc_cnn_padding_same),
                verbose=True).evaluate(self.dataset)

        if self.enable_mcnn:
            TSCParadigm(
                prediction_model=dl4tsc_mcnn(nb_classes=self.dataset.amount_classes(),
                                             verbose=self.verbose, nb_epochs=self.epochs),
                verbose=True).evaluate(self.dataset)

        if self.enable_tlenet:
            TSCParadigm(
                prediction_model=dl4tsc_tlenet(verbose=self.verbose, nb_epochs=self.epochs),
                verbose=True).evaluate(self.dataset)

        if self.enable_twiesn:
            TSCParadigm(
                prediction_model=dl4tsc_twiesn(),
                verbose=True).evaluate(self.dataset)

        if self.enable_inception:
            TSCParadigm(
                prediction_model=dl4tsc_inception(verbose=self.verbose, nb_epochs=self.epochs),
                verbose=True).evaluate(self.dataset)

        if self.enable_mcdcnn:
            TSCParadigm(
                prediction_model=dl4tsc_mcdcnn(verbose=self.verbose, nb_epochs=self.epochs),
                verbose=True).evaluate(self.dataset)


class DistanceLearningEvaluator(Evaluator):
    def __init__(self, dataset: Dataset, epochs: int = None, verbose: bool = False):
        super().__init__(dataset, epochs=epochs, verbose=verbose)

    def evaluate(self):
        from useckit.paradigms.distance_learning.distance_paradigm import DistanceMetricParadigm

        dmp_contrastive = DistanceMetricParadigm(verbose=self.verbose,
                                                 prediction_model=ContrastiveKerasPredictionModel(nb_epochs=self.epochs))
        dmp_contrastive.evaluate(self.dataset)

        dmp_triplet = DistanceMetricParadigm(verbose=self.verbose,
                                             prediction_model=OnlineTripletKerasPredictionModel(nb_epochs=self.epochs))
        dmp_triplet.evaluate(self.dataset)


class AnomalyDetectionEvaluator(Evaluator):
    def __init__(self, dataset: Dataset, epochs: int = None, verbose: bool = False):
        super().__init__(dataset, epochs=epochs, verbose=verbose)

    def evaluate(self):
        from useckit.paradigms.anomaly_detection.anomaly_paradigm import AnomalyParadigm

        adp = AnomalyParadigm(verbose=self.verbose)
        adp.evaluate(self.dataset)
