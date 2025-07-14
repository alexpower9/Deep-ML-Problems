import numpy as np

def get_random_subsets(X, y, n_subsets, replacements=True, seed=42):
    # Your code here
    rng = np.random.default_rng(seed)
    result = []
    for i in range(n_subsets):
        size = len(X) // 2 if replacements == False else len(X)
        indices = rng.choice(len(X), size=size, replace=replacements)
        X_subset = X[indices]
        y_subset = y[indices]
        result.append([X_subset, y_subset])
        
    return result 
        
    
    


X = np.array([[1, 1], [2, 2], [3, 3], [4, 4]]) ;y = np.array([10, 20, 30, 40])
print(get_random_subsets(X, y, 1, True, seed=42))
