s1=set([1,2,3,4,5])
s1.add(6)
s2={10,11,12,21}
s1.update([7,8,9,4,3,2,5,7,8,5,3],s2)
s1.remove(9)
s1.discard(10)
print("list to set:"+str(s1))#set cannot have same element twice or more

s1={1,2,3}
s2={2,3,4}
s3={3,4,5}

s4=s1.intersection(s2)
print(f"{s1}.intesection({s2}): {s4}")

s4=s1.difference(s2)
print(f"{s1}.difference({s2}): {s4}")

s4=s1.difference(s2,s3)
print(f"{s1}.difference({s2},{s3}): {s4}")

s4=s1.symmetric_difference(s2)
print(f"{s1}.symmetric_difference({s2}): {s4}")

employees = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
gym_members = ['April', 'John', 'Corey']
developers = ['Judy', 'Corey', 'Steven', 'Jane', 'April']
result=set(gym_members).intersection(gym_members,developers)
print(result)
result=set(gym_members).intersection(developers)
print(result)

if 'Corey' in developers:
	print('found')