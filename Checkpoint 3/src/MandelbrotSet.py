import numpy as np 
import matplotlib.pyplot as plt 

class MandelbrotSet(object):
    
    def __init__(self, size_of_x, size_of_y, max_iterations):
        self.size_x = size_of_x
        self.size_y = size_of_y
        self.max_ite = max_iterations
    
    # This is used to calculate the mantelbrot set and displaying
    # it in a graph
    def calculate_Man_set(self):
        x = np.linspace(-2.025,0.6, self.size_x)
        y = np.linspace(-1.125,1.125, self.size_y)
        result = np.zeros((self.size_x, self.size_y), dtype=int)
        
        xx, yy = np.meshgrid(x, y)
        grid = xx + 1j*yy
        
        for i in range(self.size_x):
            for j in range(self.size_y):
                z = 0.0j 
                for k in range(self.max_ite):
                    if abs(z) <= 2:
                        z = z*z + grid[j,i]
                        result[j,i] = k
                    else:
                        result[j,i] = k
                        break

        plt.imshow(result, interpolation='none', cmap='hot', extent = (-2.025, 0.6, -1.125, 1.125))
        plt.xlabel('Re(c)')
        plt.ylabel('Im(c)')
        plt.title('Mandelbrot Set')
        plt.show()


#END CLASS


# This will start the simulation
def main():
    size_of_x = 500 # these determines the size of the graph and the quality 
    size_of_y = 500
    max_iterations = 255


    man_set1 = MandelbrotSet(size_of_x, size_of_y, max_iterations)
    MandelbrotSet.calculate_Man_set(man_set1)
#END main()

#This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()
