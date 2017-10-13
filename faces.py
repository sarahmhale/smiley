import sys
from Network import Network
def typeOfEmotion( emotion):
    #1: Happy, 2: Sad, 3: Mischievous, 4: Mad.
    if( emotion == '1'):
        return [1,0,0,0]
    elif(emotion == '2'):
        return [0,1,0,0]
    elif(emotion == '3'):
        return [0,0,1,0]
    elif(emotion == '4'):
        return [0,0,0,1]
def loadFacit (facit_face_file, X):
    newX = []
    faces = open( facit_face_file, 'r' )
    content = faces.readline()
    while content:
        if not content.startswith('#'):
            word = content.split()
            item = (item for item in X if item["key"] == word[0]).next()
            item['emotion'] = typeOfEmotion(word[1])
            newX.append(item)
        content = faces.readline()
    return newX

def loadData(face_file):
        out = []
        faces = open( face_file, 'r' )
        content =  faces.readline()
        while content:
            if(content.startswith('#')):
                content = faces.readline()
            elif(content.startswith('I')):
                key = content.strip()
                grid = []
                content = faces.readline()
                while(content != "\n"):
                    grid+= content.split()
                    content = faces.readline()
                out.append({"key": key, "grid": list(map(int, grid))
, "emotion": 100})
            else:
                content = faces.readline()

        return out

if __name__ == "__main__":
    X = loadData(sys.argv[1])
    X = loadFacit(sys.argv[2],X)
    ANN = Network(400,200,4)

    #ANN.printStructure()
    ANN.train(X)
