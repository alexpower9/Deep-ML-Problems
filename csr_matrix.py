import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	"""
	Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

	:param dense_matrix: 2D list representing a dense matrix
	:return: A tuple containing (values array, column indices array, row pointer array)
	"""

	values_array = []
	column_indices = []
	row_pointer = [0]
	
	counter = 0

	for i in range(len(dense_matrix)):
		for j in range(len(dense_matrix[0])):
			if dense_matrix[i][j] != 0:
				values_array.append(dense_matrix[i][j])
				column_indices.append(j)
				counter += 1
		row_pointer.append(counter)
	return (values_array, column_indices, row_pointer)


dense_matrix = [
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [3, 0, 4, 0],
    [1, 0, 0, 5]
]

vals, col_idx, row_ptr = compressed_row_sparse_matrix(dense_matrix)
print("Values array:", vals)
print("Column indices array:", col_idx)
print("Row pointer array:", row_ptr)

		