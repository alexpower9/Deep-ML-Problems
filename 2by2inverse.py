def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    if ((a*d) - (b*c) == 0):
        return None
    else:
        inverse = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        print(inverse)
        factor = 1 / ((a*d) - (b*c))

        inverse[0][0] = factor * d 
        inverse[0][1] = factor * (-1 * b)
        inverse[1][0] = factor * (-1 * c)
        inverse[1][1] = factor * a 

    return inverse

matrix = [[4, 7], [2, 6]]
result = inverse_2x2(matrix)

print(result)