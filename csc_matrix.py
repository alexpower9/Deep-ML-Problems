import numpy as np

def compressed_col_sparse_matrix(dense_matrix):
    #define lists we need
    values = []
    row_indices = []
    column_pointer = [0]

    counter = 0

    for col in range(len(dense_matrix[0])):
        for row in range(len(dense_matrix)):
            if dense_matrix[row][col] != 0:
                values.append(dense_matrix[row][col])
                row_indices.append(row)
                counter += 1
        column_pointer.append(counter)

    return (values, row_indices, column_pointer)


dense_matrix = [
    [0, 0, 3, 0],
    [1, 0, 0, 4],
    [0, 2, 0, 0]
]

vals, row_idx, col_ptr = compressed_col_sparse_matrix(dense_matrix)
print(vals, row_idx, col_ptr)

