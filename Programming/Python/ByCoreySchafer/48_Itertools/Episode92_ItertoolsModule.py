import itertools

#counts infinetly adding one by one integer start from zero
#counter=itertools.count()
#for num in counter:
	#print(num)

counter=itertools.count()
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

counter=itertools.count()
List=[100,200,300,400]

count=itertools.count(start=1)
for x in count:
    print(x)
    if x==5:
        break

#zip basically combines two intervals and pair the values together  means it joins 
#the first element of counter and pair up with first element of List
val=zip(counter,List)
print(val)

counter=itertools.count()
List=[100,200,300,400]
val=list(zip(counter,List))
print(val)

#to start from certain number
counter=itertools.count(start=5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

#step making
counter=itertools.count(start=5,step=5)
print("step making: ",next(counter))
print("step making: ",next(counter))
print("step making: ",next(counter))
print("step making: ",next(counter))
counter=itertools.count(start=5,step=-2)
print("step making -2: ",next(counter))
print("step making -2: ",next(counter))
print("step making -2: ",next(counter))
print("step making -2: ",next(counter))

#use of zip function
List=[100,200,300,400]
val=list(zip(range(10),List))
print("use of zip function:" ,val)

List=[100,200,300,400]
val=list(itertools.zip_longest(range(10),List))
print("use of zip longest function:" ,val)

counter=itertools.cycle([1,2,3])
print("use of cycle: ",next(counter))
print("use of cycle: ",next(counter))
print("use of cycle: ",next(counter))
print("use of cycle: ",next(counter))
print("use of cycle: ",next(counter))
print("use of cycle: ",next(counter))

cycle=[x for x in range(1,5)]
val=itertools.cycle(cycle)
for x,y in itertools.zip_longest(cycle,val):
    print(x,y)
    cycle.pop()
    if len(cycle)<=0:
        break

counter=itertools.repeat(2)
print("repeat tool in itertools: ",next(counter))
print("repeat tool in itertools: ",next(counter))
print("repeat tool in itertools: ",next(counter))

#times is used for repeating times if more it prints stopiteration
counter=itertools.repeat(2,times=3)
print("repeat with times tool in itertools: ",next(counter))
print("repeat with times tool in itertools: ",next(counter))
print("repeat with times tool in itertools: ",next(counter))

import math
print(math.sqrt(2))
c=map(math.sqrt,range(10))
print(list(c))

counter=itertools.repeat(2,times=3)
#map does is it takes a function and takes iterables and uses the 
#values from those to pass as arguments to that function and it 
#will loop through and pass values from those intervals into a 
#function until the shortest list of arguments has run through
#all of its values so this will start off by passing in the next
#value from the range and that would start at zero and also pass in
#the iterable which is always going to be two 
squres=map(pow,range(10),itertools.repeat(2))
print("the square of range to the power 2 by map: ",list(squres))

val1=[x for x in range(1,6)]
val2=[x for x in range(1,11)]
vale=list(zip(val1,val2))
val=itertools.repeat(2,times=2)
mapval=itertools.starmap(pow,vale)
print(list(mapval))

squres=itertools.starmap(pow,[(1,2),(2,2),(3,2)])
print("the square of range to the power 2 by starmap: ",list(squres))

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['kiran','babu']
#total number of combinations here ('a','b') is same as ('b','a') not
#required
result=itertools.combinations(letters,2)
for item in result:
	print("the combination: ",item)

#total number of permutations ('a','b'), ('b','a') must be included
result=itertools.permutations(letters,2)
for item in result:
	print("the permutations: ",item)

#For repeating the numbers in combination and permuntation
#result=itertools.product(numbers,repeat=4)
#for item in result:
	#print("the repeat: ",item)

numbers=[0,1]
result=itertools.product(numbers,repeat=3)
for item in result:
	print("the repeat: ",item)

numbers=[0,1,2,3]
#to get combinations of those 3 digit numbers but it allows repeated 
#values as well 
result=itertools.combinations_with_replacement(numbers,4)
for item in result:
	print("the combinations_with_replacement: ",item)

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['kiran','babu']
#for larger number of lists and other thing chain makes easier to combine
#like combined=letters+numbers+names
combined=itertools.chain(letters,numbers,names)
for item in combined:
	print("the chain tool: ",item)

#slicing the range of 0 to 10 and stop at 6
combined=itertools.islice(range(10),6)
for item in combined:
	print("the slicing: ",item)

#assumes 1 as starting and 6 as stoping
combined=itertools.islice(range(10),1,6)
for item in combined:
	print("the slicing has starting: ",item)

#assumes 2 as step
combined=itertools.islice(range(10),1,6,2)
for item in combined:
	print("the slicing has step: ",item)

with open('sample.log','r') as f:
	#grabing first three lines
	header=itertools.islice(f,3)
	for line in header:
		print("the line in sample.log: ",line,end="")

letters=['a','b','c','d']
numbers=[0,1,2,3]
names=['kiran','babu']
selectors=[True,True,False,True]
#only selects the true values just same as filter 
result=itertools.compress(letters,selectors)
for item in result:
	print("item that are true: ",item)

def lt_2(n):
	if n<2:
		return True
	return False
numbers=[0,1,2,3]
result=filter(lt_2,numbers)
#but does not show only true values
for item in result:
	print("filtering things: ",item)

def lt_2(n):
	if n<2:
		return True
	return False
numbers=[0,1,2,3]
#True for greater than 2
result=itertools.filterfalse(lt_2,numbers)
for item in result:
	print("filtering false things: ",item)

numbers=[0,1,2,3,3,2,1,0]
result=itertools.filterfalse(lt_2,numbers)
for item in result:
	print("filtering false things1: ",item)

numbers=[0,1,2,3,3,2,1,0]
#first cuple of values were less than 2 so it drop those but once it 
#hit a value that are greater or equal to 2 then it stopped appling 
#the filter and just returned the rest of the iterable os it does not
#filter out all of the values just drops the first few lines once that
#met 
result=itertools.dropwhile(lt_2,numbers)
for item in result:
	print("dropwhiles: ",item)

result=itertools.takewhile(lt_2,numbers)
for item in result:
	print("takewhile: ",item)

letters=['a','b','c','d']
numbers=[0,1,2,3,2,1,1]
names=['kiran','babu']
#just add up by default
result=itertools.accumulate(numbers)
#0 plus 1 is 1, 1 plus 2 is 3,3 plus 3 is 6,so on
for item in result:
	print("accumulate: ",item)

import operator
letters=['a','b','c','d']
numbers=[0,1,2,3,2,1,1]
names=['kiran','babu']
#just add up by default
result=itertools.accumulate(numbers,operator.mul)
for item in result:
	print("accumulate: ",item)

numbers=[1,2,3,2,1,0]
result=itertools.accumulate(numbers,operator.mul)
#1 times 2 is 2,2 times 3 is 6,6 times 2 is 12
for item in result:
	print("accumulate1: ",item)

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]
def get_state(person):
	#group by state
	return person['state']
person_group=itertools.groupby(people,get_state)
for key,group in person_group:
	print("the key and group: ",list(key),list(group))

person_group=itertools.groupby(people,get_state)
for key,group in person_group:
	print("the key: ",key)
	for person in group:
		print("the group: ",person)
	print()

person_group=itertools.groupby(people,get_state)
for key,group in person_group:
	print("the key and len of group: ",key,len(list(group)))


a={'name':'kiran','age':'22'}
b={'name':'kira','age':'21'}

def Name(data):
    return data['name']

val=itertools.groupby([b,a],Name)

for al,j in val:
    print(al)
    for val in j:
        print(val)