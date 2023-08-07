import json
import os.path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score


def _unison_shuffle_np_arrays_3(a: np.ndarray, b: np.ndarray, c: np.ndarray):
    assert len(a) == len(b) == len(c)
    p = np.random.permutation(len(a))
    return a[p], b[p], c[p]


def create_window_slices(data: np.ndarray,
                         labels: np.ndarray,
                         stride: int,
                         slice_size: int,
                         shuffle: bool = True) -> [np.ndarray, np.ndarray]:
    if not data.shape[0] == labels.shape[0]:
        raise TypeError("Error in AutoEvaluator::_create_slices(). Data and Labels differ in size.")

    if not len(data.shape) <= 3:
        raise TypeError("Error in AutoEvaluator::_create_slices(). Dimension not supported.")

    ret_sliced_data, ret_sliced_labels, ret_sample_origin = [], [], []

    for sample_id, (array, label) in enumerate(zip(data, labels)):
        array_slices, label_slices, sample_origin = [], [], []

        lost_samples_cnt, added_cnt = 0, 0

        for step_idx in range(0, array.shape[0], stride):
            arr = array[step_idx:step_idx + slice_size]

            if not arr.any():
                pass  # do not append if slice consists only of zero
            else:
                array_slices.append(arr)
                label_slices.append(label)
                sample_origin.append(sample_id)

        for i in range(len(array_slices)):
            if array_slices[i].shape == array_slices[0].shape:
                ret_sliced_data.append(array_slices[i])
                ret_sliced_labels.append(label_slices[i])
                ret_sample_origin.append(sample_origin[i])
                added_cnt += 1
            else:
                lost_samples_cnt += 1

        if not all(s.shape == array_slices[0].shape for s in array_slices):
            print('Warning: `slices` array created in AutoEvaluator::_create_slices() is ragged. '
                  'Check parameters stride, slice_size and shape of array. Lost',
                  lost_samples_cnt, 'samples and created', added_cnt,
                  'new samples. Check your slicing window settings.', file=sys.stderr)

    ret_sliced_data_np = np.array(ret_sliced_data)
    ret_sliced_labels_np = np.array(ret_sliced_labels)
    sample_origin_np = np.array(ret_sample_origin)

    print('Info: Slicing window data consumes', round(ret_sliced_data_np.nbytes / 1024 / 1024, 2), 'mb.',
          file=sys.stderr)

    # TODO check that supressing null arrays does not result in a skewed data set

    if shuffle:
        return _unison_shuffle_np_arrays_3(ret_sliced_data_np, ret_sliced_labels_np, sample_origin_np)
    else:
        return ret_sliced_data_np, ret_sliced_labels_np, sample_origin_np


def make_some_intelligent_noise(labels: int = 4, shape: tuple = (8, 100, 100, 4), noisiness: float = 0.5):
    biases = np.array([i / labels for i in range(labels)]) + (1 / (2 * labels))
    x = []
    y = []
    shape = list(shape)
    shape[0] = int(shape[0] / labels)

    for i, b in enumerate(biases):
        x.extend(np.random.normal(b, noisiness, shape))
        y.extend(np.ones((shape[0],)) * i)

    x = np.array(x)
    y = [f'User {int(y_elem)}' for y_elem in y]
    y = np.array(y)
    x = np.clip(x, -1, 1)
    return x, y


def contrastive_make_pairs(x, y):
    """Creates a tuple containing image pairs with corresponding label.

    Arguments:
        x: List containing images, each index in this list corresponds to one image.
        y: List containing labels, each label with datatype of `int`.

    Returns:
        Tuple containing two numpy arrays as (pairs_of_samples, labels),
        where pairs_of_samples' shape is (2len(x), 2,n_features_dims) and
        labels are a binary array of shape (2len(x)).
    """
    x = np.array(x)
    y = np.array(y)
    assert x.shape[0] == y.shape[0]
    y_set = set(y)

    pairs = []
    labels = []

    matching_masks = {}
    non_matching_masks = {}
    for label in y_set:
        match = (y == label)
        matching_masks[label] = match
        non_matching_masks[label] = np.invert(match)

    for i in range(len(x)):
        x1 = x[i]
        label = y[i]

        # generate matching pair
        matches = x[matching_masks[label]]
        i = np.random.randint(0, len(matches))
        x2 = matches[i]
        pairs += [[x1, x2]]
        labels += [0]

        # generate non-matching pair
        matches = x[non_matching_masks[label]]
        i = np.random.randint(0, len(matches))
        x2 = matches[i]
        pairs += [[x1, x2]]
        labels += [1]

    return np.array(pairs), np.array(labels).astype("float32")


