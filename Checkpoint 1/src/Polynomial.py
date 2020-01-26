#Checkpoint 1

class polynomial(object):

  def __init__(self, constants1):
    self.poly1 = constants1
  

  def calculate(self):
    i = 0 
    output = ''
    for i in range(len(self.poly1)):
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
    len_p1 = len(self.poly1)
    len_p2 = len(polynomial(p1))
    add_out = []
    i = 0

    if len_p1 > len_p2:
      for i in range(len_p1):
        add_out = add_out.append(self.poly1[i] + p1[i])
      #end loop
    else:
      for i in range(len_p2):
        add_out = add_out.append(self.poly1[i] + p1[i])
      #end loop
    #end if 
    return add_out
  #END adddition()

  

  def integration(self):
    pass
  #END integration()

  def diff(self):
    pass
  #END diff()

#END CLASS polynomial