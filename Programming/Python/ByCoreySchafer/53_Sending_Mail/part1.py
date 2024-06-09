#https://myaccount.google.com/lesssecureapps?pli=1 
#go to above link and make it less secure app

#for two step verificaton you can creat app password to connect through python
#below link for app password
#https://myaccount.google.com/apppasswords?pli=1&rapt=AEjHL4MxkWWEOdqPUjRAYy2nYB1FNOmFIZ6foA7mMYb2wns9L7Klth06RhyqgqEq1AvxCmmciWpLqzUFVPpLJg5oh1A3EfnlFQ

#below like helps to make app password
#https://www.youtube.com/watch?v=ndxUgivCszE

#Turn off two step verification

import smtplib
import os

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

#For gmail 
#smtp: 'smtp.gmail.com'
#port: 587
with smtplib.SMTP('smtp.gmail.com',587) as smtp:
	try:
		print("logged in...")
		print("sending...")
		
		#ehlo method identifies the mail server that are using 
		smtp.ehlo()
		#to encrypt our traffic
		smtp.starttls()
		#now to reidentify our cell as a encrypted connection 
		smtp.ehlo()
		#log in by login method 
		smtp.login(email_address,email_password)

		subject="Hi myself python subject declaration!"
		body="Nice to meet myself!"

		msg=f"Subject: {subject}\n\n{body}"

		#smtp.sendmail(SENDER,RECEIVER,msg)
		smtp.sendmail(email_address,email_address,msg)
	except Exception as e:
		print(e)
	else:
		print("Sent the mail!")
	finally:
		print("Process completed!")

#sending each time and opening email takes lots of time to do simple we can use
#some local debug server for testing. See part 2