import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    
    result = []
    if y is None:
        #so we should loop through x at 0, increasing by batch size 
        for i in range(0, len(X), batch_size):
            result.append([X[i:i+batch_size]])
    else:
        for i in range(0, len(X), batch_size):
            result.append([X[i:i+batch_size], y[i:i+batch_size]])

    return result

X =     np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
result = batch_iterator(X, y, batch_size)

print(result)

#output should be [[[[1, 2], [3, 4]], [1, 2]],
    #  [[[5, 6], [7, 8]], [3, 4]],
    #  [[[9, 10]], [5]]]