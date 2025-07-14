import numpy as np

def shuffle_data(X, y, seed=None):
	#Use LCG to for pseduo random number generation
	#use fisher yates to perform the shuffling

	#so we need to generate random numbers in the range 0 to len
	#of X / y, start at the back, generate a random index, then swap with that index.
	
	rng = np.random.default_rng(seed) if seed is not None else np.random.default_rng()
	indicies = rng.permutation(len(X))
	X_shuffled = X[indicies]
	y_shuffled = y[indicies]

	return X_shuffled, y_shuffled

print(shuffle_data(np.array([[1, 1], [2, 2], [3, 3], [4, 4]]), np.array([10, 20, 30, 40]), seed=24))