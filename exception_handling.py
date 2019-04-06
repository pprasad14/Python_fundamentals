#Example 1
import sys

try:
    print(1/0)
except ZeroDivisionError:
    print("Divide by zero error")

##############
try:
    print(1+a)
except NameError:
    print("undefined variable detected")
##############   
try:
    '1' + 1
except TypeError:
    print("incorrect type detected")
    
##############
  
try:
    number = int(input("Enter a number between 1 - 10:  "))
    if number >10 or number <1:
        raise ValueError
except ValueError:
    print("Wrong Input")
    sys.exit()
    
print("number: ",number)
    
##############
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()

##############
try:
   fh = open("testfile", "r")   #Read permission
   fh.write("This is my test file for exception handling!!")
except IOError:
   print("Error: can\'t find file or read data")
else:
   print("Written content in the file successfully")
   fh.close()

##############
try:
    print("opening file")
    fh = open("testfile", "r")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print ("Going to close the file")
        fh.close()
except IOError:
   print ("Error: can\'t find file or read data")

##############
# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except (ValueError):
      print ("The argument does not contain numbers\n", var)

# Call above function here.
temp_convert("xyz")
temp_convert("123")


