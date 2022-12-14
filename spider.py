from urllib.request import urlopen
from linkSearch import LinkSearcher
from domain import *
import requests
import lxml 
from bs4 import BeautifulSoup

class Spider:
    ## Shared variables for the spider fleet
    qFile= ""
    cFile= ""
    name =""
    startingUrl = ""
    domainName = ""
    queue = set()
    crawled = set()
    crawled1 = []
    def __init__(self, name, startingUrl, domainName, crawled1):
        Spider.name = name
        Spider.qFile = Spider.name + "/queue.txt"
        # Spider.cFile = Spider.name + "/crawled.txt"
        Spider.startingUrl = startingUrl
        Spider.domainName = domainName
        Spider.crawled1 = crawled1
        #self.boot()
        self.crawler("Spider 1", Spider.startingUrl)

    #@staticmethod
    #def boot():
        #createDirectory(Spider.name)
        #createFiles(Spider.name, Spider.startingUrl)
        #Spider.queue = fileIntoSet(Spider.qFile)
        # Spider.crawled = fileIntoSet(Spider.cFile)

    # gets all urls on webpage
    def getLinks(URL):
        urlsTemp = []
        urlsMain = []
        try:
            page = requests.get(URL, 'lxml')
            soup = BeautifulSoup(page.content, 'lxml')
            for link in soup.find_all('a'):
                try:
                    urlsTemp.append(Spider.startingUrl)
                    urlsTemp.append(link.get('href'))
                except:
                    print("Error 66")
            for url in urlsTemp:
                #print(getSubDomainName(url))
                if getSubDomainName(url) == "www.twitter.com":
                    continue
                if getSubDomainName(url) == "www.facebook.com":
                    continue
                if getSubDomainName(url) == "auth.voxmedia.com":
                    continue
                if getSubDomainName(url) == "twitter.com":
                    continue
                if getSubDomainName(url) == "www.youtube.com":
                    continue
                try:
                    if url != None and url.startswith("h"):
                        urlsMain.append(url)
                except:
                    print("Error 77")
        except:
            print("ERROR 404")
        return urlsMain 

    #likly where checks to avoids duplicates should go
    @staticmethod
    def crawler(thread, URL):
        print(thread + " current crawling " + URL)
        Spider.crawled1 = Spider.getLinks(URL)

    def getWords(URL,searchKey):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,'lxml')
        words = str(soup.get_text(strip=True))
        words = words.lower()
        return words.count(searchKey)
        