from html.parser import HTMLParser
from urllib import parse

class LinkSearcher(HTMLParser):
    def __init__(self, homePage, searchPage):
        super().__init__
        self.homePage = homePage
        self.searchPage = searchPage
        self.URLS = set()

    def findTag(self, tag, attributes):
        if tag == "a":
            for (attribute, value) in attributes:
                if attribute == "href":
                    URL = parse.urljoin(self.homePage, value)
                    self.URLS.add(URL)

    def gatheredLinks(self):
        return self.URLS



