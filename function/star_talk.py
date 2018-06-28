import re
import random
from function.hsing import sing17
from function.s17api import s17uidrandom_star
from function.function import shelp

if __name__ == '__main__':
    res = '小星星尿床'
    print(star_talk(res))

def star_talk(messages_talk):
    if re.search("幹|fuck|操",messages_talk):
         return talk_dict('fuck')
    elif re.search("三小",messages_talk):
         return talk_dict('fuck')
    elif re.search("靠北",messages_talk):
         return talk_dict('靠北')
    elif re.search("三字經",messages_talk):
         return talk_dict('三字經')
    elif re.search("爆料",messages_talk):
         return talk_dict('爆料')
    elif re.search("壞掉了",messages_talk):
         return talk_dict('壞掉了')
    elif re.search("哈哈哈哈哈",messages_talk):
         return talk_dict('哈N')
    elif re.search("早安|早啊",messages_talk):
         return talk_dict('早安')
    elif re.search("晚安|睡囉",messages_talk):
         return talk_dict('晚安')
    elif re.search("尿好了|有尿了",messages_talk):
         return talk_dict('尿好了')
    elif re.search("(才|你|小星星)尿床",messages_talk):
         return talk_dict('尿床')
    elif re.search("小星星",messages_talk):
        if re.search("早[安|啊|上好]",messages_talk):
            return talk_dict('早安')
        if re.search("午安",messages_talk):
            return talk_dict('午安')
        if re.search("晚[安|上好]|睡[覺|了|囉]",messages_talk):
            return talk_dict('晚安')
        if re.search("你好|安安|hello|hi]",messages_talk):
            return talk_dict('hi')
        elif re.search("找[你|妳|星星]",messages_talk):
           return talk_dict('you')
        elif re.search("找星(爸|拔)|星(爸|拔)咧|星(爸|拔)在哪裡|叫一下星(爸|拔)|叫星(爸|拔)",messages_talk):
            return talk_dict('星爸')
        elif re.search("找[碴|麻煩]",messages_talk):
            return talk_dict('麻煩')
        elif re.search("聊天]",messages_talk):
            return talk_dict('talk')
        elif re.search("聽話|乖|乖乖",messages_talk):
            return talk_dict('goodboy')
        elif re.search("[喜歡|愛]什麼",messages_talk):
            return talk_dict('like')
        elif re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk):
            if re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk).group(1) == "吃":
                return talk_dict('like_eat')
            if re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk).group(1) == "喝":
                return talk_dict('like_drink')         
            if re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk).group(1) == "玩":
                return talk_dict('like_play')
            if re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk).group(1) == "看":
                return rtalk_dict('like_see')
            if re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk).group(1) == "聽":
                return talk_dict('like_listen')
            if re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk).group(1) == "誰":
                return talk_dict('like_who')
            if re.search("[喜歡|愛](吃|喝|玩|看|聽|誰|我)",messages_talk).group(1) == "我":
                return talk_dict('like_me')
        elif re.search("機器人|是[誰|什麼|男|女]",messages_talk):
            return talk_dict('robot')
        elif re.search("多大|幾歲",messages_talk):
            return talk_dict('多大')
        elif re.search("住那|住哪|家在哪|家在那",messages_talk):
            return talk_dict('住那')
        elif re.search("有什麼功能|功能表",messages_talk):
            return shelp()
        elif re.search("哈|哈哈|哈哈哈",messages_talk):
            return talk_dict('哈')
        elif re.search("哭|欠揍|打你哦",messages_talk):
            return talk_dict('cry')
        elif re.search("打屁股|打屁屁",messages_talk):
            return talk_dict('kpp')
        elif re.search("生氣",messages_talk):
            return talk_dict('angry')
        elif re.search("傻子|呆子|笨蛋|傻瓜'fool|stupid|北七|白痴",messages_talk):
            return talk_dict('fool')
        elif re.search("壞了|該修理|要修理",messages_talk):
            return talk_dict('壞掉了')
        elif re.search("出團",messages_talk):
            return talk_dict('group')
        elif re.search("運動|動一動",messages_talk):
            return talk_dict('sport')
        elif re.search("傻子|呆子|笨蛋|傻瓜'fool|stupid|北七|白痴",messages_talk):
            return talk_dict('fool')
        elif re.search("吃[大便|屎|屁]",messages_talk):
            return talk_dict('eatshit')
        elif re.search("吃什麼|想吃|愛吃|要吃|餓|吃飯",messages_talk):
            return talk_dict('eat')
        elif re.search("虧妹|虧你|虧妳|虧我",messages_talk):
            return talk_dict('bamai')
        elif re.search("[難|不好]聽",messages_talk):
            return talk_dict('badsing')
        elif re.search("[唱|唱一｜換｜換一|來一][歌|首]",messages_talk):
            content = talk_dict('sing')
            if re.search("抽歡歌",content):
                res = sing17()
                if re.search("找不到歌",res):
                    return "我不知道要唱什麼耶"
                else:
                    return res
            elif re.search("UID",content):
                if s17uidrandom_star(re.search("UID(.+)",content).group(1)) == "查不到歌曲":
                    return "突然不知道要唱什麼"
                else:
                    return s17uidrandom_star(re.search("UID(.+)",content).group(1))
            else:
                return content
        else:
            return talk_dict('random')
        
