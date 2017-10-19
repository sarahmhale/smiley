import numpy as np
class Neuron:
    def __init__(self, weights):
        self.learningRate = 0.1
        self.weights = weights[0]

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def feedForward(self,inputs):
        self.output = self.sigmoid(self.summationUnit(inputs))
        return self.output
    #summan av alla input * vikt
    def summationUnit(self,inputs):
        self.inputs = inputs
        return np.dot(inputs, self.weights)

    def updateWeights(self,target_output):
        self.calculateError(target_output)
        i = 0
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i]+ (self.learningRate * self.error * self.inputs[i])
            i=i+1

    def calculateError(self,target_output):
        self.error = (target_output - self.output)
