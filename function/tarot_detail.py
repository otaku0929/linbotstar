import re
import random

def tarot_random():
    return tarot_detail(random.randint(0,21))

def tarot_detail(res):

##fool
    if res == 0:
        title = "愚者(正位)"
        content = "愚者並不表示愚笨，他是大智若愚的狀態，身後隨身的背囊亦是旅行所需的道具，\
    代表有充分準備的意思，準備在旅途上大展身手，從人類的生命來說，\
    是一種生下來，與身俱來的天賦，且面對前方的危險，仍能站出來行走面對，其也是有勇敢的內心。\
    \n\n\
    展開的旅程之開始，是故愚者出現時，出現旅行、遠行的機會很大。而身旁的小狗，\
    是旅程中陪伴愚者同行的夥伴，就圖面的動作，可以說他是在提醒，提醒愚者前方的危險，\
    投射到實際的面向上，代表身旁的建議，或者說是重要他人、貴人的提醒。\n\n\
    在感情方面，可能雙方處於浪漫純真，純純的愛情，未有接觸到兩人實際上的層面。\n\n\
    工作方面，可能要注意未有見到的危險，多聽聽身邊他人的意見，盡自己的能力而為的話大致上未有太大的問題。"
        url = "http://cisian.pixnet.net/blog/post/43076253"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/PHsrYCM.jpg"])
            
    if res == 1:
        title = "愚者(逆位)"
        content = "逆位的愚者，可能就是真的笨了，因為重力的關係，行囊可能失去，代表準備不充足，\
    手上純真的百合丟失，代表失去純真，或者是想的太多，而逆位懸崖在上方，具有強調的意味，\
    代表眼前的危機擴大，陷入窒礙難行的狀態，而小狗在此時，展現的是一種錯誤的訊息，\
    代表外在的訊息給予之建議可能有誤，或者是太過倚賴外在，使得自己無法做出決定，\
    或是成為一種累贅，豬一樣的隊友，整體上來說因眼前的挑戰太大，想的太多，而失去了勇氣。\n\n\
    感情上的愚者逆位，表示遭遇挫折，情感無法向前，或者是遭遇情感上的危機，雙方無法闖關。\n\n\
    投資上要注意，可能會因為錯誤的信息而陷入財務上的困難。"
        url = "http://cisian.pixnet.net/blog/post/43076253"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/1ct0QRi.jpg"])

#magician
    if res == 2:
        title = "魔法師(正位)"
        content = "魔法師正位時，為信息正確的傳播，花開得茂盛，能量的順暢遞送，表示溝通良好。\
    前方的紅玫瑰與白百合，為黃金黎明的代表標誌，也揭示魔法師為其組織當中的一員，身上所穿的衣袍紅白相間也可之其一二。\
    腰間的蛇，為自吞蛇的標誌，吃掉自己的尾巴，然後又長出來，跟頭上的無限符號都是一種無限的宇宙循環的表示，\
    想法清晰，而蛇在古老的隱喻當中，包含著智慧，放於腦袋上的無限符號即為腦袋智慧的無限運轉。\n\n\
    在感情當中，雙方處於年輕的熱戀，有新鮮的熱度，彷彿關係當中充滿了無限的變化，而對方在她的眼中，\
    是一位年輕俊美的男子，具有變化萬千的魅力。\n\n\
    在工作方面，這張牌的出現代表有能力，能構統合各種的事物，並且自己的工作職權範圍內無所不知無所不曉，\
    能力表現出色，有實際上的產出。"
        url = "http://cisian.pixnet.net/blog/post/43167558"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/9FbrjDq.jpg"])
            
    if res == 3:
        title = "魔法師(逆位)"
        content = "逆位的魔法師，可能虛有其表，表現出來是一種欺騙，表面上有能力變化，實質上所完成的東西指是一種假象，\
    可能是一種假報告、假作品、抄襲之類的狀況產生。 也有可能真的沒有能力表現出來的人，頭上智慧的無限符號因逆位消失，\
    而缺乏智慧，做什麼都不行，無法掌握大局，工作一塌糊塗，技能不好，而桌上的四元素消失，也代表着環境資源不足。\n\n\
    前方的百合與玫瑰消失了，代表事物本身不再有豐富的變化，熱情熱度消退。原本在溝通天地間的流動手勢，\
    也因逆位時失去正確導引的力量方向，而產生能量的凌亂，投射在關係中，展現為溝通不佳、言詞不達。"
        url = "http://cisian.pixnet.net/blog/post/43167558"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/NYkcUYJ.jpg"])


#High_Priestess
    if res == 4:
        title = "女祭司(正位)"
        content = "女祭司屬於壓抑自我的人格特徵，對於物質享受不感興趣，然不是絕對的無情，\
    後方的帷幕代表內心的豐富性與生命力(紅石榴-生命之果)，他的內心實為充滿了生命的熱度，\
    只是外表上看起來相當的文靜與平靜，表現出來好像對事情有冷淡，實為一種矜持的體現，具有保守的性格，\
    另一方面，腳踏新月代表著純潔的特質，未經世事。手中所掌握的書本為智慧之書，掌握的是智慧，\
    黑白陰陽之間的道理，而後方沉靜寬廣的水面，就實體場景來說，該海為地中海，\
    而寬廣的水面投射於人身上，代表是潛意識的概念。\n\n\
    感情的層面，雙方可能淡淡的，對感情總有保留，但內心或許隱藏著微微的對感情的期望，就總體上來說，\
    可能關係上缺乏親密的特質，對於男女情感的投入熱度稀少，而女祭司的人物對象也顯現出對方目前對於感情並不抱持興趣，\
    若是太主動熱烈，往往感情容易踢到鐵板。\n\n\
    而該牌因比較屬於內心高層次的展現，故對於行動面較為不利，想的很多卻做得很少，有想法確無實際上的作為，\
    故物質上的收穫不大，為心靈層次的牌。"
        url = "http://cisian.pixnet.net/blog/post/43211391"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/RvTWU0o.jpg"])
            
    if res == 5:
        title = "女祭司(逆位)"
        content = "逆位的女祭司，可能雙柱被摧毀了，造成黑白是非不分，而海在上方，可能也代表水面不再平靜，\
    產生情緒上的潰堤，潛意識的躁動，或是毛躁的情緒，情感不再被壓抑，嶄露了出來，\
    另外一方面來說，布幕的失去，也有可能造成女祭司逆位時，展現絕對冷漠，裝做表面的口是心非，不夠真誠。\n\n\
    新月在上，也強調月亮的陰晴圓缺特質，具有周期與波動性，可以說是反反覆覆，情緒潮起潮落，\
    情緒不穩定，可能變得無法掌握對方的心情。"
        url = "http://cisian.pixnet.net/blog/post/43211391"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/odvdrT6.jpg"])

#empress
    if res == 6:
        title = "女皇(正位)"
        content = "女皇牌代表母親的形象，正位是一位能夠給予物質撫育，溫暖甜蜜的母親，且謹守母親的權限，\
    投射在當事人的心中，表示對方可以在事件中自我照顧，如果有懷孕的跡象的話，女皇給的訊息也是偏向肯定的。\n\n\
    顯然的，這張牌強調物質，享受於物質的沉浸當中，世俗的快樂是女皇所追逐的目標。\n\n\
    在人際方面，因為皇后是一位母親的形象，是故在關係當中，會感到親切熱絡，照顧般的溫暖，對愛情方面屬於有利的特徵。\n\n\
    工作方面，太過注重舒適度，工作上的進度需要注意，然而皇后也身為一皇，故屬於有明確個人的特質，\
    在面試時，可以給予考官印象上的分數。"
        url = "http://cisian.pixnet.net/blog/post/46242045"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/Tdd3rV4.jpg"])
            
    if res == 7:
        title = "女皇(逆位)"
        content = "逆位的女皇牌，豐盛的能量枯萎，形成一種貧瘠，掉落的權杖與從椅上跌落表示無法再享受生活\
    ，這一切可能讓女皇感到情緒上的焦躁，心生欲求不滿的情緒。\n\n\
    另一方面，也有可能逆位的女皇可能享受過度，產生拜金、懶散、縱慾過度、浪費的現象出現，要注意身體上例如肥胖的狀況。"
        url = "http://cisian.pixnet.net/blog/post/46242045"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/bRjRIKs.jpg"])

