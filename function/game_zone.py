# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:46:41 2018

@author: 宇星
"""

import re
import random
import json
import datetime, pytz

from collections import Counter

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
    _game_card = card_fight()
    content = _game_card.fight_win_item(1)
    
    #content = _game_card.goldbox('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨')
    content = _game.user_profile('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨','http://dl.profile.line-cdn.net/0hLkoyPlmqE0RSAD5u3DZsE25FHSklLhUMKmILJiUCRHQrZVRGPWZfJnJTTHJ5ZQESaWNUJn5VTics')
    #content = _game.get_user_profile('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨')
    #content = _game.get_starcoin('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨')
    #content = _game.card_pk('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨','阿貴')
    #content = _game_card.fix_eq('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨','eq1')
    #content = _game_card.get_user_items('U9f2c61013256dfe556d70192388e4c7c','藍宇星冷男星')
    #content = _game_card.get_user_equ('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨')
    #content = _game_card.buy_item('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨','阿嬤之杖')
    #content = _game_card.sell_item('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨','面紙')    
    #content = _game_card.use_eq('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨','eq2')
    #content = _game_card.unuse_eq('U9f2c61013256dfe556d70192388e4c7c','藍宇星✨victor✨','eq1')
    #content = _game_card.use_items('U9f2c61013256dfe556d70192388e4c7c','藍宇星冷男星','黃金寶箱')
    #content = _game_card.armor_store_detail()
    #content = _game_card.lucky_time('U59e79d6500b2f9cad5ed780c1a1f9f8a','謙²')
    #content = _game_card.get_item_detail('爛木頭')
    #content = _game.to_starcoin('藍宇星✨victor✨',50)
    #content = _game.get_atk_userlist()
    #content = _game_card.armor_store_detail()
#    messages = '攻擊=@陳小馬（EK)'
#    if re.match('^(對戰|攻擊)= ?@?(.+)',messages):
#        uid = 'U9f2c61013256dfe556d70192388e4c7c'
#        pkid = re.match('^(對戰|攻擊)= ?@?(.+)',messages).group(2).strip()
#        #print(pkid)
#        content = _game.card_pk(uid,'藍宇星冷男星',pkid)
        #print (content)
    #print(content[1])
    #if content[1] == '':
    #    print(content[0],'NONE')
    #else:
    #    print(content[0],content[1])
    #print(content.count())
    print(content)
    
class game_zone(object):
    
    def __init__(self):
        self.class_name = 'game_zone'
        self.sline = '------------'
        #self._game_card = card_fight()

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
       
    def to_starcoin(self,user,num):
            
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]

        sql_command = "select * from user_config where update='%s' and user_name='%s'"%(self.time(),user)
        config = _sql.select(sql_command)
        #print(config[0][0])
        if config == []:
            return '沒有 %s 使用者哦'%user
        else:      
        #config = _sql.select_config(uid)
            uid = config[0][0]
            config_json = json.loads(config[0][2])
            profile = config_json['profile']
            profile['starcoin'] = profile['starcoin']+int(num)
            profile['starcoin_time'] = time
#            
            new_startcoin = profile['starcoin']
            config = json.dumps(config_json)
            
            command = "update user_config set config = '%s', update = '%s' where user_id = '%s'" % (config,self.time(),uid)
            _sql.run(command)
            #new_startcoin = 5
            
            return '配發給 %s 小星星代幣 %s ，現有代幣共有:%s'%(user,num,new_startcoin)        
        
       
    def get_starcoin(self,uid,user_name):
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
        
        if 'starcoin' in profile:
            if profile['starcoin_time'] == 0 or profile['starcoin_time'] != time:
                profile['starcoin'] = profile['starcoin']+5
                profile['starcoin_time'] = time
            else:
                return '今日已領取過代幣'
        else:
            _config.delete_config(uid)
            return '請重新產生卡片，再領取一次代幣'
        
        new_startcoin = profile['starcoin']
        config = json.dumps(config_json)
        _sql.update_config(uid,user_name,config)
        
        return '%s領取小星星代幣成功 目前代幣共有:%s'%(user_name,new_startcoin)
                
    
    def get_atk_userlist(self):
        
        sql_command = "select user_name from user_config where update='%s'"%self.time()
        config = _sql.select(sql_command)
        if config == []:
            return '今日還沒有人產生卡牌'
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
                if 'equipment' in config_json['profile']:
                    A = config_json['profile']  
                    profile1 = '力量(STR):%s  智力(INT):%s\n速度(AGI):%s 敏捷(DEX):%s\n體值(VIT):%s 幸運(LUK):%s'\
                    %(A['STR'],A['INT'],A['VIT'],A['AGI'],A['DEX'],A['lucky'])
                    profile2 = '生命值(HP):%s\n魔法力(MP):%s\n攻擊力(ATK):%s\n防禦力(DEF):%s'\
                    %(A['hp'],A['mp'],A['ATK'],A['DEF'])
                    
                    if A['arms'] =='':
                        arms_item = A['arms']
                        arms_ed = ''
                    else:
                        for obj in A['arms']:
                            arms_item = obj
                            arms_index = A['arms'][obj][0]
                            arms_ed = '({}%)'.format(A['equ_list'][arms_index][obj]['ed'])

                    if A['armor'] =='':
                        armor_item = A['armor']
                        armor_ed = ''
                    else:
                        for obj in A['armor']:
                            armor_item = obj
                            armor_index = A['armor'][obj][0]
                            armor_ed = '({}%)'.format(A['equ_list'][armor_index][obj]['ed'])
                            
                    equipment_content = '武器:{} {}\n防具:{} {}\n道具欄:{}\n道具欄:{}'\
                    .format(arms_item,arms_ed,armor_item,armor_ed,A['item1'],A['item2'])
                    content = '%s\n\n屬性:%s\n每日運勢:%s\n小星星代幣:%s\n%s\n%s\n\n%s\n\n%s\n%s\n%s'\
                    %(A['user_name'],A['WIZ'],A['today'],A['starcoin'],self.sline,profile1,profile2,equipment_content,self.sline,A['keywords'])
                    return content
                else:
                    A = config_json['profile']  
                    profile1 = '力量(STR):%s 智力(INT):%s\n速度(AGI):%s 敏捷(DEX):%s\n體值(VIT):%s 幸運(LUK):%s'\
                    %('_','_','_','_','_',A['lucky'])
                    profile2 = '生命值(HP):%s\n魔法力(MP):%s\n攻擊力(ATK):%s\n防禦力(DEF):%s'\
                    %(A['hp'],A['mp'],A['ATK'],A['DEF'])
                    equipment_content = '武器:%s\n防具:%s\n道具欄:%s\n道具欄:%s'\
                    %('_','_','_','_')
                    content = '%s\n\n屬性:%s\n每日運勢:%s\n小星星代幣:%s\n%s\n%s\n\n%s\n\n%s\n%s\n%s'\
                    %(A['user_name'],A['WIZ'],A['today'],'_',self.sline,profile1,profile2,equipment_content,self.sline,A['keywords'])
                    return content                  
            else:
                #content = {'link':'%s 今天還沒有產生卡片哦，可以輸入 "今日卡片" 來產生哦!'%user_name}
                content = '%s 今天還沒有產生卡片哦，可以輸入 "今日卡片" 來產生哦!'%user_name
                return content                
        else:
            #content = {'link':'%s 今天還沒有產生卡片哦，可以輸入 "今日卡片" 來產生哦!'%user_name}
            content = '%s 今天還沒有產生卡片哦，可以輸入 "今日卡片" 來產生哦!'%user_name
            return content
        
    
    def card_pk(self,uid,user_name,pk_user):
        
        _card_game =  card_fight()
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        
        sql_command = "select * from user_config where update='%s' and user_id='%s'"%(time,uid)
        a_config = _sql.select(sql_command)
        #print(a_config)
        if a_config == []:
            return ('%s 沒有對戰卡片哦'%user_name,'')    
        
        sql_command = "select * from user_config where update='%s' and user_name='%s'"%(time,pk_user)
        b_config = _sql.select(sql_command)
        #print(b_config)
        if b_config == []:
            return ('%s 沒有對戰卡片哦'%pk_user,'')
        
        config_A = a_config[0][2]    
        config_B = b_config[0][2]
        
        jsonA= json.loads(config_A)
        jsonB= json.loads(config_B)
        
        A = jsonA['profile']
        B = jsonB['profile']
        #print(A,B)        
        
        #取得角色裝備
        if A['arms'] == '':
            charA_arms = ''
        else:
            for obj in A['arms']:
                charA_arms = obj
                index = A['arms'][obj][0]
                ed = A['equ_list'][index][obj]['ed']
                new_ed = ed-1
                A['equ_list'][index][obj]['ed'] = new_ed
                if new_ed == 0:
                    jsonA['profile']['arms']=''
                    del jsonA['profile']['equ_list'][index]                   
            
        if A['armor'] == '':
            charA_armor = ''
        else:
            for obj in A['armor']:
                charA_armor = obj
                index = A['armor'][obj][0]
                ed = A['equ_list'][index][obj]['ed']
                new_ed = ed-1
                A['equ_list'][index][obj]['ed'] = new_ed
                if new_ed == 0:
                    A['armor']=''
                    del A['equ_list'][index]

        if charA_arms =='' and charA_armor =='':
            weap_check = 0
        else:
            weap_check = 1
        
        if B['arms'] == '':
            charB_arms = ''
        else:
            for obj in B['arms']:
                charB_arms = obj
                
        if B['armor'] == '':
            charB_armor = ''
        else:
            for obj in B['armor']:
                charB_armor = obj
                
        
        
        profile_A = '%s (%s) hp:%s mp:%s atk:%s def:%s lucky:%s\n武器:%s 防具:%s'%(A['user_name'],A['WIZ'],A['hp'],A['mp'],A['ATK'],A['DEF'],A['lucky'],charA_arms,charA_armor)
        profile_B = '%s (%s) hp:%s mp:%s atk:%s def:%s lucky:%s\n武器:%s 防具:%s'%(B['user_name'],B['WIZ'],B['hp'],B['mp'],B['ATK'],B['DEF'],B['lucky'],charB_arms,charB_armor)
        
        charA_HP = A['hp']
        charB_HP = B['hp']
        charA_MP = A['mp']
        charB_MP = B['mp']
        
        Wiz_value_list = _card_game.WizATK(A['WIZ'], B['WIZ'])
        A_Wiz_value = Wiz_value_list[0]
        B_Wiz_value = Wiz_value_list[1]
        atk_list = {'fight_status':{},'atk_winner':{},'atk_fin':{}}
        atk_round = 0
        winitem_content = ''
        
        while charA_HP >=0 or charB_HP >=0:
            #判定誰攻誰防, 以幸運值亂數高者為攻
            A_ATK_KEY=random.randint(0,100)+int(random.randint(0,A['DEX'])/10)
            B_ATK_KEY=random.randint(0,100)+int(random.randint(0,B['DEX'])/10)
       
            if len(A['user_name'])>8:              
                A_Name = '%s..'%(A['user_name'][0:7])
            else:
                A_Name = A['user_name']
            
            if len(B['user_name'])>8:
                B_Name = '%s..'%(B['user_name'][0:7])
            else:
                B_Name = B['user_name']
                
            #print('回合:%s'%atk_round,A_ATK_KEY,B_ATK_KEY)
            if A_ATK_KEY>B_ATK_KEY:
                #print('A')
                A_ATK = _card_game.getATK(A['ATK'],A['lucky'],A_Wiz_value)
                B_DEF = _card_game.getDEF(B['DEF'],B['lucky'])
                mp_atk = 0
                if charA_MP >0:
                    mp_time = random.randint(1,100)
                    if mp_time >= 85:
                        mp_atk = random.randint(0,charA_MP)
                ATK_value= A_ATK[1]+mp_atk-B_DEF[1]
                if ATK_value <=0:
                    ATK_value = 0
                new_HP = charB_HP - ATK_value
                ATK_content = '%s 使用 %s (%s) 造成 %s %s 傷害 (%s 防禦 %s)'%(A_Name,A_ATK[2],A_ATK[1],B_Name,ATK_value,B_DEF[2],B_DEF[1])
                Status_content = '%s HP %s => %s'%(B['user_name'],charB_HP,new_HP)
                ATK_Status = '%s\n___%s'%(ATK_content,Status_content)
                #print(ATK_Status)
                if atk_list['fight_status'] == {}:
                    atk_list['fight_status'] = ATK_Status
                else:    
                    atk_list['fight_status'] = '%s\n%s'%(atk_list['fight_status'],ATK_Status)
                charA_HP = charA_HP
                charB_HP = new_HP
                charA_MP = charA_MP-mp_atk
                charB_MP = charB_MP
                if charA_HP<=0 or charB_HP<=0:
                    atk_list['atk_winner'] = A['user_name']
                    atk_list['atk_fin'] = '%s 戰勝了 %s'%(A['user_name'],B['user_name'])
                    win_item = _card_game.fight_win_item(weap_check)
                    #print(win_item)
                    if win_item[0] == 'other':
                        equ_list = A['equipment']
                        if equ_list == {}:
                            equ_list = []
                        equ_list.append(win_item[1])
                        A['equipment'] = equ_list
                        winitem_content = win_item[1]
                    if win_item[0] == 'coin':
                        A['starcoin'] = A['starcoin']+win_item[1]
                        winitem_content = '%s 代幣'%(win_item[1])
                    break
                atk_round = atk_round+1
                if atk_round >16:
                    atk_list['atk_winner'] = '平手'
                    atk_list['atk_fin'] = '打累了~ %s %s 吃飯去啦'%(A['user_name'],B['user_name'])
                    break
            else:
                B_ATK = _card_game.getATK(B['ATK'],B['lucky'],B_Wiz_value)
                A_DEF = _card_game.getDEF(A['DEF'],A['lucky'])
                mp_atk = 0
                if charB_MP >=0:
                    mp_time = random.randint(1,100)
                    if mp_time >= 85:
                        mp_atk = random.randint(0,charB_MP)
                ATK_value= B_ATK[1]+mp_atk-A_DEF[1]
                if ATK_value <=0:
                    ATK_value = 0
                new_HP = charA_HP - ATK_value
                ATK_content = '%s 使用 %s (%s) 造成 %s %s 傷害 (%s 防禦 %s)'%(B_Name,B_ATK[2],B_ATK[1],A_Name,ATK_value,A_DEF[2],A_DEF[1])
                Status_content = '%s HP %s => %s'%(A['user_name'],charA_HP,new_HP)
                ATK_Status = '%s\n>>>%s'%(ATK_content,Status_content)
                #print(ATK_Status)
                if atk_list['fight_status'] == {}:
                    atk_list['fight_status'] = ATK_Status                 
                else:    
                    atk_list['fight_status'] = '%s\n%s'%(atk_list['fight_status'],ATK_Status)
                #print(atk_list['fight_status'])
                charA_HP = new_HP
                charB_HP = charB_HP
                charA_MP = charA_MP
                charB_MP = charB_MP-mp_atk             
                if charA_HP<=0 or charB_HP<=0:
                    atk_list['atk_winner'] = B['user_name']
                    atk_list['atk_fin'] = '%s 戰勝了 %s'%(B['user_name'],A['user_name'])
                    win_item=''
                    break
                atk_round = atk_round+1
                if atk_round >16:
                    atk_list['atk_winner'] = '平手'
                    atk_list['atk_fin'] = self.get_peace(A['user_name'],B['user_name'])
                    break

        #將耐久度寫入DB
        config = json.dumps(jsonA)
        _sql.update_config(uid,user_name,config)
        #print(jsonA)
                   
        #return ('----------\n%s\n%s\n----------\n%s\n獲得戰利品:%s\n----------'%(profile_A,profile_B,atk_list['atk_fin'],win_item),'戰鬥紀錄>>\n\n%s'%atk_list['fight_status'])
        return ('%s\n獲得戰利品:%s'%(atk_list['atk_fin'],winitem_content),'----------\n%s\n%s\n----------\n戰鬥紀錄>>\n\n%s'%(profile_A,profile_B,atk_list['fight_status']))
 
    
    def get_peace(self,a_name, b_name):
        
        peace = [
                '打累了~ %s %s 吃飯去啦'%(a_name, b_name),
                '不打了不打了，%s走喝一杯去'%b_name,
                '%s %s 打累~蹲下來休息了~'%(a_name, b_name),
                '突然想到~我還有事要忙，%s 等我回來再打'%b_name,
                '%s這次就饒了你~下次見到我一定打死你'%b_name,
                '唷~想不到你很強嘛~別打了~來加一下LINE吧'
                ]
        
        return random.choice(peace)
    
    def re_user_profile(self,uid,user_name):
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        message = self.profile_game_content(uid,user_name)  
        p = config_json['profile']
        
        p['profile_time']=time
        p['user_name']=message[0]
        p['hp']=message[1]
        p['mp']=message[2]
        p['lucky']=message[3]
        p['today']=message[4]
        p['keywords']=message[5]
        p['WIZ']=message[6]
        p['ATK']=message[7]
        p['DEF']=message[8]
        p['today_value']=message[9]
        p['STR']=message[10]
        p['VIT']=message[11]
        p['INT']=message[12]
        p['AGI']=message[13]
        p['DEX']=message[14]
        
        #print(config)
        
        config = json.dumps(config_json)
        _sql.update_config(uid,user_name,config) 
                    
        content = self.get_user_profile(uid,user_name)
        
        return (content)
                
    def user_profile(self,uid,user_name,pictureUrl):
        
        _game_card =  card_fight()
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        #time = '2018-07-21'
        config = _sql.select_config(uid)
        
        if config == []:
            _config.create_config(uid,user_name)
            config = _sql.select_config(uid)
        
        config_json = json.loads(config[0][2])
               
        if 'profile_time' in config_json['profile']:
            if config_json['profile']['profile_time'] != time:
                content = '%s 今天已經產生過了，一天只產生一次哦'%user_name
                return ('0',content)
            else:
                message = self.profile_game_content(uid,user_name)  
                p = config_json['profile']
                
                if 'equipment' in  p:
                    
                    if p['arms'] == '':
                        arms_values = 0
                    else:
                        for obj in p['arms']:
                            arms_values = _game_card.item_detail(obj)['value']

                    if p['armor'] == '':
                        armor_values = 0
                    else:
                        for obj in p['armor']:
                            armor_values = _game_card.item_detail(obj)['value']
                    
                    p['profile_time']=time
                    p['user_name']=message[0]
                    p['hp']=message[1]
                    p['mp']=message[2]
                    p['lucky']=message[3]
                    p['today']=message[4]
                    p['keywords']=message[5]
                    p['WIZ']=message[6]
                    p['ATK']=message[7]+arms_values
                    p['DEF']=message[8]+armor_values
                    p['today_value']=message[9]
                    p['STR']=message[10]
                    p['VIT']=message[11]
                    p['INT']=message[12]
                    p['AGI']=message[13]
                    p['DEX']=message[14]
                    
                    config = json.dumps(config_json)
                    _sql.update_config(uid,user_name,config) 
                    
                    content = _photos.user_daily_photo(uid,message,pictureUrl)
                    
                    return (content)
                  
                else:
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
                         'today_value':message[9],
                         'STR':message[10],
                         'VIT':message[11],
                         'INT':message[12],
                         'AGI':message[13],
                         'DEX':message[14],
                         'arms':'',
                         'armor':'',
                         'item1':'',
                         'item2':'',
                         'equipment':{},
                         'equ_list':{},
                         'starcoin':0,
                         'starcoin_time':None
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
                 'today_value':message[9],
                 'STR':message[10],
                 'VIT':message[11],
                 'INT':message[12],
                 'AGI':message[13],
                 'DEX':message[14],
                 'arms':'',
                 'armor':'',
                 'item1':'',
                 'item2':'',
                 'equipment':{},
                 'equ_list':{},
                 'starcoin':0,
                 'starcoin_time':None
                 }
            }
            config_json['profile'] = new_json['profile']
            config = json.dumps(config_json)
            _sql.update_config(uid,user_name,config)         
            
            content = _photos.user_daily_photo(uid,message,pictureUrl)
            
            return (content)

    def profile_game_content(self,uid,user_name):
        
        
        WIZ = random.choice(['光','闇','金','木','水','火','土','雷','冰','風','聖','邪','日','月','星','毒','魂','萌','混','魅'])
        
        ##STR 力量 VIT 體值 INT 智力 AGI 敏捷 DEX 命中 LUK 幸運值
        STR = random.randint(1,1000)
        VIT = random.randint(1,1000)
        INT = random.randint(1,1000)
        AGI = random.randint(1,1000)
        DEX = random.randint(1,1000)
        LUK = random.randint(1,1000)
        LV = random.randint(1,99)
        ATK_LV = random.randint(1,99)
        DEF_LV = random.randint(1,99)
    
        hp = VIT*5+random.randint(LV*5,5000)
        mp = INT*5+random.randint(LV*5,5000)

        ATK = STR*5+INT*2+int(AGI*2.5)+int(DEX*1.5)+random.randint(0,ATK_LV*100)
        DEF = VIT*5+STR*2+int(DEX*2.5)+int(AGI*1.5)+random.randint(0,DEF_LV*100)       
             
        today_value = int((hp+mp+LUK)/1000)
        today=self.get_star(today_value)
        keywords = _star_talk.profile(user_name)
        content = [user_name,hp,mp,LUK,today,keywords,WIZ,ATK,DEF,today_value,STR,VIT,INT,AGI,DEX]
        return content
            
    def get_star(self,mum):

        val = int(mum+0.5)
        arr = ['☆','★','★☆','★☆','★★','★★☆','★★★','★★★☆','★★★★','★★★★☆','★★★★★']
        
        return arr[(val % 11)]
      

class card_fight(object):
    
    def __init__(self):
        self.class_name = 'card_fight'
        self.game = game_zone()
        self.sline = '------------'

    def getATK(self,atk, lucky, wiz_value):
        
        atk0 = ['失手','滑倒了','忘了攻擊','zzzzz','被沉默了','吐口水','傻笑','哇哈哈哈哈','肚子痛先大便',
                '0分考卷','佛系功擊','吃到半隻小強','共嗚~kero~kero~kero','假裝喝醉了裝死','一起來藍藍路~藍藍路',
                '大眼瞪小眼','張大鼻孔','偽裝的假五星卡']
        atk1 = ['拿棒棒糖攻擊','丟石頭','戳一下','丟樸克牌','丟RAM攻擊','咬一口','丟榴槤',
                '飛吻','五層復合金炒菜鍋','爆炸佛跳牆','獅子挽歌','甩巴掌','彈鼻屎','掃把亂掃','滴蠟燭',
                '自拍照片','打呼','惡魔棒式訓練','丟麥當勞漢堡','冰的啦','小孩不睡覺','魔貫光殺砲',
                '乖寶寶睡拳','界王拳','無上飛彈冰淇淋','野豬衝擊鐵頭功','箱神~~~~~','要你命三千',
                '豪大大雞排','奪命連環扣','嬌喘','丫宅的心聲','哇沙米沙瓦','盲人腳底按摩','烤箱裡拼命加水',
                '丟生日蛋糕','巴蕊','踩腳指','拉頭髮','丫姑親一咧','拔鼻毛','500磅鐵槌攻擊','射橡皮筋','彈額頭',
                '信用卡帳單','十字愛心極光炮','揮舞著耐久度1的釣竿','魯小小','抓奶龍抓手','放飛的汽球','仙人指路',
                '阿魯巴','3.5吋軟碟飛標','限量1000排1001的無奈','我有女朋友','進擊的裸奔巨人','丟品客的空罐子',
                '銳利的紙片','廢紙堆的釘書針','燃燒的薑餅人','黑魔導的誘惑','霍霍霍霍霍~~家拳法','亢龍有悔',
                '珍珠奶茶不要奶','先王御賜尚方寶劍','來一罐丫比吧','餵食含笑半步顛','深夜的貓叫春','喵喵肉球拳','野球拳',
                '新鮮的毒蘋果','畫了地圖的棉被','吃不完的羊乳片','三叔~~~~~叔叔叔叔叔','餵綺夢吃龍蝦','送你一枝番丫火',
                '提摩必需死','草叢倫的旋風斬','天下掉下來的烏屎','射出紙飛機','龍抓手','抽血500CC','沒有糖漿的可樂機',
                '閉店前進來的客人','捷運車廂裡的老鼠','流星蝴蝶劍','點燃的水鴛鴦','剝皮辣椒','丟芭樂，是真的芭樂',
                '冥醫的根管治療','雷恩的七星刀','倫家吃不完','一隻雨傘','灑石灰','拜請天兵天將','丟進曼陀珠的可樂',
                '音浪不晃','中國古拳法','櫻木花道式灌籃','最後一塊頂級燒肉','假日飛刀手','大力鷹爪功','黑虎掏心',
                '白鶴亮翅','馬雅人弓箭手戰術','流浪的紅舞鞋','修羅旋風拳','凍僵的手','武松打貓拳','感冒病毒',
                '花痴大蘿蔔','累積十年的膽結石','來人，請公子吃餅','6呎日光燈管','羞恥play','空氣砲','靴貓劍法',
                '工業用電風扇','肥皂泡泡槍','聲波糖果','狼牙風風拳','操氣彈','風刃','火球術','青春修煉手冊','丟水球',
                '瓦斯桶地雷','血戰十式','做古長拳','放個屁臭死你','金太郎迴旋斧','海帶拳','人肉手裏劍','金坷拉','捶背券',
                '拋繡球','七月半的末班車','雙層大麥克','卑鄙的藤木','永澤的洋蔥頭','一起來歡歡','二哈攻擊','松鼠空手道',
                '鑽石星塵拳','帥氣的飛機頭','KTV的麥克風','阿里固~阿里固','暑假的最後一天','媚娘歌舞秀','叫我女王',
                '惡夢製造機','娘家滴G精','小女孩的火柴','洞洞波','菊丸火箭砲','無線深水炸彈','熊抱','潑墨水','黑虎偷心',
                '人體手裡劍','六刀圓舞曲','人妖手刀','假裝不甘心過肩摔','大雨大雨一直下','橡膠JET槍','芭樂票','丫呆的旋風鼻涕',
                '踩腳趾'
                ]
        atk2 = ['強力攻擊','破壞拳','迴旋踢','關門放狗','伸長吧~~拳頭','奧客精神','RAP碎碎唸','恐龍攻擊',
                '百裂拳','天帝之眼','紅蓮爆炎刃','丟大便','天翔龍閃','唸經','竹筍炒肉絲','宅男的右手','氣圓斬',
                '殺豬刀','降龍十八掌','還我漂漂拳','加滕金手指','化妝化一半','魔貫光殺砲','丟出科南','濃濃的男人味',
                '動感光波','冰火五重天','瘋狂購物','天外飛仙','市場大媽的逆襲','神仙採葡萄','時代的眼淚','飛龍在天',
                '十萬伏特','怒火燒盡九重天','恰~恰~~~爆橘拳','蕃茄蛋炒飯不要蕃茄','北斗百裂拳','友為吃不完的大餅',
                '夜來巴掌聲','烈炎紅唇','無敵風火輪','拂拂拂拂拂拂…機','無敵整蠱箱','把你變個大字','少林十八銅人','千年殺',
                'LV100初心者的普攻','恨天高飛踢','烏索布的長鼻子','丟出壞掉的解碼器','純情少男的玫瑰花','高梁酒豬肉香腸',
                '小李飛刀他爸','雙持的烤玉米','屁股向後平沙落雁式','香腸攤的金骰子','金貝貝的奶瓶','妹妹背的洋娃娃',
                '喂~博愛座讓讓','黑暗料理','保夾的超強抓力','發出好人卡','昇龍餃子拳','每隔五分的鬧鐘','小雞吃米拳',
                '火車上的拍肩掌','胖小孩的雙下巴','飛天鹹豬手','蓋亞能量炮','Tmama衝擊波','超大衝天炮','傳說中的肥螳螂拳',
                '小狗快攻','一錠官銀','一斤砒霜','保特瓶飛彈','阿彌陀丸！附身合體！','老闆娘鐵拳','神所傳授的拳法',
                '凸額頭','濃密的毛髮','二代炸彈嘴','胖龍出海','KITTY逗貓棒','旋轉砲台','夢裡打拳擊','邱彼特之箭',
                '放屁地瓜','降蟲十八掌','天橋底下說書嘴','秘密資料摧毀槍','自動挨打瓦斯','魔封波','暗黑死亡彈','殘像拳',
                '人妖打排球','小雨飛腿','SM皮鞭打擊','暴風神射''F4流星雨','火風暴','虎姑婆來囉','摩登源屎人',
                'GM封帳號','浸水桶','鄉民的正義之嘴','夏美迴旋踢','對朋友熱情的一顆心','KEROKERO全壘打','奕劍術','炎陽奇功',
                'GOGORO向前衝','憤怒地普通拳','戰車大翻轉','忘心波衝擊','油燈上的老鼠','克林奶粉罐','氣象亂報',
                '三鹿毒奶','更年期翻臉術','連續喜帖炸彈','少年A讓位','魔鬼椒大餐','祖嬤跟你問聲好','學長的晚點名',
                '大牛比較懶','天舞寶輪','銀河星爆','鳳凰幻魔拳','大蒜項鍊','黃金十字架','胖丁之歌','空虛寂寞覺得冷','燒炭攻擊',
                '波洞球','用臉滾鍵盤','噴射吧~馬桶的逆襲','丟圖釘','高根鞋蠍式撩陰腿','飛射吧向日葵的種子','鼻屎幻想大砲',
                '假裝可樂的紅酒','空明拳','召喚。李奧那多皮卡丘','妮妮兔兔暴力拳','五毒排咪掌']
        atk3 = ['龜派氣功波','超級飛踢','三刀流~鬼斬','三寶上路','卍解','霸王龍之吻','昇龍拳','奪命剪刀腳',
                '人妖拳法','召喚苦力帕','飛天蟑螂','超級凍結冰箭','火龍的碎牙','天輪‧循環之劍','色誘術-女女術',
                '猴子偷桃','超濃古龍水','整形前的照片','佛山無影腳','亂開E-MAIL','驗孕棒的二條線','起床氣',
                '改不完的設計稿','胖虎演唱會門票','壓歲錢我幫你保管','聽司馬中原談中元','查水錶','三輪車上的老太太',
                '超重行李箱','旺才的最後一口氣','姦夫淫婦劍','郎情妾意劍','Keroro嘴砲','推倒快完成的骨牌',
                '連續開會12小時','眼角的魚尾紋','焰之球','天上飛來的靴子','Tamama嫉妒玉','巧克力男孩到你家','安妮的呼喚'
                '亞美蝶催眠粉','中華傲訣','羿射九日','芙蓉金針','葵花點穴手','三吋不爛之舌','洲際導彈腿','降乩。三太子附體',
                '毛利蘭的角','雷動九天','小星星給我錢','進化退化放射光線槍','沾鼻屎的一陽指','六脈神劍','愛的教鞭',
                '一拳爆螢幕','石化口水','超高離子噴射蛋糕','SS能源彈','女王的高根鞋','究極光裂術','召喚術。肥肥',
                '路西法之矛','假裝喝醉擋酒','射後不理','惡婆婆的面色','井中月','超級西南氣流','翻多羅拳法','天降流陣','流水制空圈',
                '雙刀火雞','抱大腿','月初就吃土','499吃到飽','光陰似劍','課金大法','吃貨吞食大法','殺豬的高音','章魚哥的豎笛演奏會',
                '親密無間大亂揍','卡到陰','昇龍餃子拳','閣樓裡的Girl','糖果雨','龍捲風殺球','山竹風暴','鼻屎炸彈','DDOS攻擊',
                '宴會辦桌踢擊套餐','小屁孩拆卸術','伸長吧大傑的頭髮','雙手互搏','化骨綿掌','閃電之種','佛山無影腳']
        atk4 = ['致命一擊','必殺一擊','元氣彈','跪鍵盤密術','三檔 骨氣球','九九重陽功','唱歌攻擊','召喚殺很大',
                '鬼氣九刀流','加班加到死','等五年還沒洗好澡','丫宅的怨念','媽媽的咆哮','色誘術-逆後宮之術',
                '順手拿的折凳','只剩一頁的死亡筆記本','海底自摸十三么','卸妝攻擊','路邊撿到的雷神槌','鐵杵磨成鏽花針',
                '飛吧神鳥鳳凰','Looooong龍拳','爛尾專案','邪王炎殺黑龍波','庖丁解牛功','召喚青眼白龍','老師誘導電波機',
                '自爆','把你變成巧克力','摩亞。啟示錄億分之一','認真毆打拳','老漢便當車','香蕉切片器','斷網拔電源',
                '擲出三星S6','阿姆斯特朗砲','GM偷偷Nerf術','氪金流-大撒幣','豔美魔夜不眠鬼斬','賈伯斯的怨念','石榴姐之吻',
                '解不完的每日']
        atk9 = ['讓對手拉肚子攻擊','放屁臭死了對手','召喚了神龍，進行攻擊']
        
        atk_key = random.randint(0,100)
        
        if random.randint(0,lucky) > 996:
            #print(random.randint(0,lucky))
            atk_way = random.choice(atk9)
            atk_value = 999999999           
        else:
            if atk_key < 3:
                atk_way = random.choice(atk0)
                atk_value = 0
            elif atk_key >=3 and atk_key < 51:
                atk_way = random.choice(atk1)
                #rounad_ATK = int(random.randint(1,int(atk*0.4)))
                #atk_value = int(random.randint(1,int(atk*0.4))*1.5)
                atk_value = int(random.randint(1,int(atk*0.4)))
            elif atk_key >=51 and atk_key <81:
                atk_way = random.choice(atk2)
                atk_value = int(random.randint(int(atk*0.3),int(atk*0.7))*wiz_value)
            elif atk_key >=81 and atk_key <96:
                atk_way = random.choice(atk3)
                atk_value = int(random.randint(int(atk*0.6),int(atk*0.9))*wiz_value)
            elif atk_key >=96:
                atk_way = random.choice(atk4)
                atk_value = int(random.randint(int(atk*0.8),atk)*lucky/10)


    
        return (atk,atk_value,atk_way)
    
    def getDEF(self,DEF, lucky):
        
        def0 = ['扮鬼臉嚇人','盾檔','太極一式','講笑話','岩壁','灑豆子趕人','格檔','招架','我是香菇',
                '吃成胖子','變身綿花糖','丟臭豆腐','愛的抱抱','倒沙拉油','鍋蓋','舞空術飛走','模仿猩猩','臭臭襪',
                '騎豬快跑','伸出美腿','搖籃曲','泡泡鏡像','單眼拍照','啤酒乾一杯','丟圖釘在地上','來小星星抽一張吧',
                '吃冰休息吧','魔幻甜甜圈','在椅子上黏口香糖','縮不了的小腹','這不是肯徳雞','掀榻榻米','淚眼汪汪',
                '搔癢','撒嬌','戰吼','巨人之鎧','你褲子破洞了','又富檻了','今天萌萌的','闇影之舞','酸檸檬餵食',
                '減肥的怨念','熱水放好囉','1+1等於?','一哭二鬧三上悠亞','你知不知道我爸是誰','外拍都下雨',
                '愛肝一罐20元','給你蠻牛','國王的新衣','給你呼呼','吃鮭魚卵隱身','閉眼假裝沒人','丟出金田一',
                '跳肚皮舞','土下跪','此路不通','翻開可愛巧虎島','甜甜圈束縛','丟出癢癢草','躲在牆角取暖',
                '拉繩子跘倒敵人','從龜仙人那偷來的殼','看櫻花好美哦','那裡有美女','帥氣的微笑','幫敵人戴上老花眼鏡',
                '假的樂透中獎彩券','拿出忘在冰箱很久的蛋糕','爸爸的暖肚子','找你一堆零錢','無盡的紅燈',
                '內線開60','春假大塞車','APP無法下載','誤點的火車','霧霾','只剩衛生紙滾筒的廁所',
                '變身小熊維尼~唱只有為妳','麥當勞歡樂送','合歡山上的洋芋片','壞掉的GPS','大舌頭唸饒口令',
                '沒有玉米的玉米濃湯','不然你打我啊','跳進來又跳出去','署長的和平之槍','秋本麗子的泳裝照','打扮成木村倒頭哉',
                '小星星的美女圖片庫','志玲姐姐的飛吻','猛男的胸肌','吃葉綠素補腦?','綺夢找你吃飯','九姑娘的擁抱',
                '超強LED車頭燈','便秘的痛苦','剩1元的存款薄','貼在牆上的股票','沒有蜜蜂的蜂窩','檳榔攤的結冰水',
                '掉地上的冰淇淋','面試官是前前女友','空的紅包袋','說好不打臉的','香噴噴的桶仔雞','躱進垃圾筒',
                '爺爺泡的茶','圓圓的圓圓的大餅臉','高裝檢','丫土伯的斗笠','綁在娃娃椅吃飯','泥娃娃軍團','車停站一下',
                '西瓜太郎的兜檔布','唐寅詩集','噹噹噹噹噹','掉色的千元鈔','路痴眼裡的地圖','畫地自陷',
                '小狗汪汪叫','遲頓光線','三隻雨傘標','一個人看電影的寂寞','圓豬滾球','滾動的摩天輪','多爾滾',
                '帶上西瓜皮','此地無銀二佰伍','殺蟲劑','天蠶結繭','十八摸','陰森購物台','爛命一條','女孩的紅鞋',
                '桃太郎丸子','縮小燈','變身相撲力士','烏鴨嘴的詛咒','愛X無限大','佛祖給你加持','床榻下的四賤客',
                '小小兵合唱團','鐵骨乳液','安全保護袋','說謊的鏡子','烏賊車噴射','連續啦叭聲','反擊屏障','秘術。相親術',
                '下班時的雷陣雨','大叔的愛','唐詩三百首','蜜桃成熟時','K房大爆炸','大麥克買1送1','哈比書套',
                '康安的姐姐','送你高崗屋','蟹丫金的金庫','一起學貓叫','睜一隻眼閉一隻眼','嗨~Baby','觀落陰',
                '來塊烤肉吧','POKE FACE','短爆截擊','鴨子聽雷','李組長眉頭一皺','小YG成人尿布','流著口水叫丫姐',
                '印度大甩餅','墨西哥辣椒彈','四分五裂緊急逃出','詛咒。爛卡術','還我外星人','偽裝的ATP行控中心',
                '萬國驚天掌','沾衣十八跌','美伽子刑警的擁抱'
                ]
        def1 = ['硬氣功','分身防禦','閃避','丟香蕉讓對方滑倒','拿CRT螢幕擋住','用滑鼠綁住敵人','呼叫館長',
                '丟枕頭給敵人','你有freestyle嗎','閃現','拿美食餵養','召喚龍騎士','丟煙霧蛋','空間移動',
                '請你吃苦瓜','烏索普啊~~啊~~','百花繚亂','說八卦','手機放電','可愛五連拍','你聽過安麗嗎',
                '我是工程師','洗澡下線術','召喚豬隊友','我是單身狗','點穴','妖精之鎖','手牽手去郊遊','誘惑之鎧',
                '太陽拳','封印鐵壁','色誘術-男男術','藏蹤術','誠實豆沙包','喝光妳的SKII','舒心精油按摩','躺著也中槍',
                '請死神吃蘋果','丟出特惠宣傳單','露出屁股','乾坤大挪移','伺服器維修中','舖上稻草的大洞',
                '深情的眼眸','猜猜我是誰','吃下過期的春藥','各位觀眾5隻ACE','你媽在後面很火','異術:忘記WIFY密碼',
                '警察臨檢','想學撩妹話術嗎?','限量是殘酷的','冬天洗澡沒熱水','掏耳朵','超大蟑螂屋','因果轉業','佛光普照',
                '老子不畫啦!!','熱血~熱血~~超熱血!!!','我愛一條材','皇上的龍內褲','躺在捷運裝死','超厚電話簿',
                '夜王的撩妹話術','我是鐵頭功','阿榮的退伍令','沒錢買設備','隔壁在打架','深夜的福利','姐姐的安全帽',
                '穿上蜘蛛人的緊身衣','想不出梗的苦惱','合體七矮人','蛇魔女的飛眸','爸爸私藏的影片','從臉上拿下來的粉底',
                '友藏的俳句','強力磁鐵','單身狗的生日會','不誠實的魔鏡','蓬萊仙山歌舞秀','警察叔叔就是這個人',
                '流浪漢的紙箱','垃圾筒裡的可樂罐','出門踩到的狗屎','驗蛔蟲的貼紙','過期的大還丹','你看牆上有個洞',
                '飄走的游褲','鬼屋裡的F罩杯女鬼','拉下鐵門','蓋布袋','被遺忘的點餐單','石榴姐的自畫像','今天不賣酒',
                '金童玉女劍','一箱好人卡','裝上好自在飛翔','寒冰烈火掌','海棠的頭髮','賭神的照片','黒橘的無法登入',
                '存在感很低','打10分鐘200元','媽媽說九點要回家','Blue啦 Blue啦','windows update','換掉大門鑰匙',
                '冰清玉潔小香臍','纏人的愛心筆少女','你要賤身嗎?','媽媽的三層肉','只有熱風的冷氣機','甄嬛的手巾',
                '皇上該翻牌子了','買貴退差價','內馬爾滾','拓也哥的深吼嚨','風乾橘子皮','草泥馬吐口水','蘭花拂穴手',
                '蛤蟆功','慾女心經','好高明的內功','無盡的挖礦工人','山西布政的五千兩','楊秀珍的圈圈','召喚乞丐中的霸主',
                '豬一般的隊友','大笨鍾鐵絲網','澳洲大紅岩','巫力無效化','馬可波羅的大餅','打破的砂鍋','變身瘋狂假面',
                '帽子戲法','消失的頭髮','地中海反射鏡','超音波碎石機','烏雲蔽日','阿嬤的腳皮','槓上自摸詐糊','變身北港六尺四',
                '閃避披風','國際保育類動物噴霧','消災解厄貼紙','歐巴，卡雞馬~~','丫北的硬碟','能量吸收裝置','水遁術',
                '堆糞反擊','爆風格檔','電音三太子','衝擊之暈','尖刺盔甲','聖結界','大齡剩女的反擊','烏龜烏龜蹺',
                '哇卡摩多','酸民的極限舌頭','幫我買張點數卡吧','哥哥我還要','歐吉桑的驕傲','幻魔身法','護國神山','認真往返跳躍',
                '假日就暴雨','焦糖瑪奇朵','融化的小美冰淇淋','慾女心經','阿尼又掛掉了','七天鑑賞期','媽呀你上電視了',
                '星雲鎖鏈','幻朧魔皇拳','丟滿地的玩具','多多龍坐路中間','小姐一個人嗎?','禁。繩縛術','禁。現代版吞劍術',
                '與大自然融合','冰之世界','五感剝奪','撞豆腐','轉圈圈的哈姆太郎','屁股神盾術','開幽靈馬車逃跑','毛皮強化',
                '三輪花。封','騙人終點大作戰','橡膠脾酒肚','脫牙的螺絲','畫唬爛的政客','1111零點無收訊','黑白配男生女生配',
                '天罡北斗陣','滿桌的美味蟹堡','候選人的宣傳車','葵花點穴手','鑽石屁股'
                ]
        def2 = ['超級防禦','盾牆','冰牆','催眠術','變張3讓對方傻住','混元一氣功','拿鏡子給敵人','灑鈔票','隔壁老王',
                '瞬間移動','海市蜃樓','和睦相處','水遁．泡膜壁','穿上隱形斗篷','不滅金身','tea or coffe or me?','吸星大法',
                '秘室裡的屁味','鑽石鑽石亮晶晶','你看我的項鍊','纏在一起的耳機線','滿滿的香菜','恰吉的OVER MY BADY',
                '咬鳳梨的神豬','重播877次的周星馳','凌波微步','比邊緣人還沒存在感','化整為零大法','全身脫光光',
                '兩津勘吉的幹細胞','老闆正在看著你','縮陽入腹','八陣圖','娘子快看是牛魔王','氣鋼鬥衣','煉破反衝壁','屍體復活術',
                '絕對屏障','丫尼吉的霸王色霸氣','泰式按摩','化整為零大法','破精自絕大法','陪SERVER看日出','手塚區',
                '去死去死團加油','氪金霸王氣','必殺騙人喬-彗星鐵鎚','奇門五轉','碧海潮生曲','點你淫蕩穴']
        def9 = ['我閃我閃我閃閃閃','你看不到我','嘿嘿~你打不到我','究極防禦','聖盾術','小星星壞掉了','國防布']
        
        if int(lucky/10) == 0:
            def_key = 1
        else:
            def_key = random.randint(1,int(lucky/10))
        
        #print(def_key)
        
        if def_key >= 50 and def_key<81:
            def_way = random.choice(def1)
            def_value = int(random.randint(int(DEF*0.3),int(DEF*0.7)))       
        elif def_key >= 81 and def_key<95:
            def_way = random.choice(def2)
            def_value = int(random.randint(int(DEF*0.6),int(DEF*0.9)))
        elif def_key >= 95:
            def_way = random.choice(def9)
            def_value = int(random.randint(int(DEF*0.9),DEF)*5*def_key)
        else:
            def_way = random.choice(def0)
            #rounad_DEF = random.randint(1,DEF)
            def_value = int(random.randint(1,int(DEF*0.4)))
        
        return (DEF,def_value,def_way)
    
    
    def WizATK(self,A_WIZ, B_WIZ):
        
        dict = {'混':{'聖':1.2,'光':1.2,'萌':1.5},
                '聖':{'邪':1.5,'毒':1.2,'萌':0.5},
                '邪':{'混':1.5,'萌':0.5},
                '闇':{'聖':1.2,'萌':0.5},
                '光':{'闇':1.5,'萌':0.5},
                '金':{'木':1.5,'萌':0.5},
                '木':{'土':1.5,'萌':0.5},
                '水':{'火':1.5,'萌':0.5},
                '火':{'金':1.5,'冰':0.8,'萌':0.5},
                '土':{'水':1.5,'風':0.8,'萌':0.5},
                '雷':{'魅':1.8,'萌':0.5},
                '冰':{'魅':1.8,'萌':0.5},
                '風':{'魅':1.8,'萌':0.5},
                '日':{'月':1.5,'萌':0.5},
                '月':{'星':1.5,'萌':0.5},
                '星':{'日':1.5,'萌':0.5},
                '毒':{'魅':1.8,'萌':0.5},
                '魂':{'魅':1.8,'萌':0.5},
                '魅':{'萌':1.2},
                '萌':{}
        }
        
        Wiz_list = dict[A_WIZ]
        #print(Wiz_list)
        if B_WIZ in Wiz_list:
            Wiz_ATK = Wiz_list[B_WIZ]
            return(1+Wiz_ATK,1-Wiz_ATK)
        else:
            return ([1,1])

    def get_user_items(self,uid,user_name):
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
        
        if 'equipment' in profile:
             equ_list = profile['equipment']
             show_list = None
             if equ_list == {}:
                 return '%s 目前沒有任何道具'%user_name
             else:
                 c = Counter(equ_list)
                 for obj in c.keys():
                     if show_list == None:
                         show_list = '%s：%s'%(obj,c.get(obj))
                     else:
                         object_content = '%s：%s'%(obj,c.get(obj))
                         show_list = '%s\n%s'%(show_list,object_content)
                 return '%s 擁有的道具列表：\n%s\n%s'%(user_name,self.sline,show_list) 
        else:
            return '%s 目前沒有任何道具'%user_name
        
    def get_user_equ(self,uid,user_name):
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
        
        if 'equ_list' in profile:
             equ_list = profile['equ_list']
             show_list = None
             if equ_list == {}:
                 return '%s 目前沒有擁有任何裝備'%user_name
             else:
                 for _obj in profile['equ_list']:
                     _eq_obj = profile['equ_list'][_obj]
                     for obj in _eq_obj:
                         eq_obj = _eq_obj[obj]
                         name = obj
                         val = eq_obj['val']
                         ed = eq_obj['ed']
                         _used = eq_obj['used']
                         if _used > 0:
                             used = '(裝備中)'
                         else:
                             used = ''
                         if self.item_detail(name)['index'] == 'arms':
                             obj_content = '%s：%s %s\n攻擊力增加:%s  物品耐久度:%s'%(_obj,name,used,val,ed)
                         if self.item_detail(name)['index'] == 'armor':
                             obj_content = '%s：%s %s\n防禦力增加:%s  物品耐久度:%s'%(_obj,name,used,val,ed)                        
                         if show_list == None:
                             show_list = obj_content
                         else:
                             show_list = '%s\n__\n%s'%(show_list,obj_content)
                 return '%s 擁有的裝備列表：\n%s\n%s'%(user_name,self.sline,show_list)
        else:
            return '%s 目前沒有任何道具'%user_name
        
    def use_items(self,uid,user_name,del_item):

        #game = game_zone()
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
            return '尚未建立人物卡片及領取代幣'
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
        equ_list = profile['equipment']
#        a = '黃金寶箱'
#        equ_list.append(a)
#        print(equ_list)
        if del_item in equ_list:
            equ_list.remove(del_item)
            new_status = None
            item_detail = self.item_detail(del_item)
            #print(del_item)
            index = item_detail['index']
            if index == 'LUK':
                index = 'lucky'
            if index in profile:
                old_index_values = profile[index]
                new_index_values = 0
                if index in ['hp','mp']:
                    new_index_values = profile[index]+item_detail['value']
                    if new_index_values > 99999:
                        new_index_values = 99999
                if index in ['STR']:
                    new_index_values = profile[index]+item_detail['value']
                    profile['ATK']= profile['ATK']+int(item_detail['value']*5)
                    profile['DEF']= profile['DEF']+int(item_detail['value']*2)
                    if new_index_values > 9999:
                        new_index_values = 9999
                if index in ['INT']:
                    new_index_values = profile[index]+item_detail['value']
                    profile['mp']= profile['mp']+int(item_detail['value']*5)
                    profile['ATK']= profile['ATK']+int(item_detail['value']*2)
                    if new_index_values > 9999:
                        new_index_values = 9999
                if index in ['VIT']:
                    new_index_values = profile[index]+item_detail['value']
                    profile['hp']= profile['hp']+int(item_detail['value']*5)
                    profile['DEF']= profile['DEF']+int(item_detail['value']*5)
                    if new_index_values > 9999:
                        new_index_values = 9999
                if index in ['DEX']:
                    new_index_values = profile[index]+item_detail['value']
                    profile['DEF']= profile['DEF']+int(item_detail['value']*2.5)
                    profile['ATK']= profile['ATK']+int(item_detail['value']*1.5)
                    if new_index_values > 9999:
                        new_index_values = 9999
                if index in ['AGI']:
                    new_index_values = profile[index]+item_detail['value']
                    profile['ATK']= profile['ATK']+int(item_detail['value']*2.5)
                    profile['DEF']= profile['DEF']+int(item_detail['value']*1.5)
                    if new_index_values > 9999:
                        new_index_values = 9999
                if index in ['lucky']:
                    new_index_values = profile[index]+item_detail['value']
                    if new_index_values > 999:
                        new_index_values = 999 
                if index in ['ATK','DEF']:
                    new_index_values = profile[index]+item_detail['value']
                    if new_index_values >100000:
                        new_index_values = 100000
                profile[index] = new_index_values
                new_status = '%s => %s'% (old_index_values,profile[index])
                config = json.dumps(config_json)
                _sql.update_config(uid,user_name,config)
                return '%s 已使用 %s %s\n%s'%(user_name,del_item,item_detail['detail'],new_status)
            if del_item == '角色重置卡': 
                config = json.dumps(config_json)
                _sql.update_config(uid,user_name,config)
                return self.game.re_user_profile(uid,user_name)
            if del_item == '黃金寶箱':
                config = json.dumps(config_json)
                _sql.update_config(uid,user_name,config)
                return self.goldbox(uid,user_name)
        else:
            return '%s 的背包裡並沒有 %s 這件物品，請確認輸入物品名稱是否正確'%(user_name,del_item)       
        
    def lucky_time(self,uid,user_name):
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
            return '尚未建立人物卡片及領取代幣'
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
        
        if 'starcoin' not in profile:
            return '%s 請更新卡片並領取代幣後再進行尋寶功能'%user_name
        else:
            if profile['starcoin'] ==0:
                return '%s 已沒有代幣可以進行尋寶唷'%user_name
            else:
                equ_list = profile['equipment']
                if equ_list == {}:
                    equ_list = []
                #print(equ_list)
                items = None
                status = None
                               
                lucky_poin = random.randint(1,1000)
                if lucky_poin >=999:
                    res = '99'
                    get_item = self.lucky_time_items(user_name,res)
                    items = get_item[0]
                    status = get_item[1]
                    #print(items)
                    equ_list.append(items)
                    profile['equipment'] = equ_list
                    #result['99'] = result['99']+1
                elif lucky_poin >=300 and lucky_poin <550:
                    res = '1'
                    get_item = self.lucky_time_items(user_name,res)
                    items = get_item[0]
                    status = get_item[1]
                    #print(items)
                    equ_list.append(items)
                    profile['equipment'] = equ_list
                    #result['1'] = result['1']+1
                elif lucky_poin >=550 and lucky_poin <700:
                    res = '2'
                    get_item = self.lucky_time_items(user_name,res)
                    items = get_item[0]
                    status = get_item[1]
                    #print(items)
                    equ_list.append(items)
                    profile['equipment'] = equ_list
                    #result['2'] = result['2']+1
                elif lucky_poin >=700 and lucky_poin <750:
                    res = '3'
                    get_item = self.lucky_time_items(user_name,res)
                    items = get_item[0]
                    status = get_item[1]
                    #print(items)
                    equ_list.append(items)
                    profile['equipment'] = equ_list
                    #result['3'] = result['3']+1
                elif lucky_poin >=750 and lucky_poin <800:
                    res = '4'
                    get_item = self.lucky_time_items(user_name,res)
                    items = get_item[0]
                    status = get_item[1]
                    #print(items)
                    equ_list.append(items)
                    profile['equipment'] = equ_list
                    #result['4'] = result['4']+1
                elif lucky_poin >=800 and lucky_poin <830:
                    res = '5'
                    get_item = self.lucky_time_items(user_name,res)
                    items = get_item[0]
                    status = get_item[1]
                    #print(items)
                    equ_list.append(items)
                    profile['equipment'] = equ_list
                    #result['4'] = result['4']+1
                elif lucky_poin >=830 and lucky_poin <860:
                    res = '6'
                    get_item = self.lucky_time_items(user_name,res)
                    items = get_item[0]
                    status = get_item[1]
                    #print(items)
                    equ_list.append(items)
                    profile['equipment'] = equ_list
                    #result['4'] = result['4']+1
                else:
                    res = '0'
                    #result['0'] = result['0']+1
                    items = self.lucky_time_items(user_name,res)
                    status = items
                    #print(items)
                
                profile['starcoin']=profile['starcoin']-1
                new_coin = profile['starcoin']
                
                config = json.dumps(config_json)
                _sql.update_config(uid,user_name,config)
                
                return '%s \n%s\n%s\n%s\n剩餘小星星代幣:%s'%(user_name,self.sline,status,self.sline,new_coin)  
                
    def lucky_time_items(self,ser_name,res):
        
        dict = {
                '0':['銘謝惠顧','再接再勵，下一次會更好','唉呀~沒抽中','憑你也想抽中','離中獎，還差的遠呢?',
                     '我覺得你不行，下次再抽吧','挖了滿地的坑，但什麼都沒有','被漢堡神偷偷走了寶物',
                     '回到家時發現褲子破洞，寶物都掉光了','多扶奶奶過馬路，應該會中大獎',
                     '迷路找不到山洞只好回家了','出門遇到暴雨，回家休息','想打劫山賊反而被山賊打劫了',
                     '天氣太熱，偷跑去看電影','在村口遇見胖虎，哭著跑回家','被金光黨騙走了寶物',
                     '遇到苦力帕，道具全炸飛了','被困在冒險山洞裡，什麼也沒有找到','踩到香蕉皮滑倒，把得到的藥劑給壓爛了',
                     '在森林裡被歐吉追殺，什麼沒也沒找到','坑爹啊，這什麼爛地圖什麼也沒找到','再氪個十萬應該會抽到吧',
                     '醒醒吧，中獎對你來說太難了','被史萊姆吃了，跑魂重來吧'
                     ],
                '1':['紅色藥水','藍色藥水','攻擊增加藥水','防禦增加藥水'],
                '2':['紅色藥水','藍色藥水','橙色藥水','攻擊增加藥水','防禦增加藥水','地獄辣椒','白馬乎你夯','小魚乾',
                     '鼠兒果'],
                '3':['白色藥水','濃縮藍色藥水','攻擊增加藥水','防禦增加藥水','大瓶裝攻擊增加藥水','大瓶裝防禦增加藥水'],
                '4':['白色藥水','濃縮藍色藥水','大瓶裝攻擊增加藥水','大瓶裝防禦增加藥水','龜甲萬醬油','戰狼肉','鼠兒果'],
                '5':['綠色藥水','勇敢藥水','妖精餅乾','伊娃的祝福','活力藥水','無敵星星','龜甲萬醬油','戰狼肉','鼠兒果',
                     '疾走藥水','龍之珍珠','惡魔之血','伊娃的祝福','生命樹果實','無敵星星'],
                '6':['激進藥劑','堅韌藥劑','疾走藥水','龍之珍珠','惡魔之血','伊娃的祝福','生命樹果實','無敵星星'],
                '99':['角色重置卡']
                }
        
        dict_s = [
                '本來要放棄了，結果在路口跌倒撿到< %s >',
                '在探險的山洞中，找到了< %s >',
                '東挖挖、西找找，被你找到了< %s >',
                '皇天不負苦心人，在山洞口的狗屎堆中發現< %s >',
                '是尋寶大王，發現了< %s >',
                '打敗了史萊姆，獲得< %s >',
                '在森林裡的寶箱中，找到了< %s >',
                '偷跑去看電影，還在路邊撿到< %s >',
                '在海底地監打死蟹人，獲得< %s >',
                '在遠古洞穴打死骷髏弓箭手，獲得< %s >',
                '在海神島釣魚，釣到了< %s >',
                '在太魯閣號的廁所裡撿到< %s >',
                '在迷霧森林中，打開了寶箱，獲得< %s >',
                '跑到三仙台看日出，不小心撿到< %s >',
                '在仙古的遺跡中，發現了< %s >',
                '玩迷室逃脫時，在角落發現< %s >',
                '在龍之谷外圍殺死巨蠍，獲得了< %s >',
                '在遠古戰場打死了食死鬼，獲得了< %s >',
                '在妖精地監裡殺死黑暗妖精，獲得了< %s >',
                '在藏寶海灣在尋獲了< %s >',
                '在北鬥的荒古禁區中，尋獲了< %s >',
                '誤入神秘的三角洲，發現了< %s >',
                '在黃金古路裡，打死了神秘的猛獸，獲得了< %s >'
                ]

        getitem = random.choice(dict[res])
        if res !='0':
            return [getitem,random.choice(dict_s)%getitem]
        else:        
            return getitem
    
    def get_item_detail(self,val):
        
        try:        
            item_detail = self.item_detail(val)   
            
            _index = item_detail['index']
            _val = item_detail['value']
            _detail = item_detail['detail']
            _coin = item_detail['coin']
            if _coin <0:
                _recoin = '無法出售'
            else:
                _recoin = int(_coin/3)
                if _recoin == 0:
                    _recoin = 1
            
            if _index == 'arms':
                return ('%s\n類別:武器\n數值:增加攻擊力 %s 點\n販售: %s 代幣\n說明:%s'%(val,_val,_recoin,_detail))
            if _index == 'armor':
                return ('%s\n類別:防具\n數值:增加防禦力 %s 點\n販售: %s 代幣\n說明:%s'%(val,_val,_recoin,_detail))
            else:
                return ('%s\n類別:%s道具\n數值: %s 點\n販售: %s 代幣\n說明:%s'%(val,_index,_val,_recoin,_detail))
        except:
            return '查不到此物品的說明，請確認輸入是否正確'
    
    def buy_item(self,uid,user_name,item):
        try:
            item_detail = self.item_detail(item)
            item_index = item_detail['index']
            item_coin = item_detail['coin']
            item_value = item_detail['value']
            
            if item_coin < 0:
                return '%s 此道具無法購買'%item 
            
            config = _sql.select_config(uid)
            if config == []:
                _config.create_config(uid,user_name)
                return '尚未建立人物卡片及領取代幣'
            
            config = _sql.select_config(uid)
            config_json = json.loads(config[0][2])
            
            profile = config_json['profile']
                     
            user_coin = profile['starcoin']
            
            if item_coin > user_coin:
                return '角色代幣剩餘 %s 不夠，無法購買 %s(%s)'%(user_coin, item,item_coin)
            i=1
            while i<20:
                index = 'eq%s'%i
                if index in profile['equ_list']:
                    i=i+1
                    if i >21:
                        return '每個角色最多只能持有21件裝備'
                else:                 
                    if item_index in ['arms','armor']:         
                        new_coin = user_coin-item_coin
                        profile['starcoin'] = new_coin
                        new_equ = {index:{item:{'val':item_value,'ed':100,'used':0}}}
                        profile['equ_list'].update(new_equ)
                        
                        config = json.dumps(config_json)
                        _sql.update_config(uid,user_name,config)
                        #print(profile)
                        
                        return '%s 已獲得 %s，剩餘代幣 %s'%(user_name, item, new_coin)
                    else:
                        return '道具商店目前尚未開放，所以無法採購 %s'%item           
        except:
            return '查不到此物品的說明，請確認輸入是否正確'
        
    def sell_item(self,uid,user_name,item):
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
            return '尚未建立人物卡片及領取代幣'
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
        
        if re.match('eq(.+)',item):
            if item in profile['equ_list']:
                eq_json = profile['equ_list'][item]
                for obj in eq_json:
                    if eq_json[obj]['used'] == 1:
                        return '< %s:%s > 為使用中的裝備，無法販售'%(item,obj)
                    else:
                        sell_coin = int(self.item_detail(obj)['coin']/3)
                        old_coin = profile['starcoin']
                        new_coin = old_coin+sell_coin
                        profile['starcoin'] = new_coin
                        del profile['equ_list'][item]
                        config = json.dumps(config_json) 
                        _sql.update_config(uid,user_name,config)
                        return '%s 販售< %s > 獲得 %s 代幣，人物代幣 %s >> %s'%(user_name,obj,sell_coin,old_coin,new_coin)
            else:
                return '%s 裝備背包裡沒有代碼為< %s >的裝備'%(user_name,item)
        else:
            try:
                index = self.item_detail(item)['index']
            except:
                return '查不到此物品的說明，請確認輸入是否正確'
            
            if index in ['arms','armor']:
                return '< %s >為裝備，請使用裝備代碼販售'%item
            
            if item in profile['equipment']:            
                item_coin = self.item_detail(item)['coin']
                if item_coin == -1:
                    return '道具< %s >無法販售'%item
                else:
                    sell_coin = int(item_coin/3)
                    if sell_coin == 0:
                        sell_coin = 1
                    old_coin = profile['starcoin']
                    new_coin = old_coin+sell_coin
                    profile['starcoin'] = new_coin
                    profile['equipment'].remove(item)
                    config = json.dumps(config_json) 
                    _sql.update_config(uid,user_name,config)
                    return '%s 販售< %s > 獲得 %s 代幣，人物代幣 %s >> %s'%(user_name,item,sell_coin,old_coin,new_coin)
            else:
                return '%s 道具背包裡沒有< %s >這樣物品'%(user_name,item)
            
    def check_fix_eq(self,uid,user_name,item):
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
            return '尚未建立人物卡片及領取代幣'
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2]) 
        
        profile = config_json['profile']
        
        if re.match('eq(.+)',item):
            if item in profile['equ_list']:
                eq_json = profile['equ_list'][item]
                for obj in eq_json:
                   if eq_json[obj]['ed'] == 100:
                       return '%s 此物品耐久度為100%不用修復'%item
                   else:
                       _item = eq_json[obj]
                       val = _item['val']
                       red = _item['ed']
                       _fix_coin = int(val/1000)
                       _fix_rate = [5,4,3,2,1,0]
                       _fix_ed = _fix_rate[red%6]
                       fix_coin = _fix_ed*_fix_coin                       
                       return '修理< {} {} {} %> > 需要 {} 代幣'.format(item, obj,red,fix_coin)
            else:
                return '%s 裝備背包裡沒有代碼為 %s 的裝備'%(user_name,item)
        else:
            return '%s 此物品不是裝備無法進行修復'%item
        
    def fix_eq(self,uid,user_name,item):
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
            return '尚未建立人物卡片及領取代幣'
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2]) 
        
        profile = config_json['profile']
        
        if re.match('eq(.+)',item):
            if item in profile['equ_list']:
                eq_json = profile['equ_list'][item]
                for obj in eq_json:
                   if eq_json[obj]['ed'] == 100:
                       return '<{} >此物品耐久度為100%不用修復'.format(item)
                   else:
                       _item = eq_json[obj]
                       val = _item['val']
                       red = _item['ed']
                       _fix_coin = int(val/1000)
                       #_fix_rate = [5,4,3,2,1,0]
                       _fix_ed = 5-int(red/20) #_fix_rate[red%6]
                       fix_coin = _fix_ed*_fix_coin
                
                user_coin = profile['starcoin']
                if user_coin < fix_coin:
                    return '{} 剩餘 {} 代幣，不夠錢修理< {} {} {} %>  >需要 {} 代幣'.format(user_name, user_coin, item, obj,red,fix_coin)
                else:
                    new_coin = user_coin-fix_coin
                    profile['starcoin'] = new_coin
                    eq_json[obj]['ed'] = 100
                    config = json.dumps(config_json)                   
                    _sql.update_config(uid,user_name,config)
                    return '{} 修理< {} {} > 花費 {} 代幣\n裝備耐久度 {}% > {}%\n代幣 {} > {}'.format(user_name, item, obj ,fix_coin,red,'100',user_coin,new_coin)
            else:
                return '%s 裝備背包裡沒有代碼為 %s 的裝備'%(user_name,item)
        else:
            return '%s 此物品不是裝備無法進行修復'%item

    def use_eq(self,uid,user_name,item):
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
            return '尚未建立人物卡片及領取代幣'
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
        
        if item in profile['equ_list']:
            item_json = profile['equ_list'][item]
            for obj in item_json:
                item_name = obj
                if self.item_detail(item_name)['index'] == 'arms':
                    if profile['arms'] == '':
                        #裝備道具
                        profile['arms'] = {item_name:[item,item_name]}
                        profile['equ_list'][item][obj]['used']=1
                        ed = profile['equ_list'][item][obj]['ed']
                        #更新角色數值
                        item_value = profile['equ_list'][item][obj]['val']
                        old_atk= profile['ATK']
                        new_atk = profile['ATK']+item_value
                        profile['ATK']=new_atk
                        config = json.dumps(config_json) 
                        _sql.update_config(uid,user_name,config) 
                        return '{} 已裝備< {} >物品耐久度剩餘 {}%，角色ATK {} >> {}'.format(user_name,item_name,ed,old_atk,new_atk)
                    else:
                        #取得舊的裝備
                        old_eq = profile['arms']
                        for oeq in old_eq:
                            old_eq_index = old_eq[oeq][0]
                            old_eq_name = old_eq[oeq][1]
                            old_eq_value = profile['equ_list'][old_eq_index][old_eq_name]['val']
                            oed = profile['equ_list'][old_eq_index][old_eq_name]['ed']                       
                        #更新裝備
                        profile['equ_list'][old_eq_index][old_eq_name]['used']=0
                        profile['arms'] = {item_name:[item,item_name]}
                        profile['equ_list'][item][obj]['used']=1                
                        ed = profile['equ_list'][item][obj]['ed']
                        item_value = profile['equ_list'][item][obj]['val']
                        #更新角色數值
                        old_atk= profile['ATK']
                        new_atk = old_atk-old_eq_value+item_value
                        profile['ATK']=new_atk
                        config = json.dumps(config_json)                   
                        _sql.update_config(uid,user_name,config)
                        return '{} 已卸下{}({}) 換上裝備< {} >物品耐久度剩餘 {}%，角色ATK {} >> {}'.format(user_name,old_eq_name,oed,item_name,ed,old_atk,new_atk)
                if self.item_detail(item_name)['index'] == 'armor':
                     if profile['armor'] == '':
                         #裝備道具
                        profile['armor'] = {item_name:[item,item_name]}
                        profile['equ_list'][item][obj]['used']=1
                        ed = profile['equ_list'][item][obj]['ed']
                        #更新角色數值
                        item_value = profile['equ_list'][item][obj]['val']
                        old_def= profile['DEF']
                        new_def = profile['DEF']+item_value
                        profile['DEF']=new_def                        
                        config = json.dumps(config_json)                   
                        _sql.update_config(uid,user_name,config)
                        #print (profile)
                        return '{} 已裝備< {} >物品耐久度剩餘 {}%，角色DEF {} >> {}'.format(user_name,item_name,ed,old_def,new_def)
                     else:
                         #取得舊的裝備
                        old_eq = profile['armor']
                        for oeq in old_eq:
                            old_eq_index = old_eq[oeq][0]
                            old_eq_name = old_eq[oeq][1]
                            old_eq_value = profile['equ_list'][old_eq_index][old_eq_name]['val']
                            oed = profile['equ_list'][old_eq_index][old_eq_name]['ed']
                        #更新裝備    
                        profile['equ_list'][old_eq_index][old_eq_name]['used']=0
                        profile['armor'] = {item_name:[item,item_name]}
                        profile['equ_list'][item][obj]['used']=1                        
                        ed = profile['equ_list'][item][obj]['ed']
                        item_value = profile['equ_list'][item][obj]['val']
                        #更新角色數值
                        old_def= profile['DEF']
                        new_def = old_def-old_eq_value+item_value
                        profile['DEF']=new_def
                        config = json.dumps(config_json)                   
                        _sql.update_config(uid,user_name,config) 
                        return '{} 已卸下{}({}) 換上裝備< {} >物品耐久度剩餘 {}%，角色DEF {} >> {}'.format(user_name,old_eq_name,oed,item_name,ed,old_def,new_def)
        else:
            return '人物沒有擁有< %s >，請使用裝備代碼來裝備'%item
        
    def unuse_eq(self,uid,user_name,item):
        
        config = _sql.select_config(uid)
        if config == []:
            _config.create_config(uid,user_name)
            return '尚未建立人物卡片及領取代幣'
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']
      
        try:
            index = self.item_detail(item)['index']
        except:
            return '查詢不到< %s >，請重新輸入'%item
        
        
        if index == 'arms':
            if profile['arms'] == '':
                return '人物沒有裝備< %s >這項裝備'%item
            else:
                for obj in profile['arms']:
                    item_name = obj
                    item_index = profile['arms'][obj][0]
                    profile['arms'] = ''
                    profile['equ_list'][item_index][item_name]['used']=0
                    ed = profile['equ_list'][item_index][item_name]['ed']
                    item_val = profile['equ_list'][item_index][item_name]['val']
                    old_atk = profile['ATK']
                    new_atk = old_atk-item_val
                    profile['ATK'] = new_atk
                    config = json.dumps(config_json)
                    _sql.update_config(uid,user_name,config)
                    return '{} 已卸除< {} >物品耐久度剩餘 {}%，角色ATK {} >> {}'.format(user_name,item,ed,old_atk,new_atk)
        if index == 'armor':
            if profile['armor'] == '':
                return '人物沒有裝備< %s >這項裝備'%item 
            else:
                for obj in profile['armor']:
                    item_name = obj
                    item_index = profile['armor'][obj][0]
                    profile['armor'] = ''
                    profile['equ_list'][item_index][item_name]['used']=0
                    ed = profile['equ_list'][item_index][item_name]['ed']
                    item_val = profile['equ_list'][item_index][item_name]['val']
                    old_def = profile['DEF']
                    new_def = old_def-item_val
                    profile['DEF'] = new_def
                    config = json.dumps(config_json)
                    _sql.update_config(uid,user_name,config)
                    return '{} 已卸除< {} >物品耐久度剩餘 {}%，角色DEF {} >> {}'.format(user_name,item,ed,old_def,new_def)
        else:
            return '< %s >不是裝備，無法裝備'%item
        
        
    
    def arms_store_detail(self):
        
        list = ['初心者報紙','阿嬤之杖','哈比菜刀','暗影之刃','要你命三千','黑暗大法師牌組','折凳']

        store_title = '小星星卡牌武器商店'
        obj_content = ''
        for obj in list:
            obj_dict = self.item_detail(obj)
            name = obj         
            price = obj_dict['coin']
            re_price = int(obj_dict['coin']/3)
            val = obj_dict['value']
            detail = obj_dict['detail']
            content = '%s\n價格: %s 代幣\n回收: %s 代幣\n數值:增加攻擊力 %s 點\n說明:%s'%(name,price,re_price,val,detail)
            if obj_content == '':
                obj_content = content
            else:
                obj_content = '%s\n--\n%s'%(obj_content,content)
        
        res_content = '%s\n%s\n%s'%(store_title,self.sline,obj_content)
        
        return res_content  

    def armor_store_detail(self):
        
        list = ['紙箱盔甲','南瓜盾牌','骷髏骨甲','守護者之盾','媽媽的炒菜鍋','煉妖壺','巨人殖裝']

        store_title = '小星星卡牌防具商店'
        obj_content = ''
        for obj in list:
            obj_dict = self.item_detail(obj)
            name = obj         
            price = obj_dict['coin']
            re_price = int(obj_dict['coin']/3)
            val = obj_dict['value']
            detail = obj_dict['detail']
            content = '%s\n價格: %s 代幣\n回收: %s 代幣\n數值:增加防禦力 %s 點\n說明:%s'%(name,price,re_price,val,detail)
            if obj_content == '':
                obj_content = content
            else:
                obj_content = '%s\n--\n%s'%(obj_content,content)
        
        res_content = '%s\n%s\n%s'%(store_title,self.sline,obj_content)
        
        return res_content  
    
    def item_store_detail(self,val):
        
        dict = {
                '紅色藥水':{'id':'01','name':'紅藥水','coin':2},
                '橙色藥水':{'id':'02','name':'橙色藥水','coin':4},
                '白色藥水':{'id':'03','name':'白色藥水','coin':6},
                '藍色藥水':{'id':'04','name':'藍色藥水','coin':3},
                '濃縮藍色藥水':{'id':'05','name':'濃縮藍色藥水','coin':6}
                }
                
        return dict

    def item_detail(self,val):
        
        dict = {
                '紅色藥水':{'index':'hp','name':'紅色藥水','value':500,'detail':'增加生命值(HP)500點','coin':3},
                '橙色藥水':{'index':'hp','name':'橙色藥水','value':1000,'detail':'增加生命值(HP)1000點','coin':4},
                '白色藥水':{'index':'hp','name':'白色藥水','value':2000,'detail':'增加生命值(HP)2000點','coin':6},
                '小魚乾':{'index':'hp','name':'小魚乾','value':1500,'detail':'增加生命值(HP)1500點','coin':-1},
                '戰狼肉':{'index':'hp','name':'戰狼肉','value':2500,'detail':'增加生命值(HP)2500點','coin':-1},                
                '藍色藥水':{'index':'mp','name':'藍色藥水','value':1000,'detail':'增加魔力值(MP)1000點','coin':3},
                '濃縮藍色藥水':{'index':'mp','name':'濃縮藍色藥水','value':2000,'detail':'增加魔力值(MP)2000點','coin':-1},
                '鼠兒果':{'index':'mp','name':'鼠兒果','value':1500,'detail':'增加魔力值(MP)1500點','coin':6},
                '攻擊增加藥水':{'index':'ATK','name':'攻擊增加藥水','value':1000,'detail':'增加攻擊力(ATK)1000點','coin':6},
                '地獄辣椒':{'index':'ATK','name':'地獄辣椒','value':1500,'detail':'增加攻擊力(ATK)1500點','coin':-1},
                '大瓶裝攻擊增加藥水':{'index':'ATK','name':'大瓶裝攻擊增加藥水','value':2000,'detail':'增加攻擊力(ATK)2000點','coin':-1},
                '激進藥劑':{'index':'ATK','name':'激進藥劑','value':3000,'detail':'增加攻擊力(ATK)3000點','coin':-1},
                '防禦增加藥水':{'index':'DEF','name':'防禦增加藥水','value':1000,'detail':'增加防禦(DEF)1000點','coin':6},
                '白馬乎你夯':{'index':'DEF','name':'白馬乎你夯','value':1500,'detail':'增加防禦(DEF)1500點','coin':6},
                '龜甲萬醬油':{'index':'DEF','name':'龜甲萬醬油','value':2500,'detail':'增加防禦(DEF)1500點','coin':-1},
                '大瓶裝防禦增加藥水':{'index':'DEF','name':'大瓶裝防禦增加藥水','value':2000,'detail':'增加防禦(DEF)2000點','coin':-1},
                '堅韌藥劑':{'index':'DEF','name':'堅韌藥劑','value':3000,'detail':'增加防禦(DEF)3000點','coin':-1},
                '綠色藥水':{'index':'AGI','name':'綠色藥水','value':100,'detail':'增加速度(AGI)100點，可增加攻擊力及防禦力','coin':6},
                '勇敢藥水':{'index':'STR','name':'勇敢藥水','value':100,'detail':'增加力量(STR)100點，可增加攻擊力及防禦力','coin':6},
                '妖精餅乾':{'index':'DEX','name':'妖精餅乾','value':100,'detail':'增加敏捷(DEX)100點，可增加攻擊力及防禦力，額外影響出手機率。','coin':6},
                '慎重藥水':{'index':'INT','name':'慎重藥水','value':100,'detail':'增加智力(INT)100點，可增加MP及攻擊力','coin':6},
                '活力藥水':{'index':'VIT','name':'活力藥水','value':100,'detail':'增加體力(VIT)100點，可增加防禦力','coin':6},
                '幸運餅乾':{'index':'LUK','name':'幸運餅乾','value':100,'detail':'增加幸運(LUK)100點，額外影響絕招的施放機率','coin':4},
                '疾走藥水':{'index':'AGI','name':'疾走藥水','value':200,'detail':'增加速度(AGI)200點，可增加攻擊力及防禦力','coin':-1},
                '龍之珍珠':{'index':'STR','name':'龍之珍珠','value':200,'detail':'增加力量(STR)200點，可增加攻擊力及防禦力','coin':-1},
                '惡魔之血':{'index':'DEX','name':'惡魔之血','value':200,'detail':'增加敏捷(DEX)200點，可增加攻擊力及防禦力，額外影響出手機率。','coin':-1},
                '伊娃的祝福':{'index':'INT','name':'伊娃的祝福','value':200,'detail':'增加智力(INT)200點，可增加MP及攻擊力','coin':-1},
                '生命樹果實':{'index':'VIT','name':'生命樹果實','value':200,'detail':'增加體力(VIT)200點，可增加防禦力','coin':-1},
                '無敵星星':{'index':'LUK','name':'無敵星星','value':200,'detail':'增加幸運(LUK)200點，額外影響絕招的施放機率','coin':-1},
                '角色重置卡':{'index':'reset','name':'角色重置卡','value':0,'detail':'重置人物屬性，但是魔王還是變沙包呢? 爻杯吧','coin':200},        
                '--amrs--':(),
                '初心者報紙':{'index':'arms','name':'初心者報紙','value':1000,'coin':10,'detail':'蒐集了各家報紙捲成的報紙劍，非常的厚實，無聊時還能看看上面的新聞。'},
                '阿嬤之杖':{'index':'arms','name':'阿嬤之杖','value':2000,'coin':20,'detail':'魔法阿嬤留下來的法杖，上面還銘刻了許多奇妙的咒語，其中隱約寫著猴死囝仔夠又偷吃菜...'},
                '哈比菜刀':{'index':'arms','name':'哈比菜刀','value':3000,'coin':40,'detail':'哈比兔料理紅蘿蔔用的菜刀，只不過這種紅蘿蔔跟你想像中的不太一樣，似乎會說話...'},
                '暗影之刃':{'index':'arms','name':'暗影之刃','value':4000,'coin':60,'detail':'傳說中的暗殺者所持有的匕首，可以吸收周圍的暗影來強化你的武器，並轉化為暗影傷害。'},
                '要你命三千':{'index':'arms','name':'要你命三千','value':10000,'coin':200,'detail':'這可是達聞西嘔心瀝血之作，一共結合了十種致命的武器，每一種武器皆可獨當一面，可說是威力驚人的殺人利器。'},
                '黑暗大法師牌組':{'index':'arms','name':'黑暗大法師牌組','value':15000,'coin':400,'detail':'傳說當有人蒐集全被封印的黑暗大法師魔法卡，即可召喚出大魔神-艾克佐迪亞，完成終極必殺。'},
                '折凳':{'index':'arms','name':'折凳','value':17500,'coin':600,'detail':'七大武器之首，奧妙之處，就是可以藏在民宅之中，隨手可得，還可以坐著它來隱藏殺機，打完更可以坐下休息，就算被條子捉到也告不了你。'},
                '--armor--':{},
                '紙箱盔甲':{'index':'armor','name':'紙箱盔甲','value':1000,'coin':10,'detail':'雖然是用紙箱做成的盔甲，但仍有一定的防禦能力，而且天冷時還可以可以擋擋風，可是不要碰到水哦!'},
                '南瓜盾牌':{'index':'armor','name':'南瓜盾牌','value':2000,'coin':20,'detail':'用南瓜舞者的身體製成的盾牌，再拿個南瓜燈籠就可以出發要糖果了。'},
                '骷髏骨甲':{'index':'armor','name':'骷髏骨甲','value':3000,'coin':40,'detail':'用骷髏做成的盔甲，雖然有可怕，但防禦效果挺不錯的，不過要小心路邊的小黃小白和小黑。'},
                '守護者之盾':{'index':'armor','name':'守護者之盾','value':4000,'coin':60,'detail':'傳說中的英靈所持有的盾牌，可以吸收光的元素來強化防禦並阻擋黑暗'},
                '媽媽的炒菜鍋':{'index':'armor','name':'媽媽的炒菜鍋','value':10000,'coin':200,'detail':'這不止是一個炒菜鍋，放在頭上可以當頭盔，綁在胸前可以當盔甲，沒有武器時還能拿來敲人，而且還有媽媽的味道，可說是超全面性的裝備。'},
                '煉妖壺':{'index':'armor','name':'煉妖壺','value':15000,'coin':400,'detail':'上古十大神器之一，內部有著奇異之空間，空間之大似能將天地收納於內，除了可以將所有的攻擊吸收至煉妖壼內，相傳壼內似乎隱藏了一位妖精。'},
                '巨人殖裝':{'index':'armor','name':'巨人殖裝','value':17500,'coin':600,'detail':'被稱為「降臨者」的外星人所遺留下來的強殖裝甲，金屬外殼覆蓋住強殖生物再以制禦裝置控制，能抵受任何狀況的變化。'},
                '--other--':{},
                '牙齒':{'index':'other','name':'牙齒','value':0,'coin':3,'detail':'重擊敵人後獲得的牙齒，保養的不錯沒有黃黃臭臭的'},
                '壞掉的神奇寶貝球':{'index':'other','name':'壞掉的神奇寶貝球','value':0,'coin':3,'detail':'已經壞掉的神奇寶貝球，上面還寫著小智'},
                '汽水糖':{'index':'other','name':'汽水糖','value':0,'coin':3,'detail':'QQ軟軟，嚼一嚼還有可樂的味道'},
                '爛木頭':{'index':'other','name':'爛木頭','value':0,'coin':3,'detail':'一塊爛掉的木頭，似乎稍微用力就會碎掉'},
                '內衣':{'index':'other','name':'內衣','value':0,'coin':3,'detail':'打架就打架，怎麼打到連內衣都搶到手上了咧?'}, 
                '假髮':{'index':'other','name':'假髮','value':0,'coin':3,'detail':'從敵人頭上一把扯下，刷的一下差點被敵人頭上的反光給閃瞎了。'},
                '面紙':{'index':'other','name':'面紙','value':0,'coin':6,'detail':'一包沒有用過的面紙，包裝上寫著五月春風'},
                '棒球卡':{'index':'other','name':'面紙','value':0,'coin':6,'detail':'中華職棒的球員卡，但破損的差不多了，球員的姓名只看的到一個字"張"'},
                '電影票':{'index':'other','name':'電影票','value':0,'coin':6,'detail':'美麗華IMAX的電影票，但仔細一看已經過期了'},
                '鳳凰羽毛':{'index':'other','name':'鳳凰羽毛','value':0,'coin':6,'detail':'一根神奇的羽毛，但仔細一看好像跟公雞的差不多啊'},
                '阿兩公仔':{'index':'other','name':'阿兩公仔','value':0,'coin':6,'detail':'葛飾區龜有公園前派出所兩津勘吉1:4大小公仔'},
                '打火機':{'index':'other','name':'打火機','value':0,'coin':6,'detail':'檳榔攤販賣的十元打火機，上面還有清涼美女照片'},
                '小星星照片':{'index':'other','name':'小星星照片','value':0,'coin':9,'detail':'小星星可愛的照片一張，上面還有簽名TWStar'},
                '皮鞭':{'index':'other','name':'皮鞭','value':0,'coin':9,'detail':'不知道是誰的皮鞭，握把上面還寫著暗夜女王，握把底部還有一個大大的紅唇印'},
                '星爸照片':{'index':'other','name':'星爸照片','value':0,'coin':30,'detail':'星爸帥氣的照片一張，貼在牆上可以驅魔避邪保平安'},
                '黃金寶箱':{'index':'other','name':'黃金寶箱','value':0,'coin':3,'detail':'可以輸入使用道具=黃金寶箱看看這次尋到了什麼寶藏哦!!!'},
                }
        
        return dict[val]


    def fight_win_item(self,val):
        
        #判斷是否有裝備
        if val == 0:
        #物品機率
            i1=10
            i2=10
            i3=7
            i4=7
            i5=3
            i98=5
            i99=1
            i0=1000-(i1+i2+i3+i4+i98+i99)
        else:
            i1=150
            i2=100
            i3=50
            i4=20
            i5=10
            i98=150
            i99=5
            i0=1000-(i1+i2+i3+i4+i98+i99)
            
        #產生數列
        g0 = [0]*i0
        g1 = [1]*i1
        g2 = [2]*i2
        g3 = [3]*i3
        g4 = [4]*i4
        g5 = [5]*i5
        g98 = [98]*i98
        g99 = [99]*i99
        gift_list = g0+g1+g2+g3+g4+g5+g98+g99
        random.shuffle(gift_list)
        #get_result
        res = gift_list[0]
        #return_item
        if res == 0:
            return ('none','')
        if res == 1:
            dict = ['牙齒','壞掉的神奇寶貝球','爛木頭','面紙','電影票','打火機','阿兩公仔','鳳凰羽毛','汽水糖']
            content = random.choice(dict)
            return ('other',content)
        if res == 2:
            dict = ['紅色藥水','藍色藥水','橙色藥水','皮鞭','面紙','電影票','打火機','汽水糖']
            content = random.choice(dict)
            return ('other',content)
        if res == 3:
            dict = ['防禦增加藥水','攻擊增加藥水','小星星照片','皮鞭','面紙','電影票','打火機','棒球卡']
            content = random.choice(dict)
            return ('other',content)
        if res == 4:
            dict = ['橙色藥水','攻擊增加藥水','防禦增加藥水','小星星照片','皮鞭','白馬乎你夯','棒球卡']
            content = random.choice(dict)
            return ('other',content)
        if res == 5:
            dict = ['鼠兒果','堅韌藥劑','綠色藥水','勇敢藥水','妖精餅乾','幸運餅乾','星爸照片']
            content = random.choice(dict)
            return ('other',content)
        if res == 98:
            content = random.randint(1,5)
            return ('coin',content)
        if res == 99:
            ##content = random.randint(1,10)
            return ('other','黃金寶箱')

    def goldbox(self,uid,user_name):
        
        config = _sql.select_config(uid)
        config_json = json.loads(config[0][2])
        
        profile = config_json['profile']       
        
        dict = ['coin0','coin25','coin50','coin75','coin100'
                ,'星爸照片','初心者報紙','紙箱盔甲','阿嬤之杖','哈比菜刀','南瓜盾牌','骷髏骨甲',
                '疾走藥水','龍之珍珠','惡魔之血','伊娃的祝福','生命樹果實','無敵星星','角色重置卡','小星星照片']
        
        res = random.choice(dict)
        if res[0:4] == 'coin':
            if res[4:] == '0':
                _content = random.randint(10,100)
            else:
                _content = res[4:]
            old_coin = profile['starcoin']
            new_coin = old_coin+int(_content)
            profile['starcoin'] = new_coin
            content = '%s 開啟黃金寶箱獲得了< %s代幣 > (%s >> %s)'%(user_name,_content,old_coin,new_coin)           
        else:
            item_res = self.item_detail(res)
            index = item_res['index']
            if index in ['arms','armor']:
                i=1
                while i<20:
                    index = 'eq%s'%i
                    if index in profile['equ_list']:
                        i=i+1
                        if i >21:
                            _content = random.randint(10,50)
                            old_coin = profile['starcoin']
                            new_coin = old_coin+int(_content)
                            profile['starcoin'] = new_coin
                            content = '%s 開啟黃金寶箱獲得了< %s代幣 > (%s >> %s)'%(user_name,_content,old_coin,new_coin)
                    else:
                        item = res
                        item_value = item_res['value']
                        new_equ = {index:{item:{'val':item_value,'ed':100,'used':0}}}
                        profile['equ_list'].update(new_equ)
                            
                        #print(profile)
                            
                        content = '%s 開啟黃金寶箱獲得了< %s >'%(user_name, res)
                        break
            else:
                _content = res
                equ_list = profile['equipment']
                imax = random.randint(2,5)
                i =1
                while i<(imax+1): 
                    equ_list.append(_content)
                    i=i+1
                profile['equipment'] = equ_list
                content = '%s 開啟黃金寶箱獲得了< %s %s個 >'%(user_name, res, imax)
                #print(profile)
        config = json.dumps(config_json)
        _sql.update_config(uid,user_name,config)            
        return content 
                        
if __name__ == '__main__':
    main()
