import numpy as np

#ridge loss combines the MSE and a regularization term (penalizing large weights)
def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    #first do the mse term
    mse_part = np.square(np.subtract(y_true, np.dot(X, w.T))).mean()

    #now get squared L2 norm of weights
    l2_norm = np.sum(np.square(w)) * alpha
    
    return mse_part + l2_norm

X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
w = np.array([0.2, 2])
y_true = np.array([2, 3, 4, 5])
alpha = 0.1

loss = ridge_loss(X, w, y_true, alpha)
print(loss)
    