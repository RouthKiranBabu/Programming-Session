class Employee:
	def __init__(self,first,last,pay):
		self.firstname=first
		self.lastname=last
		self.pay=pay
		self.email=first+last+'@gmail.com'
	def fullname(self):
		return ('{} {}'.format(self.firstname,self.lastname))
	def raise_pay(self):
		self.pay=int(self.pay*1.45)

emp1=Employee('routh','kiran',2500)
print(emp1.fullname())

print(emp1.pay)
emp1.raise_pay()
print(emp1.pay)
print()

class employee:
	raise_amount=1.45
	no_of_employee=0
	def __init__(self,first,last,pay):
		self.firstname=first
		self.lastname=last
		self.pay=pay
		self.email=first+last+'@gmail.com'
		employee.no_of_employee+=1
	def fullname(self):
		return ('{} {}'.format(self.firstname,self.lastname))
	def raise_pay(self):
		#If you write [self.pay=int(self.pay*raise_amount)] NameError: name 'raise_amount' is not defined 
		#To stop this 
		self.pay=int(self.pay*self.raise_amount)
		#or self.pay=int(self.pay*self.raise_amount)
emp2=employee('routh','kiran',2134)
print(emp2.pay)
emp2.raise_pay()
print(emp2.pay)
print(emp2.raise_amount)
print(employee.raise_amount)
#Doesnt show raise amount
print(emp2.__dict__)
#Does show raise amount
print(employee.__dict__)
print()

#Changing class variables if not by default it takes 1.45
emp2.raise_amount=1.05
employee.raise_amount=4.05
print(emp2.raise_amount)
print(employee.raise_amount)
print(emp2.__dict__)
print(employee.__dict__)

#To know no of employee
print(employee.no_of_employee)

#Standard class
class Employee:
	raise_amount=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
	def email(self):
		return "{}.{}'@gmail.com'".format(self.first,self.last)
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	def raise_amt(self):
		self.pay=int(self.pay*Employee.raise_amount)
emp_1=Employee('routh','krian',190000)
print(emp_1.fullname())
print(emp_1.email())
print(emp_1.pay)
emp_1.raise_amt()
print(emp_1.pay)
print(Employee.email(emp_1))
print()

#doesnt change the raise amount 
class Employee:
	raise_amount=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
	def email(self):
		return "{}.{}'@gmail.com'".format(self.first,self.last)
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	def raise_amt(self):
		self.pay=int(self.pay*Employee.raise_amount)
emp_1=Employee('routh','krian',190000)
print(emp_1.fullname())
print(emp_1.email())
print(emp_1.pay)
#we didnt change Employee.raise_amount value becouse we changed emp_1 raise amount
#just below but in raise_amt we have self.pay=int(self.pay*Employee.raise_amount)
emp_1.raise_amount=2
emp_1.raise_amt()
print(emp_1.pay)
print(Employee.email(emp_1))

#now changes becouse of self.pay=int(self.pay*self.raise_amount)
class Employee:
	raise_amount=1.04
	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
	def email(self):
		return "{}.{}'@gmail.com'".format(self.first,self.last)
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
	def raise_amt(self):
		self.pay=int(self.pay*self.raise_amount)
emp_1=Employee('routh','krian',190000)
print(emp_1.fullname())
print(emp_1.email())
print(emp_1.pay)
emp_1.raise_amount=2
emp_1.raise_amt()
print(emp_1.pay)
print(Employee.email(emp_1))