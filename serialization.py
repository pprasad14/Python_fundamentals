##########
#using pickle.dumps()
import pickle

scores = {'Alice': 50, 'Bob':78, 'Cathy':76}  #this is structured data ie dictionary

#to serialize this dictionary object, use pickle.dumps()
serial_scores = pickle.dumps(scores)
print(serial_scores) #unreadable format

#to retrieve data, use pickle.loads()
received_scores = pickle.loads(serial_scores)
print(received_scores)

###############
#using pickle.dump(), specifying file name

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

filename = 'dogs'
outfile = open(filename, 'wb')
pickle.dump(dogs_dict, outfile)
outfile.close()

#to unpickle, use pickle.load()
infile = open(filename, 'rb')
new_dict = pickle.load(infile)
infile.close()

#compare to check if successful
print(dogs_dict)
print(new_dict)
print(dogs_dict == new_dict)
print(type(new_dict))

###############

import json

def add_employee(salaries_json, name, salary):
    sal =   json.loads(salaries_json)
    sal[name] = salary

    return json.dumps(sal)

salaries = '{"Alfred" : 300, "Jane" : 400 }'  # str datatype
new_salaries = add_employee(salaries, "Me", 800)
print(new_salaries)  #json serialized objects are human readable unlike pickle serialized objects

decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])

##############

#Compressing pickled files using bzip2

import bz2
import pickle

dogs_dict = { 'Ozzy': 3, 'Filou': 8, 'Luna': 5, 'Skippy': 10, 'Barco': 12, 'Balou': 9, 'Laika': 16 }

comp_file = bz2.BZ2File('smallerfile','w')
#dump the pickled object into this file
pickle.dump(dogs_dict,comp_file)
comp_file.close()

#to retrieve the pickled data
comp_infile = bz2.BZ2File('smallerfile','r')
new_d = pickle.load(comp_infile)
print(new_d)

#comparing them:
print(new_d == dogs_dict)