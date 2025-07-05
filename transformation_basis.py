import math

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    
    #So we need to make the matrix [C | I] then row reduce, and the matrix on the 
    #LHS of | will be our matrix P and B is our identity matrix
    length = len(C)

    for row in range(length):
        for col in range(length):
            C[row].append(B[row][col])

    result = C.copy()
    
    #Now we begin to row reduce C
    for row in range(length):
        for col in range(len(C[0])):
            if row == col:
                lead_number = result[row][col]

                if lead_number == 0:
                    break

                #if not, we need to divide all elements in that row by the lead number
                if lead_number != 1:
                    curr_row = result[row]
                    for i in range(len(curr_row)):
                        curr_row[i] = curr_row[i] / lead_number
                    result[row] = curr_row

                #now the row is fixed and we need to do
                """ Now that the row has been divided, we need to:
                    Multiply the current row by the value corresponding to row col in the other row
                    and then subtract the other row by our new one
                """
                for next_row in range(len(C)):
                    if next_row != row: #so we dont compared row to itself obviously
                        scalar = result[next_row][col]
                        current_row = result[row].copy()
                        for i in range(len(current_row)):
                            current_row[i] *= scalar

                        #now we have to do result[next_row] - current_row
                        for i in range(len(current_row)):
                            result[next_row][i] -= current_row[i]

    #now just loop again and do the round
    final_mat = [[0 for _ in range(len(result))] for _ in range(len(result[0]) // 2)]

    for i in range(len(result)):
        for j in range(len(result[0]) // 2):
            result[i][j + len(result[0]) // 2] = round(result[i][j + len(result[0]) // 2], 4)
            final_mat[i][j] = result[i][j + len(result[0]) //2]

    return final_mat
             







B = [[1, 0, 0], 
             [0, 1, 0], 
             [0, 0, 1]]
C = [[1, 2.3, 3], 
             [4.4, 25, 6], 
             [7.4, 8, 9]]
result = transform_basis(B, C)
print(result)


