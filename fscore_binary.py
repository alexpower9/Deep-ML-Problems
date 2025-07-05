import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task.

    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: The weight of precision in the harmonic mean
    :return: F-Score rounded to three decimal places
    """
    #so the f scores is given as:
    # f = (1 + beta^2) * (precision * recall) / (beta^2) * precision + recall
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

    precision = true_positives / (true_positives + false_positives)
    recall = true_positives / (true_positives + false_negatives)




    return round(( (1 + beta**2) * ( (precision * recall) / ((beta**2 * precision) + recall) ) ), 3)

y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
beta = 1

print(f_score(y_true, y_pred, beta))