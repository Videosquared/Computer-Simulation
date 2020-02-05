from RadioactiveDecay import *

import os
import sys
import numpy as np

# This will ask the user to input the values required and then call the class to start
# the simulation. 
def main():

  decay_Const = float(input("Please enter the value for the decay Constant (λ): "))
  array_Size = int(input("Please enter the size of the array (N): "))
  time_Stamp = float(input("Please enther the timestamp (Δt): "))

  rad1 = RadDecay(decay_Const, array_Size, time_Stamp)
  RadDecay.calculateDecay(rad1)
  #rad3 = RadDecay.calculateActual(rad1)
  #RadDecay.display(rad1, rad2, rad3)
  
  
"""

test = np.zeros((array_Size, array_Size))

print(test)
test[0,0] = 1
"""
  

#END main()


#This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
  main()