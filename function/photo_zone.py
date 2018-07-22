# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 00:32:14 2018

@author: 宇星
"""

import requests
import random
import json
import os
from shutil import copyfile
from imgurpython import ImgurClient
from PIL import Image, ImageFont, ImageDraw, ImageColor

import function.sql
_sql = function.sql.Sql()

import function.g_function
_function = function.g_function.function()

from linebot.models import (
        MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)


def main():
    #return 'ok'
    _photos = photo_zone()
    uid = 'Ud0414e339e9c242b19a2dd22dd1f6189'
    content = _photos.add_watermark(uid)
    print (content)

class photo_zone(object):
    
    def __init__ (self):
        self.obj_name = 'imgur_function'
        self.imgur_client_id = '33ed33e765afedc'
        self.imgur_client_secret = '04f0d5531b1d0978ff97fd990554c899e9e7e1f5'
        self.imgur_client_access_token = '85b737858a3ca32f1517bd9b8e2f5d2c5c97a647'
        self.imgur_client_refresh_token = '797c2292b2600815f93cc73bec6eb7c8bdbcd67e'       
        self.API_Get_Image = 'https://otakujpbweb.herokuapp.com/api/image/random/'
        self.client = ImgurClient(self.imgur_client_id, self.imgur_client_secret, self.imgur_client_access_token, self.imgur_client_refresh_token)
        
    def random(self):
        b=self.imgur_boys
        g=self.beauty_girls
        gs=self.imgur_girls
        content = random.choice([b,g,b,g,b,g,g,gs,g,gs])
        return content()
        
                 
    def beauty_girls(self):
        images =  requests.get(self.API_Get_Image)
        url = images.json().get('Url')
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        return image_message
    
    def imgur_girls(self):
        return self.get_imgur_photo('23p2B')
    
    def imgur_boys(self):
        return self.get_imgur_photo('9eQni')       

    def joke(self):
        return self.get_imgur_photo('XpG2g')   
    
    def poker(self):
        return self.get_imgur_photo('KQjab')
    
    def gods_talk(self):
        return self.get_imgur_photo('6FM69')
    
    def single(self):
        return self.get_imgur_photo('Sy6Gm')
    
    def food(self):
        return self.get_imgur_photo('9rYK8')    
    
    def get_imgur_photo(self,album_id):
        client = ImgurClient(self.imgur_client_id, self.imgur_client_secret)
        images = client.get_album_images(album_id)
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        return image_message
    
    def upload_imgur(self,album_id,path):
        #client = ImgurClient(self.imgur_client_id, self.imgur_client_secret, self.imgur_client_access_token, self.imgur_client_refresh_token)
        conf = {"album":album_id}
        res = self.client.upload_from_path(path,config=conf,anon=False)
        return res

    def imgur_album_images_delete(self,album_id):      
        #client = ImgurClient(imgur_client_id, imgur_client_secret, imgur_client_access_token, imgur_client_refresh_token)
        image_list = self.client.get_album_images(album_id)
        for obj in image_list:
            self.client.delete_image(obj.id)
        
        return ("delete complete")

    def imgur_images_delete(self,image_id):
        
        #client = ImgurClient(imgur_client_id, imgur_client_secret, imgur_client_access_token, imgur_client_refresh_token)
        self.client.delete_image(image_id)
        
        return ("deleted image")

    def add_watermark(self,id,message_content):
        
        user_config = _sql.select_config(id)
        
        if user_config ==[]:
            return 'none'
        else:
           config_json = user_config[0][2]
           config = json.loads(config_json)   
        
   
      
        if config['watermark'] == {}:
            return 'none'
        else:                                   
            path = 'jpg/'
            #path = '../jpg/'
            #path = '/app/jpg/'
            image_file = '%s%s.jpg'%(path,id)
            output_jpg = '%swm_%s.jpg'%(path,id)
            output_dir = path
            
            with open(image_file, 'wb') as fd:
                for chunk in message_content.iter_content():
                    fd.write(chunk)
            
            data = config['watermark']
            #print(data)
            
            text = data['text']
            fontsize = data['fontsize']
            ttf = data['ttf']
            color = data['color']
            alpha = data['alpha']
            position = data['position']
            _function.add_watermark(text, int(fontsize), ttf, color, int(alpha), position, image_file, output_dir)
            res = self.upload_imgur('SZMo93Z',output_jpg)
            return res
        
    def get_ttf_path(self,ttf):
        
        ttf_path='font/'
        #ttf_path='../font/'
        
        ttf
        
        ttf_dict={'t1':'wt014.ttf',
                  't2':'wt028.ttf',
                  't3':'wt040.ttf',
                  't4':'wt064.ttf',
                  't5':'wt071.ttf',
                  't6':'c01W4.ttc',
                  't7':'c02W3.ttc',
                  'e1':'e1.ttf',
                  'e2':'e2.ttf',
                  'e3':'e3.ttf',
                  'e4':'e4.ttf',
                  }
        
        ttf_name = ttf_dict[ttf]
        
        return '%s%s'%(ttf_path,ttf_name)
 
    
    def user_daily_photo(self,id,message,pictureUrl):
        
        path = 'jpg/' 
        #path = '../jpg/'
        _card_template = '%scard_template.jpg'%path
        card_template = '%scard_%s.jpg'%(path,id)
        user_photo = '%sprofile_%s.jpg'%(path,id)
        
        with open(user_photo, 'wb') as handle:
            user_pic = requests.get(pictureUrl, stream=True)
            handle.write(user_pic.content)
        
        copyfile(_card_template,card_template)


        template_img = Image.open(card_template)
        i_width, i_height = template_img.size     
                
        #user_photo = '../jpg/SS.jpg'
                
        user_name = message[0]
        hp = message[1]
        mp = message[2]
        lucky = message[3]
        today = message[4]
        line = '=============================='
        keywords = message[5]
        
        new_keywords = []
        n = 0
        i = 18
        check = 18
        m=len(keywords)
    
        while i-m < check:
            new_keywords.append(keywords[n:i])
            n = i
            i = i+check 
        
        fontname = self.get_ttf_path('t1')
        
        template_img = self.add_words(id,user_name,32,40,20,fontname,template_img)
        template_img = self.add_photo(id,user_photo,40,64,template_img)
        template_img = self.add_words(id,hp,20,40,326,fontname,template_img)
        template_img = self.add_words(id,mp,20,40,356,fontname,template_img)
        template_img = self.add_words(id,lucky,20,40,383,fontname,template_img)
        template_img = self.add_words(id,today,20,40,410,fontname,template_img)
        template_img = self.add_words(id,line,20,40,437,fontname,template_img)
        l = 437
        for obj in new_keywords:
            l = l+27
            template_img = self.add_words(id,obj,18,40,l,fontname,template_img)
        
        template_img.save(card_template)
        del template_img
        
        res = self.upload_imgur('SZMo93Z',card_template)
        
        return res
    
    
    def add_words(self,id,text,fontsize, px, py, fontname,template_img):

        imagefile = template_img
        r=255;g=255;b=255
         
        img0 = Image.new("RGBA", (1,1))
        draw0 = ImageDraw.Draw(img0)
        font = ImageFont.truetype(fontname, fontsize)
        t_width, t_height = draw0.textsize(text, font=font)        
        img = Image.new("RGBA", (t_width, t_height), (255,0,0,0))
        draw = ImageDraw.Draw(img)
        draw.text((0,0),text,font=font, fill=(r,g,b))
        
        i_width, i_height = template_img.size     
    
        imagefile.paste(img, (px, py), img)
        del draw0, draw
        del img0, img
        
        return imagefile
 
    def add_photo(self,id,photo, px, py, template_img):

        imagefile = template_img
        
        i_width, i_height = template_img.size
        
        img = Image.open(photo)
        n_width, n_height = img.size
        
        height = 250
        radio = float(height/n_height)
        width = int(n_width*radio)
        nimg = img.resize((width,height), Image.BILINEAR)   
        imagefile.paste(nimg, (px, py))
        del img, nimg
        
        return imagefile
    


if __name__ == '__main__':
    main()