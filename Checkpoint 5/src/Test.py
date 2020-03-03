    # def runSimulation(self, mars, phobos):
    #     currentTime = 0.0 
    #     #print(self.forceExertedOnPhobos(mars, phobos))
    #     #print(self.forceExertedOnMars(mars, phobos))
    #     #print(self.accMars(mars, phobos))
    #     print(self.accPhobos(mars, phobos))

    # def forceExertedOn(self, mars, phobos, rPos):
    #     if type(rPos) == tuple:
    #         magnitudeRPos = math.sqrt(rPos[0]**2 + rPos[1]**2)
    #         force = self.gravitationalConst * ( (mars.mass * phobos.mass) / (magnitudeRPos**2) ) * magnitudeRPos
    #     else:
    #         force = self.gravitationalConst * ( (mars.mass * phobos.mass) / (rPos**2) ) * rPos
    #     return force

    # def forceExertedOnPhobos(self, mars, phobos):
    #     x1, y1 = mars.position
    #     x2, y2 = phobos.position
    #     r21 = (x1 - x2), (y1 - y2)
        
    #     force = self.forceExertedOn(mars, phobos, r21)
    #     return force

    # def forceExertedOnMars(self, mars, phobos):
    #     r12 = phobos.orbitRadius
    #     force = self.forceExertedOn(mars, phobos, r12)
    #     return force

    # def accMars(self, mars, phobos):
    #     accelMars = self.forceExertedOnMars(mars, phobos)/mars.mass
    #     return accelMars

    # def accPhobos(self, mars, phobos):        
    #     x1, y1 = mars.position
    #     x2, y2 = phobos.position
    #     r21 = (x1 - x2), (y1 - y2)
    #     magR = math.sqrt((r21[0]**2) + (r21[1]**2))
    #     accel = -self.gravitationalConst * ( (phobos.mass)/ magR**3 )
    #     accelPhobos = r21[0] * accel, r21[1] * accel
    #     return accelPhobos

    # def animation(self, mars, phobos):
    #     pass




import linecache

import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class SineAnimation1(object):

    def __init__(self):
        # set initial and final x coordinates of circle
        self.xpos = 0.0
        self.xmax = 2*math.pi
        
        # set simulation parameters
        self.niter = 500
        self.xincr = (self.xmax - self.xpos)/self.niter

    def init(self):
        # initialiser for animator
        return self.patch

    def animate(self, i):
        # update the position of the circle
        self.xpos += self.xincr
        self.patch.center = (self.xpos, math.sin(self.xpos))
        return self.patch,

    def run(self):
        # create plot elements
        fig = plt.figure()
        ax = plt.axes()

        # create circle of radius 0.1 centred at initial coordinates and add to axes
        self.patch = plt.Circle((self.xpos, math.sin(self.xpos)), 0.1, color = 'g', animated = True)
        ax.add_patch(self.patch)

        # set up the axes
        ax.axis('scaled')
        ax.set_xlim(self.xpos, self.xmax)
        ax.set_ylim(-1.1, 1.1)
        ax.set_xlabel('x (rads)')
        ax.set_ylabel('sin(x)')

        # create the animator
        anim = FuncAnimation(fig, self.animate, frames = self.niter, repeat = False, interval = 50, blit = True)

        # show the plot
        plt.show()



def main():
    s = SineAnimation1()
    s.run()
    






        


# # def main():
#     # a = (1,2)
#     # b = (2,1)
#     # x1,y1 = a
#     # x2, y2 = b

#     # print(map(3*,a))

#     # print(type(6.4185e23))
#     # print(type((0,1))

#     # readingFile = open("test.txt")
#     # allLines = readingFile.readlines()
#     # print(allLines[2])


#     # print(linecache.getline('test.txt', 1))


#     # class Planets(object):
#     #     def __init__(self):
#     #         pass

#     # class Calculations():
#     #     def __init__(self):
#     #         pass

#     #     def readFromFile(self, fileName):
#     #         pass

#     # def main():
#     #     pass



# This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()
