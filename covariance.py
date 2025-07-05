import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    transpose = np.array(vectors).T
    means = np.mean(transpose, axis=0)

    centered = transpose - means 
    centered_T = transpose.T 

    result = np.dot(centered_T, centered) * (1 / (len(vectors[0]) - 1))
    return result

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# arr2 = arr1.T
# means = np.mean(arr2, axis=0)

# centered = arr2 - means
# centered_T = arr2.T 

# result = np.dot(centered_T, centered) * (1 / (len(arr1[0]) - 1))


# print(result)
print(calculate_covariance_matrix(arr1))
    