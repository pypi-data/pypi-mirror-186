from abc import abstractmethod

import numpy as np

from useckit.util.dataset import Dataset
from ..._paradigm_base import PredictionModelBase


class AnomalyBasePredictionModel(PredictionModelBase):

    def __init__(self, output_dir: str = "model_out", verbose: bool = False):
        super().__init__(output_dir, verbose)

    @abstractmethod
    def fit(self, dataset: Dataset):
        pass

    # outputs a np array of shape (number_individual_models, x_test.shape[0]) containing the normalised mse values
    # the individual models produce when recreating the samples contained in x_test.
    # Therefore output[i][j] returns the i'th model's output (corresponding to the i'th user) of sample j.
    @abstractmethod
    def predict(self, x_test) -> np.ndarray:
        pass

    @abstractmethod
    def persist_model_trainables(self, path_like: str = 'saved_trainable_values',
                                 overridden_individual_file_name: str = None, **kwargs):
        pass

    @abstractmethod
    def restore_model_trainables(self,
                                 path_like: str,
                                 dataset: Dataset = None,
                                 path_like_individual_models_file_name: str = 'best_model.hdf5',
                                 **kwargs):
        pass

    @abstractmethod
    def modify_output_dir_for_individual_model(self, index: int, base_output_dir: str = None) -> str:
        pass