#emperor
    if res == 8:
        title = "皇帝(正位)"
        content = "皇帝是事業牌，對於工作賺錢方面有極大的助益，從身上的著裝來看，身上披著盔甲，\
    隨時準備好要上戰場作戰，現代社會的戰場就以是職場最為常見，故這張牌對於事業上的衝刺有所助益。\n\n\
    皇帝來說，一手握著球，代表運籌帷幄，一手握著權杖，代表掌握一切，又場景在山上，代表居高臨下，\
    處於有利的位置，椅子上的山羊強調極強的性能力，故這張牌面，代表是權力結構的頂點與大男人主義，\
    表現出來為高度的信心與自尊，講的是實事求是，一板一眼。\n\n\
    皇帝牌也是父親人格的原型，在心中皇帝牌出現時，能夠非常的有安排力，主動的能力，對於事情選擇目標明確。\n\n\
    在人際關係上，皇帝牌領導管理的能力很強，然而因為其為做事牌，一切以實際的物質行動面向為衡量基準，\
    是故在關係當中可能缺乏浪漫情調，但感情的走向還是有所掌握力的。"
        url = "http://cisian.pixnet.net/blog/post/46246704"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/5Fmq4Sr.jpg"])
            
    if res == 9:
        title = "皇帝(逆位)"
        content = "逆位的皇帝，喪失了皇帝的管理特質，不會帶人，失去掌控的能力與缺乏先機，大男人的特質失去了，\
    表示無法承擔責任，沒有擔當，懦弱，剛愎自用，\n\n\
    另一方面，也沒有勇氣去面對當前的一切，處處提防他人，顯得防衛心極強，疑神疑鬼。"
        url = "http://cisian.pixnet.net/blog/post/46246704"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/OQUpaB0.jpg"])

#hierophant
    if res == 10:
        title = "教皇(正位)"
        content = "教皇牌當中，教皇一手指天，代表他是上天旨意的傳達者，扮演的是傳遞天意的代表者，給予指引、\
    教導是教皇的任務；對於群體而言，教皇揭示了一種規則，這種規條一方面來講是束縛，然另外一個角度來講是一種保護，\
    在社會當中人需要一個權威，以維持群體發展，部分的國家政教是緊密相關的，也顯現出了教皇牌當中的現象。\n\n\
    而前方兩位教士，則是來聽教皇的教學，在現代的關係場合當中，是屬於學生與老師的師生關係，\
    或是有目標的團體關係，前方的鑰匙表示給予關鍵，給你關鍵的要素，是故出現教皇時，有利於學習的成份。\n\n\
    在關係當中，情愛的成分比較少，大部分都伴隨著角色權力的不對等，例如像是教學關係，指導者-被指導者、\
    給予幫助的人-接受幫助的人，如果在情愛關係的話，可能教皇會扮演為一位介紹人的情況比較大，\
    然在情感穩固的男女關係中，教皇所在之地為教堂，故是有結婚的信息存在。\n\n\
    工作的場合上，可能會有熱心指導的人物出現，帶領大家，分配任務與工作規劃。"
        url = "http://cisian.pixnet.net/blog/post/46389783"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/yWuKWVg.jpg"])
            
    if res == 11:
        title = "教皇(逆位)"
        content = "逆位的教皇，表示傳遞錯誤的資訊，溝通上產生障礙，要注意對方可能是假的教皇，\
    假的很會，別有目的而來，例如老鼠會等的組織，強調自己的偉大，如同一位救贖者，跟著我帶妳上天堂。\
    而在上方的教士，因為逆位而過度強調，使得以學生的角色為主，學生別有目的而來，來求取得上方的鑰匙。\n\n\
    另一方面逆位的教皇，代表可能在關係當中，雙方一方過度依賴權威者的角色，太過忽視自己本身的能力，\
    失去了自己做選擇的自由，一位個案與我的關係當中，出現了教皇逆位，我立刻覺察到，\
    我太過與主斷在對方的事情上了，太過具有指導性，忽略了許多事情是個案的功課與個案有辦法自己去做決定的部分，\
    當下我與她討論我們之間是否太過沒有彈性，恢復雙方彼此之間的尊重。"
        url = "http://cisian.pixnet.net/blog/post/46389783"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/j1a3GzA.jpg"])

#lovers
    if res == 12:
        title = "戀人(正位)"
        content = "在戀人牌當中，開始出現了天使，拉菲爾天使象圍繞在伊甸園的場景當中，雙手伸開環繞兩人，\
    代表這段感情，是受到祝福的，另外一方面也代表著見證，是一種認定與契約方面的確定，\
    純然的相信對方是彼此雙方在關係當中的體現。\n\n\
    女方後面的樹上纏繞著射，男方後面則是以火為象徵的生命之樹，整幅畫面帶來是生命力的現象，往成長茁壯、和諧的方向發展。\
    後面聳高的山脈，象徵著一種高峰經驗，兩人在關係當中，逐漸的併融合一，一種中心到中心的接觸經驗。\n\n\
    在工作的職場上，感到環境人際的輕鬆愉快，並且人與人之間不存在著太大的秘密遮掩。"
        url = "http://cisian.pixnet.net/blog/post/46390107"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/V5lEiQm.jpg"])
            
    if res == 13:
        title = "戀人(逆位)"
        content = "逆位的戀人，形成關係局勢上的破裂，有一種疏遠，漸行漸遠，\
    如果是已是夫妻的關係甚至有離婚的可能性，鴻溝逐漸的擴大，造成雙方彼此不合，\
    而就地理實際面向來講，可能是遠距離戀情。\n\n\
    在兩人之間的距離越來越遠，中間的天使加於兩端，似乎也暗示著，關係當中第三人現身的可能性，\
    或是出現了競爭者，愛情中的第二選擇。"
        url = "http://cisian.pixnet.net/blog/post/46390107"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/fdOwWnh.jpg"])

#chariot
    if res == 14:
        title = "戰車(正位)"
        content = "戰車為所有塔羅牌當中，表現速度最快的一張牌，在強大的力量速度面前，\
    使用的是意志力導引前方人面獅身的斯芬克斯，為了能夠駕馭車，變需要強大的結合力以達到人車和一的境界。\
    且該車名為戰車，也代表征戰，強調競爭與成功，後方即為攻下的城池。人物特質方面，站車表示對未來懷有無限的可能，\
    願意且有勇氣找尋挑戰，不願意安於當前穩定的現狀，尋求更好、更進一步的變化。\n\n\
    場景如同競技場，出現在環境當中往往帶有比較的氣氛，有如業績上排名的壓力，\
    需要有高度的心智韌性與技巧方能在激烈的搏鬥中生存下去。\n\n\
    在感情方面，屬於來的快(有可能去的也快的狀態)，進展快速的感情，快速達陣，並且可能的目的只是為爭服，\
    達倒目的即完成了他的任務，而進行下一階段的征服，感情戰場的一種收穫，如同攻城掠地般享受征服上的成就。\n\n\
    另外離開城堡也代表著遠行、旅行、出差、離開的動作"
        url = "http://cisian.pixnet.net/blog/post/54959820"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/ka5LRRU.jpg"])
        
        if re.search("15|d|逆位",res):
            title = "戰車(逆位)"
            content = "逆位的戰車，因斯芬克斯在上方，故強調該力量已無法被意志有效的掌握，\
變成方向不對，操作錯誤，技術不佳，也由原本正位的進攻變成採取守勢，進行的時候不順利，\
耽誤延遲，意志力不足，在戰場上容易變成受挫失敗，而缺乏勇氣退縮，防衛心重。\n\n\
而實際的場景當中，戰車也與實際的車輛有關，旅途中的交通工具與狀況關聯，逆位之時要注意行程進度，\
是否有交通意外車禍等等。\n\n\
與人獸合一的力量牌相比，戰車強調力量快速的推進，而力量牌則為剛柔並濟的和緩進行，是塔羅牌中兩種力量的展現方式。"
            url = "http://cisian.pixnet.net/blog/post/54959820"
            return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/9ZCFVRU.jpg"])

#strength
    if res == 16:
        title = "力量(正位)"
        content = "力量女神觸摸獅子，於是獅子就被馴服了，這裡的獅子，代表人與生俱來的生物本能，\
是一種獸性，而需要利用該力量則需一種溫柔的導引，是一種沉著、女性的力量，而面對我們本身的能力，\
我們需要的是信心，具足信心可以將該力量化為建設性的行動而不會造成毀壞。雖然說女神與獅子，\
兩者是不同的本性，其本質並不相符，但我們可以透過了解的關心，來撫觸包容涵養他者。\n\n\
獸性與女神身上纏繞的花圈，也表示這張力量的力，是考量到他人而言所展現出來的力，\
代表一種行使自己的意志時，顧及他人的感受。\n\n\
在職場上，這張牌也揭示面對外在強大力量的處事方法，而在人際關係的發展上面，\
為一種兩人逐漸加溫的感情，所表達的為一種流露的真情，有交心的感受。"
        url = "http://cisian.pixnet.net/blog/post/58195761"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/ahycbLB.jpg"])
        
    if res == 17:
        content = "力量逆位時，獸性的力量太過強大，產生獸性大發的影響，失去控制，\
破壞兩人之間的連結，感覺無能為力，也亦謂著做事不顧他人，而女神也逐漸的失其力量能力，缺乏掌握的信心，\
在關係上，雙方本質上的不同顯露，距離開始產生，兩人逐漸失去熱情溫度。\n\n\
若把這張牌引為對自己的投射，逆位時案主擔心的是對於自己無法控制自己，內在控制不佳。\n\n\
而獅子也很常被比喻為外在環境條件，在逆位的時候，現實的挑戰太大，當事人害怕，深怕受到傷害，\
常見的有如社交畏懼症，對於他者的恐懼。"
        url = "http://cisian.pixnet.net/blog/post/58195761"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/qZS7gw5.jpg"])

