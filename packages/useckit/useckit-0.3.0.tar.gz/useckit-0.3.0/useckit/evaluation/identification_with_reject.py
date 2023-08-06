from abc import abstractmethod

import numpy as np

from useckit.evaluation.identification import IdentificationModel, perform_identification_evaluation
from useckit.util.dataset import Dataset


#  This overrides the pure IdentificationModel to avoid code duplication in the actual evaluation method below.
class IdentificationOrRejectModel(IdentificationModel):

    def identify(self, samples: np.ndarray) -> np.ndarray:
        return self.identify_or_reject(samples)

    @abstractmethod
    def identify_or_reject(self, samples: np.ndarray):
        pass


def perform_identification_or_reject_evaluation(identification_model: IdentificationOrRejectModel, dataset: Dataset,
                                                output_folder: str):
    perform_identification_evaluation(identification_model=identification_model, dataset=dataset,
                                      output_folder=output_folder)
