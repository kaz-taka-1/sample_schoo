import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

import gmail_send
import my_gmail_account as gmail

msg = MIMEMultipart()
msg['Subject']='富士山の写真'
msg['From']=gmail.account
msg['To']=gmail.account

txt = MIMEText('先日ドライブに行った時に撮影した写真です。ご査収ください。')
msg.attach(txt)

with open('sky.jpg', 'rb') as fp:
    img = MIMEImage(fp.read())
    msg.attach(img)

gmail_send.send_gmail(msg)
print("ok")