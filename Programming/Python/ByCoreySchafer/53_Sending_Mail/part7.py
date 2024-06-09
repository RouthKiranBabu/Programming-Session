#Send a file
import smtplib
import os
from email.message import EmailMessage
import imghdr

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

msg=EmailMessage()
msg['Subject']="See this SMTP documention."
msg['From']=email_address
msg['To']=email_address
msg.set_content("How's the message!")

files=["smtp_documentation.pdf"]

for file in files:
	with open(file,'rb') as f:
		file_data=f.read()
		file_name=f.name
	msg.add_attachment(file_data,maintype='application',subtype='octet-stream', filename=file_name)

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