import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

class Animate():

    def __init__(self, marsArray, phobosArray, totalKArray):
        self.numFrames = len(marsArray)
        self.marsPos = marsArray
        self.phobosPos = phobosArray
        self.totalKArray = totalKArray


    def animate(self, i):
        self.patchMars.center = (self.marsPos[i][0], self.marsPos[i][1])
        self.patchPhobos.center = (self.phobosPos[i][0], self.phobosPos[i][1])

        return self.patchMars, self.patchPhobos, 

    def display(self):
        fig = plt.figure()
        ax = plt.axes()

        self.patchMars = plt.Circle((self.marsPos[0][0], self.marsPos[0][1]), 0.1, color='r', animated=True)
        self.patchPhobos = plt.Circle((self.phobosPos[0][0], self.phobosPos[0][1]), 0.1, color='b', animated=True)
        self.totalK = self.totalKArray[0]
        self.patchMars.set_radius(1605000)
        self.patchPhobos.set_radius(850000)
        ax.add_patch(self.patchMars)
        ax.add_patch(self.patchPhobos)

        ax.axis('scaled')
        ax.set_ylim(-1.5e7, 1.5e7)
        ax.set_xlim(-1.5e7, 1.5e7)

        anim = FuncAnimation(fig, self.animate, self.numFrames, repeat=True, interval=0, blit=True)
        self.showTotalK()
        plt.show()     

        
    
    def showTotalK(self):
        print("TOTAL KINETIC ENERGY: ", '{:0.4e}'.format(self.totalKArray[0]))
        for i in range(self.numFrames):
            if i % (self.numFrames/50) == 0:
                print("TOTAL KINETIC ENERGY: ", '{:0.4e}'.format(self.totalKArray[i]))