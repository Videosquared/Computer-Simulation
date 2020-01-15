#Checkpoint 1
constants1 = [2, 4, -1, 6]

class polynomial:
    
    def __init__(self, constant):
        self.constant = constants1

    #def calculate(self):

    #def addition(self):
    
    #def derive(self):

    #def integrate(self):

    def print(self):
        i = 0

        print(format(self.constant[0]) + "+", end = "", flush = True)
        
        while i <= 4:
            print(format(self.constant[i+1]) + "+", end = "", flush = True)
            if i == 2:
                break
            i += 1


class Test:
    p1 = polynomial(constants1)
    p1.print()