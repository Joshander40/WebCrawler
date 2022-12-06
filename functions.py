import os

## Make a folder for each website populated with the URL the crawler finds
def createDirectory(directory):
    if not os.path.exists(directory):
        print("The directory for " + directory + " was created")
        os.makedirs(directory)

createDirectory("Starting Page")

## Create a queue for file and crawled files if they do not exist
def createFiles(name, startingURL):
    queue = name + "/queue.txt"
    if not os.path.isfile(queue):
        writeToFile(queue, startingURL)

    crawled = name + "/crawled.txt"
    if not os.path.isfile(crawled):
        writeToFile(crawled, "")


def writeToFile(path, data):
    file = open(path, "w")
    file.write(data)
    file.close()

createFiles("Starting Page", "https://en.wikipedia.org/wiki/American_football/")

## Add information to existing file

def addToFile(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")

## Clear file data
def deleteFileData(path):
    with open(path, "w"):
        pass


## Convert each line into a set to avoid duplicates
def fileIntoSet(name):
    fileSet = set()
    with open(name, "rt") as openFile:
        for line in openFile:
            fileSet.add(line.replace("\n", ""))
    return fileSet

## Convert set to file
def setIntoFile(URLS, file):
    deleteFileData(file)
    # print("========================================================================================================================\n")
    for URL in URLS:
        if URL is not None:
            addToFile(file, URL)


