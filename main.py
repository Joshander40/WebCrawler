import threading
from queue import Queue
from spider import Spider
from domain import *
from functions import *
from database import create_dict,add_contained_urls,read_selected
from gui import gui
import json
import PySimpleGUI as GUI
import resultsList

# Start gui <<<<<<<<<<<<<<<< I have a feeling we are going to want to run the gui in here and call different layout from the file?
# ~"Create" database
    # Displays the original database write from the rip?
# Recieve selected url from user <<<<<<<<<<<<<How shall they select? Select then push a button
# Passes that into the crawler <<<<<<<<<<<<<<<Need to figure out above step and how that user inout is generated. WIll all this happen in the main while loop? I think so
# Over write the file
# Append to the dictionary <<<<<<<<<<<<<<<<< new method here
# Display right side pane based on new array <<<<<<<<<<< Learn this


# this needs to be url and rank
PROJECT_NAME = 'sbnation'
HOMEPAGE = 'https://www.sbnation.com/college-football/'
DOMAIN_NAME = getDomainName(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# # Create worker threads (will die when main exits)
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target = work)
        t.daemon = True
        t.start()


# Do the next job in the queue
def work():
    while True:
        url = queue.get()
        Spider.crawl(threading.current_thread().name, url)
        queue.task_done()


# Each queued link is a new job
def create_jobs():
    for link in fileIntoSet(QUEUE_FILE):
        if (link != "#content"):
            queue.put(link)
        print(link)
    queue.join()
    crawl()


# Check if there are items in the queue, if so crawl them
def crawl():
    queued_links = fileIntoSet(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + ' links in the queue')
        create_jobs()


create_workers()
crawl()



















