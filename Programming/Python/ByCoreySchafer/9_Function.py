"""
Instead of making same process again and again there is a simple way
to give input to a function and process it and gives the desired
value in return.
"""

#pass command does nothing and just to make a function.
def Pass_Function():
    pass

#Shows the function location.
print(Pass_Function)
#Output
#<function Pass_Function at 0x000002794CD0A2A0>

#It show None becouse function didn't return anything.
print(Pass_Function())
#Output
#None

#Executes when function calls below the function declared.
def default_Print_Function():
    print("Hello, World.")

#Function call.
default_Print_Function()
#Output
#Hello, World.

#Shows number of none 
print(print(print(print("hello"))))
#Output
'''
hello
None
None
None
'''

#Returning from functions
def Function():
	return "This is function!"
print(Function(),Function().upper())
#Output
#This is function! THIS IS FUNCTION!

#Sending values to functions
def Greetings(name):
	return "hi! {}.".format(name)
print(Greetings("Routh.kiran").upper())
#Output
#HI! ROUTH.KIRAN.

#Placing default string in functions
def Greetings(name,AnotherGreetings="How are you"):
	return "hi! {}, {}.".format(name,AnotherGreetings)
print(Greetings("Routh.kiran").upper()) 
print(Greetings("Routh.kiran","How do you do").upper())
#Output
'''
HI! ROUTH.KIRAN, HOW ARE YOU.
HI! ROUTH.KIRAN, HOW DO YOU DO.
'''

#Changing the default string in the functions
def Greetings(name,AnotherGreetings="How are you"):
	return "hi! {}, {}.".format(name,AnotherGreetings)
print(Greetings("Routh.kiran",AnotherGreetings="How do you do!").upper()) 
#Output
#HI! ROUTH.KIRAN, HOW DO YOU DO!.

#Creating tuples and dictinaries by functions
def Student_info(*Tuple,**Dictionaries):
	print(Tuple)
	print(Dictionaries)
Student_info("My name","is kiran",name="Kiran",age="19")
#Output
'''
('My name', 'is kiran')
{'name': 'Kiran', 'age': '19'}
'''

#Testing for above function
def Student_info(*Tuple,**Dictionaries):
	print("Testing"+str(Tuple))
	print(Dictionaries)
List=["name","fame"]
Dict={"Name":"Kiran","Fame":"Student"}
Student_info(List,Dict)
Student_info(*List,**Dict)
#Output
'''
Testing(['name', 'fame'], {'Name': 'Kiran', 'Fame': 'Student'})
{}
Testing('name', 'fame')
{'Name': 'Kiran', 'Fame': 'Student'}
'''

#Program for leap year
Month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def leap_year(Year):
	return Year %4==0 and (Year % 100 != 0 or Year % 400 == 0)
def days_in_months(Year,Month):
	if not 1<=Month<=12:
		return "Invalid month!"
	if Month==2 and leap_year(Year):
		return 29
	return Month_days[Month]
for x in range(1998,2009):
	print(leap_year(x))
	for y in range(1,12):
		print(days_in_months(x,y),end=" ")
	print()
#Output
'''
False
31 28 31 30 31 30 31 31 30 31 30 
False
31 28 31 30 31 30 31 31 30 31 30 
True
31 29 31 30 31 30 31 31 30 31 30 
False
31 28 31 30 31 30 31 31 30 31 30 
False
31 28 31 30 31 30 31 31 30 31 30 
False
31 28 31 30 31 30 31 31 30 31 30 
True
31 29 31 30 31 30 31 31 30 31 30 
False
31 28 31 30 31 30 31 31 30 31 30 
False
31 28 31 30 31 30 31 31 30 31 30 
False
31 28 31 30 31 30 31 31 30 31 30 
True
31 29 31 30 31 30 31 31 30 31 30 
'''
