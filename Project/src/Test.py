import numpy as np


def main():
    a = "122,222"
    b = tuple(map(float, a.split(',')))
    output = np.array( b )
    print(output)


    print(tuple(map(float, a.split(','))))























# This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()