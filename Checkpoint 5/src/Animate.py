import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

class Animate():

    def __init__(self, marsArray, phobosArray):
        self.numFrames = len(marsArray)
        self.marsPos = marsArray
        self.phobosPos = phobosArray


    def animate(self, i):
        self.patchMars.center = (self.marsPos[i][0], self.marsPos[i][1])
        self.patchPhobos.center = (self.phobosPos[i][0], self.phobosPos[i][1])

        return self.patchMars, self.patchPhobos,

    def display(self):
        fig = plt.figure()
        ax = plt.axes()

        self.patchMars = plt.Circle((self.marsPos[0][0], self.marsPos[0][1]), 0.1, color='r', animated=True)
        self.patchPhobos = plt.Circle((self.phobosPos[0][0], self.phobosPos[0][1]), 0.1, color='b', animated=True)
        self.patchMars.set_radius(1700000)
        self.patchPhobos.set_radius(900000)
        ax.add_patch(self.patchMars)
        ax.add_patch(self.patchPhobos)

        ax.axis('scaled')
        ax.set_ylim(-1.5e7, 1.5e7)
        ax.set_xlim(-1.5e7, 1.5e7)

        anim = FuncAnimation(fig, self.animate, self.numFrames, repeat=False, interval=5, blit=True)
        plt.show()     