#hermit
    if res == 18:
        title = "隱者(正位)"
        content = "隱士站在群山之上，且是所有牌當中年紀最大的一張牌，過去有豐富的經驗，\
在山峰之上尋求的是通往天國的天梯，這張牌如果投射在一個人身上，有可能內心藏著一位老靈魂，\
時時閉著雙眼沉思，向內心深處探索，一種自省，而灰暗的背景也代表著孤獨，而這份孤獨卻是能夠帶予給人成長，\
往心中的方向前進(要從人群當中走出，有自己的意見與見解，走前人未曾走過的路，\
代表著無人可以與你同行，其基本的體驗為孤獨，是一種成長的代價)；\
手中的六角星(大衛之星)，代表給予山腳下的人一種指引，猶如一座燈塔(或是說導航衛星)，有貴人的訊息，\
相較於教皇牌，隱者的貴人處在遠離人群的地方，與外界隔離，教皇為人群當中熱心的指導者，\
隱士則須本人親自與他接觸，他才會將內心的智慧展露給你。\n\n\
在工作職場上，可能會有變動的住況(因為先裁公司當中的高薪老人)，而在求職的時候，則會有貴人相助。\n\n\
因為有指引的特徵，所以尋找失物時，會是有利的。\n\n\
在人生的道路上，我們不斷的前進，時而我們會來到一個發展的階段，這是一種自然的現象，\
我們要學習到的是，如何去承接這份孤獨，讓自己在生命當中不同的孤獨階段，安住自己，在孤獨中安住。"
        url = "http://cisian.pixnet.net/blog/post/72675351"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/nPmXLzz.jpg"])
        
    if res == 19:
        title = "隱者(逆位)"
        content = "逆位時，隱者低調的特性消失，可能會假裝有智慧、經歷的狀況，貴人的特徵失去，\
而將事情往錯誤的方向帶去，給予錯誤的建議，找不著方向，往往也使人會感到心煩意亂，\
煩躁的感受(試想GSP亂帶路的情況)，而整體的行程也產生了拖累的狀況。"
        url = "http://cisian.pixnet.net/blog/post/72675351"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/QypmcUo.jpg"])

#wheeloffortune
    if res == 20:
        title = "命運之輪(正位)"
        content = "命運之輪推動著世事自然界的變化，四聖獸(牛-金牛座、土、春，獅-獅子座、\
火、夏，老鷹-天蠍座、水、秋，天使-水瓶座、風、冬)代表四季的循環，手中拿著書本誦經，\
代表學習與成長，人面獅身的斯芬克斯掌握奧秘，蛇代表智慧，胡狼頭的阿奴比斯是亡靈帶領至靈界的引領者。\
輪中的TARO-塔羅，TORA-智慧，也象徵著塔羅為一智慧之書，可以透過塔羅了藉世事自然的變化，\
述說著生命的道理；在命運當中，是一種向前的脈絡，過去與現在的延伸，一種推動的力量，\
人在命運的脈絡當中，最重要的就是參與，只要人能在脈絡之中，命運就能帶給你生命的意義與提升，\
也就是一般常見'一切都是最好的安排'的說法，難的地方在於看懂命運這點，因其本身是會澀難懂的，\
是神意，所以人們會去找各種經典、經書，希望發現生命的真理，原因就是如此。\n\n\
與TARO相同一圈的文字為神的名子，而輪的中央為鍊金術之符號，而命運以輪轉的形式出現，\
類似時鐘一樣轉阿轉的，也是代表什麼時間應該要做什麼事情，會發生什麼事情就當在這時間完成，\
都有一定的規律，比如日出而作日落而息，人生個階段的時期發展與功課等。\n\n\
正位時，偏向的是好運，喜歡的安排，然而命運之輪往往其動作機理非是人所能掌握，\
正位雖是偏向順利，然而對於命運的結果仍屬未知之狀態，尚存有不確定之資訊，然而只要懂的命運，\
看懂並且接受，抓住、把握命運之輪正位時給你創造的機會，一切仍是往正向的方向走去。"
        url = "http://cisian.pixnet.net/blog/post/73077285"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/btfO9z3.jpg"])
        
    if res == 21:
        title = "命運之輪(逆位)"
        content = "命運之輪逆位時，偏向是厄運、被環境所決定，命運的捉弄，不得已，\
時間、人、環境的不對或者是尚未準備好，作什麼事情，感到困難與險阻重重。\
人在此中，除了重新檢視自己學習的狀況，探討面對當前環境的態度之外，也要發揮自己的創造力，\
創造新的命運走向，以脫離命運的老路子。\n\n\
逆位的命運之輪也有可能是當事人對於眼前命運的態度錯誤，太過自大、太有自信，認為自己可以征服一切，\
掌握所有，然而人不過是宇宙命運的一部分角色而已，必須要以謙卑尊敬的態度來面對這浩瀚蒼窮，無盡的時空。\n\n\
還有可能當事人對於過去的經驗有所缺乏(未於該生命發展階段學習到該學習到的議題)，\
比如有位個案對於另一半相當的依賴，必須要時時刻刻對方都要在她的眼前，\
否則個案認為世界好像會毀壞兩人之間的關係，摧毀彼此雙方的存在，她在過去的經驗當中，\
缺乏對於信任感的學習，她是一位孤兒，生命階段她幼時缺乏照顧者的照顧，\
形成生命此刻她欠缺了對於環境他人的信任，以至於命運走到此，在親密關係中他是感到如此的不安與混亂。"
        url = "http://cisian.pixnet.net/blog/post/73077285"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/xKoytS2.jpg"])

#justice
    if res == 22:
        title = "正義(正位)"
        content = "正義，其場景在一個如法院般當中，一手持劍，代表決斷，一手持天秤，代表公正的裁量決斷，\
而被後緊貼的帷幕，沒有絲毫的背景空隙顯露出來，也代表著不想要受其它外力的干擾，\
為的是為做出的決定顯的公正，而一腳露出也代表此張牌面並非靜止，非只是精神思想上的描述，\
而是有包含行動能力，會去做一些事件的力量。\n\n\
而此張牌面也揭示了，行動之時，必須要以公正的態度面對當前的事物，考量正反雙方做出明智的決定。\n\n\
        左右雙住也與女祭司的BJ雙柱很像，也是代表黑白的一個現象，也可以說是女祭司的行動強化版本，\
        多加了嶄露出來的行動面向。\n\n\
        感情人際方面，顯的是公正的對待，但有時會顯得一板一眼，缺乏人情味道。\n\n\
        此張牽涉到調解訴訟方面，若以正位來說，便是雙方會得到兩方公正的裁量結果，也就是正義的勝利。\
        只是有時雙方都認為自己是正義的一方，且到底哪個是正義裁量的基準呢?這點便是很難確定，\
        ，或許正義的公正審判兩方都認為不符自己心中的公正，而認為最後的結果不符雙方其待也說不定。"
        url = "http://cisian.pixnet.net/blog/post/74103582"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/lmFfrCk.jpg"])
        
    if res == 23:
        title = "正義(逆位)"
        content = "當正義逆位時，代表不正義、不公正，懷有偏見的想法，在過程當中，\
當事者可能無法得到內心想要的東西，得到他認為自己應該得的東西，而逆位的劍，也代表錯誤的選擇或是決定，\
錯誤的判斷導致行動上的失誤，甚至是造成當事人的傷害；而後方的帷幕掉落，受到私心、自我的主觀見解、\
利害關係者的意見的影響，產生衡量的基準是自己的利益，唯利是圖。\n\n\
工作方面，倉皇的下決定，顯然無法有良好之收穫，工作結果不佳，甚至是越用越糟，導致後來需要彌補傷口與創傷。\n\n\
關係方面，出現正義之逆位之時，可能是為了解約方面，例如雙方停止合作，婚姻上可能出現的是離婚的裁量。"
        url = "http://cisian.pixnet.net/blog/post/74103582"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/DovBaU5.jpg"])

#hanged_man
    if res == 24:
        title = "吊人(正位)"
        content = "吊人這張牌的構圖相當的奇特，第一眼看到可能會感到它是否印反了，的確，吊人顛倒看世界，\
        他的眼界與看法跟常人不同，他會吊在樹上，有可能是自願的，為的是一個更大的願景，而犧牲現在的狀況，\
        也有可能遭受處罰，正在償還他的罪，又或是償還他人的罪，代罪羔羊的角色。\
正位的吊人代表著等待，等待時機的到來，失去的是當下的自由，然仔細看吊人的臉上，\
並不顯得絲毫的痛苦，乃在於吊人本身的心態是心甘情願，任勞任怨的人物。\n\n\
在人際方面，也顯得在關係當中，當事者需要承擔多些的責任，並且有可能承擔起委曲，以維持關係的存在，\
在關係中要注意可能太過在意他方，而忽略了自己本身。\n\n\
而物質金錢方面，吊人強調現在的付出，但最後的結果卻是不一定能夠得到，有可能付出所盼的目標與金錢可以達到，\
但也有可能是一場空。\n\n\
吊人雖然處於一種命運上的不自由，命運的形式將其吊在樹上，困在此處，而吊人卻透過對於事情另一側面的看法，\
而從想法精神上跳脫了命運的限制。"
        url = "http://cisian.pixnet.net/blog/post/77187729"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/jFcarxV.jpg"])
        
    if res == 25:
        title = "吊人(逆位)"
        content = "逆位的吊人兩個比較常見的講法:\
１、從樹上解脫了，有可能是目標達到了，從吊人正位轉換為逆位也代表著事情有個結果，\
從人際關係上講，代表會多注意自己，不再只是向著他人，對他人一味的付出。\n\n\
２、另外一個方面來說，吊人的逆位也表示著，可能太過自大，不願意接受安排，\
對於命運要你償還的部分顯的抗拒，不服從的態度，頭上智慧的光芒消逝也代表智慧的消失，\
尚未達到時機點就去做也有可能做的事情是白忙一場。"
        url = "http://cisian.pixnet.net/blog/post/77187729"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/Mnc7WIj.jpg"])

