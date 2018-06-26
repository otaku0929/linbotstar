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
            rate_chart_url = 'http://www.taiwanrate.org/exchange_rate_chart.php?c={}'.format(rate_chart(title))
            return [now,title,rate, re_rate, rate_chart_url]

def rate_ex(res):
    #print(res)
    rate_ex = "(.+)(美金|港幣|英鎊|澳幣|加拿大幣|加幣|新加坡幣|瑞士法郎|法郎|日圓|日幣|南非幣|瑞典幣|紐元|泰幣|泰銖|菲國比索|印尼幣|歐元|韓元|越南盾|馬來幣|人民幣)=(\d+)(\D+)"
    rate_rex = "(\D+)(\d+)=(美金|港幣|英鎊|澳幣|加拿大幣|加幣|新加坡幣|瑞士法郎|法郎|日圓|日幣|南非幣|瑞典幣|紐元|泰幣|泰銖|菲國比索|印尼幣|歐元|韓元|越南盾|馬來幣|人民幣)(.+)"
    rate_ex_0 = "(美金|港幣|英鎊|澳幣|加拿大幣|加幣|新加坡幣|瑞士法郎|法郎|日圓|日幣|南非幣|瑞典幣|紐元|泰幣|泰銖|菲國比索|印尼幣|歐元|韓元|越南盾|馬來幣|人民幣)=(\d+)"
    rate_rex_0 = "(\d+)=(美金|港幣|英鎊|澳幣|加拿大幣|加幣|新加坡幣|瑞士法郎|法郎|日圓|日幣|南非幣|瑞典幣|紐元|泰幣|泰銖|菲國比索|印尼幣|歐元|韓元|越南盾|馬來幣|人民幣)"
    if re.match(rate_ex,res):
        rate_type = re.search(rate_ex,res).group(2).replace('日幣','日圓').replace('加幣','加拿大幣').replace('泰銖','泰幣').replace('法郎','瑞士法郎')
        rate_list = rate(rate_type)
        money = int(re.search(rate_ex,res).group(3))
        get_rate = float(rate_list[2])
        count = round((money/get_rate),2)
        content = '臺灣銀行匯率 1:{}\n換算 {} {} = {} TWD'.format(get_rate, money, rate_type,count)
        return content
    if re.match(rate_rex,res):
        rate_type = re.search(rate_rex,res).group(3).replace('日幣','日圓').replace('加幣','加拿大幣').replace('泰銖','泰幣').replace('法郎','瑞士法郎')
        rate_list = rate(rate_type)
        money = int(re.search(rate_rex,res).group(2))
        get_rate = float(rate_list[3])
        count = round((money*get_rate),2)
        content = '臺灣銀行匯率 1:{}\n換算 {} TWD = {} {}'.format(get_rate, money,rate_type,count)
        return content
    if re.match(rate_ex_0,res):
        rate_type = re.search(rate_ex_0,res).group(1).replace('日幣','日圓').replace('加幣','加拿大幣').replace('泰銖','泰幣').replace('法郎','瑞士法郎')
        rate_list = rate(rate_type)
        money = int(re.search(rate_ex_0,res).group(2))
        get_rate = float(rate_list[2])
        count = round((money/get_rate),2)
        content = '臺灣銀行匯率 1:{}\n換算 {} {} = {} TWD'.format(get_rate, money, rate_type, count)
        return content
    if re.match(rate_rex_0,res):
        rate_type = re.search(rate_rex_0,res).group(2).replace('日幣','日圓').replace('加幣','加拿大幣').replace('泰銖','泰幣').replace('法郎','瑞士法郎')
        rate_list = rate(rate_type)
        money = int(re.search(rate_rex_0,res).group(1))
        get_rate = float(rate_list[2])
        count = round((money*get_rate),2)
        content = '臺灣銀行匯率 1:{}\n換算 {} TWD = {} {}'.format(get_rate, money,rate_type,count)
        return content

def rate_chart(res):
    rate_dict ={'美金':'USD',
                '港幣':'HKD',
                '英鎊':'GBP',
                '澳幣':'AUD',
                '加拿大幣':'CAD',
                '新加坡幣':'SGD',
                '瑞土法郎':'CHF',
                '日圓':'JPY',
                '南非幣':'ZAR',
                '瑞典幣':'SEK',
                '紐元':'NZD',
                '泰幣':'THB',
                '菲國比索':'PHP',
                '印尼幣':'IDR',
                '歐元':'EUR',
                '韓元':'KRW',
                '越南盾':'VND',
                '馬來幣':'MYR',
                '人民幣':'CNY'
                };
    return rate_dict[res]
    #return 'http://www.taiwanrate.org/exchange_rate_chart.php?c={}'.format(res)
