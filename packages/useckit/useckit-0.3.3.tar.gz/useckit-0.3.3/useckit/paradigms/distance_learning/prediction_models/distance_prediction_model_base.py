from abc import abstractmethod
from useckit.util.dataset import Dataset
from ..._paradigm_base import PredictionModelBase


class DistanceBasePredictionModel(PredictionModelBase):

    def __init__(self, output_dir: str = "model_out", verbose: bool = False):
        super().__init__(output_dir=output_dir, verbose=verbose)

    @abstractmethod
    def fit(self, dataset: Dataset):
        pass

    @abstractmethod
    def predict(self, x_test_1, x_test_2):
        pass
