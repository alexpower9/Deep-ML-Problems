import numpy as np

def adam_optimizer(f, grad, x0, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8, num_iterations=10):
    
    """
    f: The objective function to be optimized
    grad: A function that computes the gradient of f
    x0: Initial parameter values
    learning_rate: The step size (default: 0.001)
    beta1: Exponential decay rate for the first moment estimates (default: 0.9)
    beta2: Exponential decay rate for the second moment estimates (default: 0.999)
    epsilon: A small constant for numerical stability (default: 1e-8)
    num_iterations: Number of iterations to run the optimizer (default: 1000)
    """
    #init momentums
    m_0 = 0
    v_0 = 0
    t = 1

    for i in range(num_iterations):
        gradient = grad(x0)
        m_t = beta1 * m_0 + (1 - beta1)*gradient
        v_t = beta2 * v_0 + (1 - beta2)*(gradient ** 2)

        #now set m_0 and v_0 to be the old values
        m_0 = m_t 
        v_0 = v_t 

        m_pred = m_t / (1 - beta1**t) 
        v_pred = v_t / (1 - beta2**t)
        t += 1

        x0 = x0 - learning_rate * ( (m_pred) / (np.sqrt(v_pred) + epsilon) )

    return x0


def objective_function(x):
    return x[0]**2 + x[1]**2

def gradient(x):
    return np.array([2*x[0], 2*x[1]])

x0 = np.array([1.0, 1.0])
x_opt = adam_optimizer(objective_function, gradient, x0)

print("Optimized parameters:", x_opt)