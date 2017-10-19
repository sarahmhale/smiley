import sys
import numpy as np
from Neuron import Neuron
from Network import Network
class Faces:
    def typeOfEmotion(self, emotion):
        #1: Happy, 2: Sad, 3: Mischievous, 4: Mad.
        if( emotion == '1'):
            return [1,0,0,0]
        elif(emotion == '2'):
            return [0,1,0,0]
        elif(emotion == '3'):
            return [0,0,1,0]
        elif(emotion == '4'):
            return [0,0,0,1]
    def loadFacit (self,facit_face_file, X):
        newX = []
        faces = open( facit_face_file, 'r' )
        content = faces.readline()
        while content:
            if not content.startswith('#'):
                word = content.split()
                item = (item for item in X if item["key"] == word[0]).next()
                item['emotion'] = self.typeOfEmotion(word[1])
                newX.append(item)
            content = faces.readline()
        return newX


    def loadData(self,face_file):
            out = []
            faces = open( face_file, 'r' )
            content =  faces.readline()
            while content:
                if(content.startswith('I')):
                    key = content.strip()
                    grid = []

                    content = faces.readline()
                    while(content != "\n"):
                        grid+= content.split()
                        content = faces.readline()
                    out.append({"key": key, "grid": [float(x)/32 for x in grid]
    , "emotion": 100})
                else:
                    content = faces.readline()

            return out

if __name__ == "__main__":
    X = Faces().loadData(sys.argv[1])
    X = Faces().loadFacit(sys.argv[2],X)
    test_file = Faces().loadData(sys.argv[3])

    network = Network(4)

    training_set = X[: int(len(X)*0.7)]
    test_set = X[int(len(X)*0.7):]

    network.train(training_set,test_set)
    network.testAndPrint(test_file)



    #print "number of right answers are", float(counter)/len(test_set)*100, "%"
