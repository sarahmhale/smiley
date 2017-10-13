from Layer import Layer
from random import random
class Network:
    def __init__(self, num_inputs, num_hidden, num_outputs):
        self.num_inputs = num_inputs

        self.hidden_layer = Layer(num_hidden)
        self.output_layer = Layer(num_outputs)

        self.weight_hidden_layer = self.init_weights(num_inputs, self.hidden_layer)
        self.weight_output_layer = self.init_weights(num_hidden, self.output_layer)

    def init_weights(self,num_of_neurons_layer_above, layer):
        for h in range(len(layer.neurons)):
            for i in range(num_of_neurons_layer_above):
                layer.neurons[h].weights.append(random())
        return layer

    def feedForward(self,inputs):
        return self.output_layer.feedForward(self.hidden_layer.feedForward(inputs))

    def printStructure(self):
        print "Hidden layer: "
        for neuron in self.hidden_layer.neurons:
            print "weight: ",neuron.weights
            print "bias: ",neuron.bias

        print "Output layer: "
        for neuron in self.output_layer.neurons:
            print "weight: ",neuron.weights
            print "bias: ",neuron.bias

        print "number of inputs neurons: ", self.num_inputs
        print "number of hidden neurons: ", len(self.hidden_layer.neurons)
        print "number of output neurons: ", len(self.output_layer.neurons)


    def updateFreeParameters(self):
        #hidden_layer
        for neuron in self.hidden_layer.neurons:
            neuron.updateFreeParameters()

        #output_layer
        for neuron in self.output_layer.neurons:
            neuron.updateFreeParameters()

    def calculateError(self, facit):
        #output_layer
        i = 0
        for neuron in self.output_layer.neurons:
            print "ERROR",neuron.output_layer_error(facit[i])
            i = i+1

        #hidden_layer
        for neuron in self.hidden_layer.neurons:
            neuron.hidden_layer_error(self.output_layer.neurons)

    def train(self,traning_set):
        self.feedForward(traning_set[0]['grid'])
        self.calculateError(traning_set[0]['emotion'])
