# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:58:43 2018

@author: 宇星
"""
import json
import requests
#import urllib
#from urllib.request import urlopen
import math

def main():
    #print(get_hsing())
    gfunction = function()
    #print (gfunction.getDistance('121.7812','25.0712','21.4420','24.9976'))
    print(gfunction.getGeoForAddress('龍山寺'))

class function(object):
    
    def __init__(self):
        self.name = 'start'
    
    def is_number(self,string):
        try:
            float(string)
            return True
        except ValueError:
            pass
         
        try:
            import unicodedata
            unicodedata.numeric(string)
            return True
        except (TypeError, ValueError):
            pass
         
        return False
    

    def wt_json(self, data, filename):   
    
        with open(filename, 'w') as outfile:  
            json.dump(data, outfile ,ensure_ascii=False,indent=2)
            
        return True
    
    def rd_json(self, filename):
    
        with open(filename) as json_file:  
            data = json.load(json_file)
            return(data)
        
    def getGeoForAddress_json(self,address):
        s_url = 'http://maps.googleapis.com/maps/api/geocode/json'
        payload ={'address':address}
        _json = requests.get(s_url, params=payload)
        return json.loads(_json.content)

    def getGeoForAddress(self,address):

        responseJson = self.getGeoForAddress_json(address)
        status = responseJson['status']
        while status == 'OVER_QUERY_LIMIT':
            responseJson = self.getGeoForAddress_json(address)
            status = responseJson['status']
            if status == "OK":
                Lat = responseJson['results'][0]['geometry']['location']['lat']
                Lng = responseJson['results'][0]['geometry']['location']['lng']
                return [Lat,Lng]
                break
        
        Lat = responseJson['results'][0]['geometry']['location']['lat']
        Lng = responseJson['results'][0]['geometry']['location']['lng']
        return [Lat,Lng]
      
    def getDistance(self,lon1, lat1, lon2, lat2):  # 经度1，纬度1，经度2，纬度2 （十进制度数）
        """
        根据经纬度计算距离
        :param lon1: 点1经度
        :param lat1: 点1纬度
        :param lon2: 点2经度
        :param lat2: 点2纬度
        :return:distance
        """
        # 将十进制度数转化为弧度
        lon1, lat1, lon2, lat2 = map(math.radians, [float(lon1), float(lat1), float(lon2), float(lat2)])
    
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        r = 6371.137  # 地球平均半径，单位为公里
        return float('%.2f' % (c * r))
    
#def get_hsing():
#    return s17api.hsing.getjson(0,1912544)

if __name__ == '__main__':
    main()

