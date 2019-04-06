class poly:
    
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
        
    def inputsides(self):
        self.sides = [float(input("enter side "+str(i+1)+" : ")) for i in range(self.n)]
        
    def dispsides(self):
        for i in range(self.n):
            print("Side ",i+1," : ", self.sides[i])
            
poly1 = poly(3)
#check intance values
poly1.__dict__

#input sides
poly1.inputsides()
poly1.__dict__ #change in sides values

#display sides
poly1.dispsides()


#Creating new class Triangle that inherits from poly class

class square(poly):
    
    def __init__(self):
        poly.__init__(self, 2)  # or use: super().__init__(2)
    
    def findArea(self):
        a,b = self.sides
        area = a * b
        print("area is ",area)
        
s1 = square()
s1.inputsides()
s1.findArea()

#isintance(x,y), checks if x is an instance of y
isinstance(s1,square)  #True
isinstance(s1,poly) # True since inherited

#issubclass(x,y), checks if x is a subclass of y
issubclass(square, poly) #True
issubclass(poly, square) #False


#############

# Multiple Inheritance

class Base1:
    pass

class Base2:
    pass

class Multiple(Base1, Base2):
    pass

#Check for the Method Resolution Order (mro)
Base1.__mro__
Base2.__mro__
Multiple.__mro__ # returns a tuple 
Multiple.mro()  # returns a list 


# Multilevel Inheritance
    
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass

#Check for MRO
Base.mro()
Derived1.mro()
Derived2.mro()


#########################3
#Polymorphism

class A:
    def msg(self):
        print("This is from A")
        
class B:
    def msg(self):
        print("This is from B")
    
def msg_func(type_):
    type_.msg()

a = A()
b = B()

msg_func(a)  # This is from A
msg_func(b)  # This is from B

#Polymorphism with abstract class

class document:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method!")
    
class pdf(document):
    def show(self):
        return "Show pdf contents!"

class word(document):
    def show(self):
        return "Show word contents!"

d = document('doc')
d.show()  #raises NotImplentedError

pdf1 = pdf("PDF1")
pdf1.name
pdf1.show()        

documents = [pdf("doc1"), word("doc2"), pdf("doc3")]

for doc in documents:
    print(doc.name," : ",doc.show())


####################
#Another example
    
class Car:
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        raise NotImplementedError("Subclass should implement abstract method")
    
    def stop(self):
        raise NotImplementedError("Subclass should implement abstract method")
    
class Truck(Car):
    def drive(self):
        return "Truck is driving"
        
    def stop(self):
        return "Truck is stopping"
    
class RaceCar(Car):
    def drive(self):
        return "RaceCar is driving"
    
    def stop(self):
        return "RaceCar is stopping"
    
cars = [Truck("T1"), RaceCar("RC1"), Truck("T2")]
    
for car in cars:
    print(car.name," : ",car.drive())
        
        
        
        
        

