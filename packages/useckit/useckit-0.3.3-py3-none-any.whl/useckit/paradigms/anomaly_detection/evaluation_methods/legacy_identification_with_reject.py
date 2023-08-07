import sys

import numpy as np
from numpy import ndarray
from sklearn import metrics

from .anomaly_evaluation_method_base import AnomalyBaseEvaluationMethod
from ..prediction_models.anomaly_prediction_model_base import AnomalyBasePredictionModel
from ....util.dataset import Dataset
from ....util.plotting import plot_confusion_matrix


def _check_accuracy(threshold, predictions, assumed_label, true_labels):
    true = 0
    false = 0
    for prediction, true_label in zip(predictions, true_labels):
        if prediction <= threshold and assumed_label == true_label:
            true += 1
        else:
            false += 1
    return true / (true + false)


def _find_optimal_thersholds(thresholding_data: ndarray, thresholding_labels: ndarray,
                             prediction_model: AnomalyBasePredictionModel):
    thresh_predicts = prediction_model.predict(thresholding_data)
    model_thresholds = []
    for model_label, model_preds in enumerate(thresh_predicts):
        best_acc = 0.
        best_threshold = 0.
        for threshold_candidate in model_preds:
            acc = _check_accuracy(threshold_candidate, model_preds, model_label, thresholding_labels)
            if acc > best_acc:
                best_threshold = threshold_candidate
                best_acc = acc
        model_thresholds.append(best_threshold)
    return model_thresholds


def _predict_labels_from_thresholds(test_predicts: ndarray, model_thresholds: list):
    test_predicts = np.transpose(test_predicts)
    test_predict_labels = []
    for sample_id, sample_preds in enumerate(test_predicts):
        lowest_threshold_ratio = sys.float_info.max
        label = -1  # reject
        for model_label, pred in enumerate(sample_preds):
            if pred < model_thresholds[model_label] and pred / model_thresholds[model_label] < lowest_threshold_ratio:
                label = model_label
                lowest_threshold_ratio = pred / model_thresholds[model_label]
        test_predict_labels.append(label)

    return test_predict_labels


class LegacyIdentificationRejectIndividualThreshold(AnomalyBaseEvaluationMethod):

    def __init__(self, output_dir: str = "evaluation_identification_with_reject_legacy"):
        super().__init__(output_dir)

    def evaluate(self, dataset: Dataset, prediction_model: AnomalyBasePredictionModel, **kwargs):
        test_data, test_labels = dataset.testset_matching_data, dataset.testset_matching_labels
        thresholding_data, thresholding_labels = dataset.testset_enrollment_data, dataset.testset_enrollment_labels

        model_thresholds = _find_optimal_thersholds(thresholding_data, thresholding_labels, prediction_model)
        test_predicts = prediction_model.predict(test_data)

        number_models = test_predicts.shape[0]
        reject_mask = test_labels >= number_models  # users not seen during training
        test_labels = test_labels.copy()
        test_labels[reject_mask] = -1

        test_predict_labels = _predict_labels_from_thresholds(test_predicts, model_thresholds)
        contingency_table = metrics.confusion_matrix(test_labels, test_predict_labels)

        label_set = np.unique(np.concatenate((test_labels, test_predict_labels)))
        label_set = label_set[label_set != -1]
        label_names = dataset.reverse_label_transform(label_set)
        label_names = list(label_names)
        label_names.append("reject")
        plot_confusion_matrix(contingency_table, target_names=label_names, path=self.output_dir,
                              title='Contingency Table', fname='contingency_table.pdf', normalize=False)
