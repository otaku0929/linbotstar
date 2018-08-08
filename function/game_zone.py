# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:46:41 2018

@author: 宇星
"""

import re
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
    #content = _game.card_pk('U9f2c61013256dfe556d70192388e4c7c','藍宇星冷男星','Andersen')
    #content = _game.get_atk_userlist()
    messages = '攻擊=@陳小馬（EK)'
    if re.match('^(對戰|攻擊)= ?@?(.+)',messages):
        uid = 'U9f2c61013256dfe556d70192388e4c7c'
        pkid = re.match('^(對戰|攻擊)= ?@?(.+)',messages).group(2).strip()
        #print(pkid)
        content = _game.card_pk(uid,'藍宇星冷男星',pkid)
        #print (content)
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
        #print(A,B)

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
            A_ATK_KEY=random.randint(0,100)+int(random.randint(0,A['lucky'])/10)
            B_ATK_KEY=random.randint(0,100)+int(random.randint(0,B['lucky'])/10)
       
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
                ATK_value= A_ATK[1]-B_DEF[1]
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
                if charA_HP<=0 or charB_HP<=0:
                    atk_list['atk_winner'] = A['user_name']
                    atk_list['atk_fin'] = '%s 戰勝了 %s'%(A['user_name'],B['user_name'])
                    break
                atk_round = atk_round+1
                if atk_round >18:
                    atk_list['atk_winner'] = '平手'
                    atk_list['atk_fin'] = '打累了~ %s %s 吃飯去啦'%(A['user_name'],B['user_name'])
                    break
            else:
                B_ATK = _card_game.getATK(B['ATK'],B['lucky'],B_Wiz_value)
                A_DEF = _card_game.getDEF(A['DEF'],A['lucky'])
                ATK_value= B_ATK[1]-A_DEF[1]
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
                if charA_HP<=0 or charB_HP<=0:
                    atk_list['atk_winner'] = B['user_name']
                    atk_list['atk_fin'] = '%s 戰勝了 %s'%(B['user_name'],A['user_name'])
                    break
                atk_round = atk_round+1
                if atk_round >18:
                    atk_list['atk_winner'] = '平手'
                    atk_list['atk_fin'] = '打累了~ %s %s 吃飯去啦'%(A['user_name'],B['user_name'])
                    break
                
        return ('----------\n%s\n%s\n----------\n\n%s\n\n戰鬥紀錄**********\n%s'%(profile_A,profile_B,atk_list['atk_fin'],atk_list['fight_status']))
        
                
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
        
        #_LUK_RATE = int(LUK/100)
        #print('STR:%s'%STR, 'DEX:%s'%DEX, 'LUK:%s'%LUK, 'LUK_RATE:%s'%_LUK_RATE)
        #print('VIT:%s'%VIT, 'AGI:%s'%AGI, 'LUK:%s'%LUK, 'LUK_RATE:%s'%_LUK_RATE)
    
        #hp_all = random.randint(1000,10000)
        hp = random.randint(VIT*random.randint(1,10),10000)
        #mp_all = random.randint(1000,10000)
        mp = random.randint(INT*random.randint(1,10),10000)

        #基礎ATK, DEF計算
        if LUK == 1:
            _ATK_RATE=1
            _DEF_RATE=1
        else:
            _ATK_RATE = (STR+DEX)*(random.randint(1,10))
            _DEF_RATE = (VIT+AGI)*(random.randint(1,10))
            
        #print('_ATK_RATE',_ATK_RATE, '_DEF_RATE',_DEF_RATE )
        
        #ATK, DEF計算
        RATE_POINT = 1000
        _STR_RATE= 1+random.randint(1,STR)/RATE_POINT
        #print('_STR_RATE',_STR_RATE)
        _DEX_RATE = 1+random.randint(1,DEX)/RATE_POINT
        #print('_DEX_RATE',_DEX_RATE)
        _VIT_RATE= 1+random.randint(1,VIT)/RATE_POINT
        _AGI_RATE= 1+random.randint(1,AGI)/RATE_POINT
        
        ATK = int(_ATK_RATE*_STR_RATE*_DEX_RATE)
        DEF = int(_DEF_RATE*_VIT_RATE*_AGI_RATE)        
             
        today_value = int((hp+mp+LUK)/1000)
        today=self.get_star(today_value)
        keywords = _star_talk.profile(user_name)
        content = [user_name,hp,mp,LUK,today,keywords,WIZ,ATK,DEF,today_value]
        return content
            
    def get_star(self,mum):

        val = int(mum+0.5)
        arr = ['☆','★','★☆','★☆','★★','★★☆','★★★','★★★☆','★★★★','★★★★☆','★★★★★']
        
        return arr[(val % 11)]
    

class card_fight(object):
    
    def __init__(self):
        self.class_name = 'card_fight' 

    def getATK(self,atk, lucky, wiz_value):
        
        atk0 = ['失手','滑倒了','忘了攻擊','zzzzz','被沉默了','吐口水','傻笑','哇哈哈哈哈','肚子痛先大便',
                '0分考卷','佛系功擊','吃到半隻小強']
        atk1 = ['普通攻擊','拿棒棒糖攻擊','丟石頭','戳一下','丟樸克牌','丟RAM攻擊','咬一口','丟榴槤',
                '飛吻','五層復合金炒菜鍋','爆炸佛跳牆','獅子挽歌','甩巴掌','彈鼻屎','掃把亂掃','滴蠟燭',
                '自拍照片','打呼','惡魔棒式訓練','丟麥當勞漢堡','冰的啦','小孩不睡覺','魔貫光殺砲',
                '乖寶寶睡拳','界王拳','無上飛彈冰淇淋','野豬衝擊鐵頭功','箱神~~~~~','要你命三千',
                '豪大大雞排','奪命連環扣','嬌喘','丫宅的心聲','哇沙米沙瓦','盲人腳底按摩','烤箱裡拼命加水',
                '丟生日蛋糕','巴蕊','踩腳指','拉頭髮','丫姑親一咧','拔鼻毛']
        atk2 = ['強力攻擊','破壞拳','迴旋踢','關門放狗','伸長吧~~拳頭','奧客精神','RAP碎碎唸','恐龍攻擊',
                '百裂拳','天帝之眼','紅蓮爆炎刃','丟大便','天翔龍閃','唸經','竹筍炒肉絲','宅男的右手','氣圓斬',
                '殺豬刀','降龍十八掌','還我漂漂拳','加滕金手指','化妝化一半','魔貫光殺砲','丟出科南']
        atk3 = ['屬性攻擊','龜派氣功波','超級飛踢','三刀流~鬼斬','三寶上路','卍解','霸王龍之吻','昇龍拳',
                '人妖拳法','召喚古力帕','飛天蟑螂','超級凍結冰箭','火龍的碎牙','天輪‧循環之劍','色誘術-女女術']
        atk4 = ['致命一擊','必殺一擊','元氣彈','跪鍵盤密術','三檔 骨氣球','九九重陽功','唱歌攻擊','召喚殺很大',
                '鬼氣九刀流','加班加到死','等五年還沒洗好澡','丫宅的怨念','媽媽的咆哮','色誘術-逆後宮之術',
                '順手拿的折凳','死亡筆記本']
        atk9 = ['讓對手拉肚子攻擊','放屁臭死了對手','召喚了神龍，進行攻擊','卸妝攻擊']
        
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
                rounad_ATK = random.randint(1,atk)
                atk_value = random.randint(rounad_ATK,atk)*1.5
            elif atk_key >=51 and atk_key <81:
                atk_way = random.choice(atk2)
                atk_value = int(random.randint(int(atk*0.4),atk)*(3+wiz_value))
            elif atk_key >=81 and atk_key <96:
                atk_way = random.choice(atk3)
                atk_value = int(random.randint(int(atk*0.6),atk)*(4+wiz_value))
            elif atk_key >=96:
                atk_way = random.choice(atk4)
                atk_value = int(random.randint(int(atk*0.7),atk)*lucky/10)


    
        return (atk,atk_value,atk_way)
    
    def getDEF(self,DEF, lucky):
        
        def0 = ['扮鬼臉嚇人','盾檔','太極一式','講笑話','岩壁','灑豆子趕人','格檔','招架','我是香菇',
                '吃成胖子','變身綿花糖','丟臭豆腐','愛的抱抱','倒沙拉油','鍋蓋','舞空術飛走','模仿猩猩','臭臭襪',
                '騎豬快跑','伸出美腿','搖籃曲','泡泡鏡像','單眼拍照','啤酒乾一杯','丟圖釘在地上','來小星星抽一張吧',
                '吃冰休息吧','魔幻甜甜圈','在椅子上黏口香糖','縮不了的小腹','這不是肯徳雞','掀榻榻米','淚眼汪汪',
                '搔癢','撒嬌','戰吼','巨人之鎧','你褲子破洞了','又富檻了','今天萌萌的','闇影之舞','酸檸檬餵食',
                '減肥的怨念','熱水放好囉','1+1等於?','一哭二鬧三上悠亞','你知不知道我爸是誰','外拍都下雨',
                '愛肝一罐20元','給你蠻牛','國王的新衣','給你呼呼','吃鮭魚卵隱身'
                ]
        def1 = ['硬氣功','分身防禦','閃避','丟香蕉讓對方滑倒','拿CRT螢幕擋住','用滑鼠綁住敵人','呼叫館長',
                '丟枕頭給敵人','你有freestyle嗎','閃現','拿美食餵養','召喚龍騎士','丟煙霧蛋','空間移動',
                '請你吃苦瓜','烏索普啊~~啊~~','百花繚亂','說八卦','手機放電','可愛五連拍','你聽過安麗嗎',
                '我是工程師','洗澡下線術','召喚豬隊友','我是單身狗','點穴','妖精之鎖','手牽手去郊遊','誘惑之鎧',
                '太陽拳','封印鐵壁','色誘術-男男術','藏蹤術','誠實豆沙包','喝光妳的SKII','舒心精油按摩','躺著也中槍',
                '請死神吃蘋果'
                ]
        def2 = ['超級防禦','盾牆','冰牆','催眠術','變張3讓對方傻住','混元一氣功','拿鏡子給敵人','灑鈔票','隔壁老王',
                '瞬間移動','海市蜃樓','和睦相處','水遁．泡膜壁','穿上隱形斗篷']
        def9 = ['我閃我閃我閃閃閃','你看不到我','你打不到我','究極防禦','聖盾術']
        
        if int(lucky/10) == 0:
            def_key = 1
        else:
            def_key = random.randint(1,int(lucky/10))
        
        #print(def_key)
        
        if def_key >= 50 and def_key<81:
            def_way = random.choice(def1)
            def_value = random.randint(int(DEF*0.3),DEF)*1.5       
        elif def_key >= 81 and def_key<95:
            def_way = random.choice(def2)
            def_value = random.randint(int(DEF*0.6),DEF)*2.5
        elif def_key >= 95:
            def_way = random.choice(def9)
            def_value = random.randint(int(DEF*0.9),DEF)*5*def_key
        else:
            def_way = random.choice(def0)
            rounad_DEF = random.randint(1,DEF)
            def_value = random.randint(rounad_DEF,DEF)
        
        return (DEF,def_value,def_way)
    
    
    def WizATK(self,A_WIZ, B_WIZ):
        
        dict = {'混':{'聖':0.2,'光':0.2,'萌':0.5},
                '聖':{'邪':0.5,'毒':0.2,'萌':-2},
                '邪':{'萌':-2},
                '闇':{'聖':0.2,'萌':-2},
                '光':{'闇':0.5,'萌':-2},
                '金':{'木':0.5,'萌':-2},
                '木':{'土':0.5,'萌':-2},
                '水':{'火':0.5,'萌':2},
                '火':{'金':0.5,'冰':0.2,'萌':-2},
                '土':{'水':0.5,'風':0.2,'萌':-2},
                '雷':{'魅':0.8,'萌':-2},
                '冰':{'魅':0.8,'萌':-2},
                '風':{'魅':0.8,'萌':2},
                '日':{'萌':-2},
                '月':{'萌':-2},
                '星':{'萌':-2},
                '毒':{'魅':0.8,'萌':-2},
                '魂':{'魅':0.8,'萌':-2},
                '魅':{'萌':0.2},
                '萌':{}
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
