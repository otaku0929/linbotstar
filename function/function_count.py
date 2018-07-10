# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 19:49:28 2018

@author: 宇星
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

def gs_write(res):
    
    GDriveJSON = 'star-lucky777-580f56621f40.json'
    GSpreadSheet = 'lucky777'

    scope = ['https://spreadsheets.google.com/feeds']
    key = SAC.from_json_keyfile_name(GDriveJSON, scope)
    gc = gspread.authorize(key)
    worksheet = gc.open(GSpreadSheet).sheet1

    n = int(worksheet.acell(res).value)
    n += 1
    worksheet.update_acell(res,n)

def gs_read():
    
    GDriveJSON = 'star-lucky777-580f56621f40.json'
    GSpreadSheet = 'lucky777'

    scope = ['https://spreadsheets.google.com/feeds']
    key = SAC.from_json_keyfile_name(GDriveJSON, scope)
    gc = gspread.authorize(key)
    worksheet = gc.open(GSpreadSheet).sheet1
    
    fun_json=[]
    
    for obj in range(2,31):
        json_obj={worksheet.acell('A'+str(obj)).value:worksheet.acell('B'+str(obj)).value}
        fun_json.append(json_obj)
    
    return fun_json

def get_fun_count():
    
    obj_json = gs_read()
    content = "";
    
    for obj in obj_json:
        content = '{}\n{}'.format(content,obj)
    
    return content
    

if __name__ == '__main__':
    #res = 'B5'
    #gs_write(res)
    print(get_fun_count())
