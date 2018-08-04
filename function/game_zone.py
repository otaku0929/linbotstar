# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:46:41 2018

@author: 宇星
"""

import random
import json
import datetime, pytz

import function.star_talk
_star_talk = function.star_talk.start_talk()

import function.sql
_sql = function.sql.Sql()

import function.photo_zone
_photos = function.photo_zone.photo_zone()

import function.config_setting
_config = function.config_setting.config_setting()


def main():
    _game = game_zone()

    
    #content = _game.get_user_profile('Ud0414e339e9c242b19a2dd22dd1f6189','藍宇星冷男星','http://dl.profile.line-cdn.net/0hLkoyPlmqE0RSAD5u3DZsE25FHSklLhUMKmILJiUCRHQrZVRGPWZfJnJTTHJ5ZQESaWNUJn5VTics')
    #content = _game.get_user_profile('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨')
    content = _game.card_pk('U9f2c61013256dfe556d70192388e4c7c','藍宇星冷男星','惠')
    print(content)

    
class game_zone(object):
    
    def __init__(self):
        self.class_name = 'game_zone'

    def time(self):
        return str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        
    def r18(self):

        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        d = random.randint(1,6)
    
        rlist = [a,b,c,d]
        seen = set()      
        y = [n for n in rlist if n not in seen and not seen.add(n)]
    
        c2=""
        c3=""
        n=0
    
        for i in rlist:
            if rlist.count(int(i)) == 2:
               c2 = i
            if rlist.count(int(i)) == 3:
               c3 = i
    
        if len(y) == 4:
            content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n沒點, 再擲一次吧!!!'.format(a,b,c,d)
            return content
        if len(y) ==1:
          if y[0]==6:
             content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n豹子通殺!!!!'.format(a,b,c,d)
             return content
          else:
             content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n點數為:水哦 {}一色'.format(a,b,c,d,y[0])
             return content
        if len(y)==3:
          for i2 in rlist:
              if i2 != c2:
                  n = n+i2
              else:
                  pass
          if n ==3:
              content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n{}點 逼機 >"<" '.format(a,b,c,d,n)
              return content
          else:
              content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n{}點'.format(a,b,c,d,n)
              return content
        if len(y)==2 and c3 !='':
            content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n沒點, 再擲一次吧!!!'.format(a,b,c,d,n)
            return content
        if len(y)==2:         
           content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n水哦  十八!!!!'.format(a,b,c,d,n)
           return content
    
    def get_atk_userlist(self):
        
        sql_command = "select user_name from user_config where update='%s'"%self.time()
        config = _sql.select(sql_command)
        i = 1
        for obj in config:
            name = 'NO.%s %s'%(i,str(obj)[2:len(obj)-4])
            if i==1:
                content = name
            else:
                content = '%s\n%s'%(content,name)
            i=i+1
        return '今日可對戰玩家：\n%s'%content

       
    def get_user_profile(self,uid,user_name):
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        if 'profile_time' in config_json['profile']:
            if config_json['profile']['profile_time'] == time:
                A = config_json['profile']
                content = '%s\n屬性:%s\n生命值(hp):%s\n魔法力(mp):%s\n攻擊力(atk):%s\n防禦力(def):%s \n幸運值(lucky):%s\n每日運勢:%s\n-----------\n%s'%(A['user_name'],A['WIZ'],A['hp'],A['mp'],A['ATK'],A['DEF'],A['lucky'],A['today'],A['keywords'])
                return content        
        else:
            content = {'link':'%s 今天還沒有產生卡片哦，可以輸入 "今日卡片" 來產生哦!'%user_name}
            return content
    
    def card_pk(self,uid,user_name,pk_user):
        
        _card_game =  card_fight()
        
        sql_command = "select user_id from user_config where update='%s' and user_name='%s'"%(self.time(),pk_user)
        config = _sql.select(sql_command)
        if config == []:
            return '%s 沒有對戰卡片哦'%pk_user
        else:
            pk_id = str(config)[3:len(config)-5]
                       
        jsonA= json.loads(_sql.select_config(uid)[0][2])
        jsonB= json.loads(_sql.select_config(pk_id)[0][2])
        
        A = jsonA['profile']
        B = jsonB['profile']
        print(A,B)

        profile_A = '%s (%s) hp:%s mp:%s atk:%s def:%s lucky:%s'%(A['user_name'],A['WIZ'],A['hp'],A['mp'],A['ATK'],A['DEF'],A['lucky'])
        profile_B = '%s (%s) hp:%s mp:%s atk:%s def:%s lucky:%s'%(B['user_name'],B['WIZ'],B['hp'],B['mp'],B['ATK'],B['DEF'],B['lucky'])
        
        charA_HP = A['hp']
        charB_HP = B['hp']
        Wiz_value_list = _card_game.WizATK(A['WIZ'], B['WIZ'])
        A_Wiz_value = Wiz_value_list[0]
        B_Wiz_value = Wiz_value_list[1]
        atk_list = {'fight_status':{},'atk_winner':{},'atk_fin':{}}
        atk_round = 0
        
        while charA_HP >=0 or charB_HP >=0:
            #判定誰攻誰防, 以幸運值亂數高者為攻
            if random.randint(0,A['lucky'])>random.randint(0,B['lucky']):
                #print('A')
                A_ATK = _card_game.getATK(A['ATK'],A['lucky'],A_Wiz_value)
                B_DEF = _card_game.getDEF(B['DEF'],B['lucky'])
                ATK_value= A_ATK[1]-B_DEF[1]
                if ATK_value <=0:
                    ATK_value = 0
                new_HP = B['hp'] - ATK_value
                ATK_content = '%s 使用 %s (%s) 造成 %s %s 傷害(%s%s)'%(A['user_name'],A_ATK[2],A_ATK[1],B['user_name'],ATK_value,B_DEF[2],B_DEF[1])
                Status_content = '%s HP %s => %s'%(B['user_name'],B['hp'],new_HP)
                ATK_Status = '%s\n>>>%s'%(ATK_content,Status_content)
                #print(ATK_Status)
                if atk_list['fight_status'] == {}:
                    atk_list['fight_status'] = ATK_Status
                else:    
                    atk_list['fight_status'] = '%s\n%s'%(atk_list['fight_status'],ATK_Status)
                charA_HP = charA_HP
                charB_HP = new_HP
                if charA_HP<=0 or charB_HP<=0:
                    atk_list['atk_winner'] = A['user_name']
                    atk_list['atk_fin'] = '%s 戰勝了 %s'%(A['user_name'],B['user_name'])
                    break
                atk_round = atk_round+1
                if atk_round >31:
                    atk_list['atk_winner'] = '平手'
                    atk_list['atk_fin'] = '打累了~ %s %s 吃飯去啦'%(A['user_name'],B['user_name'])
                    break
            else:
                B_ATK = _card_game.getATK(B['ATK'],B['lucky'],B_Wiz_value)
                A_DEF = _card_game.getDEF(A['DEF'],A['lucky'])
                ATK_value= B_ATK[1]-A_DEF[1]
                if ATK_value <=0:
                    ATK_value = 0
                new_HP = A['hp'] - ATK_value
                ATK_content = '%s 使用 %s (%s) 造成 %s %s 傷害(%s%s)'%(B['user_name'],B_ATK[2],B_ATK[1],A['user_name'],ATK_value,A_DEF[2],A_DEF[1])
                Status_content = '%s HP %s => %s'%(A['user_name'],A['hp'],new_HP)
                ATK_Status = '%s\n>>>%s'%(ATK_content,Status_content)
                #print(ATK_Status)
                if atk_list['fight_status'] == {}:
                    atk_list['fight_status'] = ATK_Status
                else:    
                    atk_list['fight_status'] = '%s\n%s'%(atk_list['fight_status'],ATK_Status)
                #print(atk_list['fight_status'])
                charA_HP = new_HP
                charB_HP = charB_HP
                if charA_HP<=0 or charB_HP<=0:
                    atk_list['atk_winner'] = B['user_name']
                    atk_list['atk_fin'] = '%s 戰勝了 %s'%(B['user_name'],A['user_name'])
                    break
                atk_round = atk_round+1
                if atk_round >31:
                    atk_list['atk_winner'] = '平手'
                    atk_list['atk_fin'] = '打累了~ %s %s 吃飯去啦'%(A['user_name'],B['user_name'])
                    break
                
        return ('----------\n%s\n%s\n----------\n%s \n戰鬥紀錄**********\n%s'%(profile_A,profile_B,atk_list['atk_fin'],atk_list['fight_status']))
        
                
    def user_profile(self,uid,user_name,pictureUrl):
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        #time = '2018-07-21'
        config = _sql.select_config(uid)
        
        if config == []:
            _config.create_config(uid,user_name)
            config = _sql.select_config(uid)
        
        config_json = json.loads(config[0][2])
               
        if 'profile_time' in config_json['profile']:
            if config_json['profile']['profile_time'] == time:
                content = {'link':'%s 今天已經產生過了，一天只能玩一次哦'%user_name}
                return content
            else:

                message = self.profile_game_content(uid,user_name)   
                
                new_json = {'profile':
                    {'profile_time':time,
                     'user_name':message[0],
                     'hp':message[1],
                     'mp':message[2],
                     'lucky':message[3],
                     'today':message[4],
                     'keywords':message[5],
                     'WIZ':message[6],
                     'ATK':message[7],
                     'DEF':message[8],
                     'today_value':message[9]
                     }
                }
                config_json['profile'] = new_json['profile']
                config = json.dumps(config_json)
                _sql.update_config(uid,user_name,config) 
                
                content = _photos.user_daily_photo(uid,message,pictureUrl)
                
                return (content)
#                return self.profile_game_content(uid,user_name)               
        else:
            message= self.profile_game_content(uid,user_name)
            
            new_json = {'profile':
                {'profile_time':time,
                 'user_name':message[0],
                 'hp':message[1],
                 'mp':message[2],
                 'lucky':message[3],
                 'today':message[4],
                 'keywords':message[5],
                 'WIZ':message[6],
                 'ATK':message[7],
                 'DEF':message[8],
                 'today_value':message[9]
                 }
            }
            config_json['profile'].update(new_json)
            config = json.dumps(config_json)
            _sql.update_config(uid,user_name,config)         
            
            content = _photos.user_daily_photo(uid,message,pictureUrl)
            
            return (content)

    def profile_game_content(self,uid,user_name):
        
        
        WIZ = random.choice(['光','闇','金','木','水','火','土','雷','冰','風','聖','邪','日','月','星','毒','魂','萌','混','魅'])

        hp_all = random.randint(100,10000)
        hp = random.randint(0,hp_all)
        mp_all = random.randint(100,10000)
        mp = random.randint(0,mp_all)
        lucky = random.randint(1,1000)
        ATK = int(random.randint(1,hp_all)*(lucky/100))
        if ATK==0:
            ATK=1
        DEF = int(random.randint(1,mp_all)*(lucky/100))
        if DEF==0:
            DEF=1
        today_value = int((hp+mp+lucky)/1000)
        today=self.get_star(today_value)
        keywords = _star_talk.profile(user_name)
        content = [user_name,hp,mp,lucky,today,keywords,WIZ,ATK,DEF,today_value]
        return content
            
    def get_star(self,mum):

        val = int(mum+0.5)
        arr = ['☆','★','★☆','★☆','★★','★★☆','★★★','★★★☆','★★★★','★★★★☆','★★★★★']
        
        return arr[(val % 11)]
    

class card_fight(object):
    
    def __init__(self):
        self.class_name = 'card_fight' 

    def getATK(self,atk, lucky, wiz_value):
        
        atk0 = ['失手','滑倒了','忘了攻擊']
        atk1 = '普通攻擊'
        atk2 = '屬性攻擊'
        atk3 = '致命攻擊'
        atk9 = ['讓對手拉肚子攻擊']
        
        atk_key = random.randint(0,100)
        
        if random.randint(0,lucky) > 995:
            print(random.randint(0,lucky))
            atk_way = random.choice(atk9)
            atk_value = 999999999           
        else:
            if atk_key < 3:
                atk_way = random.choice(atk0)
                atk_value = 0
            elif atk_key >=3 and atk_key < 71:
                atk_way = atk1
                atk_value = random.randint(1,atk)
            elif atk_key >=71 and atk_key <91:
                atk_way = atk2
                atk_value = int(random.randint(1,atk)*wiz_value)
            elif atk_key >=91:
                atk_way = atk3
                atk_value = int(random.randint(1,atk)*lucky/10)

    
        return (atk,atk_value,atk_way)
    
    def getDEF(self,DEF, lucky):
        
        def0 = ['我閃我閃我閃閃閃','你看不到我','你打不到我','究極防禦','聖盾術']
        def1 = ['超級防禦','盾牆','冰牆']
        
        if int(lucky/10) == 0:
            def_key = 1
        else:
            def_key = random.randint(1,int(lucky/10))
        
        if def_key >= 80 and def_key<95:
            def_way = random.choice(def1)
            def_value = random.randint(int(DEF*0.8),DEF)*10
        elif def_key >= 95:
            def_way = random.choice(def0)
            def_value = random.randint(int(DEF*0.9),DEF)*def_key
        else:
            def_way = '防禦'
            def_value = random.randint(1,DEF)
        
        return (DEF,def_value,def_way)
    
    
    def WizATK(self,A_WIZ, B_WIZ):
        
        dict = {'混':{'聖':0.2,'光':0.2,'萌':0.5},
                '聖':{'邪':0.5,'毒':0.2,'萌':0.5},
                '邪':{'萌':0.5},
                '闇':{'聖':0.2,'萌':0.5},
                '光':{'闇':0.5,'萌':0.5},
                '金':{'木':0.5,'萌':0.5},
                '木':{'土':0.5,'萌':0.5},
                '水':{'火':0.5,'萌':0.5},
                '火':{'木':0.5,'冰':0.2,'萌':0.5},
                '土':{'水':0.5,'風':0.2,'萌':0.5},
                '雷':{'魅':0.8,'萌':0.5},
                '冰':{'魅':0.8,'萌':0.5},
                '風':{'魅':0.8,'萌':0.5},
                '日':{'萌':0.5},
                '月':{'萌':0.5},
                '星':{'萌':0.5},
                '毒':{'魅':0.8,'萌':0.5},
                '魂':{'魅':0.8,'萌':0.5},
                '魅':{'萌':0.2}
        }
        
        Wiz_list = dict[A_WIZ]
        #print(Wiz_list)
        if B_WIZ in Wiz_list:
            Wiz_ATK = Wiz_list[B_WIZ]
            return(1+Wiz_ATK,1-Wiz_ATK)
        else:
            return ([1,1])


if __name__ == '__main__':
    main()
