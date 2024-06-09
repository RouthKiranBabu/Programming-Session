#to make sample log file must contain errors or warning so we need to set level for
#handlers eg., to set to debug 
import logging
import employee

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler=logging.FileHandler('sample.log')
#You will see empty becouse there is no error logs or level didnt match 
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def add(x,y):
	return x+y
def substract(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	try:
		result= x/y
	except ZeroDivisionError:
		#which shows error message in sample log
		logger.error('Tried to divide by zero')
	else:
		return result

num_1=10
num_2=0

add_result=add(num_1,num_2)
logger.debug("Add {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
logger.debug("Sub {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
logger.debug("Mul {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
logger.debug("Div {}/{}={}.".format(num_1,num_2,div_result))
