#Send a plain text html
import smtplib
import os
from email.message import EmailMessage
import imghdr

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

contents=['routhkiran456@gmail.com']

msg=EmailMessage()
msg['Subject']="See this SMTP documention."
msg['From']=email_address
msg['To']=', '.join(contents)
msg.set_content("This is a plain text email.")

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<h1 style="color:SlateGray;">This is an Email HTML!</h1>
</body>
</html>
""",subtype='html')

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