import smtplib
import os

#to make msg more better formatting
from email.message import EmailMessage

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

msg=EmailMessage()
msg['Subject']="Hi myself python subject declaration!"
msg['From']=email_address
msg['To']=email_address
msg.set_content("Nice to meet myself!")

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	try:
		print("logged in...")
		print("sending...")
		smtp.login(email_address,email_password)
		smtp.send_message(msg)
	except Exception as e:
		print(e)
	else:
		print("Sent the mail!")
	finally:
		print("Process completed!")