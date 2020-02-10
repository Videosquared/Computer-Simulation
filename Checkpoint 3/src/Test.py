"""
import numpy as np 
import matplotlib.pyplot as plt 


numpoints = 201

x = np.linspace(-np.pi, np.pi, numpoints)
y = np.cos(x)

plt.plot(x,y)
plt.title('Cosine Plot')
plt.xlabel('Theta')
plt.ylabel('cosine')
plt.show()
 



x = np.arange(3000)
y = np.arange(3000)

xx, yy = np.meshgrid(x,y)

z = 2*xx + yy

left = x.min()
right = len(x)
bottom = y.min()
top = len(y)

plt.imshow(z, extent=(left,right,bottom,top), interpolation='none', cmap='hot', origin='lower')
plt.colorbar()
plt.show()



import numpy as np

x = np.linspace(1.0,4.0, 4)
y = np.linspace(-1.0,1.0,3)

xx, yy = np.meshgrid(x,y)

z = xx + 1j*yy

"""




import numpy as np
import matplotlib.pyplot as plt 

def main(re, im, max_it):
    c = complex(re, im)
    z = 0.0j
    for i in range(max_it):
        z = z*z + c
        if (z.real * z.real + z.imag * z.imag) > 2:
            return i 
        
    return max_it

columns = 200
rows = 200 

result = np.zeros((rows,columns))
for row_index, re in enumerate(np.linspace(-2,1,num=rows)):
    for column_index, im in enumerate(np.linspace(-1,1,num=columns)):
        result[row_index, column_index] = main(re,im,100)

plt.figure(dpi=100)
plt.imshow(result.T, cmap = 'hot', interpolation = 'bilinear', extent = (-2.025, 0.6, -1.125, 1.125))
plt.xlabel('Re')
plt.ylabel('Im')
plt.show()