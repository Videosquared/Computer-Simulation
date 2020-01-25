#Checkpoint 1

class polynomial(object):
    
    def __init__(self, constants1):
        self.poly1 = constants1
        #pp1 = polynomial.calculate(self)
"""
    def calculate(self):
        i = 0 
        output = ''
        for i in range(len(self.poly1)):
            if self.poly1[i] != 0:
                output += ' + %g*x^%d' %(self.poly1[i],i)
                i += 1
            else:
                i += 1
        return output"""


def main(): 
    const1 = [2,0,4,-1,0,6]
    const2 = [-1,-3,0,4.5]

    p1 = polynomial(const1)
    print(p1.poly1, end=" ")


if __name__ == "__main__":
    main()  
