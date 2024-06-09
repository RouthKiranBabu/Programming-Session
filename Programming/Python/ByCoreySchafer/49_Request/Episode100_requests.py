#gets information from websites 
#copy the link adress of image to get r.text
#copy the image adress for download concern
import requests
'''
r=requests.get("https://xkcd.com/353/")
print(r)
print(dir(r))

#to know things about object
print(help(r))

#to get html text of unicode
print(r.text)

r=requests.get('https://imgs.xkcd.com/comics/python.png')

#takes only byte 
print(r.content)

#creates a image file in the same directory
with open('comic.png','wb') as f:
	f.write(r.content)

#to check the good response to check our response are getting all right
#so we can check the status code 
#200 is success
#300 is redirects
#400 is client errors which does not have permission to use 
#500 is server errors
print(r.status_code)

#true for less than 400 response 
print(r.ok)

#Shows information about the image
print(r.headers)

# website https://httpbin.org/ that shows https method, auth, status
#codes, etc which is more helpful when you see it
'''
'''
payload={'page':2,'count':25}
r=requests.get('https://httpbin.org/get',params=payload)
print(r.text)
#output:
#{
#  "args": {
#    "count": "25", 
#    "page": "2"
 # }, 
 # "headers": {
 #   "Accept": "*/*", 
 #   "Accept-Encoding": "gzip, deflate", 
 #   "Host": "httpbin.org", 
 #   "User-Agent": "python-requests/2.21.0"
 # }, 
 # "origin": "106.222.144.54, 106.222.144.54", 
 # "url": "https://httpbin.org/get?page=2&count=25"
#}

#to know url
print(r.url)
'''

#to post the data to auth
payload={'username':"kiran",'password':'testing'}
r=requests.post('https://httpbin.org/post',data=payload)
#output for print(r.text)
#{
#  "args": {}, 
 # "data": "", 
 # "files": {}, 
 # "form": {
 #   "password": "testing", 
 #   "username": "kiran"
 # }, 
 # "headers": {
 #   "Accept": "*/*", 
 #   "Accept-Encoding": "gzip, deflate", 
 #   "Content-Length": "31", 
#    "Content-Type": "application/x-www-form-urlencoded", 
 #   "Host": "httpbin.org", 
 #   "User-Agent": "python-requests/2.21.0"
 # }, 
 # "json": null, 
 # "origin": "106.222.144.54, 106.222.144.54", 
 # "url": "https://httpbin.org/post"
#}
r_dict=r.json()
#output for print(r_dict['form'])
#{'password': 'testing', 'username': 'kiran'}

#the url that show the 
#{
 # "authenticated": true, 
#  "user": "kiran"
#}
r=requests.get('https://httpbin.org/basic-auth/kiran/testing',auth=('kiran','testing'))
print(r.text)
#output is: 
#{
#  "authenticated": true, 
#  "user": "kiran"
#}

#when setting wrong username
r=requests.get('https://httpbin.org/basic-auth/kiran/testing',auth=('kirans','testing'))
#print(r.text) it will show no response
print(r)
#output is:
#<Response [401]> which is a client error

r=requests.get('https://httpbin.org/basic-auth/kiran/testing',auth=('kiran','testing'))
print(r)
#output is:
#<Response [200]>

r=requests.get('https://httpbin.org/delay/1',timeout=9)
print(r)
#output is:
#<Response [200]>

