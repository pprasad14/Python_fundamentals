def func(arg):
    return arg*arg

#normal function call
print(func(10))

#passing functions as arguments
def call_func(f, arg):
    return f(arg)

print(call_func(func, 10))


#########

def decorator(some_func):
    
    def wrapper():
        print("something happening before some_func() called")
        
        some_func()
        
        print("something happening after some_func() called")
    
    return wrapper

def func1():
    print("function 1")
    
def func2():
    print("function 2")
    
f1 = decorator(func1)
f1()

f2 = decorator(func2)
f2()

############
import time

def time_func(some_function):
    
    def wrapper():
        t1 = time.time() 
        #call some_function()
        some_function()
        t2 = time.time()
        return ("Time it took to run the function:"+ str((t2-t1))+"\n")
    return wrapper

@time_func
def my_func():
    list_ = []
    for a in range(0,1000):
        list_.append(a)
    print("sum of numbers is :  ",sum(list_))

print(my_func())

##########

#decorator to limit how fast a function is called

def my_dec(function):
    
    def wrapper(*args, **kwargs):
        time.sleep(2)
        function(*args, **kwargs)
    return wrapper

@my_dec
def print_num(num):
    print (num)

print_num(123)

for num in range(1,6):
    print_num(num)
        
        
        
        
        