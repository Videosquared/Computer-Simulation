#Checkpoint 1
hello = [1, 3, 4, 6, 9]

class polynomial:
    
    def __init__(self, constant1):
        self.constant1 = hello
     

    def print(self):
        print(self.constant1)


class Test(object):
    print("hello")
    p1 = polynomial(hello)
    p1.print()