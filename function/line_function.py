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

    l = linebotapi()
    Channel_Access_Token = 'EZcRgZVSqqzxzPO+PSuREAJxtAIMuKoHWkhH/Swj5xVe9Xvpv0eiBm3k8jDcwFMjEM0pmKx2Bb1vCGN45THZCEj9dLxpkAMrPiskCmgjXNZ8ivg6bzbEaWjst92+IMUSP+MklC/YkuGZ7GAyt/Uo8wdB04t89/1O/w1cDnyilFU='
    event = '{"message": {"id": "8292540891445", "text": "#getevent", "type": "text"}, "replyToken": "3c906c12929b4af59cc95abdbb548d8d", "source": {"type": "user", "userId": "U9f2c61013256dfe556d70192388e4c7c"}, "timestamp": 1532076930183, "type": "message"}'
    gid = 'C242d43576cc89e1499857f1006192860'
    uid = 'U06de3af68c05061e744560da43c5dfcc'
    #profile = l.get_group_user_profiles(Channel_Access_Token,gid,uid)
    profile = l.get_user_name(Channel_Access_Token,event)
    print(profile['displayName'])

    
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
        
        event = json.loads(str(event_source))
        
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