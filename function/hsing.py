import requestsimport reimport randomimport jsonfrom bs4 import BeautifulSoupdef main():        _hsing = hsing()    print(_hsing.mojim('關老爺'))#    messages = '歡歌1912544'#    hsing17 = hsing()#    #print(hsing17.s17uidrandom(0,1912544))#    #match = re.match('歡歌(\d+)',messages)#    if re.match('(.+)*歡歌(\d+)[:|=](.+)',messages):#        match = re.match('(.+)*歡歌(\d+)[:|=](.+)',messages)#        print (hsing17.s17uidsong(match.group(2),match.group(3)))#    elif re.match('歡歌(\d+)',messages):#        match = re.match('歡歌(\d+)',messages)#        print(hsing17.s17uidrandom(match.group(1)))class hsing(object):    def __init__(self):        self.sid = 0        self.token = 'qNiq7LAhgTpu6iLt1Eff7rhn5VZeZgCQnrpldBdRWVbDaOh9GdYhzaXbBcLRhnSTtqWDDoBdPRoWbvJGVeYS0cCh7etW149rQBRMWbkYdJPhkSgUe6ejPlBvg6J2yeUxKwxp8EwuC1u5VFa9gqTvXyvNkwn1flkGT1jTISAXCHHd21kNiYyB5dphskDuxou_&uid=3551228&action=notice.checkNotice&time=1527303600'    def getjson(self,sid,uid):                api_url = 'http://act.17sing.tw/index.php?songId={}&qty=50&token={}&uid={}&stick=0&action=GetMySong&type=0'.format(sid,self.token,uid)        request = requests.get(api_url)        rcontent = request.content.decode('utf8')        song_json = json.loads(rcontent)                return song_json                  def s17uidrandom(self,uid):            song_url = 'http://17sing.tw/share_song/index.html?sid={}&selfUid={}'        sid = self.sid        get_song_count = 0;        song_count = 0;        new_dict = []                    while (sid==0 or get_song_count==50):                    song_json = self.getjson(sid,uid)            #print (song_json)            song_list = song_json['response_data']            get_song_count = len(song_list)            song_count += get_song_count            if int(song_count/50) == 0:                return "UUID沒有歌曲or輸入格式錯誤"                       elif get_song_count == 50:                sid = song_list[49]['id'];                                       new_dict = new_dict+song_list            random.shuffle(new_dict)                for obj in new_dict:                if (obj['privacy']=="0"):                    song_id = obj['id']                    surl = song_url.format(song_id,uid)                    song_titl = obj['name']                    song_data = '歌名:{}\n{}\n'.format(song_titl,surl)                if get_song_count <50:                return song_data            return song_data    def s17uidsong(self,uid,song):            song_url = 'http://17sing.tw/share_song/index.html?sid={}'            #match = re.match('(.+)*歡歌(\d+)[:|=](.+)',res)        #uid = match.group(2)        #if (is_number(uid) == False):        #    return "UID後面不得有中文字, 正確輸入:歡歌UID 或 歡歌UID:歌名"            #song = match.group(3)            sid = self.sid;        get_song_count = 0;        song_count = 0;        list_content=""        check_get_song = 0;                while (sid==0 or get_song_count==50):            song_json = self.getjson(sid,uid)            song_list = song_json['response_data']            get_song_count = len(song_list)            song_count += get_song_count                for obj in song_list:                if (obj['privacy']=="0" and obj['name'].find(song) !=-1 ):                    song_id = obj['id']                                     surl = song_url.format(song_id,uid)                    song_titl = obj['name']                    song_data = '歌名:{}\n{}\n'.format(song_titl,surl)                    list_content += song_data                    check_get_song +=1                    if (check_get_song > 7):                        list_content ="關鍵字查找超過8首, 請縮小範圍\n\n{}".format(list_content)                         return list_content                if get_song_count < 50:                if (len(list_content)>0):                    return list_content                else:                    return "查不到歌曲"                           else:                sid = song_list[49]['id'];                     def sing17(self):            for i in range(20):            songid  = "%08d" % random.randint(0,1e8)            url = 'http://17sing.tw/share_song/index.html?sid={}'.format(songid)            request = requests.get(url)            ycontent = request.content            soup = BeautifulSoup(ycontent, 'html.parser')            songimage = soup.find("meta",{"property":"og:image"})            img  = songimage.attrs["content"]            songurl = soup.find("meta",{"property":"og:url"})            surl = songurl.attrs["content"]            songtitl = soup.find("meta",{"property":"og:description"})            titl = songtitl.attrs["content"][0:50]                content = '{}\n{}...'.format(surl,titl)                        if len(img) > 0 :                return content            else:                pass        return "找不到歌 請再試一次!!"    def tomp3(self,res):            source_url = res[res.find("http"):]            key = source_url.find("oksing.tw")            if (key>0):            sid = source_url.find("?sid")            uid = source_url.find("&self")            if (uid>0):                sid_key = source_url[sid+5:uid]            else:                sid_key = source_url[sid+5:]                        json_url = 'http://act.oksing.tw/index.php?action=GetSongInfo&sid={}&callback=_jsoncallback'.format(sid_key)        else:            sid = source_url.find("?sid")            uid = source_url.find("&self")            if (uid>0):                sid_key = source_url[sid+5:uid]            else:                sid_key = source_url[sid+5:]            json_url = 'http://act.17sing.tw/index.php?action=GetSongInfo&sid={}&callback=_jsoncallback'.format(sid_key)            request = requests.get(json_url)            soup = request.text        mp3_source = soup.replace("_jsoncallback","").replace("(",")").replace(")","")        mp3_json = json.loads(mp3_source)        mp3_get = mp3_json['response_data']['song']['path']        #checkMV= mp3_source.find("mv_cover")        if (mp3_source.find("mv_cover")>0):            mp3_url = mp3_get.replace("mp3","mp4")        else:            mp3_url = mp3_get            return mp3_url        #唱吧轉mp3    def changbamp3(self,res):                source_url = res[res.find("http"):]            request = requests.get(source_url)        soup = BeautifulSoup(request.content, "html.parser")        script = soup.find_all('script')        #pattern = re.compile(r'mp3');', re.MULTILINE | re.DOTALL)        #mp3urlsearch = script[3].text                for obj in script:            if obj.text.find("mp3")>-1:                mp3script = obj.text    ##            print(mp3script)     ##            print(mp3script.find("http://qiniuuwmp3.changba.com"))    ##            print(mp3script.find(".mp3"))                if mp3script.find("http://qiniuuwmp3.changba.com") >-1:                    return mp3script[mp3script.find("http://qiniuuwmp3.changba.com"):mp3script.find(".mp3")+4]                elif mp3script.find("http://lzscuw.changba.com") >-1:                    return mp3script[mp3script.find("http://lzscuw.changba.com"):mp3script.find(".mp3")+4]            def songsearch17(self,res):            source_url = "http://ec2.kusoinlol.com/hsing/SongList.php"        request = requests.post(source_url,res.encode("utf-8"))        r = request.text        table_content = r[r.find("table")-1:]            tds=[]        content = ""        soup = BeautifulSoup(table_content,'html.parser')        divs = soup.findAll("table")        for div in divs:            rows = div.findAll('tr')            for row in rows:                tds.append(row.findAll('td'))                #if(row.text.find("試聽")>-1):                #    content +=row.text            list_content = ""        content = ""                for i in range(len(tds)):            if i+1 < len(tds) and i<5 :                who = tds[i+1][1].text                song = tds[i+1][2].text                link = tds[i+1][0].a['href']                data = '{},{}\n{}\n'.format(who,song,link)                list_content += data            else:                pass            if (len(list_content)==0):            content = '{}\n\n詳閱伴唱聯盟搜索引擎\n{}'.format("查不到伴奏","http://goo.gl/XXglcl")        else:            content = '{}\n詳閱伴唱聯盟搜索引擎\n{}'.format(list_content,"http://goo.gl/XXglcl")                         return content        def mojim(self,res):            _url = "https://mojim.com"        url = "{}/{}.html?t4".format(_url,res)        request = requests.get(url)        ytcontent = request.content        soup = BeautifulSoup(ytcontent, "html.parser")            _check = soup.select("title")        check = _check[0].text.find("請重新輸入")                    if (int(check) < 0):            s_list = soup.select("span[class='mxsh_ss3']")            for data in s_list[1]:                curl = "{}{}".format(_url,data.get("href"))                sing_content = data.text[0:100]                                    trequest = requests.get(curl)            tytcontent = trequest.content            tsoup = BeautifulSoup(tytcontent, "html.parser")                        t_list = tsoup.select("title")            tcontent = t_list[0].text            p = tcontent.find("歌詞")            p2 = tcontent.find("※")                title = tcontent[0:int(p)]            singer = tcontent[int(p)+3:int(p2)]            content = "資料來源-魔鏡歌詞網\n------\n{}-{}\n\n{}...\n\n{}\n".format(singer,title,sing_content,curl)        else:            content = "沒有符合的歌詞請重新輸入，可利紅豆 王菲或紅豆+王菲的方式來查找"            return content        if __name__ == '__main__':    main()