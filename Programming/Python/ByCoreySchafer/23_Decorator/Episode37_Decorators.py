def outer_function():
	message='hi'
	def inner_function():
		print(message)
	return inner_function()
outer_function()
print()

def outer_function():
	message='hi'
	def inner_function():
		print(message)
	return inner_function#Note that it doesnt have brackets which is stored in my_fun
	#variable just below

#Ready to be executed
my_fun=outer_function()
my_fun()
print()

def outer_function(msg):
	message=msg
	def inner_function():
		print(message)
	return inner_function

hi_fun=outer_function('Hi!')
bye_fun=outer_function('Bye!')
hi_fun()
bye_fun()
print()

def decorator_function(original_function):
	def wrapper_function():
		print("wrapper executes this before {}.".format(original_function.__name__))
		return original_function()#Note given a bracket to execute
	return wrapper_function
def display_function():
	print('display function ran')
my_fun=decorator_function(display_function)#Note doesnt given a bracket
my_fun()
print()

def decorator_function(original_function):
	def wrapper_function():
		print("wrapper executes this before {}.".format(original_function.__name__))
		return original_function()
	return wrapper_function

#Same as asking display=decorator_function(display_function())
@decorator_function
def display_function():
	print('display function ran!')
display_function()
print()


def decorator(original):
	def wrapper(k,a,b):
		print(f'inside wrapper and then goes to {original.__name__}')
		print(k,a,b)
		return original(k,a,b)
	return wrapper
@decorator
def display(sino,name,age):
	print(f"the syntax of sino:name:age is {sino}:{name}:{age}.")
display('1','kiran','12')


def decorator_function(original_function):
	#stops TypeError: wrapper_function() takes 0 positional arguments but 2 were given
	def wrapper_function(*args,**kwargs):
		print("wrapper executes this before {}.".format(original_function.__name__))
		return original_function(*args,**kwargs)
	return wrapper_function
@decorator_function
def display_function():
	print('display function ran')
@decorator_function
def display_info(name,age):
	print('display info ran with argument ({},{}).'.format(name,age))
display_info('Kiran',20)
display_function()
print()

#Class decorator
class decorator_class(object):
	def __init__(self,original_function):
		self.original_function=original_function
	def __call__(self,*args,**kwargs):
		print("call method executes this before {}.".format(self.original_function.__name__))
		return self.original_function(*args,**kwargs)
@decorator_class
def display_function():
	print('display function ran')
@decorator_class
def display_info(name,age):
	print('display info ran with argument ({},{}).'.format(name,age))

display_info('Kiran',20)
display_function()	
print()


def dup_func(orig):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig.__name__),level=logging.INFO)
	def wrapper(*args,**kwargs):
		logging.info(f'your name is {args[0][0]} and your age is {args[0][1]} and dictionary in it {kwargs}.')
		return orig(*args,**kwargs)
	return wrapper
@dup_func
def display(name,age):
	print(f'your name and age is {name} and {age}.')
display(('kiran','19'),{'name':'age'})


def my_logger(orig_fucn):
	import logging
	logging.basicConfig(filename="{}.log".format(orig_fucn.__name__),level=logging.INFO)

	def wrapper(*args,**kwargs):
		logging.info("Ran with args: {}, and kwargs: {}".format(args,kwargs))
		return orig_fucn(*args,**kwargs)	

	return wrapper

def my_timer(orig_fucn):
	import time

	def wrapper(*args,**kwargs):
		t1=time.clock()
		result=orig_fucn(*args,**kwargs)
		t2=time.clock()-t1
		print("{} ran in: {}sec.".format(orig_fucn.__name__,t2))
		return result
	return wrapper

@my_logger
def display_info(name,age):
	print('display info ran with argument ({},{}).'.format(name,age))
display_info('Routh.kiran1',20)

import time
@my_timer
def display_info(name,age):
	time.sleep(1)
	print('display info ran with argument ({},{}).'.format(name,age))
display_info('Routh.kiran1',20)

