import numpy as np


"""
	For the LSTM, there are a fixed number of weight thanks to the gates that are fixed. Each of these gates has a weight matrix for the input, a weight matrix
	for the hidden state, and a bias vector b
	ForgetGate: 
	InputGate:
	Cell/Candidate Gate:
	Output Gate:
	
"""
class LSTM:
    def __init__(self, input_size, hidden_size):
        self.input_size = input_size
        self.hidden_size = hidden_size

		# Initialize weights and biases
		# Wf - weight matrix for forget gate
		# Wi - weight matrix for input gate
		# Wc - weight matrix for cell candidate
		# Wo - weight matrix for output gate
        self.Wf = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wi = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wc = np.random.randn(hidden_size, input_size + hidden_size)
        self.Wo = np.random.randn(hidden_size, input_size + hidden_size)

		# and then these are the biases for those listed above. 
        self.bf = np.zeros((hidden_size, 1))
        self.bi = np.zeros((hidden_size, 1))
        self.bc = np.zeros((hidden_size, 1))
        self.bo = np.zeros((hidden_size, 1))

    def forward(self, x, initial_hidden_state, initial_cell_state):
        """
        Processes a sequence of inputs and returns the hidden states, final hidden state, and final cell state.
        Hidden state = short term memory
        """
        hidden_states = [] 

        for i in range(len(x)):

            x_i = x[i].reshape(self.input_size, 1)
            z = np.vstack((initial_hidden_state, x_i))

            # this vec combines the input and and the hidden state together, as each of the Weight matrices have the weights already
            # we first begin with the forget gate
            fg_value = self.sigmoid((np.dot(self.Wf, z)) + self.bf)

            # Placeholder for cell state update (fix variable name and logic as needed)
            initial_cell_state = initial_cell_state * fg_value

            # in the video, the left is the input gate, right side is candidate
            inp_value = self.sigmoid((np.dot(self.Wi, z)) + self.bi)
            cand_value = self.tanh((np.dot(self.Wc, z)) + self.bc)
            aggregate_val = inp_value * cand_value
            
            # Update the cell state with input and candidate values
            initial_cell_state += aggregate_val

            #now do the output gate
            output_value = self.sigmoid( (np.dot(self.Wo, z)) + self.bo)

            initial_hidden_state = output_value * self.tanh(initial_cell_state)

            hidden_states.append(initial_hidden_state)
            
        return hidden_states, initial_hidden_state, initial_cell_state

	# apply the sigmoid activate function
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def tanh(self, x):
        return np.tanh(x)


def main():
	input_sequence = np.array([[1.0], [2.0], [3.0]])
	initial_hidden_state = np.zeros((1, 1))
	initial_cell_state = np.zeros((1, 1))
	
	lstm = LSTM(input_size=1, hidden_size=1)
	final_h, h, o = lstm.forward(input_sequence, initial_hidden_state, initial_cell_state)

	print(h)

main()