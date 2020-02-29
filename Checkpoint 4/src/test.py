import numpy as np
import matplotlib.pyplot as plt


def main():
    printArray = [1,2,3,4,5,6,7,8,9]
    plt.imshow(printArray, interpolation='none')
    plt.show()
    
    
    # test = np.zeros(10, dtype=int)

    # test[2] = 1 
    
    # for i in range(len(test)):
    #     if test[i] == 1:
    #         if i <= (10 - 2):
    #             test[i] = 0
    #             test[i+1] = 1
    #     print(test)

    # roadArray = np.zeros(10, dtype=int)
    # numOfIterations = 10
    # roadLength = 10 
    # roadArray[2] = 1
    # tempRoad = roadArray
    # print("This is road array right after making roadArray[2] = 1")
    # print(roadArray)
    # print()

    # for j in range(numOfIterations):
    #     tempRoad = roadArray.copy()
    #     print("[TEMPROAD]:  ", tempRoad)
    #     print("[ROADARRAY]: ", roadArray)
    #     for i in range(len(roadArray)):
    #         if roadArray[i] == 1:
    #             if i < roadLength -1:
    #                 if roadArray[i+1] == 0:
    #                     tempRoad[i] = 0 
    #                     tempRoad[i+1] = 1
    #             elif i == roadLength - 1:
    #                 if roadArray[0] == 0:
    #                     tempRoad[0] = 1 
    #                     tempRoad[i] = 0


        # print(tempRoad)
        # print()
        # print(roadArray)
        # print()
        # roadArray = tempRoad.copy()
        # print("Iteration Number: ", j)
        # print(roadArray)



        # for n in range(self.numOfIterations):
        #     tempRoad = self.roadArray.copy()
        #     for i in range(self.roadLength):
        #         if self.roadArray[i] == 1:
        #             if i < (self.roadLength-1):
        #                 if self.roadArray[i+1] == 0:
        #                     tempRoad[i+1] = 1
        #                     tempRoad[i] = 0
        #             else:
        #                 if self.roadArray[0] == 0:
        #                     tempRoad[i] = 0 
        #                     tempRoad[0] = 1
        #     self.roadArray = tempRoad.copy()
        #     print(self.roadArray)








#This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()
