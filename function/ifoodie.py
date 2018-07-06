# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 13:51:39 2018

@author: 宇星
"""

import re
import json
import requests
import random

from linebot.models import *
#from linebot.models.template import TemplateSendMessage
#from linebot.models.template import CarouselTemplate
#from linebot.models.template import CarouselColumn
#from linebot.models.actions import (  # noqa
#    Action,
#    PostbackAction,
#    MessageAction,
#    URIAction,
#    DatetimePickerAction,
#    Action as TemplateAction,  # backward compatibility
#    PostbackAction as PostbackTemplateAction,  # backward compatibility
#    MessageAction as MessageTemplateAction,  # backward compatibility
#    URIAction as URITemplateAction,  # backward compatibility
#    DatetimePickerAction as DatetimePickerTemplateAction,  # backward compatibility
#)

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
    
    max_i = 0
    new_list = []
    for obj in food_list:
        if obj['restaurant']:
            new_list.append(obj)
        if not obj['restaurant']:
            #"obj['user']['display_name']"
            obj['restaurant'] = {'name':obj['user']['display_name']}
            new_list.append(obj)
        max_i = max_i+1
        if max_i == 5:
            return new_list

    return new_list
    #id
    #description
    #thumb
    #['restaurant']['name']
    

def ifoodie_line(city,res):
        if res == None:
            res = "美食"
        ifoodie_content = ifoodie(city,res)
        if len(ifoodie_content)==0:
            return "查詢位置暫無資料,或請確認關鍵字內容"
        if len(ifoodie_content)==1:
            carousel_template_message = TemplateSendMessage(
                alt_text='美食特搜結果',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=ifoodie_content[0]['thumb'],
                            title=ifoodie_content[0]['restaurant']['name'],
                            text=ifoodie_content[0]['description'][0:51]+'...',
                            actions=[
                                URITemplateAction(
                                    label='詳細內容',
                                    uri= 'https://ifoodie.tw/blog/'+ifoodie_content[0]['id']
                                )
                            ]
                        )
                    ]
                )
            )
            return carousel_template_message
        if len(ifoodie_content)==2:
            carousel_template_message = TemplateSendMessage(
                alt_text='美食特搜結果',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=ifoodie_content[0]['thumb'],
                            title=ifoodie_content[0]['restaurant']['name'],
                            text=ifoodie_content[0]['description'][0:51]+'...',
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
                            text=ifoodie_content[1]['description'][0:51]+'...',
                            actions=[
                                URITemplateAction(
                                    label='詳細內容',
                                    uri= 'https://ifoodie.tw/blog/'+ifoodie_content[1]['id']
                                )
                            ]
                        )
                    ]
                )
            )
            return carousel_template_message
        if len(ifoodie_content)==3:
            carousel_template_message = TemplateSendMessage(
                alt_text='美食特搜結果',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=ifoodie_content[0]['thumb'],
                            title=ifoodie_content[0]['restaurant']['name'],
                            text=ifoodie_content[0]['description'][0:51]+'...',
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
                            text=ifoodie_content[1]['description'][0:51]+'...',
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
                            text=ifoodie_content[2]['description'][0:51]+'...',
                            actions=[
                                URITemplateAction(
                                    label='詳細內容',
                                    uri= 'https://ifoodie.tw/blog/'+ifoodie_content[2]['id']
                                )
                            ]
                        )
                    ]
                )
            )
            return carousel_template_message
        if len(ifoodie_content)==4:
            carousel_template_message = TemplateSendMessage(
                alt_text='美食特搜結果',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=ifoodie_content[0]['thumb'],
                            title=ifoodie_content[0]['restaurant']['name'],
                            text=ifoodie_content[0]['description'][0:51]+'...',
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
                            text=ifoodie_content[1]['description'][0:51]+'...',
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
                            text=ifoodie_content[2]['description'][0:51]+'...',
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
                            text=ifoodie_content[3]['description'][0:51]+'...',
                            actions=[
                                URITemplateAction(
                                    label='詳細內容',
                                    uri= 'https://ifoodie.tw/blog/'+ifoodie_content[3]['id']
                                )
                            ]
                        )
                    ]
                )
            )
            return carousel_template_message
        if len(ifoodie_content)==5:
            carousel_template_message = TemplateSendMessage(
                alt_text='美食特搜結果',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=ifoodie_content[0]['thumb'],
                            title=ifoodie_content[0]['restaurant']['name'],
                            text=ifoodie_content[0]['description'][0:51]+'...',
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
                            text=ifoodie_content[1]['description'][0:51]+'...',
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
                            text=ifoodie_content[2]['description'][0:51]+'...',
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
                            text=ifoodie_content[3]['description'][0:51]+'...',
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
                            text=ifoodie_content[4]['description'][0:51]+'...',
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
            return carousel_template_message
        #line_bot_api.reply_message(reply_token,carousel_template_message)
        #gs_write('B27')
        #return 0

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
        print(ifoodie_line(city,res))
        #(wt(res))    
