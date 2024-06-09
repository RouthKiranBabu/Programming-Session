my_list=[1,2,3,4,5]

#true when item in list
for i in my_list:
	print(i)
#true where there is no item in list
else:
	print('after for loop')

for i in my_list:
	print(i)
	if i==3:
		#breaks the loop and else
		break
else:
	print('after for loop')

i=1
while i<=5:
	print(i)
	i+=1
else:
	print('after while loop')


i=1
while i<=5:
	print(i)
	i+=1
	if i==3:
		break
else:
	print('after while loop')

def find_index(to_search,target):
	for i,value in enumerate(to_search):
		if value==target:
			break

	else:
		return -1
	return i

my_list=['kiran','routh','r.kiran']
index_location=find_index(my_list,'routh')
print("the index_location is ",index_location)

def search(List,item):
	for i,x in enumerate(List):
		if item==x:
			return f"found at index {i}."
	else:
		return None
List=[1,2,3,4,5]
print(search(List,6))
