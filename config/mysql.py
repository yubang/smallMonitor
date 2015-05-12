#coding:UTF-8

"""
mysql监控配置
"""

MYSQL_PINGCOMMAND = "mysqladmin"
MYSQL_CHECKINTERVAL = 60
MYSQL_LISTS=[
    {'host':'127.0.0.1','port':3306,'username':'root','password':'root'}
]

