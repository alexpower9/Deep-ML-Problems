import numpy as np

def divide_on_feature(X, feature_i, threshold):
    # I feel like we can ge the indices where the threshold is true
    # then the others would be where it is not true and return those directly
    bool_mask = X[:,feature_i] >= threshold
    print(bool_mask)
    return X[bool_mask], X[~bool_mask]

X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
feature_i = 0
threshold = 5

print(divide_on_feature(X, feature_i=feature_i, threshold=threshold))