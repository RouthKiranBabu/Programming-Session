#Creating Variable
tesstr = 'This is a string type.'

#Shows Method document
print(tesstr.upper.__doc__)
#Output
#Return a copy of the string converted to uppercase.

#Now Lets use the method upper
retval = tesstr.upper(); print(retval)
#Output
#THIS IS A STRING TYPE.

#Makes the message to lower case
print(tesstr.lower())
#Output
#this is a string type.

#To check builtin_function_or_method
print(type(tesstr.count), type(tesstr.find))
#Output
#<class 'builtin_function_or_method'> <class 'builtin_function_or_method'>

#To count number of 's' in tesstr
print(tesstr.count('s'))
#Output
#3

#To find the index where 'h' is present
print(tesstr.find('h'))
#Output
#1

#Single line variables creating storing values having slash
message1, message2 = 'That\'s Typing!', 'https://github.com/RouthKiranBabu/PythonReference/blob/main/1_String.py'
print(message1, message2)
#Output
#That's Typing! https://github.com/RouthKiranBabu/PythonReference/blob/main/1_String.py

#Use of replace method type
mline = """This is a multiline 
Comment."""
line = "This is a single line."
print(mline, line)
#Output
'''
This is a multiline 
Comment. This is a single line.
'''

val1, val2 = mline.replace(" \nComment.", "."), line.replace(" line", "")
print(val1, val2)
#Output
#This is a multiline. This is a single.

#Attaching Two Strings
str1, str2 = 'string one!', 'string two!'
val = str1 + ' and ' + str2; print(val)
#Output
#string one! and string two!

#Difference of number addition and string addition
num1, num2 = 1, 2
sumint1_2 = num1 + num2; print(sumint1_2)
#Output
#3

str1, str2 = str(num1), str(num2)
sumstr1_2 = "Sum of string: " + str1 + str2; print(sumstr1_2)
#Output
#Sum of string: 12

#Knowing the type
print(type(num1))
#Output
#<class 'int'>

#Sum of integers
sumint1_2 = num1 + num2
#Knows about format format present in the string so converted int to str
print(help(str(num1).format))
#Output
'''
Help on built-in function format:

format(...) method of builtins.str instance
    S.format(*args, **kwargs) -> str
'''

#Use the format method of builtins.str -> str
print("The sum of {} and {} is {}.".format(num1, num2, sumint1_2))
#Output
#The sum of 1 and 2 is 3.

#Converting into string
str1, str2 = str(num1), str(num2)
#Addition of string
sumstr1_2 = "Sum of string: " + str1 + str2; print(sumstr1_2)
#Output
#Sum of string: 12

#Whats inside the str
print(dir(str))
#Output
'''
['__add__', '__class__', '__contains__', '__delattr__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__',
'__init__',
'''

#Doc and methods of str
print(help(str.__class__))
#Output
'''
Help on class type in module builtins:

class type(object)
 |  type(object) -> the object's type
 |  type(name, bases, dict, **kwds) -> a new type
'''

#Whats inside the str.replace method
print(dir(str.replace))
#Output
'''
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', 
'__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
'''

val = 'stri'
print(dir(val.replace))
#Output
'''
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', 
'__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', 
'__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
'''

print(dir(str.replace) == dir(val.replace))
#Output
#False

print(dir(str.replace) == dir(str.replace))
#Output
#True
