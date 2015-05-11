#coding:UTF-8

"""
http监控模块
"""


from config import http
from lib import core
import httplib,time


lastCheckTime = 0


def init():
    "入口函数"
    global lastCheckTime
    if time.time() - lastCheckTime <  http.HTTP_INTERVAL:
        return None
    
    lastCheckTime = time.time()
    
    for obj in http.HTTP_LISTS:
        if not check(obj['host'],obj['port'],obj['url'],obj['method'],obj['data'],obj['timeout']):
            message="发现网址无法访问http://%s:%s%s"%(obj['host'],obj['port'],obj['url'])
            core.sendEmail(message.decode("UTF-8"))
            print u"邮件已经发出！"
    
    
def check(host,port,url,method,data,timeout):
    "检测url是否可用"
    headers={}
    try:
        con=httplib.HTTPConnection(host,port,timeout)
        con.request(method,url,data,headers=headers)
        response=con.getresponse()
        code=response.status
        con.close()
        if code != 200:
            return False
        return True
    except:
        return False
