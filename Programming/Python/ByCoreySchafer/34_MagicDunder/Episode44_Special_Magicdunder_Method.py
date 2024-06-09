class Employee:
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+last+'@gmail.com'
	def fullname(self):
		return ('{} {}'.format(self.first,self.last))
	def raise_pay(self):
		self.pay=int(self.pay*1.45)

	#Used for debugging and login
	def __repr__(self):
		return "Employee('{}','{}','{}')".format(self.first,self.last,self.pay)

	#More readable representation of object or used to deplay purpose for user repr is must 
	#when representing str
	def __str__(self):
		return '{}-{}'.format(self.fullname(),self.email)

	#Dunder add method
	def __add__(self,other):
		return self.pay+other.pay

	#For finding the length of full name 
	def __len__(self):
		return len(self.fullname())


emp_1=Employee('routh','kiran',50000)
emp_2=Employee('Routh','kiran',60000)

#This result is not apropriate to user friendly when repr def is not declared output
#will be '<__main__.Employee object at 0x0000006946C0EAC8>'

#If repr is declared the output will be 'Employee('routh','kiran','50000')'

#If str is declared then the output will be 'routh kiran-routhkiran@gmail.com'
print('print(emp_1)')
print(emp_1)
print('print(repr(emp_1))')
print(repr(emp_1))
print('print(str(emp_1))')
print(str(emp_1))

#Dunder add method
print('print(1+2)')
print(1+2)
print('print(int.__add__(1,2))')
print(int.__add__(1,2))
print('print(str.__add__(a,b))')
print(str.__add__('a','b'))
print('print(emp_1+emp_2)')
print(emp_1+emp_2)
print('print(len(test))')

print(len('test'))
print('print(test.__len__())')
print('test'.__len__())
print('print(len(emp_1))')
print(len(emp_1))

