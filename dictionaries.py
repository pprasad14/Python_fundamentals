#empty dictionary
d = {}

#dictionary with integer keys
d = {'c':'prem', 2:'prasad'}
print(d)

#using dict()
d = dict({1:'apple', 2:'ball'})
print(d)

#from sequence
a = [('two',2),('four',4)]
d = dict(a)
d

#accessing elements from dictionary
d['two']

#getting dictionary items
d.items()

#getting dicitionart keys
d.keys()

#getting dictionary values
d.values()

#updating values of dictionary:
d['two'] = 3
d

#adding elements:
d['fize'] = 5
d

#dictionary comprehensions
d = {x:x*x for x in range(10)}
d

#deleting elements
d.pop(0)
d

#using "fromkeys()"
d = {}.fromkeys(['a','b','c'],[1,2,3])
d

#iterating dictionaries
for i in d.items():
    print(i)

#comparing two dictionaries
a = {1:1,2:2,3:3}
b = {1:1,2:2,3:3}
c = {1:1,2:2,3:3,4:4}

a == b
a == c

#nested dictionary
nested_dict = { 'dictA': {'key_1': 'value_1'},
                'dictB': {'key_2': 'value_2'}}

nested_dict['dictA']['key_1']

#iterating nested dictionaries
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)
    print("\nPerson details:", p_info)
    
    for key in p_info:
        print(key + ':', p_info[key])