Number_List = [1, 12, 321, 21]
for number in Number_List:
    print(number)
#Output
'''
1
12
321
21
'''

#Deleting the variable.
del Number_List
"""
Make a list with using forloop and find the element using forloop use
break statement.
"""
Number_List = [element for element in range(1,11)]
Finding_Element = 6
for index, element in enumerate(Number_List):
    #Instead of is you can use comparison operator (i.e., ==).
    if element is Finding_Element:       
        print("{} is found {}.".format(Finding_Element, index))
        #Breaks the Whole loop.
        break   
    print("{} is not {} at {}.".format(Finding_Element, element, index))
del Number_List, Finding_Element
#Output
'''
6 is not 1 at 0.
6 is not 2 at 1.
6 is not 3 at 2.
6 is not 4 at 3.
6 is not 5 at 4.
6 is found 5.
'''

#Use of continue statement.
Number_List = [2*element for element in range(1, 11)]
for number in Number_List: 
    if number < 11:   
        print(number)
        #Skips the below portion.
        continue
    if number >  10:
        """
        Please note that it does'nt continue so it will print the
        element twice.
        """
        print(number)     
    print(number)
#Output
'''
2
4
6
8
10
12
12
14
14
16
16
18
18
20
20
'''

"""
#
Without using enumerate and global variable for displaying index and
element using nested for loop and continue and break statement.
"""
Number_List = [x for x in range(11)]
for number in Number_List: 
    for character in "abcdefghijk":
        _number = number     
        if number > _number:
            continue
        print("{} is found at {}.".format(character, number))
        number += 1
    if number > len(Number_List) - 1:
        break
#Output
'''
a is found at 0.
b is found at 1.
c is found at 2.
d is found at 3.
e is found at 4.
f is found at 5.
g is found at 6.
h is found at 7.
i is found at 8.
j is found at 9.
k is found at 10.

'''

#Print even number element from 5 to 20.
#6 is the starting number and 21 is not included and 2 is the step.
for number in range(6, 21, 2):
    print(number)
#Output
'''
6
8
10
12
14
16
18
20

'''

#The above code is also writen in while loop.
start_Number, end_Number, Step = 6, 21, 2
while end_Number > start_Number:
    print(start_Number)
    start_Number += Step
print("", start_Number, sep = "\n")
#Output
'''
6
8
10
12
14
16
18
20

22
'''

#Breaking the infinite Loop.
start_Number = 6
while True:  
    print(start_Number)
    start_Number += Step   
    if start_Number > end_Number:
        print("Stops here.")
        break
#Output
'''
6
8
10
12
14
16
18
20
Stops here.
'''

st = "this"
for x in reversed(st): print(x)
#Output
#s
#i
#h
#t
