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
    return 'ok'
    #_photos = photo_zone()
    #uid = 'Ud0414e339e9c242b19a2dd22dd1f6189'
    #content = _photos.add_watermark(uid)
    #content = _photos.imgur_album_images_delete('SZMo93Z')
    #print (content)

class photo_zone(object):
    
    def __init__ (self):
        self.obj_name = 'imgur_function'
        self.imgur_client_id = '33ed33e765afedc'
        self.imgur_client_secret = '04f0d5531b1d0978ff97fd990554c899e9e7e1f5'
        self.imgur_client_access_token = '85b737858a3ca32f1517bd9b8e2f5d2c5c97a647'
        self.imgur_client_refresh_token = '797c2292b2600815f93cc73bec6eb7c8bdbcd67e'       
        self.API_Get_Image = 'https://otakujpbweb.herokuapp.com/api/image/random/'
        self.client = ImgurClient(self.imgur_client_id, self.imgur_client_secret, self.imgur_client_access_token, self.imgur_client_refresh_token)
        self.imgur_client_id_twstar = '01b89e6403895f6'
        self.imgur_client_secret_twstar = '423c3f12bf3e45076b6f31f973ab57bc98a1b8df'
        self.imgur_client_access_token_twstar = 'be57cec8bf14f5a76b4cf2548f54ac2075c69bf4'
        self.imgur_client_refresh_token_twstar = 'f1a227c506a451a28a2e71f885c64bdc83bb4917'       
        self.client_twstar = ImgurClient(self.imgur_client_id_twstar, self.imgur_client_secret_twstar, self.imgur_client_access_token_twstar, self.imgur_client_refresh_token_twstar)
        self.imgur_client_id_otakuboy = '1dda2cd41124fae'
        self.imgur_client_secret_otakuboy = 'eee6132fb319fd84509fa5a9b95cff53345b5c4c'
        #pin 87df6f85bd
        self.imgur_client_access_token_otakuboy = '68b0a143f3afa4bcdc467571dc794911f5c79366'
        self.imgur_client_refresh_token_otakuboy = '77afec5369029ad10f2dfce95929c494a1a6f848'       
        self.client_otakuboy = ImgurClient(self.imgur_client_id_otakuboy, self.imgur_client_secret_otakuboy, self.imgur_client_access_token_otakuboy, self.imgur_client_refresh_token_otakuboy)
        
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

    def upload_imgur_twstar(self,album_id,path):
        #client = ImgurClient(self.imgur_client_id, self.imgur_client_secret, self.imgur_client_access_token, self.imgur_client_refresh_token)
        conf = {"album":album_id}
        res = self.client_twstar.upload_from_path(path,config=conf,anon=False)
        return res

    def upload_imgur_otakuboy(self,album_id,path):
        #client = ImgurClient(self.imgur_client_id, self.imgur_client_secret, self.imgur_client_access_token, self.imgur_client_refresh_token)
        conf = {"album":album_id}
        res = self.client_otakuboy.upload_from_path(path,config=conf,anon=False)
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
                  't8':'t8.ttc',
                  't9':'t9.ttf',
                  'e1':'e1.ttf',
                  'e2':'e2.ttf',
                  'e3':'e3.ttf',
                  'e4':'e4.ttf',
                  }
        
        ttf_name = ttf_dict[ttf]
        
        return '%s%s'%(ttf_path,ttf_name)
 
    
    def user_daily_photo(self,id,message,pictureUrl):
        
        try:
            path = 'jpg/' 
            p#ath = '../jpg/'
            _card_template = '%scard_template.jpg'%path
            card_template = '%scard_%s.jpg'%(path,id)
            user_photo = '%sprofile_%s.jpg'%(path,id)
            
            with open(user_photo, 'wb') as handle:
                user_pic = requests.get(pictureUrl, stream=True)
                handle.write(user_pic.content)
            
            copyfile(_card_template,card_template)
    
    
            template_img = Image.open(card_template)
            i_width, i_height = template_img.size 
            #print (i_width, i_height)
                    
            #user_photo = '../jpg/SS.jpg'
                    
            user_name = message[0]
            
            if len(user_name) >8:
                ttf_name = 60
            else:
                ttf_name = 72
                
            
            hp = str(message[1])
            mp = str(message[2])
            lucky = str(message[3])
            today = message[4]
            ATK = str(message[7])
            DEF = str(message[8])
            WIZ = message[6]
            #line = '=============================='
            keywords = message[5]
     
            m=len(keywords)
            if m >=46:
                kttf = 20
                new_keywords = []
                n = 0
                i = 16
                check = 16
                
                while i-m < check:
                    new_keywords.append(keywords[n:i])
                    n = i
                    i = i+check
            else:
                kttf = 24
                new_keywords = []
                n = 0
                i = 13
                check = 13
                
                while i-m < check:
                    new_keywords.append(keywords[n:i])
                    n = i
                    i = i+check
            
            wiz_font = self.get_ttf_path('t5')
            fontname = self.get_ttf_path('t4')
            
            #user_x = i_width-68
            #print(len(user_name))
            
                      
            template_img = self.add_words(id,WIZ,ttf_name,38,28,wiz_font,template_img)
            template_img = self.add_words(id,user_name,48,120,55,fontname,template_img,120)
            template_img = self.add_photo(id,user_photo,template_img)
            template_img = self.add_words(id,hp,15,294,530,fontname,template_img,146)
            template_img = self.add_words(id,mp,15,294,530,fontname,template_img,211)
            template_img = self.add_words(id,ATK,32,110,495,fontname,template_img)
            template_img = self.add_words(id,DEF,32,110,545,fontname,template_img)
            template_img = self.add_words(id,lucky,32,420,495,fontname,template_img)
            template_img = self.add_words(id,today,24,420,550,fontname,template_img)
            #template_img = self.add_words(id,line,20,40,437,fontname,template_img)
            l = 633
            for obj in new_keywords:
                l = l+27
                template_img = self.add_words(id,obj,kttf,133,l,fontname,template_img)
            
            template_img.save(card_template)
            del template_img
            
            #imgur_dict = ['otaku','twstar','otakuboy']
            #imgur_dict = ['otaku','otakuboy']
            #imgur_dict = ['otakuboy']
            #imgur_dict = ['twstar']
            imgur_dict = ['otaku']
            imgur_upload = random.choice(imgur_dict)
            
            if imgur_upload == 'otaku':                
                res = self.upload_imgur('SZMo93Z',card_template)
                #print('oktaku')
                return ('1',res)
            if imgur_upload == 'twstar':
                res = self.upload_imgur_twstar('soO4i9j',card_template)
                #print('twstar')
                return ('1',res) 
            if imgur_upload == 'otakuboy':
                res = self.upload_imgur_otakuboy('Ub4VfUk',card_template)
                #print('otakuboy')
                return ('1',res)                
        except:
            return ('0','卡片產生失敗，重新印制卡片功能開發中，請先用[查人物屬性]指令查看今天的屬性，並進行對戰')
    
    
    def add_words(self,id,text,fontsize, px, py, fontname,template_img, pxx=None, pyy=None):

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
        
        #print(i_width, t_width)
        
        if pxx != None:
            px = int(pxx+(((i_width-pxx)-t_width)/2)/2)
        
        if pyy != None:
            py = int(pyy+(((i_height-pyy)-t_height)/2)/2)   
    
        imagefile.paste(img, (px, py), img)
        del draw0, draw
        del img0, img
        
        return imagefile
 
    def add_photo(self,id,photo, template_img):

        imagefile = template_img
        
        i_width, i_height = template_img.size
        
        img = Image.open(photo)
        n_width, n_height = img.size
        
        height = 320
        radio = float(height/n_height)
        width = int(n_width*radio)
        nimg = img.resize((width,height), Image.BILINEAR)
        
        t_width, t_height = nimg.size
        
        px = int((i_width-t_width)/2)
        py = 140
        
        imagefile.paste(nimg, (px, py))
        del img, nimg
        
        return imagefile
    


if __name__ == '__main__':
    main()