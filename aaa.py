#! /usr/bin/env python
# coding:utf-8

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import sys
def send_mail(_to_email,_subject,_message):
# 定义邮件发送
 smtp_host = 'smtp.xxx.xx'
 from_email = 'xxx@xxx.xx'
 passwd = 'xxxxxx'
 msg = MIMEText(_message,'plain','utf-8')
 msg['Subject'] = _subject
 smtp_server = smtplib.SMTP(smtp_host,25)
 smtp_server.login(from_email,passwd)
 smtp_server.sendmail(from_email,[_to_email],msg.as_string())
 smtp_server.quit()
if __name__ == '__main__':
 send_mail(sys.argv[1],sys.argv[2],sys.argv[3])
