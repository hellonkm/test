#!/usr/bin/python
# -*- coding:utf-8 -*-
from os import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
import random,time
import datetime

class kebitool(object):
    
    def __init__(self):
        self.test = 'test'

    def __del__(self):
        pass 

    def createPhone(self):
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

    def super_date(self, days=0, hours=0, minutes=0, type=1):
        '''
        type=1:%Y-%m-%d %H:%M:%S
        type=2:%Y-%m-%d
        type=3:%Y%m%d
        type=4:%Y%m
        type=5:%Y-%m
        '''
        date = datetime.datetime.now() + datetime.timedelta(days=days,
        hours=hours, minutes=minutes)
        if type == 1:
        date = date.strftime('%Y-%m-%d %H:%M:%S')
        elif type == 2:
        date = date.strftime('%Y-%m-%d')
        elif type == 3:
        date = date.strftime('%Y%m%d')
        elif type == 4:
        date = date.strftime('%Y%m')
        elif type == 5:
        date = date.strftime('%Y-%m')
        elif type == 6:
        date = date.strftime('%Y年%m月%d日 %H:%M').encode('gb2312') 
        return date
        #robotframe 的定时发文使用
        def robot_release_date(self):

        date = datetime.datetime.now() + datetime.timedelta(hours=4)
        date = date.strftime('%Y年%m月%d日 %H:%M')
        date = unicode(date,"utf-8")
        return date

# if __name__ == '__main__':
#     w = tool()
#     phone = w.createPhone()
#     print phone        