import sys

import numpy as np
from numpy import ndarray
from sklearn.preprocessing import LabelEncoder, LabelBinarizer


class Dataset:

    def __init__(self,
                 trainset_data: ndarray,
                 trainset_labels: ndarray,
                 validationset_data: ndarray = None,
                 validationset_labels: ndarray = None,
                 testset_enrollment_data: ndarray = None,
                 testset_enrollment_labels: ndarray = None,
                 testset_matching_data: ndarray = None,
                 testset_matching_labels: ndarray = None,
                 normalization_check: bool = False):

        self.trainset_data = self._check_and_convert_type_data(trainset_data, name="trainset_data")
        self.trainset_labels = self._check_and_convert_type_label(trainset_labels, name="trainset_labels")
        self.validationset_data = self._check_and_convert_type_data(validationset_data, name="validationset_data")
        self.validationset_labels = self._check_and_convert_type_label(validationset_labels,
                                                                       name="validationset_labels")
        self.testset_enrollment_data = self._check_and_convert_type_data(testset_enrollment_data,
                                                                         name="testset_enrollment_data")
        self.testset_enrollment_labels = self._check_and_convert_type_label(testset_enrollment_labels,
                                                                            name="testset_enrollment_labels")
        self.testset_matching_data = self._check_and_convert_type_data(testset_matching_data,
                                                                       name="testset_matching_data")
        self.testset_matching_labels = self._check_and_convert_type_label(testset_matching_labels,
                                                                          name="testset_matching_labels")

        # perform checks of data
        self._check_data_pairs_provided()  # check if corresponding pairs were provided,
        # no array is empty and corresponding pairs are of the same length
        self._check_nan()  # check if any NaNs exists
        self._check_dataset_is_balanced()
        if normalization_check:
            self._normalisation_check()  # check if data is normalized in [-1, 1]

        self._setup_missing_sets()
        self._setup_reject_label()

        # label processing: label encoding
        self._label_encoder = LabelEncoder()
        self._label_encoder.fit(self.gather_labels())
        self._transform_lables()
        # label processing: label binarizing
        self._label_binarizer = LabelBinarizer()
        self._label_binarizer.fit(self.gather_labels())

    def _setup_missing_sets(self):
        if self.validationset_data is None:
            if self.testset_enrollment_data is None:
                raise ValueError(f"Critical: a validation set needs to be present.")
            else:
                self.validationset_data = self.testset_enrollment_data
                self.validationset_labels = self.testset_enrollment_labels
                print(f"useckit warning: because the validation set is None, the supplied testset enrollment data will "
                      f"be used instead.", file=sys.stderr)
        if self.testset_enrollment_data is None:
            if self.testset_matching_data is None:
                print(f"useckit warning: testset enrollment and matching data are None. This will cause all evaluation "
                      f"methods to fail.", file=sys.stderr)
            else:
                self.testset_enrollment_data = self.testset_matching_data
                self.testset_enrollment_labels = self.testset_matching_labels
                print(f"useckit warning: because the enrollment testset is None, the matching testset will be used "
                      f"instead.", file=sys.stderr)
        else:
            if self.testset_matching_data is None:
                print(f"useckit warning: testset matching data is None. This will cause all evaluation "
                      f"methods to fail.", file=sys.stderr)

    def _setup_reject_label(self):
        self.reject_label = 'reject'  # In some cases this will be changed further down in the method
        if self.testset_matching_labels is not None:
            try:
                match_label_set = set(self.testset_matching_labels)
                enroll_label_set = set(self.testset_enrollment_labels)
            except TypeError:  # np.ndarray is not hashable
                match_label_set = set(self.testset_matching_labels.tolist())
                enroll_label_set = set(self.testset_enrollment_labels.tolist())
            diff = match_label_set.difference(enroll_label_set)
            if len(diff) == 1:
                self.reject_label = diff.pop()
            else:
                for user_to_reject in diff:  # This does nothing if len(diff) == 0, but it also doesn't hurt
                    self.testset_matching_labels[self.testset_matching_labels == user_to_reject] = self.reject_label

    def view_one_hot_encoded_labels(self):
        def convert_to_onehot(labels: ndarray):
            return None if labels is None else self._label_binarizer.transform(labels)

        return convert_to_onehot(self.trainset_labels), convert_to_onehot(self.validationset_labels), \
               convert_to_onehot(self.testset_enrollment_labels), convert_to_onehot(self.testset_matching_labels)

    @staticmethod
    def _check_and_convert_type_data(obj, name) -> np.array:
        """Check the types of objects, print warnings and perform conversions."""
        return Dataset._check_and_convert_type(obj, name, float)

    @staticmethod
    def _check_and_convert_type_label(obj, name) -> np.array:
        """Check the types of objects, print warnings and perform conversions."""
        return Dataset._check_and_convert_type(obj, name, str)

    @staticmethod
    def _check_and_convert_type(obj, name, dtype):
        if obj is None:
            return None

        if not isinstance(obj, np.ndarray):
            print(f"Warning: provided object {name} is of type {str(type(obj))} (expected: np.ndarray). "
                  f"Attempting a cast to np.ndarray.", file=sys.stderr)
            arr = np.array(obj, dtype=dtype)
            return arr
        else:
            return obj

    def _check_data_pairs_provided(self):
        """Checks that if training data is provided also labels are provided. Raises exception if not."""

        # check for None
        if self.trainset_data is None or len(self.trainset_data) == 0:
            raise ValueError("Critical: trainset_data must not be None or empty.")

        if self.trainset_labels is None:
            raise ValueError("Critical: trainset_labels must not be None.")

        def _check(data, labels, name):
            if data is not None:
                if labels is None:
                    raise ValueError(f"Critical: if {name}_data is not None, {name}_labels must also be not None"
                                     f"However, {name}_labels is None! You rascal!")
                if len(data) == 0:
                    raise ValueError(f"Critical: length of {name}_data is {len(self.trainset_labels)}, "
                                     f"but must be greater than 0!")
                if len(data) != len(labels):
                    raise ValueError(f"Critical: length of {name}_data ({len(self.trainset_data)}) is not equal to the "
                                     f"length of {name}_labels ({len(self.trainset_labels)})!")

        _check(self.validationset_data, self.validationset_labels, 'validationset')
        _check(self.testset_enrollment_data, self.testset_enrollment_labels, 'testset_enrollment')
        _check(self.testset_matching_data, self.testset_matching_labels, 'testset_matching')

    def _check_nan(self):
        def _check_nan(array: ndarray, name):
            try:
                if array is not None and np.isnan(array).any():
                    raise ValueError(f'Critical: provided array {name} contains NaN values!')
            except TypeError:
                print(f'Warning: could not check if NaNs exist in array {name}, as its dtype is "{array.dtype}". '
                      f'A numerical dtype (e.g., int or float) is expected. This might lead to subsequent '
                      f'critical errors and wrong calculations.', file=sys.stderr)

        _check_nan(self.trainset_data, name="trainset_data")
        _check_nan(self.trainset_labels, name="trainset_labels")
        _check_nan(self.testset_matching_data, name="testset_matching_data")
        _check_nan(self.testset_matching_labels, name="testset_matching_labels")
        _check_nan(self.testset_enrollment_data, name="testset_enrollment_data")
        _check_nan(self.testset_enrollment_labels, name="testset_enrollment_labels")
        _check_nan(self.validationset_data, name="validationset_data")
        _check_nan(self.validationset_labels, name="validationset_labels")

    def _check_dataset_is_balanced(self):
        return True  # TODO implement

    def _normalisation_check(self):
        def _normalisation_check(array: ndarray):
            if array is not None:
                _max, _min = np.amax(array), np.amin(array)
                if _max > 1:
                    raise ValueError(f"Critical: dataset contains maximum value {_max} which exceeds [-1, 1].")
                if _min < -1:
                    raise ValueError(f"Critical: dataset contains minimum value {_min} which exceeds [-1, 1].")

        _normalisation_check(self.trainset_data)
        _normalisation_check(self.validationset_data)
        _normalisation_check(self.testset_enrollment_data)
        _normalisation_check(self.testset_matching_data)

    def gather_labels(self) -> np.ndarray:
        """This function concatenates all labels and returns them as np.array."""
        labels = [self.trainset_labels]
        if self.validationset_labels is not None:
            labels.append(self.validationset_labels)
        if self.testset_enrollment_labels is not None:
            labels.append(self.testset_enrollment_labels)
        if self.testset_matching_labels is not None:
            labels.append(self.testset_matching_labels)
        return np.concatenate(labels)

    def _transform_lables(self):
        self.trainset_labels = self._label_encoder.transform(self.trainset_labels)
        if self.validationset_labels is not None:
            self.validationset_labels = self._label_encoder.transform(self.validationset_labels)
        if self.testset_enrollment_labels is not None:
            self.testset_enrollment_labels = self._label_encoder.transform(self.testset_enrollment_labels)
        if self.testset_matching_labels is not None:
            self.testset_matching_labels = self._label_encoder.transform(self.testset_matching_labels)

    def reverse_label_transform(self, labels: ndarray):
        rejection_mask = labels == -1  # find all -1
        labels[rejection_mask] = 0  # remove all -1 to not confuse the encoder
        inverse_transformed_labels = self._label_encoder.inverse_transform(labels)
        inverse_transformed_labels = np.array(inverse_transformed_labels, dtype=str)
        inverse_transformed_labels[rejection_mask] = self.reject_label  # manually transform positions with -1 in labels
        return inverse_transformed_labels

    def amount_classes(self):
        return len(self._label_encoder.classes_)

    def train_classes(self):
        return len(np.unique(self.trainset_labels))


