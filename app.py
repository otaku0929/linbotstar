import requests
import re
import random
import configparser
import urllib.request
import pandas
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient
from selenium import webdriver

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

def weather(location):
    
    doc_name = "F-C0032-001"
    user_key = "CWB-A01FD046-AA6B-4C27-A307-616C33DB89B7"
    api_link = "http://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (doc_name,user_key)
   
    headers = {'Authorization': user_key}
    res = requests.get("http://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?locationName=%s" % location,headers=headers)
    weather_api= res.json()

    weather_elements = weather_api['records']['location'][0]['weatherElement']

    Wx = (weather_elements[0]['time'])[0]['parameter'].get('parameterName')
    PoP = (weather_elements[1]['time'])[0]['parameter'].get('parameterName')
    MinT = (weather_elements[2]['time'])[0]['parameter'].get('parameterName')
    MaxT = (weather_elements[4]['time'])[0]['parameter'].get('parameterName')

    content = '{}\n天氣:{}\n溫度:{}C~{}C\n降雨機率:{}%'.format(location,Wx,MinT,MaxT,PoP)
    
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

def fwords(resf):
    words = resf
    olist = (["幹","操","靠"])
    wlist = (["三小","靠北","馬的","媽的", "放屁","美金","港幣","英鎊","澳幣","加拿大幣","新加坡幣","瑞士法郎","日圓","日幣","南非幣","瑞典幣","紐元","泰幣","菲國比索","印尼幣","歐元","韓元","越南盾","馬來幣","人民幣"])
    ylist = (["聽歌","找歌","查歌"])
    if words.find('n')>=2:
        res = words[0:words.find('n')].replace('日幣','日圓')
        nt = words[words.find('n')+1:words.find('x')]
        xt = words[words.find('x')+1:]
        content = ratecount(res,nt,xt)
        return content
    elif words[0:2] in ylist:
        res = words[3:]
        content = yourube_search(res)
        return content
    elif words[0] in olist:
        messages_talk = words[0]
        content = talk_messages(messages_talk)
        return content
    elif len(words) >=2:
        for data in wlist:
            if words[words.find(data,0):words.find(data,0)+len(data)] in wlist:
                m2list = words[words.find(data,0):words.find(data,0)+len(data)]
                messages_talk = m2list
                content = talk_messages(messages_talk)
                return content

def talk_messages(messages_talk):

    if messages_talk in {'幹','操'}:
        content = random.choice(['喵喵~','汪汪~','咩~','啊嘶~','噓~好孩子不說這個','講~f~u~c~k~才有英特內訊NO','十十人一十','操你媽好嗎~幹我媽很好'])
        return content
    if messages_talk == '三小':
        content = random.choice(['我聽過小王、小強、就是沒聽過三小','小小小', '大大大','小三小四小五','意義是三小 我只知道義氣','你是魯小小'])
        return content
    if messages_talk in {'靠北',"靠"}:
        content = random.choice(['靠北邊走','靠南', '我靠爸族啦','我有的靠你有嗎','喂喂別靠來靠去','走路要靠右邊走'])
        return content
    if messages_talk in {'馬的','媽的'}:
        content = random.choice(['馬兒跑~馬兒跳~馬兒咩咩叫~','一馬當先、馬到成功、馬耳東風、馬的成語還有很多哦~','媽媽的孩子都是寶','你8+9哦','羊的~雞的~狗的~'])
        return content
    if messages_talk in {'放屁'}:
        content = random.choice(['噗~~~~~~是誰','Lucky~Lucky~Lucky~你再躱在桌子底下會臭死','好臭~~~','快大口吸掉'])
        return content    
    if messages_talk in [ "美金","港幣","英鎊","澳幣","加拿大幣","新加坡幣","瑞士法郎","日圓","日幣","南非幣","瑞典幣","紐元","泰幣","菲國比索","印尼幣","歐元","韓元","越南盾","馬來幣","人民幣"]:
        res = messages_talk.replace('日幣','日圓')
        content = rate(res)
        return content

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    
    mlist = event.message.text
    words = event.message.text

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
    if event.message.text == "抽鮮肉":
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('9eQni')
        index = random.randint(0, len(images) - 1)
        url = images[index].link
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "抽正妹":
        image = requests.get(API_Get_Image)
        url = image.json().get('Url')
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "抽":
        
        client = ImgurClient('33ed33e765afedc', '04f0d5531b1d0978ff97fd990554c899e9e7e1f5')
        images = client.get_album_images('9eQni')
        index = random.randint(0, len(images) - 1)
        urlb = images[index].link
        
        imageg = requests.get(API_Get_Image)
        urlg = imageg.json().get('Url')
        
        url = random.choice([urlg,urlb,urlg,urlb,urlg,urlg])
        
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
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "抽歡歌":
        content = pick17sing()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "拉霸":
        content = gsheet()
        if content == 'winner':
            url = 'https://imgur.com/eYrlcRb.jpg'
            image_messages=ImageSendMessage(
               original_content_url=url,
               preview_image_url=url
            )
            line_bot_api.reply_message(event.reply_token, image_message)
            return 0
        else:        
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
            return 0
    if event.message.text == "get17":
        url = pick17sing()
        img = 'http://17sing.tw/img/song/icon_nosong.jpg'
        image_message=ImageSendMessage(
            original_content_url=url,
            preview_image_url=img
        )
        line_bot_api.reply_message(event.reply_token,image_message)
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
    
    if event.message.text=='查颱風':
        res = event.message.text
        content = ty()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0   
    
    if mlist[mlist.find('查天氣',0):3]=='查天氣':
        location = mlist[mlist.find('查天氣',0)+3:6].replace('台','臺')
        content = weather(location)
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
    
    if len(words)>=1:
        resf = words
        content = fwords(resf)
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))
        return 0    

if __name__ == '__main__':
    app.run()

