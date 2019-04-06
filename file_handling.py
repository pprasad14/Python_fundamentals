filename = "testfile"

#to open a file
file = open(filename,'r')

#to read as one big string
print(file.read())

#to write into file
file = open(filename,'w')  #creates a new file if file does not exist
file.write("hello world")

#to append text into file
file = open(filename,'a')
file.write("welcome to world")

#to display the information in file line by line
file = open(filename, 'r')
for line in file:
    print(line)

#creating new file
file = open("demofile.txt",'x')  #returns error if file already exists
file.write("hello")
file.close()


#to append multiple line from list:
file = open("demofile.txt","a")
l = "Hi this is prem".split()
for line in l:
    file.write(line)
file.close()

file = open("demofile.txt",'r')
print(file.read())
print(file.read(7)) #to print 7 characters
file.close()

#to print first line
file = open('demofile.txt','r')
file.readline()
file.close()

#to delete files
import os
os.remove("demofile")    
    
#checking if file present or not before deleting
import os
if os.path.exists("demofile"):
    os.remove("demofile")
else:
    print("file does not exist")
