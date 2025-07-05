import numpy as np

def orthogonal_projection(v, L):
    """
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
    
	"""
    #projection is defined as:
    # ((v dot j) / (J dot J)) * J

    def get_dot_product(v, L):
        value = 0

        for i in range(len(v)):
            value += (v[i] * L[i])
        return value 

    result_vec = [] 
    top_value = get_dot_product(v, L)
    bottom_value = get_dot_product(L, L)

    scalar = top_value / bottom_value


    #now do the result scaled by J
    for i in range(len(L)):
        L[i] = L[i] * scalar
    
    return L

v = [3, 4]
L = [1, 0]
print(orthogonal_projection(v, L))

