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

    
    content = _game.user_profile('Ud0414e339e9c242b19a2dd22dd1f6189','藍宇星冷男星','http://dl.profile.line-cdn.net/0hLkoyPlmqE0RSAD5u3DZsE25FHSklLhUMKmILJiUCRHQrZVRGPWZfJnJTTHJ5ZQESaWNUJn5VTics')
    print(content)

    
class game_zone(object):
    
    def __init__(self):
        self.class_name = 'game_zone'
        
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
       
    def user_profile(self,uid,user_name,pictureUrl):
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:11]
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
                new_json = {'profile_time':time}
                config_json['profile']['profile_time'] = new_json['profile_time']
                config = json.dumps(config_json)
                _sql.update_config(uid,user_name,config) 
                
                message = self.profile_game_content(uid,user_name) 
                
                content = _photos.user_daily_photo(uid,message,pictureUrl)
                
                return (content)
#                return self.profile_game_content(uid,user_name)               
        else:
            new_json = {'profile_time':time}
            config_json['profile'].update(new_json)
            config = json.dumps(config_json)
            _sql.update_config(uid,user_name,config)         
            
            message= self.profile_game_content(uid,user_name)
            
            content = _photos.user_daily_photo(uid,message,pictureUrl)
            
            return (content)

    def profile_game_content(self,uid,user_name):
        
        
        WIZ = random.choice(['光','闇','金','木','水','火','土','雷','冰','風','聖','邪','日','月','星','毒','魂','萌','混','魅'])

        hp_all = random.randint(100,10000)
        hp = random.randint(0,hp_all)
        mp_all = random.randint(100,10000)
        mp = random.randint(0,mp_all)
        lucky = random.randint(0,1000)
        ATK = int(random.randint(1,hp)*(lucky/100))
        DEF = int(random.randint(1,mp)*(lucky/100))
        today = self.get_star((hp+mp+lucky/1000))
        #today=self.get_star(random.randint(0,100)/10)
        keywords = _star_talk.profile(user_name)
        #content = '%s\n\nHP:%s/%s\nMP:%s/%s\n幸運值:%s\n今日運氣:%s\n\n==小星星叮嚀==\n%s'%(user_name,hp,hp_all,mp,mp_all,luncky,today,keywords)
        #content = [user_name,'HP：%s/%s'%(hp,hp_all),'MP：%s/%s'%(mp,mp_all),'幸運值：%s'%lucky,'今日運勢：%s'%today,keywords]
        content = [user_name,hp,mp,lucky,today,keywords,WIZ,ATK,DEF]
        return content
            
    def get_star(self,mum):

        val = int(mum+0.5)
        arr = ['☆','★','★☆','★☆','★★','★★☆','★★★','★★★☆','★★★★','★★★★☆','★★★★★']
        
        return arr[(val % 11)]



if __name__ == '__main__':
    main()
