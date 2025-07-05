import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> tuple[list[float], float]:

    #first define sigmoid function
    def sigmoid(v):
        new_vec = []

        for value in v:
            new_vec.append(round(1 / (1 + math.exp(-value)),4))

        return new_vec

    def mse(v):
        #this will be taking in the result of the sigmoid function
        summation = 0
        #the error is defined as the average squared difference between each predicted prob and the true value
        #do the loop part
        for i in range(len(v)):
            summation += math.pow(v[i] - labels[i], 2)

        return (1/len(v)) * summation 
    
    #multiply feature by each weight, then add bias at the end and append it
    results = [] 
    for feature in features:
        num = 0
        for i in range(len(feature)):
           num += feature[i] * weights[i]
        num += bias

        results.append(num)

    #now activate results
    probabilities = sigmoid(results)
    mse = mse(probabilities)

    return probabilities, mse

features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1

probs, loss = single_neuron_model(features, labels, weights, bias)

print(probs, loss)

