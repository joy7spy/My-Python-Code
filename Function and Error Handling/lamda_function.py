# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
square = lambda x : x*x 
print (square (3))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))



# The map() function applies a function to every item in an iterable
numbers = [1,2,3,4,5]
double = list (map (lambda a : a*2 , numbers))
print (double)



# The filter() function creates a list of items for which a function returns True
even = list (filter (lambda a : a%2 == 0 , numbers))
print (even)

# The sorted() function can use a lambda as a key for custom sorting
students = [("joy" , 230112 ) , ("antor" , 230125) , ("rakibul" , 230116)]
sorted_student = sorted (students , key = lambda x : x[1])
print (sorted_student)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)