# TODO: This doesn't seem like a good idea anymore, probably needs to change.
#  Also isn't updated to enrollment and matching testset...
def split_data_by_amount(data: ndarray, labels: ndarray, train_split_parts: int = 2, test_split_parts: int = 1,
                         validation_split_parts: int = 1) -> Dataset:
    assert False, 'TODO -- this function is undefined. Function is disabled.'

    assert train_split_parts > 0 and test_split_parts >= 0 and validation_split_parts >= 0
    assert len(data) == len(labels)

    total_parts = train_split_parts + test_split_parts + validation_split_parts

    split_begin = 0
    split_end = 0

    split_begin = split_end
    split_end = int(len(data) / (train_split_parts / total_parts))
    trainset_data = data[split_begin:split_end]
    trainset_labels = labels[split_begin:split_end]

    if test_split_parts > 0:
        split_begin = split_end
        split_end = split_begin + int(len(data) / (test_split_parts / total_parts))
        testset_data = data[split_begin:split_end]
        testset_labels = labels[split_begin:split_end]
    else:
        testset_data = None
        testset_labels = None

    if validation_split_parts > 0:
        split_begin = split_end
        split_end = split_begin + int(len(data) / (validation_split_parts / total_parts))
        validationset_data = data[split_begin:split_end]
        validationset_labels = labels[split_begin:split_end]
    else:
        validationset_data = None
        validationset_labels = None

    return Dataset(trainset_data=trainset_data,
                   trainset_labels=trainset_labels,
                   testset_enrollment_data=testset_data,
                   testset_enrollment_labels=testset_labels,
                   validationset_data=validationset_data,
                   validationset_labels=validationset_labels)
