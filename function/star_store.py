# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 20:40:17 2018

@author: 宇星
"""
import random

    
def star_store():
    dict=[
            {
                'title':'夜光卡通造型汽車臨時停車卡',
                'url':'http://seller.pcstore.com.tw/S198614447/C1200056412.htm',
                'image':'https://i.imgur.com/jrg2cmw.jpg',
                'detail':'..厚度增加，防止受熱后，出現卷邊情況\n..環保硅膠材質，柔軟可見，不易變形\n..防滑背面'
                    },
            {
                'title':'長效防蚊扣',
                'url':'http://seller.pcstore.com.tw/S198614447/C1200281208.htm',
                'image':'https://i.imgur.com/90WjznL.jpg',
                'detail':'使用時效長，拆封使用就能有效驅趕蚊蟲時效長達2-3個月～',
                    },
            {
                'title':'匠師的故鄉美景農場',
                'url':'http://0426815735.tw.tranews.com/',
                'image':'https://i.imgur.com/ISbRAsA.jpg',
                'detail':'匠師的故鄉‧包子匠師‧濱海體驗‧台中旅遊',
                    }
                    
            ]
    
    random.shuffle(dict)
    return dict[0:]

if __name__ == '__main__':
    print(star_store())

