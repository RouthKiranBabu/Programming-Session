#To sort a random order list
rand=[9,2,3,5,6,7,4,3,21,5,8,6,4]
Sorted=sorted(rand)
print("Sorted List is:\t",Sorted)
print("Unsorted List:\t",rand)
#Output
'''
Sorted List is:	 [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 21]
Unsorted List:	 [9, 2, 3, 5, 6, 7, 4, 3, 21, 5, 8, 6, 4]
'''

#To sort the original
rand.sort()
print("Original Sorted List: ",rand)
#Output
#Original Sorted List:  [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 21]

#To sort and reverse
rand=[9,2,3,5,6,7,4,3,21,5,8,6,4]
Sorted=sorted(rand,reverse=True)
print("Sorted and Reversed List is:\t",Sorted)
rand.sort(reverse=True)
print("Original Sorted and Reversed List: ",rand)
#Output
'''
Sorted and Reversed List is:	 [21, 9, 8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2]
Original Sorted and Reversed List:  [21, 9, 8, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2]
'''

#To sort the tuple
Tup=(2,1,2,5,6,8,7,7,8,6,5,4)
S_Tup=sorted(Tup)
print("Sorted tuple: ",S_Tup)
#Output
#Sorted tuple:  [1, 2, 2, 4, 5, 5, 6, 6, 7, 7, 8, 8]

#To sort the dictionary
Dic={'1':'one','2':'two','0.1':'zero point one'}
S_Dic=sorted(Dic)
print(S_Dic)
#Output
#['0.1', '1', '2']

#To print in ascending order by negleting positive or negitive value
num=[-1,-2,1,2,1.2]

#List num goes into abs key and that value is given to sorted to sort element of num
S_num=sorted(num,key=abs)
print(S_num)
#Output
#[-1, 1, 1.2, -2, 2]

#Class sorting
class Employee():
	def __init__(self, name, age, salary):
		self.name=name
		self.age=age
		self.salary=salary
	#Function inbuilt that says python how to format
	def __repr__(self):
		return '({},{},${})'.format(self.name,self.age,self.salary)
e1=Employee("Routh",14,2500000)
e2=Employee("Kiran",15,2600000)
e3=Employee("Routh_Kiran",28,5000000)

Employees=[e1,e2,e3]

#Custom Function to sort name
def e_sort(emp):
	return emp.name

#Employees list is sent into e_sort function and returns the corresponding name to sorted to sort
S_Employee=sorted(Employees,key=e_sort)

#Custom Function to sort age
print('S_Employee=sorted(Employees,key=e_sort)',S_Employee)
#Output
#S_Employee=sorted(Employees,key=e_sort) [(Kiran,15,$2600000), (Routh,14,$2500000), (Routh_Kiran,28,$5000000)]

def e_sort(emp):
	return emp.age
S_Employee=sorted(Employees,key=e_sort)
print(S_Employee)
#Output
#[(Routh,14,$2500000), (Kiran,15,$2600000), (Routh_Kiran,28,$5000000)]

#Custom Function to sort salary in ascending order
print(S_Employee)
def e_sort(emp):
	return emp.salary
S_Employee=sorted(Employees,key=e_sort)
print(S_Employee)
#Output
'''
[(Routh,14,$2500000), (Kiran,15,$2600000), (Routh_Kiran,28,$5000000)]
[(Routh,14,$2500000), (Kiran,15,$2600000), (Routh_Kiran,28,$5000000)]
'''

#Custom Function to sort salary in reverse order
print(S_Employee)
def e_sort(emp):
	return emp.salary
S_Employee=sorted(Employees,key=e_sort,reverse=True)
print(S_Employee)
#Output
'''
[(Routh,14,$2500000), (Kiran,15,$2600000), (Routh_Kiran,28,$5000000)]
[(Routh_Kiran,28,$5000000), (Kiran,15,$2600000), (Routh,14,$2500000)]
'''

#Custom Function to sort name using lambda
S_Employee=sorted(Employees,key=lambda e: e.name)

#Custom Function to sort age
print(S_Employee)
#Output
#[(Kiran,15,$2600000), (Routh,14,$2500000), (Routh_Kiran,28,$5000000)]

from operator import attrgetter
#Custom Function to sort name using lambda
S_Employee=sorted(Employees,key=attrgetter('name'))

#Custom Function to sort age
print(S_Employee)
#Output
#[(Kiran,15,$2600000), (Routh,14,$2500000), (Routh_Kiran,28,$5000000)]
