import numpy as np

def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    #round intermediate solutions to 4 decimals, loop n times
    x = np.zeros(A.shape[0])

   
    diag_elements = np.diag(A)
    #so we know the first len(A[0]) - 1 elements are for x[i] and so on
    for _ in range(0, n):
        current_vals = x.copy() 

        for i in range(len(x)):
            relevant_others = np.concatenate([A[i][:i], A[i][i+1:]]) #vector of numbers we need for that row
            relevant_terms = np.concatenate([current_vals[:i], current_vals[i+1:]])
            x[i] = np.round( (b[i] - np.dot(relevant_others, relevant_terms)) / diag_elements[i], 4 )

            #print(f"To get x{i}, we divided by {diag_elements[i]}, then did the summation: {b[i]} - (dot product between {relevant_others} and {relevant_terms}). This ended with {x[i]}")
    return x


A = np.array([[5, -2, 3], [-3, 9, 1], [2, -1, -7]])
b = [-1, 2, 3]
n=2

result = solve_jacobi(A, b, n)
print(result)
