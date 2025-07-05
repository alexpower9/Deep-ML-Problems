import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
    #code goes here
    m, n = X.shape
    weights = weights.reshape(-1,1)
    y = y.reshape(m, 1)

    #So we should not shuffle the data here, but need to figure out the batching
    #like could be done with nested function to make the code easier. 

    """
        Batch: Calculate the gradient with all of the training data (slow but smooth)
        Stochastic: Use just one random data point (Fast but jittery)
        mini-batch: Update after a small batch (depending on what the batch size is)
    """

    if method == 'batch':
        batch_size = len(X)

    for i in range(n_iterations):
        for j in range(0, m, batch_size):
            #get batch
            if m % batch_size != 0:
                print("There is a big issue.")
            X_train = X[j : j + batch_size]
            y_train = y[j: j + batch_size]

            y_pred = np.dot(X_train, weights)
            
            #now get the error
            error = y_pred - y_train
            
            batch_size_actual = len(X_train)
            gradient = (1 / batch_size_actual) * np.dot(np.transpose(X_train), error)
            weights = weights - learning_rate * gradient

    return np.round(weights.flatten(), 4)

# Sample data
X = np.array([[1, 1], [2, 1], [3, 1], [4, 1]])
y = np.array([2, 3, 4, 5])

# Parameters
learning_rate = 0.01
n_iterations = 1000
batch_size = 2

# Initialize weights
weights = np.zeros(X.shape[1])



# Test Batch Gradient Descent
final_weights = gradient_descent(X, y, weights, learning_rate, n_iterations, method='batch')
print(final_weights)
# Test Stochastic Gradient Descent
final_weights = gradient_descent(X, y, weights, learning_rate, n_iterations, method='stochastic')
print(final_weights)
# Test Mini-Batch Gradient Descent
final_weights = gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size, method='mini_batch')
print(final_weights)


