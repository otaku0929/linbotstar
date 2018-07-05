# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 13:51:39 2018

@author: 宇星
"""

import re
import json
import requests
import random
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

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
    #id
    #description
    #thumb
    #['restaurant']['name']
    

def ifoodie_line(reply_token, city,res):

        ifoodie_content = ifoodie(city,res)
        carousel_template_message = TemplateSendMessage(
            alt_text='美食特搜結果',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=ifoodie_content[0]['thumb'],
                        title=ifoodie_content[0]['restaurant']['name'],
                        text=ifoodie_content[0]['description'],
                        actions=[
                            URITemplateAction(
                                label='詳細內容',
                                uri= 'https://ifoodie.tw/blog/'+ifoodie_content[0]['id']
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=ifoodie_content[1]['thumb'],
                        title=ifoodie_content[1]['restaurant']['name'],
                        text=ifoodie_content[1]['description'],
                        actions=[
                            URITemplateAction(
                                label='詳細內容',
                                uri= 'https://ifoodie.tw/blog/'+ifoodie_content[1]['id']
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=ifoodie_content[2]['thumb'],
                        title=ifoodie_content[2]['restaurant']['name'],
                        text=ifoodie_content[2]['description'],
                        actions=[
                            URITemplateAction(
                                label='詳細內容',
                                uri= 'https://ifoodie.tw/blog/'+ifoodie_content[2]['id']
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=ifoodie_content[3]['thumb'],
                        title=ifoodie_content[3]['restaurant']['name'],
                        text=ifoodie_content[3]['description'],
                        actions=[
                            URITemplateAction(
                                label='詳細內容',
                                uri= 'https://ifoodie.tw/blog/'+ifoodie_content[3]['id']
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url=ifoodie_content[4]['thumb'],
                        title=ifoodie_content[4]['restaurant']['name'],
                        text=ifoodie_content[4]['description'],
                        actions=[
                            URITemplateAction(
                                label='詳細內容',
                                uri= 'https://ifoodie.tw/blog/'+ifoodie_content[4]['id']
                            )
                        ]
                    )
                ]
            )
        )
        line_bot_api.reply_message(reply_token,carousel_template_message)
        #gs_write('B27')
        return 0

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
