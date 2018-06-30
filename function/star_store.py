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
                'url':'https://seller.pcstore.com.tw/S198614447/C1200056412.htm',
                'image':'https://i.imgur.com/jrg2cmw.jpg',
                'detail':'環保硅膠材質，柔軟可見，不易變形/n尺寸：長21cm高9cm/n數字碼：0-9數字5排'
                    },
            {
                'title':'長效防蚊扣',
                'url':'https://seller.pcstore.com.tw/S198614447/C1200281208.htm',
                'image':'https://i.imgur.com/90WjznL.jpg',
                'detail':'使用時效長，拆封使用就能有效驅趕蚊蟲時效長達2-3個月～',
                    },
            {
                'title':'匠師的故鄉美景農場',
                'url':'https://beauty-farm.webnode.tw/',
                'image':'https://i.imgur.com/ISbRAsA.jpg',
                'detail':'匠師的故鄉‧包子匠師‧濱海體驗‧台中旅遊',
                    }
                    
            ]
    
    random.shuffle(dict)
    return dict[0:]

if __name__ == '__main__':
    store_content = star_store()
    print(store_content[0]['title'])

