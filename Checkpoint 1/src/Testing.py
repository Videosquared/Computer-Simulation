from Polynomial import polynomial

def main():
  
  const1 = [2,0,4,-1,0,6] 
  const2 = [-1,-3,0,4.5]
  const3 = [5,2,0,0,0,2,-31,333,82721]

  p1 = polynomial(const1)
  p2 = polynomial(const2)
  p3 = polynomial(const3)

  p11 = polynomial.calculate(p1)
  p21 = polynomial.calculate(p2)
  p31 = polynomial.calculate(p3)

  p12 = polynomial.calculate( polynomial(polynomial.addition(p1, p2)) )
  p22 = polynomial.calculate( polynomial(polynomial.addition(p2, p3)) )
  p32 = polynomial.calculate( polynomial(polynomial.addition(p3, p1)) )

  p13 = polynomial.calculate( polynomial(polynomial.integration(p1)) )
  p23 = polynomial.calculate( polynomial(polynomial.integration(p2)) )
  p33 = polynomial.calculate( polynomial(polynomial.integration(p3)) )

  p14 = polynomial.calculate( polynomial(polynomial.differentiation(p1)) )
  p24 = polynomial.calculate( polynomial(polynomial.differentiation(p2)) )
  p34 = polynomial.calculate( polynomial(polynomial.differentiation(p3)) )

  print(p11)
  print(p21)
  print(p31)

  print(" ")
  
  print(p13)
  print(p23)
  print(p33)

  print(" ")

  #print(p12)
  #print(p22)
  #print(p32)

  print(" ")

  print(p14)
  print(p24)
  print(p34)
  #END main()
  

# To start main function automatically 
if __name__ == "__main__":
  main()