#hanged_man
    if res == 26:
        title = "死神(正位)"
        content = "這裡的死神，代表象徵性的死亡，從牌面來看，場景倒下的是充滿權力與金錢的國王倒下了，\
象徵精神世界的教皇仍存活，且恭迎死神的到來，也代表著精神不死，而小孩在此也象徵新的生命，舊的結束，\
新的到來，汰舊換新，遠方的太陽也表示光明的希望，是故這張牌實為有生有滅，在這裡當中，\
我們失去的是那些阻礙我們前進的東西。\n\n\
這裡也代表著一個轉折的現象，在關係當中，妳們可能結束了這段情感，變成了純粹的友誼，又或者是從男女朋友，\
成為了一對夫妻，是種階段性的轉換現象。\n\n\
少女撇過頭，也代表世上許的人，總是無法正視死亡的現象，用各種否認來逃避\
，又或者是陷在當下的困境，卻不願從坑裡爬出，然而有一天，我們畢竟會走向終點，死神的死亡考驗終究是存在的，\
他會擋在人生道路的面前，不讓你前進，唯有我們正視自己當下的位置，與思考當前所面對的狀況，透過認識死亡，\
了解到人生是有限的，道路與決定是我們自己下的，我們可以更為有效的調整自己，承擔起自己的選擇與行動的責任。"
        url = "http://cisian.pixnet.net/blog/post/77217543"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/0uuAhQC.jpg"])
        
    if res == 27:
        title = "死神(逆位)"
        content = "逆位的死神，同樣的，有兩種解法常見。\n\n\
１、已經走過死神的考驗階段，又可以前進了，可能找到新的契機，新的開始的一段關係。\n\n\
２、在死神考驗的當下，不願意捨棄部分的自己，可能代表不願意去看，不願去改變過去的錯誤自我，\
而造成當事人仍困於現在的僵局當中，無法前進。\n\n\
這兩者是逆位牌義當中所見的兩個分歧，端看讀者的直覺與選擇運用。\n\n\
另外因為死亡與疾病習習相連，出現死神之時，也必須注意身體狀況，\
可能是外來、外在的原因所導致的疾病(如骨折、病毒感染……)"
        url = "http://cisian.pixnet.net/blog/post/77217543"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/Ko0HJNk.jpg"])

#temperance
    if res == 28:
        title = "節制(正位)"
        content = "如同調酒一般，大天使麥可將兩個杯子的水連續的倒至另一個杯中，代表著是一種淬鍊，\
一種提煉，有將物質精神揚升之力量，所以這張牌帶有修練之意味，也代表著事情的方向往步步高升的地方走去。\n\n\
兩個杯子處於不同的位階，高低之差的整合，在團體當中，必然對事情有不同的見解，兩人相處的關係當中，\
必然有價值觀有所不同，而節制的力量，就是可以在不一致當中，找尋合作的關係，而將兩端提升起來，\
也就是利用了這份弱點，將其整合到比兩者原先更為高階的狀態。\n\n\
而同時，節制的力量也需要當事人技術純熟，其秘訣在於不斷的練習，終至領會事情本身之含義，\
而在不斷練習的過程當中，雖然動作繁瑣，但用心去做，會發現許多事情的變化面，發現新的意義，具有豐富的特質存在。\n\n\
大天使一腳在潛意識的水中，一腳置於顯意識的陸地，也代表兩者的平衡狀況。\n\n\
人際關係上，能夠產生熱絡的互動狀況，也代表雙方彼此溝通狀況順暢，交換意見與價值觀，\
分享承擔喜怒哀樂，雙方能夠打開彼此的心房，近而促進兩人彼此之間的關係，而同樣的，\
也需要當事人對眼前的環境有所回應，而不是封閉，並且主動積極的參與其中。\n\n\
工作上，事件專案協調清楚，有互相幫助的可能性，當事人也可以在進行當中增加磨練的經驗與技巧的純熟。"
        url = "http://cisian.pixnet.net/blog/post/78073653"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/jQZrWfj.jpg"])
        
    if res == 29:
        title = "節制(逆位)"
        content = "逆位的節制牌組，大天使手上的水杯翻覆，代表技巧不佳，缺乏成就事情的天份。\
而提升的力量變弱，也代表心境上的降低與趨於表面，在做事情的時候，可能變成一成不變乏味的工作，\
又或者當事人只注重在技巧方面，而無法去體會實質的內涵。\n\n\
人際互動上，可能溝通不佳，又或者是注重表面的人際技巧與應對，似乎只是為了認識而認識，\
只在意名目上的關係，卻不願注重人與人之間的交心與真誠，又或者節制的力量消逝，\
形成人與人之間的不往來，冷漠，缺乏默契的狀態。"
        url = "http://cisian.pixnet.net/blog/post/78073653"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/1PDldjE.jpg"])

#devil
    if res == 30:
        title = "惡魔(正位)"
        content = "惡魔的對應層面，可能是生物本身的內分泌、賀爾蒙行為，代表一種生物的需求，\
像是繁衍的需求、飢餓進食的需求...也有可能是精神層面上如性歡愉的需求、享受的需求、金錢權力的需求...，\
本身而言可以說是牽動人們的慾望，也因為有了欲望，社會上的供需創造才會熱絡，\
而人類社會的高度建設也可以說是與之息息相關。\n\n\
惡魔的形象是怎麼出現的呢?除了原始的本能外，亦有可能是人的慾望而生，強大的慾望彷彿是一個生命力，\
控制著我們的行為，也就是人渴求渴望，想要滿足，想阿想的，反而被這個執念所控制住了。\n\n\
惡魔的創造力當然是有的，就事物上來講，他要求妳拿東西來換，就如同惡魔手上的火把一般，\
需要有交換的條件，比如在工作上，在惡魔的作用之下，妳可能受困於其中，\
把所有的生命精力灌注於其間，燃燒自我，然而妳能夠從其中，或取交換到金錢或是職位上的升遷。\n\n\
以愛情兩人的關係當中，惡魔有可能懷有性的成份在裡面，感情層面偏向關係當中最低階的救贖形式，\
性的滿足，這裡的惡魔，成為一種詛咒，用性與慾望綑綁了兩人的關係，然在具有建設性愛情的關係當中，\
生物性惡魔的力量，被提升併容於兩人之間，形成了最高潮的歡愉與肉體上的親密接觸形式。\n\n\
兩人之間套牢的鎖鍊，代表一種糾纏，在關係當中，可能雙方想用金錢、性、權力以維持關係，\
行動外表為一種引誘、誘惑、奉承，或因為為了的到這些，而自願糾纏於其間，然這些當事人可能感受不到，\
因為其未嘗想過這些，故從他者的眼光來看，或許認為當事人執迷不誤，為了某個目的而存在於當下的關係當中。"
        url = "http://cisian.pixnet.net/blog/post/78487608"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/rt9i69D.jpg"])
        
    if res == 31:
        title = "惡魔(逆位)"
        content = "逆位的惡魔牌，可能代表即將解開枷鎖，不再受束縛了，脫身於權力的關係當中，\
拿調枷鎖也代表著不再受其制約，不自欺欺人逐漸的看清現實。而另外一者的解釋，因為惡魔逆位時，\
象徵的意義消失了，人看不清楚惡魔，成了一種隱微的控制，人變得更加的被驅力所推動，無法克制自己。"
        url = "http://cisian.pixnet.net/blog/post/78487608"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/5uLrvXd.jpg"])

#tower
    if res == 32:
        title = "塔(正位)"
        content = "抽到塔牌時，代表一種警訊，敲響了一記警鐘，告訴有危險與危機正要發生，\
然而這場危機並非是來得突然，一切都有前因，因累積閃電的能量，需要時間，打雷之前，也有所前兆，\
只是當事人可能忽略了危機的先前現象，又或者是說之前選擇不去看，不去聽，執意往雲中去，\
便造成了危機真正的發生了。\n\n\
塔牌代表一種無常，案主在抽到塔牌時，可能某些信念抓得太緊了，以至於無法接受失去狀態，若出現塔牌，\
或可以與案主討論，他緊緊抓住想要抓住的是什麼?最終的結果可能是什麼，是否願意為這樣的結果負責；\
有的人是已經來到了巔峰，獲得最想要的東西後，才發現終歸虛無，自己已經失去的太多。\n\n\
人際方面，塔牌人物各自逃難，一種分離，鳥獸散，本是同林鳥，如今各自飛，決裂與組織的瓦解。\n\n\
工作與物質方面，雷電將象徵物質與權力的皇冠摧毀，也象徵著降職、解職，財富的失去。"
        url = "http://cisian.pixnet.net/blog/post/87491673"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/wesFVQj.jpg"])
        
    if res == 33:
        title = "塔(逆位)"
        content = "逆位的塔，可能經過了厄運，經歷了災害，正準備開始重建了，重零開始，另外一方面，\
也有可能未來即將出現的災難，在到來之前，以先被你逃掉了，躲避了一場災害，感到虛驚一場，\
例如有驚無險的車禍，股災之前已先退場等情形。"
        url = "http://cisian.pixnet.net/blog/post/87491673"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/3dyooAI.jpg"])

