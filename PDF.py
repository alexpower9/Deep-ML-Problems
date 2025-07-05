import math

def normal_pdf(x, mean, std_dev):

    term1 = 1 / (std_dev * math.sqrt(2 * math.pi))
    term2 = math.pow(math.e, (-1) * ((math.pow((x-mean), 2))/(2*(math.pow(std_dev, 2)))))
    val = term1 * term2

    return round(val,5)

x = 16
mean = 15
std_dev = 2.04
print(normal_pdf(x, mean, std_dev))