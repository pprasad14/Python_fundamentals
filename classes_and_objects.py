class car:
    #class attributes
    vehicle = "car"
    
    def __init__(self, color,company):
        
        #instance attributes 
        self.color = color
        self.company = company
         
    def speed(self, s):
        print("max speed of {} is {} mph".format(self.company, s))
    def get_v(self):
        return self.vehicle
    
    
car1 = car("red","Ferrari")
car2 = car("yellow","Lambo")

#accessing class and instance attributes:
print("{} is a {}".format(car1.company,car1.vehicle))

print("{} is a {} {}".format(car1.company, car1.color, car1.vehicle))
print("{} is a {} {}".format(car2.company, car2.color, car2.vehicle))

car1.speed(200)
car2.speed(250)

#Complex number
class Complex:
    
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
        
    def show(self):
        print("{} + {}j".format(self.real, self.imag))
   
c1 = Complex(1,2)
c2 = Complex(4,5)

#creating a new attribute for an object
c2.attr = 20
print("c2.real: {}, c2.imag: {}, c2.attr: {}".format(c2.real, c2.imag, c2.attr))

#to check all attributes of an object
#returns a dictionary object
print(c1.__dict__)
print(c2.__dict__)

print(c2.__dict__.keys())

#deleting object attributes
c3 = Complex(10,20)
c3.show() #no error

del c3.real
c3.show() #gives error since there is no real attribute

#deleting the whole object
del c3
c3

