#When the current file is imported in other python file it displays
print("Imported Mymodule file...")

#String formation
Test="This is string"

#Function that takes the list and the element inside the list
def Find_Index(To_Search,Target):

	#Doc string: This function is to make more useful when knowking about self module
	"""This function returns index if element is present inside the list otherwise returns -1
	to the file which imports this file"""

	for i, value in enumerate(To_Search):
		if value==Target:
			return i
	return -1