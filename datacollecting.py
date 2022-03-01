# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 14:57:37 2021

@author: Lenovo
"""

###171805064 UMUT CAN AKDAĞ

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
import xlsxwriter

workbook = xlsxwriter.Workbook('qaaa.xlsx')
worksheet = workbook.add_worksheet()
names = ["Date","BTC","BtcVol","HighBtc","LowBtc","BtcChange","SOL","SolVol","HighSol","LowSol","SolChange","XRP","XrpVol","HighXrp","LowXrp","XrpChange","ada","adaVol","Highada","Lowada","adaChange","BNB","BnbVol","HighBnb","LowBnb","BnbChange","DOT","DotVol","HighDot","LowDot","DotChange","xlm","xlmVol","Highxlm","Lowxlm","xlmChange","LTC","LtcVol","HighLtc","LowLtc","LtcChange","trx","trxVol","Hightrx","Lowtrx","trxChange","eth","ethVol","Higheth","Loweth","ethChange","Position"]
column=0
row=0

for name in names:
    worksheet.write(row,column,name)
    column+=1
while (True):
    suan=datetime.now()
    dakika= suan.minute
    saniye=suan.second
    column = 0
    while True:
        suan=datetime.now()
        dakika= suan.minute
        saniye=suan.second
        """
        fbtc = requests.get("https://tr.investing.com/crypto/bitcoin/btc-usd-technical?__cf_chl_jschl_tk__=fc419cf4253b6ac13f1f92a934e0629d10f1b02a-1624143814-0-AXAvqu9lAQsWvQQOHCve0Mvl7Zb3tHET_W3ODcFCmsOYAB-OVIdc0rF9C9DjvEewtgDuehU82MnvBsmATQkrI9jeD8fkwnLAye3XfwO_iKhVYT3EnnVapYHdkM2SQR1QJyYvGZeSABSnmHHv9KqFqqhyAXLOBhU-DzQbb5qD5HxweLDjcXhaI3XRXdFHP8sq49x74YpQgzwMVZz-Lf5XVNIZ5P2gMQCpnwbJyQCW5JUfsRXZZskHZW5M_JVcjxZCCpECk1lYxXFSnhS1_O-9XjFQaRK4gPNFyHOv1DO4kq052mtkgLCOV5Cli3lOxMc9idS5s5wKf0o1tUbFMxB-KiyD98lKEp2M0RST3N3w-3Dko4OAnkNsA3nVwfGPigkYNaOYbYlJnVCpy1FdoG5G5csgvXSgz9VBtlWE_dyxJCPUSfsCBzDuwHQvR9z2qzUcmyAPklbwVsmhQHUJnqpB_MG-89T5m5HcaUWvaQVRF5ZgqiQx_f-b4FDceVZFt49G2w")
        
        sfbtc=BeautifulSoup(fbtc.content,"lxml")
        
        pbtc=sfbtc.find('div',{'id':"techinalContent"}).txt
        
        
        if(pbtc=="Güçlü Al"):
            pbtc==2
        elif(pbtc=="Al"):
            pbtc==1
        elif (pbtc=="Sat"):
            pbtc==3
        elif(pbtc=="Güçlü Sat"):
            pbtc==4
        elif(pbtc=="Nötr"):
            pbtc==0
          """  
        hhtrx = requests.get("https://finance.yahoo.com/quote/TRX-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hheth = requests.get("https://finance.yahoo.com/quote/ETH-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhltc = requests.get("https://finance.yahoo.com/quote/LTC-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhxlm = requests.get("https://finance.yahoo.com/quote/XLM-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhdot = requests.get("https://finance.yahoo.com/quote/DOT1-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhbnb = requests.get("https://finance.yahoo.com/quote/BNB-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhbtc = requests.get("https://finance.yahoo.com/quote/BTC-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhsol = requests.get("https://finance.yahoo.com/quote/SOL1-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhxrp = requests.get("https://finance.yahoo.com/quote/XRP-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        hhada = requests.get("https://finance.yahoo.com/quote/ADA-USD/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAANq407W77o6cy5hHmgRmlOLB850aFt2TJY-83FpYdp5VzOzGkxKbOgG239x2m2wSbEuHpvbIpB-wsgMk8yb40uKT1d1VMFwGHc-HxlytMQvktpkP6bYgBhI3IXa0FNDYNUn-aw6IKxhkh3KN1BDhYSlURF-6nwxL-7bvLBD8TXPh")
        
        sssdot=BeautifulSoup(hhdot.content,"lxml")
        ssstrx=BeautifulSoup(hhtrx.content,"lxml")
        ssseth=BeautifulSoup(hheth.content,"lxml")
        sssbnb=BeautifulSoup(hhbnb.content,"lxml")
        sssxlm=BeautifulSoup(hhxlm.content,"lxml")
        sssltc=BeautifulSoup(hhltc.content,"lxml")
        ssssol=BeautifulSoup(hhsol.content,"lxml")
        sssbtc=BeautifulSoup(hhbtc.content,"lxml")
        sssxrp=BeautifulSoup(hhxrp.content,"lxml")
        sssada=BeautifulSoup(hhada.content,"lxml")
        
        volBtc=sssbtc.find("td",{"data-test":"TD_VOLUME-value"}).text
        volSol=ssssol.find("td",{"data-test":"TD_VOLUME-value"}).text
        volada=sssada.find("td",{"data-test":"TD_VOLUME-value"}).text
        volXrp=sssxrp.find("td",{"data-test":"TD_VOLUME-value"}).text
        volLtc=sssltc.find("td",{"data-test":"TD_VOLUME-value"}).text
        volDot=sssdot.find("td",{"data-test":"TD_VOLUME-value"}).text
        volBnb=sssbnb.find("td",{"data-test":"TD_VOLUME-value"}).text
        volxlm=sssxlm.find("td",{"data-test":"TD_VOLUME-value"}).text
        voltrx=ssstrx.find("td",{"data-test":"TD_VOLUME-value"}).text
        voleth=ssseth.find("td",{"data-test":"TD_VOLUME-value"}).text
        
        htrx = requests.get("https://www.gate.io/trade/TRX_USDT")
        heth = requests.get("https://www.gate.io/trade/ETH_USDT")
        hltc = requests.get("https://www.gate.io/trade/LTC_USDT")
        hxlm = requests.get("https://www.gate.io/trade/xlm_USDT")
        hdot = requests.get("https://www.gate.io/trade/DOT_USDT")
        hbnb = requests.get("https://www.gate.io/trade/BNB_USDT")
        hbtc = requests.get("https://www.gate.io/trade/BTC_USDT")
        hsol = requests.get("https://www.gate.io/trade/SOL_USDT")
        hxrp = requests.get("https://www.gate.io/trade/XRP_USDT")
        hada = requests.get("https://www.gate.io/trade/ada_USDT")
        
        hsdot=BeautifulSoup(hdot.content,"lxml")
        hstrx=BeautifulSoup(htrx.content,"lxml")
        hseth=BeautifulSoup(heth.content,"lxml")
        hsbnb=BeautifulSoup(hbnb.content,"lxml")
        hsxlm=BeautifulSoup(hxlm.content,"lxml")
        hsltc=BeautifulSoup(hltc.content,"lxml")
        hssol=BeautifulSoup(hsol.content,"lxml")
        hsbtc=BeautifulSoup(hbtc.content,"lxml")
        hsxrp=BeautifulSoup(hxrp.content,"lxml")
        hsada=BeautifulSoup(hada.content,"lxml")
        
        lowBtc=hsbtc.find("span",{"id":"tLow"}).text
        highBtc=hsbtc.find("span",{"id":"tHigh"}).text
        lowSol=hssol.find("span",{"id":"tLow"}).text
        highSol=hssol.find("span",{"id":"tHigh"}).text
        lowBnb=hsbnb.find("span",{"id":"tLow"}).text
        highBnb=hsbnb.find("span",{"id":"tHigh"}).text
        lowXrp=hsxrp.find("span",{"id":"tLow"}).text
        highXrp=hsxrp.find("span",{"id":"tHigh"}).text
        lowada=hsada.find("span",{"id":"tLow"}).text
        highada=hsada.find("span",{"id":"tHigh"}).text
        lowDot=hsdot.find("span",{"id":"tLow"}).text
        highDot=hsdot.find("span",{"id":"tHigh"}).text
        lowLtc=hsltc.find("span",{"id":"tLow"}).text
        highLtc=hsltc.find("span",{"id":"tHigh"}).text
        lowxlm=hsxlm.find("span",{"id":"tLow"}).text
        highxlm=hsxlm.find("span",{"id":"tHigh"}).text
        lowtrx=hstrx.find("span",{"id":"tLow"}).text
        hightrx=hstrx.find("span",{"id":"tHigh"}).text
        loweth=hseth.find("span",{"id":"tLow"}).text
        higheth=hseth.find("span",{"id":"tHigh"}).text
        
        tagtrxy=hstrx.find("strong",{"id":"currRateNum"}).text
        tagethy=hseth.find("strong",{"id":"currRateNum"}).text
        tagBnby=hsbnb.find("strong",{"id":"currRateNum"}).text
        tagxlmy=hsxlm.find("strong",{"id":"currRateNum"}).text
        tagDoty=hsdot.find("strong",{"id":"currRateNum"}).text
        tagLtcy=hsltc.find("strong",{"id":"currRateNum"}).text
        tagBtcy=hsbtc.find("strong",{"id":"currRateNum"}).text
        tagSoly=hssol.find("strong",{"id":"currRateNum"}).text
        tagXrpy=hsxrp.find("strong",{"id":"currRateNum"}).text
        tagaday=hsada.find("strong",{"id":"currRateNum"}).text
        
        tagSol=hssol.find("i",{"id":"currPrice"}).text
        tagtrx=hstrx.find("i",{"id":"currPrice"}).text
        tageth=hseth.find("i",{"id":"currPrice"}).text
        tagLtc=hsltc.find("i",{"id":"currPrice"}).text
        tagDot=hsdot.find("i",{"id":"currPrice"}).text
        tagxlm=hsxlm.find("i",{"id":"currPrice"}).text
        tagBnb=hsbnb.find("i",{"id":"currPrice"}).text
        tagBtc=hsbtc.find("i",{"id":"currPrice"}).text
        tagXrp=hsxrp.find("i",{"id":"currPrice"}).text
        tagada=hsada.find("i",{"id":"currPrice"}).text
        content = ["{}/{}/{}-{}:{}".format(suan.day,suan.month,suan.year,suan.hour,dakika),tagBtc,volBtc,highBtc,lowBtc,tagBtcy,tagSol,volSol,highSol,lowSol,tagSoly,tagXrp,volXrp,highXrp,lowXrp,tagXrpy,tagada,volada,highada,lowada,tagaday,tagBnb,volBnb,highBnb,lowBnb,tagBnby,tagDot,volDot,highDot,lowDot,tagDoty,tagxlm,volxlm,highxlm,lowxlm,tagxlmy,tagLtc,volLtc,highLtc,lowLtc,tagLtcy,tagtrx,voltrx,hightrx,lowtrx,tagtrxy,tageth,voleth,higheth,loweth,tagethy]
        
        row+=1
        column=0
        for item in content :
        
            worksheet.write(row, column, item)
            column += 1
        print("Data written")
        time.sleep(5)
