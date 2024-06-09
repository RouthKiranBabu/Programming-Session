#Knowing the type of int and float
three, pi = 3, 3.14
print("The type of {} is {}.".format(three, type(three)))
#Output
#The type of 3 is <class 'int'>.

print("The type of {} is {}.".format(pi, type(pi)))
#Output
#The type of 3.14 is <class 'float'>.

#Use of single and double Slash
pinum, piden = 22, 7
doubleslashpi,singleslashpi = pinum//piden, pinum/piden 
print(doubleslashpi,singleslashpi)
#Output
#3 3.142857142857143

#Double star is used for the number to the power
five, PowerTwo = 5, 2
print('Number**Power=> {}**{} = {}.'.format(five, PowerTwo, five**PowerTwo))
#Output
#Number**Power=> 5**2 = 25.

#Know about abs built-in function abs in module builtins
print(help(abs))
#Output
'''
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
'''

NegNum = -1; print('The absolute value of {} is {}.'.format(NegNum, abs(NegNum)))
#Output
#The absolute value of -1 is 1.

#Variables storing string type value
str1, str2 = '1', '2'
print('The sum of {} and {} is {}.'.format(str1, str2, str1 + str2))
#Output
#The sum of 1 and 2 is 12.

#Converting into the integer
int1, int2 = int(str1), int(str2)
#After converting into the integer doing the addition of numbers
print('The sum of {} and {} is {}.'.format(int1, int2, int1 + int2))
#Output
#The sum of 1 and 2 is 3.

#Variables storing string type value
str1, str2 = '1.23', '2.45'
print('The sum of {} and {} is {}.'.format(str1, str2, str1 + str2))
#Output
#The sum of 1.23 and 2.45 is 1.232.45.

#Converting into the float
float1, float2 = float(str1), float(str2)
#After converting into the float and then doing the addition of float numbers
print('The sum of {} and {} is {}.'.format(float1, float2, float1 + float2))
#Output
#The sum of 1.23 and 2.45 is 3.68.

#Creating different type Knowing about it without Providing values
float1, float2, int1, str1 = float(), float, int(), str()
print(type(float1), type(float2), type(int1), type(str1))
#Output
#<class 'float'> <class 'type'> <class 'int'> <class 'str'>

print(float1, float2, int1, str1, sep = "-")
#Output
#0.0-<class 'float'>-0-

#Knowing about float
print(help(float2))
#Output
'''
Help on class float in module builtins:

class float(object)
 |  float(x=0, /)
'''

print(float2 == float1)
#Output
#False

#Float with and without brackets are not same
float3 = float()
print(float1 == float3, float1 == float2)
#Output
#True False

print(3.23 + float1)
#print(3.23 + float2)#Creates Type error
#Output
#3.23
