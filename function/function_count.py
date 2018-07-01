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

if __name__ == '__main__':
    res = 'B5'
    gs_write(res)
    print('OK')