#star
    if res == 34:
        title = "星星(正位)"
        content = "正位的星星牌，指的是新的希望、靈光乍現，是一顆未來之星。\n\n\
星星女神手中的壺水，傾倒入現實面的地與情感面的綠洲當中，產生療育的感受，此張牌告訴妳，未來的日子會更好，\
給予了精神上的支持，美麗而和諧的想象，然此張牌是導向未來，所以出現在'結果'的位置之時，\
成功往往是向後延伸的部分，即成功的時間點，不在結果的當下，而在於未來。\n\n\
此牌的能力，是將我們內心的盼望，化成一種意識，透過對於意向的探索，將其意向整合辨識成為我們內心當中的想望，\
我門究竟想要的是什麼，我們的渴望、我們的願望是什麼，在此議題受阻的案主，往往失去一種導向性，此狀態下，\
人無法看見自己內心本身的需要，說不出自己想要成為的是什麼樣的人。\n\n\
願望受阻的人，雖然並不一定是如此，但星星牌給予了這樣的案主一個建議，即是，\
案主本身必須要透過不斷的接觸其本身當下，感受是什麼，對於事件與外在有什麼樣的想法，當下真正的感覺是什麼，\
透過接觸真實的自己，而澄清自己內心真正的願望。"
        url = "http://cisian.pixnet.net/blog/post/87495822"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/OV7Kzxv.jpg"])
        
    if res == 35:
        title = "星星(逆位)"
        content = "逆位的星星牌，眼前的綠洲不過是一種海市蜃樓，一切的美好雖在，然這份美好卻是一種假象，\
一種幻想幻影，可能當事人覺察錯誤，體驗不對，或是不願深刻感受，無法探究其深處的內心，\
成為表面想要的而非內心深處的需要，也有可能案主把未來想的太過美好，與現實層面脫軌，成為過度的盼望。\n\n\
另一方面，也有可能本身失去希望，產生悲觀的感覺與各種想法，未來前景不被看好。"
        url = "http://cisian.pixnet.net/blog/post/87495822"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/ZtwSc3T.jpg"])

#moon
    if res == 36:
        title = "月亮(正位)"
        content = "月有陰晴圓缺，週期性的變化，代表著捉摸不定、充滿曖昧，月亮牌是大秘儀中第2張沒有出現人物的牌，\
畫的是狼、犬、螯蝦，與月亮環境的氤氳氣息，遠方的路與月亮隱藏其中，雙塔代表與異世界的門，一端連接人世間，\
        另一端連接靈異空間，月亮牌是與異世界的連結，原鄉的呼喚，而狼犬的嗷叫，\
        代表有來自另外空間的訪客穿越雙柱到來，也象徵為一種警告，具有危險隱藏於其間。\n\n\
        水塘帶表潛意識，螯蝦從潛意識的水面出現，是一種訊息，來自潛意識當中，一種來自人類最深處的基本困境，\
        自我存在的根本覺察，而月亮牽引著水面，是一種潮汐的力量，一種緩慢的波動與不穩定的力量，\
        從外表看來，當事人內心的故事很多，對於世界認知有相當詭異的論述，脫離物質世界的表象，就人格特質上來講，\
        有一段時間來一次的情緒不穩定，而長處來說，可以透過此狀態，探究其內心的根本元素。\n\n\
        在這張牌的狀態下，人感到相當的無助、不安、焦慮，不知心中懼怕何物，是一種成為無物的驚恐，\
        是一種心中的膠著狀態，一種操煩，面對未知未來，不知是否有終點的不確定感，一種虛幻不實的體驗\
        ，而此牌的長處為未準備好之時的自我探索，潛意識深沉的醞釀與作用。\n\n\
        在人際關係上，氣氛詭譎無法掌握，雙方彼此猜疑，團體當中或許有敵人隱藏在其中，工作上，\
        感到處處懼怕，沒有挑戰的信心。"
        url = "http://cisian.pixnet.net/blog/post/96957535"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/J0zhw7z.jpg"])
        
    if res == 37:
        title = "月亮(逆位)"
        content = "逆位的月亮，月亮即將落下，破曉時分，雲霧逐漸散去，撥雲見日，前方的道路逐漸明朗，\
當事人可能逐漸明白一些道理，慢慢的有所變化，人與人之間的關係疑點也逐漸獲得了解，事務方面在不明朗之時出現了轉機，\
出現了發展的脈絡，原本困難的道路上得以前進，獲得改善。"
        url = "http://cisian.pixnet.net/blog/post/96957535"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/JGvmiNe.jpg"])

#sun
    if res == 38:
        title = "太陽(正位)"
        content = "熱力大放送，太陽牌是一張充滿熱力的牌，把你的手放上去感受，也會感到手中充滿一股熾熱，\
太陽高掛，如日中天，正是生命力最為旺盛的時刻，前景出現的嬰兒，象徵著新生，跨越了後方的圍籬，\
表示前方的努力已經跨越了險阻，接下來的一切險的相當順遂順利，美好一切的開始。\n\n\
整體的感覺是相當的高興與快樂，如同孩童那搬純真的快樂，單純的快樂，性格方面險的開朗，陽光男孩，\
沒有絲毫的隱藏，熱情滿分。\n\n\
在工作事物方面，進行順暢快速，積極進取，各方面如同太陽四射的光芒，擴展順利，進而完成目標，\
達到頂峰，相當的有成就。\n\n\
就情感面來說，代表兩人之間相處的坦然，一切攤在陽光之下，表裡一致，無有隱藏，這樣的戀情顯的少見，\
故有部份見解為一種'好朋友'的關係，一種純粹的友誼，而非是戀情關係，而面對太陽牌的人，\
感到一切都是直來直往的，且話語中感到積極的想法。"
        url = "http://cisian.pixnet.net/blog/post/96963445"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/uq2XP7v.jpg"])
        
    if res == 39:
        title = "太陽(逆位)"
        content = "逆位的太陽，依舊仍有熱度，太陽要下山之時，就是逆位的時間點，\
此刻的場境產生如熱情下坡的狀況，出現逆位，有可能當事人的付出顯的太過急躁了，未注意到自身的能力與能量，\
        過度消耗自己的汽油，走的太快太急促；而另外考量到時間點為黃昏，也代表著夜晚的黑暗即將到來，\
        有些關於未來的事物需要多加注意，要謹慎的面對未來的風險。"
        url = "http://cisian.pixnet.net/blog/post/96963445"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/6JhgKFC.jpg"])

#judgement
    if res == 40:
        title = "審判(正位)"
        content = "審判牌即是深刻的反省自己後，從中發現新的價值，棺材表示我們依靠的外在規則、道德判斷、\
價值評量...，而天使的號角表示來自內心的聲音，此刻人從棺材中站起，迎接天使的祝福，\
表示人從外在的評價轉換為傾聽內在之聲，此處也代表道德良知必須要從內心出發，而非是法律規範。\n\n\
並非摒棄傳統教條與法律，這些外在的條文幫助我們在大海，在世界上站立，是活在俗世的規矩與準則，\
只是內心的聲音一直都在，我們可以從外在轉向內在，奮力從棺材中爬起，重新的發現自己，重新的認識新的自己，\
改變自己，活過必須活過的自己，審判講的是一種突破俗世規條與掃除塵世意義而出的內心自由狀態。\n\n\
在感情中，雙方可能進入下一個階段，為一個階段性的變化，例如爭執分手後，出現的審判牌組代表有再一次的機會，\
如好好把握命運的轉機，正位的審判往往出現的是兩人得以復合的情景，兩人之間可以更加深情的轉向面對彼此，\
而因之前的經驗更加深刻兩人之間的關係。\n\n\
在人際、工作上，可能出現轉換的障礙，必須要重新檢視自己與自我反省，評估自己的作為與審視關係當中需要調整的部分。"
        url = "http://cisian.pixnet.net/blog/post/98159101"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/dPf4RYp.jpg"])
        
    if res == 41:
        title = "審判(逆位)"
        content = "逆位的審判，表示案主可能不願意檢視自己的內在，不願意深刻的體會反省，事情無法重生沒有新的作為，\
所以過去的習慣成為當前的行為根本，因為事情的錯誤沒有正確的被檢討改過，如爭吵分手的兩人復合可能會重蹈之前的爭吵情形，\
另外也有可能反省的挑戰太大，無法度過難關。\n\n\
另外也有可能案主本身不願意認罪，不願意接納自己本身，不願承擔自己行為的責任；又或者將外在的準則與判斷視為自己，\
用他人定義的種種規則、成功失敗的評斷來成就自己，蒙蔽了自我心中的理想與呼喚。\n\n\
有關於疾病的部分，因為審判逆位時，有過去的跡象復發(疾病死而複生)，故有舊疾復發的狀況產生，這點必須要注意的地方。\n\n\
在審判牌逆位中，告訴我們如人本身沒有碰觸到自己，是失望的，不知道自己是誰，呼聲的浪濤一直都在，\
卻無法拍動內心，這樣的人時常處在掙扎當中，但另一方面來說，審判的過程是痛苦的，過去的作為展現在眼前，\
人就必須為其負責，更必須償還過去的種種，為沒有活出的自己做負責，然審判雖然事情已經終結了，\
事實已就是如此，無法再改變了，消逝的時光不會回來，我們能夠做的，就是用未來來補償過去，盡力的彌補這一切。"
        url = "http://cisian.pixnet.net/blog/post/98159101"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/29swBWr.jpg"])

