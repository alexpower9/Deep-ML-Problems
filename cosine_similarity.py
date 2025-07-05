import numpy as np

def cosine_similarity(v1, v2):
    #equation is (dot product between v1 and v2 / their magnitudes)
    dot_product = np.dot(v1, v2)
    norm_1 = np.linalg.norm(v1)
    norm_2 = np.linalg.norm(v2)

    return round(dot_product / (norm_1 * norm_2),3)

v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))