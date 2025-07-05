import numpy as np

def dice_score(y_true, y_pred):
    #result ranges from 0 (no overlap) to 1 (perfect)
    #handle cases where no true values exist or predicted positives

    #formula is ( 2 * num of elements intersecting) / (2 * num of elements intersecting + false positives + false negatives)
    
    true_positives = 0
    false_positives = 0
    false_negatives = 0

    for i in range(len(y_pred)):
        if y_true[i] == 1 and y_pred[i] == 1:
            true_positives += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            false_negatives += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            false_positives += 1

    if true_positives == 0:
        return 0.0    

    res = (2 * true_positives) / (2 * true_positives + false_positives + false_negatives)

    return round(res, 3)


y_true = np.array([1, 1, 0, 1, 0, 1])
y_pred = np.array([1, 1, 0, 0, 0, 1])
print(dice_score(y_true, y_pred))