#world
    if res == 42:
        title = "世界(正位)"
        content = "大牌的最後一張，世界意味著自己的世界儼然成形，旅程當中的收穫已在最後這一階段圓滿，\
形成一個自我的世界，完成了愚者的任務，來到的一個終點。\n\n\
此牌講述的是修練完成的狀態，塔羅是一種修練之道，道路的頂點是讓人可以與高層次的宇宙經驗融合，\
人參與到命運的脈絡裡面，在這一層次當中充實自己的世界，在這個世界當中提升昇華起來。\n\n\
在世界牌當中，當事人清晰明白當前事務的狀況，一切了然於心，對於事情的總體評斷無有疑慮，且層層周到，\
就環境面來講，也象徵著當前環境中他人的互動之自然，一切彷彿是自在般的美好，沒有壓力。"
        url = "http://cisian.pixnet.net/blog/post/98162614"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/q1hLiZc.jpg"])
        
    if res == 43:
        title = "世界(逆位)"
        content = "逆位的世界，可能代表尚有東西缺乏當中，離終點只差一步之遙，缺了一角，元素尚未齊備，\
少了關鍵的一步，沒有抓到重點，整體來講，一切雖然還是不錯，只是缺了一點什麼的狀況，\
有可能的結果是延遲的成功，或是感到不夠完美。\n\n\
另外也有可能精神層次上未有達到終點，對於眼前的人事物仍有疑惑，無法通盤了解的狀況。"
        url = "http://cisian.pixnet.net/blog/post/98162614"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/YsxNZXj.jpg"])
    
#小秘儀
#king_of_wands
    if res == 44:
        title = "權杖國王(正位)"
        content = "權杖國王是權杖世界的管理者，權杖代表權力，代表工作環境，代表事業，\
所以權杖國王往往是一個積極的管理者，具有一定的身分地位，有權威的角色，帶領者，熱心的參與帶領團體的人物，\
工作事業成功的人物，腳踏實地；權杖國王的場景是在火熱的沙漠中，權杖國王身邊地上有一隻火蜥蜴，\
是一種謀定而後動的動物，表示了權杖國王處世的態度與方法，其所為之事是經過深思熟慮的，\
是故權杖國王是透過行動力，透過指導的特性，將自己的意志參與入社會環境與團體之中。"
        url = "http://cisian.pixnet.net/blog/post/181106536"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/QpyfTwk.jpg"])
        
    if res == 45:
        title = "權杖國王(逆位)"
        content = "逆位的權杖國王，管理能力不佳，權力使用的不對，不會帶人，所帶領的團理無法前進，\
或是濫用權力，使的權杖是一根打人的棒子，用自己的權力地位來修理部下，不顧下屬他人的意見，\
也有可能是提議無法獲得上級的支持，所做的事情不被肯定。"
        url = "http://cisian.pixnet.net/blog/post/181106536"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/21bQYVt.jpg"])

#king_of_cups
    if res == 46:
        title = "聖杯國王(正位)"
        content = "聖杯國王懂得管理情緒，情緒管理得很好，聖杯國王往往帶有容易親近的特點，\
有一種溫暖，溫情的感受，成熟的情感態度，具有責任心，懂得人情事故與待人處事，讓人感到放心，\
暖男角色，另外一方面來講，聖杯國王可能感情的經歷豐富，城府深厚的特點，聖杯國王的角色常出現得像是長輩的角色，\
對於後輩有一種照顧與關心，溫厚的關懷，慈祥而親切，高EQ與親和力，\
值得注意的是桃花運出現此張牌組有可能是具有家室的男人；聖杯國王的場景是在波光淋漓的海面上航行，\
閱歷各地，相當有經驗，而從海中跳出的魚也象徵的是情感的生命力，具有情感的多元與創造性。"
        url = "http://cisian.pixnet.net/blog/post/181106680"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/ayZ5w4J.jpg"])
        
    if res == 47:
        title = "聖杯國王(逆位)"
        content = "逆位的聖杯國王，情緒使用不適宜，往往有情緒上的偏頗，偏心的狀態，或是濫用情感，\
玩弄他人，比如老而不修的男人，心中想要逾越界線，出現不合時宜與不符關係狀態的肢體碰觸，感覺起來噁心，\
而且往往這樣的角色社交狀態帶有一定程度的複雜特性，其對人的目的性增加，別有它圖。"
        url = "http://cisian.pixnet.net/blog/post/181106680"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/a5q4YrE.jpg"])

#king_of_swords
    if res == 48:
        title = "寶劍國王(正位)"
        content = "寶劍國王是想法的管理者與將理念推動的人物，是一位軍師級的人物，其本身具有相當的專業性，\
與寶劍國王討論事情寶劍國王可以給與其專業上的協助，講出的是專業的智慧指導，提出自己的見解，\
告訴他人背後的理念與原理是什麼，並且能夠從多個角度上去分析，採取客觀的態度，極高度的分析能力，\
提出最佳的建議，與精闢的見解，天上有兩隻飛鳥，也是代表寶劍的風元素與綜覽全局的能力，\
常見的人物比如像是學者、教授等，而寶劍國王與寶劍皇后相比較，寶劍國王有待人的經驗，\
所以提出得面像還是比較偏向有考量到人的一面的。"
        url = "http://cisian.pixnet.net/blog/post/181106827"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/sNHbPUZ.jpg"])
        
    if res == 49:
        title = "寶劍國王(逆位)"
        content = "逆位的寶劍國王思想偏頗，可能有偏見，無法公正的採納各種想法，對於討論總是懷有批評的態度，\
或是對某些知識有所偏頗，對於不同門派、不同的意見給與貶低，意圖將自己的認知理念想法塞給他人，\
無法公正客觀的看待事物，也有可能其本身專業度不夠，給與錯誤的意見與建議，指導的方向錯誤等等，\
另外走一些偏門小徑也有可能是逆位的寶劍國王會做的事情。"
        url = "http://cisian.pixnet.net/blog/post/181106827"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/RV6Mcie.jpg"])

#king_of_pentacles
    if res == 50:
        title = "錢幣國王(正位)"
        content = "錢幣國王是財富的管理者，場景是錢幣國王安坐於自己的城堡中，\
整個構圖是宮廷牌中最為豐滿的一張牌，象徵的是財富的成功與享受，擁有權杖也表示有一定的財富自由，\
高度的商業投資資歷與敏銳度是錢幣國王的能力，地上踩在腳上的牛也表示征服了市場，\
歷經投資的風險與努力獲致成功，若對方沒有投資的動作，可能是之前的儲蓄積累豐厚，\
生活穩定實在的老男人，在錢幣國王時，可以象徵的是投資者或是靠山，常見的另有如退休的老阿杯。"
        url = "http://cisian.pixnet.net/blog/post/181106917"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/SZBP6qN.jpg"])
        
    if res == 51:
        title = "錢幣國王(逆位)"
        content = "逆位的錢幣國王可能表示會失去財富，失去已經獲得的財富，投資不當或能力不佳，\
經營管理不當，擁有資源卻肆意揮霍，燃燒本錢；也有可能是對於金錢有強烈的控制慾望，\
以致於雖然坐擁金山，確不捨享受的人物；要注意的是也有可能是失去靠山，人際關係或是投資關係上的變化。"
        url = "http://cisian.pixnet.net/blog/post/181106917"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/UpT8ixR.jpg"])

#queen_of_wands
    if res == 52:
        title = "權杖皇后(正位)"
        content = "權杖皇后是沉浸於火元素中的皇后，火代表熱情，是故權杖皇后從性格來講讓人感到充滿熱力，\
主動而且積極，有時還帶有火辣的氣質，手中拿著的向日葵也代表陽光，一種開朗，黑貓則是性感的象徵，\
憑著對於生命的一種直覺、樂觀、爽朗的方式下去進行，生命熱度的展現，高度的自我價值感，相信自己，\
未嘗擔心過失敗，對自己抱持著高度的自信，行動直接反應快速且靈活，然而這樣的作風有點大喇喇的，\
對於細心的事情可能比較沒有耐心；常見的如職場上的女強人，對於做事顯的相當積極，有自己的主張與個人風格。"
        url = "http://cisian.pixnet.net/blog/post/181105348"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/2sFuEQF.jpg"])
        
    if res == 53:
        title = "權杖皇后(逆位)"
        content = "逆位的權杖皇后，代表元素的過度氾濫或不足，透過人物的方式顯現出來，如果過度的話，\
那就是燃燒的太過熱烈，可能火爆脾氣的產生，兇悍的個性，不饒人的態度，凶巴巴恰北北，\
另外一方面如果元素的作用消逝或不足時，代表失去熱力，有可能是之前過度燃燒自我，反而已經疲累沒有能量了，\
熱情消退消失。"
        url = "http://cisian.pixnet.net/blog/post/181105348"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/cDVdLI3.jpg"])

