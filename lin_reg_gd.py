import numpy as np

"""
    So we are training weights using gradient descent. The regression model is y = Xθ
	
    For each iteration, we are simply making a prediction with the formula above, computing the error, 
	compute the gradient of the error with respect to theta and then update theta?
"""
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape 
    theta = np.zeros((n, 1))
    y = y.reshape(m, 1)

    for i in range(iterations):
        y_pred = np.dot(X, theta) #mat mul

        error = y_pred - y 
        
        #now compute the gradient of the MSE with respect to theta
        gradient = (1 / m) * np.dot(np.transpose(X), error)
        theta = theta - alpha * gradient

    theta = np.round(theta, decimals=4)
    return theta



X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000
result = linear_regression_gradient_descent(X, y, alpha, iterations)

print(result)
