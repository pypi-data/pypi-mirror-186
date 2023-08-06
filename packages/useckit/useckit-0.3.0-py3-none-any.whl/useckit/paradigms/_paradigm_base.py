import os
import random
import time
from abc import ABC, abstractmethod
from datetime import datetime

import dill
import numpy as np

from useckit.util.dataset import Dataset
from useckit.util.plotting import plot_history_df


class PredictionModelBase(ABC):
    def __init__(self, output_dir: str = "model_out", verbose: bool = False):
        self.output_dir = output_dir
        self.verbose = verbose

    def _plot_history(self, history):
        try:
            history['epoch'] = history.index
            history['modelname'] = str(type(self))

            plot_history_df(history, self.output_dir)
        except Exception as e:
            print(e)

    def merge_paradigm_output_folder(self, paradigm_output_folder: str):
        self.output_dir = os.path.join(paradigm_output_folder, self.output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    @abstractmethod
    def persist_model_trainables(self, path_like: str = 'saved_trainable_values', **kwargs):
        pass

    @abstractmethod
    def restore_model_trainables(self, path_like: str, **kwargs):
        pass

    @abstractmethod
    def fit(self, *args, **kwargs):
        pass

    @abstractmethod
    def predict(self, *args, **kwargs):
        pass


class EvaluationMethodBase(ABC):
    def __init__(self, output_dir: str = "evaluation"):
        self.output_dir = output_dir

    def merge_paradigm_output_folder(self, paradigm_output_folder: str):
        self.output_dir = os.path.join(paradigm_output_folder, self.output_dir)
        os.makedirs(self.output_dir, exist_ok=True)

    @abstractmethod
    def evaluate(self, dataset: Dataset, prediction_model: PredictionModelBase, **kwargs):
        pass


class ParadigmBase(ABC):
    # static variables shared across all instances of ParadigmBase
    _experiment_number: int = 1
    _init_timestamp: str = None

    # Verbose should probably rather be an int between 0 and 2 as that is what keras expects to receive.
    # 1 and 2 still evaluate to True when cast as bool, so they don't even mess with UsecKit's internal logic,
    # assuming no if verbose==True nonsense is left somewhere in the code.
    # Seed also should proabably not be an instance parameter as it is just used to call a static method.
    def __init__(self,
                 prediction_model: PredictionModelBase,
                 name: str = None,
                 subname: str = None,
                 output_dir: str = None,
                 evaluation_methods: [EvaluationMethodBase] = tuple(),
                 verbose: bool = True,
                 seed=None,
                 create_new_output_folder=False):
        if ParadigmBase._init_timestamp is None or create_new_output_folder:
            self.renew_init_folder()
        self.verbose = verbose
        if seed is not None:
            self.set_seed(seed)
        self._manage_output_dir(name, output_dir, subname, prediction_model)
        self._propagate_output_dir_to_model_evaluation(prediction_model, evaluation_methods)

    def persist(self):
        with open(os.path.join(self.output_dir, f"paradigm_{self.name}.pickle"), "wb") as file:
            dill.dump(self, file)

    @staticmethod
    def restore(persisted_path_like: str, new_name: str, new_output_dir: str):
        with open(persisted_path_like, "rb") as file:
            paradigm = dill.load(file)
            paradigm._manage_output_dir(new_name, new_output_dir)
            paradigm._propagate_output_dir_to_model_evaluation(paradigm.prediction_model, paradigm.evalution_methods)
        return paradigm

    def _manage_output_dir(self, name: str, output_dir: str, subname: str, prediction_model):
        # root folder
        if output_dir is None or output_dir.strip() == "":
            self.output_dir = f"_useckit-out_" \
                              f"{ParadigmBase._init_timestamp}"
        else:
            self.output_dir = output_dir
        # subfolder
        if name is None or name.strip() == "":
            self.name = f"experiment_{ParadigmBase._experiment_number}_{type(self).__name__}"
            if subname is not None:  # append to name if appendix is given
                if subname.strip() != "":
                    self.name += f'_{subname}'
            else:
                try:
                    self.name += '_' + prediction_model.model_description.__name__
                except AttributeError:
                    # some models do not provide these descriptions, then we try to get the string via class name
                    # in case this does not work out, we append nothing
                    try:
                        self.name += '_' + type(prediction_model).__name__
                    except Exception:
                        pass  # append nothing

        else:
            self.name = name
        self.output_dir = os.path.join(self.output_dir, self.name)
        os.makedirs(self.output_dir, exist_ok=True)
        ParadigmBase._experiment_number += 1
        if len(os.listdir(self.output_dir)) != 0:
            raise AttributeError(
                "Please choose a unique name for your experiment or delete/move previous results, " +
                "if you want to refrain from naming them by hand")

    def _propagate_output_dir_to_model_evaluation(self, prediction_model: PredictionModelBase,
                                                  evaluation_methods: [EvaluationMethodBase]):
        self.prediction_model = prediction_model
        prediction_model.merge_paradigm_output_folder(self.output_dir)
        if isinstance(evaluation_methods, EvaluationMethodBase):
            evaluation_methods = [evaluation_methods]
        evaluation_methods = list(evaluation_methods)
        self._set_evaluation_methods(evaluation_methods)

    def _set_evaluation_methods(self, evaluation_methods: [EvaluationMethodBase]):
        for eval_method in evaluation_methods:
            eval_method.merge_paradigm_output_folder(self.output_dir)
        self.evalution_methods = evaluation_methods

    def evaluate(self, dataset: Dataset):
        start_time = time.time()

        if self.verbose > 0:
            print(f'useckit info: persisting paradigm {self.name} of type {type(self).__name__}')
        self.persist()

        if self.verbose > 0:
            print(f'useckit info: fitting model of type {type(self.prediction_model).__name__}')
        self.fit_prediction_model(dataset)

        if self.verbose > 0:
            print(
                f'useckit info: finished fitting model of type {type(self.prediction_model).__name__} ' +
                f'after {round((time.time() - start_time), 2)} seconds.')
            print(f'useckit info: running evaluation methods')

        self.run_evaluation_methods(dataset)

        if self.verbose > 0:
            print(
                f'useckit info: Finished evaluation the paradigm {self.name} of type {type(self)} ' +
                f'after {round((time.time() - start_time), 2)} seconds.')

    def fit_prediction_model(self, dataset: Dataset) -> PredictionModelBase:
        self.prediction_model.fit(dataset)
        return self.prediction_model

    @abstractmethod
    def restore_prediction_model_trainables(self, *args, **kwargs) -> PredictionModelBase:
        pass

    def run_evaluation_methods(self, dataset: Dataset, **kwargs):
        for eval_method in self.evalution_methods:
            eval_method.evaluate(dataset, self.prediction_model)

    @staticmethod
    def set_seed(seed: int):
        import tensorflow as tf
        tf.keras.backend.clear_session()
        tf.random.set_seed(seed)
        random.seed(seed)
        np.random.seed(seed)
        os.environ['PYTHONHASHSEED'] = str(seed)
        os.environ['TF_CUDNN_DETERMINISTIC'] = '1'

    def renew_init_folder(self):
        """Upon importing useckit, all paradigms share the same output folder.
        Calling this method will ensure that a new output folder is created for the next experiments."""
        ParadigmBase._init_timestamp = str(datetime.now().replace(microsecond=0)).replace(' ', '_').replace(':', '-')
