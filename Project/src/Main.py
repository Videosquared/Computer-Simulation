from SimulationUtils import SimUtils

class Main():

    @staticmethod
    def main():
        fileName = "Data.txt"

        allLines = SimUtils.readFromFile(fileName)


# This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    Main.main()