#Same as display_info=my_logger(my_timer(display_info))
@my_timer
@my_logger
def display_info(name,age):
	time.sleep(1)
	print('display info ran with argument ({},{}).'.format(name,age))
display_info('Routh.kiran2',20)
print()

@my_logger
@my_timer
def display_info(name,age):
	time.sleep(1)
	print('display info ran with argument ({},{}).'.format(name,age))
display_info('Routh.kiran2',20)
print()

def display_info(name,age):
	time.sleep(1)
	print('display info ran with argument ({},{}).'.format(name,age))
display_info=my_timer(display_info)
print(display_info.__name__)
print()

from functools import wraps
def my_logger(orig_fucn):
	import logging
	logging.basicConfig(filename="{}.log".format(orig_fucn.__name__),level=logging.INFO)

	@wraps(orig_fucn)
	def wrapper(*args,**kwargs):
		logging.info("Ran with args: {}, and kwargs: {}".format(args,kwargs))
		return orig_fucn(*args,**kwargs)	

	return wrapper

def my_timer(orig_fucn):
	import time

	@wraps(orig_fucn)
	def wrapper(*args,**kwargs):
		t1=time.clock()
		result=orig_fucn(*args,**kwargs)
		t2=time.clock()-t1
		print("{} ran in: {}sec.".format(orig_fucn.__name__,t2))
		return result
	return wrapper
def display_info(name,age):
	time.sleep(1)
	print('display info ran with argument ({},{}).'.format(name,age))
display_info=my_timer(display_info)
print(display_info.__name__)
display_info('Routh',20)
print()

@my_logger
@my_timer
def display_info(name,age):
	time.sleep(1)
	print('display info ran with argument ({},{}).'.format(name,age))

display_info('Routh',20)

from functools import wraps
import time 
def decorator(origfunc):
	import logging
	logging.basicConfig(filename='loggingfile.log',level=logging.DEBUG,format='%(asctime)s:%(levelname)s:%(message)s')
	@wraps(origfunc)
	def innerfunc(*args,**kwargs):
		t1=time.clock()
		logging.info(f"this executes first than {origfunc.__name__}.")
		print(origfunc.__name__==innerfunc.__name__)#true when line 220 @wraps(origfunc) exists
		origfunc(*args,*kwargs)
		t2=time.clock()
		print(f'and time took {t2-t1}.')
	return innerfunc

@decorator
def display(name,age):
	print(f"your name is {name} and age is {age}.")
display('kiran','13')

'''
import time
def cal_square(numbers):
	start_time=time.time()
	result=[]
	for number in numbers:
		result.append(number**2)
	stop_time=time.time()
	#1000 is multiplied to make into milisecond
	print(f"Total time took: {(stop_time-start_time)*1000} miliseconds.")
	return result

def cal_cube(numbers):
	start_time=time.time()
	result=[]
	for number in numbers:
		result.append(number**3)
	stop_time=time.time()
	#1000 is multiplied to make into milisecond
	print(f"Total time took: {(stop_time-start_time)*1000} miliseconds.")
	return result

array=range(1,10**4)
out_square=cal_square(array)
out_cube=cal_cube(array)
'''
#The above two function code has same thing for measuring the time but it
#makes more complexcity and this makes us to write it again and again in every
#function to calculate time took another problem is the main thing of the function
#is to measure square and cube but unnessarily we kept the timing things 

#Functions are first class objects in python. what it means is that they can be 
#created just like any other variable and you can pass them as argument to another
#function or even return them as a return value.

import time

def time_it(func):
	def wrapper(*args,**kwargs):
		start=time.time()
		result=func(*args,**kwargs)#Goes to function either cal_square or cal_cube
		end=time.time()
		print(func.__name__+" took "+str((end-start)*1000)+" Milliseconds.")
		return result
	return wrapper

@time_it
def cal_square(numbers):
	result=[]
	for number in numbers:
		result.append(number**2)
	return result

@time_it
def cal_cube(numbers):
	result=[]
	for number in numbers:
		result.append(number**3)
	return result

array=range(1,10**4)
out_square=cal_square(array)
out_cube=cal_cube(array)