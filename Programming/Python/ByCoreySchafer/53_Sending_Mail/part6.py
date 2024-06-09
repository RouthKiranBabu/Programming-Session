#Send a multi photo
import smtplib
import os
from email.message import EmailMessage
import imghdr

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

msg=EmailMessage()
msg['Subject']="See this image"
msg['From']=email_address
msg['To']=email_address
msg.set_content("How's the message!")

files=["hack_photo.jpg","scenery.jpg","goku_transform.jpg"]

for file in files:
	with open(file,'rb') as rp:
		photo_data=rp.read()
		file_type=imghdr.what(rp.name)
		file_name=rp.name
	msg.add_attachment(photo_data,maintype='image',subtype=file_type, filename=file_name)

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