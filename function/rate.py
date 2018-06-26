# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas
import datetime

def rate(res):

    url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
    dfs = pandas.read_html(url)
    currency = dfs[0]
    currency = currency.ix[:,0:3]
    currency.columns = [u'貨幣',u'匯率(賣)',u'匯率(買)']
    currency[u'貨幣'] = currency[u'貨幣'].str.split('\(',1).str[0]
    currency[u'貨幣'] = currency[u'貨幣'].str.split().str[0]

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    for a in currency.index:
        data = currency.ix[a,0]
        if data == res:
            title = currency.ix[a,0]
            rate =currency.ix[a,2]
            ratedata = '{} 1:{}'.format(title,rate)   

    return '臺灣銀行牌告匯率\n查詢時間{}\n{}'.format(now,ratedata)
