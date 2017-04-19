import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config

USER = config.email
PASS = config.password
TO = config.recipient

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(msg):
    content = MIMEMultipart('alternative')
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(USER, PASS)

    content['Subject'] = 'Mieszkanie PasPI'
    text = MIMEText(msg, 'plain')
    content.attach(text)

    smtpserver.sendmail(USER, TO, content.as_string())
    smtpserver.close()
