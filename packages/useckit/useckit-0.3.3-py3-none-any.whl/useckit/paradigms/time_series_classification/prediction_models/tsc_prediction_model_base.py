from abc import abstractmethod

import numpy as np

from useckit.util.dataset import Dataset
from ..._paradigm_base import PredictionModelBase


class TSCBasePredictionModel(PredictionModelBase):
    def __init__(self, output_dir: str = "tsc_model_out", verbose: int = 0):
        super().__init__(output_dir, verbose)

    def convert_dataset_to_legacy_values(self, dataset: Dataset) -> (
            np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray, int, int):
        x_train, x_val = dataset.trainset_data, dataset.validationset_data
        y_train, y_val, _, _ = dataset.view_one_hot_encoded_labels()

        # https://github.com/hfawaz/dl-4-tsc/issues/40#issuecomment-1144629152
        # y_test is the label OneHotEncoded, while y_true is the label as an integer.
        # For convenience, all the classifiers have been coded using the same signature for the functions.

        y_true = np.argmax(y_val, axis=1)
        nb_classes = dataset.amount_classes()
        input_shape = x_train.shape[1:]

        assert isinstance(nb_classes, int)
        assert x_train.shape[0] == y_train.shape[0]
        assert x_val.shape[0] == y_val.shape[0]

        return x_train, x_val, y_train, y_val, y_true, input_shape, nb_classes

    @abstractmethod
    def fit(self, dataset: Dataset, *args, **kwargs):
        pass

    @abstractmethod
    def predict(self, x_test, y_true, x_train, y_train, y_test, return_df_metrics=True):
        pass

    @abstractmethod
    def restore_model_trainables(self, path_like, dataset: Dataset = None, **kwargs):
        pass
