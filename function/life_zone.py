# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 17:47:46 2018

@author: 宇星
"""

import requests
import re
import json
from bs4 import BeautifulSoup
import datetime, pytz
import random

from linebot.models import (
        MessageEvent, 
        TextMessage, 
        TextSendMessage, 
        ImageSendMessage, 
        TemplateSendMessage,
        CarouselTemplate,
        CarouselColumn
        )

from linebot.models.actions import (  # noqa
    Action,
    PostbackAction,
    MessageAction,
    URIAction,
    DatetimePickerAction,
    Action as TemplateAction,  # backward compatibility
    PostbackAction as PostbackTemplateAction,  # backward compatibility
    MessageAction as MessageTemplateAction,  # backward compatibility
    URIAction as URITemplateAction,  # backward compatibility
    DatetimePickerAction as DatetimePickerTemplateAction,  # backward compatibility
)

import function.g_function
_g_function = function.g_function.function()


def main():

    _life=life_zone()
    message='日劇'
    content = _life.hot_tvshow(message)
    print(content)
    #return(_life.gamer(messages))
    
class life_zone(object):
    
    def hot_tvshow(self,res):
        if res == '日劇':
            url = 'http://jp03.jplovetv.com/'
        if res == '韓劇':
            url = 'http://kr14.vslovetv.com/'
        if res == '陸劇':
            url = 'http://cn.lovetvshow.info/'            
            
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser") 
        soup_div = soup.select('tr td')
        soup_td = soup_div[1].select('td')
        
        pull_list = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
        random.shuffle(pull_list)
        get_list = pull_list[0:5]
        
        #print(soup_td[get_list[0]].select('a')[0].text)
        #print(soup_td[get_list[0]].select('a')[0]['href'])
        
#        show_list = ''
#        for obj in get_list:
#            show = soup_td[obj].text
#            show_detail = self.google_search_detail(show)
#            show_content = '>> %s\n簡介:%s'%(show,show_detail)
#            show_list = '%s\n\n%s\n--------'%(show_list,show_content)
#            #print(soup_td[obj].text)
#        content = '%s\n\n*因版權問題 小星星僅提供追劇參考不提供追劇連結\n*部份簡介因維基百科查不到就沒有\n*本列表隨機5部追劇參考'%show_list
#        return content

        carousel_template_message = TemplateSendMessage(
            alt_text='追劇參考',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/j5pDXdG',
                        title=soup_td[get_list[0]].select('a')[0].text,
                        text=self.google_search_detail(soup_td[get_list[0]].select('a')[0].text)[0:51]+'...',
                        actions=[
                            URITemplateAction(
                                label='追劇連結',
                                uri= soup_td[get_list[0]].select('a')[0]['href']
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/j5pDXdG',
                        title=soup_td[get_list[1]].select('a')[0].text,
                        text=self.google_search_detail(soup_td[get_list[1]].select('a')[0].text)[0:51]+'...',
                        actions=[
                            URITemplateAction(
                                label='追劇連結',
                                uri= soup_td[get_list[1]].select('a')[0]['href']
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/j5pDXdG',
                        title=soup_td[get_list[2]].select('a')[0].text,
                        text=self.google_search_detail(soup_td[get_list[2]].select('a')[0].text)[0:51]+'...',
                        actions=[
                            URITemplateAction(
                                label='追劇連結',
                                uri= soup_td[get_list[2]].select('a')[0]['href']
                            )
                        ]
                    ),
                      CarouselColumn(
                        thumbnail_image_url='https://imgur.com/j5pDXdG',
                        title=soup_td[get_list[3]].select('a')[0].text,
                        text=self.google_search_detail(soup_td[get_list[3]].select('a')[0].text)[0:51]+'...',
                        actions=[
                            URITemplateAction(
                                label='追劇連結',
                                uri= soup_td[get_list[3]].select('a')[0]['href']
                            )
                        ]
                    ),
                       CarouselColumn(
                        thumbnail_image_url='https://imgur.com/j5pDXdG',
                        title=soup_td[get_list[4]].select('a')[0].text,
                        text=self.google_search_detail(soup_td[get_list[4]].select('a')[0].text)[0:51]+'...',
                        actions=[
                            URITemplateAction(
                                label='追劇連結',
                                uri= soup_td[get_list[4]].select('a')[0]['href']
                            )
                        ]
                    )
                ]
            )
        )
        
        return carousel_template_message
    
    def google_search_detail(self,res):
        url = 'https://www.google.com.tw/search?q=%s&aqs=chrome..69i57j0.1154j0j7&sourceid=chrome&ie=UTF-8'%res
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser") 
        soup_div = soup.select("div[class='FSP1Dd']")
        
        if soup_div == []:
            content = ''
        else:
            try:
                soup_div2 = soup.select("div[class='mraOPb']")
                _content = soup_div2[0].text
                content = _content[0:(len(_content)-4)]
            except:
                content = ''
        
        return content
    
    def __init__(self):
        self.class_name = 'life_zone'
        
    def starweek(self,res):
        
        time = str(datetime.datetime.now(pytz.timezone('Asia/Taipei')))[0:10]
        year = int(time[0:4])
        month = int(time[5:7])
        date = int(time[8:10])

        today_res = _g_function.weekDay(year, month, date)

        
        weekdate_s = str(datetime.datetime.now(pytz.timezone('Asia/Taipei'))-datetime.timedelta(days=int(today_res[0])))[0:10]
        weekdate_e = str(datetime.datetime.now(pytz.timezone('Asia/Taipei'))+datetime.timedelta(days=(6-int(today_res[0]))))[0:10]             
        
        #print(weekdate_s,weekdate_e)

        starnumber = self.starnumber(res)
        
        url = 'http://astro.click108.com.tw/weekly_10.php?iAcDay=%s&iType=1&iAstro=%s'%(time,starnumber)
        
        request = requests.get(url)
        soup = BeautifulSoup(request.content, "html.parser")
        soup_class = soup.select("div[class='TODAY_CONTENT']")
        
        soup_p = soup_class[0].findAll('p')
        
        x_content = ''
        for x in soup_p:
            x_content = '%s\n\n%s'%(x_content,x.text)
        
        content = '本周< %s >星座運勢解析\n%s ~ %s%s'%(res,weekdate_s,weekdate_e,x_content)
        
        
#        f=open('output.txt','w', encoding='UTF-8')
#        f.write(format(soup))
#        f.close()

        return content



    
    def starnumber(self,res):
        
        if res == '牡羊座':
            return 0
        if res == '金牛座':
            return 1
        if res == '雙子座':
            return 2
        if res == '巨蟹座':
            return 3
        if res == '獅子座':
            return 4
        if res == '處女座':
            return 5
        if res == '天秤座':
            return 6
        if res == '天蠍座':
            return 7
        if res == '射手座':
            return 8
        if res == '摩羯座':
            return 9
        if res == '水瓶座':
            return 10
        if res == '雙魚座':
            return 11
    
    #巴哈姆特    
    def gamer(self,res):
    
        s_url = 'https://www.googleapis.com/customsearch/v1element'
        payload = {
               'key':'AIzaSyCVAXiUzRYsML1Pv6RwSG1gunmMikTzQqY',
                'cx':'partner-pub-9012069346306566:kd3hd85io9c',
                'q': res,
                'cse_tok': 'AF14hljhr7Db4l8Sce_AXfC9IO6BAlnjaA:1530609483589'
                }
        _json = requests.get(s_url, params=payload)
        json_content = json.loads(_json.content)
        
        #print(json_content)
        game_list = json_content['results']
    
        content = ""
        i = 0
        for obj in game_list:
            _obj = str(obj['richSnippet']['metatags'])
            if re.search('ogUrl',_obj):
                url = obj['richSnippet']['metatags']['ogUrl']
                content = content + url +'\n\n'
                i = i+1;
                if i == 5:
                    return content
                
    #mygopen
    def mygopen(self,res):
        
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
    

if __name__ == '__main__':
    main()