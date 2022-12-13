import threading
from threading import *
from queue import Queue
from spider import Spider
from domain import *
from functions import *
from database import *
from gui import gui
import json
import PySimpleGUI as GUI
import resultsList
import requests
import lxml 
from bs4 import BeautifulSoup
import time
import operator

# Start gui <<<<<<<<<<<<<<<< I have a feeling we are going to want to run the gui in here and call different layout from the file?
# ~"Create" database
    # Displays the original database write from the rip?
# Recieve selected url from user <<<<<<<<<<<<<How shall they select? Select then push a button
# Passes that into the crawler <<<<<<<<<<<<<<<Need to figure out above step and how that user inout is generated. WIll all this happen in the main while loop? I think so
# Over write the file
# Append to the dictionary <<<<<<<<<<<<<<<<< new method here
# Display right side pane based on new array <<<<<<<<<<< Learn this
#
GUI.theme('LightBrown4')
queue = getDataBaseUrls()
runningQueue = getDataBaseUrls()
NUMBER_OF_THREADS = 8
#print("current queue\n")
#print(queue)
objSem = Semaphore(8)
dbSem = Semaphore(1)
time.sleep(5)

def getWords(URL,searchKey):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'lxml')
    words = str(soup.get_text(strip=True))
    words = words.lower()
    return words.count(searchKey)

# this needs to be url and rank
def create_workers():
    for x in range(NUMBER_OF_THREADS):
        objSem.acquire()
        threaded = threading.Thread(target = work)
        threaded.value = x
        threaded.daemon = True
        threaded.start()

# Do the next job in the queue
def work():
    url = queue[0]
    #print("tester 1")
    queue.pop(0)
    #print("tester 2")
    #print("\n......................\n")
    #print("\n number of stuff: ")
    #print(threading.current_thread().value) # possibly the number of the current thread
    #print("\n......................")
    Spider.crawler(threading.current_thread().name, url)
    #print("tester 3")
    #print("SPIDER\n")
    #print(Spider.crawled1)
    #print("SPIDER\n\n")
    dbSem.acquire()
    add_contained_urls(url,Spider.crawled1)
    dbSem.release()
    for link in Spider.crawled1:
        if doesNotAlreadyExists(runningQueue, link):
            runningQueue.append(link)
            dbSem.acquire()
            add_contained_parent_url(link)
            dbSem.release()
#    for link in Spider.crawled1:
#        if(doesNotAlreadyExists(getDataBaseUrls(),link)):
#            add_contained_parent_url(link)
    objSem.release()
    #queue.task_done()
    

# Each queued link is a new job
#def create_jobs():
    #print(link)
    #queue.join()
    #crawl()


# Check if there are items in the queue, if so crawl them
#def crawl():
    #if len(queue) > 0:
#        print("\n 11111111111")
        #print("crawled1\n")
        #print(Spider.crawled1)
        #print("\n 11111111111\n")
#        create_jobs()

# for x in range(200):
#     #create_workers()
#     #crawl()
#     print("hi")

# this needs to be url and rank
headings = [["URL"],["KeyWord"],["Rank"]]

table_array = []
c2table_array = []
with open('database.JSON','r') as file:
    queue_array = []
    dictionary = {}
    dictionary = json.load(file)
    url_list = list(dictionary['URL'])
    shhh_quiet = 0
    for url_dict in url_list:
        for url in url_dict:
            shhh_quiet += 1
            if(shhh_quiet > 10):
                break
            # print(url)
            # These 3 lines have to stay together. This is what creates a full list. List must = [ [] [] [] [] [] [] ] not [[]]
            queue_array = []
            queue_array.append(url)
            table_array.append(queue_array)
            # print(table_array)
            # Populate array for second column with ranked URLs
            # 1. User to click one of the initial links and click crawl
            # 2. Crawl selected page for roughly 20 URLs
            # 3. Grab all data from each page and search each one for the keyword
        with open('rank_database.JSON','r') as file:
            r_dict = {}
            r_dict = json.load(file)
            for array in range(len(table_array)):
                try:
                    for k,v in r_dict['URL'][array][url]['Keyword'][0].items():
                        table_array[array].append(k)
                        table_array[array].append(v)
                except:
                    continue
    # Second Column using dictionary['contained_urls']
    # Does this need to be in the event tag? I think that makes if different every time the user chooses

# print(table_array)


layout_url = [

    [GUI.Table(
    values=table_array,
    headings=headings,
    max_col_width=100,
    auto_size_columns=False,
    display_row_numbers=True,
    justification='middle',
    num_rows=10,
    enable_events = True,
    enable_click_events = True,
    key="-TABLE-",
    row_height=35,
    col_widths= [50,50,50]
    )]
]

layout_picked_url = [
    [GUI.Table(
        values=c2table_array,
        headings=headings,
        max_col_width=50,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='left',
        num_rows=10,
        enable_events = True,
        key="-TABLE-",
        row_height=35
        )]
]

layout = [ 
    [
    [GUI.Text("Enter search term:"), GUI.Input(key='-KEYWORD-', do_not_clear=True, size=(20,1))],    
    [GUI.Button('-SUBMIT-')],
    [GUI.Column(layout_url)],
    # GUI.Button('Search',key='-SEARCH-'),
    # GUI.VSeparator(),
    # GUI.Column(layout_picked_url)
    ]

]

window = GUI.Window("Football Web Crawler",layout, resizable=True)

def sort_table(table_array, col_num_clicked):
    try:
        table_data = sorted(table_array, key=operator.itemgetter(col_num_clicked), reverse=True)
    except Exception as e:
        GUI.popup_error('Error in sorting table','Error',e)
    return table_data

