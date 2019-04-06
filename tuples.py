#creating tuples
a = 1, 3.4, "dog"
b = ('Prem', 2, 4.5)

#combining two tuples
c = a+b
c

#accessing elements of tuples
d = tuple('prasad')
d[4]
d[2:]

#tuple unpacking
x,y,z = b
print (x,y,z)

#tuple with only one element
t = ('prem')
type(t)  #type str

t = ('prem') #or
t = 'prem',
type(t)  #type tuple

# nested tuple
n_tuple = (list("mouse"), [8, 4, 6], (1, 2, 3))
n_tuple[2][2]

#changing elements of a tuple
n_tuple[0] = 'prem' #gives error
n_tuple[1] = [1,2,3] #gives error
n_tuple[1][0] = 9  #no error

n_tuple

#deleting tuple
del n_tuple

#getting count
x = (1,1,2,3,4,4,4,5)
x.count(4)

#getting index
a,b,c=x.index(4)

#tuple membership test
print(1 in x)
print(6 not in x)