import math


"""
    defined as σ(z) = 1 / (1 + exp(-z)).
"""
def sigmoid(z:float) -> float:
    return round(1 / (1 + math.exp(-z)), 4)

z = 0
res = sigmoid(z)

print(res)