def talk_dict(res):
    dict={
            '尿好了':['很好~那快去睡吧日~晚安','那就不用包屁屁了'],
            '尿床':['我早就不用包屁屁了','我很久沒尿床了','前天~~~~~~'],
            'fuck':['喵喵~','汪汪~','咩~','啊嘶~','噓~好孩子不說這個','講~f~u~c~k~才有英特內訊NO','十十人一十','操你媽好嗎~幹我媽很好',
                    '你媽知道你在講幹話嗎','汝聲何其大','E04','每60秒就會有一分鐘過去~你還在這講幹話','人生何其短~何必幹不停',
                    '喂~氣質一點','別操來幹去啦','不要過來~我會叫~','來跟著小星星幹~一定會成功','環保不分你我~垃圾不分藍綠',
                    '哇！你火氣那麼大，要不要我今晚給你下下火啊？','區區一馱屎值的了幾個錢,何必大驚小怪！',
                    '罵人都沒幾招了，還說是黑社會？','文也不行，武也不行，醒醒吧！','只要有心~人人都可以是幹話大王'],
            '三小':['我聽過小王、小強、就是沒聽過三小','小小小', '大大大','小三小四小五','意義是三小 我只知道義氣',
                  '你是魯小小','汝聲何其大','不知汝之所言','干卿底事'],
            '靠北':['靠北邊走','靠南', '我靠爸族啦','我有的靠你有嗎','喂喂別靠來靠去','走路要靠右邊走','麥靠啦, 飲啦~',
                  '人之初性本善性相近習相遠~','哇！你火氣那麼大，要不要我今晚給你下下火啊？','區區一馱屎值的了幾個錢,何必大驚小怪！',
                  '罵人都沒幾招了，還說是黑社會？','文也不行，武也不行，醒醒吧！'],
            '三字經':['人之初性本善性相近習相遠. 茍不教性乃遷教之道貴以專. 昔孟母擇鄰處子不學斷機杼. 竇燕山有義方教五子名俱揚. 養不教父之過教不嚴師之惰. 子不學非所宜 ...'],
            '爆料':['爆料公社裡抄來的嗎?','爆什料呢?','什麼好料的~說來聽聽','沒圖沒真相','有料爆~卡一個','搬椅子~買爆玉花~等聽爆料'],
            '住那':['住在妳心裡','不告訴你','猜猜看啊','住在...','我忘了耶','住在星爸家裡','我來自M78星雲','星爸住那我就住那啊',
                  '我以天為幕，以地為席，住所只是一個代名詞而以~'],
            '多大':['爸說不可以講','這是個秘密','不如你先說說你幾歲','嘿嘿嘿...','佛曰不可說','1~2~3~4~.....','我1歲'],
            '早安':['早安','熬早','牛沒奶','Good Morning','早安~祝你有美好的一天','記得吃早餐哦','早安~來杯咖啡嗎?','起來動一動吧~','別滾床了',
                  '早安~今天一定會有好事發生的'],
            '午安':['午安','吃飽了嗎?','午餐要吃什麼呢?','今天天氣如何呢?','加油~別忘記喝水哦','午~要喝咖啡嗎?','下午再加油一下'],
            '晚安':['晚安','嗯~我也要睡了','乖乖睡哦','噓~快睡吧','zzzzzz','噓~~~~','記得睡前先尿尿哦','別尿床了哦~','記得刷牙哦~'],
            'hi':['hi','hello','你好啊','今天天氣如何?','要抽一張嗎?','安安啊~','有什麼事嗎?','找我嗎?','嗨嗨~'],
            'you':['找我有什麼事嗎?','想聊天嗎?','要做什麼呢?','沒事別叫我'],
            '星爸':['爸~有人叫你','他沒空哦','有什麼事嗎?','噓~~星爸正在忙','小聲點~他在錄歌','爸爸爸爸爸~~','藍藍路~~',
                  '自已叫~','他在睡覺啦~'],
            '麻煩':['你想怎樣','我叫警察哦','關門放狗','小心我叫羊羊咬你','不要過來我要叫了哦','啊~~~~~~~~'],
            'talk':['要聊什麼呢?','嗯~我聽著','你說說~','好啊~','有什麼心事嗎?','我不知道要聊什麼耶'],
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
                        '就隔閉班的~~','看著我的眼睛~~裡面有妳要的答案'],
            'like_me': ['喜歡~','好き~~好き~~大好き~~','不喜歡','爸說要多一點選擇','你知道嗎?昨天我去~~~~~','什麼?','還要問嗎?',
                        '妳知道的','嗯~就是妳心裡想的那樣'],
            'robot':['是啊','我是星爸做的機器人唷','你說呢?','我可愛嗎?','很認真的告訴你，我是機器人','是機器人錯了嗎?','身為一個機器人我可以做的更多'],
            '哈':['笑屁','笑什麼笑~牙齒白啊','嘴巴再張大一點','我看到金牙了','笑什麼','有什麼事那麼好笑?','哈','哈哈','哈哈哈','哈哈哈哈哈'],
            '哈N':['嘴巴張那麼大做什麼'],
            'cry':['你欺負我','爸有人欺負我','警察叔叔就是這個人','不能哭嗎?','我就是愛哭','你..打..我.......','別打我，有事好好說',
                   '我咬你哦','我是妳的人了~妳要怎麼打我~罵我~我都....','不要打了~嗚~~~~'],
            'kpp':['色狼','警察叔叔就是這個人','嗯~多打二下嘛~','不要打了~嗚~~~~','很有彈性吧~'],
            'angry':['我才沒有生氣','怎樣不行嗎?','啦啦啦啦啦','你才愛生氣','就是生氣','哼~~~~~'],
            '壞了':['保修價8萬1~','維修專線0800080000','你弄壞的厚~','舊的不去新的不來','不是我弄壞的~','賣了就當廢鐵賣了',
                  '你才壞掉了','快呼叫星爸','沒壞啦','小星星不壞女人不愛','維修專線~忘了'],
            'fool':['你才傻的','我不笨我只是不聰明','我可是擁有最先進的人工智障','哭給你看哦~','哼~~~','給你87分不能再多了',
                    '傻瓜是誰?','白痴說話','叫星爸咬你哦','黛比有人欺負你弟弟'],
            'group':['出什麼團?','龍谷YYYY','要去那裡玩呢?','吃BOSS嗎?','密室團嗎?0.0'],
            'sport':['one毛~two毛~tree毛','找星爸去~他太胖了','走吧爬枕頭山~','要去那邊運動啊~','嘿~我動動嘴巴就好~','要做什麼運動啊',
                     '動一動~可以再多吃二碗~','GoGoGo~','看到那顆樹了嗎?左去右回~來回10圈~~~','啥~你說什麼'],
            'eatshit':['你自已吃','你要吃大便?','你怎麼有那麼特別的嗜好啊','原來你喜歡吃...難怪嘴巴那麼臭','記得刷牙'],
            'eat':['你想帶我去吃什麼','我要吃牛排','減肥中禁止餵食','換現金給星爸就好','整天就想著要吃','滷肉飯','我想想哦~',
                   '餓了嗎?吃點東西吧!','甜甜圈','現在吃什麼','冰淇淋','只要是好吃的東西我都愛','肉肉~我要吃肉肉~','蝦蝦~',
                   '你要帶我去吃什麼好料的嗎?','牛排~~大大塊的牛排'],
            'bamai':['我有嗎?','你想太多了','虧一下不可以嗎?','不要發我好人卡','都是羊羊教我的','我很想你','等等喝咖啡啊',
                     '看著我的眼~ 妳看到了什麼?','為什麼我在妳的眼裡~看到了愛心呢?','不要走~要走的話先把我的心還給我'],
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
                    '抽歡歌','UID526155','UID1048784','UID637621','UID954530','UID181460','UID814357','UID1585626'],
            'random':['一閃一閃亮晶晶 滿天都是小星星','是誰在叫我啊','你看不到我0.0',
               '來了來了~','麥吵~底睏啦~','小星星你的好幫手',
               '要抽一張嗎','噓~~','抽','你好~找我嗎',
               '我跳出來了','底家底家','笑咪咪',
               '別一直叫我啦','你 就是我的小星星 掛在那天上放光明  我已經決定要愛你 就不會輕易放棄',
               '要唱歌嗎?','登愣~我跳出來啦~','噓~跟你說一個秘密~',
               '你長得好像我一個朋友，未來的女朋友','霹靂卡霹靂拉拉 波波力那貝貝魯多',
               '拍拍砰呸 噗哇噗哇噗 ','帕美魯克 拉魯克 拉哩摟哩波',
               '你知道嗎人一生中可以喝一次岩漿','你有freestyle嗎',
               '嚇死寶寶了','言之有理乎','假的~都是假的~~',
               '啊~我眼睛業障重','各位觀眾~一顆小星星~~','沒事退朝',
               '那我去睡了哦~','星星不壞, 女人不愛','星爸~有人欺負我~~',
               '你傻了啊~','笑什麼笑~牙齒白啊!', '抽籤算命嗎? 不準找星爸~',
               '老闆~來一份蛋餅+無榶綠茶','此言差矣~吾向來木訥寡言的~',
               '再靠近一點~看到了嗎? 我的眼中有個美女~',
               '我只是略懂略懂啦~','嚇到吃手手','去看星星~星星就在妳的眼裡啊~',
               '你知道為什麼你眼睛很漂亮嗎?因為妳的眼裡有我','啊!我就只會這麼多啊~不然妳教我',
               '這不是肯德雞~~~','走去那哦~妳說咧~',
               '隱藏著黑暗力量的鑰匙阿　請在我的面前顯示真正的力量~','你要羞恥Play嗎? 我先摭眼一下',
               '來啊來啊~現在就走','只有這樣而已嗎？',
               '不要問~你會怕','我到底看了什麼啊','燒毀~燒毀~','要不要來點夯吉~放屁會噗噗噗哦~',
               '床前明月光~疑似地上霜~舉頭~~舉頭~~~都你啦叫我害我忘記了~',
               '上上下下左左右右ABBA','好討厭的感覺啊~~~~',
               '你知道嗎?吃七分熟的牛排~就會減輕牛排三分的痛楚',
               '奶茶之所以叫奶茶~是因為你忘了點珍珠~認同請分享~',
               '我覺的不行','別聊了~包廂開好了~來唱歌吧~~~','別教壞我~星星很單純的~',
               '你在講笑話嗎?我講的比較好笑~','哈哈哈哈哈哈哈哈哈~','嗚~~~~~~~~~~',
               '為什麼我叫小星星啊~ 因為要照亮妳的心','你是什麼星座的呢?',
               '飛飛飛~~~~拔我怎麼不會飛~','胖胖的~~','伊啊伊啊唷~~','噯唷~不錯哦~',
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
               '沉醉在本大爺的抽牌當中吧!','我要下了!',
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
               '就算是一條內褲一卷衛生紙也有它的用處，而你呢?',
               '我養你啊！','人是人他媽生的，妖是妖他媽生的，小星星是?',
               '憑你的智慧，我唬得了你嗎？','你完全沒問題，是你爸媽有問題，把你生成這個樣子!',
               '你無聊啊？跑這騙傻子玩！','小姐，不可否認我長得很醜，可是我很溫柔，而且永遠不會說謊。',
               '誰生ㄉ誰照顧ㄚ','說不說，不說我就灌你豬油哦~','聽說你唱歌很好聽~來一首吧~',
               '人來啊，落閘，放狗！','文也不行，武也不行，醒醒吧！',
               '實不相瞞，小弟我就是人稱玉樹臨風勝潘安，一支李花壓海棠的鮮帥哥~小星星！',
               '現在聽懂沒有？','我正在談兒女私情，改程式這種小事改天再說啦！',
               '只要有心~人人都可以是幹話大王','喝醉了我誰也不服，就扶牆！',
               '不吃飽哪有力氣減肥啊','我月巴我驕傲','沒什麼事不要找我，有事更不用找我',
               '保護自己，愛護他人，請不要半夜出來嚇人','我以為我很頹廢，今天我才知道，原來我早報廢了',
               '腦袋空不要緊、關鍵是不要進水','不要臉這事，如果幹的好，叫心理素質過硬！',
               '沒知識也要有常識、沒常識也要常看電視、不看電視總也要逛逛夜市、不逛夜市那就找小星星抽張試一試',
               '平時罵你就算了，非要等我打你才知道我文武雙全',
               '我的優點是：我很帥；但是我的缺點是：我帥的不明顯',
               '人家有的是背景，咱有的是背影,還特別的厚實',
               '羊腸小道,GG小一號','我不是不想減肥，我只是怕反彈而已',
               '錢不是問題，問題是沒錢','人生就像衛生紙，沒事的時候，儘量少扯！',
               '我很純潔的，就像再生紙一般','你真的是他媽的幹話王耶!',
               '我覺得妳看起來有點營養不良，建議妳可以吃掉羊羊',
               '只要每天省下買一杯奶茶的錢，十天後就能買十杯奶茶',
               '當你的左臉被人打，那你的左臉就會痛','煎魚一直不翻面，就一定會燒焦',
               '當我眼睛閉上時 我就看不到','你們是在安靜什麼啦',
               '冰淇淋不拿去冰，一定會融化，統一除外','偷偷告訴你，在床上尿尿就會尿床',
               '我先了解一下，之後再回覆你','我必須公平對待每個人','我想這事情原本就不該發生⋯⋯',
               '我很想幫你加薪，但是⋯⋯','這麼晚還在加班啊？',
               '根據研究，人類的死因有99%是因為無法吸到下一口空氣',
               '墮落是不需要理由的，但是，不墮落卻是有原因的','終於，結束了啊',
               '去實現夢想吧，啊~~~~~~','你，是誰？',
               '世界是靠力量判定，力量能決定一切事物的優劣，你實在太弱了…所以才會輸…',
               '我們仰望着同一片天空卻看着不同的地方','閃閃閃!!!撞到不負責!!!',
               '肉!!!我要肉~~~','燃燒吧!我的小宇宙','你打我,連我爸都沒這樣打過我…',
               '我的靈魂永遠與您同在','今天的我沒有極限','你只要相信你所相信的你自己就行了',
               '他是我的靈魂也是我的驕傲,出來吧!青眼白龍~~~','就決定是你了',
               '滴滴滴滴滴～～～嗶嗶！時間到！','你是笨蛋嗎？','又砍了無聊的東西了啊…',
               'σ`∀´)σㄎㄎ','將你的幻想抹殺掉','我得到神騎寶貝了',
               '剛好……一分鐘…你做了一場好夢了嗎?','就這樣插進去就行了','我是輸給了地球的重力',
               '那是要給我的嗎?','爸說，陌生人的東西不可以吃','和我簽訂契約','戳一個',
               '重要的日曆缺了一頁','我好像有點強','你比的贏GG的舌頭嗎?',
               '這是人生的選擇，別人的說話是沒用的','去沖個水好好冷靜吧','因為我是天才',
               '我會讓你成為真正的王牌','這是禁止事項','人類LOVE！我喜歡人類！我愛人類！所以人類應該也要愛我',
               '八目共賞，賞花賞月賞秋香',
               '小星星是你的好朋友']
            }
    
    return random.choice(dict[res])
    
