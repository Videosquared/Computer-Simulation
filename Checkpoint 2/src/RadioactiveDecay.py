import numpy as np
import random 

class RadDecay(object):

  # This is used to setup the array to the right size. 
  def __init__(self, decay_Const, array_Size, time_Stamp):
    self.arraySize = array_Size
    self.decayConst = decay_Const
    self.timeStamp = time_Stamp
  #END __init__()


  # This will display all the iterations of the decay and then
  # display the final half life when the flag is set to true
  def display(self):
    pass
    """while True:
      if flag == True:
        print(time)
        print(initail nuclei)
        print(final nuclei)
        print(simulated half-life)
        print(actual halflife )
        break"""
  #END display()
  
  # This starts an infinite loop to calculate the half life of the
  # element and then return the time
  def calculate(self):
    #flag = False 
    num_decayed = 0 
    out_array = np.zeros((self.arraySize,self.arraySize))
    radTime = 0.00

    while True:
      if num_decayed == ((self.arraySize * self.arraySize) / 2):
        break
      else:
        for i in range(self.arraySize):
          for j in range(self.arraySize):
            if out_array[i,j] == 0:
              rnd_num = random.random()
              probability = (self.decayConst * radTime)
              if probability <= rnd_num:
                out_array[i,j] = 1
                num_decayed += 1
              #end if 
            #end if 
            radTime += self.timeStamp
          #end for 
        #end for
      #end if 
    #end while
    return out_array
  #END calculate()

  # This is used to calculate the actual half life of the element
  # using the formula and return the value. 
  def calculateActual(self):
    pass
  #END calculateActual()



    

#END CLASS 
