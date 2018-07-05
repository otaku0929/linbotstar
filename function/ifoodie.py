# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 13:51:39 2018

@author: 宇星
"""

import re
import json
import requests
import random

def ifoodie(city,res):
    
    s_url = 'https://ifoodie.tw/api/blog/'
    payload = {
           'order_by':'-date',
            'city_name':city,
            'q': res,
            }
    _json = requests.get(s_url, params=payload)
    json_content = json.loads(_json.content)
     
    food_list = json_content['response']
    random.shuffle(food_list)
    
    return food_list[0:5][0]['restaurant']['name']
    #id blog-id
    #description
    #thumb
    #['restaurant']['name']
    
    

if __name__ == '__main__':
    messages = '查美食=南京復興餐廳'
    pattern = re.compile(r'查美食=(\D.)[市縣]*(.+)')
    match = pattern.match(messages)
    if match:
        city = match.group(1).replace('新北','台北') 
        #print(city)
        res = match.group(2)
        #print(res)
        #print (res)
        print(ifoodie(city,res))
        #(wt(res))    