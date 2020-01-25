#Checkpoint 1
constants1 = [2, 4, -1, 6]
constants2 = [-1, -3, 4.5]

class polynomial:
    
    def __init__(self, constant):
        self.constant = constants1

    #def 

    #def calculate(self):


    #def addition(self):

    
    #def derive(self):


    #def integrate(self):



    def print(self):
        i = 0

        print(format(self.constant[0]) + " + ", end = "", flush = True)
        
        while i <= 4:
            print(format(self.constant[i+1]) + "x +", end = "", flush = True)
            print(format(self.constant[i+2]) + "x^3" + "+", end = "", flush = True)
            if i == 3:
                break
            i += 1




class Test:
    p1 = polynomial(constants1)
    p1.print()

    #This is a test line
    #this is a test line 12