#queen_of_cups
    if res == 54:
        title = "聖杯皇后(正位)"
        content = "聖杯皇后沉浸於情感中，而且是浪漫的情愛感覺，聖杯女王專注於情感的水杯，\
且這杯子是所有的聖杯牌組中裝飾的最為華麗的一個，附有蓋子，更加得令人對杯中的內容物產生想像，\
聖杯皇后所關注的是情愛，一種特定對象的愛，且椅子華麗，腳踩在彩色的鵝軟石上方，\
把感情的世界想的很唯美，富有創造力，聖杯女王是相當得溫柔婉約的，體貼的個性，柔柔的姿態，\
偶爾不時還會臉紅害羞，心態上也很容易掌握，沒什麼大腦，喜歡談論的是各種感情的八卦小道消息，\
是一位正在戀愛當中的美女子壓，出現這張牌時，如果個案是男性，可能的狀況代表是他內心當中理想女性交往的對向。"
        url = "http://cisian.pixnet.net/blog/post/181105495"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/Cv090bR.jpg"])
        
    if res == 55:
        title = "聖杯皇后(逆位)"
        content = "逆位的聖杯皇后，可能感情上過度氾濫，過度的情緒化，已到達缺乏理性的程度了，\
很難以掌握情感，不知道要如何與之應對與溝通，無法應付，另外一方面可能對於情感的想望太過於強烈了，\
想要很多對象，用情不專，無法忍受孤寂而極欲得抓住他人，顯得花癡；另外一方面來講有可能元素消散，\
失去感覺不再愛了。"
        url = "http://cisian.pixnet.net/blog/post/181105495"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/32E9KDw.jpg"])

#queen_of_swords
    if res == 56:
        title = "寶劍皇后(正位)"
        content = "寶劍皇后是沉浸於理智的代表，具有各種知識與評斷的能力，本身是孤高的，\
特別是寶劍皇后的上方鳥僅有一隻，或許是一隻孤鷹也說不定，對於事物採取知的態度，\
任和時候都是理智的，是一種主觀，告訴他任何的資訊他都會經過處理後擬出最佳化、效益極大化的作法，\
然這樣的作法僅在於理論上可行，碰到人性層面或許不適用，是故寶劍皇后比較適合純學術層面的人物，\
且寶劍皇后來講，其劍是相當筆直，是公正不阿且判斷果決快速的，這樣的個性在人際場合比較難以靠近，\
與聖杯皇后是兩種不同的性格，寶劍皇后較不易產生親密感，甚至是有距離感，容易把感情往外推，\
易成情愛殺手，人際方面也是在所規範，要與她建立關係需要高度的挑戰，相當的難以贏取寶劍皇后的愛，\
然而遇到挫折，寶劍皇后是具備較多的韌性，能施展以理智應付狀況。"
        url = "http://cisian.pixnet.net/blog/post/181105612"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/ahGMtNv.jpg"])
        
    if res == 57:
        title = "寶劍皇后(逆位)"
        content = "逆位的寶劍皇后，可能胡亂作決定，做事沒有理智可言，對待他人尖酸刻薄，\
想法偏激，沒有談話的空間，無法溝通，胡亂批評，亂罵一通，無法為他人所理解，過度反對情感，\
把自己武裝起來，與世界為敵，高傲的態度；另一方面也有可能遲遲無法下定決定，資訊錯誤矛盾等等狀況產生。"
        url = "http://cisian.pixnet.net/blog/post/181105612"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/adftMYo.jpg"])

#queen_of_pentacles
    if res == 58:
        title = "錢幣皇后(正位)"
        content = "錢幣皇后是沉浸於金錢中的皇后，具有高度的專注程度，將自己的生命投注於澆灌培育，\
不受外界打擾，本身的個性是務實的，實際的，省錢的女性角色，而也不太打扮自己，喜歡二手的衣物，\
出門也以輕便為原則，常常做的就是在各種報紙、網站購物網尋找打折消息或是折價券，\
許多家庭主婦的角色便是顯得如此，錢幣皇后的牌組將錢幣放在子宮之處也代表示多有所產出，\
能構安排各種省錢賺錢的計畫，兔子的動物，除了代表錢幣皇后的專心，不受外界的躁動打擾外，\
亦有代表多產的意思，是一位節儉持家的家庭主婦，穩定的感覺也是一位可以信賴角色，給予人具有相當的安全感。"
        url = "http://cisian.pixnet.net/blog/post/181105744"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/qFQWt7I.jpg"])
        
    if res == 59:
        title = "錢幣皇后(逆位)"
        content = "逆位的錢幣皇后，對於理財的能力消失了，可能拜金花錢，失心瘋，太過注重外表，\
崇尚名牌，受不了外界的誘惑與刺激而花費增加；另外一方面或許太過節儉，而省的有些的小氣；\
而逆位的角色個性也從內向專注的狀態轉而受到外界的干擾，無法集中專注，心有旁騖。"
        url = "http://cisian.pixnet.net/blog/post/181105744"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/ROdhaIi.jpg"])

#knight_of_wands
    if res == 60:
        title = "權杖騎士(正位)"
        content = "權杖騎士是一位身體勇健的騎士，可能有在健身，身上的肌肉與盔甲均展現出他的有力，\
整張牌的顏色，人物的動作與馬兒的姿態，看起來火力全開，具有強大生命力的展現，強大的行動能力衝破一切，\
臉上充滿著自信還有勇敢果決的態度，在正位之時，權杖騎士是有計畫，有強烈的方向感的，面向挑戰毫無怯意，\
充滿無可救藥的熱情，同時也表現出對於成功相當的渴望，目標導向的人物，權杖騎士相當著重目標，\
所以就愛情來講，雖然一開始的熱烈熱情挑戰相當的吸引權杖騎士，但要注意達陣後，\
權杖騎士可能會想要找尋新的方向而離去。"
        url = "http://cisian.pixnet.net/blog/post/181103752"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/dyw6za7.jpg"])
        
    if res == 61:
        title = "權杖騎士(逆位)"
        content = "逆位的權杖騎士，可能熱情之火燃燒的太旺了，變成衝動，方向錯誤或是做過頭卻不知道自己在做什麼，\
忘記評量當前的動作是否與目標一致，可能結果是打水漂，做錯了確毫不知道；另外也有可能火的力量削減，\
行動力減弱，對目標失去興趣，想要轉換跑道尋求更好玩更刺激；技巧不佳尚未準備好去做也有可能只是憑藉著一股熱情，\
但有勇無謀，做事太過魯莽。"
        url = "http://cisian.pixnet.net/blog/post/181103752"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/MrnDLH1.jpg"])

#knight_of_cups
    if res == 62:
        title = "聖杯騎士(正位)"
        content = "聖杯騎士是感情的行動者，本身的速度與腳步是和緩的，更像是在騎馬漫步，\
蜿蜒的河水流動更顯情感上的流動緩緩向前，聖杯騎士所代表的形象是白馬王子，懂得浪漫與調情，華麗的盔甲與精良的裝備，\
顯得注重外貌與外表，這張牌對於女性而言是心中情愛的理想形象，具有令人陶醉於其中的特質；故在實際的面向上，\
可能是心儀的對象出現，一個來自對方的告白，真心地邀請與碰觸，專情一致的對象出現，\
而且對方是具有情感上的創意能力，能夠給予許多的歡樂與樂趣，心臟撲通撲通地跳，感受到愛情的溫熱，\
而在男性方面，出現聖杯騎士也表示的是愛情上的成功機會增大，有機會獲得對方情感上的回應回饋。"
        url = "http://cisian.pixnet.net/blog/post/181103845"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/xVatjV0.jpg"])
        
    if res == 63:
        title = "聖杯騎士(逆位)"
        content = "逆位的聖杯騎士，可能嚮往的對象太多了，情感上的行動太多，變成不專情，\
花心，這個想要那個也要，僅是使用調情技巧，花言巧語，愛的不真誠，想要對方的愛自己卻不願意付出自己的愛，\
將聖杯視為一種收藏品，一種收藏的心態；另一方面逆位的聖杯騎士對於情感的行動錯誤，有可能對於情感產生懦弱，\
退縮遲疑不前，無法下定決心的行動，也有隱含告白失敗的訊息，不是對方喜歡的人，被拒絕。"
        url = "http://cisian.pixnet.net/blog/post/181103845"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/OBREKI7.jpg"])

