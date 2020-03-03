import numpy as np
# from Calculations import Calculations

class Planets(object):

    def __init__(self, name, mass, orbitRadius, position, velocity):
        self.name = name
        self.mass = mass
        self.orbitRadius = orbitRadius
        self.position = position
        self.velocity = velocity
        # self.tempPosition = tuple()
        # self.tempVelocity = tuple()

    def animation(self):
        pass

    def updateValues(self, newPos, newVelo):
        self.position = newPos
        self.velocity = newVelo
        
