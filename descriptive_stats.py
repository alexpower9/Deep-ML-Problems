import numpy as np
import math

def descriptive_statistics(data):
	
    new_data = np.array(data)

    #mean
    mean = np.mean(new_data)
    median = np.median(new_data)
    
    prev_count = 0
    most_common = 0
    mode = 0
    for i in range(len(new_data)):
        num = new_data[i]
        for j in range(len(new_data)):
            if new_data[j] == num:
                most_common += 1
        if most_common > prev_count:
            prev_count = most_common
            mode = num
        most_common = 0

    


    variance = np.var(new_data)
    std_dev = math.sqrt(variance)
    
    percentiles = []
    num = 25
    while True:
        if num > 75:
            break 
        percentiles.append(np.percentile(new_data, num))
        num += 25
    iqr = percentiles[2] - percentiles[0]
        

    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
    return stats_dict

res = descriptive_statistics([10, 20,20,20, 30, 40, 50])

print(res)

