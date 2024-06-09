class Employee():
	pass

#Unique instances for a class named Employee
emp_1=Employee()
emp_2=Employee()

print(emp_1,'\n',emp_2)
emp_1.firstname="Routh"
emp_1.lastname="Kiran"
emp_1.email="routhkiran456@gmail.com"
emp_1.pay=50000

emp_2.firstname="firstname"
emp_2.lastname="lastname"
emp_2.email="name@gmail.com"
emp_2.pay=50000

print(emp_1.email)
print(emp_2.email)
print()

class employee():
	def __init__(self,firstname,lastname,pay):
		self.firstname=firstname
		self.lastname=lastname
		self.email=firstname+'.'+lastname+"@gmail.com"
		self.pay=pay
e1=employee("Routh","kiran",5000)
print(e1.email)
print("Full name is {} {}.".format(e1.firstname,e1.lastname))
print()

class employee():
	def __init__(self,firstname,lastname,pay):
		self.firstname=firstname
		self.lastname=lastname
		self.email=firstname+'.'+lastname+"@gmail.com"
		self.pay=pay
	def full_name(self):
		return ("Full name is {} {}.".format(self.firstname,self.lastname))
e1=employee("Routh","kiran",5000)

#Ready to execute
print(e1.full_name)

#full_name is a method not an attribute so brackets are placed
print(e1.full_name())

print(employee.full_name(e1))

