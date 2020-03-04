import numpy as np

# from Calculations import Calculations

class Planets(object):

    # This will hold all the information about the planets and patch
    def __init__(self, name, mass, orbitRadius, position, velocity):
        self.name = name
        self.mass = mass
        self.orbitRadius = orbitRadius
        self.position = position
        self.velocity = velocity
        self.positionArray = list()
        self.velocityArray = list()

    # This will set the current values to the new values from the integration. 
    def updateValues(self, newPos, newVelo):
        self.position = newPos
        self.velocity = newVelo
