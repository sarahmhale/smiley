from math import exp
class Neuron:
    def __init__(self,bias):
        self.learningRate = 0.5
        self.bias = bias
        self.weights = []
    def sigmoid(self, x):
        return 1/(1+exp(-x))

    def summationUnit(self,inputs):
        netValue = 0
        for i in range(len(inputs)):
            netValue += inputs[i] * self.weights[i]
        return netValue
    def newBias(self):
        self.bias = self.bias + learningRate * 1 * self.delta

    def updateFreeParameters(self):
        self.newBias()
        for weight in self.weights:
            weight = weight + self.learningRate * self.output* self.delta
        
    def calculateOutput(self, inputs):
        self.output = self.sigmoid(self.summationUnit(inputs)) + self.bias
        return self.output

    def output_layer_error(self,facit_output):
        self.delta = self.calculateDelta() * self.calculateOutPutError(facit_output)
        return self.delta

    def hidden_layer_error(self,output_layer):
        self.delta = self.calculateDelta() * self.calculateHiddenError(output_layer)
        return self.delta

    def calculateHiddenError(self,output_layer):
        i=0
        for neuron in output_layer:
            error = neuron.delta * self.weights[i]
            i = i+1
        return error

    def calculateOutPutError(self,facit_output):
        return facit_output - self.output

    def calculateDelta(self):
        return self.output * (1 - self.output)
