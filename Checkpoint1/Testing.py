#from Polynomials.py import polynomial

def main():
  const1 = [2,0,4,-1,0,6]
  const2 = [-1,-3,0,4.5]
    
  selected = const2
  """ 
  test1 = polynomial(selected)
  print(test1)
  """
  i = 0 
  output = ''
  for i in range(len(selected)):
    if selected[i] != 0:
      output += ' + %g*x^%d' %(selected[i],i)
      i += 1
    else:
      i += 1

  print(output, end=" ")





main()
         
     

    
    
    
    
    
    
    
    
    
    
    
"""
class Test:
  Const1 = [2,0,4,-1,0,6]
  Const2 = [-1,-3,0,4.5]
    
    
    p1 = polynomial(constants1)
    p1.print()




selected = Const1

class polynomial(object):

  def __init__(self, constants):
    self.coeff = constants

  def __cal__(self):
    print (self.coeff)


  


#print(Const1, end = "", flush = True)
#print(Const2, end = "", flush = True)
    
class Test(object):
    print("hello")
    """
    


