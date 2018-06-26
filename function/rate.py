# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import pandas
import datetime
import pytz
import re

def rate(res):

    url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
    dfs = pandas.read_html(url)
    currency = dfs[0]
    currency = currency.ix[:,0:3]
    currency.columns = [u'貨幣',u'匯率(賣)',u'匯率(買)']
    currency[u'貨幣'] = currency[u'貨幣'].str.split('\(',1).str[0]
    currency[u'貨幣'] = currency[u'貨幣'].str.split().str[0]

    tw = pytz.timezone('Asia/Taipei')
    #us = pytz.timezone('US/Pacific')
    now = datetime.datetime.now(tw).strftime("%Y-%m-%d %H:%M")

    for a in currency.index:
        data = currency.ix[a,0]
        if data == res:
            title = currency.ix[a,0]
            rate =currency.ix[a,2]
            re_rate = currency.ix[a,1]

    return [now,title,rate, re_rate]

def rate_ex(res):
    
    rate_ex = "(美金|日幣|人民幣)=(\d+)"
    rate_rex = "(\d+)=(美金|日幣|人民幣)"
    if re.match(rate_ex,res):
        rate_type = re.search(rate_ex,res).group(1)
        rate_list = rate(rate_type)
        money = int(re.search(rate_ex,res).group(2))
        get_rate = float(rate_list[2])
        count = round((money/get_rate),2)
        content = '臺灣銀行匯率 1:{}\n換算 {} TWD = {} {}'.format(get_rate, money,rate_type,count)
        return content
    if re.match(rate_rex,res):
        rate_type = re.search(rate_rex,res).group(2)
        rate_list = rate(rate_type)
        money = int(re.search(rate_rex,res).group(1))
        get_rate = float(rate_list[3])
        count = round((money*get_rate),2)
        content = '臺灣銀行匯率 1:{}\n換算 {} {} = {} TWD'.format(get_rate, count, rate_type,money)
        return content
