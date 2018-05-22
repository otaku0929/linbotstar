import time
import requests
import random
import re
import urllib.request
import pandas
from bs4 import BeautifulSoup
from imgurpython import ImgurClient
from datetime import datetime, timedelta


def shelp():

    helplist=['..!help',
              '..小星星粉絲頁',
              '..抽',
              '..抽正妹',
              '..抽鮮肉',
              '..查天氣縣市 ex查天氣台北市',
              '..查空氣品質',
              '..天氣特報',
              '..查颱風',
              '..抽籤',
              '..星座名　ex天秤座',
              '..抽金句',
              '..time',
              '..time20180101',
              '..time2017010113',
              '..現在吃什麼',
              '..查樂透',
              '..查股市',
              '..查股票股號 ex查股號鴻海',
              '..查匯率',
              '..查歌詞+關鍵字',
              '..抽歡歌',
              '..轉換歡歌或愛K歌mp3',
              '..18啦',
              '..拉霸',
              '..比大小',
              '..聽歌+關鍵字',
              '..youtube熱門',
              '..youtube華語',
              '..聽歌華語',
              '..聽歌台語',
              '..蘋果新聞',
              '..看電影',
              '..看電影+電影名',
              '..本週上映',
              '..查集點',
              '..查咖啡',
              '..PTTHOT',
              '..PTT笨版',
              '..PTT表特',
              '..即時廢文',
              '..翻譯+英文',
              '..傳送LINE座標',
              '..詳細說明詳見小星星粉絲頁',
              'https://www.facebook.com/%E5%B0%8F%E6%98%9F%E6%98%9F-138369020128285/'
              
              
]
    content = ""
    for i in helplist:
        a = '{}\n'.format(i)
        content += a
       
    return content
    

def p():

    content = shelp()
    print (content)


              
def wt():
    
    content = lotto_super()
    f=open('output.txt','w', encoding='UTF-8')
    f.write(format(content))
    f.close()
    print ('--print ok--')

if __name__ == '__main__':
    print(p())
    #print(p1())
    #print(wt())



