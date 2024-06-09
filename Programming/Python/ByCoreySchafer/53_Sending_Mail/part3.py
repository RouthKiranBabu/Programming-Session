import smtplib
import os

email_address=os.environ.get("EMAIL_ACCOUNT")
email_password=os.environ.get('EMAIL_PASSWORD')

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
	try:
		print("logged in...")
		print("sending...")
		smtp.login(email_address,email_password)

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