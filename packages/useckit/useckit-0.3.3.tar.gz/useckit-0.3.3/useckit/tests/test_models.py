import os
import sys
import unittest

from useckit.paradigms.anomaly_detection.anomaly_paradigm import AnomalyParadigm
from useckit.paradigms.distance_learning.distance_paradigm import DistanceMetricParadigm
from useckit.paradigms.distance_learning.prediction_models.online_triplet_loss.online_triplet_keras_prediction_model import \
    OnlineTripletKerasPredictionModel
from useckit.paradigms.time_series_classification.prediction_models.classification_keras_prediction_model import \
    ClassificationKerasPredictionModel
from useckit.paradigms.time_series_classification.prediction_models.inception import dl4tsc_inception
from useckit.paradigms.time_series_classification.prediction_models.keras_model_descriptions import *
from useckit.paradigms.time_series_classification.prediction_models.mcdcnn import dl4tsc_mcdcnn
from useckit.paradigms.time_series_classification.prediction_models.mcnn import dl4tsc_mcnn
from useckit.paradigms.time_series_classification.prediction_models.tlenet import dl4tsc_tlenet
from useckit.paradigms.time_series_classification.prediction_models.twiesn import dl4tsc_twiesn
from useckit.paradigms.time_series_classification.tsc_paradigm import TSCParadigm
from useckit.tests.test_utils import make_some_intelligent_noise
from useckit.util.dataset import Dataset
from useckit.util.utils import triplet_make_pairs_random
from useckit.paradigms.distance_learning.prediction_models.offline_triplet_loss.offline_triplet_keras_prediction_model import \
    TripletKerasPredictionModel

# resolves issues with gitlab runner
sys.setrecursionlimit(10000)
# disable gpu training for unittests
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


class TestUseckit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        x_train, y_train = make_some_intelligent_noise()
        x_val, y_val = make_some_intelligent_noise()
        x_enroll, y_enroll = make_some_intelligent_noise()
        x_test, y_test = make_some_intelligent_noise()
        self.data = Dataset(x_train, y_train, x_val, y_val, x_enroll, y_enroll, x_test, y_test)

    def test_tsc_mlp(self):
        keras_mlp = TSCParadigm(
            prediction_model=ClassificationKerasPredictionModel(verbose=True, nb_epochs=2,
                                                                model_description=dl4tsc_mlp),
            verbose=True)
        keras_mlp.evaluate(self.data)

    def test_tsc_fcn(self):
        keras_fcn = TSCParadigm(
            prediction_model=ClassificationKerasPredictionModel(verbose=True, nb_epochs=2,
                                                                model_description=dl4tsc_fcn),
            verbose=True)
        keras_fcn.evaluate(self.data)

    def test_tsc_resnet(self):
        keras_resnet = TSCParadigm(
            prediction_model=ClassificationKerasPredictionModel(verbose=True, nb_epochs=2,
                                                                model_description=dl4tsc_resnet),
            verbose=True)
        keras_resnet.evaluate(self.data)

    def test_tsc_encoder(self):
        keras_encoder = TSCParadigm(
            prediction_model=ClassificationKerasPredictionModel(verbose=True, nb_epochs=2,
                                                                model_description=dl4tsc_encoder),
            verbose=True)
        keras_encoder.evaluate(self.data)

    def test_tsc_cnn_padding_valid(self):
        keras_cnn_valid = TSCParadigm(
            prediction_model=ClassificationKerasPredictionModel(verbose=True, nb_epochs=2,
                                                                model_description=dl4tsc_cnn_padding_valid),
            verbose=True)
        keras_cnn_valid.evaluate(self.data)

    def test_tsc_padding_same(self):
        keras_cnn_same = TSCParadigm(
            prediction_model=ClassificationKerasPredictionModel(verbose=True, nb_epochs=2,
                                                                model_description=dl4tsc_cnn_padding_same),
            verbose=True)
        keras_cnn_same.evaluate(self.data)

    def test_tsc_mcnn(self):
        mcnn = TSCParadigm(
            prediction_model=dl4tsc_mcnn(nb_classes=self.data.amount_classes(), verbose=True, nb_epochs=2),
            verbose=True)
        mcnn.evaluate(self.data)

    def test_tsc_tlenet(self):
        tlenet = TSCParadigm(
            prediction_model=dl4tsc_tlenet(verbose=True, nb_epochs=2),
            verbose=True)
        tlenet.evaluate(self.data)

    def test_tsc_twiesn(self):
        twiesn = TSCParadigm(
            prediction_model=dl4tsc_twiesn(),
            verbose=True)
        twiesn.evaluate(self.data)

    def test_tsc_inception(self):
        inception = TSCParadigm(
            prediction_model=dl4tsc_inception(verbose=True, nb_epochs=2),
            verbose=True)
        inception.evaluate(self.data)

    def test_tsc_mcdcnn(self):
        mcdcnn = TSCParadigm(
            prediction_model=dl4tsc_mcdcnn(verbose=True, nb_epochs=2),
            verbose=True)
        mcdcnn.evaluate(self.data)

    def test_siamese_contrastive_loss(self):
        from useckit.paradigms.distance_learning.prediction_models.contrastive_loss.contrastive_keras_prediction_model \
            import ContrastiveKerasPredictionModel
        x_train, y_train = make_some_intelligent_noise(shape=(20, 64, 64, 4))
        x_val, y_val = make_some_intelligent_noise(shape=(20, 64, 64, 4))
        x_enroll, y_enroll = make_some_intelligent_noise(shape=(20, 64, 64, 4))
        x_test, y_test = make_some_intelligent_noise(shape=(20, 64, 64, 4))
        self.data = Dataset(x_train, y_train, x_val, y_val, x_enroll, y_enroll, x_test, y_test)

        dmp = DistanceMetricParadigm(prediction_model=ContrastiveKerasPredictionModel(nb_epochs=2), verbose=True)
        dmp.evaluate(self.data)

    def test_siamese_triplet_loss_offline(self):
        shape = (100, 200, 12)
        x_train, y_train = make_some_intelligent_noise(shape=shape)
        x_val, y_val = make_some_intelligent_noise(shape=shape)
        x_enroll, y_enroll = make_some_intelligent_noise(shape=shape)
        x_test, y_test = make_some_intelligent_noise(shape=shape)
        data = Dataset(x_train, y_train, x_val, y_val, x_enroll, y_enroll, x_test, y_test)

        dmp = DistanceMetricParadigm(verbose=True,
                                     prediction_model=TripletKerasPredictionModel(verbose=True,
                                                                                  pair_function=
                                                                                  triplet_make_pairs_random))

        dmp.evaluate(data)

    def test_siamese_triplet_loss_online(self):
        shape = (100, 200, 12)
        x_train, y_train = make_some_intelligent_noise(shape=shape)
        x_val, y_val = make_some_intelligent_noise(shape=shape)
        x_test, y_test = make_some_intelligent_noise(shape=shape)
        data = Dataset(x_train, y_train, x_val, y_val, x_test, y_test)

        dmp = DistanceMetricParadigm(verbose=True,
                                     prediction_model=OnlineTripletKerasPredictionModel(verbose=True))
        dmp.evaluate(data)

    def test_encoders(self):
        from useckit.paradigms.anomaly_detection.prediction_models.auto_encoder_keras_prediction_model import \
            AutoEncoderKerasPredictionModel
        encoder = AnomalyParadigm(prediction_model=AutoEncoderKerasPredictionModel(nb_epochs=2), verbose=True)
        encoder.evaluate(self.data)


if __name__ == '__main__':
    unittest.main()
