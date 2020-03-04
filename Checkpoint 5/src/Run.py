from Planets import Planets
from Calculations import Calculations
from Animate import Animate

def main():
    planetList = list()

    # Read the data from the file
    allLines = Calculations.readFromFile("Data.txt")
    
    # This splits the lines read in to the right classes
    index = 3 
    while index < len(allLines):
        if index < 4:
            simulationData = Calculations(int(allLines[1].replace('\n', '')), float(allLines[3].replace('\n', '')))
            index += 2
        else:
            planetList.append(allLines[index]) 
            index += 1

    # Information read from the files in the correcty datatypes
    marsInfo = Calculations.splitData(planetList[0])
    phobosInfo = Calculations.splitData(planetList[1])

    # Planet class
    mars = Planets(marsInfo[0], marsInfo[1], marsInfo[2], marsInfo[3], marsInfo[4])
    phobos = Planets(phobosInfo[0], phobosInfo[1], phobosInfo[2], phobosInfo[3], phobosInfo[4])
    
    # This will trigger the simulation an begin. 
    Calculations.runSimulation(simulationData, mars, phobos)

    # This will start the animation process
    Ani1 = Animate(mars.positionArray, phobos.positionArray, simulationData.totalKineticEnergyArray)
    Ani1.display()



# This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()