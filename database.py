import json

def read_file():
    queue_file = []
    with open("sbnation\queue.txt",'r') as file:
        for line in file:
            if(line[:3] == "htt"):
                # print(line)
                queue_file.append(line)
    return queue_file

def read_selected():
    queue_file = []
    with open("selected_page\queue.txt",'r') as file:
        for line in file:
            if(line[:3] == "htt"):
                # print(line)
                queue_file.append(line)
    with open('selected_page\queue.txt','w') as file:
        file.write("")
    return queue_file

def create_database():
    dictionary = {'URL': []}
    queue_file = read_file()
    rank = "N/A"
    # print(queue_file)
    for elem in queue_file:
        rank = elem[-2:-1]
        dictionary['URL'].append({elem[0:-2] : {'contained_urls' : []}})
    write_json(dictionary,'database.JSON')

def add_contained_parent_url(parent_url):
    dictionary = {}
    with open ('database.JSON','r') as file:
        dictionary = json.load(file)
        dictionary['URL'].append({parent_url : {'contained_urls' : []}})
    append_json(dictionary)

def add_contained_urls(parent_url,sub_urls):
    print("parent url ",parent_url)
    # print(len(sub_urls))
    parent_dict = {}
    with open('database.JSON','r') as json_file_r:
        url_dict = {parent_url: {'contained_urls' : []}}
        # print("url dict" , url_dict)
        parent_dict = json.load(json_file_r)
    with open('database.JSON','w') as append_json:
        # print(len(parent_dict['URL']))
        for index in range(len(parent_dict['URL'])):
            if(parent_dict['URL'][index] == url_dict):
                # print("Hello World")
                for url in sub_urls:
                    # print(url[0:-2])
                    parent_dict['URL'][index][parent_url]['contained_urls'].append(url[0:-2])
                    # print(parent_dict['URL'][index][parent_url]['contained_urls'])
                    # print(parent_dict)
                # print(parent_dict)
                json.dump(parent_dict,append_json,indent=4)
       
def create_rank_database():
    queue_file = read_file()
    dictionary = {'URL': []}
    rank_array = {'Keyword': []}
    for elem in queue_file:
        dictionary['URL'].append({elem[0:-2] : rank_array})
    write_json(dictionary,'rank_database.JSON')

def add_rank(parent_url,keyword,rank):
    parent_dict = {}
    rank = {keyword:rank}
    with open('rank_database.JSON','r') as json_file_r:
        parent_dict = json.load(json_file_r)
        url_dict = {parent_url: {'Keyword' : []}}
        # print(url_dict, "\n", "\n")
    with open('rank_database.JSON','w') as append_json:
        for index in range(len(parent_dict['URL'])):
            # print(parent_dict['URL'][index], "\n===", "\n")
            if(parent_dict['URL'][index] == url_dict):
                parent_dict['URL'][index][parent_url]['Keyword'].append(rank)
                # print("parent dict: ", parent_dict['URL'][index][parent_url]['Keyword'] ,"\n")
                json.dump(parent_dict,append_json,indent=4)

def write_json(table_dict,file):
    with open(file,'w') as json_file:
        json.dump(table_dict,json_file,indent=4)

def append_json(dictionary):
    with open('database.JSON','a') as json_file:
        json.dump(dictionary,json_file,indent=4)

def check_contained(parent_url):
    print("===================")
    parent_dict = {}
    with open('database.JSON','r') as json_file_r:
        parent_dict = json.load(json_file_r)
        
    for index in range(len(parent_dict['URL'])):
        # print(parent_dict['URL'][index])
        for k,v in parent_dict['URL'][index].items():
            # print(k)
            if(k == parent_url):
                arr = []
                arr = parent_dict['URL'][index][parent_url]['contained_urls']
                # print(len(arr))
                if(len(arr)<=0):
                    return True
                else: 
                    return False

def getDataBaseUrls():
    with open('database.JSON','r') as file:
        dictionary = {}
        queue_array = []
        dictionary = json.load(file)
        # for index in range(len(dictionary['URL'])):
        url_list = list(dictionary['URL'])
        # print(url_list)
        for url_dict in url_list:
            for url in url_dict:
                queue_array.append(url)
                # length = len(dictionary['URL'][url_dict][url]['contained_urls'])
    #print("the array ")
    #print(queue_array)
    return queue_array


# create_database()
# create_rank_database()
# sub_urls = ["http://www.postingandtoasting.com/\n","http://www.postingandtoasting.com/\n","http://www.postingandtoasting.com/\n"]
# add_contained_urls("http://www.postingandtoasting.com/\n",sub_urls)
