condition=False
if condition:
	x=1
else:
	x=0
print(x)
#can also be written as 
condition=False
x=1 if condition else 0
print(x)

num=10_000_000
num1=12_456_555
result=num+num1
print(f"{result:,}")

try:
	f=open('sample.txt','r')
	file_content=f.read()
	f.close()
except Exception as e:
	print(e)
else:
	words=file_content.split(' ')
	word_count=len(words)
	print(word_count)
#can also be written as 
try:
	with open('sample.txt','r') as f:
		file_content=f.read()
except Exception as e:
	print(e)
else:
	words=file_content.split(' ')
	word_count=len(words)
	print(word_count)

names=['krian','kiran','routh','Rout']
index=0
for name in names:
	print(index,name)
	index+=1
#can also be written as 
for index,name in enumerate(names):
	print(index,name)
print()
#for initial starting
for index,name in enumerate(names,start=1):
	print(index,name)
#for each element
for index,name in enumerate(names[0]):
	print(index,name)

names=['krian','kiran','routh','Rout']
heros=['superman','spiderman','batman','thor']
for index,name in enumerate(names):
	hero=heros[index]
	print(f'{hero} name is {names[index]}.')
#can also be written as 
for name,hero in zip(names,heros):
	print(f'{hero} name is {name}.')
universes=['dc','marvels','dc','marvels']
for name,hero,universe in zip(names,heros,universes):
	print(f'{hero} name is {name} in {universe} universe.')

a,b=(1,2)
print(a)
print(b)

#not required is left _
a,b,c,d,_,_,_,_=(1,2,3,4,5,6,7,8)
print(a,b,c,d)
#or if needed
a,b,c,*d=(1,2,3,4,5,6,7,8)
print(a,b,c,d)
a,b,*_,d=(1,2,3,4,5,6,7,8)
print(a,b,c,d)
a,b,*c,d=(1,2,3,4,5,6,7,8)
print(a,b,c,d)

class group:
	pass 
setattr(group,'name','kira')
print(group.name)#output: kira
nameval=getattr(group,'name')
print(nameval)#output: kira

class Person():
	pass
person=Person()
person.first='krian'
person.last='routh'
print(person.first)
print(person.last)
print()
first_key='first'
first_val='kiran'
person.first_key=first_val
print(person.first)
print()
first_val='kiran1'
setattr(person,'first','Kiran')
print(person.first)
print()
first=getattr(person,first_key)
print(first)
print()
person_info={'first':'KIRAN','last':'ROUTH'}
for key,value in person_info.items():
	setattr(person,key,value)
print(person.first)
print(person.last)
print()
for key in person_info.keys():
	print(getattr(person,key))

class group:
	pass 

setattr(group,'name','kira')
print(group.name)

nameval=getattr(group,'name')
print(nameval)

class dicgroup:
	pass
import itertools
a=[x for x in range(10)]
b=[y for y in range(5)]
Dict={str(x):y for x,y in itertools.zip_longest(a,b)}
print(Dict)
for x,y in Dict.items():
	setattr(dicgroup,x,y)
	val=getattr(dicgroup,x)
	print(val)

#go to command line and observvation says that getpass will not show any writable
from getpass import getpass
username=input("username: ")
password=getpass("password: ")
print("logged in...")