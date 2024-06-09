#If statement.
Condition = True
if Condition:
    print("Condition is True.")    
if False*Condition:
    print("Condition is False.")
if Condition != False:
    print("Condition is True again.")
#Output
'''
Condition is True.
Condition is True again.
'''

a = b = 1
#Checking the identity of the object like variable.
print(id(a), id(b), a is b, "", sep = "\n")
#Output
'''
140703771204024
140703771204024
True
'''

print(a == b, a != b, sep = "\n")
#Output
'''
True
False
'''

#OR operator is true if any one of the condition is true.
if "" or None or {} or []:
    print("True for empty string, empty set, None and empty list.")
else:
    print("False for empty string, empty set, None and empty list.")
#Output
#False for empty string, empty set, None and empty list.

#AND operator is true if all the condition is true.
if "element_1" and {"Element_1"} and ["eLEMENT_1"]:
    print("True for element is present.")
    if 0:
        print("True for zero.")
    if 1 and 10 and -1:
        print("True for 1, 10, and -1.")
else:
    print("False for element is present.")
#Output
'''
True for element is present.
True for 1, 10, and -1.
'''  
