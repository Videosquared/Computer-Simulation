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

  p12 = polynomial.addition(p1, p2)
  p22 = polynomial.addition(p2, p3)
  p32 = polynomial.addition(p3, p1)

  print(p11)
  print(p21)
  print(p31)

  print(p12)
  print(p22)
  print(p32)
  

# To start main function automatically 
if __name__ == "__main__":
  main()