def triplet_make_pairs_random(x, y):
    """Creates a tuple containing sample pairs with corresponding label. Both positive and negative samples are selected randomly.

    Arguments:
        x: Numpy array containing samples, each index in this list corresponds to one sample.
        y: Numpy array containing samples, each label with datatype of `int`.

    Returns:
        Tuple containing two numpy arrays as (pairs_of_samples, labels),
        where pairs_of_samples' shape is len(x) containing the base (0), positive (1) and negative sample (2) and
        labels are an array of shape len(x) containing the label of each base sample.
    """

    x = np.array(x)
    y = np.array(y)
    assert x.shape[0] == y.shape[0]
    y_set = set(y)

    pairs = []  # output: sample pairs for the siamese net (anchor, positive, negative)
    labels = []  # output: labels of the anchor sample per pair

    # indexes of the sample positions per label
    matching_masks = {}
    non_matching_masks = {}
    for label in y_set:
        matching_masks[label] = np.where(y == label)  # returns the indices of the current label
        non_matching_masks[label] = np.where(y != label)  # returns the indices of all other labels

    # iterate over all provided samples to build one pair per sample
    for i in range(x.shape[0]):
        # get anchor sample and its label
        anchor = x[i]
        anchor_label = y[i]

        # generate the positive pair -> another sample having the same label as the base sample
        positive_index = np.random.choice(matching_masks[anchor_label][0])
        while positive_index == i:  # the positive sample may not be the same as the base sample
            positive_index = np.random.choice(matching_masks[anchor_label][0])
        positive = x[positive_index]

        # generate non-matching pair
        negative = x[np.random.choice(non_matching_masks[anchor_label][0])]

        # append the sample pair to the output arrays
        pairs += [[anchor, positive, negative]]
        labels += [anchor_label]

    return np.array(pairs), np.array(labels).astype("float32")


def triplet_make_pairs_exhaust_positives(x, y):
    """Creates a tuple containing sample pairs with corresponding label. The positive values are exhaustedly matched,
     while negative samples are selected randomly.

    Arguments:
        x: Numpy array containing samples, each index in this list corresponds to one sample.
        y: Numpy array containing samples, each label with datatype of `int`.

    Returns:
        Tuple containing two numpy arrays as (pairs_of_samples, labels),
        where pairs_of_samples' shape is (len(samples per label) * (len(samples per label)-1) containing the anchor (0), positive (1) and negative sample (2) and
        labels are an array of shape (len(samples per label) * (len(samples per label)-1) containing the label of each base sample.
    """

    x = np.array(x)
    y = np.array(y)
    assert x.shape[0] == y.shape[0]
    y_set = set(y)

    pairs = []  # output: sample pairs for the siamese net (anchor, positive, negative)
    labels = []  # output: labels of the anchor sample per pair

    matching_masks = {}
    non_matching_masks = {}
    for label in y_set:
        matching_masks[label] = np.where(y == label)  # returns the indices of the current label
        non_matching_masks[label] = np.where(y != label)  # returns the indices of all other labels

    for i in range(x.shape[0]):
        anchor = x[i]
        anchor_label = y[i]

        for j in range(len(matching_masks[anchor_label][0])):

            if matching_masks[anchor_label][0][
                j] != i:  # ensure that the base and positive sample are not equal, skip if true
                positive = x[matching_masks[anchor_label][0][j]]

                # generate non-matching pair by choosing a random sample from the samples not being the anchor
                negative = x[np.random.choice(non_matching_masks[anchor_label][0])]

                pairs += [[anchor, positive, negative]]
                labels += [anchor_label]

    return np.array(pairs), np.array(labels).astype("float32")


