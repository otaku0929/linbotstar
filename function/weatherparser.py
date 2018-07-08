# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 23:09:59 2018

@author: 宇星
"""

import requests
import json
import re
from .get_wp_state import get_state


import g_function
gfunction = g_function.function()

def main():
    messages = '天氣=台北公館'
    match = re.match('(.+)*天氣=(.+)',messages)
    loc = match.group(2)
    #print(loc)
    wp = WeatherParser()
    locA =  gfunction.getGeoForAddress(loc)
    wp_name = get_state(locA,'C0')
    #print(wp_name['state_name'])
    #print(wp_location)
    wp_content = (wp.getReportWithAPI(wp_name['state_name']))
    content = '地點:{}\n{}'.format(loc,wp_content)
    print(content)

class WeatherParser(object):
    
    def __init__(self):
        self.doc_name = "O-A0001-001"#"F-C0032-001"  
        self.user_key = "CWB-A01FD046-AA6B-4C27-A307-616C33DB89B7"
        #self.api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (self.doc_name,self.user_key)
        
    def getReportWithAPI(self, location):
               
       # https://opendata.cwb.gov.tw/api/v1/rest/datastore/
       #{dataid}? 資料編號
       #locationName={locationName} #
       #&elementName={elementName}
       #&sort={sort}
       #&parameterName={parameterName}

        #print(location)
        headers = {'Authorization': self.user_key}
        #url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/%s' % self.doc_name
        url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/%s?locationName=%s' % (self.doc_name, location)
        #res = requests.get("http://opendata.cwb.gov.tw/api/v1/rest/datastore/%s?locationName=%s" % (self.doc_name, location), headers=headers)
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
        #print(wp_json['records']['location'][0]['weatherElement'])
        TIME = wp_json['records']['location'][0]['time']['obsTime']
        TEMP = wp_json['records']['location'][0]['weatherElement'][3]['elementValue']
        HUMD = wp_json['records']['location'][0]['weatherElement'][4]['elementValue']
        H_24R = wp_json['records']['location'][0]['weatherElement'][7]['elementValue']
        
        content = '查詢時間:{}\n溫度:{} C\n濕度:{}%\n日累積雨量:{} 毫米'.format(TIME[0:16],TEMP,HUMD,H_24R)
        return content
    

if __name__ == '__main__':
    main()
