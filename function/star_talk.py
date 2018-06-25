import random
import re
from .hsing import sing17
from .s17api import s17uidrandom_star

def star_talk(messages_talk):

    if messages_talk.find('幹')>-1 or messages_talk.find('操')>-1:
        content = random.choice(['喵喵~','汪汪~','咩~','啊嘶~','噓~好孩子不說這個','講~f~u~c~k~才有英特內訊NO','十十人一十','操你媽好嗎~幹我媽很好','你媽知道你在講幹話嗎',\
                                '汝聲何其大','E04','每60秒就會有一分鐘過去~你還在這講幹話','人生何其短~何必幹不停','喂~氣質一點','別操來幹去啦','不要過來~我會叫~',\
                                '來跟著小星星幹~一定會成功','環保不分你我~垃圾不分藍綠','哇！你火氣那麼大，要不要我今晚給你下下火啊？','區區一馱屎值的了幾個錢,何必大驚小怪！'\
                                '罵人都沒幾招了，還說是黑社會？','文也不行，武也不行，醒醒吧！','只要有心~人人都可以是幹話大王'])
        return content
    if messages_talk.find('三小')>-1:
        content = random.choice(['我聽過小王、小強、就是沒聽過三小','小小小', '大大大','小三小四小五','意義是三小 我只知道義氣','你是魯小小','汝聲何其大','不知汝之所言','干卿底事'])
        return content
    if messages_talk.find('靠北')>-1:
        content = random.choice(['靠北邊走','靠南', '我靠爸族啦','我有的靠你有嗎','喂喂別靠來靠去','走路要靠右邊走','麥靠啦, 飲啦~','人之初性本善性相近習相遠~',\
                                '哇！你火氣那麼大，要不要我今晚給你下下火啊？','區區一馱屎值的了幾個錢,何必大驚小怪！','罵人都沒幾招了，還說是黑社會？','文也不行，武也不行，醒醒吧！'])
        return content
    if messages_talk.find('馬的')>-1 or messages_talk.find('媽的')>-1:
        content = random.choice(['馬兒跑~馬兒跳~馬兒咩咩叫~','一馬當先、馬到成功、馬耳東風、馬的成語還有很多哦~','媽媽的孩子都是寶','你8+9哦','羊的~雞的~狗的~'])
        return content
    if messages_talk.find('爆料')>-1 or messages_talk.find('八卦')>-1:
        content = random.choice(['卡一個','爆米花準備好了','沒圖沒真相','有卦快抄','爆漿會不會比較精彩','筆記ing','乾、坤、坎、離、震、巽、艮、兌','真相永遠只有一個'])
        return content
    if messages_talk.find('放屁')>-1 or messages_talk.find('屁啦')>-1 or messages_talk.find('狗屁')>-1:
        content = random.choice(['噗~~~~~~是誰','Lucky~Lucky~Lucky~你再躱在桌子底下會臭死','好臭~~~','快大口吸掉','多吸多健康','聽說屁聞多了人會變聰明','看到一條小狗要叫它「旺財」'])
        return content
    if messages_talk.find('三字經')>-1 or messages_talk.find('幹你娘')>-1:
        content = "人之初性本善性相近習相遠. 茍不教性乃遷教之道貴以專. 昔孟母擇鄰處子不學斷機杼. 竇燕山有義方教五子名俱揚. 養不教父之過教不嚴師之惰. 子不學非所宜 ..."
        return content
    if messages_talk.find('壞掉了')>-1:
        content = random.choice(['保修價8萬1~','維修專線0800080000','你弄壞的厚~','舊的不去新的不來','不是我弄壞的~','賣了就當廢鐵賣了'])
        return content
    if re.search("小星星",messages_talk):
        if re.search("住那|住哪|家在哪|家在那",messages_talk):
            return random.choice(where())
        elif re.search("多大|幾歲",messages_talk):
            return random.choice(howold())
        elif re.search("早[安|啊|上好]",messages_talk):
            return random.choice(morning())
        elif re.search("午安",messages_talk):
            return random.choice(moon())
        elif re.search("晚[安|上好]|睡[覺|了|囉]",messages_talk):
            return random.choice(goodninght())
        elif re.search("你好|安安|hello|hi]",messages_talk):
            return random.choice(hi())
        elif re.search("找[你|妳|星星]",messages_talk):
            return random.choice(you())
        elif re.search("找星(爸|拔)|星(爸|拔)咧|星(爸|拔)在哪裡|叫一下星(爸|拔)|叫星(爸|拔)",messages_talk):
            return random.choice(father())
        elif re.search("找[碴|麻煩]",messages_talk):
            return random.choice(trouble())
        elif re.search("聊天]",messages_talk):
            return random.choice(talk())
        elif re.search("喜歡什麼",messages_talk):
            return random.choice(like())
        elif re.search("機器人|是[誰|什麼|男|女]",messages_talk):
            return random.choice(robot())
        elif re.search("哭|欠揍",messages_talk):
            return random.choice(cry())
        elif re.search("生氣",messages_talk):
            return random.choice(angry())
        elif re.search("壞掉了|壞了",messages_talk):
            return random.choice(broken())
        elif re.search("傻子|呆子|笨蛋|傻瓜'fool|stupid",messages_talk):
            return random.choice(fool())
        elif re.search("吃[大便|屎|屁]",messages_talk):
            return random.choice(eatshit())
        elif re.search("吃什麼|想吃|愛吃|要吃|餓|吃飯",messages_talk):
            return random.choice(eat())
        elif re.search("虧妹|虧你|虧妳|虧我",messages_talk):
            return random.choice(bamai())
        elif re.search("[唱|唱一｜換｜換一|來一][歌|首]",messages_talk):
            content = random.choice(sing())
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
        elif re.search("[難|不好]聽",messages_talk):
            return random.choice(badsing())
        else:
            return random.choice(words())


