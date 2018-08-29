#!/usr/bin/python
# -*- coding:utf-8 -*-
from os import sys
sys.path.append("..")
reload(sys)
sys.setdefaultencoding('utf-8')
from kebi.lib import baselib
from kebi.tool import kebitool
import datetime
import json

class insertDate(object):
    def __init__(self):
        self.baselib = baselib.baselib()
        self.kebitool = kebitool.kebitool()

    def __del__(self):
        pass

    def register_Date(self,index):
        phone_data = []
        delta = datetime.timedelta(days=3)
        now = datetime.datetime.now()
        #增加日期
        n_days = delta + now   
        for i in range(index): 
            username = 'userlgq' + str(index)          
            phone = self.kebitool.createPhone()

            phone_data.append(phone)
            phone_change = '+86|'+ phone
            sql = '''select mobile_phone from member where mobile_phone = '%s' ''' %(phone)
            res = self.baselib.querybitrade(sql)
            if res:            
                sql1 = '''insert into member(      
                    appeal_success_times,appeal_times,certified_business_status,first_level,
                    jy_password,country,country_no,login_count,member_level,mobile_phone,
                    password,publish_advertise,real_name_status,
                    registration_time,salt,second_level,sign_in_ability,status,third_level,
                    token_expire_time,transaction_status,transactions,username,local)  
                    values(0,0,0,0,'9b7a825f48f84b60326ad60b690910f1','中国','+86',0,0,'%s','0d76d25e8dcff4179f6c714013b30f47',
                    1,0,now(),3836313232383333393138343331323338,0,1,0,0,
                    '%s','1','0','%s','中国') ''' %(phone,n_days,username)
                sql1 = sql1.decode("utf8")
                res1 = self.baselib.updateBitrade(sql1)  
            else:
                return ('手机号已存在')    
            sql2 = '''insert into user(      
                    username,mobile,password,rand_code,paypassword,paypassSetting,
                    logins,addtime,updatetime,status,bind_userid,invite_code,
                    idcard_verify_status,advert_evaluate,advert_trust,trade_nums,
                    google_status,fee_free,is_start_paypwd)  
                    values('%s','%s','6c80ef95db4fe2d48c248d2299a3657e',8345,'e10adc3949ba59abbe56e057f20f883e',1,1,now(),now(),1,0,
                    'DBB9346A',0,0.00000000,0,0,0,0,0) ''' %(username,phone_change)
            sql2 = sql2.decode("utf8")
            res2 = self.baselib.update_trade(sql2)

        return json.dumps(phone_data)

    def register_Date1(self,index):
        phone_data = []
        phonenumber = {}
        delta = datetime.timedelta(days=3)
        now = datetime.datetime.now()
        #增加日期 
        n_days = delta + now   
        for i in range(index): 
            username = 'userlgq' + str(i)          
            phone = self.kebitool.createPhone()
            userPhone = 'userphone' + str(i)
            phonenumber[userPhone]= phone 
            phone_data.append(phone)
            phone_change = '+86|'+ phone
            sql = '''select mobile_phone from member where mobile_phone = '%s' ''' %(phone)
            res = self.baselib.querybitrade(sql)
            if res:            
                sql1 = '''insert into member(      
                    appeal_success_times,appeal_times,certified_business_status,first_level,
                    jy_password,country,country_no,login_count,member_level,mobile_phone,
                    password,publish_advertise,real_name_status,
                    registration_time,salt,second_level,sign_in_ability,status,third_level,
                    token_expire_time,transaction_status,transactions,username,local)  
                    values(0,0,0,0,'9b7a825f48f84b60326ad60b690910f1','中国','+86',0,0,'%s','0d76d25e8dcff4179f6c714013b30f47',
                    1,0,now(),3836313232383333393138343331323338,0,1,0,0,
                    '%s','1','0','%s','中国') ''' %(phone,n_days,username)
                sql1 = sql1.decode("utf8")
                res1 = self.baselib.updateBitrade(sql1)  
            else:
                return ('手机号已存在')    
            sql2 = '''insert into user(      
                    username,mobile,password,rand_code,paypassword,paypassSetting,
                    logins,addtime,updatetime,status,bind_userid,invite_code,
                    idcard_verify_status,advert_evaluate,advert_trust,trade_nums,
                    google_status,fee_free,is_start_paypwd)  
                    values('%s','%s','6c80ef95db4fe2d48c248d2299a3657e',8345,'e10adc3949ba59abbe56e057f20f883e',1,1,now(),now(),1,0,
                    'DBB9346A',0,0.00000000,0,0,0,0,0) ''' %(username,phone_change)
            sql2 = sql2.decode("utf8")
            res2 = self.baselib.update_trade(sql2)
#        print json.dumps(phonenumber)
#        return json.dumps(phone_data)
        return json.dumps(phonenumber)
if __name__ == '__main__':
    w = insertDate()
    res = w. register_Date1(2)        
    print res             
