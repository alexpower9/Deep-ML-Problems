def matrixmul(a: list[list[int | float]], b: list[list[int | float]]) -> list[list[int | float]]:
    if len(a[0]) != len(b):
        return -1
    else:
        result = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

        for row in range(len(a)):
            for col in range(len(b[0])):
                for j in range(len(a[0])):
                    result[row][col] += a[row][j] * b[j][col]

    return result

				
A = [[1,2],[2,4]]
B = [[2,1],[3,4]]

res = matrixmul(A, B)
print(res)