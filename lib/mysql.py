#coding:UTF-8


"""
mysql检测模块
@author:yubang
2015-05-12
"""


import os
from config import mysql
from lib import core

def init():
    "入口函数"
    sign=True
    for obj in mysql.MYSQL_LISTS:
        if not check(obj['host'],obj['port'],obj['username'],obj['password']):
            sign=False
            message=(u"检测到数据库不可用（数据库主机：%s，数据库端口：%d）！")%(obj['host'],obj['port'])
            core.sendEmail(message)
            print u"邮件已经发送"
    return sign
    
    
def getIntervalTime():
    "获取检测间隔时间"
    return mysql.MYSQL_CHECKINTERVAL
    
    
def check(host,port,username,password):
    "检测数据库服务是否可用"
    pipeline=os.popen('%s ping -h %s -u %s -p%s -P %d'%(mysql.MYSQL_PINGCOMMAND,host,username,password,port))
    result=pipeline.read().strip()
    if result == 'mysqld is alive':
        return True
    else:
        return False


