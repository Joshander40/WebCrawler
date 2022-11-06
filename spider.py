from urllib.request import urlopen
from linkSearch import LinkSearcher
from functions import *

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
        Spider.cFile = Spider.name + "/crawled.txt"
        Spider.startingUrl = startingUrl
        Spider.domainName = domainName
        self.boot()
        self.crawl("Spider 1", Spider.startingUrl)

    def boot():
        createDirectory(Spider.name)
        createFiles(Spider.name, Spider.startingUrl)
        Spider.queue = fileIntoSet(Spider.qFile)
        Spider.crawled = fileIntoSet(Spider.cFile)

    def crawl(thread, URL):
        if URL not in Spider.crawled:
            print(thread + " current crawling " + URL)
            print("Queue " + str(len(Spider.queue)))
            print("Crawled " + str(len(Spider.crawled)))
            Spider.addToQueue(Spider.getLinks(URL))
            Spider.queue.remove(URL)
            Spider.crawled.add(URL)
            Spider.updateFiles()

    def getLinks(URL):
        htmlValue = ""
        try:
            value = urlopen(URL)
            if value.getHeader("Content-Type") == "text/html":
                bytes = value.read()
                htmlString = bytes.decode("utf-8")
            searcher = LinkSearcher(Spider.startingUrl, URL)
            searcher.feed(htmlString)
        except:
            print("Error page can't be crawled")
            return set()
        return searcher.gatheredLinks()

    def addToQueue(URLs):
        for url in URLs:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            if Spider.domainName not in url:
                continue
            Spider.queue.add(url)

    def updateFile():
        setIntoFile(Spider.queue, Spider.qFile)
        setIntoFile(Spider.crawled, Spider.cFile)
            




