#creating a list
a = [1,2,3,4]
print(a)

#add element to list at the end
a.append(5)
print(a)

#add elements to list at given position
a.insert(3,10)
print(a)

#adding a list to a list
b = [6,7,8]
a.extend(b)
print(a)

#indexing elements in list:
print(a[2])

#slicing a list
a[3:6]
a[:-2]

#searching a list:
c = list("premprasad")
if 'p' in c:
    print("Yes")
    
#deleting elements in a list:
del a[4]
print(a)

del a[1:4]
print(a)

#getting count of numbers in list
a.count(6)

#finding position of matching value
a.index(7)

#getting reverse of list
a.reverse()
print(a)


#list comprehension
x = [a*a for a in range(10)]
x

#list comprehension with condition
y = [a*a for a in range(20) if a%2!=0]
y
