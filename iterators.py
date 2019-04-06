#define a list

a = [1,2,3,4]

#get an iterator object

a_iter = iter(a)

next(a_iter) #prints 1
next(a_iter) #prints 2
next(a_iter) #prints 3
next(a_iter) #prints 4

next(a_iter) # StopIteratin error

#printing elements of list using iterator and while loop

b = [6,7,8,9,10]

b_iter = iter(b)

while True:
    try:
        print(next(b_iter))
    
    except:
        print("No more items")
        break
    
#sample program to show all even numbers until a given number
        
class Even:
    
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = self.n + 2
            self.n += 2
            return result
        else:
            raise StopIteration
            
            
obj = Even(10)

iterator = iter(obj)

while True:
    try:
        print(iterator.__next__())
    except:
        print("No more items")
        break    
            
            
            
            