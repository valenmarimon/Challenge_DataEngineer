import email, smtplib, os, time, fnmatch
from datetime import date, timedelta, datetime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def sendMailTo():
    recepient_id=str(input('Type the email address to send the status to: '))
    today = datetime.now()
    today = today.strftime("%Y/%m/%d %H:%M:%S")
    
    login_id = 'testvm.challenge@gmail.com'
    login_pwd = "secure000"
    fro_ = login_id
    s_name = 'smtp.gmail.com'
    s_port = 587

    srvr = smtplib.SMTP(s_name, s_port)
    srvr.ehlo()
    srvr.starttls()
    srvr.ehlo()
    srvr.login(login_id, login_pwd)

    sub = "Status for data ingestion on " + str(today) + ": Successful"
    # loading MIMEMultipart obj onto outer var
    outer = MIMEMultipart('alternative')
    outer["From"] = 'testvm.challenge@gmail.com'
    outer["To"] = recepient_id 
    outer['Subject'] = sub

    #start sending email with attachment with original file name
    srvr.sendmail(fro_, recepient_id, outer.as_string())
    srvr.quit()

