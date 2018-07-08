# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 23:09:59 2018

@author: 宇星
"""
import math
import requests
import json
import re
from .get_wp_state import get_state

import function.g_function
_function = function.g_function.function()

def main():
    wp = WeatherParser()
    #print(wp.getReportWithAPI('龜山'))
    messages = '查天氣=中壢高中'
    match = re.match('(.+)*天氣=(.+)',messages)
    loc = match.group(2)
    #print(loc)
    #locA =  gfunction.getGeoForAddress(loc)
    #wp_state = get_state(locA,'wp')
    #print(wp_name['state_name'])
    #print(wp_location)
    #print(wp_state)
    #wp_content = (wp.getReportWithAPI(wp_state['state_name']))
    wp_content = wp.getReportWithAPI(loc)
    content = '地點：{}\n{}'.format(loc,wp_content)
    print(content)

class WeatherParser(object):
    
    def __init__(self):
        self.doc_name_C0 = "O-A0001-001"#"F-C0032-001"
        self.doc_name_46 = "O-A0003-001"
        self.user_key = "CWB-A01FD046-AA6B-4C27-A307-616C33DB89B7"
        #self.api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (self.doc_name,self.user_key)
        
    def getReportWithAPI(self, location):
        locA =  _function.getGeoForAddress(location)
        wp_state = get_state(locA,'wp')
        #print(wp_state)
        wp_loc = wp_state['state_name']
        
        if re.match('^46(.+)',wp_state['state_no']):
            doc_name = self.doc_name_46
        elif re.match('^C0(.+)',wp_state['state_no']):
            doc_name = self.doc_name_C0
               
       # https://opendata.cwb.gov.tw/api/v1/rest/datastore/
       #{dataid}? 資料編號
       #locationName={locationName} #
       #&elementName={elementName}
       #&sort={sort}
       #&parameterName={parameterName}

        #print(location)
        headers = {'Authorization': self.user_key}
        #url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/%s' % self.doc_name
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/%s?locationName=%s' % (doc_name, wp_loc)
        #res = requests.get("http://opendata.cwb.gov.tw/api/v1/rest/datastore/%s?locationName=%s" % (doc_name, wp_loc), headers=headers)
        res = requests.get(url, headers=headers)
        wp_json = res.json()
        
        #ELEV 高度 公尺
        #WDIR 風向 度
        #WDSD 風速 公尺/秒
        #TEMP 溫度 攝氏
        #HUMD 濕度 %
        #PRES 氣壓 百帕
        #SUN 日照時數 
        #H_24R 日累積雨量 毫米
        #WS15M
        #WD15M
        #WS15T
        #D_TX 本日最高溫   #D_TXT 本日最低溫時間
        #D_TN 本日最低溫   #D_TNT 本日最低溫時間
        #CITY_SN 縣市編號  #TOWN_SN 鄉鎮編號
        #print(wp_json['records']['location'][0]['weatherElement'])
        if len(wp_json['records']['location']) == 0:
            return '目前 {} 觀測站沒有任何資料'.format(wp_loc)
        else:
            TIME = wp_json['records']['location'][0]['time']['obsTime']
            WDSD = wp_json['records']['location'][0]['weatherElement'][2]['elementValue']
            TEMP = wp_json['records']['location'][0]['weatherElement'][3]['elementValue']
            HUMD = wp_json['records']['location'][0]['weatherElement'][4]['elementValue']
            H_24R = wp_json['records']['location'][0]['weatherElement'][7]['elementValue']
            #D_TX = wp_json['records']['location'][0]['weatherElement'][14]['elementValue']
            #D_TN = wp_json['records']['location'][0]['weatherElement'][16]['elementValue']
            e = float(HUMD)/100*6.105*math.exp(17.27*float(TEMP)/(237.7+float(TEMP)))      
            AT = round(1.07*float(TEMP)+0.2*e-0.65*float(WDSD)-2.7,1)
            
            content = '觀測站：{}\n時間：{}\n溫度：{}°C\n體感溫度：{}°C\n濕度：{}%\n風速：{} m/s\n日累積雨量：{} 毫米\n-------------------\n資料來源：中央氣象局'.format(wp_loc,TIME[5:16],TEMP,AT,HUMD,WDSD,H_24R)
            return content
    

if __name__ == '__main__':
    main()
