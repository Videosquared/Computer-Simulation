
class Test(object):
    print("hello")


class polynomial:
    def __init__(self, x, y):
        self.x = x 
        self.y = y 

    def print(self):
        print("This is x " + self.x)


p1 = polynomial("hello", 38)
p1.print()
