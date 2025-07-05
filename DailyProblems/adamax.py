import numpy as np

def adamax_optimizer(parameter, grad, m, u, t, learning_rate=0.002, beta1=0.9, beta2=0.999, epsilon=1e-8):
    """
    Update parameters using the Adamax optimizer.
    Adamax is a variant of Adam based on the infinity norm.
    It uses the maximum of past squared gradients instead of the exponential moving average.
    Args:
        parameter: Current parameter value
        grad: Current gradient
        m: First moment estimate
        u: Infinity norm estimate
        t: Current timestep
        learning_rate: Learning rate (default=0.002)
        beta1: First moment decay rate (default=0.9)
        beta2: Infinity norm decay rate (default=0.999)
        epsilon: Small constant for numerical stability (default=1e-8)
    Returns:
        tuple: (updated_parameter, updated_m, updated_u)
    """
    if isinstance(parameter, (float, int)):
        m = beta1*m + (1 - beta1)*grad 
        u = np.maximum(beta2*u, np.abs(grad))

        parameter = parameter - (learning_rate / (u + epsilon))*m
    else:
        for i in range(len(parameter)):
            m[i] = beta1*m[i] + (1 - beta1)*grad[i]
            u[i] = np.maximum(beta2*u[i], np.abs(grad[i])) 

            #NEED TO ADD BIAS TERM
            parameter[i] = parameter[i] - (learning_rate / (u[i] + epsilon))*m[i] 


    return np.round(parameter, 5), np.round(m, 5), np.round(u, 5)

print(adamax_optimizer(np.array([1., 2.]), np.array([0.0, 0.0]), np.array([0.1, 0.1]), np.array([0., 0.]), 1, 0.002, 0.9, 0.999, 1e-8))