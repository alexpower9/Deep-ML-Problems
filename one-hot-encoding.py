import numpy as np

def to_categorical(x, n_col=None):
    # Your code here

    number_of_cols = len(np.unique(x)) if n_col is None else n_col
    id_mat = np.eye(number_of_cols)
    result = np.zeros((len(x), number_of_cols))

    for i in range(len(x)):
        result[i] = id_mat[x[i]]

    # if n_col is None:
    #     number_of_cols = len(np.unique(x))
    #     identity_matrix = np.eye(number_of_cols)
    #     result = np.zeros((len(x), number_of_cols))

    #     for i in range(len(x)):
    #         result[i] = identity_matrix[x[i]]
    # else:
    #     identity_matrix = np.eye(n_col)
    #     result = np.zeros((len(x), n_col))

    #     for i in range(len(x)):
    #         result[i] = identity_matrix[x[i]]

    return result
	
x = np.array([0, 1, 2, 1, 0])
output = to_categorical(x)
print(output)