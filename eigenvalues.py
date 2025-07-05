import numpy as np
import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	
    eigenvalues = []

    #so basically we have the ad - bc, then use quadratic formula
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]

    #now we just need the a, b and c terms to perform the quadratic equation (assume the roots are real numbers)
    a_1 = 1 #always 1
    b_1 = (-1*a) + (-1*d) 
    c_1 = (a * d) - (b*c)

    def quadratic_formula(a, b, c):
        answer1 = ( ((-1 * b) + math.sqrt((b ** 2) - (4*a*c))) / (2*a))
        answer2 = ( ((-1 * b) - math.sqrt((b ** 2) - (4*a*c))) / (2*a))

        return answer1, answer2
    
    for value in quadratic_formula(a_1, b_1, c_1):
        eigenvalues.append(value)

    return eigenvalues

matrix = [[2,1],[1,2]]
res = calculate_eigenvalues(matrix)

print(res)