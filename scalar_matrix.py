import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

    result = matrix.copy()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = matrix[i][j] * scalar

    return result


matrix = [[1,2,3],
          [4,5,6]]

res = scalar_multiply(matrix, 2)
print(res)