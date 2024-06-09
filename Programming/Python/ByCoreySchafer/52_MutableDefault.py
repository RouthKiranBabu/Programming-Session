def add_emp1(emp,List=[]):
	List.append(emp)
	print(List)
NList=[1,2,3,4]
add_emp1(5,NList)
add_emp1(1)
add_emp1(2)
add_emp1(3)
add_emp1(4)
print()
def add_emp2(emp,List=None):
	if List==None:
		List=[]
	List.append(emp)
	print(List)
NList=[1,2,3,4]
add_emp2(5,NList)
add_emp2(1)
add_emp2(2)
add_emp2(3)
add_emp2(4)

def add_emp3(emp,List=[]):
	List.append(emp)
	print(List)
print("the defaults: ",add_emp3.__defaults__)
add_emp3('kiran')
print("the defaults: ",add_emp3.__defaults__)

def add_emp4(emp,List=None):
	if List==None:
		List=[]
	List.append(emp)
	print(List)
print("the defaults of fixed: ",add_emp4.__defaults__)
add_emp4('kiran')
print("the defaults of fixed: ",add_emp4.__defaults__)
add_emp4('Routh')
print("the defaults of fixed: ",add_emp4.__defaults__)

import time
from datetime import datetime

def display_time(time_to_print=None):
	if time_to_print==None:
		time_to_print=datetime.now()
	print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

print(display_time.__defaults__)
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()

