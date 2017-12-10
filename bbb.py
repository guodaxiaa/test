#!/usr/bin/python
#coding:utf-8
import smtplib
from email.mime.text import MIMEText
import sys
#邮箱服务器地址
mail_host = 'smtp.163.com'
#邮箱用户名
mail_user = '15271819735@163.com'
#邮箱密码
mail_pass = 'guorui520'
mail_postfix = '163.com'
def send_mail(to_list,subject,content):
    me =mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content)
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False
if __name__ =="__main__":
    send_mail('601492323@qq.com','12345','这个是我的第一个Python发送邮件的测试!!!')
    #send_mail(sys.argv[1], sys.argv[2],sys.argv[3])