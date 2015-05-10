#coding:UTF-8

"""
一个简单的服务器监控工具
@author:yubang
2015-05-10
"""

from lib import disk
import time

def main():
    "入口函数"
    while True:
        disk.init()
        time.sleep(5)
    
if __name__ == "__main__":
    main()
