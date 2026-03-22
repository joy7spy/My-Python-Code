# # name = input("Enter your name : ")
# # print(name)

# a = "joy" 
# print(a.capitalize())
# a = a.capitalize()
# print(a)
# print(a)
# b = "AosOcDds"
# print(b.casefold())  
# a = "joy"
# print(f"amar sonar bangla {a} ami tomay valobashi" )

# s = "a3gd" 
# if s[1] <= '9' or s[1] >= '0' :
#   print("true")
# else :
#   print("false")

# for i in range(4):
#   print("joy")

# print(bin(2).count("1"))


# a = bin(24342) 
# a = a[2:]
# print(a)

# a = "abc"
# b = "def"
# c = "igk"

# print(a,b,c) # abc def igk
# # print(a+b+c) # abcdefigk

# a =int ( input() )

# for i in range (a) :
#   print(i+1)

# for i in range (1,6) :
#   print (i)

# a = int(input())
# sum = 0 
# for i in range(1 , a+1) :
#   sum += i 

# print(sum)

# a = int(input())

# for i in range (1 , 11) :
#   mul = a * i 
#   print(f"{a} * {i} = {mul}")

# a = int(input("input : "))
# fact = 1 
# for i in range (1 , a+1):
#   fact *= i

# print ("output = " + str(fact))
# s = input("Enter number :")
# for i in range (-1 , len(s) * (-1) -1 , -1) :
#   print(s[i] , end = " ")
# for i in range (len(s)-1 , -1 , -1):
#   print(i)
# a = len(s) * (-1)
# print (a)
# for i in range (-1 ,-6 , -1) :
#   print(i)

# for i in range (5):
#   for j in range (i+1):
#     print("*" , end = "")
#   print("")


# s = """ fofhf
# fffpfpmmf O I am a boy .
# I love my country ."""

# print (s)

# s = "GeeksforGeeks"
# print(s[1:4])    # characters from index 1 to 3
# print(s[:3])     # from start to index 2
# print(s[3:])     # from index 3 to end
# print(s[::-1])   # reverse string


# a = s[::-1]
# print(a)
# s = s[::-1]
# print(s)

# # case changing string methods 
# name = "Joydeb Roy Joy"
# name2 = "joydeb roy Joy"

# print(name.upper())   #JOYDEB ROY JOY
# print(name.lower())   #joydeb roy joy
# print(name2.capitalize())    #Joydeb roy joy
# print(name2.title())         #Joydeb Roy Joy
# print(name.swapcase())
# print("")

# str2 = "Hello World" 
# cnt = str2.count("o" , 6 , 11) 
# print(cnt)
# cn2 = str2.count("ll" )    substring should be one character only
# print(cnt2)

# index = name2.find("Joy" , 5)   # returns the first index of main string , if substring is found
# print( index  )                 # if substring is not found , returns -1
# c = "welcome"
# d = "Thank" 
# e = "You"
# print(c.center(20 , '-'))   #------welcome-------
# print(d.center(20 , '-'))   #-------Thank--------
# print(e.center(20 , '-'))   #--------You---------

# age = 22
# print("Myself {}, I am {} years old".format( name , age))

# print(c + ", " + d +" " + e )

# int to string
# l = str(age) 
# print(l)
# # string to int
# print(int("458646645"))        #decimal binary to decimal int by default decimal int
# print(int("81548415" , 10))    #decimal binary to decimal int
# print(int("10101" , 2))        #string binary to decimal int
# print(int("AC47E" , 16))       #string hexadecimal to decimal int

# eman = name[::-1]
# print(eman)

# eman[2] = 'Z'  # strings are immutable , they don't support assignment 
# # print(eman)
# l = []
# l.append(10) 
# print(l)
# l.insert(0,5)
# print(l)
# l.extend([15,20,25 , 10 ])
# print(l)
# l.remove(10)
# print(l)
# # l.remove(30)   # if the element is not found , it gives error
# m = l.pop(1)     #removes the element at a specific index  same as del l[1]
# print(m)
# print(l)

# m = l.pop()     #if no specific index , then removes last element
# print(l)
# cubes = [x**3 for x in range (1,6) ]   # comprehension
# print (cubes)
# cub = [val for val in cubes if val%2 == 0]
# print(cub)

# # normal way of list comprehension
# cube = []
# for x in cubes :
#   if(x%2 == 0) :
#     cube.append(x)
# print(cube)
# l.append ([2,4,5,5,3,5,5678])
# print(l)

# print(l.index(5))
# n = [2,4,5,6]
# print(n.reverse())
# print(n)

# print(n.sort())
# print(n)
# d = n.copy()
# print(d)
# print(n)
# a = [1, 2, 3, 4] 
# b = a 
# c = a.copy() 
# d = a
# a[0] = [5] 
# print(a, b, c, d)


# tup = () 
# tup2 = tuple ()
# print((2,4,5) + (3,6,8))

# tupe = (1,2) + (3,)
# print(tupe)

# a , *b , c = tupe
# print(a, b, c)
# d = {1:"one" , 2 : "two" , 3 : "three" , 4 : "four" } 
# print(d)
# print(len(d))
# print(d[1])
# print(d.get(1))
# d[5] = "five"
# print(d)
# del d[2]
# print(d)
# d.pop(1)
# print(d)
# d.popitem()    # removes the last item of dictionary
# print(d)

# val = d.pop(3)  # returns the value of this key
# print(d)
# print(val)
# val2 = d.popitem()
# print(d)
# print(val2)

# key , valu = d.popitem()
# print(key , valu)

# dc = {"joy" : "roy" , "boy" : "girl" , "good" : "bad"}
# # some built-in method for iteration in dictionary

# for x in dc.keys():
#   print(x)

# for x in dc.values():
#   print(x)

# for x in dc.items():
#   print(x , end = " ")

# for k , v in dc.items():
#   print(k , v , )

# arbitrary arguments 
# def joy (*args):
#   print(args)
#   for a in args:
#     print(a)

# joy("Joydeb Roy Joy" , 22)

# def joy2 (**kwargs):
#   print(kwargs)
#   for key , value in kwargs.items():
#     print(key , value)

# joy2 (a="Collectorate" , b = "Thakurgaon" , c = 2020 , d = 2022)

fun = lambda x : x*x 

print(fun(3))

check = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(check(5))   
print(check(-3))  
print(check(0))

ck = lambda x : "even" if x %2==0 else "odd" 

print(ck(5))

c = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, c)
print(type(even))
print(list(even))


