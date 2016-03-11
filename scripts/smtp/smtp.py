#!/usr/bin/python3
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg['From'] = 'Email address'
msg['To'] = 'to email address'
msg['Subject'] = 'Subject header'
message = 'here is the body of the email'
msg.attach(MIMEText(message))

mailserver = smtplib.SMTP('mail server address', port)
#identify to mail server
mailserver.ehlo()
#start TLS
mailserver.starttls()
#re-id after encrpytion
mailserver.ehlo()
mailserver.login('user', 'pass')

mailserver.sendmail('From', 'To',msg.as_string())

mailserver.quit()

