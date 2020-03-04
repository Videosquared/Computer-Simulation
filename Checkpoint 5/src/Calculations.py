from Planets import Planets
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import math

class Calculations():
    # Holds all the info for the calculations
    def __init__(self,numberOfIterations ,timeStep):
        self.timeStepLength = timeStep
        self.numOfIter = numberOfIterations
        self.gravitationalConst = 6.67408e-11
        self.tempPosition = tuple()
        self.tempVelocity = tuple()
        self.totalKineticEnergyArray = list()

    # This will calculate all the required positions and the velocities 
    # and put them into an array in the planet class
    def runSimulation(self, mars, phobos):
        for i in range(self.numOfIter):
            # sets the initial kinetic energy to the first element of the array
            self.totalKineticEnergyArray.append(self.totalKineticEnergy(mars, phobos))
            # this will add the positions to the array in class Planets
            mars.positionArray.append(mars.position)
            phobos.positionArray.append(phobos.position)
            mars.velocityArray.append(mars.velocity)
            phobos.velocityArray.append(phobos.velocity)

            # This calls the code for calculating the new position and velocity.
            newMarsPos = self.newPos(mars, phobos)
            newMarsVelo = self.newVelocity(mars, phobos)
            newPhobosPos = self.newPos(phobos, mars)
            newPhobosVelo = self.newVelocity(phobos, mars)

            # change the "old" values to the new values
            Planets.updateValues(mars, newMarsPos, newMarsVelo)
            Planets.updateValues(phobos, newPhobosPos, newPhobosVelo)


    # This calculates the force for the 2 given bodies
    def calculateForce(self, v1, v2):
        rPos = v1.position[0] - v2.position[0], v1.position[1] - v2.position[1]
        magRPos = math.sqrt(rPos[0]**2 + rPos[1]**2)
        unitRPos = rPos[0] / magRPos, rPos[1] / magRPos
        tempForce = self.gravitationalConst*((v1.mass*v2.mass)/ magRPos**2)
        force = unitRPos[0] * tempForce, unitRPos[1] * tempForce
        return force
    
    # calculates the acceleration for the 2 bodies
    def calculateAcc(self, body1, body2):
        force = self.calculateForce(body2, body1)
        accel = force[0] / body1.mass, force[1] / body1.mass
        return accel

    # calculates the new velocity for body 1
    def newVelocity(self, body1, body2):
        accel = self.calculateAcc(body1, body2)
        newVelo = body1.velocity[0] + (accel[0] * self.timeStepLength), body1.velocity[1] + (accel[1] * self.timeStepLength)
        return newVelo

    # calculate the new position of body 1
    def newPos(self, body1, body2):
        nextVelo = self.newVelocity(body1, body2)
        newPos = body1.position[0] + (nextVelo[0]*self.timeStepLength), body1.position[1] + (nextVelo[1]*self.timeStepLength)
        return newPos

    # Using the formula to calculate the total kinetic energy
    def totalKineticEnergy(self, mars, phobos):
        magM = math.sqrt(mars.velocity[0]**2 + mars.velocity[1]**2)
        magP = math.sqrt(phobos.velocity[0]**2 + phobos.velocity[1]**2)
        totalKEnergy = (0.5 * mars.mass * magM**2 )+(0.5 * phobos.mass * magP**2)
        return totalKEnergy

    # This will split the data into the correct data types and into an list
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

    # This will read from the file supplied into an array with all the lines. 
    @staticmethod
    def readFromFile(fileName):
        readingFile = open(fileName)
        output = readingFile.readlines()
        readingFile.close()
        return output
        