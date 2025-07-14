import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    predicted_probs = np.clip(predicted_probs, epsilon, 1 - epsilon)
    loss = -np.mean(np.sum(true_labels * np.log(predicted_probs), axis=1))
    
    return loss

predicted_probs = [[0.7, 0.2, 0.1], [0.3, 0.6, 0.1]]
true_labels = [[1, 0, 0], [0, 1, 0]]

loss = compute_cross_entropy_loss(predicted_probs, true_labels)
print(loss)