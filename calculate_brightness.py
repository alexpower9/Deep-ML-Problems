def calculate_brightness(img):
    if len(img) == 0:
        return -1
    
    running_sum = 0
    total_count_values = len(img) * len(img[0])
    cols = len(img[0])

    for i in range(len(img)):
        row = img[i]
        col_length = len(row)

        if cols != col_length:
            return -1
        else:
            for j in range(col_length):
                if row[j] > 255 or row[j] < 0:
                    return -1
                else:
                    running_sum += row[j]

    return round(running_sum / total_count_values, 2)

            

img = [
    [100, 200],
    [50, 150]
]
print(calculate_brightness(img))