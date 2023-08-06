import os
from abc import ABC, abstractmethod

import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

from useckit.util.dataset import Dataset
from useckit.util.plotting import plot_confusion_matrix
from useckit.util.utils import serialize_classification_report


class IdentificationModel(ABC):

    @abstractmethod
    def identify(self, samples: np.ndarray) -> np.ndarray:
        pass


def perform_identification_evaluation(identification_model: IdentificationModel, dataset: Dataset, output_folder: str):
    testset_data, testset_labels = dataset.testset_matching_data, dataset.testset_matching_labels

    testset_predictions = identification_model.identify(testset_data)
    testset_labels_reverse_transformed = dataset.reverse_label_transform(testset_labels)

    cm = confusion_matrix(testset_labels_reverse_transformed, testset_predictions)

    os.makedirs(output_folder, exist_ok=True)
    serialize_classification_report(testset_labels_reverse_transformed, testset_predictions, output_folder)
    all_labels = dataset.reverse_label_transform(dataset.gather_labels())
    all_labels = np.unique(all_labels)
    plot_confusion_matrix(cm, all_labels, output_folder,
                          normalize=False)
