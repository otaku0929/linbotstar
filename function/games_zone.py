# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 08:30:04 2018

@author: 宇星
"""

import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

def main():
    _games = games_zone()
    content = _games.r18()
    print(content)

class games_zone(object):
    
    def __init__(self):
        self.class_name = 'games_zone'
        
    def r18(self):

        a = random.randint(1,6)
        b = random.randint(1,6)
        c = random.randint(1,6)
        d = random.randint(1,6)
    
        rlist = [a,b,c,d]
        seen = set()      
        y = [n for n in rlist if n not in seen and not seen.add(n)]
    
        c2=""
        c3=""
        n=0
    
        for i in rlist:
            if rlist.count(int(i)) == 2:
               c2 = i
            if rlist.count(int(i)) == 3:
               c3 = i
    
        if len(y) == 4:
            content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n沒點, 再擲一次吧!!!'.format(a,b,c,d)
            return content
        if len(y) ==1:
          if y[0]==6:
             content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n豹子通殺!!!!'.format(a,b,c,d)
             return content
          else:
             content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n點數為:水哦 {}一色'.format(a,b,c,d,y[0])
             return content
        if len(y)==3:
          for i2 in rlist:
              if i2 != c2:
                  n = n+i2
              else:
                  pass
          if n ==3:
              content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n{}點 逼機 >"<" '.format(a,b,c,d,n)
              return content
          else:
              content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n{}點'.format(a,b,c,d,n)
              return content
        if len(y)==2 and c3 !='':
            content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n沒點, 再擲一次吧!!!'.format(a,b,c,d,n)
            return content
        if len(y)==2:         
           content = '18啦~~\n\n本次擲出結果為:{},{},{}.{}\n\n水哦  十八!!!!'.format(a,b,c,d,n)
           return content

    def luck777():
        
        GDriveJSON = 'star-lucky777-580f56621f40.json'
        GSpreadSheet = 'lucky777'
    
        scope = ['https://spreadsheets.google.com/feeds']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
    
        n = int(worksheet.acell('A1').value)
        x = "%03d"% random.randint(0,999)
    
        if x == '777':
            content ="winner"
            n = 0
            worksheet.update_acell('A1',n)
        else:
            n += 1
            content = 'Lucky 777 \n目前累積拉霸次數:{}\n本次幸運號為:{} \n再試試手氣吧'.format(n,x)
            worksheet.update_acell('A1',n)
    
        return content

if __name__ == '__main__':
    main()