def triplet_make_pairs_exhaust_all(x, y):
    """Creates a tuple containing sample pairs with corresponding label. The positive values are exhaustedly matched,
         for the negative samples the matches are choosen equally between the other labels and are each only used once
          per anchor.

        Arguments:
            x: Numpy array containing samples, each index in this list corresponds to one sample.
            y: Numpy array containing samples, each label with datatype of `int`.

        Returns:
            Tuple containing two numpy arrays as (pairs_of_samples, labels),
            where pairs_of_samples' shape is (len(samples per label)^2 * (len(samples per label)-1) containing the anchor (0), positive (1) and negative sample (2) and
            labels are an array of shape (len(samples per label)^2 * (len(samples per label)-1) containing the label of each anchor sample.
        """

    x = np.array(x)
    y = np.array(y)
    assert x.shape[0] == y.shape[0]
    y_set = set(y)

    pairs = []  # output: sample pairs for the siamese net (anchor, positive, negative)
    labels = []  # output: labels of the anchor sample per pair

    matching_masks = {}
    non_matching_indexes = {}  # contains indexes in this implementation
    for label in y_set:
        matching_masks[label] = np.where(y == label)  # returns the indices of the current label

    for i in range(x.shape[0]):
        anchor = x[i]
        anchor_label = y[i]

        non_matching_masks = []  # returns the indices of all other labels in separate arrays
        for other_label in y_set:
            if other_label != anchor_label:
                non_matching_masks.append(np.where(y == other_label))

        for j in range(len(matching_masks[label][0])):

            if matching_masks[anchor_label][0][
                j] != i:  # ensure that the base and positive sample are not equal, skip if true
                # generate positive pair
                positive = x[matching_masks[anchor_label][0][j]]

                # generate non-matching pair
                for k in range(len(non_matching_masks)):
                    rand_index = np.random.randint(0, len(non_matching_masks[k][0]))
                    negative = x[non_matching_masks[k][0][rand_index]]

                    # delete taken sample from mask to ensure that it is not taken a second time
                    non_matching_masks[k] = tuple([np.delete(non_matching_masks[k][0], rand_index)])

                    pairs += [[anchor, positive, negative]]
                    labels += [anchor_label]

    return np.array(pairs), np.array(labels).astype("float32")


def calculate_metrics(y_true, y_pred, duration, y_true_val=None, y_pred_val=None):
    res = pd.DataFrame(data=np.zeros((1, 4), dtype=np.float64), index=[0],
                       columns=['precision', 'accuracy', 'recall', 'duration'])
    res['precision'] = precision_score(y_true, y_pred, average='macro')
    res['accuracy'] = accuracy_score(y_true, y_pred)

    if not y_true_val is None:
        # this is useful when transfer learning is used with cross validation
        res['accuracy_val'] = accuracy_score(y_true_val, y_pred_val)

    res['recall'] = recall_score(y_true, y_pred, average='macro')
    res['duration'] = duration
    return res


def plot_epochs_metric(hist, file_name, metric='loss'):
    plt.figure()
    plt.plot(hist.history[metric])
    plt.plot(hist.history['val_' + metric])
    plt.title('model ' + metric)
    plt.ylabel(metric, fontsize='large')
    plt.xlabel('epoch', fontsize='large')
    plt.legend(['train', 'val'], loc='upper left')
    plt.savefig(file_name, bbox_inches='tight')
    plt.close()


def save_logs(output_directory, hist, y_pred, y_true, duration, lr=True, y_true_val=None, y_pred_val=None):
    hist_df = pd.DataFrame(hist.history)
    hist_df.to_csv(os.path.join(output_directory, 'history.csv'), index=False)

    df_metrics = calculate_metrics(y_true, y_pred, duration, y_true_val, y_pred_val)
    df_metrics.to_csv(os.path.join(output_directory, 'df_metrics.csv'), index=False)

    index_best_model = hist_df['loss'].idxmin()
    row_best_model = hist_df.loc[index_best_model]

    df_best_model = pd.DataFrame(data=np.zeros((1, 6), dtype=np.float64), index=[0],
                                 columns=['best_model_train_loss', 'best_model_val_loss', 'best_model_train_acc',
                                          'best_model_val_acc', 'best_model_learning_rate', 'best_model_nb_epoch'])

    df_best_model['best_model_train_loss'] = row_best_model['loss']
    df_best_model['best_model_val_loss'] = row_best_model['val_loss']
    df_best_model['best_model_train_acc'] = row_best_model['accuracy']
    df_best_model['best_model_val_acc'] = row_best_model['val_accuracy']
    if lr == True:
        df_best_model['best_model_learning_rate'] = row_best_model['lr']
    df_best_model['best_model_nb_epoch'] = index_best_model

    df_best_model.to_csv(os.path.join(output_directory, 'df_best_model.csv'), index=False)

    # for FCN there is no hyperparameters fine tuning - everything is static in code

    # plot losses
    plot_epochs_metric(hist, os.path.join(output_directory, 'epochs_loss.png'))

    return df_metrics


