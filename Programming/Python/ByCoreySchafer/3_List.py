#Creating List
lst = list()
print(lst)
#Output
#[]

print(lst == [])
#Output
#True

#Know more about the list and methods in it
print(help(list))
#Output
'''
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
'''

#Doc of the list
print(list.__doc__)
#Output
'''
Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.
'''

#Doc of the list.remove
print(list.remove.__doc__)
#Output
'''
Remove first occurrence of value.

Raises ValueError if the value is not present.
'''

"""The content can be chaged without changing the identity are called as
mutable. The objects like lists and dictionaries.
The content that cannot be changable called as immutable. Example like
string and tuples"""
#Providing values in the list
playlist = ['Engineering Mathematics', 'Network Theory', 'Signals and Systems']
#Finding the number of elements present
print('The playlist {} has {} number of elements.'.format(playlist, len(playlist)))
#Output
#The playlist ['Engineering Mathematics', 'Network Theory', 'Signals and Systems'] has 3 number of elements.

#Providing values in the list
playlist = ['Engineering Mathematics', 'Network Theory', 'Signals and Systems']
#First index is 0 and last index is -1
print(playlist[0], playlist[1], playlist[2], playlist[-1], sep = "\n")
#Output
'''
Engineering Mathematics
Network Theory
Signals and Systems
Signals and Systems
'''

#Start printing from 0 and Stop printing for index 2
print(playlist[0 : 2])
#Output
#['Engineering Mathematics', 'Network Theory']

#To check what inside the list
print(dir(list))
#Output
'''
['__add__', '__class__', '__class_getitem__', '__contains__', 
'__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__',
'''

#To know about append
print(help(list.append))
#Output
'''
Help on method_descriptor:

append(self, object, /) unbound builtins.list method
    Append object to the end of the list.
'''

#Doc about append
print(list.append.__doc__)
#Output
#Append object to the end of the list.

#Providing values in the list
playlist = ['Engineering Mathematics', 'Network Theory', 'Signals and Systems']
print(playlist)
#Output
#['Engineering Mathematics', 'Network Theory', 'Signals and Systems']

#Adding elements to the last index
playlist.append('Digital Electronics')
print(playlist)
#Output
#['Engineering Mathematics', 'Network Theory', 'Signals and Systems', 'Digital Electronics']

#Adding elements to the target index
playlist.insert(1, 'Control Systems')
print(playlist)
#Output
#['Engineering Mathematics', 'Control Systems', 'Network Theory', 'Signals and Systems']

#Creating list having inner list or sublist
lst = [['1', '2'], [3, 4, 5], [6.54, 7.45, 8.12, 9.45]]
print(lst); newlst = [True, False, False, True, True]
#output
#[['1', '2'], [3, 4, 5], [6.54, 7.45, 8.12, 9.45]]

#Inserting a new list at the index one
lst.insert(1, newlst); print(lst)
#To get the value int 3
print(lst[2][0]); print("Integer list at {}, 3 at {} of type is {}.".format(2, 0, type(lst[2][0])))
#Output
'''
[['1', '2'], [True, False, False, True, True], [3, 4, 5], [6.54, 7.45, 8.12, 9.45]]
3
Integer list at 2, 3 at 0 of type is <class 'int'>.
'''

#Creating list having inner list or sublist
lst = [['1', '2'], [3, 4, 5], [6.54, 7.45, 8.12, 9.45]]
print(lst); newlst = [True, False, False, True, True]
#Output
#[['1', '2'], [3, 4, 5], [6.54, 7.45, 8.12, 9.45]]

#Inserting a new list at the index one
lst.insert(1, newlst); print(lst)
#Output
#[['1', '2'], [True, False, False, True, True], [3, 4, 5], [6.54, 7.45, 8.12, 9.45]]

#To get the value int 3
print(lst[2][0]); print("Integer list at {}, 3 at {} of type is {}.".format(2, 0, type(lst[2][0])))
#Output
'''
3
Integer list at 2, 3 at 0 of type is <class 'int'>.
'''

lst1, lst2 = [1, 2, 3], [True, False, True]
#Adds elements at the last index by using extend
lst1.extend(lst2), print(lst1, lst2, sep = '\n'),#With ,
#Output
'''
[1, 2, 3, True, False, True]
[True, False, True]
'''

