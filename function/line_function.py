# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:32:32 2018

@author: 宇星
"""


import requests
import json
import re

import function.photo_zone
_photos = function.photo_zone.photo_zone()

def main():

        print('None')

    
class linebotapi(object):
    
    
    def __init__(self):
        
        #config = configparser.ConfigParser()
        #config.read("config.ini")
        #self.channel_access_token = config['line_bot']['Channel_Access_Token']
        self.user_api_url = 'https://api.line.me/v2/bot/profile/%s'
        self.group_api_url = 'https://api.line.me/v2/bot/group/%s/member/%s'
        self.room_api_url = 'https://api.line.me/v2/bot/room/%s/member/%s'
        self.content_url = 'https://api.line.me/v2/bot/message/%s/content'
        
    def get_profile(self,channel_access_token,source,uid,gid=None):
        
        if source == 'g':
            return self.get_group_user_profiles(channel_access_token,gid,uid)
        if source == 'r':
            return self.get_room_user_profiles(channel_access_token,gid,uid)
        if source == 'u':
            return self.gt_user_profiles(channel_access_token,uid)
        
    def get_user_name(self,channel_access_token,event_source):
        
        event = json.loads(event_source)
        source = event['source']['type']
        userId = event['source']['userId']
        #print(source, userId)
        if source == 'group':
            groupId = event['source']['groupId']
            return self.get_group_user_profiles(channel_access_token,groupId,userId)
        if source == 'room':
            roomId = event['source']['roomId']
            return self.get_room_user_profiles(channel_access_token,roomId,userId)
        if source == 'user':
            return self.gt_user_profiles(channel_access_token,userId)
        
    def get_photo(self,channel_access_token,message_id):
        
        url = self.content_url % message_id
        headers = {'Authorization': 'Bearer '+channel_access_token}        
        response = requests.get(url,headers=headers)
        message_content = response
        path = 'jpg/'
        #path = '../jpg/'
        image_file = '%s%s.jpg'%(path,'get_photo')
        
        with open(image_file, 'wb') as fd:
            for chunk in message_content.iter_content():
                fd.write(chunk)
                
        _photos.upload_imgur('sYVusGO',image_file)

        return 'upload'
        
    
    def gt_user_profiles(self,channel_access_token,userid):
        
        url = self.user_api_url % userid
        headers = {'Authorization': 'Bearer '+channel_access_token}   
        response = requests.get(url,headers=headers) 
        profiles = json.loads(response.content)
        
        return profiles      
    
    def get_group_user_profiles(self,channel_access_token,groupid,userid):
        
        url = self.group_api_url % (groupid,userid)
        headers = {'Authorization': 'Bearer '+channel_access_token}   
        response = requests.get(url,headers=headers) 
        profiles = json.loads(response.content)
        
        return profiles
    
    def get_room_user_profiles(self,channel_access_token,roomid,userid):
        
        url = self.room_api_url % (roomid,userid)
        headers = {'Authorization': 'Bearer '+channel_access_token}   
        response = requests.get(url,headers=headers) 
        profiles = json.loads(response.content)
        
        return profiles


if __name__ == '__main__':
    main()
