import os

#Changing the name of vedio files
os.chdir('E:/abhishek')

#Shows the location you are in
print(os.getcwd())

#To print all the listed vedio available
for f in os.listdir():
	print(f,end='\n')

#To split extension and name of file
for f in os.listdir():
	print(os.path.splitext(f))

#To seperate files and extensions
for df in os.listdir():
	file, extensions=os.path.splitext(df)
	title, text, number=file.split('-')
	print(title)
	print('{}-{}-{}-{}{}'.format(number,title,text,file,extensions))

	#For sorting
	title=title.strip()
	text=text.strip()
	number=number.strip()
	print('{}-{}-{}-{}{}'.format(number,title,text,file,extensions))

	title=title.strip()
	text=text.strip()

	#Unnessary requirement delection
	number=number.strip()[1:]
	print('{}-{}-{}-{}{}'.format(number,title,text,file,extensions))

	title=title.strip()
	text=text.strip()

	#Making two digits so that can be in increasing order
	number=number.strip()[0:].zfill(2)
	print('{}-{}-{}-{}{}'.format(number,title,text,file,extensions))

	new_name='{}-{}{}'.format(number,title,text,extensions,file)
	os.rename(df,new_name)