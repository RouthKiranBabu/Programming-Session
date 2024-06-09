def squareon(List):
	result=[]
	for i in List:
		result.append(i**2)
	return result

List=squareon([1,2,3,4,5])
print(f"The square of elements in the list {List}.")

def square_numbers(nums):
	for i in nums:
		yield (i*i)
my_nums=square_numbers([1,2,3,4,5])
#If more than index error occurance name is StopIteration
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))

#With out use of next iteration
def square_numbers1(nums):
	for i in nums:
		yield (i*i)
my_nums=square_numbers1([1,2,3,4,5])
for i in my_nums:
	print(i)
print()

#List comprehension
my_list=[x*x for x in [1,2,3,4,5]]
print(my_list)

my_list=(x*x for x in [1,2,3,4,5])
print(list(my_list))
print()

#import mem_profile
import random
import time
names=['john','Corey','Adam','Steve','Rick','Thomas']
majors=['Math','Engineering','CompSci','Arts','Business']

#print('Memory (before): {}Mb'.format(mem_profile.memory_usage_resource()))
def people_list(num_people):
	result=[]
	for i in range(num_people):#See tutorials for x range
		person={
		"id":i,
		"name":random.choice(names),
		"major":random.choice(majors)
		}
		result.append(person)
	return result

def people_generator(num_people):
	for i in range(num_people):
		people={
		"id":i,
		"name":random.choice(names),
		"major":random.choice(majors)
		}
	yield people
t1=time.clock()
people=people_list(1000000)
t2=time.clock()
#print("Memory (after): {}Mb.".format(mem_profile.memory_usage_resource()))
print("Took {} Seconds".format(t2-t1))

t3=time.clock()
people=people_generator(1000000)
t4=time.clock()
#generator uses less time than the normal list and memory size is less becouse it is 
#waiting for next respond stores only one values
print("Took {} Seconds".format(t4-t3))

t5=time.clock()
people=list(people_generator(1000000))
t6=time.clock()
#Makes more time and memory space
print("Took {} Seconds".format(t6-t5))

#There is no x range in python3 in exchange range itself