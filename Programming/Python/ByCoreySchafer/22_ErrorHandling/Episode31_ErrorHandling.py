#For every error it prints error occured
try:
	f=open('Reading1.txt')
except Exception:
	print("Error occured")

#Except works for filenotfounderror
try:
	f=open('Reading1.txt')
except FileNotFoundError:
	print("File not exists!")

#Exception is kept bottom becouse this is the general thing alway given more 
#prirority 
try:
	f=open('Reading1.txt')
	var=f
except NameError:
	print("name {} is not found".format('var'))
except Exception:
	print("Somethings went wrong!")
	
#For more specific in error handling
try:
	f=open('Reading1.txt')
	var=f
except NameError as e:
	print(e)
except Exception as e:
	print(e)

#Else is use just like next line of try condition else does when exception not occured
#Finally always does that even or not the exception occurs
try:
	f=open('Reading.txt')
except NameError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
finally:
	print("Executed finally!")

#Raising exception
try:
	f=open('Reading.txt')
	if f.name=='Reading.txt':
		raise Exception
except NameError as e:
	print(e)
except Exception as e:
	print(e)
	print("Error occured")
else:
	print(f.read())
	f.close()
finally:
	print("Executed finally!")

#To see what is the name of the error
try:
	with open('file.txt','r') as rf:
		result=f.read()
		print(result)
except Exception as e:
	print(dir(e))
	print(e.with_traceback)
else:
	print("Hi done sucessfully!")
finally:
	print("Executed as normally")