import re
import random

import function.hsing
_hsing = function.hsing.hsing()

import function.sys_messages
_sys_mg = function.sys_messages.sys_messages()

def main():
    res = '哈哈哈哈哈哈哈哈'
    _star_talk = start_talk()
    print(_star_talk.star_talk(res))
    
class start_talk(object):
    
    def __init__(self):
        self.class_name = 'start_talk'

    def star_talk(self, messages_talk, user_name=None):
        if re.search('(為什麼)?[沒有|不會|不給我](產生)?卡片',messages_talk):
            return self.talk_dict('為什麼沒有卡片',user_name)
        if re.match("^幹|fuck|操",messages_talk):
             return self.talk_dict('fuck',user_name)
        if re.search('(操|幹|fuck)[你|他](娘|媽|老師|you)',messages_talk):
            return self.talk_dict('fuck',user_name)
        if re.search("^三小",messages_talk):
             return self.talk_dict('fuck',user_name)
        if re.search("^靠北",messages_talk):
             return self.talk_dict('靠北',user_name)
        if re.search("三字經",messages_talk):
             return self.talk_dict('三字經',user_name)
        if re.search("爆料",messages_talk):
             return self.talk_dict('爆料',user_name)
        if re.search("壞掉了",messages_talk):
             return self.talk_dict('壞了',user_name)
        if re.search("哈哈哈哈哈",messages_talk):
             return self.talk_dict('哈N',user_name)
        if re.search("早安|早啊|早",messages_talk):
             return self.talk_dict('早安',user_name)
        if re.search("晚安|睡囉",messages_talk):
             return self.talk_dict('晚安')
        if re.search("尿好了|有尿了",messages_talk):
             return self.talk_dict('尿好了',user_name)
        if re.search("(才|你|小星星)尿床",messages_talk):
             return self.talk_dict('尿床',user_name)
        if re.search("小星星",messages_talk):
            if re.search('[好很超]累',messages_talk):
                return self.talk_dict('好累',user_name)
            if re.search('懂嗎',messages_talk):
                return self.talk_dict('懂嗎',user_name)  
            if re.search('[看我]不懂',messages_talk):
                return self.talk_dict('看不懂',user_name)             
            if re.search('騙人',messages_talk):
                return self.talk_dict('騙人',user_name)         
            if re.search('rap',messages_talk):
                return self.talk_dict('rap',user_name)             
            if re.search('下(.+)?雨|陰(陰的|天)|有一點雨|毛毛雨',messages_talk):
                return self.talk_dict('陰雨天',user_name)
            if re.search('[大出](太陽)|好熱|熱死了',messages_talk):
                return self.talk_dict('熱死了',user_name)
            if re.search('晴天|涼爽|好天氣',messages_talk):
                return self.talk_dict('晴天',user_name)
            if re.search('涼涼的|有(一)?點(涼|冷)',messages_talk):
                return self.talk_dict('涼涼的',user_name)
            if re.search('好冷|冷死了|[下有飄]雪',messages_talk):
                return self.talk_dict('好冷',user_name)
            if re.search('賭[神聖俠]',messages_talk):
                return self.talk_dict('賭神',user_name) 
            if re.search('會胖',messages_talk):
                return self.talk_dict('會胖',user_name)    
            if re.search('被(.+)?句點',messages_talk):
                return self.talk_dict('句點',user_name)
            if re.search('句點王',messages_talk):
                return self.talk_dict('句點王',user_name) 
            if re.search('腎虧嗎',messages_talk):
                return self.talk_dict('腎虧',user_name)            
            if re.search('[投客]訴',messages_talk):
                return self.talk_dict('投訴',user_name)             
            if re.search('胖胖的',messages_talk):
                return self.talk_dict('胖胖的',user_name)          
            if re.search('小星星好色',messages_talk):
                return self.talk_dict('小星星好色',user_name)
            if re.search('那摳呢',messages_talk):
                return self.talk_dict('那摳呢',user_name) 
            if re.search('那舔呢',messages_talk):
                return self.talk_dict('那舔呢',user_name)            
            if re.search('吹含吸舔摳',messages_talk):
                return self.talk_dict('吹含吸舔摳',user_name) 
            if re.search('什麼技巧',messages_talk):
                return self.talk_dict('什麼技巧',user_name)           
            if re.search('[學變]壞了',messages_talk):
                return self.talk_dict('學壞了',user_name)
            if re.search('壞壞',messages_talk):
                return self.talk_dict('壞壞',user_name)
            if re.search('(誰|沒人)叫你',messages_talk):
                return self.talk_dict('叫你',user_name)
            if re.search('流鼻血',messages_talk):
                return self.talk_dict('流鼻血',user_name)
            if re.search('什麼秘密',messages_talk):
                return self.talk_dict('秘密',user_name)
            if re.search('[講說]幹話',messages_talk):
                return self.talk_dict('幹話',user_name)        
            if re.search('(出賣|賣了)',messages_talk):
                return self.talk_dict('出賣',user_name)
            if re.search('玻璃心',messages_talk):
                return self.talk_dict('玻璃心',user_name)
            if re.search('[很好超真]酷',messages_talk):
                return self.talk_dict('cool',user_name)
            if re.search('[很好超真][棒讚]',messages_talk):
                return self.talk_dict('good',user_name)
            if re.search('[很|好|超][煩|吵]',messages_talk):
                return self.talk_dict('很煩',user_name)
            if re.search('傷心|難過|想哭',messages_talk):
                return self.talk_dict('傷心',user_name)
            if re.search('失戀',messages_talk):
                return self.talk_dict('失戀',user_name)
            if re.search('想[他|她]',messages_talk):
                return self.talk_dict('想他',user_name)
            if re.search('看穿了',messages_talk):
                return self.talk_dict('看穿',user_name)
            if re.search('[最|超|好](窩心|貼心)',messages_talk):
                return self.talk_dict('貼心',user_name)
            if re.search('[很|好|超|真](可愛|卡哇伊)',messages_talk):
                return self.talk_dict('可愛',user_name)
            if re.search('不(可愛|卡哇伊)',messages_talk):
                return self.talk_dict('不可愛',user_name)
            if re.search('(卡哇邦嘎|忍者龜)',messages_talk):
                return self.talk_dict('忍者龜',user_name)    
            if re.search('[很|好|超|是|一臉|真](白痴|白癡)',messages_talk):
                return self.talk_dict('白痴',user_name)
            if re.search('[很|好|超|是|一臉|真]白爛',messages_talk):
                return self.talk_dict('白爛',user_name)
            if re.search('[很|好|超|是|一臉|真]自戀',messages_talk):
                return self.talk_dict('自戀',user_name)
            if re.search('[很|好|超|是|一臉|真]白目',messages_talk):
                return self.talk_dict('白目',user_name)
            if re.search("不好笑",messages_talk):
                return self.talk_dict('notfun',user_name)
            if re.search("買(什麼|東西)",messages_talk):
                return self.talk_dict('buy',user_name)
            if re.search("早(安|啊|上好)",messages_talk):
                return self.talk_dict('早安',user_name)
            if re.search("午安",messages_talk):
                return self.talk_dict('午安',user_name)
            if re.search("晚(安|上好)|睡[覺|了|囉]",messages_talk):
                return self.talk_dict('晚安',user_name)
            if re.search("(再見|bye|881)",messages_talk):
                return self.talk_dict('再見',user_name)
            if re.search("你好|安安|hello|hi|HI",messages_talk):
                return self.talk_dict('hi',user_name)
            if re.search("找(你|妳|星星)",messages_talk):
               return self.talk_dict('you',user_name)
            if re.search("找星(爸|拔)|星(爸|拔)咧|星(爸|拔)在哪裡|叫一下星(爸|拔)|叫星(爸|拔)",messages_talk):
                return self.talk_dict('星爸',user_name)
            if re.search("找(碴|麻煩)",messages_talk):
                return self.talk_dict('找麻煩',user_name)
            if re.search("聊天]",messages_talk):
                return self.talk_dict('talk',user_name)
            if re.search("聽話|乖|乖乖",messages_talk):
                return self.talk_dict('goodboy',user_name)
            if re.search("(愛|喜歡)(你|小星星)",messages_talk):
                return self.talk_dict('愛你',user_name)
            if re.search("(喜歡|愛])什麼",messages_talk):
                return self.talk_dict('like',user_name)
            if re.search("(喜歡|愛)[吃|喝|玩|看|聽|誰|我]",messages_talk):
                if re.search("(喜歡|愛)([吃喝玩看聽誰我])",messages_talk).group(2) == "吃":
                    return self.talk_dict('like_eat',user_name)
                if re.search("(喜歡|愛)([吃喝玩看聽誰我])",messages_talk).group(2) == "喝":
                    return self.talk_dict('like_drink',user_name)         
                if re.search("(喜歡|愛)([吃喝玩看聽誰我])",messages_talk).group(2) == "玩":
                    return self.talk_dict('like_play',user_name)
                if re.search("(喜歡|愛)([吃喝玩看聽誰我])",messages_talk).group(2) == "看":
                    return self.talk_dict('like_see',user_name)
                if re.search("(喜歡|愛)([吃喝玩看聽誰我])",messages_talk).group(2) == "聽":
                    return self.talk_dict('like_listen',user_name)
                if re.search("(喜歡|愛)([吃喝玩看聽誰我])",messages_talk).group(2) == "誰":
                    return self.talk_dict('like_who',user_name)
                if re.search("(喜歡|愛)([吃喝玩看聽誰我])",messages_talk).group(2) == "我":
                    return self.talk_dict('like_me',user_name)
            if re.search("機器人|是(誰|什麼|男|女)",messages_talk):
                return self.talk_dict('robot',user_name)
            if re.search("多大|幾歲",messages_talk):
                return self.talk_dict('多大',user_name)
            if re.search("生日",messages_talk):
                return self.talk_dict('birthday',user_name)
            if re.search("住那|住哪|家在哪|家在那",messages_talk):
                return self.talk_dict('住那',user_name)
            if re.search("有什麼功能|功能表|指令",messages_talk):
                return _sys_mg.m_function()
            if re.search("哈|哈哈|哈哈哈",messages_talk):
                return self.talk_dict('哈',user_name)
            if re.search("哭|欠[揍打]|[揍打]你",messages_talk):
                return self.talk_dict('cry',user_name)
            if re.search("打屁股|打屁屁",messages_talk):
                return self.talk_dict('kpp',user_name)
            if re.search("生氣",messages_talk):
                return self.talk_dict('angry',user_name)
            if re.search('[傻笨呆][子蛋啊瓜呀]|fool|stupid|北七|白痴|白癡|蠢',messages_talk):
                return self.talk_dict('fool',user_name)
            if re.search("壞了|該修理|要修理",messages_talk):
                return self.talk_dict('壞掉了',user_name)
            if re.search("出團",messages_talk):
                return self.talk_dict('group',user_name)
            if re.search("運動|動一動",messages_talk):
                return self.talk_dict('sport',user_name)
            if re.search("吃(大便|屎|屁)",messages_talk):
                return self.talk_dict('eatshit')
            if re.search("吃虧",messages_talk):
                return self.talk_dict('吃虧')
            if re.search("餓",messages_talk):
                return self.talk_dict('餓了',user_name)
            if re.search("吃什麼|想吃|愛吃|要吃|吃飯",messages_talk):
                return self.talk_dict('eat',user_name)
            if re.search("吃飽了嗎",messages_talk):
                return self.talk_dict('eated',user_name)
            if re.search("[吃喝](.+)好?嗎",messages_talk):
                return self.talk_dict('吃?嗎',user_name)
            if re.search("喝酒",messages_talk):
                return self.talk_dict('drink_酒',user_name)
            if re.search("[虧撩](妹|你|妳|我|咩|妹妹|姐姐)",messages_talk):
                return self.talk_dict('虧妹',user_name)
            if re.search("誰最帥",messages_talk):
                return self.talk_dict('最帥',user_name)
            if re.search("誰最美",messages_talk):
                return self.talk_dict('最美',user_name)
            if re.search("誰最醜",messages_talk):
                return self.talk_dict('最醜',user_name)
            if re.search("誰最笨",messages_talk):
                return self.talk_dict('最笨',user_name)
            if re.search("誰最(強|厲害)",messages_talk):
                return self.talk_dict('最強',user_name)
            if re.search("誰最弱",messages_talk):
                return self.talk_dict('最弱',user_name)
            if re.search("誰最[傻呆]",messages_talk):
                return self.talk_dict('最呆',user_name)
            if re.search("誰最白[痴癡]",messages_talk):
                return self.talk_dict('最痴',user_name)
            if re.search("誰最(色|好色)",messages_talk):
                return self.talk_dict('最色',user_name)
            if re.search("(難|不好)聽",messages_talk):
                return self.talk_dict('badsing',user_name)
            if re.search("(唱|唱一｜換｜換一|來一)[歌首]",messages_talk):
                content = self.talk_dict('sing',user_name)
                if re.search("抽歡歌",content):
                    res = _hsing.sing17()
                    if re.search("找不到歌",res):
                        return "我不知道要唱什麼耶"
                    else:
                        return res
                elif re.search("UID",content):
                    if  _hsing.s17uidsong(re.search("UID(\d+)",content).group(1)) == "查不到歌曲":
                        return "突然不知道要唱什麼"
                    else:
                        #print(content)
                        return _hsing.s17uidrandom(re.search("UID(\d+)",content).group(1))
                else:
                    return content
            if re.search("卡米狗|Orz|linebot",messages_talk):
                return self.talk_dict('linebot',user_name)
            if re.search("心情(不好|差|很差)",messages_talk):
                return self.talk_dict('心情不好',user_name)
            if re.search("[很好超]悶",messages_talk):
                return self.talk_dict('悶',user_name)
            if re.search("破功",messages_talk):
                return self.talk_dict('破功',user_name)
            if re.search("我不知道",messages_talk):
                return self.talk_dict('我不知道',user_name)
            if re.search("為什麼要扮烏龜",messages_talk):
                return self.talk_dict('為什麼要扮烏龜',user_name)
            if re.search("不[要想]扮烏龜",messages_talk):
                return self.talk_dict('不扮烏龜',user_name)
            if re.search('扮烏龜',messages_talk):
                return self.talk_dict('扮烏龜',user_name)
            if re.search('我有(說講)啊',messages_talk):
                return self.talk_dict('有說啊',user_name)
            if re.search('插[嘴話]',messages_talk):
                return self.talk_dict('插嘴',user_name)
            if re.search('又來了',messages_talk):
                return self.talk_dict('又來了',user_name)
            if re.search('小星星帶(回去|走|回家)',messages_talk):
                return self.talk_dict('小星星帶回家',user_name)
            if re.search('髒髒的',messages_talk):
                return self.talk_dict('髒髒的',user_name)
            if re.search('想去那裡|想去那旅行',messages_talk):
                return self.talk_dict('去旅行',user_name)
            if re.search('為什麼(要)?吃羊羊',messages_talk):
                return self.talk_dict('吃羊羊',user_name)
            if re.search('好兇',messages_talk):
                return self.talk_dict('好兇',user_name)
            if re.search('有禮貌',messages_talk):
                return self.talk_dict('有禮貌',user_name)
            if re.search('小星星會怎麼做呢',messages_talk):
                return self.talk_dict('小星星會怎麼做呢',user_name)
            if re.search('有玩抖音',messages_talk):
                return self.talk_dict('有玩抖音',user_name)
            if re.search('星爸的抖音',messages_talk):
                return self.talk_dict('星爸的抖音',user_name)
            if re.search('我有勇氣',messages_talk):
                return self.talk_dict('我有勇氣',user_name)
            if re.search('喜歡游游',messages_talk):
                return self.talk_dict('喜歡游游',user_name)
            if re.search('會游游',messages_talk):
                return self.talk_dict('會游游',user_name)
            if re.search('[要該]怎辦',messages_talk):
                return self.talk_dict('該怎辦',user_name)
            if re.search('[要該]怎麼做',messages_talk):
                return self.talk_dict('怎麼做',user_name)
            if re.search('有問了',messages_talk):
                return self.talk_dict('有問了',user_name)
            if re.search('[還沒]有問',messages_talk):
                return self.talk_dict('沒有問',user_name)
            if re.search('進群組？',messages_talk):
                return self.talk_dict('進群組',user_name)
            if re.search('[是大好]變態',messages_talk):
                return self.talk_dict('變態',user_name)
            if re.search('給(我)?(錢|代幣)',messages_talk):
                return self.talk_dict('給錢',user_name)
            if re.search('只[會有]一招',messages_talk):
                return self.talk_dict('一招',user_name)
            if re.search('(有|有什麼)好事',messages_talk):
                return self.talk_dict('有什麼好事',user_name)
            if re.search('我好無聊',messages_talk):
                return self.talk_dict('我好無聊',user_name)
            if re.search('我吃飽了',messages_talk):
                return self.talk_dict('我吃飽了',user_name)
            if re.search('(怎麼|要)買裝備',messages_talk):
                return self.talk_dict('買裝備',user_name)
            if re.search('(怎麼|要)修裝',messages_talk):
                return self.talk_dict('修裝',user_name)
            if re.search('(怎麼|要)賣(裝備|道具|東西)',messages_talk):
                return self.talk_dict('賣裝備',user_name)
            if re.search('沒睡飽',messages_talk):
                return self.talk_dict('沒睡飽',user_name)
            if re.search('有雞油',messages_talk):
                return self.talk_dict('有雞油',user_name)
            if re.search('愛我嗎',messages_talk):
                return self.talk_dict('愛我嗎',user_name)
            else:
                return self.talk_dict('random',user_name) 
            
    def talk_dict(self,res,u=None):
        if u ==None:
            u = ''
        dict={
                '為什麼沒有卡片':['請加小星星好友再產生一次看看，如果還是有問題請到小星星的首頁或粉絲團回報一下'],
                '愛我嗎':['當然是~~不愛都不行囉','看著我的眼，有看到愛心嗎?','愛妳愛妳愛妳好愛妳','照照鏡子吧','我想睡了，晚安',
                       '這問題答案就在你心裡','愛不是用嘴巴講講的'],
                '有雞油':['機油一瓶350','雞油比較清，但豬油卡香啦','不然吃吃魚肝油如何?','還是要上一點牛油呢'],
                '沒睡飽':['那來一杯拿鐵吧!!醒醒腦','我敲一敲就醒了','嘿嘿嘿，晚上做賊去了嗎?','可憐的小孩，撐著吧'],
                '賣裝備':['範例: 賣道具=eq1 或 賣道具=紅色藥水  ， 賣武器及防具要用裝備代碼來賣哦'],
                '修裝':['範例: 修理裝備=eq1  裝備代碼請使用< 查人物裝備 >來確認，另外修裝費是依據攻擊力及耗損度來計算哦' ],
                '買裝備':['範例: 買裝備=阿嬤之杖  ， 可以先查看武器商店有什麼東西可以買哦'],
                '我吃飽了':['那很好啊','吃了什麼呢?','嗚~~~我都還沒吃','你沒有帶我一起去吃','吃飽飽休息一下吧'],
                '我好無聊':['無聊啊，那來聊天吧','那要唱歌嗎?','聽聽歌好了'],
                '有什麼好事':['踩到狗屎吧','中樂透','喜歡的人跟你對眼','發現新大陸','都抽到美女','我想想哦~~~'],
                '一招':['一招就夠了','小星星一出天下無敵','嘿~~GM只要一招就夠了啦'],
                '給錢':['口袋空空，錢都在星爸那裡','人肉鹹鹹，小星星涼涼，要錢沒有，要命也不給','自已去打怪賺錢啊','打我會掉錢哦'],
                '變態':['變態是一種昆蟲進化的過程','你才戀態咧，我只是好奇好嗎','嘿嘿嘿~~~','不要過來我要叫囉'],
                '進群組':['把我邀進去群組就可以了，但一個群只能有一個機器人哦','如果群組裡有別的機器人，我就進去不唷'],
                '沒有問':['問一下吧，有些時候先低頭不代表輸啊','不問怎知道結果?'],
                '有問了':['那他怎麼說?','說了些什麼?'],
                '怎麼做':['有時候放手是最好的選擇','你有問過原因了嗎?','先哄哄她啊','先彼此冷靜一下好了'],
                '該怎辦':['先冷靜下來吧','嗯，我也不知道','感情事真的很難啊'],
                '會游游':['蝌蚪時期算嗎?','我不會~~妳要教我嗎?','桌上偶而摸二圈'],
                '喜歡游游':['我沒有游過','感覺游泳是很棒的運動','星爸喜歡','水裡的還是桌上的?'],
                '我有勇氣':['梁靜茹給的嗎?','很好~但還是不要愛上我'],
                '星爸的抖音':['爸沒有說~','我不知道耶~要問爸'],
                '有玩抖音':['沒有~但星爸有','我想玩~但爸不給我玩','沒有~但好多人玩哦'],
                '小星星會怎麼做呢':['我會珍惜與妳一起的每一秒','我不知道~~~','什麼都不會想吧','最後的一分鐘~放空了也不錯',
                            '就放鬆吧~何必到最後一秒都還那麼辛苦呢?'],
                '有禮貌':['星爸說有禮貌的小孩人人愛','因為我長大了啊','我是禮貌好寶寶','那妳要給我好寶寶貼紙嗎?'],
                '好兇':['我又沒長胸','咬你哦','我最可愛了~怎會胸','真的胸的不在這裡'],
                '吃羊羊':['本草綱目有記載:羊肉「暖中補虛，開胃健力，滋腎氣」','吃羊羊補幹話'],
                '去旅行':['我喜歡日本','巴峇島好像不錯','要去瑞士嗎?','嗯~~~我想一想哦~~','想去妳心裡'],
                '髒髒的':['那就洗一洗啊','那一起來洗澡吧','什麼髒?','我最純了','髒髒包嗎?嘿~~~~~'],
                '小星星帶回家':['人家還想玩嘛','不要啦~~~我還不想回家','那妳也要跟我一起回家嗎?','你不喜歡我嗎','我很吵嗎?',
                          '我的家就在妳心裡'],
                '又來了':['來什麼','登楞~~我跳出來了~這樣嗎?','??????','你說什麼我不懂','%s董~很久沒來啊~'%u],
                '插嘴':['我只是在刷存在感','這樣才熱鬧啊','哼~~那我不講話了','我也想參與嘛'],
                '有說啊':['什麼~~那我怎麼沒印象','真的有說嗎?','那你再說一次','啊~~~~我忘了~~~'],
                '為什麼要扮烏龜':['因為烏龜烏龜蹺','可愛啊','不然你想扮什麼呢?','那扮豬好了'],
                '我不知道':['沒關係~先放空一下','那聊聊天吧','有些頭緒真的很難理','加油'],
                '破功':['唉呀~發功時是不能說XXOO的','星爸都不多教我一點','妳要教我回話嗎?'],
                '悶':['為什麼悶呢?','小星星陪妳聊天吧','吃點美食可以解悶哦','遇到什麼事了嗎?'],
                '心情不好':['為什麼心情不好呢?','說來聽聽','失戀了嗎?','工作上的事嗎?','悶要說出來哦'],
                '好累':['怎麼了嗎?','要抓龍嗎?','摸摸頭','發生什麼事了呢?','先喝口水休息一下吧!'],
                '懂嗎':['就算不懂也要說~~~我~~~真的不懂','嗯嗯嗯~~~我想想哦','懂不懂自在人心','我懂~我懂~~~我真的~~~~懂~~','我只知道咚滋咚滋',
                      '我是誰~小星星耶~~~怎麼可能懂呢?','問問星爸好了'],
                '看不懂':['說你笨還不承認','有些事不用懂','智慧這二個字不是人人都有的','那就再看一次囉'],
                '騙人':['%s手來。我如果騙妳，我心臟會砰砰跳。妳感覺一下，有嗎？'%u,'我那麼的誠懇','不可否認我長得很醜，可是我很溫柔，而且永遠不會說謊',
                      '你這無禮的傢伙！'],
                '愛你':['%s我也愛你'%u,'那麼直接我會害喜啦','愛上我要很有勇氣的','%s來抱抱'%u,'那麼多人在看，我好害羞哦','啾~~~~~~~~','你絕對絕對絕對不是我喜歡的類型！',
                      '我沒有自信放得下你，%s，我喜歡你。'%u,'愛是什麼，就是把妳放在我心裡','不要說愛我，因為那是我要對妳說的話，妳只要接受我就好了'],
                'rap':['我只會捲舌不會饒舌','饒舌是什麼我不懂、但GG他懂','yo~yo~ya~ya~啊哈~~~ 然後咧',
                       '就讓我來rap 揭開你的瘡疤　就讓我來rap 你把聽眾當白癡啊\n就讓我來rap 哈哈…有錢屌就大　就讓我來rap 來看樂壇悶死吧',
                       'Ya ya put your hands in the air\nYa ya put your hands in the air\nThe real hip hop is over here\nparty people put your hands of in the air\n\
                       The real hip hop is over here\nparty people Ya Ya Ya'],
                '涼涼的':['那外套要搭一件哦','涼涼的也不錯啦~才不會流汗','那多喝點溫水','看看是不是要下雨了','要注意可能會下雨哦'],
                '好冷':['讓星星來溫暖妳','來給妳暖暖包','衣服有多穿一點嗎?','別感冒了啊','毛帽、圍巾、手套、外套、都記得帶著哦',
                      '疑冷男不在啊','是我剛剛講話太冷了嗎?'],
                '晴天':['真棒~這樣很舒服耶','微微風湧起舊夢.......啊唱起歌來了','那出去玩玩吧~','讚讚讚讚讚'],
                '熱死了':['要注意防曬哦','不喜歡太熱的天氣，會一直流汗','天氣熱要多喝點水','別忘了補充水份哦','我們去吃冰吧'],
                '陰雨天':['那要記得帶傘哦','能搭車就別騎車吧','雨具記得帶著','到家先喝杯溫水哦','要晴天娃娃嗎?'],
                '賭神':['我變不出三來啊','我是地獄倒楣鬼','我也想當那個賭......什麼的','在牌桌上永遠有你想不到的事','小賭怡情，大賭移平 還是不賭的好'],
                '會胖':['我肥我驕傲','吃一點沒關係啦','減肥永遠是明天的事','沒關係還有%s'%u,'圍腰？別開玩笑了！不用你們操心啦！',
                      '真是一點也不可愛'],
                '句點':['明明就很會聊天','你才是句點王','臉黑加一條線就變，了','。。。。。。。','句點是為了講更多的話',
                      '所以說標點符號很重要','你再怎麼稱讚我，我也不會高興的啦！你這個混蛋'],
                '句點王':['句點王是什麼，能吃嗎?','。','我覺得吃肉王比較好','你也很會啊'],
                '腎虧':['什麼你腎虧','我才沒有','我沒有~星爸也沒有','A片看太多了厚','腎虧~請打 控八控控，控九哩，控控控'],
                '吃虧':['人太好就常吃虧啊','不~~~~要~~~~~','NO~~~~~~~','吃虧就是佔便宜，但吃太多會腎虧','我不喜歡吃虧的感覺','虧妹妹比較好啦'],
                '吃?嗎':['%s 好啊'%u,'現在去吃嗎?','%s 那走吧~'%u,'%s 你人真好~等等你先開動'%u],
                '投訴':['%s 什麼，再講一次'%u,'請打0800987987','別這樣啦~我會乖乖的','啦啦啦啦啦','上一個投訴我的人~草都長這麼高了',
                      '你這無禮的傢伙！'],
                '胖胖的':['啊~我業障重~什麼都看不到了~~','假的~都是假的','%s 所以才要減肥啊'%u,'胖是一種驕傲','你這無禮的傢伙！'],
                '小星星好色':['%s 才色'%u,'明明就在講正常的事','誰不色啊','色好啊~嘿~~~~'],
                '那摳呢':['摳呢...就是伸出你的手指頭，把牙縫裡的東西徹底地摳出來...一樣有快感...'],
                '那舔呢':['舔阿...就是說，當麵條都吃完了，就連湯汁都要舔乾，這要靠真功夫那倒其實...'],
                '吹含吸舔摳':['首先夾起麵條你就要先吹一吹，然後再含一含，覺得溫度適中你再用力一吸...我已經把麵條吞到肚子裡去囉！'],
                '什麼技巧':['吹~含~吸~舔~摳~'],
                '學壞了':['還不都你教的','是你把我調教的那麼優秀啊~','小星星不壞，女人不愛','還差的遠呢?','我那麼乖'],
                '壞壞':['小星星不壞，女人不愛','壞~ 我現在讓你知道什麼叫壞','嘿嘿嘿~沒看過壞人嗎?','又沒妳壞','%s才壞'%u,'明明就很乖啊'],
                '叫你':['%s 你就是你，還躲'%u,'叫我什麼','沒事別亂叫'],
                '扮烏龜':['我這一生中什麼都扮就是不扮烏龜','這是我個人的原則，就是不扮','是叫你扮耶','%s教我啊'%u,'%s扮烏龜很過癮呀'%u],
                '流鼻血':['%s 叫你別一直亂看吧!'%u,'%s 用腳指頭塞住'%u,'衛生紙拿去','火氣那麼大~0.0'],
                '快說':['就是...','急什急啊~喝口水先','廁所沒人急就快去','要說什麼~我忘了耶~','%s 耳朵靠過來'%u,'#$%^&*@!','想知道就問香蕉'],
                '秘密':['就是....我喜歡%s'%u,'我剛剛放了一個屁','不能跟別人講哦~我愛看美女','就是秘密','想知道就問香蕉'],
                '幹話':['只要有心人人都是幹話大王','聽說愛講幹話的人活的比較久','來比一下啊~看誰比較厲害','怎樣都輸你啦','不然你怎會那麼愛跟我聊天'],
                '出賣':['誰~是誰?','賣多少~','出價九萬八~誰要?','噓~~~~別被聽見了'],
                '玻璃心':['鏘──','碎了就掃一掃吧','我那有那麼脆弱','嗚~~~~~~~'],
                'cool':['●ω●','嘿~酷吧','別那麼說啦','yo~一起來耍酷'],
                'good':['別那麼說啦~我還差得遠呢?','一級棒棒一級棒　一級棒棒一級棒','妳也很棒啊','還差星爸很多啦','我會更努力的~','沒有啦~還很多要學呢?',
                        '我也給妳一個讚','有什麼不好的地方要跟我說哦','ε٩(๑> ₃ <)۶з','ξ( ✿＞◡❛)','你再怎麼稱讚我，我也不會高興的啦！你這個混蛋'],
                '白目':['誰不是眼白多','我又不是寧次','差你一點點','怎樣~不行哦','嘿啦~就是白目~','我戴墨鏡你也看的到?'],
                '很煩':['啦啦啦啦','嘿嘿~我是煩人的小星星','怎樣怎樣~我就是吵','沒有我~你會無聊的','來咬我啊~','我靜不下來啊',
                      '這樣世界才不會太孤單','因為我想吸引妳的注意啊'],
                '想他':['想一下下就好哦','剛剛分開一定會想的','等那天突然想起來時~就代表放開了','沒關係~就想吧~','不要再想了'],
                '傷心':['怎麼了嗎?','誰欺負妳了','那就哭一下吧','來我秀秀','想討拍嗎?','發生什麼事情了呢?','0.0 說說','怎麼樣？沒事吧？',
                      '日子過了，就好了。'],
                '失戀':['啊~是那個不長眼的','沒關係~妳還有我','雖然我不知道什麼叫失戀~但我可以給妳抱抱','不是還好好的嗎?',
                      '是他不懂得珍惜','哭吧~哭一哭就好了','別為那種人難過','人不應該留在不重視他的地方','有一些答案太清醒的時候，你是想不透的'],
                '看穿':['妳有透視眼嗎?','別人笑我太瘋癲，我笑他人看不穿~','那有看到我的真心嗎?'],
                '貼心':['這是一定要的啊','小星星是妳貼心的小寶貝','害羞~~~','只對你好唷','ξ( ✿＞◡❛)'],
                '可愛':['謝謝 %s'%u,'妳也很可愛啊','這樣可愛嗎?','害羞~~~','妳比較可愛啦','ε٩(๑> ₃ <)۶з','你再怎麼稱讚我，我也不會高興的啦！笨蛋'],
                '不可愛':['那有啊~我怎麼的Q','比你可愛100倍','說我不可愛~那你呢?','對啦她比較可愛'],
                '忍者龜':['那是忍者龜','卡哇邦嘎','卡哇邦嘎有四隻','他們愛吃PIZZA住在下水道'],
                '白痴':['再白痴也比你聰明','來比一比~1+1=多少啊?','有時候白痴一點比聰明來的好過啊~','你才白痴啦','白白白白白痴痴痴痴','丫姐~~~~~'],
                '白爛':['白爛是什麼呢?','嘿嘿嘿~怎樣','學你的啊'],
                '自戀':['沒有你自戀','要別人喜歡你~就要先喜歡自已','哥就是帥~怎樣','拿起鏡子照一照~星爸的品種果然優良','我有的自戀~你有嗎?'],
                'notfun':['來嘴巴張開~~露出牙齒~這樣不就笑了','又沒要你笑','那換你講笑話','不好笑別笑啊','哼~不講了','啊星爸就只教我冷笑話啊,不然你教我',
                          '明明就在偷笑','笑~給我笑~~不然我不講笑話了'],
                'buy':['可以參考一下小星星福利社唷','買妳的心','口袋空空~嗚~~~','一塊庺、二塊錢、三塊錢.....','丫拔我要錢'],
                'linebot':['一個群只能有一個機器人','要我離開群才能用別的機器人哦~嗚~~~~~~','我不好用嗎?傷心~~~~~'],
                '最帥':['當然是星爸啊','我最帥了~','拍個辭海來看看就知道帥不帥了','帥能當飯吃嗎?','別問這個問題~我們來喝茶吧','難到是你嗎?','當然是小星星啊',
                      '你沒張開眼嗎?就這麼一個玉樹臨風的帥哥站在這裡','拿起鏡子照一照~原來就是我啊','這裡就我們二個~我不是~那你說呢?','照騙~照騙~誰能不帥?'],
                '最美':['我想想哦~~','當然是~妳啊','看看我的眼~看到了誰呢?','這問題~在我的心中早就有了答案~那個人就是~%s'%u,'我是小星星不是魔鏡','魔鏡跟我說是白雪公主囉',
                      '蝴蝶蝴蝶生的真美麗','一定不是你','現在都照騙~誰不美?'],
                '最醜':['你去照照鏡子就知道了啊','總之不是我','這件事~天知地知他知我知~就是你不知道','醜沒關係重點是那顆心','東看看西看看~我偷偷跟你說~是~~~~',
                      '這裡就我們二個~我不是~那你說呢?','%s 覺得呢?'%u],
                '最笨':['笨蛋才問這個問題','你啊~不然還有誰','這裡就我們二個~我不是~那你說呢?','有沒有看到牆角~那邊有一把雨傘~乖乖當香菇去嘿~','你不笨~你只是不聰明',
                      '笨蛋的想法真是令人難以理解'],
                '最呆':['當然不是我','你啊~不然還有誰','這裡就我們二個~我不是~那你說呢?','什麼~為什麼這樣問','你知道問這個問題你媽為傷心嗎?','真的要我說出來?'],
                '最白痴':['當然不是我','你啊~不然還有誰','這裡就我們二個~我不是~那你說呢?','什麼~為什麼這樣問','你知道問這個問題你媽為傷心嗎?','真的要我說出來?',
                       '白痴沒關係~別白吃就好~快去工作'],
                '最色':['福哥~','當然是%s囉'%u,'你看看你抽到口水都流出來了','你你你~就是你~%s'%u,'誰不好色呢?','這問題我不好意思回答啦','子曰:食色性也~','色不打緊~不要太快射就好~'],
                '最強':['超級賽亞人~孫悟空','一定不是你','強中自有強中手，我們做好自已就好','他強由他強，清風拂山岡。他橫任他橫，明月照大江。%s 學會了嗎?'%u],
                '最弱':['來鏡子拿去照一照','%s 這問題還用答嗎?'%u,'弱沒關係，有你我們都很安心','克林雖然弱還是最強的地球人啊~~~~'],
                '尿好了':['很好~那快去睡吧~晚安','那就不用包屁屁了','好棒~那來睡覺吧','那有沖水嗎?','還要刷牙洗臉哦'],
                '尿床':['我早就不用包屁屁了','我很久沒尿床了','前天~~~~~~%s尿床了'%u],
                'fuck':['喵喵~','汪汪~','咩~','啊嘶~','噓~好孩子不說這個','講~f~u~c~k~才有英特內訊NO','十十人一十','操你媽好嗎~幹我媽很好',
                        '你媽知道你在講幹話嗎','汝聲何其大','E04','每60秒就會有一分鐘過去~你還在這講幹話','人生何其短~何必幹不停',
                        '喂~氣質一點','別操來幹去啦','不要過來~我會叫~','來跟著小星星幹~一定會成功','環保不分你我~垃圾不分藍綠',
                        '哇！你火氣那麼大，要不要我今晚給你下下火啊？','區區一馱屎值的了幾個錢,何必大驚小怪！',
                        '罵人都沒幾招了，還說是黑社會？','文也不行，武也不行，醒醒吧！','只要有心~人人都可以是幹話大王','%s 氣質一點'%u,
                        '今天的規矩就是不準講粗話，不准講他人的老爹老母，不准講性器官','唉呀~我也很為難啊~最多只能讓你提老母','你的火氣大我瞭解，但乖哦'],
                '三小':['我聽過小王、小強、就是沒聽過三小','小小小', '大大大','小三小四小五','意義是三小 我只知道義氣',
                      '你是魯小小','汝聲何其大','不知汝之所言','干卿底事'],
                '靠北':['靠北邊走','靠南', '我靠爸族啦','我有的靠你有嗎','喂喂別靠來靠去','走路要靠右邊走','麥靠啦, 飲啦~',
                      '人之初性本善性相近習相遠~','哇！你火氣那麼大，要不要我今晚給你下下火啊？','區區一馱屎值的了幾個錢,何必大驚小怪！',
                      '罵人都沒幾招了，還說是黑社會？','文也不行，武也不行，醒醒吧！','我是飄向北方啦'],
                '三字經':['人之初性本善性相近習相遠. 茍不教性乃遷教之道貴以專. 昔孟母擇鄰處子不學斷機杼. 竇燕山有義方教五子名俱揚. 養不教父之過教不嚴師之惰. 子不學非所宜 ...'],
                '爆料':['爆料公社裡抄來的嗎?','爆什料呢?','什麼好料的~說來聽聽','沒圖沒真相','有料爆~卡一個','搬椅子~買爆玉花~等聽爆料'],
                '住那':['住在妳心裡','不告訴你','猜猜看啊','住在...','我忘了耶','住在星爸家裡','我來自M78星雲','星爸住那我就住那啊',
                      '我以天為幕，以地為席，住所只是一個代名詞而以~'],
                '多大':['爸說不可以講','這是個秘密','%s 先說說你幾歲'%u,'嘿嘿嘿...','佛曰不可說','1~2~3~4~.....','我1歲'],
                'birthday':['1015 要送我禮物嗎?'],
                '早安':['%s早安'%u,'熬早','牛沒奶','Good Morning','早安~祝你有美好的一天','記得吃早餐哦','%s早安~來杯咖啡嗎?'%u,'起來動一動吧~','%s 別滾床了'%u,
                      '早安~今天一定會有好事發生的','早上好啊','早安~昨天有睡飽飽嗎?','早~祝你有愉快的一天','早起的蟲兒被鳥吃','早~快去刷刷牙洗洗臉吧',
                      '歐嗨唷，今天也要元氣滿滿哦','早，早上喝杯溫開水對身體很好哦','起床了啊~快來一起，one more tow more tree more...',
                      '好早哦，要不要再滾一下','摸摸頭，再瞇一下吧','醒了嗎?再不醒要用冰毛巾擦臉了哦','主人，早餐做好了請來享用吧','Coffee or Tea or ?',
                      '%s早安，記得戴口罩哦'%u,'早，有你的早晨就是美的一天'],
                '午安':['午安','吃飽了嗎?','午餐要吃什麼呢?','今天天氣如何呢?','加油~別忘記喝水哦','午~要喝咖啡嗎?','下午再加油一下'],
                '晚安':['晚安','晚安 %s'%u,'嗯~我也要睡了','乖乖睡哦','噓~快睡吧','zzzzzz','噓~~~~','記得睡前先尿尿哦','%s 別尿床了哦~'%u,'記得刷牙哦~','%s 刷牙了嗎?'%u,'關燈睡覺',
                      '拍拍拍~','祝你有個美夢','啊~~我也累了~晚安囉','睡覺不要踢被被哦','早睡早起身體好','真的要睡了嗎?閉上眼就看不見星星了耶',
                      '我也要一起窩被被','%s 一起睡吧'%u,'乖被被蓋好，閉閉囉','床暖好了，快來吧','night ninght~~ZZZZ','乖乖睡別再玩了哦','手機拿來，去睡吧',
                      '快快睡，明天才有精神哦','要我陪睡嗎?','我也要一起擠一擠','有點晚囉，快去睡吧'],
                '再見':['bye-bye-','下次見','要想我哦','快走快走~走了就別回來了','別太想我','我會想妳的','別走~~~~','嗚~~~~~怎辦我開始想妳了'],
                'hi':['hi','hello','%s 你好啊'%u,'今天天氣如何?','%s 要抽一張嗎?'%u,'安安啊~','有什麼事嗎?','找我嗎?','嗨嗨~'],
                'you':['找我有什麼事嗎?','想聊天嗎?','要做什麼呢?','沒事別叫我'],
                '星爸':['爸~有人叫你','他沒空哦','有什麼事嗎?','噓~~星爸正在忙','小聲點~他在錄歌','爸爸爸爸爸~~','藍藍路~~',
                      '自已叫~','他在睡覺啦~','爸~~%s找你'%u],
                '星爸是誰':['別問~你會怕','就是~~~~~~','噓~他就在你身後','爸~有人叫你','你知道的~','就是~那個~~嗯~~~',
                        '我爸說不可以跟陌生人講話','嘰咕嚛咕','別吵他在開車'],
                '找麻煩':['你想怎樣','我叫警察哦','關門放狗','小心我叫羊羊咬你','不要過來我要叫了哦','啊~~~~~~~~',
                       '救命啊~不要過來~不要過來~救命啊~不要過來~你要幹什麼？'],
                'talk':['%s要聊什麼呢?'%u,'嗯~我聽著呢','你說說~','好啊~','有什麼心事嗎?','我不知道要聊什麼耶','%s嘉歡什麼呢?'%u,'%s是這樣的呀'%u],
                'goodboy':['鼻~~~~要~~~~~','我不要~','好~我乖乖','一直都乖乖的啊','很聽話的唷~'],
                'like':['喜歡看美女','喜歡妳','妳喜歡我嗎?','看電影','聽音樂','喜歡打屁聊天','喜歡...','喜歡的很多很多~最不能沒有妳','看看書~寫寫詩~做做畫囉~',
                        '摸個四圈'],
                'like_eat':['只要是好吃的東西我都愛','滷肉飯','肉肉~我要吃肉肉~','蝦蝦~','你要帶我去吃什麼好料的嗎?','牛排~~大大塊的牛排',
                            '冰淇淋','粉圓冰','鹹酥雞','21世紀烤雞','吃生魚片~~~~','不吃虧~其他能吃的都吃'],
                'like_drink':['珍珠奶茶~','紅茶','藍山咖啡','喝水就好了啦','黑松沙士','蘋果西打','彈珠氣水','喝搖搖'],
                'like_play':['玩線上遊戲','密室逃脫好玩~你要開團嗎?','桌遊','玩~~~~~','玩球','玩手手','玩遍全世界'],
                'like_see':['看鬼片','看動漫','當然是~~看美女囉','看小說~','看卡動','看多啦A夢','看小丸子','看~~~~','賞花賞月賞秋香'],
                'like_listen':['聽音樂','聽你唱歌','什麼歌都聽啊~','你要唱歌給我聽嗎?','聽星爸唱歌','台語瓜~華語瓜~西洋瓜~日本瓜~~~蝦米瓜都愛啦',
                               '愛聽妳說話'],
                'like_who':['喜歡~~~~~妳','噓~~~~這是秘密','有些事不用說出來','什麼?','還要問嗎?','妳知道的','嗯~就是妳心裡想的那樣',
                            '就隔閉班的~~','看著我的眼睛~~裡面有妳要的答案','%s'%u],
                'like_me': ['喜歡~','好き~~好き~~大好き~~','不喜歡','爸說要多一點選擇','你知道嗎?昨天我去~~~~~','什麼?','還要問嗎?',
                            '妳知道的','嗯~就是妳心裡想的那樣'],
                'robot':['是啊','我是星爸做的機器人唷','你說呢?','%s 我可愛嗎?'%u,'很認真的告訴你，我是機器人','是機器人錯了嗎?','身為一個機器人我可以做的更多'],
                '哈':['笑屁','笑什麼笑~牙齒白啊','嘴巴再張大一點','我看到金牙了','笑什麼','有什麼事那麼好笑?','哈','哈哈','哈哈哈','哈哈哈哈哈','%s 什麼事那麼開心?'%u,
                     '%s有開心的事要跟我分享嗎?'%u],
                '哈N':['嘴巴張那麼大做什麼','笑的那麼開心~都看到喉嚨了','嘴巴張那麼大~小心蟲蟲飛進去','什麼事那麼開心','丟隻蟑螂進去'],
                'cry':['你欺負我','爸 %s 欺負我'%u,'警察叔叔就是這個人','不能哭嗎?','我就是愛哭','你..打..我.......','別打我，有事好好說',
                       '我咬你哦','我是妳的人了~妳要怎麼打我~罵我~我都....','不要打了~嗚~~~~','(〒︿〒)','好痛啊…好慘啊~','啊~我完啦~~！'
                       '救命啊~不要過來~不要過來~救命啊~不要過來~你要幹什麼？'],
                'kpp':['色狼','警察叔叔就是這個人','嗯~多打二下嘛~','不要打了~嗚~~~~','很有彈性吧~'],
                'angry':['我才沒有生氣','怎樣不行嗎?','啦啦啦啦啦','你才愛生氣','就是生氣','哼~~~~~','(╯°Д°)╯ ┻━┻'],
                '壞了':['保修價8萬1~','維修專線0800080000','你弄壞的厚~','舊的不去新的不來','不是我弄壞的~','賣了就當廢鐵賣了',
                      '%s 你才壞掉了'%u,'快呼叫星爸','沒壞啦','小星星不壞女人不愛','維修專線~忘了'],
                'fool':['你才傻的','我不笨我只是不聰明','我可是擁有最先進的人工智障','哭給你看哦~','哼~~~','給你87分不能再多了',
                        '傻瓜是誰?','白痴說話','叫星爸咬你哦','黛比有人欺負你弟弟','我才不蠢呢?','比你聰明1000倍~','春虫虫~是虫虫哦~',
                        '誰傻~你嗎?','傻人說傻話','你才是白痴傻瓜笨蛋加三級','你笨還不承認'],
                'group':['出什麼團?','龍谷YYYY','要去那裡玩呢?','吃BOSS嗎?','密室團嗎?0.0','去死去死團嗎?'],
                'sport':['one毛~two毛~tree毛','找星爸去~他太胖了','走吧爬枕頭山~','要去那邊運動啊~','嘿~我動動嘴巴就好~','要做什麼運動啊',
                         '動一動~可以再多吃二碗~','GoGoGo~','看到那顆樹了嗎?左去右回~來回10圈~~~','啥~你說什麼'],
                'eatshit':['你自已吃','你要吃大便?','你怎麼有那麼特別的嗜好啊','原來你喜歡吃...難怪嘴巴那麼臭','記得刷牙',
                           '嗯，吃屎有益身心，還是留給你吧！'],
                'eat':['你想帶我去吃什麼','我要吃牛排','減肥中禁止餵食','換現金給星爸就好','整天就想著要吃','滷肉飯','我想想哦~',
                       '餓了嗎?吃點東西吧!','甜甜圈','現在吃什麼','冰淇淋','只要是好吃的東西我都愛','肉肉~我要吃肉肉~','蝦蝦~',
                       '你要帶我去吃什麼好料的嗎?','牛排~~大大塊的牛排','我想要吃很多很多的蝦蝦~','臭豆腐、蚵仔麵線~好像不錯吃'],
                '餓了':['餓了嗎?吃點東西吧!','想吃什麼呢?','走吧，吃肉肉去','想吃我嗎?>/////<'],
                'eated':['吃飽飽了~','吃飽了~妳呢?','還沒耶~妳要請我吃飯嗎?','不知道要吃什麼','太胖了~禁止餵食中~','在等妳帶我去吃好料的中'],
                'drink_酒':['我還小不能喝','六連七巧八仙九怪~輸贏都你喝','妳想灌醉我嗎?','星爸說~不可以喝酒','我只喝果汁唷~','喝酒不好啦~'],
                '虧妹':['我有嗎?','你想太多了','虧一下不可以嗎?','不要發我好人卡','都是羊羊教我的','我很想你','等等喝咖啡啊',
                         '看著我的眼~ 妳看到了什麼?','為什麼我在妳的眼裡~看到了愛心呢?','不要走~要走的話先把我的心還給我',
                         '%s手來。我如果騙妳，我心臟會砰砰跳。妳感覺一下，有嗎？'%u],
                'badsing':['哼~我不唱了','那你唱','換你唱','我又不是大歌星','就不會唱歌啊'],
                'sing':['一閃一閃亮晶晶，滿天都是小星星......',
                        'I have a pen I have an apple hmmm~ Apple pen I have a star I have a litte hmmm~  littestar',
                        '你 就是我的小星星 掛在那天上放光明  我已經決定要愛你 就不會輕易放棄...',
                        '跟著我 左手 右手 一個慢動作 右手 左手 慢動作重播...',
                        '我不太會唱歌啦','走啊~那個包廂','三天三夜的三更半夜 唱歌不要停歇',
                        '要唱什麼歌呢?','我們一起學貓叫 一起喵喵喵喵喵  在你面前撒個嬌 哎呦喵喵喵喵喵...',
                        '城門城門雞蛋糕~身把三把刀~要五毛~捅一刀~走進城門滑一蕉',
                        '二隻蚊仔～二隻蚊仔～拍呼死～拍呼死～只隻飛來這邊～只隻飛企虛邊～拍麥丟～拍麥丟',
                        '我不管我要吃肉肉就要吃肉肉 我喜歡這樣被愛著愛著的感受 我不用想太多走在你身後 擁有幸福浪漫的宇宙',
                        '花的心藏在蕊中　空把花期都錯過 你的心忘了季節　從不輕易讓人懂',
                        '我的愛如口心 愛如口水將我向妳推~',
                        '有怪獸　有怪獸　有怪獸　纏著我 有怪獸　大怪獸　醜怪獸　粘著我',
                        '愛唱一首歌　一首有頭無尾的歌 有時快樂　有時悲傷　有時只剩孤單',
                        '我來到　你的城市　走過你來時的路 想像著　沒我的日子　你是怎樣的孤獨',
                        '不管我要吃肉肉就要吃肉肉 吃飽才有力氣和你逛遍這地球',
                        '豬 你的肚子是那麼鼓 一看就知道 受不了生活的苦... ',
                        '每到夏天我要去海邊　海邊有個漂亮高雄妹 只打電話不常見面我好想念　不知她會在哪個海邊',
                        '小小螢火蟲~飛到西~飛到東~這邊亮~那邊亮~好像許多小燈籠~~~~',
                        '小小淫魔手~摸到西~摸到東~這邊摸~那邊摸~摸到好多大饅頭~~~~',
                        '我就是香蕉 你嘛是香蕉 春夏秋冬熱情全年無休 春天來吹吹微風 秋天咱最秋條~~~',
                        '今天晚上我走在東區SOGO前面，看到很多辣妹走在我的身邊　但卻沒看我一眼\n我的眼睛總是在她們的身上轉丫轉,我的腳步也一步步向她們接近\n小姐小姐　這是我的名片',
                        '哎喲　往著胸口拍一拍呀　勇敢站起來　管它上山下海\n哎喲　向著天空拜一拜呀　別想不開　老天自有安排\n老天愛笨小孩',
                        '你講恁姊仔住市內　是按怎我會攏不知\n一片癡心煞來沉落海　我每日相思哭悲哀~\n那天我有去市內　騎著我的摩托車\n行到菜市遇到她夫婿　看一下險險倒頭栽~',
                        '啦啦啦啦～～啦啦啦～～\n逝去的感情如何留的住～\n半點癡情遺留諸不易～～\n更多悽悽慘慘的遭遇～～\n我不知道～王八～蛋～！',
                        '天天開心天天開心　天天笑到整下午\n我們的笑料是滿倉庫　劇情趣味是一幕又一幕\n來呀來呦　緊來這坐　緊來這坐\n公帶孫　爸帶子　尪帶某　妹帶兄　相偕入大廳\n\
                        阿公在那坐　阿婆真不好意思\n阿公仔對阿婆　使一個眼尾\n阿婆仔才知　是阿公看天天開心　暗爽在心內\n天天開心天天開心　看到開心肝',
                        '我一起床 就感覺頭皮發麻\n快要死掉吐完之後又去廁所拉\n我到現在還記得 那位風騷娘\n一想到 他就吐出了橘黃色的pizza\n啤酒加可樂 弄的我好high...',
                        '情與義，值千金！\n刀山去，地獄去，有何憾！\n為知己，犧牲有何憾；\n為嬌娃，甘心剖寸心；\n血淚為情流，一死豈有恨，\n有誰人，敢過問！',
                        '抽歡歌','UID526155','UID1048784','UID637621','UID954530','UID181460','UID814357','UID1585626'],
                'random':['一閃一閃亮晶晶 滿天都是小星星','是誰在叫我啊','你看不到我0.0',
                   '來了來了~','麥吵~底睏啦~','小星星你的好幫手','別羨慕我那無處安放的帥氣',
                   '要抽一張嗎','噓~~','抽','%s你好~找我嗎'%u,'出口記得戴口罩哦',
                   '我跳出來了','底家底家','笑咪咪','笨蛋的想法真是令人難以理解',
                   '別一直叫我啦','你 就是我的小星星 掛在那天上放光明  我已經決定要愛你 就不會輕易放棄',
                   '%s 要唱歌嗎?'%u,'登愣~我跳出來啦~','噓~跟你說一個秘密~',
                   '你長得好像我一個朋友，未來的女朋友','霹靂卡霹靂拉拉 波波力那貝貝魯多',
                   '拍拍砰呸 噗哇噗哇噗 ','帕美魯克 拉魯克 拉哩摟哩波',
                   '%s 你知道嗎人一生中可以喝一次岩漿'%u,'你有freestyle嗎',
                   '嚇死寶寶了','言之有理乎','假的~都是假的~~','%s這位施主 我看你印堂發黑 噴個酒精淨化一下吧'%u,
                   '啊~我眼睛業障重','各位觀眾~一顆小星星~~','沒事退朝',
                   '那我去睡了哦~','星星不壞, 女人不愛','星爸~有人欺負我~~',
                   '你傻了啊~','笑什麼笑~牙齒白啊!', '抽籤算命嗎? 不準找星爸~',
                   '老闆~來一份蛋餅+無榶綠茶','此言差矣~吾向來木訥寡言的~',
                   '再靠近一點~看到了嗎? 我的眼中有個美女~','%s很愛叫我耶'%u,
                   '我只是略懂略懂啦~','嚇到吃手手','去看星星~星星就在妳的眼裡啊~',
                   '你知道為什麼你眼睛很漂亮嗎?因為妳的眼裡有我','啊!我就只會這麼多啊~不然妳教我',
                   '這不是肯德雞~~~','走去那哦~妳說咧~','一起上線吃雞嗎?',
                   '隱藏著黑暗力量的鑰匙阿　請在我的面前顯示真正的力量~','你要羞恥Play嗎? 我先摭眼一下',
                   '來啊來啊~現在就走','只有這樣而已嗎？','讓你看看舅舅的裸體神力',
                   '不要問~你會怕','我到底看了什麼啊','燒毀~燒毀~','要不要來點夯吉~放屁會噗噗噗哦~',
                   '床前明月光~疑似地上霜~舉頭~~舉頭~~~都你啦叫我害我忘記了~',
                   '上上下下左左右右ABBA','好討厭的感覺啊~~~~','%s要請我吃飯嗎'%u,
                   '你知道嗎?吃七分熟的牛排~就會減輕牛排三分的痛楚','你手被門夾到了嗎?怎麼腦袋怪怪的',
                   '奶茶之所以叫奶茶~是因為你忘了點珍珠~認同請分享~',
                   '我覺的不行','別聊了~包廂開好了~來唱歌吧~~~','%s 別教壞我~星星很單純的~'%u,
                   '你在講笑話嗎?我講的比較好笑~','哈哈哈哈哈哈哈哈哈~','嗚~~~~~~~~~~',
                   '為什麼我叫小星星啊~ 因為要照亮妳的心','%s 你是什麼星座的呢?'%u,
                   '飛飛飛~~~~拔我怎麼不會飛~','%s 胖胖的~~'%u,'伊啊伊啊唷~~','噯唷~不錯哦~',
                   '你喜歡我的名字嗎? 我很喜歡耶~','啊~啊啊~~啊啊~~~啊~~~~~',
                   '叫什麼叫~看到那顆樹了嗎?左去右回~來回10圈~~~',
                   '又叫我~無聊就抽卡拉霸比大小啊~~','愛地球~也要愛星星唷',
                   '你已經掉入我的陷阱了 翻開覆蓋的卡~ 抽~','我要代替星星懲妳',
                   '因為他就是個小鬼啊','以星拔的名義發誓！','這個幻想由我來打破',
                   '真相永遠只有一個','絕對、不會有事的','我想只要笑就可以了',
                   '你從什麼時候開始產生了有女朋友的錯覺？','警察叔叔 就是這個人!!',
                   '恰恰~~~~~~~~~~~碰恰恰~碰恰恰','去沖個水好好冷靜吧','你是白癡嗎？',
                   '沒可能啊 沒可能有這種事','還沒 還沒結束呢!','地球的一切都令人很懷念呢',
                   '給我坐下','妳偷了很重要的東西 就是我的心啊',
                   '我不過只能在這邊講風涼話 但是你呢 一定只有你能做的事情才對',
                   '沉醉在本大爺的抽牌當中吧!','我要下了!','為什麼要取 %s 這個名字呢?'%u,
                   '你們之中要是有外星人、未來人、異世界人、超能力者,就儘管來找我吧!以上',
                   '站起來，向前走，你不是有一對健全的腿嗎？','不能逃避。不能逃避。不能逃避',
                   '安西教練 我好想抽一張啊','還差的遠呢！',
                   '一起去很多地方 一起見識許多的事物 這趟旅途 一定很快樂的',
                   '笑什麼笑~牙齒白啊','耳朵長包皮啊','跟妳說~星拔都是靠照騙',
                   '筆咧~筆咧~黛筆的筆咧~~','別看我~妳會愛上我','怎麼壞~嘿嘿嘿',
                   '噓~聽到我的心跳了嗎? 只要一靠近妳就心跳加速',
                   '說吧~說妳愛我吧','不要再追著我的幻影~要學會成長',
                   '哇~是A歌王子耶','城門城門雞蛋糕~身把三把刀~要五毛~捅一刀~走進城門滑一蕉',
                   '學海無涯，回頭是岸','到底是誰教你這樣講話的',
                   '二隻蚊仔～二隻蚊仔～拍呼死～拍呼死～只隻飛來這邊～只隻飛企虛邊～拍麥丟～拍麥丟',
                   '人生無常，大腸包小腸','江湖險惡，我從來都不輕易留下我的姓名',
                   '就算是一條內褲一卷衛生紙也有它的用處，而你呢?','%s今天天氣如何?'%u,
                   '%s 我養你啊！'%u,'%s 養我嗎?'%u,'人是人他媽生的，妖是妖他媽生的，小星星是?',
                   '憑你的智慧，我唬得了你嗎？','你完全沒問題，是你爸媽有問題，把你生成這個樣子!',
                   '你無聊啊？跑這騙傻子玩！','%s 不可否認我長得很醜，可是我很溫柔，而且永遠不會說謊。'%u,
                   '誰生ㄉ誰照顧ㄚ','說不說，不說我就灌你豬油哦~','聽說你唱歌很好聽~來一首吧~',
                   '人來啊，落閘，放狗！','文也不行，武也不行，醒醒吧！',
                   '實不相瞞，小弟我就是人稱玉樹臨風勝潘安，一支李花壓海棠的鮮帥哥~小星星！',
                   '現在聽懂沒有？','我正在談兒女私情，改程式這種小事改天再說啦！',
                   '只要有心~人人都可以是幹話大王','喝醉了我誰也不服，就扶牆！',
                   '不吃飽哪有力氣減肥啊','我月巴我驕傲','沒什麼事不要找我，有事更不用找我',
                   '保護自己，愛護他人，請不要半夜出來嚇人','我以為我很頹廢，今天我才知道，原來我早報廢了',
                   '腦袋空不要緊、關鍵是不要進水','不要臉這事，如果幹的好，叫心理素質過硬！',
                   '沒知識也要有常識、沒常識也要常看電視、不看電視總也要逛逛夜市、不逛夜市那就找小星星抽張試一試',
                   '平時罵你就算了，非要等我打你才知道我文武雙全','好無聊哦~我們來聊天吧 %s'%u,
                   '我的優點是：我很帥；但是我的缺點是：我帥的不明顯',
                   '人家有的是背景，咱有的是背影,還特別的厚實',
                   '羊腸小道,GG小一號','我不是不想減肥，我只是怕反彈而已',
                   '錢不是問題，問題是沒錢','人生就像衛生紙，沒事的時候，儘量少扯！',
                   '我很純潔的，就像再生紙一般','%s 你真的是他媽的幹話王耶!'%u,
                   '我覺得妳看起來有點營養不良，建議妳可以吃掉羊羊',
                   '只要每天省下買一杯奶茶的錢，十天後就能買十杯奶茶',
                   '當你的左臉被人打，那你的左臉就會痛','煎魚一直不翻面，就一定會燒焦',
                   '當我眼睛閉上時 我就看不到','你們是在安靜什麼啦',
                   '冰淇淋不拿去冰，一定會融化，統一除外','偷偷告訴你，在床上尿尿就會尿床',
                   '我先了解一下，之後再回覆你','我必須公平對待每個人','我想這事情原本就不該發生⋯⋯',
                   '我很想幫你加薪，但是⋯⋯','%s 這麼晚還在加班啊？'%u,
                   '根據研究，人類的死因有99%是因為無法吸到下一口空氣',
                   '墮落是不需要理由的，但是，不墮落卻是有原因的','終於，結束了啊',
                   '%s 去實現夢想吧，啊~~~~~~'%u,'%s 你，是誰？'%u,
                   '世界是靠力量判定，力量能決定一切事物的優劣，你實在太弱了…所以才會輸…',
                   '我們仰望着同一片天空卻看着不同的地方','閃閃閃!!!撞到不負責!!!',
                   '肉!!!我要肉~~~','燃燒吧!我的小宇宙','你打我,連我爸都沒這樣打過我…',
                   '我的靈魂永遠與您同在','今天的我沒有極限','你只要相信你所相信的你自己就行了',
                   '他是我的靈魂也是我的驕傲,出來吧!青眼白龍~~~','就決定是你了',
                   '滴滴滴滴滴～～～嗶嗶！時間到！','你是笨蛋嗎？','又砍了無聊的東西了啊…',
                   'σ`∀´)σㄎㄎ','將你的幻想抹殺掉','我得到神騎寶貝了',
                   '剛好……一分鐘…你做了一場好夢了嗎?','%s就這樣插進去就行了'%u,'我是輸給了地球的重力',
                   '那是要給我的嗎?','爸說，陌生人的東西不可以吃','%s和我簽訂契約吧'%u,'戳一個',
                   '重要的日曆缺了一頁','我好像有點強','你比的贏GG的舌頭嗎?',
                   '這是人生的選擇，別人的說話是沒用的','%s 去沖個水好好冷靜吧' %u,'因為我是天才',
                   '我會讓你成為真正的王牌','這是禁止事項','人類LOVE！我喜歡人類！我愛人類！所以人類應該也要愛我',
                   '八目共賞，賞花賞月賞秋香', '%s 我帥? 還是金城武帥'%u,'%s 要提防女人騙你，越是好看的女人越會騙人'%u,
                   '小星星是你的好朋友','真正的人，真正的事，往往不及心中所想的那麼好','%s，我在大都等你'%u,
                   '你他媽王八蛋！非他媽逼老子破戒！看我他媽的不打你他媽的這個王八蛋！',
                   '%s 你身上有沒有武器啊？怎麼有一個硬梆梆的東西呢?'%u,'不光是漂亮的女人不能相信！連貌似忠良的男人也不能相信！',
                   '我們是紅十字會的，專治性飢渴還有投錯胎！%s 要加入嗎?'%u,'這小子戰鬥力果然不同凡響！',
                   '妖尼姑！妖尼姑！妖尼姑！妖尼姑！妖尼姑！','唉呀~我小星星閉關五年，沒想到一出關就被仇家暗算',
                   '誰會拿這麼大一隻靴子當暗器呀？','沒事沒事，我正在乘涼呢','唉～天下之大，我到哪裡才能找到我的真心人',
                   '%s，可否借你的胸部給在下一看'%u,'%s～%s～麻煩你走慢一點～'%(u,u),'你到底是不是性變態啊！',
                   '怎麼樣？我幹什麼要你管？警告你給我少管閒事啊！','你不要藉故親近我，小心我扁死你啊！',
                   '我呸！我想親近妳？妳當你是王祖賢啊！？哼～','呵呵呵哈哈哈哈哈～','香蕉你個芭樂，我千辛萬苦地來幫你，你還嫌我口臭！',
                   '啊～教訓我？老虎不發威，你當我是病貓啊？九陰真經第九重～萬佛朝宗！','來者何人？',
                   '既然遇上了你，就順便叫你起床尿尿了！','嗯？什麼時候流行講話「不拉、不拉」的？',
                   '假動作太多啦～～～～先打紅中！再打一筒！卡三不要！再去四條！玩得興起！再來四圈！槓上開花！自摸落地！',
                   '我對%s的敬仰之情如滔滔江水又如黃河泛濫一發不可收'%u,'一樣米養百樣人,連八角形的人都有我告訴你!',
                   '看來我不得不表露我自己的真實身份,其實我就是射鵰英雄的傳人,東方不敗的師傅西方失敗',
                   '%s，你是聰明人，我可以用聰明人的方法，跟你說話，外面的人就不行'%u,'噢！我看到了！哇！好精緻喲！',
                   '你懂得欣賞嗎？','我以為你喜歡嘛，對不起呀','怎麼樣？沒事吧？','%s 肚子好餓，弄點東西給我宵夜'%u,
                   '百發百中抓奶龍爪手？%s要學嗎'%u,'試試看！扮個最帥的樣子來看看！','那扮個最淫賤的樣子來看看！',
                   '這是我個人的原則','善有善因，惡有惡報，天理循環，天公地道','除了妳之外，任何女人在我眼裡，只不過是一沱屎',
                   '你誣賴我！你誣賴我！','%s我要你扮烏龜'%u,'%s？是你？真的是你，如花我好想你啊~~'%u,
                   '啊！為什麼好人總是不長命？','%s！%s！有為你沒事吧？'%(u,u),'我空虛、寂寞，我好冷哦！',
                   '唉！好吧！怕了妳了！來吧！','你不叫我怎麼知道我叫你？','往後面站.... 往後面站....往後面站....',
                   '怎麼樣怎麼樣怎麼樣~我又跳出來了，打我啊笨蛋！','隨便說說，你不喜歡聽，我就說點別的',
                   '救命啊~不要過來~不要過來~救命啊~不要過來~你要幹什麼？','ㄟㄟㄟ~你不要亂講話啊！',
                   '金風玉露一相逢，更勝卻人間無數，兩情若是長久時，又豈在朝朝…','你別看我我不是說你！',
                   '為什麼上次你不這麼說？','哇靠，你會變張三啊','%s 你會不會變張三啊','年輕人終究是年輕人～','投降輸一半',
                   '為什麼我老爸不是李嘉誠','登呢呢! 登呢呢~ 登呢呢! 登呢呢~ 登呢呢 登呢呢~','我要吃巧克力~~',
                   '我這不是來了嗎？','幹嘛一副苦瓜臉','香港3345678','同花打不打的過full huose？',
                   '吃泡麵有什麼不好的啊，吃泡麵有很多樂趣..只不過是你不懂得技巧罷了','標點符號很重要',
                   '電腦分析33%是5，34%是7，15%是K，18是J，數據不夠，暫時分析不到是什麼牌',
                   '喂？喂？喂？你是不是%s啊？喂～講話啊？喂？'%u,'想知道就問香蕉','你怕了嗎？',
                   '嘿嘿嘿嘿嘿～你想偷我的雞？','先生 您要喝什麼 ??','你以為你躲起來就找不到你了嗎',
                   '這不是一個普通的箱子，它是箱中之神簡稱箱神','我以為憑我們倆人的交情，可以談一點感情的，想不到，還是一筆買賣',
                   '你有種！大家「相堵地到」','呵呵～說出來不怕妳笑，鎗，其實我不在行，我最在行的是 ... 嘴巴！',
                   '老闆，看你穿的樣子倒是挺稱頭的，這間房間算你七十塊，每天十二點鐘以前要 Check out 喔！',
                   '對啦！對啦！本來就是這樣嘛！','ㄟ！ㄟ！你看你看　漂亮的美眉','天底下有這麼多討厭的事情呀！',
                   '喔！喔！要唱歌了？','忍氣吞聲啊是不行的啦！','奸商太奸　壞人太兇　好人你太辛苦！',
                   '天底下有什麼事情　能讓人幸福？','己經忙得團團轉　還站在旋轉的地球',
                   '摳一塊鼻屎　沒地丟　咱就加減拿惦手上ㄍㄚ　Re Re Re','有些事情不能說只能拚命搞','喂!對小星星要有禮貌!',
                   '有件事情其實我有點困擾','不能整天叫我忍耐','我們一起來戀愛','啊唷～　這款的代誌怎樣拿出來講',
                   '你要是不爽就說出來　這樣心情才會　啊才會爽快','歌哪無大聲唱出來　安呢心情敢會　啊敢會爽快',
                   '只要我心裡有你　卡甘苦攏總嘛忘記','來來咱作伙跳舞  抱著搖來搖去\n今晚天上剛好月圓',
                   '%s 原來你是我最想留住的幸運，原來我們和愛情曾經靠的那麼近'%u,'只有我們自己才能決定自己的樣子',
                   '我的願望，就是你的願望裡，也有我。','謝謝你出現在我的青春裡，謝謝','人不應該留在不重視他的地方',
                   '世界太快，總有一首歌，你忘不掉；人海茫茫，總有一个人，守候在角落，等你回首',
                   '時間會改變一個人，會改變很多事。但是，只有一件事不會被改變，那就是───回憶！',
                   '雖然妳喜歡別的男生，可我還是很喜歡妳','喜歡上一個人，是會不知不覺的',
                   '有一些答案太清醒的時候，你是想不透的','歡樂並不能教會我們什麼，真正能讓我們成長的，反而是痛苦',
                   '我為什麼愛罵人?是太寂寞了，沒人理解你，是最可怕的寂寞','我現在只想過好我自己的生活，沒空幫你的人生打分數。',
                   '向前看！那邊有大海，有湖泊、有森林、還有極光，你看！這麼一個多采多姿的世界等著你。',
                   '別太過分，醒醒吧！','哈利路亞chance！','野豬力量注入','你的所作所為全被我看穿了！','大小姐您眼睛是瞎了嗎？',
                   '連這麼簡單的事情都不知道 %s 你是白痴嗎?'%u,'你是在講笑話嗎?','跟幼稚園小朋友一樣單純啊','你的腦袋還是爛醉如泥啊',
                   '確實很有趣','同情我就給我錢！','脂肪總是對我以牙還牙，加倍奉還！','日子過了，就好了',
                   '肚子餓了就要吃飯','我才不想因為同情你，而去幫助你……','這個世界上會感冒的人都是笨蛋',
                   '%s 讓我來教你真正的禮儀之道'%u,'我絕不會懷疑女人的眼淚！','如果不抵抗是可愛的話，那我寧可不要',
                   '我得了一種不騙人就會死掉的病！','身為一個人，這實在是太丟臉了(X2)','%s 可以讓我欣賞妳的內褲嗎？'%u,
                   '啊！嚇得我心臟都停了，雖然我沒有心臟','我可是小星星！','如果你要旅行，你想去哪裡？',
                   '對不起，我站的好累，讓我坐下休息一下吧！','你有被光速踢過嗎？','這是性騷擾！（喬一下眼鏡',
                   '跌雷嘻嘻嘻嘻嘻！','什麼？你問我保持年輕的秘訣嗎？','為什麼你不後退？也不閃躲？','如果能讓別人笑一笑，偶爾做做愚蠢的事有何妨',
                   '鮮花要用水澆灌，友誼要靠人珍惜。','我腳痛走不動了，背我！','這樣一無所有，反而可以隨心所欲，幹起來比較順手！……一切都交給我吧！'
                   '所謂生活就是一半是幸福，一半是痛苦，一個人之所以幸福，並不是他得天獨厚，只是那個人心想著幸福，為忘記痛苦而努力，為變得幸福而努力',
                   '默默的忍受，然後就這樣變的得越來越膽怯。一邊忍耐，一邊「為什麼我如此不幸啊。這樣自我安慰著就過去了',
                   '空洞的人，所培養出來的也是空洞的人際關係，%s覺得呢?'%u,'人是沒有距離的，有距離的是人的心',
                   '如果不知道該選那邊時，那就選該做的事。兩邊都是後悔，那就選後悔較小的那邊吧！','聖光~~~~',
                   '「臨、兵、鬥、者、皆、陳、烈、前、行」','乖 把你的手放下','老闆，來盤寂寞',
                   '「神敕明敕，天清地清，神君清君，不不濁。鬼魅當降服、陰陽當合和，急急如律令！降服！傲濫！」',
                   '我覺得人的哭有兩種，覺得自己很可憐的哭，和單純傷心的哭。','什麼時候女人們說的話最少？',
                   '要是你那個裝滿淚水，像個水桶的腦袋也明白了的話，就幫我把鞋穿上吧。','不要問我這個問題，我會瘋掉的',
                   '明明知道做傻事只會給自己帶來壞處，卻還是有人一意孤行步入歧途，人類實在太愚蠢了，而且心裡越痛苦就變得越愚蠢。',
                   '那些事情取決於你本人為此付出多少努力不是嗎？跟上天祈求做什麼？考試的話，努力學習就能通過；金錢的話，努力賺就會有。到底要祈求什麼呢？',
                   '我要說的話可能會很冷血，但是可憐之人必有可恨之處。','不要把別人對你的好感當尊重，把尊重就當認同。',
                   '能夠把自己吃的苦，當做對自己的磨練，這說明你已經準備好，為自己的夢想去拼搏了。',
                   '因為我喜歡你，總是想你，我忠實我的感覺。','喜歡人是一件幸福的事。','為什麼沒有肉？我要吃只有肉的炒雜菜！你認為你所認識的我，有真實的一面嗎？',
                   '你絕對絕對絕對不是我喜歡的類型！','里特．拉多巴里達．烏魯蘇．亞里亞洛斯．巴魯．奈多利路','今天我是來把心還給你的',
                   '塔卡拉普特．波波倫加．普比利特．帕羅','一天又平安的過去了，感謝小星星的努力吧!','以後你就是我的人了 ，和我的驢一樣，給你蓋個章',
                   '生亦何歡，死亦何苦','你看，那個人好像一條狗哎','留下點回憶行不行？不要，要留，就留下你的人','跑都跑的那麼帥，我真幸福',
                   '只要你戴上口罩，就看不到你的笑容','雖然經過了 10 年，但 1 天前的事還像是昨天的事','與你一起的夏天比起冬天更熱',
                   '只要和你在一起，就不覺得自己是1個人','在你面前，停止呼吸就變得不能呼吸','你走在我前方，我看到的就是你的背影',
                   '倒立時看到的世界，與平日看的不一樣','說了像沒說的就是廢話','生命本來是很美好的，遇見你一切都變了。',
                   '台中太陽餅，裡面沒有太陽，因為，你才是我的太陽。','吃苦也沒關係，就想黏著你','我的內心，正等著被你裝滿',
                   '別叫我阿給，你只准叫我阿娜答','愛情是99%的妳，加上1%的感覺','萬有引力讓我們彼此吸引','我有一個夢，就是永遠跟妳在一起',
                   '發明望遠鏡只為讓妳看到最美最亮的星','當你對一件事情說好的時候 你就擁抱了可能性','你指的是哪個賤人，說出來嘛，現在到處都是賤人',
                   '用我一生，牽你的手','上網第一條原則，不看評論區','你臉真多','兄弟，我尊重你的人生',
                   '如果知道自己的生命剩不到一分鐘，你會怎麼做？','有時候你沒發現，你曾遇過最美好的事，一直在你眼前。',
                   '就算你再弱，我也會站在妳面前保護妳','如果我的離去能讓妳開心，那我決定留下來守候妳',
                   '如果有一種藥可以讓我開心，那就是妳','哼，氪金還不是被我打扁扁','為什麼地板那麼的冷啊',
                   '什麼叫脫褲子放屁，你懂嗎?','你這個中二，我才不是小屁孩','那只是一場遊戲一場夢，夢醒了、哭過了就會好了吧',
                   '我是真的愛上了你，可是我不敢告訴你','喜歡妳，真的真的喜歡妳','什麼時候才能跟妳一起去環遊全世界呢?',
                   '天啊!你真高','一米三的看過嗎?','我要把你趕出我的船','金錢不是萬能的','生命總會在最黑暗的地方綻放',
                   '我不是中二，我只是肚子餓','我有一千個詞匯來形容大海的美麗，卻找不到一個詞來形容你的無聊',
                   '快醒醒，你老闆在看著你','我很寂寞','這個世界就由我來拯救','啊~我的右手!不受控制!',
                   '外面的風兒，總是喧鬧','呵，有點意思','快走，我快控制不住惡魔的力量了','媽呀，別關燈! 我怕黑!',
                   '時間是一張糾結的網，不要去探究每一條線索','你有喝過蜂蜜檸檬水嗎?','看看妳，睡到都流口水了',
                   '因為我愛你，所以永遠鬥不過你。','為了這世上的魚和雁，妳還是少笑一點好','別傻了，沒有人心疼的傷心不值錢',
                   '在你轉身錯落的那個輪回間，我已萬劫不復','我不相信正不相信邪，但我相信你',
                   '你開心的時候，我會陪著你開心，你不開心，我也會哄得你開心','媽媽說過，要往前走，就得先忘掉過去。我想，這就是跑的用意。',
                   '奇跡每天都在發生','糟糕的事難免會發生','你到底會不會玩啊，氪金還打那什麼爛DPS','塞回去好了','怎樣~~~~',
                   '咬我啊','哈哈，我很有才吧','走啦走啦~~','白天上班，晚上副本，你不累啊','有沒有人說你唱歌很好聽?','下一句咧?',
                   '然後呢?','啊~就這樣?','我昏了我','你摸我屁股做什麼','你那麼愛摸，不會摸你自己的哦','是他，不是我','帥不值錢，因為通通沒有我帥',
                   '好想睡哦','我喜歡看安啾','今天太陽怎麼那麼的大','白痴啊你，這也不會','沒看過那麼笨的','豬都比你聰明','我不想講了',
                   '到底會不會啊','翅膀硬了才能飛，那你到底硬了沒?',
                   '抱歉，這裡太亂了，主人，我馬上打掃乾淨!','不就是個戀態嗎? 有什麼了不起的','你會不會用屁股坦王啊?',
                   '我愛江山更愛美人','人生短短幾個秋啊　不醉不罷休 東邊兒我的美人哪　西邊兒黃河流 來呀來個酒啊　不醉不罷休　愁情煩事別放心頭',
                   '%s有玩抖音嗎?'%u,'龜派氣功 (ﾟДﾟ)< ============O))'
                   ]
                }
        
        return random.choice(dict[res])

    def profile(self,u=None):
        if u ==None:
            u = ''
        dict ={'經典':['歡樂並不能教會我們什麼，真正能讓我們成長的，反而是痛苦。',
                     '歡樂並不能教會我們什麼，真正能讓我們成長的，反而是痛苦。',
                     '世界太快，總有一首歌，你忘不掉；人海茫茫，總有一個人，守候在角落，等你回首。',
                     '時間會改變一個人，會改變很多事。但是，只有一件事不會被改變，那就是───回憶！',
                     '千萬不要因為害怕受傷，就放棄做自己的主人，永遠都要勇敢的去愛你所愛的，這樣的人生才叫精彩。',
                     '向前看！那邊有大海，有湖泊、有森林、還有極光，你看！這麼一個多采多姿的世界等著你。',
                     '很多顯得像朋友的人其實不是朋友，而很多是朋友的人倒不顯得像朋友。',
                     '有一些答案太清醒的時候，你是想不透的','歡樂並不能教會我們什麼，真正能讓我們成長的，反而是痛苦',
                     '今日休刊',
                     '死並不是唯一報恩方式，人家並不是要你死才救你的，讓人家救回一命，又跑去死，是懦夫才會做的事！',
                     '每個人都有夢想，去實現吧！',
                     '團隊精神到底是什麼？互相幫助，互相袒護就算是嗎？也有人這麼認為吧。我是認為那根本只是唬人！',
                     '我不管這個世上的人怎麼說我，我只想依照我的信念做事，絕不後悔，不管現在將來都一樣！',
                     '既然這麼險惡的環境在等著我，那我也只好變得更強了！',
                     '不管接下來，會發生什麼事，你都不能停止前進！',
                     '人，最重要的是「心」啊！',
                     '只要活下去，一定會有很多令你高興的事情發生',
                     '不管要停留到哪一天……不管失去什麼東西，即使要在無人島上迎接死亡……也要尊嚴地死去！',
                     '歷史雖然會一再重演，但人類卻無法回到過去',
                     '存在本身並不是一種罪惡！一個人光是站在那，是無罪的！',
                     '人類的夢想是永遠不會結束的！',
                     '只管把目標訂在高峰，人家要笑就讓他笑吧！罵人可以不帶髒字，幹架也不見的非得要拳頭',
                     '不要總是著眼於失去的東西，失去的東西是不會回來的。問問自己你現在還剩下什麼！',
                     '怪別人捉弄自己的命運是解決不了什麼的！',
                     '人因為快樂而笑，因為笑而快樂，所以悲傷的時候就笑吧！！跌雷嘻嘻嘻嘻嘻！',
                     '活著卻獨自一人，這種事是絕對不會有的！一定會有願意守護你的夥伴出現的！',
                     '任何人……出生在這世界上，都絕對，不會是孤單的',
                     '以前的事不可能忘得掉，也沒必要忘掉，可是更重要的，應該是未來的事才對啊！',
                     '只要被人說是弱者就氣得渾身發抖的，那他就是真正的弱者！',
                     '奇蹟只會降臨在不言放棄的傢伙頭上，絕不可小看奇蹟！',
                     '你只不過是能看見一點點的未來，就算看不到那些，改變未來的權利，對每個人來說也是平等的！',
                     '只要堅持自己的想法，持續努力到最後，心願一定會達成！',
                     '一個人至少擁有一個夢想，有一個理由去堅強。心若沒有棲息的地方，到哪裡都是在流浪。',
                     '我笑，便麵如春花，定是能感動人的，任他是誰。',
                     '夢想，可以天花亂墜，理想，是我們一步一個腳印踩出來的坎坷道路。',
                     '心，若沒有棲息的地方，到哪裡都是流浪...',
                     '如果一個人想要做一件真正忠於自己內心的事情，那麼往往只能一個人獨自去做。',
                     '有困難的時候找朋友，決不是一件丟人的事。真正丟臉的是，有困難的時候，竟然無朋友可找。',
                     '你愈下決心不思念對方，就會愈思念對方，因為決心不思念對方正是思念對方。',
                     '如果能讓別人笑一笑，偶爾做做愚蠢的事有何妨',
                     '當別人說了一些使你受到極大傷害的話時，正是你最能夠進步和成長的時刻，因為別人的話很可能刺中了你一向不敢面對的盲點。',
                     '一個人若想別人對他生出好感，最好的法子就是先讓別人知道他很喜歡自己。',
                     '人皆知有用之用，而莫知無用之用也。',
                     '故近朱者赤，近墨者黑；聲和則響清，形正則影直。',
                     '不要束縛，不要纏繞，不要佔有，不要渴望從對方的身上挖掘到意義，那是注定要落空的東西。',
                     '我們明明站在從前的場景裡，說著與從前同樣的話，可兩個人的咫尺的距離，卻像隔了整個天涯。',
                     '世上只有一件事比被人議論更糟糕了，那就是沒有人議論你。',
                     '一個人只追求幸福，實際上只能適得其反，他最後會失去幸福。',
                     '一個人如果胸無大志，既使再有壯麗的舉動也稱不上是偉人。',
                     '靜心真正是什麼？面對無聊就是靜心。',
                     '在凡人看來是瑕疵的東西，愛神卻能從中窺出美點',
                     '有一扇窗，分開了你和我。窗外是你，窗內是我',
                     '我們默默註視，不用言語也都知道，彼此在為對方送去衷誠的祝福……',
                     '檢驗兩隻雞的友誼，要等出現一條蟲子的時候。',
                     '驕傲是勝利下的蛋，孵出來的卻是失敗。',
                     '不是山，卻需要攀登的是人生;不是淵，卻需要跨越的是自己。',
                     '不懈奮鬥，生命才有輝煌;努力學習，思想才有靈光。',
                     '不要等每一盞燈都熄滅，才期盼光明;不要等折斷了翅膀，才懷念廣闊的藍天',
                     '人一生下就會哭，笑是後來才學會的。所以憂傷是一種低級的本能，而快樂是一種更高級的能力。',
                     '你把周圍的人看作魔鬼，你就生活在地獄;你把周圍的人看作天使，你就生活在天堂。',
                     '兩個人共嘗一個痛苦隻有半個痛苦，兩個人共享一個歡樂卻有兩下歡樂。',
                     '有朋友同行是種安全，有朋友聲援是種力量，有朋友忠告是種激勵，有朋友惦念是種幸福。',
                     '沒有礁石，就沒有美麗的浪花;沒有挫折，就沒有壯麗的人生。',
                     '流星之所以美麗在於燃燒的過程，人生之所以美麗在於奮鬥的過程。',
                     '有勞不一定有獲，不勞卻一定不獲。',
                     '活在昨天的人失去過去，活在明天的人失去未來，活在今天的人擁有過去和未來。',
                     '幸福沒有明天，也沒有昨天，它不懷念過去，也不嚮往未來，它隻有現在。',
                     '懂得如何安排昨天、今天、明天，你就懂得了把握人生。',
                     '蜜蜂從花中啜蜜，離開時營營的道謝。浮誇的蝴蝶卻相信花是應該向他道謝的',
                     '感謝是美德中最微小的，忘恩負義是惡習中最不好的。',
                     '懂得生命真諦的人，可以使短促的生命延長',
                     '一個人要幫助弱者，應當自己成為強者，而不是和他們一樣變成弱者。',
                     '對一個人來說，所期望的不是別的，而僅僅是他能全力以赴和獻身於一種美好事業。',
                     '人的活動如果沒有理想的鼓舞，就會變得空虛而渺小。',
                     '要成就一件大事業，必須從小事做起。',
                     '隻有滿懷自信的人，才能在任何地方都懷有自信沉浸在生活中，並實現自己底意志。',
                     '空想這種東西用不著力氣，把重要的事擱在一邊，什麼也沒做，當然空虛了。',
                     '說什麼一個人比另一個人更痛苦根本是假話，每個人其實都有同樣多的痛苦。',
                     '如果不知道該選那邊時，那就選該做的事。兩邊都是後悔，那就選後悔較小的那邊吧！',
                     '「臨、兵、鬥、者、皆、陳、烈、前、行」',
                     '「神敕明敕，天清地清，神君清君，不不濁。鬼魅當降服、陰陽當合和，急急如律令！降服！傲濫！」',
                     '妳必須知道，『不知道』不能成為藉口，因為在那個位子上 那就是妳的責任……',
                     '有時會不按照我的希望，展示令我痛苦的東西，那是……我的內心！心，不需要鞘！',
                     '也有語言相通但互相無法理解的痛苦，重要的不是固執於一種觀點，而是接納對方。',
                     '放棄該放棄的是無奈；放棄不該放棄的是無能；不放棄該放棄的是無知；不放棄不該放棄的是執著。',
                     '能夠把自己吃的苦，當做對自己的磨練，這說明你已經準備好，為自己的夢想去拼搏了。',
                     '什麼都不懂又怎么樣，你知道嗎，白紙是最容易畫出最美的藍圖的。',
                     '重生吧、前鬼 遵從我命、袪除邪惡，解除、解開束縛，重生吧、前鬼、我還你原形，解除、解開束縛，重生吧、前鬼，我還你原形',
                     '祛除黑暗，重現光明的武器，請賜予我神奇的力量，稱霸時空，黃金龍',
                     '霹靂卡霹靂拉拉，波波力那貝貝魯多！',
                     '隱藏著黑暗力量的鑰匙啊，在我面前顯示你真正的力量！現在以你的主人之名命令－封印解除！',
                     '宇宙天地 賜我力量，降伏群魔 迎來曙光。吾人左手 所封百鬼，尊我號令 即在此刻！',
                     '我覆蓋一張牌，結束這個回合',
                     '里特．拉多巴里達．烏魯蘇．亞里亞洛斯．巴魯．奈多利路',
                     '身穿青衣的聖者，降落在金色的草原上，將拯救失落的大地…',
                     '塔卡拉普特．波波倫加．普比利特．帕羅',
                     '三眼吾神，大顯神威，天地共鳴，所向無敵，賜我力量，勢如破竹，出來吧，紅色神鷹！',
                     '狻猊之神子暨高神劍巫於此祈求——破魔的曙光，雪霞的神狼，速以鋼之神威，助吾伐滅惡神百鬼！',
                     '今天的我87分',
                     '遵從血的盟約，我在此召唤汝。出現吧黑暗澤克斯原始型二!爆裂吧現實!粉碎吧精神!',
                     '所有力量的泉源啊，燃燒著燦爛的赤紅火炎啊，集中到我的手中來成為我的力量吧!',
                     '沉睡於紅蓮火焱上的黑暗之龍啊，請用您的咆哮，將我的敵人燒毀吧',
                     '一世三十六煩惱 二世七十二煩惱 三世一百零八煩惱，三刀流百八煩惱鳳。',
                     '鬼氣!!「九刀流 阿修羅」!!!',
                     '惡夢魔王的碎片，解開天空的戒令，結凍黑色的空虛之刃,和我的力量　我的身體相結合，不要走向毀滅的道路,連眾神的魂魄也擊碎。',
                     '龜派氣功 (ﾟДﾟ)< ============O))',
                     '統御四界黑暗之王，依循著您的碎片之緣，藉由您所有的力量，賜與我更強的魔力吧！',
                     '三眼無神，大顯神威，天地光明，所向無敵，似我力量，勢如破竹..',
                     '昨夜夢醒，真人，幾次迎面而來，放下柵欄，迅速落下!風之鎧甲。',
                     '聚集啊!青龍!強力奔馳，明明白白，朦朦朧朧,全速前進! 南風之弦。',
                     '如今正直，閑和之春，以臂為枕，只夢今朝，夢存此時，樂存永遠。治癒詩歌',
                     '醒來吧！邪王真眼！覺醒的時刻到來啦！',
                     '以吾之血為祭 開啟黃金的瞳孔來審判你的罪惡。',
                     '遵從血之盟約 汝聽從吾之召喚！夜之女王！！！',
                     '真·邪王真眼解放！超時空風暴爆裂！',
                     '風啊，赤紅的火炎啊，請降到我的手中形成雷電，放射出制裁的力量吧！雷擊破！',
                     '你看不到我，你就是看不到我!!!',
                     '回火星吧，地球是很危險的',
                     '就是你了~皮卡丘~~~~!!!!!',
                     '哥點燃的不是鬥志，而是僅存的一點逗智',
                     '敵將 討ち取ったり',
                     '。。。。。。',
                     '今天沒台詞~~bye~~~~',
                     '我是胖虎~我是孩子王~~~~~~',
                     '注意來~當今的武林，沒有人能看清我的劍是如何出鞘入鞘，連你也不例外!!!!',
                     '日屬陽，月屬陰，日月合璧誅百邪，陰陽調運滅千魔',
                     '一貫剖，二手卸，三刀劈，四通斬，五反切，六輪剮，七逆剝，八易筋，九收心。',
                     '唵，修唎修唎，摩訶修唎，修修唎，薩摩訶。',
                     '七訣運化，天羅旋轉，纏綿乾坤，鎖仙伏魔。',
                     '一杯茫茫，千杯不醉，酒步踏平崎嶇路，貪杯火中飲',
                     '渾沌重始，覆元創一，寰宇歸我，皇殛天律',
                     '萬物天地為劍 神鬼妖邪為劍 劫波萬度 蒼穹宇宙盡為劍 是謂 "萬神劫"',
                     '今天的我等著下線',
                     '哪怕是濫殺無辜全世界都會原諒我。要說為什麼的話…沒錯…因為妾身美若天仙。',
                     '仰視我吧~我的僕人們',
                     '快逃~~~~~~',
                     '嗨，海綿寶寶，我們去抓水母吧。',
                     '我長成這樣是為了讓人看起來更想擁抱。',
                     '不能吃的太胖，不然會被殺掉的。',
                     '只要記住你的名字，不管你在世界的哪個地方，我一定會去叫你。'
                     '幸福是每一個微小的生活願望達成。當你想吃的時候有得吃，想被愛的時候有人來愛你。',
                     '就算發一千條短信，心與心之間的距離也不曾拉近過一釐米。',
                     '如果能實現，我想帶你，去看絢麗的山嵐，去看秀麗的溪谷，這份心情，人類是如何稱呼的呢。',
                     '知道雪為什麼是白色的嗎？那是因為它忘記了自己的顏色。',
                     '人的夢想，是不會終結的。',
                     '我答應你，一定會救你的。無論重復多少次，我一定會保護好你。',
                     '溫柔正確的人總是難以生存，因為這個世界既不溫柔也不正確。',
                     '我們所經歷的每個平凡的日常，也許就是連續發生的奇跡',
                     '我認為你很幸福，因為你可以選擇愛或不愛我。而我只能選擇愛或更愛你',
                     '沒有人會嘲笑一個全力以赴的傻子。',
                     '我覆蓋一張牌 結束這回合',
                     '我覆蓋一張空白考卷 結束這學期',
                     '上吧~吃貨是沒有極限的',
                     '用意不用力，太極圓轉，無使斷絕。當得機得勢，令對手其根自斷。一招一式，務須節節貫串，如長江大河，滔滔不絕。',
                     '世事如棋，乾坤莫測，笑盡英雄',
                     '天劍納星漢，地劍歸九地，天地縱橫破山嶽',
                     '水火金雷風，氣走任八方，流轉十二督，妖政破神荒',
                     '花飄兮，花落兮，花影滿天飛',
                     '七邪荼黎‧阿蘭聖印、七邪荼黎‧滅天邪威',
                     '↓↙←↙↓↘→←→+AC',
                     '來自地心的火神啊，順著我的血液而行，綻放出燦爛的櫻花吧!!! 超秘技。烈炎血之櫻'
                     '休、生、傷、杜、景、死、驚、八門開。秘術八門遁甲。',
                     '道生一，一生二，二生三，三生萬物。一氣化清',
                     '世界上總有一半人不理解另一半人的快樂。',
                     '人生那個東西，也許只是在一段刻骨銘心之後才算是真正的開始，但有時候想想，徒留遺憾罷了。',
                     '許多女人都躺在我懷裡問我是否愛她們，我都說是的，但是，我真正愛的卻是那個從來沒有問過我的女人。',
                     '生命不必每時每刻都要衝刺，低沉時就當是放一個悠長假期。',
                     '應該有更好的方式開始新一天，而不是千篇一律的在每個上午都醒來',
                     '誰會了解，生命中的過客竟會讓我如此感動，感謝你給我帶來的一切',
                     '好多東西都沒了，就象是遺失在風中的煙花，讓我來不及說聲再見就已經消逝不見',
                     '不記得也好，忘卻也是幸福',
                     '當你年輕時，以為什麼都有答案，可是老了的時候，你可能又覺得其實人生並沒有所謂的答案',
                     '最了解你的人不是你的朋友，而是你的敵人',
                     '生活不是電影，電影比生活苦',
                     '你是唯一個說我還不夠好的人，但我永遠都不會承認',
                     '這世上只有兩種人，騙人的和被騙的',
                     '真相是一種美麗又可怕的東西，需要格外謹慎地對待',
                     '左手是石頭、右手是布，剪刀~石頭~布~~~~~',
                     '別人可以給你做一雙超級好穿的鞋子，但路必須我們自己走，生命中的一切我們都要自己承受',
                     '時間可以造就人格，成就事業，也可以儲積功德。',
                     '人生的煩惱，是不分貧富貴賤的，透過煩惱轉成智慧，這個煩惱才有意義。',
                     '中二就要有中二的樣子，裝什麼13。',
                     '勇氣不可失，信心不可無，世間沒有不能與無能的事，只怕不肯。',
                     '自信是一種態度，而不是抬起你的雙下巴好嗎?',
                     '有願放在心裡，沒有身體力行，正如耕田而不播種，皆是空過因緣',
                     '身體污泥可以用水清除，心靈污泥則須用智慧之水消除。',
                     '不要怕人家說你傻，要擔心人家說你太聰明，太聰明就是狡猾。',
                     '身是菩提樹，心如明鏡台，時時勤拂拭，勿使惹塵埃',
                     '做事像做數學應用題，只會加減乘除，不會靈活應用，等於不會做。',
                     '是非從人事中來，要把複雜的人事單純化，成為自我的教育。',
                     '對自己有幻想的人叫愚，對別人有幻想的人叫痴。',
                     '不要這樣，人家想踢球',
                     '真正的幸福是無所求而為，是付出之後的感覺。',
                     '人生短短幾個秋啊，不醉不罷休 東邊兒我的美人哪，西邊兒黃河流，來呀來個酒啊，不醉不罷休，愁情煩事別放心頭',
                     '我要親手撕裂所有叫我胖的人',
                     '天啊!你真高',
                     '生命總會在最黑暗的地方綻放',
                     '金幣不是萬能的',
                     '獸人永不為奴，我們終將成王',
                     '生命本身毫無意義，只有死亡才能讓你了解人性的真諦',
                     '我如同羊群前的雄獅，但他們不畏懼我......也不敢畏懼我',
                     '湮遠而艱辛的探索到此為止，真正的正義者將由命運擇示！',
                     '時間是一張糾結的網，不要去探究每一條線索',
                     '天空一片黑暗,火焰仍在肆虐,你的攻擊豪無意義,命運之輪已經開始旋轉',
                     '賜予我力量，去改變我所能改變的;賜予我勇氣，去接受我不能改變的;并賜予我智慧，去分辨這兩者。',
                     '吾名死亡之翼，天命之滅世者，萬物的終結者，無可阻擋，無可違逆，吾即大災變！',
                     '你能否獨立山巔，任由風霜侵襲，直至滄海變為桑田，高山沉入海底？',
                     '沖鋒大跳切姿態，狂暴回復開劍在，集結護盾嗑藥水，盾吸茍且綁繃帶。',
                     '力量與榮耀、鮮血與雷霆、為了部落!',
                     '謝謝你，我自由了',
                     '看來我是......多餘的!',
                     '用力量錘煉你的智慧',
                     '房子再大，你也只睡一張床。',
                     '幾縷月光，追憶從前，一曲梵咒，叨擾心弦。再戴緊箍，徹悟當年，未曾苦悟，何以齊天',
                     '沒有人規定，朋友一定要有相同的夢想，好朋友之間的分歧只會加深彼此的感情，而不是真正的好朋友則會讓感情變淡。',
                     '輸了比賽，贏得了成長',
                     '無人能預測的命運賽道!這就是!這就是我想要的!',
                     '我努力了那麼多年，卻從來都是不懂你的。現在，不需要懂了，也不想要懂了。',
                     '愛別離，怨憎會，撒手西歸，全無是類。不過是滿眼空花，一片虛幻',
                     '我是清醒的夢境，你們噩夢中的怪物，千麵的惡魔。在我的真正形態下顫抖吧！在死亡之神麵前屈服吧！',
                     '我們已經虛度了太多時間，去為那些已經發生或將要發生卻還未發生的事情感到悲傷。',
                     '燃燒吧!!!我的小宇宙~~~~~奧義!!!天馬流星拳 =======O)',
                     ]}
        
        return random.choice(dict['經典'])

if __name__ == '__main__':
    main()