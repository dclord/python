#!/usr/bin/python
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

def getip():
    u = "http://icanhazip.com"
    r = requests.get(u)
    ip = r.text.strip("\n")
    today = date.today()
    today = today.strftime("%d/%m/%Y")
    sendemail(ip, today)

def sendemail(ip, today):
    msg = MIMEMultipart()
    msg['From'] = '<to address>'
    msg['To'] = '<from address>'
    msg['Subject'] = 'External IP - %s' % (today)
    message = '%s' % (ip)
    msg.attach(MIMEText(message))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.ehlo()
    s.login("<username>", "<password>")
    s.sendmail('From', 'To', msg.as_string())
    s.quit()

if __name__ == "__main__":
    getip()
