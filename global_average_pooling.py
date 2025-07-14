import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
    # so takes in array of (height, width, channels), then returns an an array of shape (channels,)
    # where it takes the mean from each channel
    print(x)
    x = np.mean(x, axis=(0,1))
    return x
x = global_avg_pool(np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]))
print(x)