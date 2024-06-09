
#This whole command is no a python programming and this code is writen in command prompt

#command for help
#pip help
#Output
'''
Usage:   
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
'''

#To check all the modules
#pip list
#Output
'''
Package                   Version
------------------------- --------------
anyio                     4.3.0
argon2-cffi               23.1.0
argon2-cffi-bindings      21.2.0
arrow                     1.3.0
asgiref                   3.8.1
asttokens                 2.4.1
...
'''

#Command that helps for installation
#pip help install
'''
Usage:
  pip install [options] <requirement specifier> [package-index-options] ...
  pip install [options] -r <requirements file> [package-index-options] ...
  pip install [options] [-e] <vcs project url> ...
  pip install [options] [-e] <local project path> ..
'''
'''
To search the module and know its description
This may not be available or install by having interner it does just above work'''
#pip search Pympler
#Output
'''
ERROR: XMLRPC request failed [code: -32500]
'''

#To install any module
#pip install Pympler
#Output
'''
Collecting Pympler
  Using cached Pympler-1.0.1-py3-none-any.whl.metadata (3.4 kB)
Using cached Pympler-1.0.1-py3-none-any.whl (164 kB)
Installing collected packages: Pymp
'''

#To uninstall any module
#pip uninstall Pympler
#Output
'''
Found existing installation: Pympler 1.0.1
Uninstalling Pympler-1.0.1:
  Would remove:
    c:\users\kiran\
'''

#To check outdated version of every module
#pip list -o
#Output
'''
Package           Version Latest Type
----------------- ------- ------ -----
Babel             2.14.0  2.15.0 wheel
Django            5.0.4   5.0.6  wheel
Jinja2            3.1.3   3.1.4  wheel
jupyter_client    8.6.1   8.6.2  wheel
'''

#To update a package
#pip install -U matplotlib
#Output
'''
Requirement already satisfied: matplotlib in c:\users\kiran\appdata\local\programs\python\python312\lib\site-packages (3.8.4)
Collecting matplotlib
  Downloading matplotlib-3.9.0-cp312-cp312-win_amd64.whl.metadata (11 kB)
Requirement already satisfied: contourpy>=1.0.1 in c:\users\kiran\appdata\local\programs\python\python312\lib\site-packages (from matplotlib) (1.2.1)
Requirement already satisfied: cy
'''

#After updating django-taggit is not listed on command output named: pip list -o

#To check its new version go for list command: pip list
