#String formating
Dict={'Name':'Kiran','Age':'19'}
print("I am {0} and my age is {1}.".format(Dict['Name'],Dict['Age']))
print("I am {1} and my age is {0}.".format(Dict['Name'],Dict['Age']))
#Output
'''
I am Kiran and my age is 19.
I am 19 and my age is Kiran.
'''

#Other way to string formating
sentence="<{0}>This is a headerline</{1}>".format("hi",".")
print(sentence)
#Output
#<hi>This is a headerline</.>

#String formating
Dict={'Name':'Kiran','Age':'19'}
print("I am {0[Name]} and my age is {1[Age]}.".format(Dict,Dict))
print("I am {0[Age]} and my age is {1[Name]}.".format(Dict,Dict))
print("I am {0[Name]} and my age is {0[Age]}.".format(Dict))
#Output
'''
I am Kiran and my age is 19.
I am 19 and my age is Kiran.
I am Kiran and my age is 19.
'''

#Example of string formating
List=["Kiran",19]
print("My name is {0[0]} and my age is {0[1]}.".format(List))
#Output
#My name is Kiran and my age is 19.

#Class formating
class Employee():
	def __init__(self,name,age):
		self.name=name
		self.age=age
Person=Employee("Routh.Kiran",19)
print("My name is {0.name} and my age is {0.age}.".format(Person))
#Output
#My name is Routh.Kiran and my age is 19.

#Keyword formating
Sentence="My name is {name} and i am of age {age}.".format(name="Routh.Kiran",age="29")
print(Sentence)
#Output
#My name is Routh.Kiran and i am of age 29.

#Dictionary unpacking
Dict={'name':'Routh.Kiran','age':29}
print('My name is {name} and age is {age}.'.format(**Dict))
print('My name is {age} and age is {name}.'.format(**Dict))
#Output
'''
My name is Routh.Kiran and age is 29.
My name is 29 and age is Routh.Kiran.
'''

#String formating for three digits
for i in range(0,11):
	print("This is {:02}.".format(i))
#Output
'''
This is 00.
This is 01.
This is 02.
...
This is 08.
This is 09.
This is 10.
'''

#Printing 2 decimal places
pi=3.14159
print("The value of pi is {:0.2f}.".format(pi))
print("The value of pi is {:0.3f}.".format(pi))
#Output
'''
The value of pi is 3.14.
The value of pi is 3.142.
'''

#Placing comma for more understading
print("1 MB is equal to {:,} bytes.".format(1000000))
print("1 MB is equal to {:,.2f} bytes.".format(1000000))
#Output
'''
1 MB is equal to 1,000,000 bytes.
1 MB is equal to 1,000,000.00 bytes.
'''

#https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
#Date and time formating
import datetime
Datetime=datetime.datetime(2016,9,24,12,30,45)
print(Datetime)
Sentence='{:%B %d, %Y}'.format(Datetime)
print(Sentence)
#Output
'''
2016-09-24 12:30:45
September 24, 2016
'''

Datetime=datetime.datetime(2016,9,24,12,30,45)
print(Datetime)
#Becomes error for below for not having place holders
#Sentence='{:%B %d, %Y} fell on a {:%A} and was the {:%j} day of the year.'.format(Datetime)
Sentence='{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(Datetime)
print(Sentence)
#Output
'''
2016-09-24 12:30:45
September 24, 2016 fell on a Saturday and was the 268 day of the year.
'''
