#from Polynomials.py import polynomial

def main():
    
    Const1 = [2,0,4,-1,0,6]
    #Const2 = [-1,-3,0,4.5]
     
    selected = Const1 
    """
    test1 = polynomial(selected)
    print(test1)
    """
    i = 0 
    out = ' '
    for i in range(len(selected)+1):
        if selected[i] != 0:
            output += ' + %g*x^%d' % (selected[i],i)
             
    print output
    print Const1
    
         
     
     
    
    
    
    
    
    
    
    
    
    
    
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