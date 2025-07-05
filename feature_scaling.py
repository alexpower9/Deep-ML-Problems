import numpy as np

from typing import Tuple

def feature_scaling(data: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:

    #return two arrays, one scaled by standardization and one scaled by min max
    rows, cols = data.shape
    standardized_data = np.zeros((rows, cols))
    normalized_data = np.zeros((rows, cols))

    for i in range(len(data[0])):
        standardized_data[:, i] = np.round((data[:, i] - np.mean(data[:, i])) / np.std(data[:, i]), 4)
        normalized_data[:,i] = np.round((data[:,i] - np.min(data[:,i])) / (np.max(data[:,i]) - np.min(data[:, i])),4)


    return standardized_data, normalized_data

data = np.array([[1, 2], [3, 4], [5, 6]])

std, norm = feature_scaling(data)

print(std,"\n", norm)