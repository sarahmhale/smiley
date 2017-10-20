import numpy as np
class Neuron:
    """
    Purpose:    Initiates the neuron and sets all the attributes.
    Input:      weights: [0,0.1,0.2 .....]
                learningRate: a int or double
    """
    def __init__(self, weights, learningRate):
        self.learningRate = learningRate
        self.weights = weights
        self.output = 0
        self.inputs = []
        self.error = 0

    """
    Purpose:    Get a value between 0 and 1
    Input:      a double
    Output:     a double
    """
    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    """
    Purpose:    Get's the neurons output and saves it.
    Input:      [0,0.1,0.2 .....]
    Output:     a double
    Comment:    Uses the sigmoid and summationUnit function to calculate the
                output.
    """
    def feedForward(self,inputs):
        self.output = self.sigmoid(self.summationUnit(inputs))
        return self.output

    """
    Purpose:    Sums all of the inputs multipled by the corresponding weight.
    Input:      [0,0.1,0.2 .....]
    Output:     a double
    """
    def summationUnit(self,inputs):
        self.inputs = inputs
        return np.dot(inputs, self.weights)
    """
    Purpose:    Updates the weights of the neuron.
    Input:      a int
    comment:    For the network to work the input int should be either 0 or 1.
    """
    def updateWeights(self,target_output):
        self.calculateError(target_output)
        i = 0
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i]+ (self.learningRate * self.error * self.inputs[i])
            i=i+1
    """
    Purpose:    calculates the difference between the target_output and the
                neurons output.
    Input:      a int
    comment:    For the network to work the input int should be either 0 or 1.
    """
    def calculateError(self,target_output):
        self.error = (target_output - self.output)
