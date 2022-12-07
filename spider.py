from urllib.request import urlopen
from linkSearch import LinkSearcher
from functions import *
import requests
# import lxml 
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
    def __init__(self, name, startingUrl, domainName):
        Spider.name = name
        Spider.qFile = Spider.name + "/queue.txt"
        # Spider.cFile = Spider.name + "/crawled.txt"
        Spider.startingUrl = startingUrl
        Spider.domainName = domainName
        self.boot()
        self.crawl("Spider 1", Spider.startingUrl)

    @staticmethod
    def boot():
        createDirectory(Spider.name)
        createFiles(Spider.name, Spider.startingUrl)
        Spider.queue = fileIntoSet(Spider.qFile)
        # Spider.crawled = fileIntoSet(Spider.cFile)

    @staticmethod
    def crawl(thread, URL):
        # if URL not in Spider.crawled:
            print(thread + " current crawling " + URL)
            print("Queue " + str(len(Spider.queue)))
            # print("Crawled " + str(len(Spider.crawled)))
            Spider.addToQueue(Spider.getLinks(URL))
            Spider.queue.remove(URL)
            # Spider.crawled.add(URL)
            Spider.updateFiles()

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
    def getLinks(URL):
        page = requests.get(URL)

        soup = BeautifulSoup(page.content,'lxml')
        
        urls = []
        for link in soup.find_all('a'):
            urls.append(Spider.startingUrl)
            urls.append(link.get('href'))
        return urls
    
    def getWords(URL,searchKey):
        page = requests.get(URL)
        soup = BeautifulSoup(page.content,'lxml')
        words = str(soup.get_text(strip=True))
        words = words.lower()
        words.count(searchKey)


    def addToQueue(URLs):
        for url in URLs:
            if url in Spider.queue:
                continue
            # if url in Spider.crawled:
            #     continue
            Spider.queue.add(url)

    def updateFiles():
        setIntoFile(Spider.queue, Spider.qFile)
        # setIntoFile(Spider.crawled, Spider.cFile)
            





