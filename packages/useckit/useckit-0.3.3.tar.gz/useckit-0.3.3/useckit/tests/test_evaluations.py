import os
import sys
import unittest

from useckit.paradigms.anomaly_detection.anomaly_paradigm import AnomalyParadigm
from useckit.paradigms.anomaly_detection.evaluation_methods.identification import \
    IdentificationOnly as AnomalyIdentification
from useckit.paradigms.anomaly_detection.evaluation_methods.identification_with_reject import \
    IdentificationWithReject as AnomalyIdentificationWithReject
from useckit.paradigms.anomaly_detection.evaluation_methods.verification import \
    Verification as AnomalyVerification
from useckit.paradigms.anomaly_detection.prediction_models.auto_encoder_keras_prediction_model import \
    AutoEncoderKerasPredictionModel
from useckit.paradigms.distance_learning.distance_paradigm import DistanceMetricParadigm
from useckit.paradigms.distance_learning.evaluation_methods.identification import \
    IdentificationOnly as DistanceIdentification
from useckit.paradigms.distance_learning.evaluation_methods.identification_with_reject import \
    IdentificationWithReject as DistanceIdentificationWithReject
from useckit.paradigms.distance_learning.evaluation_methods.verification import \
    Verification as DistanceVerification
from useckit.paradigms.distance_learning.prediction_models.contrastive_loss.contrastive_keras_prediction_model import \
    ContrastiveKerasPredictionModel
from useckit.paradigms.time_series_classification.evaluation_methods.identification import \
    IdentificationOnly as TSCIdentification
from useckit.paradigms.time_series_classification.prediction_models.classification_keras_prediction_model import \
    ClassificationKerasPredictionModel
from useckit.paradigms.time_series_classification.prediction_models.keras_model_descriptions import *
from useckit.paradigms.time_series_classification.tsc_paradigm import TSCParadigm
from useckit.util.dataset import Dataset
from useckit.util.utils import make_some_intelligent_noise

# resolves issues with gitlab runner
sys.setrecursionlimit(10000)
# disable gpu training for unittests
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


class TestUseckit(unittest.TestCase):

    @staticmethod
    def make_dataset(*args, **kwargs):
        x_train, y_train = make_some_intelligent_noise(*args, **kwargs)
        x_val, y_val = make_some_intelligent_noise(*args, **kwargs)
        x_test_enroll, y_test_enroll = make_some_intelligent_noise(*args, **kwargs)
        if 'labels' in kwargs:
            kwargs['labels'] += 3
        else:
            kwargs['labels'] = 7
        x_test_match, y_test_match = make_some_intelligent_noise(*args, **kwargs)
        return Dataset(x_train, y_train, x_val, y_val, x_test_enroll, y_test_enroll, x_test_match, y_test_match)

    def test_anomaly_prediction(self):
        data = TestUseckit.make_dataset(shape=(16, 10, 10))
        encoder = AnomalyParadigm(verbose=True, prediction_model=AutoEncoderKerasPredictionModel(nb_epochs=2),
                                  evaluation_methods=[AnomalyVerification(), AnomalyIdentification(),
                                                      AnomalyIdentificationWithReject()])
        encoder.evaluate(data)

    def test_time_series_classification(self):
        data = TestUseckit.make_dataset(shape=(16, 20, 20, 4))
        tsc = TSCParadigm(
            prediction_model=ClassificationKerasPredictionModel(verbose=True, nb_epochs=10,
                                                                model_description=dl4tsc_mlp),
            verbose=True, evaluation_methods=[TSCIdentification()])
        tsc.evaluate(data)

    def test_distance_metric(self):
        data = TestUseckit.make_dataset(shape=(16, 20, 20, 4))
        siamese = DistanceMetricParadigm(verbose=True, prediction_model=ContrastiveKerasPredictionModel(nb_epochs=10),
                                         evaluation_methods=[DistanceVerification(), DistanceIdentification(),
                                                             DistanceIdentificationWithReject()])
        siamese.evaluate(data)


if __name__ == '__main__':
    unittest.main()
