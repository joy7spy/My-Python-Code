class Calculator:
  def add (self,a , b):
    return a + b
  def multiply (self , a , b):
    return a*b
  
cal = Calculator()
print ("add = " + str(cal.add (3 , 9)))
print ("Multiply = " + str(cal.multiply(3,9)))