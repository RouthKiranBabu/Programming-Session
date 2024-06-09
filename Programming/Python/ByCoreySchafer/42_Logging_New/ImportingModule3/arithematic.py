import logging
#When importing a file module the file executes first and makes employees
import employee

#here it doesnt create sample log file and created employees log file becouse
#employee module has basicconfig and it is declared firstabove

#When you run this file you will not get the output for this file until the employee
#basicconfig level=logging.INFO but this file logging sample file is logging.DEBUG

#to hit that level make logging.debug at message line 26 to 33
logging.basicConfig(filename='sample.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')

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
logging.info("Add {}+{}={}.".format(num_1,num_2,add_result))
sub_result=substract(num_1,num_2)
logging.info("Sub {}-{}={}.".format(num_1,num_2,sub_result))
mul_result=multiply(num_1,num_2)
logging.info("Mul {}*{}={}.".format(num_1,num_2,mul_result))
div_result=divide(num_1,num_2)
logging.info("Div {}/{}={}.".format(num_1,num_2,div_result))

#creates sample.log when run this program
#root is present when no logger is declared