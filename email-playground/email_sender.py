import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage

email = EmailMessage()

load_dotenv("./.env")

email['from'] = "<name_of_sender>"
email['to'] = "<recepient's_email_address>"
email['subject'] = "<subject_of_the_email>"
email.set_content("<content_of_email>")
email_sender = str(os.getenv("EMAIL"))
password = str(os.getenv("PASSWORD"))

with smtplib.SMTP_SSL(host="smtp.gmail.com",port=465) as smtp:
    smtp.ehlo()
    smtp.login(email_sender,password)
    smtp.send_message(email)
    print("all good boss")
