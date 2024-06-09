#Send a photo
import smtplib
import os
from email.message import EmailMessage
#to determine what kind of image that we are attaching
import imghdr

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

msg=EmailMessage()
msg['Subject']="See this image"
msg['From']=email_address
msg['To']=email_address
msg.set_content("How's the message!")

with open("hack_photo.jpg",'rb') as rp:
	photo_data=rp.read()
	file_type=imghdr.what(rp.name)
	#print(file_type)
	#output is: jpeg
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