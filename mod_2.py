#importing mod_1 file.
#set working directory to the location where mod_1 is present

import mod_1
#show("hello")  #gives error

#using the module name and '.' operator to access the module objects
mod_1.show("hello")
mod_1.a


a=mod_1.Complex()
a.show()

#to access mod_1 objects without using the module name
from mod_1 import show, a

show("hello")
a

#importing non-existent module

import xyz  #gives error: ModuleNotFoundError: No module named 'xyz'

#exception handling while importing modules

try:
    import xyz
    
except ImportError:
    print("Module not found")
    
#importing existing module but non-existent object:
    
try:
    from mod_1 import abc
    
except ImportError:
    print("Object not found in Module")
    

#importing mod_3(factorial) using a different name
import mod_3_factorial as mod_3   

mod_3.fact(4)