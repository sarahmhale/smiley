from Neuron import Neuron
from random import random
class Layer:
    def __init__(self,num_neurons):
        self.bias = random()
        self.neurons = []

        for i in range(num_neurons):
            self.neurons.append(Neuron(self.bias))

    def feedForward(self,inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.calculateOutput(inputs))
        return outputs
