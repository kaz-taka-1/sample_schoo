import smtplib, ssl
from email.mime.text import MIMEText
import my_gmail_account as gmail
import gmail_send

msg = MIMEText('こんにちは。CCのテストでみんなに送っています！')
msg['Subject'] = 'CCのテスト'
msg['To'] = gmail.account
msg['From'] = gmail.account
msg['Cc'] = gmail.account
# msg['Bcc'] = ''
msg.add_header('reply-to', 'test@example.com') #

gmail_send.send_gmail(msg)
print("ok")