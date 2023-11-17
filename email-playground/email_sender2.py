from string import Template
import smtplib
from dotenv import load_dotenv
import os
from email.message import EmailMessage
from pathlib import Path

html = Template(Path("./index.html").read_text())
email = EmailMessage()

load_dotenv("./.env")

email['from'] = "<name_of_sender>"
email['to'] = "<recepient's_email_address>"
email['subject'] = "<subject_of_the_email>"
email.set_content(html.substitute({'name':"asmodius"}),'html')
# html variable has text from index.html
# During initialization it is converted to Template object
# so $name in the text of html variable can be substituted with "asmodisu"
# 'html' is the 2nd argument of set_content and it sets the subtype of the email content
email_sender = str(os.getenv("EMAIL"))
password = str(os.getenv("PASSWORD"))

with smtplib.SMTP_SSL(host="smtp.gmail.com",port=465) as smtp:
    smtp.ehlo()
    smtp.login(email_sender,password)
    smtp.send_message(email)
    print("all good boss")