#knight_of_swords
    if res == 64:
        title = "寶劍騎士(正位)"
        content = "寶劍騎士是宮廷騎士牌中速度最快的一張，從構圖與馬兒的姿勢來看，是飛奔而馳的，\
來無影去無蹤，難以捉模他的蹤跡，是漂丿的男子漢，有自己的目標與方向，從不為他人駐足停留，奔馳是他的本性，\
懷有浪子之心，瀟灑的態度，因其獨特的魅力，總是以酷酷的方式吸引女性或他者的注意；在正位的時候，\
頭腦是清晰且思考快速的，行事匆匆，快速地完成，但是考量上來講沒有顧及太多，可能忽略小小的細節，精緻程度不高，\
是以速度換來的成果，快速的發展演變，表示事情馬上就有答案了。"
        url = "http://cisian.pixnet.net/blog/post/181103929"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/hw3xVaR.jpg"])
        
    if res == 65:
        title = "寶劍騎士(逆位)"
        content = "逆位的保健騎士，飛馳的速度太快，卻未嘗好好的想過，糊走瞎忙，沒有計畫，僅是靠著感覺行事，\
缺乏思考，沒有正確的使用自己的能力，沒有用理智去做事，而飛奔太快的馬兒也表示聽不到他人的話語，對他人視而無見，\
令人感受到一種絕情，拋下他人而去；另一方面寶劍騎士可能在戰場上失敗，逃避前線撤退，也表示逃避眼前的問題，\
不去理睬思索這些。"
        url = "http://cisian.pixnet.net/blog/post/181103929"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/SusrkTB.jpg"])

#knight_of_pentacles
    if res == 66:
        title = "錢幣騎士(正位)"
        content = "錢幣騎士是務實的行動者，背後開闊墾荒的田野，表示正在進行大規模的耕作行為，\
馬匹在四張宮廷騎士牌當中是走的最慢的一張，務實穩定，一步一步走的穩健，努力賺錢提升自己，\
正位時努力的工作，未來是可以期待的，預估的收穫是正向的，馬匹四肢腳皆走於陸地上也代表腳踏實地，\
對於愛情的層面上來講，比較看重未來的投資與規劃，一些家庭務實層面，比較少的談情說愛，或許感到不浪漫，\
然而卻是能夠給予安全感與未來的承諾，附帶一提的是，在感情中出現錢幣宮廷人物牌，\
通常帶給對方的是一種安全穩定的感覺(錢幣侍者除外，錢太少了，錢幣侍者最多給予對方有錢途就是)，\
或許在感情方面聖杯騎士是很好的戀愛對象，然而能夠結婚成家有歸屬感的則偏向是錢幣騎士這樣的角色。"
        url = "http://cisian.pixnet.net/blog/post/181104013"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/bKJepUd.jpg"])
        
    if res == 67:
        title = "錢幣騎士(逆位)"
        content = "逆位的錢幣騎士，有可能太過著重於工作層面了，形成工作狂，以公司為家，無心於他處，\
感情、家庭、生活被視為第二順位，以事業為重，忘了聯繫與身旁他人的情感，一心只想要得到物質的條件，\
把生命奉獻給事業；另外也有可能逆位的錢幣騎士失去勤勉的心，找尋不著方向，失去工作的計畫目標，\
亂投資也有可能，一心想賺大錢卻鋌而走險，想要以小博大，有可能背負巨額欠債欠款，失去金錢而烙跑。"
        url = "http://cisian.pixnet.net/blog/post/181104013"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/r5qtTfj.jpg"])

#page_of_wands
    if res == 68:
        title = "權杖侍者(正位)"
        content = "權杖侍者在權力地位中屬於初階者，通常代表的是階級較為基層的人，比如像是公司剛進來的新人，\
工讀生，傳遞消息的事務員，輔佐的助理，在正位的時候，做好其服務的角色，對於權力較高的人物抱持專注認真，\
虛心請教，並且從中學習工作的事物，而就一個新手來講的話，猶如剛冒芽的生命，未來充滿無限可能的成長性，\
對於前途懷有憧憬與嚮往，有種活潑率真的個性；而權杖侍者角色本身是訊息傳達者，權杖又為生命的象徵，\
所以可能代表著是新的契機，符合人生規畫的好機會的訊息到來。"
        url = "http://cisian.pixnet.net/blog/post/180636532"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/jmMH2SL.jpg"])
        
    if res == 69:
        title = "權杖侍者(逆位)"
        content = "逆位的權杖侍者總是讓人感到不受教的，沒有上進心，對於權力並不懂的敬畏，\
不想被管，自以為是，自認為聰明，而實際上是無知又常常賣弄自己，不知在搞什麼名堂，以自我為中心，\
然而其能力卻不受他人肯定；又或者是假借權力，在他人面前裝作威風，不受控制；又或者是掌握不住學習的技巧，\
東探西湊，每個都嘗試一點，但每件事情與工作卻又做的不好，抑或是三分鐘熱度，做事只是一股腦兒的，\
常常發現新的有趣事物就放棄當前的目標；訊息傳送方面，逆位的權杖侍者角色可能代表不符合人生規劃的工作機會或相關訊息，\
或是過度等待盼望等待機會的到來卻不做努力。"
        url = "http://cisian.pixnet.net/blog/post/180636532"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/WhTWyk9.jpg"])

#page_of_cups
    if res == 70:
        title = "聖杯侍者(正位)"
        content = "聖杯侍者是感情界的新手與初心者，對於感情世界的嚮往，聖杯侍者手拿的杯子正在試驗如何使用它，\
對於感情的事物抱有熱情，能讓人感到有趣好玩，猶如果小學生那種小小的愛情世界觀，\
對於創造感情的手法與做法總是讓人會心一笑，更多的是一種調皮的個性，散播歡樂散撥愛，\
人物的角色是情感的積極回應，關懷與分享，大方天真又無所保留，開放輕鬆；而聖杯侍者通常也代表感情的訊息到來，\
想是情書、傳情小卡或紙條等。"
        url = "http://cisian.pixnet.net/blog/post/180637297"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/UIPQFzC.jpg"])
        
    if res == 71:
        title = "聖杯侍者(逆位)"
        content = "逆位的聖杯侍者可能對於感情有所追求，但用錯方法，想逗逗對方開心卻玩得太過火，\
惡作劇，耍猴戲，引起他人的不滿；而逆位的時候也有可能是感情上不知如何進入他人的情感，\
對於他人的認知感覺無法體驗，無法或不願從對方的角度來感受，不知道要怎麼做，不懂得與他人產生連結；\
聖杯當中沒有水也有可能只是應付對方而已，再搭配侍者的角色，也是感情上的表面敷衍，\
如果積極的話多半也只是一種奉承應付，又或者是喜歡浮華的感情遊戲。"
        url = "http://cisian.pixnet.net/blog/post/180637297"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/HvXrxRw.jpg"])

#page_of_swords
    if res == 72:
        title = "寶劍侍者(正位)"
        content = "寶劍侍者是資訊與訊息的收集者，蒐集資料資訊，打聽消息，而一方面角色的代表也可以像是學校新生，\
學習新的才藝的人物，在正位時，謹慎的判斷與觀察事物，獲得正確的資訊，了解整體狀況，心思銳利且敏捷，\
掌握先機，機警的態度，表達清楚；而寶劍通常也與溝通有關，正位的寶劍侍者代表一些溝通的機會管道，一些訊息的出現。"
        url = "http://cisian.pixnet.net/blog/post/180637747"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/pgadKVA.jpg"])
        
    if res == 73:
        title = "寶劍侍者(逆位)"
        content = "逆位的寶劍侍者，對於訊息是不懂得加以過濾分析的，所以往往來講事情感到繁雜無章，\
帶有錯誤的資訊資料，不了解狀況，訊息不完全，遺漏重要的訊息，或是傳達錯誤，口才不佳。"
        url = "http://cisian.pixnet.net/blog/post/180637747"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/ZEkV4sI.jpg"])

#page_of_pentacles
    if res == 74:
        title = "錢幣侍者(正位)"
        content = "錢幣侍者是剛進投資市場的新手，正在專心地面對眼前投資的機會，學習如何將金錢投入以產生效益收穫，\
是故錢幣是者是對金錢物質充滿嚮往的，理財之道是錢幣侍者學習的主題，身價與財富穩定的成長，謹慎專注小心翼翼，\
並且掌握時機；正位的時候可以說是一些投資的資訊到來，一些門路。"
        url = "http://cisian.pixnet.net/blog/post/180638242"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/lEAjvYX.jpg"])
        
    if res == 75:
        title = "寶劍侍者(逆位)"
        content = "逆位的錢幣侍者，掌握不住投資的方法，能力差，錯誤的投資內容，沒有金錢概念，\
短視近利不懂長遠的規劃，最終失去財富與財產；而另一方面也有可能太想要財富，面對誘惑，想要以小博大，\
卻忽視了風險；逆位的錢幣侍者也有可能代表的是一些錯誤、危險的投資訊息，或是錯過時機的投資訊息。"
        url = "http://cisian.pixnet.net/blog/post/180638242"
        return (["{}\n\n{}\n{}".format(title,content,url),"https://i.imgur.com/B00TALC.jpg"])

if __name__ == '__main__':
    print(tarot_random())
