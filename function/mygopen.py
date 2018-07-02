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
    soup_content0 = soup.select("article[class='post hentry']")
    soup_content = soup.select("div[class='img-thumbnail']")
    return_obj = ""
    i = 0
    
    if len(soup_content) == 0:
        return "查無相關資料,請更新關鍵字或至https://www.mygopen.com登錄流言"    
    else:
        for obj in soup_content0:
          content = obj.select("a")[1].get('href')
          return_obj = '{}\n{}'.format(return_obj,content)
          i += 1;
          if i == 5:
              return '{}\n{}\n\n{}'.format("MyGoPen Say:",return_obj,'*超過5筆，僅列出前5筆*\n請共同抵制假消息')            
    
        return '{}\n{}\n\n{}'.format("MyGoPen Say:",return_obj,'請共同抵制假消息')
    
def wt(res):

    content = mygopen(res)
    f=open('mygopen.txt','w', encoding='UTF-8')
    f.write(format(content))
    f.close()
    print ('--print ok--')   

if __name__ == '__main__':
    messages = '查證LINE隱私'
    #print(messages[0:2])
    res = re.search("查證(.+)",messages).group(1)
    print(mygopen(res))
