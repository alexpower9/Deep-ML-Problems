import math

def binomial_probability(n, k, p):
    term1 = math.comb(n,k)
    term2 = pow(p, k)
    term3 = pow((1 - p), (n - k))
    prob = term1 * term2 * term3

    return round(prob, 5)

test = binomial_probability(6,2,0.5)
print(test)