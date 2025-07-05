import numpy as np
import math


"""
    Define this as as log_soft(z_i) = z_i - log(np.sum(math.pow(e, z_i))
"""
def log_softmax(scores: list) -> np.ndarray:
    results = []

    sum_of_all = 0
    for element in scores:
        sum_of_all += math.pow(math.e, element)

    for element in scores:
        results.append(element - np.log(sum_of_all))

    return np.array(results)

A = np.array([1, 2, 3])
print(log_softmax(A))