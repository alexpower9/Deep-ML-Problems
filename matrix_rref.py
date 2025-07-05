import numpy as np

def rref(matrix):
    mat = matrix.copy().astype(float)

    for row in range(len(mat)):
        flag = False
        for col in range(len(mat[0])):
            if row == col: #means the row and columns are mixed up
                lead_number = mat[row][col]

                #so this handles the swapping
                if lead_number == 0:
                    #find row where element in the column is not zero swap
                    break_occured = False
                    for swap_row in range(len(mat)):
                        for swap_col in range(len(mat[0])):
                            if swap_row > row and mat[swap_row][col] != 0:
                                temp_row = mat[row].copy()
                                mat[row] = mat[swap_row]
                                mat[swap_row] = temp_row
                                lead_number = mat[row][col]
                                break_occured = True
                                print("Did a row swap.")
                                break
                            elif swap_row > row and mat[row][swap_col] != 0:
                                flag = True
                                lead_number = mat[row][swap_col]
                                break_occured = True
                                print(f"No rows to swap with found. Now making lead number: {lead_number}")
                                break
                        if break_occured:
                            break 
                    if not break_occured:
                        return mat
                        
                if lead_number != 1:
                    curr_row = mat[row]
                    curr_row /= lead_number
                    mat[row] = curr_row
                
                #now current row has been fixed, we check against other rows and fix those
                for other_row in range(len(mat)):
                    if other_row != row:
                        column_to_use = col if flag == False else swap_col
                        mat[other_row] = mat[other_row] - mat[other_row][column_to_use] * mat[row]

                print(f"After {row}, the matrix is now {mat}\n")

    return mat 

# matrix = np.array([ [1, 2, -1], [2, 4, -1], [-2, -4, -3]])
matrix = np.array([ [2, 4, -2], [4, 9, -3], [-2, -3, 7] ])

                  

rref_matrix = rref(matrix)
print(rref_matrix) 