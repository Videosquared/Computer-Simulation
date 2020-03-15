import numpy as np
from Body import Body

class SimUtils():

    def __init__(self):
        pass

    @staticmethod
    def splitData(planetInfo):
        output = list()
        planetInfo = planetInfo.replace('\n', '')
        planetInfo = planetInfo.replace('(', '')
        planetInfo = planetInfo.replace(')', '')
        output = planetInfo.split("/")
        output[1] = float(output[1])
        output[2] = float(output[2])
        output[3] = float(output[3])
        output[3] = np.array(tuple(map(float, output[3].split(','))))
        output[4] = np.array(tuple(map(float, output[4].split(','))))
        output[5] = np.array(tuple(map(float, output[5].split(','))))

        return output 

    @staticmethod
    def readFromFile(fileName):
        readingFile = open(fileName)
        output = readingFile.readlines()
        readingFile.close()
        return output
