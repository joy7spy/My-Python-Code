# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.

# In Python, a function is defined using the def keyword, followed by a function name and parentheses:
def addition (a , b):
  s = a + b
  return s

result = str (addition (5,6))
print (result)
# Function definitions cannot be empty. 
# If you need to create a function placeholder without any code, 
# use the pass statement
def not_defining ():
  pass 

not_defining()

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the actual value that is sent to the function when it is called.
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# with keyword arguments, the order of the arguments does not matter.
def display(name , roll , mark):
  print ("My name is " + name) 
  print (f"Roll = {roll}" )
  print (f"mark = {mark}" )


display(roll=230112 , name = "Joy" , mark = 97)

# arbitrary arguments , keyword arbitrary arguments
# *args and **kwargs allow functions to accept a unknown number of arguments.
def student (*name):
  print (f"first student : {name[0]}")
  print (f"second student : {name[1]}")

student ("joy" , "rakibul" , "antor")

def total_sum (*arg):
  total = 0
  for i in arg :
    total += i 
  return total 

print (f"sum = {total_sum(10,20,30,40,50)}")

def naming (**kwarg):
  print ("his last name " + kwarg["lname"])
  print ("his first name " + kwarg["fname"])

naming (fname = "Joy" , lname= "Roy")

# The * and ** operators can also be used when calling functions to unpack (expand) 
# a list or dictionary into separate arguments.

# unpacking list
def my_function(a, b, c):
  return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

#unpacking dictionaries
def my_function(fname, lname):
  print("Hello", fname, lname)
person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")