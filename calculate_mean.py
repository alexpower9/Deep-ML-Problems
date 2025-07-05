import numpy as np

#so accept either row or column
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
    means = []

    if mode == 'row':
        
        for row in range(len(matrix)):
            summation = 0
            for column in range(len(matrix[0])):
                summation += matrix[row][column]
            final = float(summation / len(matrix))
            means.append(final)

    else: #so column
        for col in range(len(matrix[0])):
            summation = 0
            for row in range(len(matrix)):
                summation += matrix[row][col]
            final = float(summation / len(matrix))
            means.append(final)
    return means

matrix = np.array([[1,2,3],
				   [4,5,6]])

res = calculate_matrix_mean(matrix, 'column')
print(res)