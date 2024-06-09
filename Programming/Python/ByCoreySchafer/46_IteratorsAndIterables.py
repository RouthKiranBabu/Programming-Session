nums=[1,2,3]
for num in nums:
	print(num)

#it is said to be iterator or dunder iterator when it has __iter__
#during iteration it know the location and what to do next and knows the next location
#by dunder next method but not available so it is iterator but not really an iterator
print(dir(nums))

#print(next(nums)) TypeError: 'list' object is not an iterator becouse dunder next is not available

nums=[1,2,3]
i_num=iter(nums)
print("the value of i_num: ",i_num)
print(dir(i_num))#now it contains next 
print("the value in i_num: ",next(i_num))
print("the value in i_num: ",next(i_num))
print("the value in i_num: ",next(i_num))

nums=[1,2,3]
i_num=nums.__iter__()
print(dir(i_num))#now it contains next 
print("the value in i_num: ",next(i_num))
print("the value in i_num: ",next(i_num))
print("the value in i_num: ",next(i_num))
#print("the value in i_num: ",next(i_num)) Error: StopIteration

nums=[1,2,3]
i_num=iter(nums)
while True:
	try:
		item=next(i_num)
		print(item)
	except StopIteration:
		break

class MyRange:
	def __init__(self,start,end):
		self.value=start
		self.end=end

	def __iter__(self):
		return self

	def __next__(self):
		if self.value>=self.end:
			raise StopIteration
		current=self.value
		self.value+=1
		return current

num=MyRange(1,10)
for item in num:
	print("class item: ",item)

num=MyRange(1,10)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))

#generators are like iterator the keep on incremeting until it stop and generate itself again
#dunder iterator and next is created automatically in generator

def my_range(start,end):
	current=start
	while current<end:
		yield current
		current+=1

num=my_range(1,10)
print("inside generator: ",next(num))
print("inside generator: ",next(num))
print("inside generator: ",next(num))
print("inside generator: ",next(num))
print("inside generator: ",next(num))
print("inside generator: ",next(num))
print("inside generator: ",next(num))
print("inside generator: ",next(num))
print("inside generator: ",next(num))
#print("inside generator: ",next(num)) Error: StopIteration

num=my_range(1,10)
for n in num:
	print("inside for loop: ",n)

#to get odd words in sentence
def generator(sentence):
	words=sentence.split()
	for i in range(0,len(words),2):
		yield words[i]
my=generator("this is my sentence")
for item in my:
	print(item)