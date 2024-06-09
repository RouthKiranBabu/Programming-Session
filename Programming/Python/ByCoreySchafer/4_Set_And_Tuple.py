set1, set2, set3, se = set(), {}, {1, }, {'key': 'value'}
#Use the type to know the type of variable and what does it return
print(type(set1), type(set2), type(set3), type(se))
#Output
#<class 'set'> <class 'dict'> <class 'set'> <class 'dict'>

#To show the doc we use __doc__
print(set1.__doc__, set2.__doc__, set3.__doc__, se.__doc__, sep = 99*"~"+3*"\n")
#Output
'''
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


set() -> new empty set object
set(iterable) -> new set object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


dict() -> new empty dictionary
dict(mapping) -> new dictionary initialized from a mapping object's
    (key, value) pairs
dict(iterable) -> new dictionary initialized as if via:
    d = {}
'''

lst = [x for x in range(1, 11)]
#Converting list into set
sct1, sct2, sct3 = set(lst), {1, }, {}; print(sct1, sct2, type(sct1))
#Output
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} {1} <class 'set'>

#Checking the type is same
print(type(sct1) == type(sct2), type(sct1) == type(sct3))
#Output
#True False

#Other way of creating set
sct1 = {x for x in range(1, 11)}; print(sct1)
#Output
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#Checking element is present in the set or not
print(5 in sct1)
#Output
#True

sct = {1, 2, 3}
#To check what this set has
print(dir(sct))
#Output
'''
['__and__', '__class__', '__class_getitem__', '__contains__', 
'__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
'__iand__', 
'''

#To know all about set and its Method
print(help(sct.__class__))
#Output
'''
Help on class set in module builtins:

class set(object)
 |  set() -> new empty set object
 |  set(iterable) -> new set object
'''

set1, set2 = {1, 2, 3}, {2, 3, 4}
#Use of intersection, difference, union
print(set1.intersection(set2)); print(set1.difference(set2)); print(set2.union(set1))
#Output
'''
{2, 3}
{1}
{1, 2, 3, 4}
'''

#Creating tuple
tp1, tp2 = tuple(), ()
#Checking the type
print(type(tp1), type(tp2), type(tp1) == type(tp2))
#Output
#<class 'tuple'> <class 'tuple'> True

#Whats inside the tuple
print(dir(tuple))
#Output
'''
['__add__', '__class__', '__class_getitem__', '__contains__',
'__delattr__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
'__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__',
'''

#Know more about the tuple
print(help(tuple.__class__))
#Output
'''
Help on class type in module builtins:

class type(object)
 |  type(object) -> the object's type
 |  type(name, bases, dict, **kwds) -> a new type
'''

#Creating tuple and getting data
tp = (1, 2, 3, 4); print(tp, tp[0], tp[1], sep = '\n')
#Output
'''
(1, 2, 3, 4)
1
2
'''

#Getting values using for loop
for val in tp: print(val)
#Output
'''
1
2
3
4
'''

#Updating list element
lst = [1, 2, 3]; lst[0] = 4; print(lst)
#Output
#[4, 2, 3]

#Updating tuple element is not possible TypeError: 'tuple' object does not support item assignment
#tp = (1, 2, 3); tp[0] = 4; print(tp)
#Conversion between tuple, set and list
lst = [1, 2, 3]; print(type(lst), lst)
#Output
#<class 'list'> [1, 2, 3]

lstTOtp = tuple(lst); print(type(lstTOtp), lstTOtp); tp = lstTOtp
#Output
#<class 'tuple'> (1, 2, 3)

lstTOset = set(lst); print(type(lstTOset), lstTOset); sct = lstTOset
#Output
#<class 'set'> {1, 2, 3}

tpTOlst = list(tp); print(type(tpTOlst), tpTOlst)
#Output
#<class 'list'> [1, 2, 3]

setTOtp = tuple(sct); print(type(setTOtp), setTOtp)
#Output
#<class 'tuple'> (1, 2, 3)

tpTOset = set(tp); print(type(tpTOset), tpTOset)
#Output
#<class 'set'> {1, 2, 3}

setTOlst = list(sct); print(type(setTOlst), setTOlst)
#Output
#<class 'list'> [1, 2, 3]
