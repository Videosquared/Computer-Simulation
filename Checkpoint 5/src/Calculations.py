from Planets import Planets
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import math

class Calculations():
    def __init__(self,numberOfIterations ,timeStep):
        self.timeStepLength = timeStep
        self.numOfIter = numberOfIterations
        self.gravitationalConst = 6.67408e-11
        self.tempPosition = tuple()
        self.tempVelocity = tuple()

    def runSimulation(self, mars, phobos):
        currentTime = 0.0

        for i in range(self.numOfIter):
            # These 2 lines are for testing delete when done
            #print("Mars Pos:    ", mars.position)
            #print("Phobos Pos:", phobos.position)

            mars.positionArray.append(mars.position)
            phobos.positionArray.append(phobos.position)
            mars.velocityArray.append(mars.velocity)
            phobos.velocityArray.append(phobos.velocity)

            newMarsPos = self.newPosMars(mars, phobos)
            newMarsVelo = self.newVelocityMars(mars, phobos)
            newPhobosPos = self.newPosPhobos(mars, phobos)
            newPhobosVelo = self.newVelocityPhobos(mars, phobos)

            Planets.updateValues(mars, newMarsPos, newMarsVelo)
            Planets.updateValues(phobos, newPhobosPos, newPhobosVelo)


    def calculateForce(self, mars, phobes, magR, unitR):
        tempForce = self.gravitationalConst*((mars.mass*phobes.mass)/ magR**2)
        force = unitR[0] * tempForce, unitR[1] * tempForce
        return force
    
    def calculateForcePhobos(self, mars, phobos):
        r21 = mars.position[0] - phobos.position[0], mars.position[1] - phobos.position[1]
        magR21 = math.sqrt(r21[0]**2 + r21[1]**2)
        unitR21 = r21[0] / magR21, r21[1] / magR21
        force = self.calculateForce(mars, phobos, magR21, unitR21)
        return force
    
    def calculateForceMars(self, mars, phobos):
        r12 = phobos.position[0] - mars.position[0], phobos.position[1] - mars.position[1]
        magR12 = math.sqrt(r12[0]**2 + r12[1]**2)
        unitR12 = r12[0] / magR12, r12[1] / magR12
        force = self.calculateForce(mars, phobos, magR12, unitR12)
        return force
        
    def calculatAccPhobos(self, mars, phobos):
        force = self.calculateForcePhobos(mars, phobos)
        accPhobos = force[0] / phobos.mass, force[1] / phobos.mass
        return accPhobos

    def calculatAccMars(self, mars, phobos):
        force = self.calculateForceMars(mars, phobos)
        accMars = force[0] / mars.mass, force[1] / mars.mass 
        return accMars

    def newVelocityMars(self, mars, phobos):
        marsAcc = self.calculatAccMars(mars, phobos)
        newVelo = mars.velocity[0] + (marsAcc[0] * self.timeStepLength), mars.velocity[1] + (marsAcc[1] * self.timeStepLength)
        return newVelo

    def newVelocityPhobos(self, mars, phobos):
        phobosAcc = self.calculatAccPhobos(mars, phobos)
        newVelo = phobos.velocity[0] + (phobosAcc[0] * self.timeStepLength), phobos.velocity[1] + (phobosAcc[1] * self.timeStepLength)
        return newVelo

    def newPosMars(self, mars, phobos):
        nextVelo = self.newVelocityMars(mars, phobos)
        newPos = mars.position[0] + (nextVelo[0]*self.timeStepLength), mars.position[1] + (nextVelo[1]*self.timeStepLength)
        return newPos

    def newPosPhobos(self, mars, phobos):
        nextVelo = self.newVelocityPhobos(mars, phobos)
        newPos = phobos.position[0] + (nextVelo[0]*self.timeStepLength), phobos.position[1] + (nextVelo[1]*self.timeStepLength)
        return newPos


    @staticmethod
    def splitData(planetInfo):
        output = list()
        planetInfo = planetInfo.replace('\n', '')
        planetInfo = planetInfo.replace('(', '')
        planetInfo = planetInfo.replace(')', '')
        output = planetInfo.split()
        output[1] = float(output[1])
        output[2] = float(output[2])
        output[3] = tuple(map(float, output[3].split(',')))
        output[4] = tuple(map(float, output[4].split(',')))

        return output 

    @staticmethod
    def readFromFile(fileName):
        readingFile = open(fileName)
        output = readingFile.readlines()
        readingFile.close()
        return output
        