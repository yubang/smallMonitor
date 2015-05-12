#coding:UTF-8

"""
一个简单的服务器监控工具
@author:yubang
2015-05-10
"""


from lib import disk,http,mysql
from config import config
import time,threading


class Monitor(threading.Thread):
    "监视器线程"
    def __init__(self,fn,sleepTime):
        threading.Thread.__init__(self)
        self.__fn=fn
        self.__sleepTime=sleepTime
    def run(self):
        startMonitor(self.__fn,self.__sleepTime)


def checkNeedRun(lastWarnTime):
    "检测是否可以运行监控"
    if time.time() - lastWarnTime > config.WARN_INTERVAL:
        return True
    else:
        return False


def startMonitor(fn,sleepTime):
    "开始监控"
    lastWarnTime=0
    while True:
        if checkNeedRun(lastWarnTime) and not fn():
            lastWarnTime = time.time()
        time.sleep(sleepTime)
    

def main():
    "入口函数"
    if config.USE_DISK:
        monitor=Monitor(disk.init,disk.getIntervalTime())
        monitor.setDaemon(True)
        monitor.start()
    if config.USE_HTTP:
        monitor=Monitor(http.init,http.getIntervalTime())
        monitor.setDaemon(True)
        monitor.start()
    if config.USE_MYSQL:
        monitor=Monitor(mysql.init,mysql.getIntervalTime())
        monitor.setDaemon(True)
        monitor.start()
    raw_input("按任意键退出！")
    
if __name__ == "__main__":
    main()
