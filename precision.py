import numpy as np

def precision(y_true, y_pred):
    true_positives = 0
    false_positives = 0

    #precision = TP / (TP + FP)
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            true_positives += 1
        elif y_true[0] == 0 and y_pred[i] == 1:
            false_positives += 1
    
    print(f"True positives: {true_positives}")
    print(f"false_positives: {false_positives}")
    return (true_positives / (true_positives + false_positives)) 

y_true = np.array([1, 0, 1, 1, 0, 0])
y_pred = np.array([1, 0, 0, 0, 0, 1])

result = precision(y_true, y_pred)
print(result)

