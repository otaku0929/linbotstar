# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 22:58:43 2018

@author: 宇星
"""
import os
import json
import requests
import math
from PIL import Image, ImageFont, ImageDraw

def main():
    #print(get_hsing())
    gfunction = function()
    #print (gfunction.getDistance('121.7812','25.0712','21.4420','24.9976'))
    print(gfunction.getGeoForAddress('龍山寺'))
    
    imgur_client_id = '33ed33e765afedc'
    imgur_client_secret = '04f0d5531b1d0978ff97fd990554c899e9e7e1f5'
    imgur_client_access_token = '85b737858a3ca32f1517bd9b8e2f5d2c5c97a647'
    imgur_client_refresh_token = '797c2292b2600815f93cc73bec6eb7c8bdbcd67e'
    album_id = 'sJMh0RE'

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
        #print(responseJson)
        
        if status == "ZERO_RESULTS":
            return "ZERO_RESULTS"
        
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

    def degToCompass(self,num):
        val=int((num/22.5)+.5)
        #arr=["N","NNE","NE","ENE","E","ESE", "SE", "SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
        arr=['北','北北東','東北','東北東','東','東南東','東南','南南東','南','南南西','西南','西南西','西','西北西','西北','北北西']
        return arr[(val % 16)]

    def mergejpg_h(self,p1,p2,output):
        
        img1 = Image.open(p1)
        img2 = Image.open(p2)
        w1,h1 = img1.size
        w2,h2 = img2.size
        
        #resized = im2.resize((w1,))
        _h=int(float(w1)/float(w2)*h2)
        nim = img2.resize((w1,_h),Image.BILINEAR)
        nim.save("/app/temp_jpg/resized.jpg")
        #nim.save("..//jpg//resized.jpg")
        
        mh= h1+_h
        merge_img = Image.new('RGB', (w1, mh), 0xffffff)
        i=0
        merge_img.paste(img1, (0, i))
        merge_img.paste(nim, (0, i+h1))
    
        merge_img.save(output)
        #merge_img.save("..//temp_jpg//merge_img.png")   
        
        return ("merge_OK")
    
    def imgur_album_images_delete(self,album_id):
        
        client = ImgurClient(imgur_client_id, imgur_client_secret, imgur_client_access_token, imgur_client_refresh_token)
        image_list = client.get_album_images(album_id)
        for obj in image_list:
            client.delete_image(obj.id)
        
        return ("delete complete")
    
    def imgur_images_delete(self,image_id):
        
        client = ImgurClient(imgur_client_id, imgur_client_secret, imgur_client_access_token, imgur_client_refresh_token)
        client.delete_image(image_id)
        
        return ("delete complete")

    def add_watermark(self,text, fontsize, ttf, position, imagefile, output_dir):
        
        #ttf_path='..//font//'
        ttf_path='/app/font/'
        
        if ttf == 't1':
            fontname = ttf_path+'wt014.ttf'
        elif ttf == 't2':
            fontname = ttf_path+'/wt028.ttf'
        elif ttf == 't3':
            fontname = ttf_path+'wt040.ttf'
        elif ttf == 't4':
            fontname = ttf_path+'wt064.ttf'
        elif ttf == 't5':
            fontname = ttf_path+'wt071.ttf'
            
            
        img0 = Image.new("RGBA", (1,1))
        draw0 = ImageDraw.Draw(img0)
        font = ImageFont.truetype(fontname, fontsize)
        t_width, t_height = draw0.textsize(text, font=font)
        #t_width, t_height = draw0.textsize(unicode(text, 'UTF-8'), font=font)
        img = Image.new("RGBA", (t_width, t_height), (255,0,0,0))
        draw = ImageDraw.Draw(img)
        #draw.text((0,0),unicode(text, 'UTF-8'), font=font, fill=(255,255,255,128))
        draw.text((0,0),text,font=font, fill=(255,255,255,128))
        img2 = Image.open(imagefile)
        i_width, i_height = img2.size
        
        if position == 'p1':
            px = int(i_width*(1/15))
            py = int(i_height*(1/15))
        elif position == 'p2':
            px = int(i_width*(1/15))
            py = int((i_height-t_height)/2)
        elif position == 'p3':
            px = int(i_width*(1/15))
            py = int((i_height-t_height)*(14/15))
        elif position == 'p4':
            px = int((i_width-t_width)/2)
            py = int(i_height*(1/15))
        elif position == 'p5':
            px = int((i_width-t_width)/2)
            py = int((i_height-t_height)/2)
        elif position == 'p6':
            px = int((i_width-t_width)/2)
            py = int(i_height*(14/15))
        elif position == 'p7':
            px = int((i_width-t_width)*(14/15))
            py = int(i_height*(1/15))
        elif position == 'p8':
            px = int((i_width-t_width)*(14/15))
            py = int((i_height-t_height)/2)
        elif position == 'p9':
            px = int((i_width-t_width)*(14/15))
            py = int((i_height-t_height)*(14/15))
    
        img2.paste(img, (px, py), img)
        imagefile = imagefile.split('/')[-1]
        imagefile = "wm_" + imagefile
        print (imagefile + " saved...")
        img2.save(output_dir + imagefile)
        del draw0, draw
        del img0, img, img2
        
        return ("imagefile saved")

    def set_watermark(self,uid, text, fontsize, ttf, position):

        set_json = '/app/json_file/watermark_{}.json'.format(uid)
        #set_json = '..//json_file//watermark_{}.json'.format(uid)'
        print(set_json)
        watermark_json = {'watermark':{'text':text,'fontsize':fontsize,'ttf':ttf,'position':position}}
        if os.path.exists(set_json):
            with open(set_json) as jsonfile:
                data = json.load(jsonfile)
                data.update(watermark_json)
                print(data)
        else:        
            with open(set_json,'w') as outfile:
                json.dump(watermark_json, outfile ,ensure_ascii=False,indent=2)

        return '完成設定'
    
#def get_hsing():
#    return s17api.hsing.getjson(0,1912544)

if __name__ == '__main__':
    main()

