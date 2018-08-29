#!/usr/bin/python
# -*- coding:utf-8 -*-
from os import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
#import logging
#logging.basicConfig(level=logging.INFO)
from flask import Flask
from flask import request
import json
from kebi.lib import baselib
from kebi.tool import kebitool

# https://www.cnblogs.com/he12345/p/7486309.html
# https://www.cnblogs.com/vovlie/p/4182814.html
app = Flask(__name__)
 

# @app.route('/', methods=['GET', 'POST'])
# def home():
#     return '<h1>Home</h1>'
 

# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#     <p><input name="username"></p>
#     <p><input name="password" type="password"></p>
#     <p><button type="submit">Sign In</button></p>
#     </form>'''
 

# @app.route('/signin', methods=['POST'])
# def signin():
#     if request.form['username']=='admin' and request.form['password']=='password':
#         return '<h3>Hello, admin!</h3>'
#     return '<h3>Bad username or password.</h3>'
 

@app.route('/user/<phone>', methods=['GET'])
def getUserMessage(phone):
    
    sql = '''select * from admin where mobile_phone = '%s' ''' %(phone)
    w = baselib.baselib()
    datares = w.GetBitradeSqlAll(sql)
    
    if datares == None:
        return '查询结果为空'
    w.conn.commit()
    w.cursor.close
    w.conn.close
    # jsonData = []
    # data={}
    # user_id = ','.join(str(i) for i in user_id)
    # data ["wm_id"] = wm_id
    # jsonData.append(data)
    # logging.info(jsonData)
    return json.dumps(datares)

@app.route('/changecoinnicewallet/<phone>', methods=['GET'])
def updateCoinniceWallet(phone):
    
    sql = '''update member_wallet set balance = balance + '50000' where member_id in (select id from member where mobile_phone = '%s') ''' %(phone)
    u = baselib.baselib()
    datares = u.updateCoinBitrade(sql)
    # if datares == None:
    #     return '查询结果为空'    
    u.conn.commit()         
    u.cursor.close
    u.conn.close
        # jsonData = []
        # data={}
        # user_id = ','.join(str(i) for i in user_id)
        # data ["wm_id"] = wm_id
        # jsonData.append(data)
        # logging.info(jsonData)
    return json.dumps(datares)



@app.route('/changewallet/<phone>', methods=['GET'])
def updateWallet(phone):
    
    sql = '''update member_wallet set balance = balance + '50000' where member_id in (select id from member where mobile_phone = '%s') ''' %(phone)
    u = baselib.baselib()
    datares = u.updateBitrade(sql)
    # if datares == None:
    #     return '查询结果为空'    
    u.conn.commit()         
    u.cursor.close
    u.conn.close
        # jsonData = []
        # data={}
        # user_id = ','.join(str(i) for i in user_id)
        # data ["wm_id"] = wm_id
        # jsonData.append(data)
        # logging.info(jsonData)
    return json.dumps(datares)

@app.route('/changecoinphone/<phone>', methods=['GET'])
def updateCoinPhone(phone):

    t = kebitool.kebitool()
    u = baselib.baselib()
#    w = baselib.baselibtrade()    
    changePhone = t.createPhone() 
    sql1 = ''' update member set mobile_phone = '%s' where mobile_phone = '%s' ''' %(changePhone,phone)
    res1 = u.updateCoinBitrade(sql1)         

    change_phone = '+86|'+ changePhone
    phone_change = '+86|'+ phone 
    sql2 = ''' update trade$platform_user set mobile = '%s' where mobile = '%s' ''' %(change_phone,phone_change)
    res2 = u.update_coin_trade(sql2)
    u.conn.commit()
    u.conn1.commit()         
    u.cursor.close
    u.conn.close
    u.conn1.close
    return change_phone

@app.route('/changephone/<phone>', methods=['GET'])
def updatePhone(phone):

    t = kebitool.kebitool()
    u = baselib.baselib()
#    w = baselib.baselibtrade()    
    changePhone = t.createPhone() 
    sql1 = ''' update member set mobile_phone = '%s' where mobile_phone = '%s' ''' %(changePhone,phone)
    res1 = u.updateBitrade(sql1)         

    change_phone = '+86|'+ changePhone
    phone_change = '+86|'+ phone 
    sql2 = ''' update trade$platform_user set mobile = '%s' where mobile = '%s' ''' %(change_phone,phone_change)
    res2 = u.update_trade(sql2)
    u.conn.commit()
    u.conn1.commit()         
    u.cursor.close
    u.conn.close
    u.conn1.close
    return change_phone

if __name__ == '__main__':
    app.run(host='192.168.10.46',port=8088,debug=True)
 

