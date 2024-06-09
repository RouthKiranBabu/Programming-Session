# 1. open the command window

# 2. and type: python -m smtpd -c DebuggingServer -n localhost:1025. press enter

import smtplib
import os

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

with smtplib.SMTP('localhost',1025) as smtp:
	try:
		print("logged in...")
		print("sending...")
		subject="Hi myself python subject declaration!"
		body="Nice to meet myself!"
		msg=f"Subject: {subject}\n\n{body}"
		smtp.sendmail(email_address,email_address,msg)
	except Exception as e:
		print(e)
	else:
		print("Sent the mail!")
	finally:
		print("Process completed!")
#output in command prompt
'''
---------- MESSAGE FOLLOWS ----------
b'Subject: Hi myself python subject declaration!'
b'X-Peer: ::1'
b''
b'Nice to meet myself!'
------------ END MESSAGE ------------
'''