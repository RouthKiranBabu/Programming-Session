import random

#Value of float between 0 and 1 of seventeen decimal places
val=random.random()
print(val)

#Value of float between 0 and 10 of seventeen decimal places
val=random.uniform(1,10)
print(val)

#To get random integer
val=random.randint(1,10)
print(val)

#Selecting random elements from greetings
greetings=['Hi, ','Hey, ','Hura, ','Hello, ']
rand=random.choice(greetings)
print(rand+'Kiran.')

#Selecting from colors and shows 10 experiments result at a time
colors=['red','green','blue']
result=random.choices(colors,k=10)
print(result)

#Probability control by weights the more the value the more the choice comes
colors=['red','green','blue']
result=random.choices(colors,weights=[18,15,1],k=10)
print(result)

#Making the list where 53 is non inclusive means range from 0 to 52
deck=list(range(1,53))
print(deck)

#Suffel the dect means arrange unordered sequence
deck=list(range(1,53))
random.shuffle(deck)
print(deck)

#Select random sample from deck which is unique
deck=list(range(1,53))
Sample=random.sample(deck,k=5)
print(Sample)

#Choice of probability
List=['1','2','3']
rand=random.choices(List,k=10,weights=[0.5,0.3,0.2])
print(rand)