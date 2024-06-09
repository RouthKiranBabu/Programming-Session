import logging
#DEBUG:	detailed information, typically of interest only when diagnosing problems

#INFO:	confirmation that things are working as excepted

#Warning: an indication that something unexpected happened, or indicative of some 
#problem in the near future (e.g., 'disk space low'), The software is still working
#as expected

#ERROR: due to more serious problem, the software has not been able to perform some
#function

#CRITICAL: a serious error, indicating that the program itself may be unable to
#continue running 


def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y
num_1=10
num_2=5
add_result=add(num_1,num_2)
print("Add {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
print("Sub {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
print("Mul {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
print("Div {}/{}={}.".format(num_1,num_2,div_result))

add_result=add(num_1,num_2)
logging.debug("Add {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
logging.debug("Sub {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
logging.debug("Mul {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
logging.debug("Div {}/{}={}.".format(num_1,num_2,div_result))

add_result=add(num_1,num_2)
logging.warning("Addlogwar {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
logging.warning("Sublogwar {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
logging.warning("Mullogwar {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
logging.warning("Divlogwar {}/{}={}.".format(num_1,num_2,div_result))


logging.basicConfig(filename='test.log',level=logging.DEBUG)#DEBUG is a integer at background
#debug is 10,info is 20,warnings is 30,error is 40 and critical is 50

def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y

#Contains previous and present values
#num_1=10
#num_2=5
num_1=10
num_2=5
#test.log contains
#DEBUG:root:Add 10+5=15.
#where debug is log level root is logger 
add_result=add(num_1,num_2)
logging.debug("Add {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
logging.debug("Sub {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
logging.debug("Mul {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
logging.debug("Div {}/{}={}.".format(num_1,num_2,div_result))


#after comma and before dubug in test1 is milliseconds
logging.basicConfig(filename='test1.log',level=logging.INFO,
	format='%(asctime)s:%(levelname)s:%(message)s')

def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y

#Contains previous and present values
#num_1=10
#num_2=5
num_1=10
num_2=5
#test.log contains
#DEBUG:root:Add 10+5=15.
#where debug is log level root is logger 
add_result=add(num_1,num_2)
logging.debug("Add {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
logging.debug("Sub {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
logging.debug("Mul {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
logging.debug("Div {}/{}={}.".format(num_1,num_2,div_result))



logging.basicConfig(filename='employee.log',level=logging.INFO,
	format='%(levelname)s:%(message)s')
class Employee:
	def __init__(self,first,last):
		self.first=first
		self.last=last
		logging.info('Created Employee: {}-{}'.format(self.fullname,self.email))

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first,self.last)

	#@property
	def fullname(self):
		return '{} {}'.format(self.first,self.last)
emp_1=Employee('routh','kiran')
emp_2=Employee('james','bond')
emp_3=Employee('james1','bond1')
print(emp_1.fullname())