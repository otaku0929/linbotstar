def shelp():

    helplist=['..!help',
              '小星星指令集',
              '',
              '==抽圖類==',
              '',
              '..抽',
              '..抽正妹',
              '..抽鮮肉',
              '..抽金句',
              '..現在吃什麼',
              '..講笑話',
              '',
              '===占卜類==',
              '',           
              '..抽塔羅牌/抽tarot',
              '..塔羅牌3張/抽tarot3張',
              '..抽塔羅牌5張/抽tarot5張', 
              '..抽籤', 
              '..星座名　ex天秤座',
              '',
              '==生活類==',
              '',
              '..查證  (查假消息',
              '..查天氣縣市 ex查天氣台北市',
              '..查空氣品質',
              '..天氣特報',
              '..查颱風',
              '..time (查農民曆)',
              '..time20180101',
              '..time2017010113',   
              '..蘋果新聞',
              '..看電影',
              '..看電影+電影名',
              '..本週上映',
              '..查集點',
              '..查咖啡',
              '..PTTHOT',
              '..PTT笨版',
              '..PTT表特',
              '..即時廢文',
              '..傳送LINE座標',
              '    (查座查附近的餐廳',
              '',
              '==金融類==',
              '',
              '..輸入美金、日幣可查匯率',
              '..1000=美金 (查TWD換匯',
              '..美金=100 (查美金換TWD',
              '..查股市',
              '..查股票股號 ex查股號鴻海',
              '',
              '==音樂類==',
              '',
              '..聽歌+關鍵字',
              '   (查youtube影片',
              '..youtube熱門',
              '..youtube華語',
              '..聽歌華語',
              '..聽歌台語',
              '..查歌詞+關鍵字',
              '',
              '==小遊戲==',
              '',
              '..18啦',
              '..拉霸',
              '',
              '==歡歌類==',
              '',
              '..抽歡歌',
              '..歡歌UID',
              '..歡歌UID:關鍵字',
              '..查伴奏+關鍵字',
              '',
              '== 小星星福利社 ==',
              '',
              '..小星星福利社 ',
              '    (精選商品',
              ''
]
    content = ""
    for i in helplist:
        a = '{}\n'.format(i)
        content += a
       
    return content
    


if __name__ == '__main__':
    print(shelp())
