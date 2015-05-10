#coding:UTF-8

"""
核心方法
"""

import smtplib
from email.mime.text import MIMEText
from config import config

def sendEmail(message):
    _user = config.EMAIL_FROM
    _pwd  = config.EMAIL_PASSWORD
    _to   = config.EMAIL_TO

    #使用MIMEText构造符合smtp协议的header及body
    msg = MIMEText(message.encode("UTF-8"),_charset='UTF-8')
    msg["Subject"] = config.EMAIL_TITLE
    msg["From"]    = _user
    msg["To"]      = _to

    s = smtplib.SMTP(config.EMAIL_SMTP, timeout=30)#连接smtp邮件服务器,端口默认是25
    s.ehlo()
    s.starttls()
    s.login(_user, _pwd)#登陆服务器
    s.sendmail(_user, _to, msg.as_string())#发送邮件
    s.close()
