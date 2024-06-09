#When certain python module is in different location you can call or import by sys module
import sys

#Location of directory where the module name mymodule is present
sys.path.append('/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary')
from Mymodule import *


#Creating a list
courses=['History','math','physics','compsci']

#Calling a module inbuilt function
#Sending list name courses and the element to the function
index=Find_Index(courses,'physics')

print(index)
print(Test)

#Prints sys paths available to search or import module
print(sys.path)