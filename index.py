#coding:UTF-8

"""
一个简单的服务器监控工具
@author:yubang
2015-05-10
"""

from lib import disk,http
from config import config
import time

def main():
    "入口函数"
    while True:
        if config.USE_DISK:
            disk.init()
        if config.USE_HTTP:
            http.init()
        time.sleep(5)
    
if __name__ == "__main__":
    main()
