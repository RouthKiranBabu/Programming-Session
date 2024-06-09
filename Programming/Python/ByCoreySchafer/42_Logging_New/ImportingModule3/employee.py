import logging

logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(levelname)s:%(name)s:%(message)s')

class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last
		#if you write info in place of debug the the output will have employee
		#result and then the arithematic result where arithematic file imported this file
		logging.info('Created Employee: {}-{}'.format(self.fullname,self.email))#makes root to __main__

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first,self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
emp_1=Employee('routh','kiran')
emp_2=Employee('james','bond')
emp_3=Employee('james1','bond1')
#Creates employee.log when we run here