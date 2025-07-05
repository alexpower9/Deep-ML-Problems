import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1,
     learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
    
    n_samples, n_features = X.shape
    weights = np.zeros((n_features,1))
    y = y.reshape(n_samples, 1)
    bias = 0
    """
        We want to find the weights that minimize the Lasso Objective function.
        The whole point is to drive weights towards 0, adding the weights to the loss calculation
        effectively penalizing the model for high weights
    """
    for i in range(max_iter):
        #so we have a MSE term, and a l1 penalty
        y_pred = np.dot(X, weights) + bias

        mse_grad = (1 / n_samples) * np.dot(np.transpose(X), (y_pred - y)) 
        l1_penalty = np.sign(weights)

        full_weight_grad = mse_grad + alpha * l1_penalty

        #now update the weight and bias
        weights = weights - (learning_rate * full_weight_grad)
        bias -= learning_rate * (1 / n_samples) * np.sum(y_pred - y)

    
    return weights.flatten(), bias

X = np.array([[0, 0], [1, 1], [2, 2]])
y = np.array([0, 1, 2])

alpha = 0.1
weights, bias = l1_regularization_gradient_descent(X, y, alpha=alpha, learning_rate=0.01, max_iter=1000)
print(weights, bias)