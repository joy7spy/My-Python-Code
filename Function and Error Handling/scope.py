# If you operate with the same variable name inside and outside of a function, 
# Python will treat them as two separate variables, one available in the global scope 
# (outside the function) and one available in the local scope (inside the function)

# The global keyword makes the variable global.
x = 300 
def inner ():
  global x
  x = 200 
  print (x)
print (x)
inner ()
print (x)

# The nonlocal keyword is used to work with variables inside nested functions.
# The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())



# Python follows the LEGB rule when looking up variable names, and searches for them in this order:

# Local - Inside the current function
# Enclosing - Inside enclosing functions (from inner to outer)
# Global - At the top level of the module
# Built-in - In Python's built-in namespace

x = "global"  # global variable

def outer():
  x = "enclosing"   # enclosing variable
  def inner():
    x = "local"    # local variable
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)