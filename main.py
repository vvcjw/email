# -*- coding:utf-8 -*-

import os
import smtplib
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import json

'''
reference

https://coding-kindergarten.tistory.com/219
'''


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
        smtp.ehlo()

    smtp.login(email, passwd)
    return smtp


 
def send_email(From, To, subject, message, attach_files=[], subtype='plain'):
    form = MIMEBase('multipart', 'mixed')
    form['From']=From
    form['To']=','.join(To)
    form['Subject']=Header(subject.encode('utf-8'), 'utf-8')
    msg = MIMEText(
        message.encode('utf-8'),
        _subtype=subtype,
        _charset='utf-8'
    )
    form.attach(msg)

	for fpath in attach_files:
        
        folder, file = os.path.split(fpath) 
        
        with open(fpath, 'rb') as f:
            body = f.read()
        
        msg = MIMEApplication(body, _subtype=subtype)
        msg.add_header('Content-Disposition', 'attatchment',
                        filename=(Header(file, 'utf-8').encode()))
        form.attach(msg)




#msg = MIMEText('content')
#msg['Subject'] = 'title'
#msg['To'] = 'sender@email.com'
#smtp.sendmail('sender@email.com', 'receiver@email.com', msg.as_string())
#smtp.quit()
