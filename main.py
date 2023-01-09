# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import json


def email_login(email, passwd):
    with open('server_info.json') as f:
	    server_info = json.load(f)

    domain = email.split('@')[1]
    smtp_server = server_info[domain]
    smtp_port = server_info[domain]
    smtp_protocol = server_info[domain]
    
    if smtp_protocol == 'TLS':
        smtp = smtplib.SMTP(smtp_server, stmp_port)
        # say Hello
        smtp.ehlo() 
        smtp.starttls()
    elif smtp_protocol == 'SSL':
        # not tested
        smtp = smtplib.SMTP_SSL(smtp_server, stmp_port)

    smtp.login(email, passwd)
    return smtp
 

msg = MIMEText('content')
msg['Subject'] = 'title'
msg['To'] = 'sender@email.com'
smtp.sendmail('sender@email.com', 'reciver@email.com', msg.as_string())
smtp.quit()
