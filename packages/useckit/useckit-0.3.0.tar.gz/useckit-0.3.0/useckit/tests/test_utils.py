import numpy as np


def make_some_intelligent_noise(labels: int = 4, shape: tuple = (100, 100, 100), noisiness: float = 0.1):
    biases = np.array([i / labels for i in range(labels)]) + (1 / (2 * labels))
    x = []
    y = []
    shape = list(shape)
    shape[0] = int(shape[0] / labels)
    i = 0
    for b in biases:
        x.extend(np.random.normal(b, noisiness, shape))
        y.extend(np.ones((shape[0],)) * i)
        i += 1
    x = np.array(x)
    y = np.array(y)
    x = np.clip(x, -1, 1)
    return x, y
