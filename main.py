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
    if event =="-SEARCH-":
        print(table_array[values['-TABLE-']])
        # Pass in a new URL for crawling and overwrite the file

        # # new name. Probably the url
        # NAME = values.read()
        # # New url here
        # HOME_PAGE = "https://www.sbnation.com/college-football/"
        # DOMAIN_NAME = getDomainName(HOME_PAGE)
        # # I think we should overwrite this file
        # QUEUE_FILE = NAME + "/queue.txt"
        # # This too? Not sure how this works
        # CRAWLED_FILE = NAME + "/crawled.txt"
        # NUM_OF_THREADS = 8
        # queue = Queue()
        # Spider(NAME, HOME_PAGE, DOMAIN_NAME)

        # Update database function
        break;

window.close()



create_dict()



















