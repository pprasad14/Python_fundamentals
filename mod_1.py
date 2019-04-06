a = "This is module 1"

b = [1,2,3]

def show(msg):
    print("your message is :",msg)
    
#the following gets printed on terminal when imported
# >>>import mod_1
'''
print(a)
print(b)
show("hi")
'''
#to import without printing
class Complex:
    
    def __init__(self, real = 0, imag = 0):
        self.real = real
        self.imag = imag
        
    def show(self):
        print("{} + {}j".format(self.real, self.imag))
if(__name__ == '__main__'):
    print(a)
    print(b)
    show("hi")  
