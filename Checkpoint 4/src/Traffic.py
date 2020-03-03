import numpy as np
import random
import matplotlib.pyplot as plt 

np.set_printoptions(threshold=np.inf, linewidth = np.inf)

class Traffic:
    def __init__(self, numIterations, lengthOfRoad, carDensityOnRoad, numberOfCarDensityChecks):
        self.numOfIterations = numIterations
        self.roadLength = lengthOfRoad
        self.carDensity = carDensityOnRoad
        self.numOfCars = int(self.carDensity * self.roadLength)
        self.roadArray = np.zeros(self.roadLength, dtype=int)
        self.averageSpeed = 0
        # This is for printing of the road to show it changing over time
        self.printArray = np.zeros((self.numOfIterations, self.roadLength), dtype=int)
        self.carDensityArray = np.linspace(0, 1, numberOfCarDensityChecks) 
        # This is used to help print the gradual increase in car density
        self.steadyStateArray = np.zeros(numberOfCarDensityChecks) 

    # This will move the car along the road using the periodic 
    # boundary conditions. This also uses an counter to calculate
    # an average speed of the car.s
    def calculate(self):
        if self.numOfCars == 0:
            self.averageSpeed = 0
        else:
            for n in range(self.numOfIterations):
                for i in range(self.roadLength):
                    self.printArray[n][i] = self.roadArray[i]

                tempRoad = np.zeros(self.roadLength, dtype=int)
                counter = 0 
                for i in range(self.roadLength):
                    if self.roadArray[i] == 1:
                        if self.roadArray[(i+1)%self.roadLength] == 1:
                            tempRoad[i] = 1
                        else:
                            tempRoad[i] = 0 
                            counter += 1
                    elif self.roadArray[i] == 0:
                        if self.roadArray[(i-1)%self.roadLength] == 1:
                            tempRoad[i] = 1
                        else: 
                            tempRoad[i] = 0 
                
                self.roadArray = tempRoad.copy()
                self.averageSpeed = (counter/self.numOfCars)

    # This adds the cars to the road depending on the number of
    # cars set by the car density.
    def addCarsToRoad(self):
        counter = 0 
        if self.carDensity != 0.0:
            while True:
                if counter == self.numOfCars:
                    break
                randNumber = random.randint(0, self.roadLength-1)
                if self.roadArray[randNumber] == 0:
                    self.roadArray[randNumber] = 1 
                    counter += 1 

    # This is used to calculate the graph for how average 
    # speed changes as car density changes. We use the same road length 
    # and the number of iterations as user input.
    def regularIntervalCalculate(self):
        for i in range(len(self.carDensityArray)):
            self.carDensity = self.carDensityArray[i]
            self.numOfCars = int(self.carDensity * self.roadLength)
            self.clearRoad()
            self.addCarsToRoad()
            self.calculate()
            self.steadyStateArray[i] = self.averageSpeed

    # This will print the graph of the acerage speed against change in 
    # car density.
    def printGraph(self):
        plt.figure(2)
        plt.plot(self.carDensityArray, self.steadyStateArray)
        plt.xlabel('Change in Car Density')
        plt.ylabel('Steady Rate')
        plt.title('Change in steady state as car density changes')

    # This will clear the road of all cars and reset it to emoty 
    def clearRoad(self):
        for i in range(len(self.roadArray)):
            self.roadArray[i] = 0 

    # This will print the road into an grid and shows the road change over time
    def printVisualRep(self):
        plt.figure(1)
        plt.imshow(self.printArray, interpolation='none', origin='lower', cmap='hot')
        plt.xlabel('Road from left to right (->)')
        plt.ylabel('Time from bottom to top')
        plt.title('Representation of road changing over time')

    # Shows all graphs/plots at the end at the same time
    def showGraphs(self):
        plt.show()

# This is the method that starts the program an then asks the user for the required inputs
# to run the program. 
def main():
    numberOfIterations = int(input("Please enter the max number of iterations: "))
    lengthOfRoad = int(input("Please enter the length of the road (N): "))
    # User input checking if its between 0-1
    while True:
        carDensityOnRoad = float(input("Please enter the car density from 0 to 1 (0.1 = 10%): "))
        if carDensityOnRoad >= 0 and carDensityOnRoad <= 1:
            break
        
    numOfCarDensityChecks = 100

    # These values below are used for testing purposes ONLY
    # numberOfIterations = 100
    # lengthOfRoad = 100
    # carDensityOnRoad = 0.5
   

    road1 = Traffic(numberOfIterations, lengthOfRoad, carDensityOnRoad, numOfCarDensityChecks)
    road1.addCarsToRoad()
    road1.calculate()
    road1.printVisualRep()
    road1.regularIntervalCalculate()
    road1.printGraph()
    road1.showGraphs()


#This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()
