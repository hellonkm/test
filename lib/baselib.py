#!/usr/bin/python
# -*- coding:utf-8 -*-
from os import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
# from logging import logging
import mysql.connector
import json,datetime 
from Crypto.Cipher import AES
import base64

class baselib(json.JSONEncoder):
    def __init__(self):
        self.conn = mysql.connector.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='bitrade')
        self.conn1= mysql.connector.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='trade')
        self.conn2= mysql.connector.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='coinnice_bitrade')
        self.conn3= mysql.connector.connect(host='127.0.0.1',port=3306,user='root',passwd='123456',db='coinnice_trade',)

    def __del__(self):
        pass
    def querybitrade(self,sql):
        try:
            self.cursor = self.conn.cursor()
            datares = self.cursor.execute(sql)
            datares = self.cursor.fetchone()
            datares = json.dumps(datares,cls=CJsonEncoder).decode("unicode-escape")            
        except mysql.connector.Error as e:
            print ('Error : {}'.format(e))
        # finally:
        #     print 'Connect wemedia closed in finally'
        return datares

    def updateCoinBitrade(self,sql):
        try:
            self.cursor = self.conn2.cursor()
            self.cursor.execute(sql)
            self.conn2.commit()
            
            # 提交到数据库执行
        except mysql.connector.Error as e:
            self.conn2.rollback()
            return  json.dumps('connecterror')   
        
        return json.dumps('success')

    def updateBitrade(self,sql):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(sql)
            self.conn.commit()
            
            # 提交到数据库执行
        except mysql.connector.Error as e:
            self.conn.rollback()
            return  json.dumps('connecterror')           
        return json.dumps('success')

    def update_trade(self,sql):
        try:
            self.cursor = self.conn1.cursor()
           
            self.cursor.execute(sql)
            self.conn1.commit()
            # 提交到数据库执行
        except mysql.connector.Error as e:
            self.conn1.rollback()
            return  json.dumps('connecterror')   
        
        return json.dumps('success')

    def Get_tradeSqlAll(self,sql):
        try:
            self.cursor = self.conn1.cursor()
            datares = self.cursor.execute(sql)
            datares = self.cursor.fetchall()
            datares = json.dumps(datares,cls=CJsonEncoder).decode("unicode-escape")
        
        except mysql.connector.Error as e:
            print ('Error : {}'.format(e))
        # finally:
        #     print 'Connect wemedia closed in finally'
        return datares 

    def query_trade(self,sql):
        try:
            self.cursor = self.conn1.cursor()
            datares = self.cursor.execute(sql)
            datares = self.cursor.fetchone()
            datares = json.dumps(datares,cls=CJsonEncoder).decode("unicode-escape")         
        except mysql.connector.Error as e:
            print ('Error : {}'.format(e))
        # finally:
        #     print 'Connect wemedia closed in finally'
        return datares

    def GetBitradeSqlAll(self,sql):
        try:
            self.cursor = self.conn.cursor()
            datares = self.cursor.execute(sql)

            datares = self.cursor.fetchall()
            datares = json.dumps(datares,cls=CJsonEncoder).decode("unicode-escape")

        except mysql.connector.Error as e:
            print ('Error : {}'.format(e))
        # finally:
        #     print 'Connect wemedia closed in finally'
        return datares
         
    def update_coin_trade(self,sql):
        try:
            self.cursor = self.conn3.cursor()
           
            self.cursor.execute(sql)
            self.conn3.commit()
            # 提交到数据库执行
        except mysql.connector.Error as e:
            self.conn3.rollback()
            return  json.dumps('connecterror')   
        
        return json.dumps('success')

        #针对datetime数据重构json
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime("%Y-%m-%d")
        else:
            return json.JSONEncoder.default(self, obj)

#        解密           
#        generator = AES.new(key, AES.MODE_CBC, iv)
#        recovery = generator.decrypt(crypt)
#        print recovery.rstrip(PADDING) 

class signKey():
    def __init__(self):
        self.key = 'duyu123456java'
        self.mode = AES.MODE_CBC
        self.iv = 'duyu123456java'
        self.bs = 16  # block size
        self.PADDING = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def getSign(self,phone):
        
        PADDING = '\0'
        phone = str(phone)
        #PADDING = ' '
        generator = AES.new(self.key, self.mode, self.iv)
        crypt = generator.encrypt(self.PADDING(phone))
        #加密后的值   
        cryptedStr = base64.b64encode(crypt)
        result = cryptedStr.decode()
   
        return result            

# if __name__ == '__main__':
#     w= baselib()
# #     sign = w.getSign(13602455810)
# #     print sign   
#     sql = '''select * from trade$platform_user where mobile = '+86|13602455810' '''
# #    sql = '''select * from admin where mobile_phone = 13602455810 '''
#     data1 = w.update_trade(sql)
#     print data1
#     w.conn.commit()
#     w.cursor.close
#     w.conn.close
