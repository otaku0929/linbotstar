import requests
import re
import random
import json
from bs4 import BeautifulSoup


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
    

def s17uidrandom(res):

    song_url = 'http://17sing.tw/share_song/index.html?sid={}&selfUid={}'

    uid = re.match('歡歌(\d+)',res).group(1)
    if (is_number(uid) == False):
        return "UID後面不得有中文字, 正確輸入:歡歌UID"
    print (uid)
    sid = 0;
    get_song_count = 0;
    song_count = 0;
    new_dict = []

    while (sid==0 or get_song_count==50):        
        song_json = getsongjson(sid,uid)
        #print (song_json)
        song_list = song_json['response_data']
        get_song_count = len(song_list)
        song_count += get_song_count
        if int(song_count/50) == 0:
            return "UUID沒有歌曲or輸入格式錯誤"           
        elif get_song_count == 50:
            sid = song_list[49]['id'];
                       
        new_dict = new_dict+song_list
        random.shuffle(new_dict)

        for obj in new_dict:
            if (obj['privacy']=="0"):
                song_id = obj['id']
                surl = song_url.format(song_id,uid)
                song_titl = obj['name']
                song_data = '歌名:{}\n{}\n'.format(song_titl,surl)

        if get_song_count <50:
            return song_data

    return song_data


def s17uidrandom_star(res):

    song_url = 'http://17sing.tw/share_song/index.html?sid={}&selfUid={}'

    uid = re.match('歡歌(\d+)',res).group(1)
    if (is_number(uid) == False):
        return "UID後面不得有中文字, 正確輸入:歡歌UID"
    #print (uid)
    sid = 0;
    get_song_count = 0;
    song_count = 0;
    new_dict = []

    while (sid==0 or get_song_count==50):        
        song_json = getsongjson(sid,uid)
        #print (song_json)
        song_list = song_json['response_data']
        get_song_count = len(song_list)
        song_count += get_song_count
        if int(song_count/50) == 0:
            return "UUID沒有歌曲or輸入格式錯誤"           
        elif get_song_count == 50:
            sid = song_list[49]['id'];
                       
        new_dict = new_dict+song_list
        random.shuffle(new_dict)

        for obj in new_dict:
            if (obj['privacy']=="0"):
                song_id = obj['id']
                surl = song_url.format(song_id,uid)
                song_titl = obj['name']
                song_data = '歌名:{}\n{}\n'.format(song_titl,surl)

        if get_song_count <50:
            return song_data

    return song_data

def s17uidsong(res):

    song_url = 'http://17sing.tw/share_song/index.html?sid={}'

    match = re.match('(.+)*歡歌(\d+)[:|=](.+)',res)
    uid = match.group(2)
    if (is_number(uid) == False):
        return "UID後面不得有中文字, 正確輸入:歡歌UID 或 歡歌UID:歌名"

    song = match.group(3)

    sid = 0;
    get_song_count = 0;
    song_count = 0;
    list_content=""
    check_get_song = 0;
    
    while (sid==0 or get_song_count==50):        
        song_json = getsongjson(sid,uid)
        song_list = song_json['response_data']
        get_song_count = len(song_list)
        song_count += get_song_count

        for obj in song_list:
            if (obj['privacy']=="0" and obj['name'].find(song) !=-1 ):
                song_id = obj['id']                 
                surl = song_url.format(song_id,uid)
                song_titl = obj['name']
                song_data = '歌名:{}\n{}\n'.format(song_titl,surl)
                list_content += song_data
                check_get_song +=1
                if (check_get_song > 7):
                    list_content ="關鍵字查找超過8首, 請縮小範圍\n\n{}".format(list_content) 
                    return list_content

        if get_song_count < 50:
            if (len(list_content)>0):
                return list_content
            else:
                return "查不到歌曲"               
        else:
            sid = song_list[49]['id']; 
        
 
#
def getuidimg(uid):

    song_json = getsongjson(0,uid)
    song_list = song_json['response_data']

    _song_url = 'http://17sing.tw/share_song/index.html?sid={}'
    song_url = _song_url.format(song_list[0]['id'],uid)

    request = requests.get(song_url)
    soup = BeautifulSoup(request.content,"html.parser")

    url = soup.find("meta",property="og:image")   

    return url["content"]

     

def getsongjson(sid,res):

    #type=0 全部 1 合唱 2 底版 3 MV
    #qyt最多50筆
    #token = 'CXDYeA-EQZvjkHav_Z3hAgQlO9hKVVhFJpWqT2-yOUiXznYtAObKlmHfcRru8huomWqdupzIGi_My77-oU-Wj2kvQtaZmEbhab-Vihd9vjChJzuAwpb3Y4Tf9CR1W2Qho_YkL2FbtPuRDvOfVBwsQp6RdF9Vo6HZBNXKOGuAmp5f-1x-tHge-swl9SVh8Fhh'
    token='9rGhKd1Fsohwgr-XBTamFXqt839O3l9zXom8wbKg_s8kRCz8_CHk7ZE1kI9Rqa8qmGc4OpjA61fyZTPp9YRr_jdVt3P8HTf90jlzb3kt5UWKlmeLr4gr8hjCTQgkOb6OEMCh3C1NVlFsAyfKxGeHqJlj76iTdgJOLAThbOJnZvn38wMUC0hNOcmWIPk35YYo'
    api_url = 'http://act.17sing.tw/index.php?songId={}&qty=50&token={}&uid={}&stick=0&action=GetMySong&type=0'.format(sid,token,res)
    #print(api_url)
    request = requests.get(api_url)
    rcontent = request.content.decode('utf8')
    song_json = json.loads(rcontent)

    return song_json   




if __name__ == '__main__':
    res = '我想查歡歌1912544=我要吃肉肉'
    #match = re.match('歡歌(\d+)',res)
    match = re.match('(.+)*歡歌(\d+)[:|=](.+)',res)
    #print(match.group(0))
    if re.match('(.+)*歡歌(\d+)[:|=](.+)',res):
        print (s17uidsong(res))
