#Checkpoint 1

class polynomial(object):

  def __init__(self, constants1):
    self.poly1 = constants1
  

  def calculate(self):
    output = ''
    for i in range(len(self.poly1)): # This sets the original layout to ax^n including 1x^0
      if self.poly1[i] != 0:
        output += ' + %g*x^%d' %(self.poly1[i],i) 
        i += 1
      else:
        i += 1

    output = output.replace('+ -', '- ') # This replaces a + - to just a -
    output = output.replace('x^0', '1') # This replaces the x^0 to just 1
    output = output.replace(' 1*', ' ') # This replaces 1* to just the x
    output = output.replace('x^1 ', 'x ') # This replaces the x^1 to just x 
    output = output.replace('*1', '') # This fixes the first term from 5*1
    
    if output[0:3] == ' + ':  # remove initial +
      output = output[3:]
    if output[0:3] == ' - ':  # fix spaces for initial -
      output = '-' + output[3:]
    return output
  #END calculate()

  def addition(self, p1):
    po1 = self.poly1
    po2 = p1.poly1  
    len_po1 = len(po1) # Calculate the length of the lists and places them into an variable
    len_po2 = len(po2)
    diff_len =  max(len_po1 - len_po2, len_po2 - len_po1) # Find out the difference between the length of both list
    add_out = []

    if len_po1 > len_po2:
      po2 += [0] * diff_len
    else:
      po1 += [0] * diff_len
    #end if
    
    for i in range( max(len_po1, len_po2) ):
      add_out += [(po1[i] + po2[i])] 
    #end loop

    return add_out
  #END adddition()

  def integration(self):
    integ1 = self.poly1 
    inte_out = []

    for i in range(len(integ1)):
      inte_out += [( integ1[i]/(i+1) )]
    #end loop

    inte_out.insert(0, 2) 

    return inte_out
  #END integration()

  def differentiation(self):
    diff1 = self.poly1
    diff_out = []

    for i in range(len(diff1)):
      diff_out += [(diff1[i] * i)]
    #end if
    diff1.pop(0)
    return diff_out
  #END diff()

#END CLASS polynomial