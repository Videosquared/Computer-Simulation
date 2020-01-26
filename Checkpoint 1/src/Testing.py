from Polynomial import polynomial

def main():
  
  const1 = [2,0,4,-1,0,6] 
  const2 = [-1,-3,0,4.5]
  const3 = [5,2,0,0,0,2,-31,3,8]

  p1 = polynomial(const1)
  p2 = polynomial(const2)
  # Test Subject
  p3 = polynomial(const3)

  p11 = polynomial.calculate(p1)
  p21 = polynomial.calculate(p2)
  # Test Subject 
  p31 = polynomial.calculate(p3)

  # This calculates all the additon of the Polynomials
  p12 = polynomial.calculate( polynomial(polynomial.addition(p1, p2)) )
  p22 = polynomial.calculate( polynomial(polynomial.addition(p2, p3)) )
  p32 = polynomial.calculate( polynomial(polynomial.addition(p3, p1)) )

  # This calculates all the integration of the polynomials 
  p13 = polynomial.calculate( polynomial(polynomial.integration(p1)) )
  p23 = polynomial.calculate( polynomial(polynomial.integration(p2)) )
  p33 = polynomial.calculate( polynomial(polynomial.integration(p3)) )

  # This calculates all the first derivative of the polynomials
  p14 = polynomial.calculate( polynomial(polynomial.differentiation(p1)) )
  p24 = polynomial.calculate( polynomial(polynomial.differentiation(p2)) )
  p34 = polynomial.calculate( polynomial(polynomial.differentiation(p3)) )

  # This is p1 as the main P(x)
  print("This is the original P(x):")
  print(p11)
  print("This is Additon of P_1(x) and P_2(x):")
  print(p12)
  print("This is the first derivative of P(x):")
  print(p14)
  print("This is the integrated if P(x):")
  print(p13)
  
  print(" ") # Gap between the lines of code
  
  # This is p2 as the main P(x)
  print("This is the original P(x):")
  print(p21)
  print("This is Additon of P_1(x) and P_2(x):")
  print(p22)
  print("This is the first derivative of P(x):")
  print(p24)
  print("This is the integrated if P(x):")
  print(p23)

  print(" ") # Gap between the lines of code

  # This is p3 as the main P(x)
  print("This is the original P(x):")
  print(p31)
  print("This is Additon of P_1(x) and P_2(x):")
  print(p32)
  print("This is the first derivative of P(x):")
  print(p34)
  print("This is the integrated if P(x):")
  print(p33)
  #END main()
  

# To start main function automatically 
if __name__ == "__main__":
  main()