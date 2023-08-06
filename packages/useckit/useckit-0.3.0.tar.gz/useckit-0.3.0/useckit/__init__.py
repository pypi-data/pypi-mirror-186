from useckit.paradigms.time_series_classification.tsc_paradigm import TSCParadigm
from useckit.paradigms.anomaly_detection.anomaly_paradigm import AnomalyParadigm
from useckit.paradigms.distance_learning.distance_paradigm import DistanceMetricParadigm
from useckit.util.dataset import Dataset


def set_seed(seed: int = 42) -> None:
    """Sets RNG seed to python, numpy, tensorflow, and environment to the provided number."""
    from useckit.paradigms._paradigm_base import ParadigmBase
    ParadigmBase.set_seed(seed)
