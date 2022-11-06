from urllib.parse import urlparse


def getSubDomainName(url):
    try:
        return urlparse(url).netloc
    except:
        return ""

def getDomainName(url):
    try:
        values = getSubDomainName(url).split(".")
        return values[-2] + "." + values[-1]
    except:
        return ""
