import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
# from Calculations import Calculations

class Planets(object):

    def __init__(self, name, mass, orbitRadius, position, velocity):
        self.name = name
        self.mass = mass
        self.orbitRadius = orbitRadius
        self.position = position
        self.velocity = velocity
        self.positionArray = list()
        self.velocityArray = list()

    def updateValues(self, newPos, newVelo):
        self.position = newPos
        self.velocity = newVelo

    # DO NOT COPY BELOW THIS LINE

    def animate(self, i):
        self.patchMars.center = (self.positionArray[i][0], self.positionArray[i][1])

    def display(self):
        fig = plt.figure()
        ax = plt.axes()

        self.patchMars = plt.Circle((self.positionArray[0][0], self.positionArray[0][1]), 0.1, color='b', animated=True)
        ax.add_patch(self.patchMars)

        ax.axis('scaled')

        numFrames = len(self.positionArray)
        anim = FuncAnimation(fig, self.animate, numFrames, repeat=False, interval=20, blit=True)
        plt.show()     




    @staticmethod
    def animation(mars, phobos):
        pass
        # fig = plt.figure()
        # ax = plt.axes()

        # marsPatch = plt.Circle((mars.position[0], mars.positon[1]), radius=10, animated=True)
        # phobosPatch = plt.Circle((phobos.position[0], phobos.positon[1]), radius=5, animated=True)
        
        # ax.add_patch(marsPatch)
        # ax.add_patch(phobosPatch)

        # ax.axis('scaled')
        # ax.set_xlabel('x (rads)')
        # ax.set_ylabel('sin(x)')

        # anim = FuncAnimation(fig, Calculations.runSimulation(), frames = self.niter, repeat = False, interval = 50, blit = True)




        
