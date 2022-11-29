import threading
from queue import Queue
from spider import Spider
from domain import *
from functions import *
from database import create_dict,add_contained_urls
from gui import gui
import json
import PySimpleGUI as GUI

# Start gui <<<<<<<<<<<<<<<< I have a feeling we are going to want to run the gui in here and call different layout from the file?
# ~"Create" database
    # Displays the original database write from the rip?
# Recieve selected url from user <<<<<<<<<<<<<How shall they select? Select then push a button
# Passes that into the crawler <<<<<<<<<<<<<<<Need to figure out above step and how that user inout is generated. WIll all this happen in the main while loop? I think so
# Over write the file
# Append to the dictionary <<<<<<<<<<<<<<<<< new method here
# Display right side pane based on new array <<<<<<<<<<< Learn this


# this needs to be url and rank
headings = ["URL"]

table_array = []
with open('database.JSON','r') as file:
    queue_array = []
    dictionary = {}
    dictionary = json.load(file)
    # for index in range(len(dictionary['URL'])):
    url_list = list(dictionary['URL'])
    # print(url_list)
    for url_dict in url_list:
        
        for url in url_dict:
            print(url)
            # These 3 lines have to stay together. This is what creates a full list. List must = [ [] [] [] [] [] [] ] not [[]]
            queue_array = []
            queue_array.append(url)
            table_array.append(queue_array)
            # Populate array for second column with ranked URLs
            # 1. User to click one of the initial links and click crawl
            # 2. Crawl selected page for roughly 20 URLs
            # 3. Grab all data from each page and search each one for the keyword

# print(table_array)


layout_url = [

    [GUI.Table(
    values=table_array,
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

layout_picked_url = [
    [GUI.Table(
        values="",
        headings=headings,
        max_col_width=50,
        auto_size_columns=True,
        display_row_numbers=True,
        justification='left',
        num_rows=10,
        key="-PTABLE-",
        enable_events = True,
        row_height=35
        )]
]

layout = [ 
    [
    GUI.Column(layout_url),
    GUI.Button('Search',key='-SEARCH-'),
    GUI.VSeparator(),
    GUI.Column(layout_picked_url)
    ]

]

window = GUI.Window("Test",layout)

while True:
    # Initial window is a start button
    event, values = window.read()
    
    # This is the Exit button/window close event
    if event == "EXIT" or event == GUI.WIN_CLOSED:
        break
    # This event will do the initial crawl
    if event == "-START-":
        # Initial first 10 database display
        break;
    if event =="-TABLE-":
        print(values[event][0])
        # Pass in a new URL for crawling and overwrite the file
        index = values[event][0]
        print(table_array[index][0])
        # new name. Probably the url
        # NAME = values.read()         
        # New url here
        # HOME_PAGE = "https://www.sbnation.com/college-football/"    # this will be the user's selected URL
        # DOMAIN_NAME = getDomainName(HOME_PAGE)
        # # I think we should overwrite this file
        # QUEUE_FILE = NAME + "/queue.txt"
        # # This too? Not sure how this works
        # CRAWLED_FILE = NAME + "/crawled.txt"
        # NUM_OF_THREADS = 8
        # queue = Queue()
        # Spider(NAME, HOME_PAGE, DOMAIN_NAME)


        # Pass this index to spider, new searched URL
        # based on results of crawl, make new file with URLs
        # Tell eric to add to database
        # Pass URLs into second column gui from database

        # Future: Check if selected url has contained urls in database -Eric
        

        # Update database function
        break;

window.close()



create_dict()



















