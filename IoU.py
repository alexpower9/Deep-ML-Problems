import numpy as np

def compute_mask_iou(mask1, mask2):
    #IoU = Intersection area / union area
    intersection = 0
    union = 0
    
    for i in range(len(mask1)):
        for j in range(len(mask2)):
            if mask1[i][j] == 1 and mask2[i][j] == 1:
                intersection += 1
            if mask1[i][j] == 1 or mask2[i][j] == 1:
                union += 1
    
    if union == 0:
        return 0.0
    
    return intersection / union 

print(compute_mask_iou(np.array([[1, 0], [0, 1]]), np.array([[1, 0], [0, 1]])))