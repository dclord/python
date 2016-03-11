#!/usr/bin/python3
# Edit all sections below which are encompassed in <> 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

try:
	file = open('emaillist')
	
	emails = []
	
	for text in file.readlines()
		text = text.rstrip()
		
		msg = MIMEMultipart()
		msg['From'] = <from addr> 
		msg['To'] = text
		msg['Subject'] = 'Testing Script'
		message = 'If you get this, the script worked!'
		msg.attach(MIMEText(message))

		mailserver = smtplib.SMTP('<smtp server addr>', 25)
		#identify to mail server
		mailserver.ehlo()
		#start TLS
		mailserver.starttls()
		#re-id after encrpytion
		mailserver.ehlo()
		mailserver.login('<username>', '<password>')

		mailserver.sendmail('<email addr>', text ,msg.as_string())

		mailserver.quit()

else
except IOError as err:
	print('opps error: %s') % err
	
	



