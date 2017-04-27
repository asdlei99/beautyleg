#coding-utf-8
import requests,re,json,html2text,sys,time,base64
from bs4 import BeautifulSoup
from array import array
import time
from urllib.request import urlretrieve
import os
from urllib import parse
from axelDownLoader import AxelDownLoader
from xunleiDownLoader import addTasktoXunlei

sys.setrecursionlimit(1000000) #例如这里设置为一百万
url="http://www.beautylegmm.com/Sarah/beautyleg-1420.html"
urlhead="http://www.beautylegmm.com"
path = 'D:\\1111\\'
basepath = "D:\\MY_DownLoad\\"


class ContextDownLoader(object):

    def __init__(self, link, path='D:\\1111\\'):
        self.link = link
        self.path = path

    def setLink(self,link):
        self.link = link
        return self

    def getLink(self):
        return self.link

    def setPath(self,path):
        self.path = path
        return self

    def getPath(self):
        return self.path

    def downHtmlCont(self):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
        hasNext = True
        isGetTitle = False
        nextLink = self.link
        while hasNext:
            hasNext = False
            while True:
                try:
                    get_url = requests.get(nextLink, headers=headers)
                    break
                except requests.exceptions.ContentDecodingError as e:
                    print('requests.exceptions.ContentDecodingError...')
                    time.sleep(1)
                    continue
                except requests.exceptions.ProxyError as e:
                    print('equests.exceptions.ProxyError...')
                    time.sleep(1)
                    continue
                except requests.packages.urllib3.exceptions.ProtocolError as e:
                    print('requests.packages.urllib3.exceptions.ProtocolError...')
                    time.sleep(1)
                    continue
                except requests.exceptions.ConnectionError as e:
                    print('requests.exceptions.ConnectionError...')
                    time.sleep(1)
                    continue
            codingTypr = get_url.encoding
            soup = BeautifulSoup(get_url.text,"html5lib")
            if isGetTitle == False:
                titleList = soup.find_all("div", class_="title")
                pageTitle = titleList[0].h2.string
                pageTitleList = pageTitle.split()
                pageTitle = pageTitleList[-4]+"_"+pageTitleList[-3]+"_"+pageTitleList[-2]
                pageTitle = pageTitle.replace('.', '_')
                pageTitle = basepath+pageTitle+".txt"
                try:
                    with open(pageTitle, 'w') as f:
                        f.write('')
                except OSError as e:
                    return
                isGetTitle = True
            srcDiv = soup.find_all("div", class_="post")
            imgList = srcDiv[0].find_all("img")
            for i in imgList:
                link = urlhead+i['src']
                print(link)
                try:
                    with open(pageTitle, 'a') as f:
                        f.write('%s\n'%(link))
                except OSError as e:
                    return
            nextLinkDiv = soup.find_all("div", class_="archives_page_bar")
            nextLinkF = nextLinkDiv[0].find_all("a", class_="next")
            for i in nextLinkF:
                nextLink = i["href"]
                hasNext = True





if __name__=="__main__":
    print('runing..............')
    a = ContextDownLoader(url)
    a.downHtmlCont()
    print('done')








