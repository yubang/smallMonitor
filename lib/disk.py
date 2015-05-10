#coding:UTF-8

"""
磁盘监控模块
"""

from config import disk
from lib import core
import os,re,time

login_time=0

def init():
    "对外接口"
    global login_time
    
    if not time.time()-login_time>disk.DISK_DELAY:
        return False
    
    for t in disk.DISK_PATH:
        warn,data=check(t)
        if not warn:
            login_time=time.time()
            message="磁盘监控预警提示，磁盘使用率超过%s"%(disk.DISK_USED)+"%\n监控结果："+data
            message=message.decode("UTF-8")
            print message
            core.sendEmail(message)
            print u"邮件已经发出"
    
def check(path):
    "检测是否超出预警"
    r=os.popen("df -h "+path)
    for line in r:
        data=line.rstrip()
    datas=re.split(r'\s+',data)
    used=datas[4].encode("UTF-8").replace("%","")
    return int(used) < disk.DISK_USED,data
