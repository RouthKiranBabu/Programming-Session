#getter
'''
class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last
		self.email=first+last+'@gmail.com'

	def fullname(self):
		return ('{} {}'.format(self.first,self.last))

emp_1=Employee('Routh','kiran')

#updating the first name but the email is still as older so this makes a problem on
#making change on email every time
emp_1.first='R'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname())
'''
'''
class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last

	def fullname(self):
		return ('{} {}'.format(self.first,self.last))

	def email(self):
		return f'{self.first}{self.last}@gmail.com'

emp_1=Employee('Routh','kiran')

#But here it act like a function eg email and full name 
emp_1.first='R'

print(emp_1.first)
print(emp_1.email())
print(emp_1.fullname())
'''
'''
class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last

	@property
	def fullname(self):
		return ('{} {}'.format(self.first,self.last))

	@property
	def email(self):
		return f'{self.first}{self.last}@gmail.com'

emp_1=Employee('Routh','kiran')

#But here it act like a function eg email and full name 
emp_1.first='R'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
'''
#setter
class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last

	#property is must for setter and deleter
	@property
	def fullname(self):
		return ('{} {}'.format(self.first,self.last))

	@property
	def email(self):
		return f'{self.first}{self.last}@gmail.com'

	@fullname.setter
	def fullname(self,name):
		first,last=name.split(' ')
		self.first=first
		self.last=last

	@fullname.deleter
	def fullname(self):
		print('Delete name!')
		self.first=None
		self.last=None

emp_1=Employee('R','kiran')

#We cant directly make a full name so we need a setter
#emp_1.fullname='Routh kiran'
emp_1.fullname='Routh kiran'
print(emp_1.email)
print(emp_1.first)

#To delete a name
del emp_1.fullname
print(emp_1.email)
print(emp_1.first)

