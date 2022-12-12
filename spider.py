from urllib.request import urlopen
from linkSearch import LinkSearcher
from functions import *
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
        self.boot()
        self.crawl("Spider 1", Spider.startingUrl)

    @staticmethod
    def boot():
        createDirectory(Spider.name)
        #createFiles(Spider.name, Spider.startingUrl)
        #Spider.queue = fileIntoSet(Spider.qFile)
        # Spider.crawled = fileIntoSet(Spider.cFile)

    # gets all urls on webpage
    def getLinks(URL):
        #print("Test 5")
        urlsTemp = []
        urlsMain = []
        try:
            page = requests.get(URL,'lxml')
            print("Test 6")
        # ,'lxml'
            soup = BeautifulSoup(page.content,'lxml')
            print("URLS")
            for link in soup.find_all('a'):
                urlsTemp.append(Spider.startingUrl)
                urlsTemp.append(link.get('href'))
            for url in urlsTemp:
                try:
                    if url != None and url.startswith("h"):
                        urlsMain.append(url)
                except:
                    print("Error your mom")
            print(urlsMain)
        except:
            print("ERROR 404")
        return urlsMain 

    #likly where checks to avoids duplicates should go
    @staticmethod
    def crawler(thread, URL):
    # if URL not in Spider.crawled:
        print(thread + " current crawling " + URL)
        #print("Queue " + str(len(Spider.queue)))
        # print("Crawled " + str(len(Spider.crawled)))
        #Spider.addToQueue(Spider.getLinks(URL))
        #tempValue = ""
        #print("\n\n\n\ntempValue")
        #print(tempValue)
        #tempValue = Spider.getLinks(URL)
        #print(tempValue)
        print("tempValue2\n\n\n\n")
        Spider.crawled1 = Spider.getLinks(URL)
        print("tester 4")
        #Spider.queue.remove(URL)
        #Spider.crawled.add(URL)
        #Spider.updateFiles()

      
 
    # def getLinks(URL):
    #     htmlValue = ""
    #     try:
    #         value = urlopen(URL)
    #         if value.getHeader("Content-Type") == "text/html":
    #             bytes = value.read()
    #             htmlString = bytes.decode("utf-8")
    #         searcher = LinkSearcher(Spider.startingUrl, URL)
    #         searcher.feed(htmlString)
    #     except:
    #         print("Error page can't be crawled "+ URL)
    #         return set()
    #     return searcher.gatheredLinks()
    
    
    # gets all urls on webpage
    #def getLinks(URL):
        #print("Test 5")
        #page = requests.get(URL)
        #print("Test 6")
        #soup = BeautifulSoup(page.content,'lxml')
        #print("URLS")
        #urls = []
        #or link in soup.find_all('a'):
        #    urls.append(Spider.startingUrl)

        #    urls.append(link.get('href'))
        #print(urls)
        #return urls

    
    
    def getWords(URL,searchKey):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,'lxml')
        words = str(soup.get_text(strip=True))
        words = words.lower()
        return words.count(searchKey)
        


    #def addToQueue(URLs):
        #for url in URLs:
            #if url in Spider.queue:
            #    continue
            # if url in Spider.crawled:
            #     continue
            #Spider.queue.add(url)

    #def updateFiles():
        #setIntoFile(Spider.queue, Spider.qFile)
        # setIntoFile(Spider.crawled, Spider.cFile)
            





