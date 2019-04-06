num_set = set([10,2,2,3,3,4])
num_set  #removes duplicates

#printing individual elements in set
for n in num_set:
    print(n)
    
#empty set
s = set()

#add single member
s.add('prem')

#add multiple members
s.update(['prasad','hello','world'])
print(s)

#removing items from set
s.pop() #pops random value. takes no argument
s.remove('prem') # hard remove. so if doesn't exist, then error
s.discard('world') #if exists then remove, if not exits, then no error

# intersection of sets

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1 & set2)  #intersection
print(set1 | set2)  #union
print(set1 - set2)  #difference
print(set2 - set1)  #difference
print(set1 ^ set2)  #symmetric difference

#shallow copy
set3 = set2.copy() # hard  copy
set3.clear()

set3 = set2 #link copy
set3.clear()