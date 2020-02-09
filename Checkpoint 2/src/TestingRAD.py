from RadioactiveDecay import RadDecay

# This will ask the user to input the values required and then call the class to start
# the simulation. 
def main():

    decay_Const = float(input("Please enter the value for the decay Constant (λ): "))
    array_Size = int(input("Please enter the size of the array (N): "))
    time_Stamp = float(input("Please enther the timestamp (Δt): "))

    rad1 = RadDecay(decay_Const, array_Size, time_Stamp)
    RadDecay.calculateDecay(rad1)
    RadDecay.calculateActual(rad1)

#END main()


#This is used to make the program run automatically without any arguments 
if __name__ == "__main__":
    main()