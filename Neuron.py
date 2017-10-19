import numpy as np
class Neuron:
    """
    Purpose:
    Input:
    Output:
    """
    def __init__(self, weights, learningRate):
        self.learningRate = learningRate
        self.weights = weights
        self.output = 0
        self.inputs = []
        self.error = 0

    """
    Purpose:
    Input:
    Output:
    """
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    """
    Purpose:
    Input:
    Output:
    """
    def feedForward(self,inputs):
        self.output = self.sigmoid(self.summationUnit(inputs))
        return self.output

    """
    Purpose:
    Input:
    Output:
    """
    def summationUnit(self,inputs):
        self.inputs = inputs
        return np.dot(inputs, self.weights)
    """
    Purpose:
    Input:
    Output:
    """
    def updateWeights(self,target_output):
        self.calculateError(target_output)
        i = 0
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i]+ (self.learningRate * self.error * self.inputs[i])
            i=i+1
    """
    Purpose:
    Input:
    Output:
    """
    def calculateError(self,target_output):
        self.error = (target_output - self.output)
