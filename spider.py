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
        Spider.startingUrl = startingUrl
        Spider.qFile = Spider.name + "/queue.txt"
        Spider.cFile = Spider.name + "/crawled.txt"
        Spider.startingUrl = startingUrl
        Spider.domainName = domainName
        self.boot()
        self.crawl("Spider 1", Spider.startingUrl)

    @staticmethod
    def boot():
        createDirectory(Spider.name)
        createFiles(Spider.name, Spider.startingUrl)
        Spider.queue = fileIntoSet(Spider.qFile)
        Spider.crawled = fileIntoSet(Spider.cFile)


    @staticmethod
    def crawl(currentThread, URL):
        if URL not in Spider.crawled:
            if (URL == "#context"):
                Spider.queue.remove(URL)
                return
            print(currentThread + " current crawling " + URL) #Displays the page being crawled
            print("Queue " + str(len(Spider.queue)))
            print("Crawled " + str(len(Spider.crawled)))
            Spider.addToQueue(Spider.getLinks(URL))
            try:
                Spider.queue.remove(URL)
                Spider.crawled.add(URL)
                Spider.updateFiles()
            except:
                print("invalid 1")

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
        try:
            page = requests.get(URL)
            #print("1")
            soup = BeautifulSoup(page.content,'lxml')
            #print("2")
            urls = []
            #print("3")
            i = 0
            #print("4")
            for link in soup.find_all('a'):
                #print("5")
                
                #print("6")
                i += 1
                #print("7")
                #print("\n found link: " + link)
                #print("8")
                urls.append(Spider.startingUrl)
                #print("9")
                urls.append(link.get('href'))
            print(urls)    
            return urls
        except:
             print("Error page can't be crawled "+ URL)
             return set()

    def addToQueue(URLs):
        for url in URLs:
            #print("URL \n" + url + "URL\n")
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            try:
                print("URL \n" + url + "URL\n")
                if url != url.startswith("h"):
                    continue
            except:
                print("invalid 2")
            Spider.queue.add(url)

    def updateFiles():
        setIntoFile(Spider.queue, Spider.qFile)
        setIntoFile(Spider.crawled, Spider.cFile)
            





