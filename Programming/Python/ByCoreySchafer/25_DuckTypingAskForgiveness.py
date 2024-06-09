class Duck:
	def quack(self):
		print('Quack, quack')
	def fly(self):
		print('Flap, flap!')
class Person:
	def quack(self):
		print("I'm quacking like a Duck!")
	def fly(self):
		print("I'm flapping my arms!")

#Is instance is used to check the thing is of function Duck()
def quack_and_fly(thing):
	if isinstance(thing,Duck):
		thing.quack()
		thing.fly()
	else:
		print('This has to be duck!')

d=Duck()
quack_and_fly(d)
p=Person()
quack_and_fly(p)

#2nd program non-pythonic LBYL
class Duck:
	def quack(self):
		print('Quack, quack')
	def fly(self):
		print('Flap, flap!')
class Person:
	def quack(self):
		print("I'm quacking like a Duck!")
	def fly(self):
		print("I'm flapping my arms!")
print()
def quack_and_fly(thing):

	#If function thing has attribute quack
	if hasattr(thing,'quack'):

		#If the thing is callable like thing.quack
		if callable(thing.quack):
			thing.quack()
	if hasattr(thing,'fly'):
		if callable(thing.fly):
			thing.fly()
d=Duck()
quack_and_fly(d)
p=Person()
quack_and_fly(p)
print()

#3rd program
class Duck:
	def quack(self):
		print('Quack, quack')
	def fly(self):
		print('Flap, flap!')
class Person:
	def quack(self):
		print("I'm quacking like a Duck!")
	def fly(self):
		print("I'm flapping my arms!")

#EAFP pythonic
def quack_and_fly(thing):
	try:
		thing.quack()
		thing.fly()
		#I know this is an error
		thing.bark()
	except AttributeError as e:
		print(e)

d=Duck()
quack_and_fly(d)
p=Person()
quack_and_fly(p)
print()

person={'name':'Routh','age':14,'job':'programmer'}
if 'name' in person and 'age' in person and 'job' in person:
	print("I'm {name}, I'm {age} years old and I am a {job}".format(**person))
else:
	print('Missing some key!')

person={'name':'Routh','age':14}
if 'name' in person and 'age' in person and 'job' in person:
	print("I'm {name}, I'm {age} years old and I am a {job}".format(**person))
else:
	print('Missing some key!')

person={'name':'Routh','age':14}
try:
	print("I'm {name}, I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
	print('Missed key: {}'.format(e))
print()

List=[0,1,2,3,4,5,6]
if len(List)>=6:
	print(List[6])
else:
	print("The index does not exist!")
List=[0,1,2,3,4,5]
try:
	print(List[6])
except IndexError:
	print("The index does not exist!")

#This program is used to access the file from certain location and read it
#Race condition
import os
my_file = "C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode31/Reading.txt"
if os.access(my_file,os.R_OK):
	with open(my_file) as f:
		print(f.read())
else:
	print("File cannot be accessed!")
#No race condition
try:
	f=open(my_file)
except IOError as e:
	print("File cannot be accessed")
else:
	with f:
		print(f.read())

