import logging
#logger has more advantages than basicconfig logging
#logging.basicConfig(filename='employee.log',level=logging.INFO,format='%(levelname)s:%(name)s:%(message)s')
logger=logging.getLogger(__name__)#name is __main__ when we run here employee when run at other file 
#to set employee loger
logger.setLevel(logging.INFO)
#we can also do formating for more attractive look which is done in filehandler not logger
formatter=logging.Formatter('%(levelname)s:%(name)s:%(message)s')

#still it is a root for configuring a file now we need to configure logger variable
#and leave root logger
#to specify or handling employee log that we want to log to we need to add file handler
file_handler=logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
#to make logger attached to file handler variable
logger.addHandler(file_handler)

class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last
		logger.info('Created Employee: {}-{}'.format(self.fullname,self.email))

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first,self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
emp_1=Employee('routh','kiran')
emp_2=Employee('james','bond')
emp_3=Employee('james1','bond1')