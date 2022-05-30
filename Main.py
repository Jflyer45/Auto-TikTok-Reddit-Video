from genericpath import isfile
from re import sub
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RedditPost import RedditPost
from moviepy.editor import *
from Picture import Picture
from Manager import Manager
from TikTokUploadManager import UploadManager
from RedditManager import *
import shutil

subredditList = ["TruthOffMyChest", "AmItheAsshole"]

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

class TopOfEnum:
    def __init__(self):
        self.Today = "Today"
        self.Week = "Week"
        self.Month = "Month"
        self.Year = "Year"
        self.AllTime = "AllTime"

def createAndPost(subreddit, TopEnum=TopOfEnum().Today):
    if TopEnum == TopOfEnum().Today:
        link = getTopOfTodayLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().Week:
        link = getTopOfWeekLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().Month:
        link = getTopOfWeekLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().Year:
        link = getTopOfYearLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().AllTime:
        link = getTopOfAllTimeLinks(subreddit)[0]
    else:
        link = getTopOfTodayLinks(subreddit)[0]
    
    m = Manager()
    m.createTikTok(link)
    absolutePath = os.path.abspath(m.currentVideoPath)
    um = UploadManager()
    um.uploadVideo(absolutePath, f"{m.currentTitle} #Reddit #{subreddit}")
    # Once uploaded move video to posted folder
    m.moveToPosted()
    addToDoneVideos(link)

createAndPost("AmItheAsshole", TopOfEnum().AllTime)


# subreddit = "TrueOffMyChest"
# linkStorage = f"{subreddit}_Stories.txt"

# if not os.path.exists(linkStorage):
#     links = getTopOfTodayLinks(subreddit)
#     links = removeDoneLinks(links)
#     listToFile(links, linkStorage)
# else:
#     if isFileEmpty(linkStorage):
#         os.remove(linkStorage)
#         links = getTopOfTodayLinks(subreddit, Level().Default)
#         links = removeDoneLinks(links)
#         listToFile(links, linkStorage)
#     else:
#         links = fileToList(linkStorage)

# m = Manager()
# for link in links:
#     print(f"Now creating video for: {link}")
#     didWork = m.createTikTok(link)
#     if didWork:
#         deleteFromFile(linkStorage, link)
#         addToDoneVideos(link)
# print(f"During the operation there were: {m.errorCount} deletion problems")

#TODO sanaitize the text for text to speech, AITA -> Am i the asshole
#TODO add ability to read comments
#TODO Create a txt to store all the videos that were created before