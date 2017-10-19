from Neuron import Neuron
import numpy as np

class Network:
    def __init__(self,numberOfNeurons):
        self.neurons = []
        for i in range(numberOfNeurons):
            self.neurons.append(Neuron(np.random.rand(1,400)/1000))

    def feedForward(self, training_set):
        for face in training_set:
            i = 0
            for neuron in self.neurons:
                neuron.feedForward(face['grid'])
                neuron.updateWeights(face['emotion'][i])
                i = i +1

    def testAndPrint(self, test_set):
        for face in test_set:
            y = []
            for neuron in self.neurons:
                y.append(neuron.feedForward(face['grid']))
            print "mood: ", y.index(max(y))+1

    def compareToFacit(self,facit, y,counter):
        if(y.index(max(y)) == facit.index(max(facit))):
            return counter + 1
        return counter

    def test(self, test_set):
        counter = 0
        for face in test_set:
            y= []
            for neuron in self.neurons:
                y.append(neuron.feedForward(face['grid']))
            counter = self.compareToFacit(face['emotion'], y, counter)
        return counter

    def train(self, training_set, test_set):
        counter = 0
        while(float(counter)/len(test_set)<0.7):
            np.random.shuffle(training_set)
            self.feedForward(training_set)
            counter = self.test(test_set)
