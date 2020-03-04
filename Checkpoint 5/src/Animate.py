import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

class Animate():

    # These will hold all the required values for the simulation
    def __init__(self, marsArray, phobosArray, totalKArray):
        self.numFrames = len(marsArray)
        self.marsPos = marsArray
        self.phobosPos = phobosArray
        self.totalKArray = totalKArray

    # This will update both circle positions as the simulation goes on 
    def animate(self, i):
        self.patchMars.center = (self.marsPos[i][0], self.marsPos[i][1])
        self.patchPhobos.center = (self.phobosPos[i][0], self.phobosPos[i][1])

        return self.patchMars, self.patchPhobos, 

    def display(self):
        fig = plt.figure()
        ax = plt.axes()

        # Creates 2 circles to represent the moon phobos and planet mars, also size of the circles are added and
        # then added to the plot at the starting postions. 
        self.patchMars = plt.Circle((self.marsPos[0][0], self.marsPos[0][1]), 0.1, color='r', animated=True)
        self.patchPhobos = plt.Circle((self.phobosPos[0][0], self.phobosPos[0][1]), 0.1, color='b', animated=True)
        self.patchMars.set_radius(1605000)
        self.patchPhobos.set_radius(850000)
        ax.add_patch(self.patchMars)
        ax.add_patch(self.patchPhobos)

        ax.axis('scaled')
        ax.set_ylim(-1.5e7, 1.5e7)
        ax.set_xlim(-1.5e7, 1.5e7)

        # Animate the plot
        anim = FuncAnimation(fig, self.animate, self.numFrames, repeat=False, interval=1, blit=True)
        # This prints the total Kinetic Energy just before the animation is shown.
        self.showTotalK()
        plt.show()     

        
    # Displaying the total Kinetic energy at regualar intervals to the command line. 
    def showTotalK(self):
        print("TOTAL KINETIC ENERGY: ", '{:0.4e}'.format(self.totalKArray[0]))
        for i in range(self.numFrames):
            if i % (self.numFrames/50) == 0:
                print("TOTAL KINETIC ENERGY: ", '{:0.4e}'.format(self.totalKArray[i]))