import numpy as np
import random 

class RadDecay(object):

  # This is used to setup the array to the right size. 
  def __init__(self, decay_Const, array_Size, time_Stamp):
    self.arraySize = array_Size
    self.decayConst = decay_Const
    self.timeStamp = time_Stamp
  #END __init__()
  
  # This starts an infinite loop to calculate the half life of the
  # element and then display it in an array form.
  def calculateDecay(self): 
    num_decayed = 0 
    out_array = np.zeros((self.arraySize,self.arraySize))
    radTime = 0.0

    while True:
      if num_decayed >= ((self.arraySize * self.arraySize) / 2):
        break
      else:
        for i in range(self.arraySize):
          for j in range(self.arraySize):
            if out_array[i,j] == 0:
              rnd_num = (random.random())
              probability = (self.decayConst * self.timeStamp)
              if rnd_num < probability:
                out_array[i,j] = 1
                num_decayed += 1

      radTime += self.timeStamp
  
    np.set_printoptions(threshold=np.inf, linewidth = np.inf)
    print(out_array)
    print("\n")
    print("The simulated half life is: ", round(radTime, 2), " mins")
    print("Number of nuclei decayed: ", num_decayed)
    print("The original number of nuclei: ", (self.arraySize * self.arraySize))
  #END calculate()

  # This is used to calculate the actual half life of the element
  # using the formula and display the value. 
  def calculateActual(self):
    actual_time = np.log(2)/self.decayConst
    actual_time = round(actual_time, 2)

    print("The actual value of half life (using decay consant): ", actual_time , " mins")
  #END calculateActual()



    

#END CLASS 
