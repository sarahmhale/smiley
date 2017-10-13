from Layer import Layer
from random import random
class Network:
    def __init__(self, num_inputs, num_outputs):
        self.num_inputs = num_inputs

        self.output_layer = Layer(num_outputs)

        self.weight_output_layer = self.init_weights(num_inputs, self.output_layer)

    def init_weights(self,num_of_neurons_layer_above, layer):
        for h in range(len(layer.neurons)):
            for i in range(num_of_neurons_layer_above):
                layer.neurons[h].weights.append(random())
        return layer

    def feedForward(self,inputs):
        return self.output_layer.feedForward(inputs)

    def printStructure(self):


        print ""
        print "Output layer: "
        for neuron in self.output_layer.neurons:
            print "weight: ",neuron.weights
            print "bias: ",neuron.bias
        print ""
        for neuron in self.output_layer.neurons:
            print "output: " , neuron.output
            print "delta: " , neuron.delta

        print ""
        #print "number of inputs neurons: ", self.num_inputs
        #print "number of hidden neurons: ", len(self.hidden_layer.neurons)
        #print "number of output neurons: ", len(self.output_layer.neurons)


    def updateFreeParameters(self):
        for neuron in self.output_layer.neurons:
            neuron.updateFreeParameters()

    def calculateError(self, facit):
        #output_layer
        i = 0
        error = []
        for neuron in self.output_layer.neurons:
            error.append(neuron.output_layer_error(facit[i]))
            i = i+1

        print "Error:" ,error


    def train(self,traning_set):
        for i in range(0,100,1):
            for face in traning_set:
                self.feedForward(traning_set[i]['grid'])
                self.calculateError(traning_set[i]['emotion'])
                self.updateFreeParameters()


        self.feedForward(traning_set[0]['grid'])
