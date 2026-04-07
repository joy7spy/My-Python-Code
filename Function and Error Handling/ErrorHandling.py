# Error
# An error is a serious problem in a program.
# It usually happens due to incorrect syntax or system-level issues.
# Program cannot run properly when an error occurs.
# Generally not handled by the programmer.

# Exception
# An exception is a problem that occurs during program execution.
# It can be handled using try-except blocks.
# Program does not crash if properly handled.


# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks
# The raise keyword is used to raise an exception.


try :
  #print (x)
  x = 10 /0
  # raise ArithmeticError ("ArithmeticErro is occured.")
except ZeroDivisionError as e :
  print ("Exception is occured : " , e)
except ArithmeticError as e :
  print ("Exception is occured : " , e)
except :
  print ("An exception is occured.")

else :
  print ("Nothing error is occured.")

finally:
  print ("this block is always executed wherever error occurs or not.")