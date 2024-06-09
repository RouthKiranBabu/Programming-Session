import os
from datetime import datetime

#Shows attributes and methods
print(dir(os))
#Output
'''
['DirEntry', 'EX_OK', 'F_OK', 'GenericAlias', 'Mapping', 
'MutableMapping', 'O_APPEND', 'O_BINARY', 'O_CREAT', 'O_EXCL',
'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', 'O_SEQUENTIAL',
'O_SHORT_LIVED...
'''

#Shows current working directory
print(os.getcwd())
#Output
#c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python

#Shifts past working directory to new directory this does'nt means that 
#this python file moves to that location
os.chdir('c:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python')
print(os.getcwd())
#Output
#c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python

#Going back
print(os.getcwd())
os.chdir("./Folder")
os.chdir("../");os.chdir(2*"../")
print(os.getcwd(), os.listdir(), sep = ". ")
#Output
#c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python
#c:\Users\kiran\OneDrive\Desktop. ['CareerNotes', 'desktop.ini', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']

#This shows files and directories in the current directory
print(os.listdir())
#Output
#['CareerNotes', 'desktop.ini', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']

#Mkdir creates the file but not the subfolders like makedirs you can execute only ones
os.mkdir('FolderCreated')
print(os.listdir())
#Output
'''
['CareerNotes', 'desktop.ini', 'FolderCreated', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']
'''

#Makedirs must include subfolders otherwise error occurs
os.makedirs('makedirsFolder/SubFolder/Newfoldr')
print(os.listdir())
os.chdir("./makedirsFolder")
print(os.listdir())
os.chdir("./SubFolder")
print(os.listdir())
os.chdir("./Newfoldr")
print(os.listdir())
#Output
'''
['CareerNotes', 'desktop.ini', 'FolderCreated', 'makedirsFolder', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']
['SubFolder']
['Newfoldr']
[]
'''

#Make makedirs as comment otherwise FileExistsError
#os.makedirs('makedirsFolder/SubFolder/Newfoldr')
os.chdir(3*"../")
print(os.getcwd(), os.listdir())
#Output
#c:\Users\kiran\OneDrive\Desktop ['CareerNotes', 'desktop.ini', 
#'FolderCreated', 'makedirsFolder', 'ProteusAndArduino', 'ScriptLearn', 
#'TechNotes']

#Removes directories
print(os.listdir())
os.rmdir('FolderCreated')
os.removedirs('makedirsFolder/SubFolder/Newfoldr')
print(os.listdir())
#Output
#['CareerNotes', 'desktop.ini', 'FolderCreated', 'makedirsFolder', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']
#['CareerNotes', 'desktop.ini', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']

print(os.getcwd())
#Output
#c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python
os.chdir(2*"../")
print(os.getcwd())
#Output
#c:\Users\kiran\OneDrive\Desktop
print(os.listdir())
#Output
#['CareerNotes', 'desktop.ini', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']
os.mkdir("NewMkDir")
print(os.listdir())
#Output
#['CareerNotes', 'desktop.ini', 'NewMkDir', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']

#Renames the file from name called FileCreatedByOS to Renamed file
os.rename('NewMkDir','osCreatedFolder')
print(os.listdir())
#Output
#['CareerNotes', 'desktop.ini', 'osCreatedFolder', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']

print(os.getcwd())
os.chdir(2 * "../")
print(os.getcwd())
print(os.listdir())
#Output
#c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python
#c:\Users\kiran\OneDrive\Desktop
#['CareerNotes', 'desktop.ini', 'osCreatedFolder', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']

#To know more about the file or directory 
print(os.stat('osCreatedFolder'))
#Output
#os.stat_result(st_mode=16895, st_ino=26458647810860475, 
#st_dev=8539039635429594001, st_nlink=1, st_uid=0, st_gid=0, 
#st_size=0, st_atime=1716520844, st_mtime=1716519998, st_ctime=1716519998)

#To print secefic stat st_mtime is modification time
print(os.stat('osCreatedFolder').st_mtime)
#Output
#1716519998.5734873

#To print datetime of modification
mod_time=os.stat('osCreatedFolder').st_mtime
print(datetime.fromtimestamp(mod_time))
#Output
#2024-05-24 08:36:38.573487

#To check all the directory path,dirnames,filenames within the walk directory
for dirpath,dirnames,filenames in os.walk('c:/Users/kiran/OneDrive/Desktop'):
	print('current path: ',dirpath)
	print('dirnames: ',dirnames)
	print('filenames: ',filenames)
#Output
'''
current path:  c:/Users/kiran/OneDrive/Desktop
dirnames:  ['CareerNotes', 'osCreatedFolder', 'ProteusAndArduino', 'ScriptLearn', 'TechNotes']
filenames:  ['desktop.ini']
current path:  c:/Users/kiran/OneDrive/Desktop\CareerNotes
dirnames:  []
filenames:  ['CentralizedCounselling.pdf', 'ContactDetailsOfPaticipatingInstitutes.pdf', 'FAQ.pdf', 'TentativeSchedulePhaseOne.pdf']
current path:  c:/Users/kiran/OneDrive/Desktop\osCreatedFolder
dirnames:  []
filenames:  []
...
'''

#Gets system variable present from 
#(View Advanced System Settings -> Environment variables 
#-> System Variables -> Variable=OS has a value=Windows_NT)
print(os.environ.get('OS'))
#Output
#Windows_NT

#Shows the base name or last subdirectory
print(os.path.basename('C:/Users/user/Desktop/ScriptLearn/Learn Python'))
print(os.path.basename('C:/Users/user/Desktop/ScriptLearn/'))
print(os.path.basename('C:/Users/user/Desktop/ScriptLearn/Learn Python/FromGit.py'))
#Output
'''
Learn Python

FromGit.py
'''

#Shows the directory path above the base name
print(os.path.dirname('C:/Users/user/Desktop/ScriptLearn'))
#Output
#C:/Users/user/Desktop

#To show both the name and directory
print(os.path.split('C:/Users/user/Desktop/Programming/Python/Python Programming/Programs/Episode9_Importing_modules_and_Exploring_Libuary/Mymodule.py'))
#Output
#('C:/Users/user/Desktop/ScriptLearn/Learn Python', '1_FromGit.py')

#Check wether the path exist or not
print(os.path.exists('C:/Users/user/Desktop/ScriptLearn/Learn Python'))
#Output
#False

#Check wether the path exist or not in the environment variable -> System Variables
print(os.path.exists('C:/Users/user/Desktop/ScriptLearn/Learn Python'))
print(os.path.exists('C:/Windows'))
print(os.path.exists('%USERPROFILE%\AppData\Local\Microsoft\WindowsApps'))
#Output
#c:\Users\kiran\OneDrive\Desktop\ScriptLearn\Learn Python\2_LearnGit.py:39: SyntaxWarning: invalid escape sequence '\A'
#  print(os.path.exists('%USERPROFILE%\AppData\Local\Microsoft\WindowsApps'))
#False
#True
#False

#check wether it is a file or not
print(os.path.isfile('C:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python/Folder'))
print(os.path.isfile('C:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python/1_FromGit.py'))
print(os.path.isfile('C:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python/file.txt'))
#Output
'''
False
True
True
'''

#Check wether it is a director or not
print(os.path.isdir('C:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python/Folder'))
print(os.path.isdir('C:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python/1_FromGit.py'))
#Output
'''
True
False
'''

#Splits the extension of the file
print(os.path.splitext('C:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python/1_FromGit.py'))
#Output
#('C:/Users/kiran/OneDrive/Desktop/ScriptLearn/Learn Python/1_FromGit', '.py')