def save_test_duration(file_name, test_duration):
    res = pd.DataFrame(data=np.zeros((1, 1), dtype=np.float64), index=[0],
                       columns=['test_duration'])
    res['test_duration'] = test_duration
    res.to_csv(file_name, index=False)


def create_directory(directory_path):
    if os.path.exists(directory_path):
        return None
    else:
        try:
            os.makedirs(directory_path)
        except:
            # in case another machine created the path meanwhile !:(
            return None
        return directory_path


def save_logs_t_leNet(output_directory, hist, y_pred, y_true, duration):
    hist_df = pd.DataFrame(hist.history)
    hist_df.to_csv(os.path.join(output_directory, 'history.csv'), index=False)

    df_metrics = calculate_metrics(y_true, y_pred, duration)
    df_metrics.to_csv(os.path.join(output_directory, 'df_metrics.csv'), index=False)

    index_best_model = hist_df['loss'].idxmin()
    row_best_model = hist_df.loc[index_best_model]

    df_best_model = pd.DataFrame(data=np.zeros((1, 6), dtype=np.float64), index=[0],
                                 columns=['best_model_train_loss', 'best_model_val_loss', 'best_model_train_acc',
                                          'best_model_val_acc', 'best_model_learning_rate', 'best_model_nb_epoch'])

    df_best_model['best_model_train_loss'] = row_best_model['loss']
    df_best_model['best_model_val_loss'] = row_best_model['val_loss']
    df_best_model['best_model_train_acc'] = row_best_model['accuracy']
    df_best_model['best_model_val_acc'] = row_best_model['val_accuracy']
    df_best_model['best_model_nb_epoch'] = index_best_model

    df_best_model.to_csv(os.path.join(output_directory, 'df_best_model.csv'), index=False)

    # plot losses
    plot_epochs_metric(hist, os.path.join(output_directory, 'epochs_loss.png'))


def serialize_classification_report(arr1, arr2, output_folder, filename='classification-report.txt'):
    """Writes a classification_report from sklearn to file as .txt and .json."""
    from sklearn.metrics import classification_report
    with open(os.path.join(output_folder, filename), 'w') as f:
        f.write('Classification Report\n')
        f.write(classification_report(arr1, arr2))
    with open(os.path.join(output_folder, filename.replace('.txt', '.json')), 'w') as f2:
        f2.write(json.dumps(classification_report(arr1, arr2, output_dict=True)))


def analyze_samplelength(DATASET_LIST: list):
    """Creates a boxplot and descriptive statistics of a list of samples."""
    from statistics import mean, stdev, median
    samplelen_min, samplelen_max, samplelen_mean, samplelen_sd, samplelen_median = min(len(x['df']) for x in DATASET_LIST), \
                                                                                   max(len(x['df']) for x in DATASET_LIST), \
                                                                                   round(mean(len(x['df']) for x in DATASET_LIST)), \
                                                                                   round(stdev(len(x['df']) for x in DATASET_LIST)), \
                                                                                   round(median(len(x['df']) for x in DATASET_LIST)), \

    def get_q75_q25(dist):
        return np.percentile(dist, 75), np.percentile(dist, 25)
    samplelen_q75, samplelen_q25 = get_q75_q25([len(x['df']) for x in DATASET_LIST])

    plt.boxplot([[len(x['df']) for x in DATASET_LIST if x['sess'] == 1], [len(x['df']) for x in DATASET_LIST if x['sess'] == 2]], vert=False)
    plt.suptitle('Boxplot of sample lengths for scene "ButtonScene1H".')
    plt.title(f"Global min: {samplelen_min}, "
              f"max: {samplelen_max}, "
              f"M: {samplelen_mean}, "
              f"SD: {samplelen_sd}, "
              f"Med: {samplelen_median}, "
              f"Q25: {samplelen_q25}, "
              f"Q75: {samplelen_q75}.")
    plt.xlabel('Sample length (VR Sample Rate: 72 hz)')
    plt.ylabel('Session')
    plt.grid()
    plt.show()
    return {'min': samplelen_min, 'max': samplelen_max, 'mean': samplelen_mean, 'sd': samplelen_sd,
            'median': samplelen_median, 'q75': samplelen_q75, 'q25': samplelen_q25}
