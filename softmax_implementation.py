import math

"""
    Softmax converts a list of values into probability distribution
    They are proportional to the exponential of each element divided by the sum
    of the exponentials of all elements in the list

    Defined as: softmax(z_i) = e^(z_i) / (sum of all e^(z_i))
"""
def softmax(scores: list[float]) -> list[float]:
    results = [] #just append to this as we go
    
    sum_of_all = 0
    #first get the bottom term of the formula, the summation
    for element in scores:
        sum_of_all += math.pow(math.e, element)

    #now append the values
    for element in scores:
        results.append(round(math.pow(math.e, element) / sum_of_all, 4))

    return results 

results = softmax([1,2,3])

print(results)

