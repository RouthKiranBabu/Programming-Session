import os

transcript_file_copied = 'guide.txt'

print(os.listdir())
for dir in os.listdir():
    if "." not in dir:
        os.chdir("./{}".format(dir))
        print(dir, os.listdir())
        if transcript_file_copied in os.listdir():
            print("Found! '{}' file in [{}] folder.".format(transcript_file_copied, dir))
            break 
        else: os.chdir("../")


#If the file(copiedtranscript.txt) has f type of transcript which you have copied from 
#youtube and pasted in the file
'''
hey there how's it going everybody in this video we'll be learning how to use our application to add users to our database and also how to authenticate
0:06
users so that they can log in log out and also soon be able to create posts
0:11
and things like that so let's go ahead and get started so in a previous video we created our database and saw how we
0:17
could manually create some users and posts but now let's add that same logic to our application to create these users
0:24
...
'''
#Using the function create_transcript will create the transcript.txt in your current directory
'''#Then it creates the file transcript.txt which has the following form of text
hey there how's it going everybody in this video we'll be learning how to use our application to add users to our database and also how to authenticate
users so that they can log in log out and also soon be able to create posts
and things like that so let's go ahead and get started so in a previous video we created our database and saw how we
could manually create some users and posts but now let's add that same logic to our application to create these users
through the registration form now before we create our users we're going to need a way to hash our passwords so in the
previous video we were using plain text passwords for our examples but you never want to do this with your actual website
because if anyone was to ever get access to your database then they would have the logins for all of your users and
that's definitely not a good thing so there are several different hashing algorithms but one good one that we can
use is called bcrypt and there's an extension for flask that makes this easy to use and that is
called flask bcrypt so let's pull up our command line and install this with pip so I have my
virtual environment activated and I'm here in my project directory and I'm going to install this just by saying pip
install and this is flask - be crypt so let's install that and once that is
...
'''

def create_transcript(file = transcript_file_copied):
    modified_file = "transcript.txt"
    if modified_file in os.listdir(): os.remove(modified_file)
    with open(file, 'r') as rf:
        with open(modified_file, 'w') as wf:
            val = rf.readline()
            while val:
                if not val[0].isdigit():
                    wf.write(val)
                val = rf.readline()
    return modified_file

create_transcript()
