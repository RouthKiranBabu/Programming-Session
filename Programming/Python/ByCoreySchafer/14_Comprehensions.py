#Just copping the list or dulplication
n=[1,2,3,4,5,6]
l=[]
for item in n:
	l.append(item)
#print(l)
#Output
#[1, 2, 3, 4, 5, 6]

#The above for loop can be written as
num=[item for item in n]
print(num)
#Output
#[1, 2, 3, 4, 5, 6]

#Squaring each element
n=[1,2,3,4,5,6]
l=[]
for item in n:
	l.append(item**2)
print(l)
#Output
#[1, 4, 9, 16, 25, 36]

#The above for loop can be written as
num=[item**2 for item in n]
print(num)
#Output
#[1, 4, 9, 16, 25, 36]

#Map runs every thing of certain range of function
#Does the same as above code
List=map(lambda n: n**2,n)
print("Location: "+str(List))
List=set(List)
print("Using map and lambda: "+str(List))
#Output
'''
Location: <map object at 0x000001C3D8C045B0>
Using map and lambda: {1, 4, 36, 9, 16, 25}
'''

#This function is used for multiple or divisible by two
num=[]
for item in n:
	if item%2==0:
		num.append(item)
print(num)
#Output
'''
[2, 4, 6]
'''

#Above forloop can be written as 
n=[1,2,3,4,5,6]
i=[item for item in n if item%2==0]
print(i)
#Output
#[2, 4, 6]

#Does the same as above three statements
mylist=filter(lambda n:n%2 ==0,n)
print("Filter location: "+str(mylist))
mylist=set(mylist)
print("Mylist: "+str(mylist))
#Output
'''
Filter location: <filter object at 0x00000210C2CB4B80>
Mylist: {2, 4, 6}
'''

#Making each letter corresponds to range 0 to 3
n=[]
for letter in "abcd":
	for num in range(4):
		n.append([num,letter])
print(n)
#Output
'''
[[0, 'a'], [1, 'a'], [2, 'a'], [3, 'a'], [0, 'b'], [1, 'b'], 
[2, 'b'], [3, 'b'], [0, 'c'], [1, 'c'], [2, 'c'], [3, 'c'], 
[0, 'd'], [1, 'd'], [2, 'd'], [3, 'd']]
'''

#Does same output as before
n=[[num,letter] for letter in "abcd" for num in range(4)]
print(n)
#Output
'''
[[0, 'a'], [1, 'a'], [2, 'a'], [3, 'a'], [0, 'b'], [1, 'b'], [2, 'b'], 
[3, 'b'], [0, 'c'], [1, 'c'], [2, 'c'], [3, 'c'], [0, 'd'], [1, 'd'], 
[2, 'd'], [3, 'd']]
'''

#Creating a dictionary having pair of element in tuple
name=['Bruce','Clark','Peter','Logan','Wade']
Hero=['Batman','Superman','Spiderman','Wolverine','Deadpool']
Set=set(zip(name,Hero))
print(Set)
#Output
'''
{('Clark', 'Superman'), ('Bruce', 'Batman'), ('Logan', 'Wolverine'), 
('Peter', 'Spiderman'), ('Wade', 'Deadpool')}
'''

#Just making a dictionary
dicti={}
for name,Hero in Set:
	dicti[name]=Hero
print("Dictionary: "+str(dicti))
#Output
'''
Dictionary: {'Peter': 'Spiderman', 'Logan': 'Wolverine', 
'Bruce': 'Batman', 'Clark': 'Superman', 'Wade': 'Deadpool'}
'''

#Just same output as before
Dict={name:Hero for name,Hero in Set}
print("Comprehension: "+str(Dict))
#Output
'''
Comprehension: {'Clark': 'Superman', 'Peter': 'Spiderman', 
'Logan': 'Wolverine', 'Wade': 'Deadpool', 'Bruce': 'Batman'}
'''

#For not including peter key and value in dictionary
Dict={name:Hero for name,Hero in Set if name!="Peter"}
print("Comprehension: "+str(Dict))
#Output
'''
Comprehension: {'Wade': 'Deadpool', 'Logan': 'Wolverine', 
'Bruce': 'Batman', 'Clark': 'Superman'}
'''

#Use of set is stops repetation
List=[1,1,1,2,3,4,4,5,6,7,7,7,6,3,4,5,6,7,7]
Set=set()
for n in List:
	Set.add(n)
print(Set)
#Output
#{1, 2, 3, 4, 5, 6, 7}

#Above comprehension is
List=[1,1,1,2,3,4,4,5,6,7,7,7,6,3,4,5,6,7,7]
Set={n for n in List}
print(Set)
#Output
#{1, 2, 3, 4, 5, 6, 7}

#Generators and yield commands
num=[1,2,3,4,5,6,7,8,9,10]
def Generator(num):
	for n in num:
		yield n*n
My_gen=Generator(num)
for i in My_gen:
	print("->", i)

comp=(n*n for n in num)
print(comp)
for i in My_gen:
	print(i)
#Output
'''
-> 1
-> 4
-> 9
-> 16
-> 25
-> 36
-> 49
-> 64
-> 81
-> 100
<generator object <genexpr> at 0x000002CA021FC520>
'''
