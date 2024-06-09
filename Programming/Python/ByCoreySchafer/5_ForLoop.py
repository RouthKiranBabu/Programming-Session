#Creating the list
lst = list(); print(lst)
#Output
#[]

#Otherway of creating list
lstnew = []; print(lstnew)
#Output
#[]

#To check both of them are same
print(lst == lstnew)
#Output
#True

#Knowing the type
print(type(lst))
#Output
#<class 'list'>

#What is inside the lst
print(dir(lst))
#Output
'''
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
'__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getitem__', '__getstate__', '__gt__'
'''

#Knowing methods and doc
print(help(lst.__class__))
#Output
'''
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
'''

#Knowing the type of append wether it is the builtin function or not
print(type(lst.append))
#Output
#<class 'builtin_function_or_method'>

#Knowing the document of the append
print(lst.append.__doc__)
#Output
#Append object to the end of the list.

#Providing values to the list
lst, lstnew = [x for x in range(1, 11)], list(x for x in range(1, 11))
print(lst, lstnew)
#Output
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#To check the list is same
print(lst == lstnew)
#Output
#True

lst = [ele for ele in range(1, 11)]
#Using for loop to get values of the list in a single line using end = ', '
for val in lst: print(val, end = ', ')
#Output
#1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 

print()

for val in lst: 
    #Using if condition to print values if it is divisible by two
    if val%2 == 0: print(val)
#Output
'''
2
4
6
8
10
'''

#Importing builtins to check enumerate is present or not
import builtins
print(dir(builtins))
#Output
'''
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 
'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError',
'BytesWarning', 'ChildProcessError',
'''

print('enumerate' in dir(builtins))
#Output
#True

#Using enumerate For Programming
lst = list(enumerate([1, 2, 3]))
print(lst)
#Output
#[(0, 1), (1, 2), (2, 3)]

#Collecting values of enumerate from lst
index1, val1, index2, val2, index3, val3 = lst[0][0], lst[0][1], lst[1][0], lst[1][1], lst[2][0], lst[2][1]
print('First element: index = {}, value = {}.'.format(index1, val1))
#Output
#First element: index = 0, value = 1.

print('Second element: index = {}, value = {}.'.format(index2, val2))
#Output
#Second element: index = 1, value = 2.

print('Second element: index = {}, value = {}.'.format(index3, val3))
#Output
#Second element: index = 2, value = 3.

#Using for loop to get index and values from enumerate which gives index and value
lst = [x for x in range(1, 11)]
for index, value in enumerate(lst):
    print("Index is {}, and corresponding value is {}.".format(index, value))
#Output
'''
Index is 0, and corresponding value is 1.
Index is 1, and corresponding value is 2.
Index is 2, and corresponding value is 3.
Index is 3, and corresponding value is 4.
...
'''

lst = [x for x in range(11, 21)]
#Let index starts from the value 5
for index, value in enumerate(lst, start = 5):
    print(index, value)
#Output
'''
5 11
6 12
7 13
...
12 18
13 19
14 20
'''

#Creating List having tuple items
string, lst = '123', []
for val1 in string:
    for val2 in string:
        #For single line if for val1 not equal to val2
        if val1 != val2: lst.append((int(val1), val2))
#Converting Into List
lstnew = list(enumerate('123', start = 1))
print(lst, lstnew)
#Output
#[(1, '2'), (1, '3'), (2, '1'), (2, '3'), (3, '1'), (3, '2')] [(1, '1'), (2, '2'), (3, '3')]

#Geting values from tuple items of List
for num, str in lst: print(num, str)
#Output
'''
1 2
1 3
2 1
2 3
3 1
3 2

'''
