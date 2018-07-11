# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 13:03:45 2018

@author: 宇星
"""

def main():
    
    _sys_mg=sys_messages()
    print(_sys_mg.m_addmark())
    
class sys_messages(object):
    
    def __init__ (self):
        self.obj_name = 'sys_messages'
    
    def m_addmark(self):
        return '請先設定浮水印輸出格式，方式如下:\n\
 浮水印t=小星星浮水印f=52ttf=t4c=whiteal=128p=p9\n\
  ------------\n\
  *t=浮水印內容\n\
  *f=字體大小\n\
  *ttf=字型：目前共有中文7,英文4種t1~t7 e1~e4 \n\
  *c=顏色:支援red|green|blue|white|break|pink|yellow|gold, 也可以輸入色票#ffffff\n\
  *al=透明度:0~255 (建議不要小於128)\n\
  *p=浮水印位置：以九宮格方式劃分'
    
    
if __name__ == '__main__':
    main()