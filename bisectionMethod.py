# function : x^3 - x^2 - 1 
def func(x):
	return x*x*x - x*x - 1

# bisection method 
def bisection (a, b, tolerence, times):
	if( func(a) * func(b) >= 0) :
		print("Assumed a and b are not correct .")
		return
	c = a 
	count = 0
	while((b-a) >= tolerence and times  > count):
		c = (a+b) / 2 
		print(f"a = {a} , b = {b} , mid = {c}\n")
		if( func(c) == 0):
			break

		if( func(c)* func(a) < 0) :
			b = c 
		else:
			a = c
		count = count + 1
	print (f"the root of these function is : {c}")
# guess number a and b
a = float(input("Enter number , a : "))
b = float(input("Enter number , b : "))
tolerence = float(input("Enter the maximum tolerence : "))
times = int (input("Enter the maximum number of iteration : ")) 
bisection (a, b, tolerence, times)
