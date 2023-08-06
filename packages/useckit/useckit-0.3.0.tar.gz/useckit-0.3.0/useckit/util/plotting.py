import os
from collections import Counter

import keras.callbacks
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as metrics

from useckit.util.utils import serialize_classification_report


def plot_roc_curve(labels_test, predictions, output_directory):
    fpr, tpr, threshold_roc = metrics.roc_curve(labels_test, predictions)
    roc_auc = metrics.auc(fpr, tpr)

    plt.title('Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.tight_layout()
    plt.savefig(os.path.join(output_directory, "roc_curve.pdf"))
    plt.clf()

    precision, recall, threshold_prc = metrics.precision_recall_curve(labels_test, predictions)
    precision = np.array(precision[:-1])
    recall = np.array(recall[:-1])
    f1 = precision * recall / (precision + recall)
    plt.title('Precision, Recall and F1-Score over Threshold')
    plt.plot(threshold_prc, precision)
    plt.plot(threshold_prc, recall)
    plt.plot(threshold_prc, f1)
    plt.xlabel("Threshold")
    plt.ylabel("Rate")
    plt.legend(['precision', 'recall', 'f1'], loc='lower left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_directory, "precision_recall_curve.pdf"))
    plt.clf()

    return fpr, tpr, threshold_roc, precision, recall, threshold_prc


def plot_history_df(history: keras.callbacks.History, path, name=''):
    """Plots keras history."""
    import matplotlib.pyplot as plt
    import os

    # adapt type if keras-object is passed
    if isinstance(history, keras.callbacks.History):
        history = history.history

    if not isinstance(history, dict):
        raise ValueError("history-object must be of type dict.")

    if 'acc' not in history.keys() and 'accuracy' in history.keys():
        history['acc'] = history['accuracy']

    if 'val_acc' not in history.keys() and 'val_accuracy' in history.keys():
        history['val_acc'] = history['val_accuracy']

    if 'acc' not in history.keys():
        print("useckit warning: cannot plot history df without accuracy keys")
        return

    training_acc = history['acc']
    validation_acc = history['val_acc']
    loss = history['loss']
    val_loss = history['val_loss']

    epochs = range(len(training_acc))

    plt.ylim(0, 1)
    plt.plot(epochs, training_acc, 'tab:blue', label='Training acc')
    plt.plot(epochs, validation_acc, 'tab:orange', label='Validation acc')
    plt.title('Training and validation accuracy ' + name)
    plt.legend()
    plt.savefig(os.path.join(os.path.dirname(path), 'history_acc.pdf'))
    # plt.show()
    plt.close()

    plt.figure()

    plt.plot(epochs, loss, 'tab:green', label='Training loss')
    plt.plot(epochs, val_loss, 'tab:red', label='Validation loss')
    plt.title('Training and validation loss ' + name)
    plt.legend()
    plt.savefig(os.path.join(os.path.dirname(path), 'history_loss.pdf'))
    # plt.show()
    plt.close()
    return training_acc, validation_acc


def plot_confusion_matrix(cm,
                          target_names,
                          path='',
                          title='Confusion Matrix',
                          cmap=None,
                          normalize=True,
                          fname='confusion-matrix.pdf'):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    fname:        filename.

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html
    """
    import matplotlib.pyplot as plt
    import numpy as np
    import itertools

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    plt.figure()  # figsize=(4, 3.33))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        plt.xticks(tick_marks, target_names, rotation=45)
        plt.yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            plt.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            plt.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True class')
    plt.xlabel('Predicted class\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    plt.savefig(os.path.join(path, fname), bbox_inches='tight')
    # plt.show()
    plt.close()


def do_cm(x_val: np.ndarray,
          y_val: np.ndarray,
          model,  # : TSCBasePredictionModel should be the type hint, but that can lead to circular imports. However,
          # the real underlying issue is that the model is used in plotting at all!
          output_dir: str,
          perform_per_sample_majority_vote: bool = False,
          val_sample_origin: bool = False,
          perform_majority_vote: bool = False):
    from sklearn.metrics import confusion_matrix

    assert isinstance(x_val, np.ndarray), 'Param `X` must be np.ndarray but is ' + str(type(x_val))
    assert isinstance(y_val, np.ndarray), 'Param `Y_labels` must be np.ndarray but is ' + str(type(y_val))

    assert x_val.shape[0] == y_val.shape[0]

    # Confusion Matrix and Classification Report
    y_pred = model.predict(x_val, y_val, x_val, y_val, y_val, return_df_metrics=False)
    y_val = np.argmax(y_val, axis=1)
    cm = confusion_matrix(y_val, y_pred)

    serialize_classification_report(y_val, y_pred, output_dir)
    plot_confusion_matrix(cm, set(y_val), output_dir, normalize=False)

    assert perform_per_sample_majority_vote is False or \
           perform_majority_vote is False, 'perform_per_sample_majority_vote and _perform_majority_vote cannot both be active in do_cm()!'

    if perform_per_sample_majority_vote:
        cm_lst = np.zeros(np.array(cm).shape).tolist()
        val_sample_origin_np = np.array(val_sample_origin)

        for sample_id in set(val_sample_origin_np.flatten()):  # loop over all existing sample origin id's
            indices = np.where(val_sample_origin_np == sample_id)[0]  # find all indices that belong to some sample
            majority_vote_pred = Counter(y_pred[indices].tolist()).most_common()[0][
                0]  # find the sample that was most commonly predicted
            ground_truth = Counter(y_val[indices].tolist()).most_common()  # find ground truth for current segment
            assert len(ground_truth) == 1  # check that ground truth really exists only once for all slices
            ground_truth = ground_truth[0][0]  # determine ground truth label

            cm_lst[ground_truth][majority_vote_pred] += 1  # increment confusion matrix at correct cell

        plot_confusion_matrix(np.array(cm_lst), set(y_val),
                              path=output_dir,
                              fname=f'confusion-matrix-per-sample-vote-normalized.pdf')
        plot_confusion_matrix(np.array(cm_lst).astype(int), set(y_val),
                              normalize=False,
                              path=output_dir,
                              fname=f'confusion-matrix-per-sample-vote-nonnormalized.pdf')
        with open(os.path.join(output_dir, "confusion-matrix-per-sample-vote-nonnormalized.txt"),
                  'w') as f:
            f.write(np.array2string(np.array(cm_lst).astype(int)))

    if perform_majority_vote:
        assert False, 'perform_majority_vote has been disabled.'
        reduced_cm = []
        if perform_majority_vote:
            for line in cm:
                # we first see how long the current line is
                # then we add zeros to a reduced_cm
                # then we determine the relative majority and set this one to '1'
                # => relative majority vote
                line_len = len(line)  # check length of current line
                reduced_cm.append([0] * line_len)  # add zeros to fit the line length
                reduced_cm[-1][np.argmax(line)] = 1  # find argmax of line and set it to '1'
        reduced_cm_arr = np.array(reduced_cm)  # create np array
        plot_confusion_matrix(reduced_cm_arr,
                              set(y_val),
                              path=output_dir,
                              normalize=False,
                              fname='confusion-matrix-vote.pdf')
