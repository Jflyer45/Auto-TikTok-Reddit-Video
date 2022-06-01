import os, shutil

def listToFile(list, fileName):
    with open(fileName, 'w') as fp:
        for i in range(0, len(list)):
            if i != len(list)-1:
                fp.write("%s\n" % list[i])
            else:
                fp.write("%s" % list[i])

def fileToList(file):
    list2 = []
    with open(file, 'r') as fp:
        for line in fp:
            # remove linebreak from a current name
            # linebreak is the last character of each line
            x = line[:-1]

            # add current item to the list
            list2.append(x)
    return list2

def deleteFromFile(file, item):
    links = fileToList(file)
    links.remove(item)
    listToFile(links, file)

def isFileEmpty(file):
    return os.path.getsize(file) == 0

def addToDoneVideos(link):
    links = fileToList("doneVideos.txt")
    links.append(link)
    listToFile(links, "doneVideos.txt")

def removeDoneLinks(links):
    doneLinks = fileToList("doneVideos.txt")
    finalList = []
    for link in links:
        if link not in doneLinks:
            finalList.append(link)
    return finalList