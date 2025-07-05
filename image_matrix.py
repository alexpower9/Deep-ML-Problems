import numpy as np

def matrix_image(A):
	# Write your code here
    new_mat = A.copy()
    #convert A to RREF, record pivot columns, then take those from the original matrix
    indicies = []


    for row in range(len(A)):
        for col in range(len(A[0])):
            if row == col: #meaning we have the leading number
                lead_number = new_mat[row][col]
                
                if lead_number == 0:
                    break

                if lead_number != 1:
                    cur_row = new_mat[row]
                    cur_row /= lead_number
                    new_mat[row] = cur_row 

                indicies.append(col)
                #Now we need to take all the values in the other rows and make the first index 0
                for next_row in range(len(A)): #now check against all the other rows
                     if next_row != row: #do not check the pivot row against itself
                         new_mat[next_row] = new_mat[next_row] - new_mat[next_row][col] * new_mat[row]
    
    vector_matrix = [[0 for _ in range(len(indicies))] for _ in range(len(A))]
    #we now have the indices by column
    for row in range(len(A)):
        for col in range(len(A[0])):
            if col in indicies:
                vector_matrix[row][col] = A[row][col]

    vector_matrix = np.array(vector_matrix).astype(int).tolist()


    return vector_matrix

matrix = np.array([[1,2,3],
          [4,5,6],
          [7,8,9]], dtype=np.float64)

print(matrix_image(matrix))