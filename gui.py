import PySimpleGUI as GUI
import json

table_array = []

def gui():

    headings = ["url"]

# Read the values from the json file
    # The json file is set up as init""" cralwed[]
    



    # with open("sbnation\queue.txt",'r') as file:
    #     for line in file:
    #         if(line[:3] == "htt"):

    #             # These 3 lines have to stay together. This is what creates a full list. List must = [ [] [] [] [] [] [] ] not [[]]

    #             queue_array = []
    #             # print(line)
    #             # print(line)
    #             queue_array.append(line)
    #             table_array.append(queue_array)


    # print(queue_array)
    with open('database.JSON','r') as file:
        queue_array = []
        dictionary = {}
        dictionary = json.load(file)
        # for index in range(len(dictionary['URL'])):
        url_list = list(dictionary['URL'])
        for url_dict in url_list:
            for url in url_dict:
                # These 3 lines have to stay together. This is what creates a full list. List must = [ [] [] [] [] [] [] ] not [[]]
                queue_array = []
                queue_array.append(url)
                table_array.append(queue_array)



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

    layout = [ 
        [
        GUI.Column(layout_url),
        GUI.VSeparator(),
        GUI.Column(layout_picked_url)
        ]

    ]

    window = GUI.Window("Test",layout)

    while True:
        event, values = window.read()

        if event == "OK" or event == GUI.WIN_CLOSED:
            break

    window.close()

# def write_json(arr):

gui()