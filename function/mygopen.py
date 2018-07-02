# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 21:14:28 2018

@author: 宇星
"""

import requests
import re
from bs4 import BeautifulSoup


def mygopen(res):
    
    ourl ='https://www.mygopen.com/search?q='
    #url = '{}{}'.format(ourl,res.encode('utf-8'))
    url = '{}{}'.format(ourl,res)
    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")
    soup_content = soup.select("article[class='post hentry'] a")
    if len(soup_content) == 0:
        return "查無相關資料,請更新關鍵字或至https://www.mygopen.com登錄流言"    
    else:
        return '{}\n{}\n\n{}'.format("這是假消息:",soup_content[1].get('href'),'請共同抵制假消息')
    
def wt(res):

    content = mygopen(res)
    f=open('mygopen.txt','w', encoding='UTF-8')
    f.write(format(content))
    f.close()
    print ('--print ok--')   

if __name__ == '__main__':
    res = '這種雞蛋不要買'
    print(mygopen(res))