import os
from abc import ABC, abstractmethod

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

from useckit.util.dataset import Dataset
from useckit.util.plotting import plot_confusion_matrix

from useckit.util.utils import serialize_classification_report


class VerificationModel(ABC):

    @abstractmethod
    def verify(self, samples: np.ndarray, identity_claims: np.ndarray) -> np.ndarray:
        # identity_claims should be a 1-dim array of ints corresponding to the number transformed by the dataset used
        # in training. It should have the same size as the first dimension of samples
        # the result is a boolean array of same size as identity_claims
        pass


def perform_verification_evaluation(verification_model: VerificationModel, dataset: Dataset, output_folder: str):
    testset_matching_data, testset_matching_labels = dataset.testset_matching_data, dataset.testset_matching_labels
    testset_enrollment_labels = dataset.testset_enrollment_labels

    total_ground_truth = np.zeros(len(set(testset_enrollment_labels)) * len(testset_matching_data), dtype=int)
    total_predictions = np.zeros(len(set(testset_enrollment_labels)) * len(testset_matching_data), dtype=int)
    total_index = 0

    for enrollment_label in set(testset_enrollment_labels):
        label_ground_truth: np.ndarray = testset_matching_labels
        label_claims: np.ndarray = np.ones(shape=label_ground_truth.shape, dtype=int) * enrollment_label
        ground_truth: np.ndarray = label_ground_truth == label_claims
        predictions: np.ndarray = verification_model.verify(testset_matching_data, label_claims)

        label_reverse_transformed = str(dataset.reverse_label_transform(np.array([enrollment_label]))[0])
        label_sub_dir = os.path.join(output_folder, label_reverse_transformed)
        os.makedirs(label_sub_dir, exist_ok=True)

        serialize_classification_report(ground_truth, predictions, label_sub_dir,
                                        f'{label_reverse_transformed}-classification-report.txt')

        total_ground_truth[total_index:total_index + len(ground_truth)] = ground_truth
        total_predictions[total_index:total_index + len(predictions)] = predictions
        total_index += len(ground_truth)

        cm = confusion_matrix(ground_truth, predictions)
        plot_confusion_matrix(cm, target_names=['reject', 'accept'], path=label_sub_dir, normalize=False)

    os.makedirs(output_folder, exist_ok=True)

    serialize_classification_report(total_ground_truth, total_predictions,
                                    output_folder, 'all_labels_classification-report.txt')

    cm = confusion_matrix(total_ground_truth, total_predictions)
    plot_confusion_matrix(cm, target_names=['reject', 'accept'], path=output_folder, normalize=False)
