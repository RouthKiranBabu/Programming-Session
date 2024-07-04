#This is not the dictionary
notdict = {1, }; print(notdict, type(notdict))
#Output
#{1} <class 'set'>

#Creating the dictionary
dict1, dict2 = {}, dict()
print(dict1, type(dict1), dict2, type(dict2))
#Output
#{} <class 'dict'> {} <class 'dict'>

#Whats inside the dictionary
print(dir(dict))
#Output
'''
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', 
'__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
'__getitem__', '__getstate__', '__gt__',
'''

#Knowing all about dict and its methods and documents
print(help(dict.__class__))
#Output
'''
Help on class type in module builtins:

class type(object)
 |  type(object) -> the object's type
'''

"""
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets,
and they have keys and values.
"""
Python = {
    "Designed by" : "Guido van Rossum",
    "Typing" : "Duck, Dynamic, gradual",
    "First appeared" : 1990,
    }
print(Python)
#Output
#{'Designed by': 'Guido van Rossum', 'Typing': 'Duck, Dynamic, gradual', 'First appeared': 1990}

print(Python["Typing"])
#Output
#Duck, Dynamic, gradual

#Key value is not present inside the dictionary.
print(Python.get("C++"));print(Python.get("Designed by"))
#Output
'''
None
Guido van Rossum
'''

#Making .get to not give None as response.
print(Python.get("C++", "Not Found!"))
#Output
#Not Found!

#Sys module importing.
import sys
#Displays python version.
print(sys.version)
#Output
#3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)]

#Converting the system version to string.
Python["Sys version"] = str(sys.version)
print(Python)
#Output
'''
{'Designed by': 'Guido van Rossum', 'Typing': 'Duck, Dynamic, gradual', 'First appeared': 1990, 'Sys version': '3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)]'}
'''

Hacker = {
    "Name" : "xyz",
    "Born" : 1998,
    "Needs" : "Money"
    }
#Update changes the key and also adds new key and value.
Hacker.update({
    "Name" : "abc",
    "Born" : 2002,
    "Primary Need" : "Save World!"
    })
print(Hacker)
#Output
#{'Name': 'abc', 'Born': 2002, 'Needs': 'Money', 'Primary Need': 'Save World!'}

#Showcasing all the keys in Dictionary.
print(Hacker.keys())
#Output
#dict_keys(['Name', 'Born', 'Needs', 'Primary Need'])

#Showcasing all the values in Dictionary. 
print(Hacker.values())
#Output
#dict_values(['abc', 2002, 'Money', 'Save World!'])

#Showing the all keys and values in form of tuples inside the list.
print(Hacker.items())
#Output
'''
dict_items([('Name', 'abc'), ('Born', 2002), ('Needs', 'Money'), ('Primary Need', 'Save World!')])
'''

for key, value in Hacker.items():
    print(key + " -> " + str(value))
#Output
'''
Name -> abc
Born -> 2002
Needs -> Money
Primary Need -> Save World!
'''

del Hacker["Needs"]
print(Hacker)
#Output
#{'Name': 'abc', 'Born': 2002, 'Primary Need': 'Save World!'}

Need = Hacker.pop("Primary Need")
print(Need, Hacker, sep = "\n")
#Output
'''
Save World!
{'Name': 'abc', 'Born': 2002}
'''

#Showing the number of items.
print(len(Hacker))
#Output
#2

di = {"a" : 5}
print(di.get("a"))
#Output
#5

# Number of times(as values) the string(as key) is present
strng = list("adfadfg")
unmp = {}
for i in strng:
    # Get will take the key and returns the value
    unmp[i] = unmp.get(i, 0) + 1
print(unmp)
#Output
#{'a': 2, 'd': 2, 'f': 2, 'g': 1}
