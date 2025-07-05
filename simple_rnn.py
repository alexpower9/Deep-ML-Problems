import numpy as np

def rnn_forward(input_sequence: list[list[float]], initial_hidden_state: list[float], Wx: list[list[float]], Wh: list[list[float]], b: list[float]) -> list[float]:
    
    def tanh_activation(v):
        return np.tanh(v)
    
    final_hidden_state = np.array(initial_hidden_state).reshape(-1, )
    for i in range(len(input_sequence)):
        new_input = np.array(input_sequence[i]).flatten()

        final_hidden_state = tanh_activation( (np.dot(Wx, new_input)) + (np.dot(Wh, final_hidden_state)) + b)
    
    return np.round(final_hidden_state, 4)

input_sequence = [[1.0], [2.0], [3.0]]  # Use regular Python lists
initial_hidden_state = [0.0]            # Use regular Python list
Wx = [[0.5]]                            # Use regular Python list
Wh = [[0.8]]                            # Use regular Python list
b = [0.0]     

res = rnn_forward(input_sequence, initial_hidden_state, Wx, Wh, b)

print(res)