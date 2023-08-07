import unittest

from useckit.tests.test_utils import make_some_intelligent_noise
from useckit.util.dataset import Dataset


class TestUseckit(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.x_train, self.y_train = make_some_intelligent_noise(labels=3, shape=(15, 10, 1))
        self.x_val, self.y_val = make_some_intelligent_noise(labels=3, shape=(15, 10, 1))
        self.x_test, self.y_test = make_some_intelligent_noise(labels=3, shape=(15, 10, 1))

    def test_dataset_initialization_train(self):
        exception_thrown = False
        try:
            data = Dataset(trainset_data=self.x_train,
                           trainset_labels=self.y_train)
        except ValueError:
            exception_thrown = True
        assert exception_thrown

    def test_dataset_initialization_trainval(self):
        data = Dataset(trainset_data=self.x_train,
                       trainset_labels=self.y_train,
                       validationset_data=self.x_val,
                       validationset_labels=self.y_val)
        return data

    def test_dataset_initialization_trainvalenroll(self):
        data = Dataset(trainset_data=self.x_train,
                       trainset_labels=self.y_train,
                       validationset_data=self.x_val,
                       validationset_labels=self.y_val,
                       testset_enrollment_data=self.x_test,
                       testset_enrollment_labels=self.y_test)
        return data

    def test_dataset_initialization_trainvalenrolltest(self):
        data = Dataset(trainset_data=self.x_train,
                       trainset_labels=self.y_train,
                       validationset_data=self.x_val,
                       validationset_labels=self.y_val,
                       testset_enrollment_data=self.x_test,
                       testset_enrollment_labels=self.y_test,
                       testset_matching_data=self.x_test,
                       testset_matching_labels=self.y_test)
        return data

    def test_dataset_initialization_traintest(self):
        data = Dataset(trainset_data=self.x_train,
                       trainset_labels=self.y_train,
                       testset_enrollment_data=self.x_test,
                       testset_enrollment_labels=self.y_test)
        return data

    # def test_slicing(self):
    #     data = Dataset(trainset_data=self.x_train,
    #                    trainset_labels=self.y_train,
    #                    validationset_data=self.x_val,
    #                    validationset_labels=self.y_val,
    #                    testset_enrollment_data=self.x_test,
    #                    testset_enrollment_labels=self.y_test,
    #                    enable_window_slicing=True,
    #                    window_slicing_size=4,
    #                    window_slicing_stride=2)
    #     assert data.trainset_data.shape == (60, 4, 1)
    #     assert data.validationset_data.shape == (60, 4, 1)
    #     assert data.testset_data.shape == (60, 4, 1)


if __name__ == '__main__':
    unittest.main()
