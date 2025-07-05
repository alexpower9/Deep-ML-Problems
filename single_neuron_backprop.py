import numpy as np
def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    #define sub functions
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    
    def mse_loss(X, y):
        return np.square(np.subtract(X, y)).mean()
    
    def mse_backward(X, y):
        return 2*(X - y) / X.shape[0]
    
    def sigmoid_backward(x,dvalues):
        return (x * (1 - x)) * dvalues
    
    def optimize(weights, biases, dweights, dbiases):
        new_weights = weights - learning_rate * dweights
        new_bias = biases - learning_rate * dbiases

        return new_weights, new_bias

    loss_values = []
    weights = initial_weights.copy()
    bias = initial_bias
    #so batch gradient descent
    for _ in range(0, epochs):
        z = np.dot(features, weights) + bias

        activated_values = sigmoid(z)
        loss = mse_loss(activated_values, labels)
        loss_values.append(loss.item())
        #now that we have the loss, lets do the backprop step.


        dvalues = mse_backward(activated_values, labels)
        dvalues = sigmoid_backward(activated_values,dvalues)
        dweights = np.dot(features.T, dvalues)
        dbiases = np.sum(dvalues, axis=0) #try with not keeping_dims
        
        weights, bias = optimize(weights, bias, dweights, dbiases)

    loss_values = [round(float(x),4) for x in loss_values]
    return np.round(weights, 4), np.round(bias, 4), loss_values

features = np.array([[1.0, 2.0], [2.0, 1.0], [-1.0, -2.0]])
labels = np.array([1, 0, 0])
initial_weights = np.array([0.1, -0.2])
initial_bias = 0.0
learning_rate = 0.1
epochs = 2

weights, bias, loss_values = train_neuron(features, labels, initial_weights, initial_bias, learning_rate, epochs)

print(f"Weights: {weights}")
print(f"Bias: {bias}")
print(f"Loss values: {loss_values}")