def words():
    content = ['一閃一閃亮晶晶 滿天都是小星星','是誰在叫我啊','你看不到我0.0',
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
               '小星星是你的好朋友']

    return content

def where():
    content =['住在妳心裡','不告訴你','猜猜看啊','住在...','我忘了耶','住在星爸家裡']
    return content

def howold():
    return ['爸說不可以講','這是個秘密','不如你先說說你幾歲','嘿嘿嘿...']

def morning():
    return ['早安','熬早','牛沒奶','Good Morning','早安~祝你有美好的一天','記得吃早餐哦','早安~來杯咖啡嗎?','起來動一動吧~',
            '別滾床了']

def moon():
    return ['午安','吃飽了嗎?','午餐要吃什麼呢?','今天天氣如何呢?','加油~','午~要喝咖啡嗎?','下午再加油一下']

def goodningh():
    return ['晚安','嗯~我也要睡了','乖乖睡哦','噓~快睡吧','zzzzzz','噓~~~~','記得睡前先尿尿哦','別尿床了哦~','記得刷牙哦~']

def hi():
    return ['hi','hello','你好啊','今天天氣如何?','要抽一張嗎?','安安啊~','有什麼事嗎?','找我嗎?']

def like():
    return ['喜歡看美女','喜歡妳','妳喜歡我嗎?','看電影','聽音樂','喜歡打屁聊天','喜歡...']

def robot():
    return ['是啊','我是星爸做的機器人唷','你說呢?','我可愛嗎?','很認真的告訴你，我是機器人',
            '是機器人錯了嗎?','身為一個機器人我可以做的更多']

def cry():
    return ['你欺負我','爸有人欺負我','警察叔叔就是這個人','不能哭嗎?','我就是愛哭',
            '別打我，有事好好說','我咬你哦']

def angry():
    return ['我才沒有生氣','怎樣不行嗎?','啦啦啦啦啦','你才愛生氣','就是生氣','哼~~~~~']

def broken():
    return ['你才壞掉了','快呼叫星爸','沒壞啦','小星星不壞女人不愛','維修專線~忘了',
            '保修價8萬1~','維修專線0800080000','你弄壞的厚~','舊的不去新的不來','壞了就當廢鐵賣了']

def you():
    return ['找我有什麼事嗎?','想聊天嗎?','要做什麼呢?','沒事別叫我']

def father():
    return ['爸~有人叫你','他沒空哦','有什麼事嗎?','噓~~星爸正在忙','小聲點~他在錄歌','爸爸爸爸爸~~','藍藍路~~',
            '自已叫~','他在睡覺啦~']

def trouble():
    return ['你想怎樣','我叫警察哦','關門放狗','小心我叫羊羊咬你','不要過來我要叫了哦','啊~~~~~~~~']

def talk():
    return ['要聊什麼呢?','嗯~我聽著','你說說~','好啊~','有什麼心事嗎?']

def fool():
    return ['你才傻的','我不笨我只是不聰明','我可是擁有最先進的人工智障','哭給你看哦~','哼~~~']

def eatshit():
    return ['你自已吃','你要吃大便?','你怎麼有那麼特別的嗜好啊','原來你喜歡吃...難怪嘴巴那麼臭','記得刷牙']

def eat():
    return ['你想帶我去吃什麼','我要吃牛排','減肥中禁止餵食','換現金給星爸就好','整天就想著要吃',
            '滷肉飯','我想想哦~','餓了嗎?吃點東西吧!','甜甜圈','現在吃什麼','冰淇淋']

def bamai():
    return ['我有嗎?','你想太多了','虧一下不可以嗎?','不要發我好人卡','都是羊羊教我的','我很想你','等等喝咖啡啊']

def badsing():
    return ['哼~我不唱了','那你唱','換你唱','我又不是大歌星','就不會唱歌啊']

def sing():
    return ['一閃一閃亮晶晶，滿天都是小星星......',
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
            '抽歡歌','UID526155','UID1048784','UID637621','UID954530','UID181460','UID814357','UID1585626']
