import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape
    padded_input = np.pad(input_matrix, pad_width=padding, mode='constant', constant_values=0) if padding != 0 else input_matrix
    # Your code here
    # only count the input where the kernel fully fits the padded input
    # Use the formulas to determine the shape of the output matrix
    # height = floor( (h_in + 2P - h_k) / S ) + 1
    output_height = np.floor( (input_height + 2*padding - kernel_height) / stride ) + 1
    output_width = np.floor ((input_width + 2*padding - kernel_width) / stride) + 1
    output_matrix = np.zeros((output_height.astype(int), output_width.astype(int)))
    

    #now we do the convolution
    for i in range(len(output_matrix)):
        for j in range(len(output_matrix[0])):
            start_row = i * stride 
            start_col = j * stride 
            relevant_section = padded_input[start_row:start_row + kernel_height, start_col:start_col+kernel_width]
            output_value = np.sum(relevant_section * kernel)
            output_matrix[i][j] = output_value

    return output_matrix



input_matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])



kernel = np.array([
    [1, 0],
    [-1, 1]
])

padding = 1
stride = 2

output = simple_conv2d(input_matrix, kernel, padding, stride)
print(output)