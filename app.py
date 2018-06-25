import time
import requests
import re
import random
import configparser
import urllib.request
import pandas
import gspread
import twstock
import json
from oauth2client.service_account import ServiceAccountCredentials as SAC
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient
from selenium import webdriver
from datetime import datetime, timedelta
from function.function import shelp
from function.star_talk import star_talk
from function.s17api import s17uidrandom
from function.s17api import s17uidsong
from function.tarot_detail import tarot_random
from function.tarot_detail import tarot_random_get
from function.tarot_detail import tarot_detail

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
handler = WebhookHandler(config['line_bot']['Channel_Secret'])
client_id = config['imgur_api']['Client_ID']
client_secret = config['imgur_api']['Client_Secret']
album_id = config['imgur_api']['Album_ID']
API_Get_Image = config['other_api']['API_Get_Image']

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'


def pattern_mega(text):
    patterns = [
        'mega', 'mg', 'mu', 'ＭＥＧＡ', 'ＭＥ', 'ＭＵ',
        'ｍｅ', 'ｍｕ', 'ｍｅｇａ', 'GD', 'MG', 'google',
    ]
    for pattern in patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return True


def eyny_movie():
    target_url = 'http://www.eyny.com/forum-205-1.html'
    print('Start parsing eynyMovie....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ''
    for titleURL in soup.select('.bm_c tbody .xst'):
        if pattern_mega(titleURL.text):
            title = titleURL.text
            if '11379780-1-3' in titleURL['href']:
                continue
            link = 'http://www.eyny.com/' + titleURL['href']
            data = '{}\n{}\n\n'.format(title, link)
            content += data
    return content


def apple_news():
    target_url = 'http://www.appledaily.com.tw/realtimenews/section/new/'
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')

    news_list = soup.select('div.item a')
    random.shuffle(news_list)
    randomnews = news_list[0:5]
    
    content = ""
    for data in randomnews:
        url = data.get('href')
        text = data.select('img')[0]['alt']
        news = '{}\n{}'.format(text,url)
        content += '{}\n'.format(news)
    return content


def get_page_number(content):
    start_index = content.find('index')
    end_index = content.find('.html')
    page_number = content[start_index + 5: end_index]
    return int(page_number) + 1


def craw_page(res, push_rate):
    soup_ = BeautifulSoup(res.text, 'html.parser')
    article_seq = []
    for r_ent in soup_.find_all(class_="r-ent"):
        try:
            # 先得到每篇文章的篇url
            link = r_ent.find('a')['href']
            if link:
                # 確定得到url再去抓 標題 以及 推文數
                title = r_ent.find(class_="title").text.strip()
                rate = r_ent.find(class_="nrec").text
                url = 'https://www.ptt.cc' + link
                if rate:
                    rate = 100 if rate.startswith('爆') else rate
                    rate = -1 * int(rate[1]) if rate.startswith('X') else rate
                else:
                    rate = 0
                # 比對推文數
                if int(rate) >= push_rate:
                    article_seq.append({
                        'title': title,
                        'url': url,
                        'rate': rate,
                    })
        except Exception as e:
            # print('crawPage function error:',r_ent.find(class_="title").text.strip())
            print('本文已被刪除', e)
    return article_seq


def crawl_page_gossiping(res):
    soup = BeautifulSoup(res.text, 'html.parser')
    article_gossiping_seq = []
    for r_ent in soup.find_all(class_="r-ent"):
        try:
            # 先得到每篇文章的篇url
            link = r_ent.find('a')['href']

            if link:
                # 確定得到url再去抓 標題 以及 推文數
                title = r_ent.find(class_="title").text.strip()
                url_link = 'https://www.ptt.cc' + link
                article_gossiping_seq.append({
                    'url_link': url_link,
                    'title': title
                })

        except Exception as e:
            # print u'crawPage function error:',r_ent.find(class_="title").text.strip()
            # print('本文已被刪除')
            print('delete', e)
    return article_gossiping_seq


def ptt_gossiping():
    rs = requests.session()
    load = {
        'from': '/bbs/Gossiping/index.html',
        'yes': 'yes'
    }
    res = rs.post('https://www.ptt.cc/ask/over18', verify=False, data=load)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_page_url = soup.select('.btn.wide')[1]['href']
    start_page = get_page_number(all_page_url)
    index_list = []
    article_gossiping = []
    for page in range(start_page, start_page - 2, -1):
        page_url = 'https://www.ptt.cc/bbs/Gossiping/index{}.html'.format(page)
        index_list.append(page_url)

    # 抓取 文章標題 網址 推文數
    while index_list:
        index = index_list.pop(0)
        res = rs.get(index, verify=False)
        # 如網頁忙線中,則先將網頁加入 index_list 並休息1秒後再連接
        if res.status_code != 200:
            index_list.append(index)
            # print u'error_URL:',index
            # time.sleep(1)
        else:
            article_gossiping = crawl_page_gossiping(res)
            # print u'OK_URL:', index
            # time.sleep(0.05)
    content = ''

    random.shuffle(article_gossiping)
    randomdata = article_gossiping[0:3]
    
    for article in randomdata:
        data = '{}\n{}\n\n'.format(article.get('title', None), article.get('url_link', None))
        content += data
    return content

def ptt_beauty():
    rs = requests.session()
    res = rs.get('https://www.ptt.cc/bbs/Beauty/index.html', verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_page_url = soup.select('.btn.wide')[1]['href']
    start_page = get_page_number(all_page_url)
    page_term = 3  # crawler count
    push_rate = 10  # 推文
    index_list = []
    article_list = []
    for page in range(start_page, start_page - page_term, -1):
        page_url = 'https://www.ptt.cc/bbs/Beauty/index{}.html'.format(page)
        index_list.append(page_url)

    # 抓取 文章標題 網址 推文數
    while index_list:
        index = index_list.pop(0)
        res = rs.get(index, verify=False)
        # 如網頁忙線中,則先將網頁加入 index_list 並休息1秒後再連接
        if res.status_code != 200:
            index_list.append(index)
            # print u'error_URL:',index
            # time.sleep(1)
        else:
            article_list = craw_page(res, push_rate)
            # print u'OK_URL:', index
            # time.sleep(0.05)
    content = ''
    for article in article_list:
        data = '[{} push] {}\n{}\n\n'.format(article.get('rate', None), article.get('title', None),
                                             article.get('url', None))
        content += data
    return content

def ptt_Stupid():
    rs = requests.session()
    res = rs.get('https://www.ptt.cc/bbs/StupidClown/index.html', verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_page_url = soup.select('.btn.wide')[1]['href']
    start_page = get_page_number(all_page_url)
    page_term = 3  # crawler count
    push_rate = 10  # 推文
    index_list = []
    article_list = []
    for page in range(start_page, start_page - page_term, -1):
        page_url = 'https://www.ptt.cc/bbs/StupidClown/index{}.html'.format(page)
        index_list.append(page_url)

    # 抓取 文章標題 網址 推文數
    while index_list:
        index = index_list.pop(0)
        res = rs.get(index, verify=False)
        # 如網頁忙線中,則先將網頁加入 index_list 並休息1秒後再連接
        if res.status_code != 200:
            index_list.append(index)
            # print u'error_URL:',index
            # time.sleep(1)
        else:
            article_list = craw_page(res, push_rate)
            # print u'OK_URL:', index
            # time.sleep(0.05)
    content = ''
    for article in article_list:
        data = '[{} push] {}\n{}\n\n'.format(article.get('rate', None), article.get('title', None),
                                             article.get('url', None))
        content += data
    return content

def ptt_hot():
    target_url = 'http://disp.cc/b/PttHot'
    print('Start parsing pttHot....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""

    hotlist = soup.select('#list div.row2 div span.listTitle')
    del hotlist[len(hotlist)-1]
    random.shuffle(hotlist)
    randomhot = hotlist[0:5]
   
    for data in randomhot:
        title = data.text
        link = "http://disp.cc/b/" + data.find('a')['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def movie():
    alist = []
    for page in range(1,3):#collect movies from 5 page
        page_url = 'http://tw.movies.yahoo.com/movie_intheaters.html?page={}'.format(page)
        res = requests.get(page_url)
        movie_list = ymovie_content(res)
        for movie in movie_list:
            alist.append(movie)        
    
    #select 3 mobvies from 5 page
    random.shuffle(alist)
    randommovie = alist[0:3]

    #export movie information 
    content = ""
    for data in randommovie:
        title = format(data.get("data-ga")[20:].strip("]"))
        url = format(data.get("href"))
        #img = data.select('img')[0]['src']
        content += '院線電影{}\n{}\n\n'.format(title,url)

    return content

def movie_new():

    alist = []
    for page in range(1,2):#collect movies from 5 page
        page_url = 'https://tw.movies.yahoo.com/movie_thisweek.html?page={}'.format(page)
        res = requests.get(page_url)
        movie_list = ymovie_content(res)
        for movie in movie_list:
            alist.append(movie)        
    
    #select 3 mobvies from 5 page
    random.shuffle(alist)
    randommovie = alist[0:3]

    #export movie information 
    content = ""
    for data in randommovie:
        title = format(data.get("data-ga")[23:].strip("]"))
        url = format(data.get("href"))
        #img = data.select('img')[0]['src']
        content += '本週上映{}\n{}\n\n'.format(title,url)

    return content
    
def ymovie_content(res):
    #rescontent = res.content
    soup = BeautifulSoup(res.content,'html.parser')
    
    content = ""
    alist = soup.select("div.release_foto a[class='gabtn']")
    
    return alist

def technews():
    target_url = 'https://technews.tw/'
    print('Start parsing movie ...')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""

    for index, data in enumerate(soup.select('article div h1.entry-title a')):
        if index == 12:
            return content
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content


def panx():
    target_url = 'https://panx.asia/'
    print('Start parsing ptt hot....')
    rs = requests.session()
    res = rs.get(target_url, verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = ""
    for data in soup.select('div.container div.row div.desc_wrap h2 a'):
        title = data.text
        link = data['href']
        content += '{}\n{}\n\n'.format(title, link)
    return content

def yt():

    url = "https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ/featured?gl=TW#loc0=it"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
   
    content = ""
    ytlist= ""   

    all_mv = soup.select("h3.yt-lockup-title a[dir='ltr']")
    random.shuffle(all_mv)
    randomfivemv = all_mv[0:3]

    for data in randomfivemv:
        url="https://www.youtube.com{}".format(data.get("href"))
        title=format(data.get("title"))
        ytlist = 'YOUTUBE流行精選{}\n{}\n\n'.format(title, url)  
        content += ytlist
    return content
    
def yt_hot():
    
    url = "https://www.youtube.com/feed/trending?gl=TW#loc0=it"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
    
    content = ""
    ytlist = ""
    
    all_mv = soup.select("a[class='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ']")
    random.shuffle(all_mv)
    randomfivemv = all_mv[0:3]
    
    for data in randomfivemv:
        url="https://www.youtube.com{}".format(data.get("href"))
        title=format(data.get("title"))
        ytlist = 'YOUTUBE熱門影片{}\n{}\n\n'.format(title, url)  
        content += ytlist
    return content

def youtube_cnew():

    url = "https://www.youtube.com/playlist?list=PLsyOSbh5bs16vubvKePAQ1x3PhKavfBIl"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
   
    content = ""
    ytlist= ""

    all_mv = soup.select("a[class='pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link ']")
    random.shuffle(all_mv)
    randomfivemv = all_mv[0:3]

    for data in randomfivemv:
        url="https://www.youtube.com{}".format(data.get("href"))
        title=data.text.strip()
        ytlist = 'YOUTUBE最新華語精選\n{}\n{}\n\n'.format(title, url)  
        content += ytlist
    return content

def youtube_tnew():

    url = "https://www.youtube.com/playlist?list=PLsyOSbh5bs14fcCVYVMcnbiuhhaeF5LYl"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")
   
    content = ""
    ytlist= ""

    all_mv = soup.select("a[class='pl-video-title-link yt-uix-tile-link yt-uix-sessionlink spf-link ']")
    random.shuffle(all_mv)
    randomfivemv = all_mv[0:3]

    for data in randomfivemv:
        url="https://www.youtube.com{}".format(data.get("href"))
        title=data.text.strip()
        ytlist = 'YOUTUBE最新台語精選\n{}\n{}\n\n'.format(title, url)  
        content += ytlist
    return content

def youtube_search(res):

     url="https://www.youtube.com/results?search_query={}".format(res)
     request = requests.get(url)
     ytcontent = request.content
     soup = BeautifulSoup(ytcontent, "html.parser")
    
     content = ""

     all_mv = soup.select("a[class='yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link ']")
     mvlist = all_mv[0]

     url="https://www.youtube.com{}".format(mvlist.get("href"))
     title=mvlist.get("title")

     content='{}\n{}'.format(title,url)

     return content

def pick17sing():
    for i in range(10):
        songid  = "%08d" % random.randint(0,1e8)
        prefixlink  = 'http://17sing.tw/share_song/index.html?sid='
        link = prefixlink + songid
        
        oplink = urllib.request.urlopen(link)
        soup = BeautifulSoup(oplink, 'html.parser')
        songinfo = soup.find("meta",{"property":"og:description"})
        songcontext = songinfo.attrs["content"]
        if len(songcontext) > 0 :
            return link
        else:
            pass
    return "Try again!"

def sing17():

    for i in range(10):
        songid  = "%08d" % random.randint(0,1e8)
        url = 'http://17sing.tw/share_song/index.html?sid={}'.format(songid)
        request = requests.get(url)
        ycontent = request.content
        soup = BeautifulSoup(ycontent, 'html.parser')
        songimage = soup.find("meta",{"property":"og:image"})
        img  = songimage.attrs["content"]
        songurl = soup.find("meta",{"property":"og:url"})
        surl = songurl.attrs["content"]
        songtitl = soup.find("meta",{"property":"og:description"})
        titl = songtitl.attrs["content"][0:50]

        content = '{}\n{}...'.format(surl,titl)
        
        if len(img) > 0 :
            return content
        else:
            pass
    return "找不到歌 請再試一次!!"

def ask():
    url = "http://wisdomer2002.pixnet.net/blog/post/224560-%E5%AA%BD%E7%A5%96%E7%B1%A4%E8%A9%A960%E9%A6%96"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")

    content = ""

    alist = soup.select("div.article-content li a" )
    random.shuffle(alist)
    askdata = alist[0]

                                    
    url=askdata.get("href")
    text=askdata.get_text()

    content = '{}\n詳解:{}\n\n'.format(text,url)
    
    return content

def star(res):
    url = "http://www.daily-zodiac.com/mobile"
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")

    startlist = soup.select("li a")
    for data in startlist:
        if data.select('img')[0]['alt'] ==res:
            sdata = data
            sdata = 'http://www.daily-zodiac.com{}'.format(sdata.get("href"))
            content = starcontent(sdata)
            
    return content   

def starcontent(sdata):
    sdata_link = urllib.request.urlopen(sdata)
    soup_today = BeautifulSoup(sdata_link,'html.parser')
    souptoday_data = soup_today.select('ul.today')
    souptext_data = soup_today.select('article')
    #soup3_data = soup2.s
    for today_data in souptoday_data:
        today = today_data.get_text()
    for text_data in souptext_data:
        text = text_data.get_text().strip()
    content = '{}{}'.format(today,text)
    return content

def rate(res):

    url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
    dfs = pandas.read_html(url)
    currency = dfs[0]
    currency = currency.ix[:,0:3]
    currency.columns = [u'貨幣',u'匯率(賣)',u'匯率(買)']
    currency[u'貨幣'] = currency[u'貨幣'].str.split('\(',1).str[0]
    currency[u'貨幣'] = currency[u'貨幣'].str.split().str[0]
    #a = currency.values

    title = ""
    content = ""

    request = requests.get(url)
    soup = BeautifulSoup(request.content, "html.parser")

    datelist = soup.select('p.text-info')

    for data in datelist:
        ratedate = data.get_text().strip() 
 
    for a in currency.index:
        data = currency.ix[a,0]
        if data == res:
            title = currency.ix[a,0]
            rate =currency.ix[a,2]
            ratedata = '{} 1:{}'.format(title,rate)
          
    content = '臺灣銀行牌告匯率\n{}\n\n{}'.format(ratedate,ratedata)

    return content
     

def ratecount(res,nt,xt):
    
    url = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
    dfs = pandas.read_html(url)
    currency = dfs[0]
    currency = currency.ix[:,0:3]
    currency.columns = [u'貨幣',u'匯率(賣)',u'匯率(買)']
    currency[u'貨幣'] = currency[u'貨幣'].str.split('\(',1).str[0]
    currency[u'貨幣'] = currency[u'貨幣'].str.split().str[0]

    a = currency.values

    for a in currency.index:
        data = currency.ix[a,0]
        if data == res:
            title = currency.ix[a,0]
            rate =currency.ix[a,2]
            ratecountnt = round(int(nt)/float(rate),2)
            ratecountxt = round(int(xt)*float(rate))
            if int(nt)>1 and int(xt)==1:
                content = '臺灣銀行牌告匯率 {} 1:{}\n台幣 {} 可換得 {} {}'.format(title,rate,nt,ratecountnt,title)
                return content
            if int(nt)==1 and int(xt)>1:
                content = '臺灣銀行牌告匯率 {} 1:{}\n兌換 {} {} 需要 {} 台幣'.format(title,rate,xt,title,ratecountxt)
            else:
                content = "輸入金額有誤 NT換 幣名n10000x1  換回NT 幣名n1x10000"

    return content

def check_coffie():

    url = 'https://cafe.goodlife.tw/'
    request = requests.get(url)
    ycontent = request.content
    soup = BeautifulSoup(ycontent, 'html.parser')

    datalist = soup.select('div.item')

    content = ""
    store_list = datalist[0:10]
    
    for storedata in store_list:
        store = storedata.find('h3').text
        title_list = storedata.select('li a')
        title_data = check_coffie_content(store,title_list) 
        store_content = '<{}>\n{}\n'.format(store,title_data)
        content += store_content
        
    return content              

def check_coffie_content(store,title_list):

    title_content=""

    for data in title_list:
        if data.text.find(store) < 0:
            title = '{}\n'.format(data.text)
            title_content += title
       
    return title_content 

def goodlife(res):

    url = 'http://goodlife.tw/search?keyword={}'.format(res)
    request = requests.get(url)
    ycontent = request.content
    soup = BeautifulSoup(ycontent, 'html.parser')
    

    soup1 = soup.select('ul')

    content = ""
    span_data = ""
    
    for data in soup1[0:13]:
        if len(data.select('span[class="dis0 qualifier"]')) == 1:
            span = data.select('li.topic a')
            span_data = format(goodlife_data(span)).strip()
            content += '{}\n'.format(span_data)
            
    if len(content) ==0:
        return "查無優惠"

    return content.strip()

def goodlife_data(span):

    content = ""

    for data in span:
        if data.text.find('已過期')<0:
            a = data.text.strip()
            #title = '{}'.format(a)
            content += a
        else:
            pass
        return content

def weather(location):
    
    doc_name = "F-C0032-001"
    user_key = "CWB-A01FD046-AA6B-4C27-A307-616C33DB89B7"
    api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (doc_name,user_key)
   
    headers = {'Authorization': user_key}
    res = requests.get("http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?locationName=%s" % location,headers=headers)
    weather_api= res.json()

    weather_elements = weather_api['records']['location'][0]['weatherElement']
    

    sTs = (weather_elements[0]['time'])[0].get('startTime')[5:16]
    eTs = (weather_elements[0]['time'])[0].get('endTime')[5:16]
    Wxs = (weather_elements[0]['time'])[0]['parameter'].get('parameterName')
    PoPs = (weather_elements[1]['time'])[0]['parameter'].get('parameterName')
    MinTs = (weather_elements[2]['time'])[0]['parameter'].get('parameterName')
    MaxTs = (weather_elements[4]['time'])[0]['parameter'].get('parameterName')

    sTe = (weather_elements[0]['time'])[1].get('startTime')[5:16]
    eTe = (weather_elements[0]['time'])[1].get('endTime')[5:16]
    Wxe = (weather_elements[0]['time'])[1]['parameter'].get('parameterName')
    PoPe = (weather_elements[1]['time'])[1]['parameter'].get('parameterName')
    MinTe = (weather_elements[2]['time'])[1]['parameter'].get('parameterName')
    MaxTe = (weather_elements[4]['time'])[1]['parameter'].get('parameterName')

    if Wxs == Wxe:
        Wx = '{}'.format(Wxs)
    else:
        Wx = '{} 轉 {}'.format(Wxs,Wxe)

    if PoPs > PoPe:
        PoP = '降雨機率:{}%~{}%'.format(PoPe,PoPs)
    elif PoPs < PoPe:
        PoP = '降雨機率:{}%~{}%'.format(PoPs,PoPe)
    else:
        PoP = '降雨機率:{}%'.format(PoPs)

    if MinTs < MinTe:
        MinT = MinTs
    elif MinTs > MinTe:
        MinT = MinTe
    else:
        MinT = MinTs

    if MaxTs < MaxTe:
        MaxT = MaxTe
    elif MaxTs > MaxTe:
        MaxT = MaxTs
    else:
        MaxT = MaxTs
        

    #content1 = '{}\n時間:{}~{}\n天氣:{}\n溫度:{}C~{}C\n降雨機率:{}%'.format(location,sTs,eTs,Wxs,MinTs,MaxTs,PoPs)
    #content2 = '時間:{}~{}\n天氣:{}\n溫度:{}C~{}C\n降雨機率:{}%'.format(sTe,eTe,Wxe,MinTe,MaxTe,PoPe)

    _content3 = '{}\n{}\n溫度:{}C~{}C\n{}'.format(location,Wx,MinT,MaxT,PoP)

    #content = '{}\n\n{}'.format(content1,content2)
   
    return _content3

def sweather():

    res = requests.get("http://opendata.cwb.gov.tw/api/v1/rest/datastore/W-C0033-002?Authorization=CWB-A01FD046-AA6B-4C27-A307-616C33DB89B7")
    weather_api= res.json()

    content=""
    weather_info = weather_api['records']['record'][0]['datasetInfo']['datasetDescription']
    weather_data = weather_api['records']['record'][0]['contents']['content']['contentText'].strip()

    content='<{}>\n{}'.format(weather_info,weather_data)
       
    return content

def ty():

    src = 'http://www.cwb.gov.tw/V7/prevent/typhoon/Data/PTA_NEW/index.htm?dumm=Wed#'
    url = urllib.request.urlopen(src)
    soup = BeautifulSoup(url, 'html.parser')
    data = soup.select('div.patch')
    text = data[0].get_text().strip()
    imgsoure = soup.select('div.download a')

    imgurl = imgsoure[0].get('href')
    imglink = 'http://www.cwb.gov.tw/V7/prevent/typhoon/Data/PTA_NEW/{}'.format(imgurl)

    content = '{}\n{}'.format(text,imglink)

    return content

def gsheet():
    
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

def r18():

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

def getpoint():

    url = 'https://onelife.tw/%E9%9B%86%E9%BB%9E%E6%B4%BB%E5%8B%95'
    request = requests.get(url)
    ycontent = request.content
    soup = BeautifulSoup(ycontent, 'html.parser')

    datalist = soup.select('a[style="text-decoration:none;"]')

    content = ""

    for data in datalist:
        url = data.get('href')
        title = data.text
        text = '{}\nhttps://onelife.tw/{}\n'.format(title,url)
        content += text
    return content

def movie_search(res):

    url = 'https://tw.movies.yahoo.com/moviesearch_result.html?keyword={}'.format(res)
    request = requests.get(url)
    ycontent = request.content
    soup = BeautifulSoup(ycontent, 'html.parser')

    m_check = soup.select('div.release_movie_name a')
            

    if len(soup.select('div.errorbox_title')) ==1:
        return "查無結果"
    else:
        for i in range(0,len(m_check)):
            if m_check[i].text == res:
                movie_url =  m_check[i].get('href')
                break
            else:
                movie_url =  m_check[0].get('href')


    mrequest = requests.get(movie_url)
    mcontent = mrequest.content
    movie_soup = BeautifulSoup(mcontent,'html.parser')

    #電影名
    title_soup= movie_soup.select('div.movie_intro_info_r h1')
    for ndata in title_soup:
        title = ndata.text
 
    #期待度
    level_soup= movie_soup.select('div.circle_percent') 
    for ldata in level_soup:
        lv = ldata.get('data-percent')
    #滿意度
    score_soup= movie_soup.select('div[class="score_num count"]') 
    for sdata in score_soup:
        score = sdata.get('data-num')

    #簡介
    data_soup= movie_soup.select('div.gray_infobox_inner')
    for ddata in data_soup:
        data = ddata.text.strip()[0:120]

    #時刻表URL
    if len(movie_soup.select('ul[class="movie_tab_list"] a[class="gabtn"]')) < 4:
        time = "非上映中"
    else:
        if movie_soup.select('ul[class="movie_tab_list"] a[class="gabtn"]')[3].text != '時刻表':
            time = "非上映中"
        else:
            time_soup = movie_soup.select('ul[class="movie_tab_list"] a[class="gabtn"]')[3]
            for tdata in [time_soup]:
                time = tdata.get('href')


    content = '<{}>\n\n期待度:{}\n滿意度:{}\n*****\n{}...\n*****\n時刻表:{}'.format(title,lv,score,data,time)
    return content

def chdate(cyear,cmonth,cdate,chour):

    url = 'http://www.nongli.info/huangli/days/index.php?year={}&month={}&date={}'.format(cyear,cmonth,cdate)
    request = requests.get(url)
    soup = BeautifulSoup(request.content,"html.parser")

    dlist = soup.select('div[id="qna"] li')
    d0=dlist[0].text

    if len(d0)==3:
        content = "輸入格式錯誤"
        return(content)
    else:
        d0=dlist[0].text
        d1=dlist[1].text
        d2=dlist[2].text
        d5=dlist[5].text
        d6=dlist[6].text
        d10=dlist[10].text
        d11=dlist[11].text

        if int(chour) >= 0 and int(chour)<2:
            dh1 = dlist[12].text
            dh2 = dlist[13].text
            dh3 = dlist[14].text
        elif int(chour) >= 2 and int(chour)<3:
            dh1 = dlist[15].text
            dh2 = dlist[16].text
            dh3 = dlist[17].text
        elif int(chour) >= 3 and int(chour)<5:
            dh1 = dlist[18].text
            dh2 = dlist[19].text
            dh3 = dlist[20].text
        elif int(chour) >= 5 and int(chour)<7:
            dh1 = dlist[21].text
            dh2 = dlist[22].text
            dh3 = dlist[23].text
        elif int(chour) >= 7 and int(chour)<9:
            dh1 = dlist[24].text
            dh2 = dlist[25].text
            dh3 = dlist[26].text
        elif int(chour) >= 9 and int(chour)<11:
            dh1 = dlist[27].text
            dh2 = dlist[28].text
            dh3 = dlist[29].text
        elif int(chour) >= 11 and int(chour)<13:
            dh1 = dlist[30].text
            dh2 = dlist[31].text
            dh3 = dlist[32].text
        elif int(chour) >= 13 and int(chour)<15:
            dh1 = dlist[33].text
            dh2 = dlist[34].text
            dh3 = dlist[35].text
        elif int(chour) >= 15 and int(chour)<17:
            dh1 = dlist[36].text
            dh2 = dlist[37].text
            dh3 = dlist[38].text
        elif int(chour) >= 17 and int(chour)<19:
            dh1 = dlist[39].text
            dh2 = dlist[40].text
            dh3 = dlist[41].text
        elif int(chour) >= 19 and int(chour)<21:
            dh1 = dlist[42].text
            dh2 = dlist[43].text
            dh3 = dlist[44].text
        elif int(chour) >= 21 and int(chour)<23:
            dh1 = dlist[45].text
            dh2 = dlist[46].text
            dh3 = dlist[47].text
        elif int(chour) >= 23 and int(chour)<24:
            dh1 = dlist[48].text
            dh2 = dlist[49].text
            dh3 = dlist[50].text
        else:
            dh1 = dlist[12].text
            dh2 = dlist[13].text
            dh3 = dlist[14].text
        content = '{}\n{}\n{}\n{}\n{}\n{}\n{}\n\n{}\n{}\n{}'.format(d0,d1,d2,d5,d6,d10,d11,dh1,dh2,dh3)
        return(content)

def tomp3(res):

    source_url = res[res.find("http"):]    
    key = source_url.find("oksing.tw")

    if (key>0):
        sid = source_url.find("?sid")
        uid = source_url.find("&self")
        if (uid>0):
            sid_key = source_url[sid+5:uid]
        else:
            sid_key = source_url[sid+5:]
        
        json_url = 'http://act.oksing.tw/index.php?action=GetSongInfo&sid={}&callback=_jsoncallback'.format(sid_key)
    else:
        sid = source_url.find("?sid")
        uid = source_url.find("&self")
        if (uid>0):
            sid_key = source_url[sid+5:uid]
        else:
            sid_key = source_url[sid+5:]
        json_url = 'http://act.17sing.tw/index.php?action=GetSongInfo&sid={}&callback=_jsoncallback'.format(sid_key)

    request = requests.get(json_url)

    soup = request.text
    mp3_source = soup.replace("_jsoncallback","").replace("(",")").replace(")","")
    mp3_json = json.loads(mp3_source)
    mp3_get = mp3_json['response_data']['song']['path']
    #checkMV= mp3_source.find("mv_cover")
    if (mp3_source.find("mv_cover")>0):
        mp3_url = mp3_get.replace("mp3","mp4")
    else:
        mp3_url = mp3_get

    return mp3_url

#唱吧轉mp3
def changbamp3(res):
    
    source_url = res[res.find("http"):]

    request = requests.get(source_url)
    soup = BeautifulSoup(request.content, "html.parser")
    script = soup.find_all('script')
    #pattern = re.compile(r'mp3');', re.MULTILINE | re.DOTALL)
    mp3urlsearch = script[3].text
    
    for obj in script:
        if obj.text.find("mp3")>-1:
            mp3script = obj.text
##            print(mp3script) 
##            print(mp3script.find("http://qiniuuwmp3.changba.com"))
##            print(mp3script.find(".mp3"))
            if mp3script.find("http://qiniuuwmp3.changba.com") >-1:
                return mp3script[mp3script.find("http://qiniuuwmp3.changba.com"):mp3script.find(".mp3")+4]
            elif mp3script.find("http://lzscuw.changba.com") >-1:
                return mp3script[mp3script.find("http://lzscuw.changba.com"):mp3script.find(".mp3")+4]

def songsearch17(res):

    source_url = "http://ec2.kusoinlol.com/hsing/SongList.php"
    request = requests.post(source_url,res.encode("utf-8"))
    r = request.text
    table_content = r[r.find("table")-1:]

    tds=[]
    content = ""
    soup = BeautifulSoup(table_content,'html.parser')
    divs = soup.findAll("table")
    for div in divs:
        rows = div.findAll('tr')
        for row in rows:
            tds.append(row.findAll('td'))
            #if(row.text.find("試聽")>-1):
            #    content +=row.text

    list_content = ""
    content = ""
    
    for i in range(len(tds)):
        if i+1 < len(tds) and i<5 :
            who = tds[i+1][1].text
            song = tds[i+1][2].text
            link = tds[i+1][0].a['href']
            data = '{},{}\n{}\n'.format(who,song,link)
            list_content += data
        else:
            pass

    if (len(list_content)==0):
        content = '{}\n\n詳閱伴唱聯盟搜索引擎\n{}'.format("查不到伴奏","http://goo.gl/XXglcl")
    else:
        content = '{}\n詳閱伴唱聯盟搜索引擎\n{}'.format(list_content,"http://goo.gl/XXglcl")    
         
    return content

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
    
def pm25():

    url = 'http://opendata.epa.gov.tw/ws/Data/AQI/?$format=json'
    res=requests.get(url)
    soup = res.json()
    
    data = ""
    data2 = ""
    data3 = ""
    data4 = ""
    content=""


    for i in range(0,len(soup)-1):
        if soup[i].get('Status') in ['對敏感族群不健康']:
            dsoup = soup[i]
            County = pm25content(dsoup,data)
            if County != '':
                ldata = '{} '.format(County)
                data += ldata
            else:
                pass
        elif soup[i].get('Status') in ['對所有族群不健康']:
            dsoup = soup[i]
            County = pm25content(dsoup,data)
            if County != '':
                ldata2 = '{} '.format(County)
                data2 += ldata
            else:
                pass
        elif soup[i].get('Status') in ['非常不健康']:
            dsoup = soup[i]
            County = pm25content(dsoup,data)
            if County != '':
                ldata3 = '{} '.format(County)
                data3 += ldata
            else:
                pass
        elif soup[i].get('Status') in ['危害']:
            dsoup = soup[i]
            County = pm25content(dsoup,data)
            if County != '':
                ldat4 = '{} '.format(County)
                data4 += ldata
            else:
                pass
        else:
            pass

        
    content = '空氣品質危害地區\n****************\nLV1敏感警戒:{}\nLV2全民警戒:{}\nLV3非常不健康:{}\nLV4危害:{}'.format(data,data2,data3,data4)
    return (content)

def pm25content(dsoup,data):

    if dsoup['County'] in data:
        return ''
    else:
        return dsoup['County']
    #_data['城市']=dsoup[0]['County']
    #_data['觀測站']=dsoup.get('SiteName')
    #_data['AQI']=dsoup.get('AQI')
    #_data['PM2.5']=dsoup.get('PM2.5')
    #_data['空氣品質']=dsoup.get('Status')

def yelp(location):
    yelp_id = config['yelp api']['YELPCLIENT_ID']
    API_KEY = '_T1xjfZnjA3r5D_xh6VPzwcpwKwLQD-SewJKcwD5yr62u4Jv_hLLX8H88ZZn-5WScfTLRMY9td45_r1Dxet_wTRMpMPLX236xf8-jc0T_kUm3BZQQlAT7jf4mWssW3Yx'    
    #print(API_KEY)
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {
        'Authorization': 'Bearer %s' % API_KEY,
    }
    params = {'location': location.replace(' ', '+'),
              'term': 'Restaurant',
              'limit': 15,
              'radius': 1000
              }

    resp = requests.get(url=url, params=params, headers=headers)
    #print(headers)
    #print(resp.json())
    businesses = resp.json()['businesses']

    restaurants = []
    for business in businesses:
        restaurant = {}
        restaurant['name'] = business['name']
        restaurant['address'] = business['location']['display_address'][0]
        restaurant['photo'] = business['image_url']
        restaurant['yelp_url'] = business['url']
        restaurants.append(restaurant)
    return restaurants

def yelp_data(randomres,i):

    name = randomres[i]['name']
    address = randomres[i]['address']
    photo = randomres[i]['photo']
    yelp_url=randomres[i]['yelp_url']

    return {"title":name,"description":address,"urltoimage":photo,"url":yelp_url}

def photorace():

    url = 'http://www.uart.org.tw/uart/show/tourney/tourney106.html'
    request = requests.get(url)
    soup = BeautifulSoup(request.content,"html.parser")

    plist = soup.select('tr tr')[3:]
   
    content = ""  
    for i in range(len(plist)-1):
        res = plist[i]
        cdata = photoracedata(res)
        _content = '{}\n'.format(cdata)
        content += _content
    return(content)
    
def photoracedata(res):

    for data in [res]:
       title = ''.join(data.select('a')[0].text.split())
       link = data.select('a')[0]['href'].strip()
       date = data.select('td[align="center"]')[2].text.strip().replace(' ','')
       content = '{}\n屆止日:{}\nhttp://www.uart.org.tw/uart/show/tourney/{}'.format(title,date,link)
    return (content)

def lotto():

    source = ['http://www.pilio.idv.tw/lto/list.asp','http://www.pilio.idv.tw/ltobig/ServerA/list.asp']

    content_get = ""
    for i in source:
        url = i
    
        table = pandas.read_html(url)[3]
        a = table.iloc[1:6,0:3]

        request=requests.get(url)
        req = request.content
        soup = BeautifulSoup(req)

        _bonus = soup.select('span')[0].text

        name = _bonus[2:5]
        bonus_c = _bonus[18:]

        if int(bonus_c[0]) == 0:
            bonus = bonus_c[1:]
        else:
            bonus = bonus_c
        
        _date = a.iloc[0,0]
        date = '{}/{}'.format(_date[0:3],_date[4:])
        number1 = a.iloc[0,1]
        number2 = a.iloc[0,2]
    
        _content = '{} {}獎號\n{} [{}]\n累計獎金:{:,}\n\n'.format(date,name,number1,number2,int(bonus))

        content_get += _content

    _super_number_1 = random.sample(range(1,37),6)
    _super_number_1.sort()
    super_number_2 = random.randint(1,9)
    super_number_1 = format(_super_number_1).strip('[]')
    content_s = '下一期威力彩選號:\n{} [{}]'.format(super_number_1,super_number_2)

    _lotto_number = random.sample(range(1,50),7)
    _lotto_number_1=_lotto_number[0:6]
    _lotto_number_1.sort()
    lotto_number_2 = _lotto_number[6]
    lotto_number_1 = format(_lotto_number_1).strip('[]')
    content_l = '下一期大樂透選號:\n{} [{}]'.format(lotto_number_1,lotto_number_2)

    content_number = '小星星選號\n{}\n\n{}'.format(content_s,content_l)

    content = '{}\n{}'.format(content_get,content_number)
       
    return content

def stock(res):

    url = 'https://tw.stock.yahoo.com/'
    request = requests.get(url)
    ycontent = request.content
    soup = BeautifulSoup(ycontent, 'html.parser',from_encoding='cp950')

    if res=='亞股':
        skey = 'tbd tbd1'
    elif res == '歐股':
        skey = 'tbd tbd2'
    elif res == '美股':
        skey = 'tbd tbd3'
    else:
        skey = 'tbd tbd0'

    soupkey = 'div[id="ystkchatw"] div[class="{}"] tr'.format(skey)

    stocksoup = soup.select(soupkey)
    content = ""
    data = ""

    if res in ['亞股','歐股','美股']:
        si = int(len(stocksoup)-1)
    else:
        si = int(len(stocksoup))

    for i in range(si):
       stocki = stocksoup[i]
       a = stockdata(res,stocki)
       ta = '{}\n'.format(a)
       data += ta
    content = '{}當日行情\n{}'.format(res,data)
    return (content)
         
def stockdata(res,stocki):
    data = stocki.text
    c = data.find('.',data.find('.')+1)
    title = data[0:data.find('.')+3]
    ud = data[data.find('.')+3:data.find('.',data.find('.')+1)+3]
    op = data[data.find('.',data.find('.')+1)+3:]
    content = ""
    if res in ['亞股','歐股','美股']:
        content = '{} {}'.format(title,ud)
    else:
        content = '{} {}\n成交金額{}\n'.format(title,ud,op)
    return content

def stocks(res):

    if res in twstock.codes:
        content = ""
        stockh = twstock.Stock(res)
        bfp = twstock.BestFourPoint(stockh)
        note = bfp.best_four_point()
        hprice = stockh.price
        bprice = (hprice[len(hprice)-1])
    
        stock = twstock.realtime.get(res)
        code = stock['info']['code']
        name = stock['info']['name']
        timef = stock['info']['time']
        time = timef.replace(timef[timef.find(":")-2:timef.find(":")],str(int(timef[timef.find(":")-2:timef.find(":")])+8))
        realtime = stock['realtime']['latest_trade_price']
        sopen = stock['realtime']['open']
        shigh = stock['realtime']['high']
        slow = stock['realtime']['low']
        best_bid_volume = stock['realtime']['best_bid_volume']
        best_ask_volume = stock['realtime']['best_ask_volume']
        udp = '%.2f%%' % ((float(realtime)-float(bprice))/float(bprice)*100)
        ma_p5 = stockh.moving_average(stockh.price, 5)[len(stockh.price)-5]
        br_p5 = '%.2f%%' % ((float(realtime)-float(ma_p5))/float(ma_p5)*100)
        ma_p10 = stockh.moving_average(stockh.price, 10)[len(stockh.price)-10]
        br_p10 = '%.2f%%' % ((float(realtime)-float(ma_p10))/float(ma_p10)*100)
        if time[len(time)-8:] == "14:30:00":
            content = '股號:{} {}\n資料時間:{}\n本日收盤價:{}\n漲跌:{}\n前日收盤:{}\n今日開盤:{}\n最高:{}\n最低:{}\n委買:{}\n委賣:{}\n五日線:{} 十日線:{}\nBIAS5:{} BISA10:{}\nNote:{}'.format(code,name,time,realtime,udp,bprice,sopen,shigh,slow,best_bid_volume,best_ask_volume,ma_p5,ma_p10,br_p5,br_p10,note)
        else:
            content = '股號:{} {}\n資料時間:{}\n即時行情:{}\n漲跌:{}\n前日收盤:{}\n今日開盤:{}\n最高:{}\n最低:{}\n委買:{}\n委賣:{}\n五日線:{} 十日線:{}\nBIAS5:{} BISA10:{}\nNote:{}'.format(code,name,time,realtime,udp,bprice,sopen,shigh,slow,best_bid_volume,best_ask_volume,ma_p5,ma_p10,br_p5,br_p10,note)
    else:
        content = "沒有此股號"
    
    return content

def stockcode(cres):
      
    url = 'http://www.twse.com.tw/zh/stockSearch/stockSearch'
    post_params = {'stkNo': cres}
    post_args = urllib.parse.urlencode(post_params).encode("utf-8")
    fp = urllib.request.urlopen(url,post_args)
    soup = BeautifulSoup(fp)
    
    urls = 'http://www.tpex.org.tw/web/regular_emerging/corporateInfo/regular/regular_stock_detail.php?l=zh-tw&stk_code={}'.format(cres)
    request = requests.get(urls)
    sp = request.content
    soups = BeautifulSoup(sp)
    sdata = soups.select('td[class="page-table-body-right"] a[class="page-text-over"]')
    
    check = soup.select('div.body article')
    check_data = check[0].text
    data = soup.select('div.body article td a')
    
    if len(check_data) == 4:
        if len(sdata) == 0:
            content = "查無此股號"
            return content
        else:    
            scontent = sdata[0].get('href')
            res = scontent[77:]
            content = stocks(res)
            return content
    else:
        rdata = data[0].text
        res = rdata[0:rdata.find(cres)]
        content = stocks(res)
        return content

def tk(a):
    # 获取google翻译内容的tk值
    # a：要翻译的内容，以字符串指定
    # 注意：要翻译的内容只能是英文，即只能是包含ASCII码的英文字符串
    #;TKK=eval('((function(){var a\x3d1003361859;var b\x3d975588639;return 420060+\x27.\x27+(a+b)})())')
    TKK = (lambda a=561666268, b=1526272306:str(406398) + '.' + str(a + b))()
    
    def b(a, b):
        for d in range(0, len(b)-2, 3):
            c = b[d + 2]
            c = ord(c[0]) - 87 if 'a' <= c else int(c)
            c = a >> c if '+' == b[d + 1] else a << c
            a = a + c & 4294967295 if '+' == b[d] else a ^ c
        return a
    
    e = TKK.split('.')
    h = int(e[0]) or 0
    g = []
    d = 0
    f = 0
    while f < len(a):
        c = ord(a[f])
        if 128 > c:        
            g.insert(d,c)
            d += 1
        else:
            if 2048 > c:
                g[d] = c >> 6 | 192
                d += 1
            else:
                if (55296 == (c & 64512)) and (f + 1 < len(a)) and (56320 == (ord(a[f+1]) & 64512)):
                    f += 1
                    c = 65536 + ((c & 1023) << 10) + (ord(a[f]) & 1023)
                    g[d] = c >> 18 | 240
                    d += 1
                    g[d] = c >> 12 & 63 | 128
                    d += 1
                else:
                    g[d] = c >> 12 | 224
                    d += 1
                    g[d] = c >> 6 & 63 | 128
                    d += 1
                g[d] = c & 63 | 128
                d += 1
        f += 1
    a = h
    for d in range(len(g)):
        a += g[d]
        a = b(a, '+-a^+6')
    a = b(a, '+-3^+b+-f')
    a ^= int(e[1]) or 0
    if 0 > a:a = (a & 2147483647) + 2147483648
    a %= 1E6
    return str(int(a)) + '.' + str(int(a) ^ h)


def translate(res): 

    if len(res) > 4891:
        return "翻譯內容長度超過限制"
    else:
        words = res.replace(' ','%20')
        a=res
        atk = tk(a)
        url ='https://translate.google.cn/translate_a/single?client=t&'\
             'text =sl=en&tl=zh-TW&hl=zh-TW&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&'\
             'dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=1&tk={}&q={}'.format(atk,words)
    
        hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  
        response = requests.get(url)
        json_data = response.text
        data = json.loads(json_data)

        content = data[0][0][0]
        return content
    
def mojim(res):

    _url = "https://mojim.com"
    url = "{}/{}.html?t4".format(_url,res)
    request = requests.get(url)
    ytcontent = request.content
    soup = BeautifulSoup(ytcontent, "html.parser")

    _check = soup.select("title")
    check = _check[0].text.find("請重新輸入")
    

    if (int(check) < 0):
        s_list = soup.select("span[class='mxsh_ss3']")
        for data in s_list[1]:
            curl = "{}{}".format(_url,data.get("href"))
            
        trequest = requests.get(curl)
        tytcontent = trequest.content
        tsoup = BeautifulSoup(tytcontent, "html.parser")
        
        t_list = tsoup.select("title")
        tcontent = t_list[0].text
        p = tcontent.find("歌詞")
        p2 = tcontent.find("※")

        title = tcontent[0:int(p)]
        singer = tcontent[int(p)+3:int(p2)]
        content = "資料來源-魔鏡歌詞網\n------\n{}-{}\n{}\n------".format(singer,title,curl)
    else:
        content = "沒有符合的歌詞請重新輸入，可利紅豆 王菲或紅豆+王菲的方式來查找"

    return content
       
def fwords(resf):
    words = resf
    print(words)
    olist = (["幹","操","靠"])
    wlist = (["三小","靠北","馬的","媽的","放屁","屁啦","狗屁","爆料","八卦","三字經","幹你娘","壞掉了","小星星"])
    #rlist = (["美金","港幣","英鎊","澳幣","加拿大幣","新加坡幣","瑞士法郎","日圓","日幣","南非幣","瑞典幣",\
    #         "紐元","泰幣","菲國比索","印尼幣","歐元","韓元","越南盾","馬來幣","人民幣"])
    ylist = (["聽歌","找歌"])
    tlist = (['翻譯'])
    glist = (['查優惠'])
    mlist = (['看電影'])
    dlist = (['time','Time'])
    slist = (['抽歡歌'])
    sdlist = (['查歌詞'])
    if words.find('n')>=2:
        res = words[0:words.find('n')].replace('日幣','日圓')
        nt = words[words.find('n')+1:words.find('x')]
        xt = words[words.find('x')+1:]
        content = ratecount(res,nt,xt)
        return content
    elif words[0:2] in ylist:
        res = words[2:]
        content = youtube_search(res)
        return content
    elif words[0:2] in tlist:
        res = words[2:]
        content = translate(res)
        return content
    elif words[0:3] in glist:
        res = words[3:]
        content = goodlife(res)
        return content
    elif words[0:3] in mlist:
        res = words[3:]
        content = movie_search(res)
        return content
    elif words[0:3] in sdlist:
        res = words[3:]
        content = mojim(res)
        return content
    elif words[0:3] in slist:
        if str(words[3:].isnumeric())=="False":
            content = "UID error"
            return content
        else:
            if len(words[3:])>8 or len(words[3:])<6:
                content = "UID error"
                return content
            else:
                res = words[3:]
                content = s17uid(res)
                #print (content)
                return content
    elif words[0:4] in dlist:
        if len(words[0:])>4:
            if str(words[4:].isnumeric())=="False":
                content = "date type error: 20170101 or 2017010113"
                return content
            else:
                if len(words[4:])<7 or len(words[4:])>10:
                    content = "輸入格式錯誤"
                    return content
                else:
                    cyear = (words[4:8])
                    cmonth = (words[8:10])
                    cdate = (words[10:12])
                    if len(words[4:])==10:
                        chour = (words[12:14])
                    else:
                        chour = '00'
                    content = chdate(cyear,cmonth,cdate,chour)
                    return content
        else:
            ctime = datetime.now()+timedelta(hours=8)
            cyear = ctime.strftime("%Y")
            cmonth = ctime.strftime("%m")
            cdate = ctime.strftime("%d")
            chour = ctime.strftime("%H")
            content = chdate(cyear,cmonth,cdate,chour)
            return content
    elif words[0] in olist:
        messages_talk = words[0]
        content = star_talk(messages_talk)
        return content
    elif len(words) >=2:
        for data in wlist:
            if words.find(data)>-1:
                return (star_talk(words))
        #for data in rlist:
        #    if words.find(data)>-1:
        #        return rate(data.replace('日幣','日圓'))

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event",event)
    print("event.groupID:",event.source)
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)

    grouplist = str(event.source)
    mlist = event.message.text
    words = event.message.text
#    profile = line_bot_api.get_profile(event.source.user_id)
    #gprofile = line_bot_api.get_profile(event.source.group_id)

    if event.message.text == "eyny":
        content = eyny_movie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "蘋果新聞":
        content = apple_news()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "PTT表特":
        content = ptt_beauty()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "抽金句":
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('6FM69')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "比大小":
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('KQjab')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text in ["說笑話","講笑話","小星星說笑話","小星星講笑話"]:
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('XpG2g')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "抽單身":
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('Sy6Gm')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "抽鮮肉":
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('9eQni')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        content = "想秀自已嗎 歡迎把照片分享到小星星粉絲團哦"
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=content)])
        return 0
    if event.message.text == "抽正妹":
        image = requests.get(API_Get_Image)
        url = image.json().get('Url')
        content = "想秀自已嗎 歡迎把照片分享小星星粉絲團哦"
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=content)])
        return 0
    if event.message.text in ["抽","來點正能量"]:
        
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('9eQni')
        index = random.randint(0, len(images) - 1)
        urlb = images[index].link
        
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('23p2B')
        index = random.randint(0, len(images) - 1)
        urlgv = images[index].link
        
        imageg = requests.get(API_Get_Image)
        urlg = imageg.json().get('Url')

        url = random.choice([urlg,urlb,urlg,urlb,urlg,urlg,urlg,urlgv])
        
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "PTTHOT":
        content = ptt_hot()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "即時廢文":
        content = ptt_gossiping()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "PTT笨版":
        content = ptt_Stupid()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "看電影":
        content = movie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "本週上映":
        content = movie_new()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "科技新報":
        content = technews()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "PanX泛科技":
        content = panx()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "聽歌":
        content = yt()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "youtube熱門":
        content = yt_hot()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "聽歌華語":
        content = youtube_cnew()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "聽歌台語":
        content = youtube_tnew()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "抽籤":
        content = ask()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "現在吃什麼":
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('9rYK8')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        return 0
    if event.message.text == "抽歡歌":
        content = sing17()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "拉霸":
        content = gsheet()
        if content == 'winner':
            url = 'https://imgur.com/eYrlcRb.jpg'
            image_message=ImageSendMessage(
               original_content_url=url,
               preview_image_url=url
            )
            line_bot_api.reply_message(event.reply_token, image_message)
            return 0
        else:        
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
            return 0
    if event.message.text == "18r" or event.message.text == "18啦":
        content = r18()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "查集點":
        content = getpoint()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "查咖啡":
        content = check_coffie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text in ["查PM2.5","查空氣品質","查pm2.5"]:
        content = pm25()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "天氣特報":
        content = sweather()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "查攝影比賽":
        content = photorace()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "checkid":
        content = getid(profile)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == 'Getid':
        if isinstance(event.source, SourceUser):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(
                        text='Display name: ' + profile.display_name
                    ),
                    TextSendMessage(
                        text='User_Id: ' + profile.user_id
                    )
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextMessage(text="Bot can't use profile API without user ID"))
    if event.message.text == 'Getgid':
        content = grouplist
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == '群發新聞':
        content = apple_news()
        line_bot_api.push_message(
            'U9f2c61013256dfe556d70192388e4c7c',
            TextSendMessage(text=content))
        return 0
    if event.message.text == "一閃一閃亮晶晶":
        buttons_template = TemplateSendMessage(
            alt_text='開始玩 template',
            template=ButtonsTemplate(
                title='歡迎使用小星星',
                text='請選擇使用功能',
                thumbnail_image_url='https://imgur.com/j5pDXdG.jpg',
                actions=[
                    MessageTemplateAction(
                        label='生活相關',
                        text='生活'
                    ),
                    MessageTemplateAction(
                        label='休閒影音',
                        text='休閒影音'
                    ),
                    MessageTemplateAction(
                        label='抽一下',
                        text='抽一下'
                    ),
                    MessageTemplateAction(
                        label='功能說明',
                        text='功能說明'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "生活":
        buttons_template = TemplateSendMessage(
            alt_text='開始玩 template',
            template=ButtonsTemplate(
                title='生活功能',
                text='請選擇使用功能',
                thumbnail_image_url='https://imgur.com/oHli0XL.jpg',
                actions=[
                    MessageTemplateAction(
                        label='新聞',
                        text='新聞'
                    ),
                    MessageTemplateAction(
                        label='匯率查詢',
                        text='請輸入查詢幣別 例如:美金、日圓、人民幣 若要查詢換匯 1.新台幣1000換幣  美金n1000x1  2.查換1000日圓要多少台幣 日圓n1x1000 '
                    ),
                    MessageTemplateAction(
                        label='PTT看版',
                        text='PTT看版'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "新聞":
        buttons_template = TemplateSendMessage(
            alt_text='新聞 template',
            template=ButtonsTemplate(
                title='新聞類型',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/vkqbLnz.png',
                actions=[
                    MessageTemplateAction(
                        label='蘋果即時新聞',
                        text='蘋果新聞'
                    ),
                    MessageTemplateAction(
                        label='科技新報',
                        text='科技新報'
                    ),
                    MessageTemplateAction(
                        label='PanX泛科技',
                        text='PanX泛科技'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "休閒影音":
        buttons_template = TemplateSendMessage(
            alt_text='休閒影音 template',
            template=ButtonsTemplate(
                title='服務類型',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/sbOTJt4.png',
                actions=[
                    MessageTemplateAction(
                        label='電影',
                        text='電影'
                    ),
                    MessageTemplateAction(
                        label='Youtube',
                        text='Youtube'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "電影":
        buttons_template = TemplateSendMessage(
            alt_text='電影 template',
            template=ButtonsTemplate(
                title='服務類型',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/sbOTJt4.png',
                actions=[
                    MessageTemplateAction(
                        label='院線電影精選',
                        text='看電影'
                    ),
                    MessageTemplateAction(
                        label='本週上映電影精選',
                        text='本週上映'
                    ),
                    MessageTemplateAction(
                        label='eyny',
                        text='eyny'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "Youtube":
        buttons_template = TemplateSendMessage(
            alt_text='Youtube template',
            template=ButtonsTemplate(
                title='服務類型',
                text='請選擇',
                thumbnail_image_url='https://imgur.com/OYR2ciy.jpg',
                actions=[
                    MessageTemplateAction(
                        label='youtube隨選流行音樂',
                        text='聽歌'
                    ),
                    MessageTemplateAction(
                        label='youtube隨選熱門影片',
                        text='youtube熱門'
                    ),
                    MessageTemplateAction(
                        label='歡歌隨選歌曲',
                        text='抽歡歌'
                    )
                ]
            )
        )

        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "PTT看版":
        buttons_template = TemplateSendMessage(
            alt_text='PTT看版 template',
            template=ButtonsTemplate(
                title='看PPT長智識',
                text='請選擇',
                thumbnail_image_url='https://imgur.com/prkXPHI.jpg',
                actions=[
                    MessageTemplateAction(
                        label='PTT熱門文章',
                        text='PTTHOT'
                    ),
                    MessageTemplateAction(
                        label='即時廢文',
                        text='即時廢文'
                    ),
                     MessageTemplateAction(
                        label='熱門笨文',
                        text='PTT笨版'
                    ) 
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "抽一下":
        buttons_template = TemplateSendMessage(
            alt_text='抽一下 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qKkE2bj.jpg',
                actions=[
                     MessageTemplateAction(
                        label='養眼一下',
                        text='養眼一下'
                    ),
                     MessageTemplateAction(
                        label='星座求籤',
                        text='星座求籤'
                    ),
                     MessageTemplateAction(
                        label='現在吃什麼',
                        text='現在吃什麼'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "養眼一下":
        buttons_template = TemplateSendMessage(
            alt_text='養眼一下 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qKkE2bj.jpg',
                actions=[
                     MessageTemplateAction(
                        label='隨便來張鮮肉或正妹圖片',
                        text='抽'
                    ),
                     MessageTemplateAction(
                        label='隨便來張鮮肉圖片',
                        text='抽鮮肉'
                    ),
                    MessageTemplateAction(
                        label='隨便來張正妹圖片',
                        text='抽正妹'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "星座求籤":
        buttons_template = TemplateSendMessage(
            alt_text='星座求籤 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://imgur.com/aLJkS5G.jpg',
                actions=[
                     MessageTemplateAction(
                        label='每日星座運勢',
                        text='請輸入星座名稱 例如金牛座、天秤座'
                    ),
                     MessageTemplateAction(
                        label='媽祖六十籤',
                        text='抽籤'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "功能說明":
        buttons_template = TemplateSendMessage(
            alt_text='開始玩 template',
            template=ButtonsTemplate(
                title='歡迎使用小星星',
                text='請選擇使用功能',
                thumbnail_image_url='https://imgur.com/j5pDXdG.jpg',
                actions=[
                    MessageTemplateAction(
                        label='功能說明',
                        text='詳見小星星粉絲頁'
                    ),
                    MessageTemplateAction(
                        label='小星星粉絲頁',
                        text='https://www.facebook.com/%E5%B0%8F%E6%98%9F%E6%98%9F-138369020128285/'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text in ['!help','功能表']:
        res = event.message.text
        content = shelp()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == '小星星粉絲頁':
        res = event.message.text
        content = 'https://www.facebook.com/%E5%B0%8F%E6%98%9F%E6%98%9F-138369020128285/'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0  
    if event.message.text=='查颱風':
        res = event.message.text
        content = ty()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0   
    if event.message.text in ['查樂透','抽樂透']:
        res = event.message.text
        content = lotto()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if (mlist.find('17sing')>-1 or mlist.find('oksing')>-1):
        res = event.message.text
        content = tomp3(res)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if mlist.find('changba')>-1:
        res = event.message.text
        content = changbamp3(res)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if mlist[mlist.find('查天氣',0):3]=='查天氣':
        location = mlist[mlist.find('查天氣',0)+3:6].replace('台','臺')
        content = weather(location)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0    
    if mlist[mlist.find('查股市',0):3]=='查股市':
        res = mlist[mlist.find('查股市',0)+3:5]
        content = stock(res)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if mlist[mlist.find('查股票',0):3]=='查股票':
        res = mlist[mlist.find('查股票',0)+3:]
        if res >= '\u0030' and res <='\u0039':
            content = stocks(res)
        else:
            cres = res
            content = stockcode(cres)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0 
    if mlist[mlist.find('查伴奏',0):3]=='查伴奏':
        res = mlist[mlist.find('查伴奏',0)+3:]
        content = songsearch17(res)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if mlist[mlist.find('歡歌',0):2]=='歡歌':
        if mlist.find(':')<0:
            content = s17uidrandom(mlist)
        else:
            content = s17uidsong(mlist)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text in [ "牡羊座","金牛座","雙子座","巨蟹座","獅子座","處女座","天秤座","天蠍座","射手座","魔羯座","水瓶座","雙魚座"]:
        res = event.message.text
        content = star(res)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    #查塔羅牌說明
    if re.search("查(塔羅牌|塔羅|tarot)說明(\d+)",event.message.text):
        tarot_content = tarot_detail(int(re.search("查(塔羅牌|塔羅|tarot)說明(\d+)",event.message.text).group(2)))
        url = tarot_content[4]
        content = '{}\n\n{}\{}'.format(tarot_content[1],tarot_content[2],tarot_content[3])
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, [image_message, TextSendMessage(text=content)])
        return 0
    #抽塔羅牌
    if re.search("抽[塔羅牌|塔羅|tarot]",event.message.text):
        if re.search("3|三[張]|三角",event.message.text):
            tarot_content = tarot_random_get(3)
            carousel_template_message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[0][4],
                            title="過去/自已/靈魂/上司",
                            text=tarot_content[0][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text= '{}{}'.format("查塔羅牌說明",tarot_content[0][0])
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[1][4],
                            title="現在/關係/心理/自已",
                            text=tarot_content[1][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text='{}{}'.format("查塔羅牌說明",tarot_content[1][0])
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[2][4],
                            title="未來/對方/身體/屬下",
                            text=tarot_content[2][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text='{}{}'.format("查塔羅牌說明",tarot_content[2][0])
                                )
                            ]
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,carousel_template_message)
        elif re.search("5|五[張]",event.message.text):
            tarot_content = tarot_random_get(5)
            carousel_template_message = TemplateSendMessage(
                alt_text='Carousel template',
                template=CarouselTemplate(
                    columns=[
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[0][4],
                            title="過去",
                            text=tarot_content[0][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text= '{}{}'.format("查塔羅牌說明",tarot_content[0][0])
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[1][4],
                            title="現在",
                            text=tarot_content[1][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text='{}{}'.format("查塔羅牌說明",tarot_content[1][0])
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[2][4],
                            title="未來",
                            text=tarot_content[2][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text='{}{}'.format("查塔羅牌說明",tarot_content[2][0])
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[3][4],
                            title="忠告",
                            text=tarot_content[3][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text='{}{}'.format("查塔羅牌說明",tarot_content[3][0])
                                )
                            ]
                        ),
                        CarouselColumn(
                            thumbnail_image_url=tarot_content[4][4],
                            title="可能結果",
                            text=tarot_content[4][1],
                            actions=[
                                MessageTemplateAction(
                                    label='牌義說明',
                                    text='{}{}'.format("查塔羅牌說明",tarot_content[4][0])
                                )
                            ]
                        )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token,carousel_template_message)
        else:
            tarot_content = tarot_random()
            url = tarot_content[4]
            content = '{}\n\n{}\{}'.format(tarot_content[1],tarot_content[2],tarot_content[3])
            image_message = ImageSendMessage(
                original_content_url=url,
                preview_image_url=url
            )
            line_bot_api.reply_message(
                event.reply_token, [image_message, TextSendMessage(text=content)])
        return 0
    #匯率
    rate_list = "美金|港幣|英鎊|澳幣|加拿大幣|新加坡幣|瑞士法郎|日圓|日幣|南非幣|瑞典幣|紐元|泰幣|菲國比索|印尼幣|歐元|韓元|越南盾|馬來幣|人民幣"
    if re.search(rate_list,event.message.text):
        res = re.search(rate_list,event.message.text).group(0).replace('日幣','日圓')
        content = rate(res)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0
    if len(words)>=1:
        resf = words
        content = fwords(resf)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0    

@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    
    #profile = line_bot_api.get_profile(event.source.user_id)
    #gprofile = line_bot_api.get_profile(event.source.group_id)
    
    
    token = event.reply_token
    location = event.message.address
    print(location)
    _columns=[]
    res = yelp(location)
    random.shuffle(res)
    randomres=res[0:5]
    for i in range(5):
        data = yelp_data(randomres,i)
        title = data["title"]
        description = data["description"]
        urltoimage=data["urltoimage"]
        url=data["url"]
        _columns[len(_columns):] = [
        {
            "thumbnailImageUrl":urltoimage,
            "title":title,
            "text":description,
            "label":"View detail",
            "uri":url
        } 
        ]
    carousel_template_message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=_columns[0]["thumbnailImageUrl"],
                    title=_columns[0]["title"],
                    text=_columns[0]["text"],
                    actions=[
                        URITemplateAction(
                            label='View detail',
                            uri=_columns[0]["uri"]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=_columns[1]["thumbnailImageUrl"],
                    title=_columns[1]["title"],
                    text=_columns[1]["text"],
                    actions=[
                        URITemplateAction(
                            label='View detail',
                            uri=_columns[1]["uri"]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=_columns[2]["thumbnailImageUrl"],
                    title=_columns[2]["title"],
                    text=_columns[2]["text"],
                    actions=[
                        URITemplateAction(
                            label='View detail',
                            uri=_columns[2]["uri"]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=_columns[3]["thumbnailImageUrl"],
                    title=_columns[3]["title"],
                    text=_columns[3]["text"],
                    actions=[
                        URITemplateAction(
                            label='View detail',
                            uri=_columns[3]["uri"]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=_columns[4]["thumbnailImageUrl"],
                    title=_columns[4]["title"],
                    text=_columns[4]["text"],
                    actions=[
                        URITemplateAction(
                            label='View detail',
                            uri=_columns[4]["uri"]
                        )
                    ]
                ) 
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,carousel_template_message)
    return 0 
       
if __name__ == '__main__':
    app.run()

