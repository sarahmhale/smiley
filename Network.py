from Neuron import Neuron
import numpy as np

class Network:
    """
    Purpose:    Initiates the network with the number of neurons given
    Input:      An integer represeting the number of neurons one for each
                feeling.
    Output:     void
    Comment:    self.neurons is list with the neurons for each emotion.
    """
    def __init__(self,numberOfNeurons):
        self.rightAnswerRate = 0.7
        self.neurons = []
        self.nrOfRightAnswers = 0
        for i in range(numberOfNeurons):
            self.neurons.append(Neuron(np.random.rand(400)/1000,0.1))

    """
    Purpose:    For each image in images it loops through the emotion
                neurons and activates the neurons feedForward function and
                then the updateWeights function

    Input:      [{'key': "image1", 'grid':[0,32,20.....],'emotion': [0,1,0,0] },
                {'key': "image2", 'grid':[1,16,20.....],'emotion': [1,0,0,0] }]

    Output:     void
    """
    def feedForward(self, images):
        for image in images:
            for i in range(len(self.neurons)):
                self.neurons[i].feedForward(image['grid'])
                self.neurons[i].updateWeights(image['emotion'][i])

    """
    Purpose:    For each image in images it loops through the emotion
                neurons and activates the neurons feedForward and then prints
                the emotion with the highest output value.

    Input:      [{'key': "image1", 'grid':[0,32,20.....],'emotion': [0,1,0,0] },
                {'key': "image2", 'grid':[1,16,20.....],'emotion': [1,0,0,0] }]
    Output:     void
    """
    def testAndPrintAnswers(self, images):
        for image in images:
            neuronOutputs = []
            for neuron in self.neurons:
                neuronOutputs.append(neuron.feedForward(image['grid']))
            print "mood: ", neuronOutputs.index(max(neuronOutputs))+1

    """
    Purpose:    compares the index of highest value in neuronOutputs and the
                facit.
                checks if they have the same value.
                If they are the same the the number of right answers
                is updated with +1
    Input:      facit: [0,1,0,0]
                neuronOutputs: [0.7, 0, 0, 0]
    Output:     void
    """
    def compareToFacit(self,facit, neuronOutputs):
        if(neuronOutputs.index(max(neuronOutputs)) == facit.index(max(facit))):
            self.nrOfRightAnswers = self.nrOfRightAnswers + 1

    """
    Purpose:    For each image in images it loops through the emotion
                neurons and activates the neurons feedForward and then sends
                the the neuronOutputs and the right answer to the
                compareFunction.

    Input:      [{'key': "image1", 'grid':[0,32,20.....],'emotion': [0,1,0,0] },
                {'key': "image2", 'grid':[1,16,20.....],'emotion': [1,0,0,0] }]
    Output:     void
    """
    def test(self, test_set):
        self.nrOfRightAnswers = 0
        for face in test_set:
            neuronOutputs= []
            for neuron in self.neurons:
                neuronOutputs.append(neuron.feedForward(face['grid']))
            self.compareToFacit(face['emotion'], neuronOutputs)

    """
    Purpose:    Runs through the training data. training_images are used to
                train and update weights and the test_images are for checking if
                the network is good enough.
                
    Input:      training_images:
                [{'key': "image1", 'grid':[0,32,20.....],'emotion': [0,1,0,0] },
                {'key': "image2", 'grid':[1,16,20.....],'emotion': [1,0,0,0] }]

                test_images:
                [{'key': "image1", 'grid':[0,32,20.....],'emotion': [0,1,0,0] },
                {'key': "image2", 'grid':[1,16,20.....],'emotion': [1,0,0,0] }]
    Output:     void
    """
    def train(self, training_images, test_images):
        while(float(self.nrOfRightAnswers)/len(test_images) < self.rightAnswerRate):
            np.random.shuffle(training_images)
            self.feedForward(training_images)
            self.test(test_images)
