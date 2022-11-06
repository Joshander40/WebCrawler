import threading
from queue import Queue
from spider import Spider
from domain import *
from functions import *

NAME = "nfl"
HOME_PAGE = "https://www.nfl.com/"
DOMAIN_NAME = getDomainName(HOME_PAGE)
QUEUE_FILE = NAME + "/queue.txt"
CRAWLED_FILE = NAME + "/crawled.txt"
NUM_OF_THREADS = 8
queue = Queue()
Spider(NAME, HOME_PAGE, DOMAIN_NAME)
















