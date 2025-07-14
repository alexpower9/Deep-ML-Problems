import numpy as np

def calculate_f1_score(y_true, y_pred):
    true_positives = 0
    false_positives = 0
    false_negatives = 0


    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            true_positives += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            false_negatives += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            false_positives += 1
            
    if true_positives == 0 and false_negatives == 0:
        return 0.0

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)
    
    round( 2 * ((precision * recall) / (precision + recall)) ,3)
    
print(calculate_f1_score([0, 0, 0, 0], [1, 1, 1, 1]))