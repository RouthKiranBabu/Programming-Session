'''
#opening the file for reading('r'), for writing('w'), appending
#('a'), for read and write('r+')
f=open('TargetedFile.txt','r')

#To know file name
print(f.name)

#To know the mode which we opened
print(f.mode)

#Closing a file
f.close()
'''

#This helps when the loop is finished up the opened file 
#automatically closed when outside the with statement
with open('TargetedFile.txt','r') as f:
	pass

#To know wether the file is closed or not
print(f.closed)

#Reads every text in the file and shows exact
with open('TargetedFile.txt','r') as f:
	content=f.read()
	print(f"the content inside the TargetedFile is \n{content}.\n")

#Reads every text in the file and in a array
with open('TargetedFile.txt','r') as f:
	content=f.readlines()
	print(f"The readline command content\n{content}.\n")

#Reads first line and shows exact
with open('TargetedFile.txt','r') as f:
	content=f.readline()
	print(f"the single readline command \n{content}.\n")

#Reads line by line and shows exact. end='' removes spaces 
#between two lines
with open('TargetedFile.txt','r') as f:
	content=f.readline()
	print(content,end='')
	content=f.readline()
	print(content,end='')

#To read every lines the targeted file
with open('TargetedFile.txt','r') as f:
	for line in f:
		print(line,end='')
print('\n')

#To print number of characted in file
with open('TargetedFile.txt','r') as f:
	content=f.read(100)
	print(content)

#Prints every thing using while loop
with open('TargetedFile.txt','r') as f:
	sizeOFcontent=10
	content=f.read(sizeOFcontent)
	print()

	#Shows the current location of reading
	print(f.tell())

	while len(content)>0:
		print(content,end='*')

		#If this is not written this becomes the infinite loop
		content=f.read(sizeOFcontent)
print('\n')

#Making the reading cursor to change the location of reading
with open('TargetedFile.txt','r') as f:
	sizeOFcontent=10
	content=f.read(sizeOFcontent)
	print(content)

	#Makes the cursor to move into the zeroth position
	f.seek(0)
	content=f.read(sizeOFcontent)
	print(content)

#Writing the file it automatically creates the file if it doesnt
#exist if does exit and dont want to over write you can change 
#to 'a' mode to append the writing
with open('WritingFile.txt','w') as f:
	f.write('This is self')
	f.write(' created.')

#To change the cursor location
with open('WritingFile.txt','w') as f:
	f.write('This is self')
	f.seek(0)
	f.write(' created.')

#Making copy of TargetedFile 
with open('TargetedFile.txt','r') as rf:
	with open('Writing.txt','w') as wf:
		for item in rf:
			wf.write(item)

#Copying a image need to be in binary reading and writing
with open('i.JPG','rb') as rf:
	with open('Writing.JPG','wb') as wf:
		for item in rf:
			wf.write(item)

with open('i.JPG','rb') as rf:
	with open('Chunk.JPG','wb') as wf:
		chunk=1024
		r_f=rf.read(chunk)
		while len(r_f)>0:
			wf.write(r_f)
			r_f=rf.read(chunk)

with open('file.txt','r') as rd:
	result=rd.readlines(9)#try to change the numbers of any range and find it out
	print(list(result))