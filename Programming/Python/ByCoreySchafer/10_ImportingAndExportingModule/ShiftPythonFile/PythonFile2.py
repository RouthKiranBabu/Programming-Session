#Importing a module random for random operations
import random

#Importing maths for maths inbuilt programs
import math

#Importing datetime and os module
import datetime
import os

#Importing a module which shows a file in webbrowser
#This module or python file is present in location: C:\Python\Python36\Lib
#import antigravity

#For printing choices from a list
courses=['History','math','physics','compsci']
Random=random.choice(courses)
print(Random)

Radian=math.radians(90)
print("Radian="+str(Radian),". Its sin value: "+str(math.sin(Radian)))

today=datetime.datetime.today()
Date=datetime.date.today()
print(today)
print(Date)

#For printing current directory
print(os.getcwd())