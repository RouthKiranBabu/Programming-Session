'''
#Importing used made module in same directory as the rename called Module
import Mymodule as Module

#Line 17 is written as [index=Module.Find_Index(courses,'physics')]
'''

#Importing only Find_Index and Test from Mymodule or can be written as 
#from Mymodule import *
from Mymodule import Find_Index as FI,Test as T

#Creating a list
courses=['History','math','physics','compsci']

#Calling a module inbuilt function
#Sending list name courses and the element to the function
index=FI(courses,'physics')

print(index)
<<<<<<< HEAD


=======
>>>>>>> e58f9d753d42ed589b79667eadd6224767bdcffa
