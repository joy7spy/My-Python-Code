with open ("file.txt" , 'r') as f :
  print (f.read())

f = open("file.txt" , 'a')
f.write("\nI am 22 years old.")
f.close()