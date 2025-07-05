import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    #matrix can only be reshaped if n * m = r * c, where r and c are the dimensions of the new matrix
    dims1 = len(a) * len(a[0])
    dims2 = new_shape[0] * new_shape[1]

    if dims1 != dims2:
        reshaped_matrix = []
    else:
        reshaped_matrix = np.zeros((new_shape[0],new_shape[1]))
        flattened_a = np.array(a).flatten()

        for index in range(len(flattened_a)):
            row = index // len(a[0])
            col = index % len(a[0])

            element = a[row][col]

            new_row = index // len(reshaped_matrix[0])
            new_col = index % len(reshaped_matrix[0])

            reshaped_matrix[new_row][new_col] = element

    return reshaped_matrix


arr1 = [[1,2,3],
        [2,2,2],
        [3,3,3],
        [4,4,4]]

res = np.array(reshape_matrix(arr1, (3,4)))
print(res)


