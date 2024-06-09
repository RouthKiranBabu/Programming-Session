class Employee:
	num_of_emps=0
	raise_amt=1.04

	def __init__(self,first,last,pay):
		self.first=first
		self.last=last
		self.pay=pay
		self.email=first+'.'+last+'@gmail.com'

		Employee.num_of_emps+=1

	def full_name(self):
		return (f"{self.first}{self.last}")

	def apply_raise(self):
		self.pay=int(self.pay+self.raise_amt)

	@classmethod
	def set_raise_amt(cls,amount):#cls is for class named Employee
		cls.raise_amt=amount

	@classmethod
	def from_string(cls,emp_str):
		first,last,pay=emp_str.split('-')

		#runs the class name Employee
		return cls(first,last,pay)

	#Staticmethods have connection with class but not change any other things in class
	#it doesnt take class or instance as arguments
	@staticmethod
	def is_workday(day):
		if day.weekday()==5 or day.weekday()==6:#saturday or sunday
			return False
		return True

emp_1=Employee('kiran','babu',50000)
emp_2=Employee('kira','ba',40000)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#Advantage of classmethods is that to change a variable permanently this methods is used
Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#Still changes a class variable 
emp_1.set_raise_amt(1.04)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

#Simple problem case
#To write every time better to make constructor in class name from_string
emp_str_1='Routh-kiran-80000'
first,last,pay=emp_str_1.split('-')
new_emp_1=Employee(first,last,pay)
print(new_emp_1.email)
print(new_emp_1.pay)

emp_str_2='Routh-kira-50000'
new_emp_2=Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)

import datetime
my_date=datetime.date(2019,5,31)
print('is to day is working day: ',end='')
print(Employee.is_workday(my_date))