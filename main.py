import threading
from queue import Queue
from spider import Spider
from domain import *
from functions import *
from database import create_dict,add_contained_urls
from gui import init_crawl

NAME = "sbnation"
HOME_PAGE = "https://www.sbnation.com/college-football/"
DOMAIN_NAME = getDomainName(HOME_PAGE)
QUEUE_FILE = NAME + "/queue.txt"
CRAWLED_FILE = NAME + "/crawled.txt"
NUM_OF_THREADS = 8
queue = Queue()
Spider(NAME, HOME_PAGE, DOMAIN_NAME)

create_dict()



