while True:
    
    # Initial window is a start button
    event, values = window.read()    
    # This is the Exit button/window close event
    if event == "EXIT" or event == GUI.WIN_CLOSED:
        break
    # This event will do create a new window
    if event =="-SUBMIT-":
        keyword = values['-KEYWORD-']
        with open('rank_database.JSON','r') as file: 
            r_dict = {}
            r_dict = json.load(file)
            for index in range(len(r_dict['URL'])):
                for k,v in r_dict['URL'][index].items():
                    URL = k
                    print("==============================",URL)
                    DOMAIN_NAME = getDomainName(URL)
                    try:
                        word_count = getWords(URL,keyword)
                    except: 
                        word_count = 0
                    print(word_count)
                    add_rank(URL,keyword,word_count)
                    # add table update statement in GUI                 #window["-PTABLE-"].update(c2table_array)
                    window["-TABLE-"].update(table_array)

                

    if event[0] == '-TABLE-':
        if event[2][0] == -1 and event[2][1] != -1:
            col_num_clicked = event[2][1]
            new_table_array = sort_table(table_array, col_num_clicked)
            window['-TABLE-'].update(new_table_array)

    if event =="-TABLE-":
       
        # Pass in a new URL for crawling and overwrite the file
        url_index = values[event][0]                                                  # setting index from values table   
        URL = table_array[url_index][0];              # this will be the user's selected URL (EX: https://www.sbnation.com/college-football/)
        DOMAIN_NAME = getDomainName(URL)          # Get domain name from selected URL
        Spider("selected_page", URL, DOMAIN_NAME, None)            # Pass this index to spider, new searched URL, based on results of crawl, make new file with URLs


        
        if(check_contained(URL)):
            c2table_array = []
            print("adding contained")
            add_contained_urls(table_array[url_index][0],read_selected())
            with open('database.JSON','r') as file:
                c2column_links = []
                c2dictionary = {}
                c2dictionary = json.load(file)
                print(URL)
                c2column_links = (c2dictionary['URL'][url_index][URL]['contained_urls']) #index of each contained_urls position in database.JSON

                #group all links into bracketed array. [ [] [] [] [] [] [] ] not [[]]
                for url in c2column_links:
                    # These 3 lines have to stay together. This is what creates a full list. List must = [ [] [] [] [] [] [] ] not [[]]
                    c2queue_array = []
                    c2queue_array.append(url)
                    c2table_array.append(c2queue_array)
            

              
        else:
            c2table_array = []
              # Add new links to array at index of clicked link
            with open('database.JSON','r') as file:
                c2column_links = []
                c2dictionary = {}
                c2dictionary = json.load(file)
                print(URL)
                c2column_links = (c2dictionary['URL'][url_index][URL]['contained_urls']) #index of each contained_urls position in database.JSON
                
                #group all links into bracketed array. [ [] [] [] [] [] [] ] not [[]]
                for url in c2column_links:
                    # print(url)
                    # These 3 lines have to stay together. This is what creates a full list. List must = [ [] [] [] [] [] [] ] not [[]]
                    c2queue_array = []
                    c2queue_array.append(url)
                    c2table_array.append(c2queue_array)
                    
                # print(c2table_array)
        print(len(c2table_array))
        resultsList.create(c2table_array, headings)
 
        # Future: Check if selected url has contained urls in database -Eric
    GUI.theme('I like potatoes')
window.close()




















# if event =="-PTABLE-":
#         print("Hello World")
#         # print("print 1: ",values[event][0])                                     # Printing index of column 1 link
#         # Pass in a new URL for crawling and overwrite the file
#         index = values[event][0]                                                  # setting index from values table 
#         # print("Print 2",table_array[index][0])                                  # Printing link from specified index of column 1
#         # new name. Probably the url
#         NAME = "selected_page"                          # Name of new directory
#         # New url here
#         HOME_PAGE = table_array[index][0]              # this will be the user's selected URL (EX: https://www.sbnation.com/college-football/)
#         DOMAIN_NAME = getDomainName(HOME_PAGE)          # Get domain name from selected URL
#         # print(DOMAIN_NAME)
#         # I think we should overwrite this file
#         QUEUE_FILE = NAME + "/queue.txt"

#         # NUM_OF_THREADS = 8
#         queue = Queue()
#         Spider(NAME, HOME_PAGE, DOMAIN_NAME)            # Pass this index to spider, new searched URL, based on results of crawl, make new file with URLs
        
#         add_contained_parent_url(HOME_PAGE)
#         add_contained_urls(HOME_PAGE,read_selected())   # Add new links to array at index of clicked link
    
#         # create table to read all values from contained urls
        
#         with open('database.JSON','r') as file:
#             c2queue_array = []
#             c2column_links = []
#             c2dictionary = {}
#             c2dictionary = json.load(file)
#             # for index in range(len(dictionary['URL'])):
#             c2column_links = (c2dictionary['URL'][index][table_array[index][0]]['contained_urls']) #index of each contained_urls position in database.JSON

#             #group all links into bracketed array. [ [] [] [] [] [] [] ] not [[]]
#             for url in c2column_links:
#                 # print(url)
#                 # These 3 lines have to stay together. This is what creates a full list. List must = [ [] [] [] [] [] [] ] not [[]]
#                 c2queue_array = []
#                 c2queue_array.append(url)
#                 c2table_array.append(c2queue_array)
        
#                 # print(c2table_array)

#         # Pass URLs into second column gui from database
#         #window["-PTABLE-"].update(c2table_array)
#         #c2table_array = []
#             resultsList.create(c2table_array, headings) 