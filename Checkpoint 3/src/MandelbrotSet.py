import numpy as np 
import matplotlib.pyplot as plt 

class MandelbrotSet:
    
    def __init__(self, size_of_x, size_of_y, max_iterations):
        self.size_x = size_of_x
        self.size_y = size_of_y
        self.max_ite = max_iterations
    
    # This is used to calculate the mantelbrot set and displaying
    # it in a graph
    def calculate_Man_set(self):
        x_points = np.linspace(-2.025,0.6, self.size_x)
        y_points = np.linspace(-1.125,1.125, self.size_y)
        result = np.zeros((self.size_x, self.size_y), dtype=int) # This array is used to store the number of iterations and used to plot graph
        
        x_coord, y_coord = np.meshgrid(x_points, y_points)
        grid = x_coord + 1j*y_coord
        
        # This is use to iterate thru the array grid using 2 loops the grid is in the format [y, x]
        for i in range(self.size_x):
            for j in range(self.size_y):
                z = 0.0j 
                for k in range(self.max_ite): # this is the max number of iterations 
                    if abs(z) <= 2:
                        z = z*z + grid[j,i]
                        result[j,i] = k+1
                    else:
                        result[j,i] = k+1
                        break

        # Using matplotlib to plot the graph
        plt.imshow(result, cmap='hot', extent = (-2.025, 0.6, -1.125, 1.125))
        plt.xlabel('Re(c)')
        plt.ylabel('Im(c)')
        plt.title('Mandelbrot Set')
        plt.show()


#END CLASS


# This will start the simulation
def main():
    size_of_x = 800 # these determines the size of the graph and the quality, these can also create an rectangle graph as well
    size_of_y = 800
    max_iterations = 255

    man_set1 = MandelbrotSet(size_of_x, size_of_y, max_iterations)
    MandelbrotSet.calculate_Man_set(man_set1)
#END main()

#This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()
