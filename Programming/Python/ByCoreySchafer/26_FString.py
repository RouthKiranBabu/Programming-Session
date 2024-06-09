firstName="Routh"
lastName="Kiran"
sentence="My name is {} {}.".format(firstName,lastName)
print(sentence)

#f is used to rechorgnise that it is a f string or formated string
firstName="Routh"
lastName="Kiran"
sentence=f"My name is {firstName} {lastName}."
sentence1=f"My name is {firstName.upper()} {lastName.lower()}."
print(sentence,sentence1)
print()

Dict={"Name":"Routh.Kiran","Age":14}
sentence="My name is {} and i am {} years old.".format(Dict['Name'],Dict['Age'])
print(sentence)
Dict={"Name":"Routh.Kiran","Age":14}
sentence=f"My name is {Dict['Name']} and i am {Dict['Age']} years old."
print(sentence)
print()

calculation=f"2 time the 11 = {2*11}"
print(calculation)
for n in range(1,11):
	print(f"The number is {n}")
print()

#For two padding
for n in range(1,11):
	print(f"The number is {n:02}")
for n in range(1,11):
	print(f"The number is {n:05}",end=" ")
print()

pi=3.14159265
sentence=f"The value of pi is {pi}"
print(sentence)

#Dot represents the point right side value up to 4 digits of f means floating value
pi=3.14159265
sentence=f"The value of pi is {pi:.4f}"
sentence1=f"The value of pi is {pi:.6f}"
print(sentence,"\n",sentence1)

from datetime import datetime
DOB= datetime(1998,9,14)
print(f"Date of birth is {DOB}")
print(f"Date of birth is {DOB:%B %d, %Y}")