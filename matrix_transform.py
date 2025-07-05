import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	
    if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
        return -1
    
    try:

        a_times_s = np.dot(A, S)
        t_inverted = np.linalg.inv(T)

        transformed_matrix = np.dot(t_inverted, a_times_s)
    except Exception as e:

        return -1
    


    return transformed_matrix


A = [[1,2],[3,4]]
T = [[2,0], [0,2]]
S = [[1,1], [0,1]]

result = transform_matrix(A, T, S)
print(result)


