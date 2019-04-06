# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
a = my_gen()

next(a)  #This is printed first
next(a)  #This is printed second
next(a)  #This is printed last

next(a)  #StopIteration error

#using for loop
for item in my_gen():
    print(item)
    
def rev_str(s):
    l = len(s)
    for i in range(l - 1, -1, -1):
        yield s[i]

for char in rev_str("prem"):
    print(char)

######
    
#Python Generator Expression

#Initialize a list
a = [1,2,3,4,5]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in a]

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>
(x**2 for x in a)

#printing n numbers of the series

ob = (x**2 for x in a) 

flag = 1
while(flag == 1):
    try:
        print(next(ob))
    except:
        print("No more items")
        break
    flag = int(input("continue? 1 for yes, 0 for no:  "))
    

#Generator function to implement PowerOfTwo

def PowTwoGen(max_ = 0):
    n = 0
    while n < max_:
        yield 2**n
        n+=1

gen_10 = PowTwoGen(10)

next(gen_10) 


#Infinite Stream of Squares

def Inf():
    n = 0
    while True:
        yield n*n
        n += 1

inf_ob = Inf()

next(inf_ob)