lst1.extend(lst2); print(lst1, lst2, sep = '\n');#With ;
#Output
'''
[1, 2, 3, True, False, True]
[True, False, True]
'''

lst = [1, 2, 3]
#Know about pop
print(lst.pop.__doc__, help(lst.pop), end = 100*"*" + '\n')
#Output
'''
Help on built-in function pop:

pop(index=-1, /) method of builtins.list instance
    Remove and return item at index (default last).

Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range. 
None********************************************************
******************************************
'''

#Use the pop to remove the last element and store the return value
popvalue = lst.pop(); print(popvalue, lst)
#Output
#3 [1, 2]

#Removing element based on index
lst = [1, 4, 3]
retval = lst.pop(1)
print(retval, lst)
#Output
#4 [1, 3]

lstint = [1, 3, 2]; print("Use of Reverse", lstint, sep = '\n')
#Use of Reverse
returnvalue = lstint.reverse(); print(lstint, returnvalue, '\n\nUse of list.sort')
#Output
'''
Use of Reverse
[1, 3, 2]
[2, 3, 1] None 

Use of list.sort
'''

#Use of Sort
lstint, lststr = [1, 3, 2], ['One', 'Four', 'Two']; print(lstint, lststr)
#Output
#[1, 3, 2] ['One', 'Four', 'Two']

returnvalue = lstint.sort(); print(lstint, returnvalue)
#Output
#[1, 2, 3] None

returnvalue = lststr.sort(); print(lststr, returnvalue, '\n\nUse of list.sort(reverse = true)')
#Output
'''
['Four', 'One', 'Two'] None 

Use of list.sort(reverse = true)
'''

#Use of Sort reverse True
lstint, lststr = [1, 3, 2], ['One', 'Four', 'Two']; print(lstint, lststr)
#Output
#[1, 3, 2] ['One', 'Four', 'Two']

returnvalue = lstint.sort(reverse = True); print(lstint, returnvalue)
#Output
#[3, 2, 1] None

returnvalue = lststr.sort(reverse = True); print(lststr, returnvalue, '\n\nUse of Sorted(list)')
#Output
'''
['Two', 'One', 'Four'] None 

Use of Sorted(list)
'''

#Use of Sorted which returns a value
lstint, lststr = [1, 3, 2], ['One', 'Four', 'Two']; print(lstint, lststr)
#Output
#[1, 3, 2] ['One', 'Four', 'Two']

returnvalue = sorted(lstint); print(lstint, returnvalue)
#Output
#[1, 3, 2] [1, 2, 3]

returnvalue = sorted(lststr); print(lststr, returnvalue, '\n')
#Output
#['One', 'Four', 'Two'] ['Four', 'One', 'Two'] 

numlist = [3, 4, 1]; print(numlist)
#Output
#[3, 4, 1]

#Use of Max, Min and Sum to find the maximum, minimum and sum of elements
bigval, smallval, sumval = max(numlist), min(numlist), sum(numlist)
print("Big value: "+ str(bigval) + ", Small value: " + str(smallval) + ", Sum of values: " + str(sumval))
#Output
#Big value: 4, Small value: 1, Sum of values: 8

numlist = ['zeroIndexValue', 'oneIndexValue', 'twoIndexValue', 'threeIndexValue']
#Returns the use of index of list type
print(type(numlist), numlist.index('oneIndexValue'))
#Output
#<class 'list'> 1

#To check the element is in the list or not
print('Some value' in numlist)
#Output
#False

#'zeroIndexValue' is in the numlist
print('zeroIndexValue' in numlist)
#Output
#True

#Joins all elements in the list element
lst = ['one', 'two', 'three']
jndval = '_'.join(lst); print(jndval)
#Output
#one_two_three

#Split is used for the creating sentence to the list
strval = "This is the sentence."
sptval = strval.split(' '); print(sptval)
#Output
#['This', 'is', 'the', 'sentence.']

#Easiest way to Convert word to the List of letters
word = 'RouthKiranBabuSaysJaiSriRam'
print(list(word))
#Output
#['R', 'o', 'u', 't', 'h', 'K', 'i', 'r', 'a', 'n', 'B', 'a', 'b', 'u', 'S', 'a', 'y', 's', 'J', 'a', 'i', 'S', 'r', 'i', 'R', 'a', 'm']
