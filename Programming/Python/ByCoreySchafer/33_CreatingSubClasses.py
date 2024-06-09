class Employee:
	raise_amt=1.04

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'

	def full_name(self):
		return (f"{self.first}{self.last}")

	def apply_raise(self):
		self.pay=int(self.pay*self.raise_amt)

#Makes a doc(below) string where in resolution order it checks first the developer and 
#then checks the employee and lastly builtin we get a method which is inherited from 
#the employee class

#hi there
#Inheritance from employee class
class Developer(Employee):
	#Changing the parent raise_amt
	raise_amt=1.10

	def __init__(self,first,last,pay,prog_lang):
		#This makes let init be take care of employee class making this class to be
		#less comples
		super().__init__(first,last,pay)
		self.prog_lang=prog_lang

class Manager(Employee):
	def __init__(self,first,last,pay,employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emp(self,emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self,emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->',emp.full_name())

dev_1=Employee('kiran','babu',50000)
dev_2=Employee('kira','ba',40000)
print("from employee class")
print(dev_1.email)
print(dev_2.email+'\n')

dev_1=Developer('kiran','babu',50000,'Python')
dev_2=Developer('kira','ba',60000,'Java')
print("from developer class")
print(dev_1.email)
print(dev_1.prog_lang)
print(dev_2.email+'\n')

print(help(Developer))

#but doest have effect in parent class named Employee
print('the pay in developer')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay,'\n')

mgr_1=Manager('kiran','routh',90000,[dev_1])
print('manager 1:')
print(mgr_1.email,'\n')

mgr_1.print_emps()

#adds employee 
print('adding a employee')
mgr_1.add_emp(dev_2)

#print no of employees manager1 supervises
mgr_1.print_emps()

#removes employee 
print('removing the employee')
mgr_1.remove_emp(dev_1)

#print no of employees manager1 supervises
mgr_1.print_emps()

#To check instance of class
print('To check instance of class:')
print(isinstance(mgr_1,Manager))
print('To check instance of class:')
print(isinstance(mgr_1,Employee))
print('To check instance of class:')
print(isinstance(mgr_1,Developer))

print('To check is subclass of class:')
print(issubclass(Employee,Developer))
print(issubclass(Developer,Employee))
print(issubclass(Developer,Manager))
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))

#See the project 17:54 if needed for http