import json

def read_file():
    queue_file = []
    with open("sbnation\queue.txt",'r') as file:
        for line in file:
            if(line[:3] == "htt"):
                # print(line)
                queue_file.append(line)
    return queue_file

def create_dict():
    dictionary = {'URL': []}

    queue_file = read_file()
    rank = "N/A"
    # print(queue_file)
    for elem in queue_file:
        dictionary['URL'].append({elem : {'contained_urls' : []}})
    write_json(dictionary)
    
def add_contained_urls(parent_url,sub_urls):
    print(len(sub_urls))
    parent_dict = {}
    with open('database.JSON','r') as json_file_r:
        url_dict = {parent_url: {'contained_urls' : []}}
        parent_dict = json.load(json_file_r)
    with open('database.JSON','w') as append_json:
        # print(len(parent_dict['URL']))
        for index in range(len(parent_dict['URL'])):
            # print(parent_dict['URL'][index])
            if(parent_dict['URL'][index] == url_dict):
                print("Hello World")
                for url in sub_urls:
                    parent_dict['URL'][index][parent_url]['contained_urls'].append(url)
                    print(parent_dict['URL'][index][parent_url]['contained_urls'])
                    print(parent_dict)
                json.dump(parent_dict,append_json,indent=4)
        

def write_json(table_dict):
    with open('database.JSON','w') as json_file:
        json.dump(table_dict,json_file,indent=4)



create_dict()
sub_urls = ["http://www.postingandtoasting.com/\n","http://www.postingandtoasting.com/\n","http://www.postingandtoasting.com/\n"]
add_contained_urls("http://www.postingandtoasting.com/\n",sub_urls)
