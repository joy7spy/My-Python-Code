# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "x" - Create - Creates the specified file, returns an error if the file exists



text = ["amar sonar bangla \n" , "ami tomay valobashi\n" , "chirodin tomar akash \n"]
with open ("file.txt" , 'w') as f :
  f.writelines (text)


with open ("file.txt" , 'r') as f :
  print (f.read())

f = open("file.txt" , 'a')
f.write("I am 22 years old.")
f.close()

with open ("file.txt" , 'r') as f :
  for x in f :
    print (x)

with open ("files.txt" , 'x') as fi :
  fi.write("My name is Joy Roy")
