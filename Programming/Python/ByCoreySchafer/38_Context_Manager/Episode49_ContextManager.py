f=open('sample.txt','w')
f.write('Hi this is the first sentence.')
f.close()
#Or you can write as
with open('sample.txt','w') as f:
	f.write('Hi this is the first sentence.')

class Open_File():
	def __init__(self,filename,mode):
		self.filename=filename
		self.mode=mode
	def __enter__(self):
		self.file=open(self.filename,self.mode)
		return self.file
	def __exit__(self,exc_type,exc_val,traceback):
		self.file.close()
with Open_File('sample1.txt','w') as f:
	f.write('This the first new sentence.')
print(f.closed)

from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
	try:
		f=open(file,mode)
		yield f
	except Exception as e:
		print(e)
	finally:
		f.close()

with open_file('sample2.txt','w') as f:
	f.write('this is the first line and first sentence.')
print(f.closed)

import os
cwd=os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd=os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)
print()
#Above can also be written as below

@contextmanager
def change_dir(destination):
	try:
		cwd=os.getcwd()
		os.chdir(destination)
		yield
	finally:
		os.chdir(cwd)

with change_dir('Sample-Dir-One'):
	print(os.listdir())
with change_dir('Sample-Dir-Two'):
	print(os.listdir())

