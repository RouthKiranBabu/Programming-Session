def decorator_function(original_function):
	def wrapper_function(*args,**kwargs):
		print("Executed before",original_function.__name__)
		result=original_function(*args,**kwargs)
		print("Executed after",original_function.__name__,'\n')
		return result
	return wrapper_function

@decorator_function
def display_info(name,age):
	print('display_info ran with arguments ({},{}).'.format(name,age))
print()
display_info('Routh',11)
display_info('Kira',9)

def prefix_decorator(prefix):
	def decorator_function(original_function):
		def wrapper_function(*args,**kwargs):
			print(prefix,"Executed before",original_function.__name__)
			result=original_function(*args,**kwargs)
			print(prefix,"Executed after",original_function.__name__,'\n')
			return result
		return wrapper_function
	return decorator_function

@prefix_decorator('Testing: ')
def display_info(name,age):
	print('display_info ran with arguments ({},{}).'.format(name,age))

display_info('Routh',14)
display_info('Kira',5)

