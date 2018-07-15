# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 22:32:32 2018

@author: 宇星
"""

#from .http_client import HttpClient, RequestsHttpClient
#from .models import (
#    Error, Profile, MemberIds, Content, RichMenuResponse
#)
#from abc import ABCMeta, abstractmethod, abstractproperty

import requests
import json



def main():
    api = linbotapi()
    gid = 'C486996bc0cf57372409c1dc6d7a4f6f3'
    uid = 'Ud0414e339e9c242b19a2dd22dd1f6189'
    print(api.get_group_member_profile(gid,uid))
    
class linbotapi(object):
    
    DEFAULT_API_ENDPOINT = 'https://api.line.me'
     
    def __init__(self, endpoint=DEFAULT_API_ENDPOINT,
                 timeout=5):
        
        self.__version__ = '1.7.1'
        self.channel_access_token = 'EZcRgZVSqqzxzPO+PSuREAJxtAIMuKoHWkhH/Swj5xVe9Xvpv0eiBm3k8jDcwFMjEM0pmKx2Bb1vCGN45THZCEj9dLxpkAMrPiskCmgjXNZ8ivg6bzbEaWjst92+IMUSP+MklC/YkuGZ7GAyt/Uo8wdB04t89/1O/w1cDnyilFU='
        self.endpoint = endpoint
        self.headers = {
            'Authorization': 'Bearer ' + self.channel_access_token,
            'User-Agent': 'line-bot-sdk-python/' + self.__version__
        }

        #self.http_client = RequestsHttpClient(timeout=timeout)
            
    def get_group_member_profile(self, group_id, user_id, timeout=None):
        """Call get group member profile API.

        https://devdocs.line.me/en/#get-group-room-member-profile

        Gets the user profile of a member of a group that
        the bot is in. This can be the user ID of a user who has
        not added the bot as a friend or has blocked the bot.

        :param str group_id: Group ID
        :param str user_id: User ID
        :param timeout: (optional) How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is self.http_client.timeout
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`linebot.models.responses.Profile`
        :return: Profile instance
        """
        response = self._get(
            '/v2/bot/group/{group_id}/member/{user_id}'.format(group_id=group_id, user_id=user_id),
            timeout=timeout
        )
        print(response)
        #response.replace('b','')
        content = json.loads(response)
        return(content)
        #return Profile.new_from_json_dict(response.json)
    
    def _get(self, path, params=None, headers=None, stream=False, timeout=None):
        url = self.endpoint + path

        if headers is None:
            headers = {}
        headers.update(self.headers)

        response = self.http_client_get(
            url, headers=headers, params=params, stream=stream, timeout=5
        )

        #self.__check_error(response)
        return response
        
    def http_client_get(self, url, headers=None, params=None, stream=False, timeout=None):
        """GET request.

        :param str url: Request url
        :param dict headers: (optional) Request headers
        :param dict params: (optional) Request query parameter
        :param bool stream: (optional) get content as stream
        :param timeout: (optional), How long to wait for the server
            to send data before giving up, as a float,
            or a (connect timeout, read timeout) float tuple.
            Default is :py:attr:`self.timeout`
        :type timeout: float | tuple(float, float)
        :rtype: :py:class:`RequestsHttpResponse`
        :return: RequestsHttpResponse instance
        """
        if timeout is None:
            timeout = self.timeout

        response = requests.get(
            url, headers=headers, params=params, stream=stream, timeout=timeout
        )
        
        return response.content



if __name__ == '__main__':
    main()
