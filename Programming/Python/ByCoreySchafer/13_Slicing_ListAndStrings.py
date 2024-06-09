my_List=[0,1,2,3,4,5,6,7,8,9]
#       (0,1,2,3,4,5,6,7,8,9)
#     -(10,9,8,7,6,5,4,3,2,1)

#Print element by its index
print(my_List[0],my_List[-10])
#Output
#0 0

#Printing range having default step=1
#Printing element from index zero to 4 terminating point is not inclusive
print(my_List[0:5],my_List[-10:-5])
#Output
#[0, 1, 2, 3, 4] [0, 1, 2, 3, 4]

#Printing element from positive 0 index to positive 9 index or -1 index
print(my_List[:-1])
#Output
#[0, 1, 2, 3, 4, 5, 6, 7, 8]

#Printing through step
print(my_List[0:10:2])
#Output
#[0, 2, 4, 6, 8]

#Negitive step
print(my_List[-1:0:-2])
#Output
#[9, 7, 5, 3, 1]

#Reversing the list
print(my_List[::-1])
#Output
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#For reversing the string
String="My name is kiran"
print(String[::-1])
#Output
#narik si eman yM
