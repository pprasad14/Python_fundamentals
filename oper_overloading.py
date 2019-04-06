class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
p1 = Point(2,3)
p2 = Point(3,4)

#check instance values:
#p1.__dict__
#p2.__dict__

#gives error, since + has no meaning for these objects
p1 + p2

print(p1) #does not give sensible output

#to fix output, create special function __str__:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):   
        return "({0},{1})".format(self.x, self.y)

p1 = Point(2,3)
print(p1)
str(p1)  #  or  p1.__str__() 


#operator overloading for +

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
        
    def __lt__(self, other):
        if self.x < other.x and self.y < other.y:
            return [True,True]
        elif self.x < other.x and not self.y < other.y:
            return [True, False]
        elif self.x > other.x and not self.y > other.y:
            return [False, True]
        else:
            return [False, False]
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


p1 = Point(3,3)
p2 = Point(3,3)

print(p1 - p2)

print(p2 < p1)

print(p1 == p2)
