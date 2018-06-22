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

    uid = res[2:]
    if (is_number(uid) == False):
        return "UID後面不得有中文字, 正確輸入:歡歌UID"
    print (uid)
    sid = 0;
    get_song_count = 0;
    song_count = 0;
    list_content=""
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

    uid = res
    if (is_number(uid) == False):
        return "UID後面不得有中文字, 正確輸入:歡歌UID"
    #print (uid)
    sid = 0;
    get_song_count = 0;
    song_count = 0;
    list_content=""
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

    uid = res[2:res.find(':')]
    if (is_number(uid) == False):
        return "UID後面不得有中文字, 正確輸入:歡歌UID 或 歡歌UID:歌名"

    song = res[res.find(':')+1:].strip()

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
    token='xp9tH2ESXEjYdYDQalrPy8UaUrR4Lbe1PjYhiZqdg1jSfsdq_Iz_Rh0BinheXCPrdvEn_nEEQi_gH_G5PVq4S75KphKBh9bxpxK8tKve_C5l-C2SmZQRXmYoaDrNd7hzm_U884m8oTMAoFCBNwigQRbHhscm51mhbxeqnyr9kuTEcZ1XgVEd5rxz5Pxnfr0T'
    api_url = 'http://act.17sing.tw/index.php?songId={}&qty=50&token={}&uid={}&stick=0&action=GetMySong&type=0'.format(sid,token,res)

    request = requests.get(api_url)
    rcontent = request.content.decode('utf8')
    song_json = json.loads(rcontent)

    return song_json   