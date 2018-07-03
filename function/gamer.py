# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 16:34:14 2018

@author: 宇星
"""

import requests
import re
import json

def gamer(res):
    
    s_url = 'https://www.googleapis.com/customsearch/v1element'
    payload = {
           'key':'AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY',
            'cx':'partner-pub-9012069346306566:kd3hd85io9c',
            'q': res,
            'cse_tok': 'AF14hljhr7Db4l8Sce_AXfC9IO6BAlnjaA:1530609483589'
            }
    _json = requests.get(s_url, params=payload)
    json_content = json.loads(_json.content)
    
    game_list = json_content['results'][0:5]
    #game_list[0]['richSnippet']
    content = ""
    for obj in game_list:
        url = obj['richSnippet']['metatags']['ogUrl']
        content = content + url +'\n'
    
    return content

def wt(res):

    content = gamer(res)
    f=open('gamer.txt','w', encoding='UTF-8')
    f.write(format(content))
    f.close()
    print ('--print ok--')   

if __name__ == '__main__':
    messages = '巴哈天堂M黑妖練法'
    #print(messages[0:2])
    res = re.search("巴哈(.+)",messages).group(1)
    print(gamer(res))
    print(wt(res))