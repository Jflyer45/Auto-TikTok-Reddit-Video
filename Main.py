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
from FileManager import *
from PostingManager import *

subredditList = ["TruthOffMyChest", "AmItheAsshole"]

# Manager().createTikTok("https://www.reddit.com/r/tifu/comments/uwtkqz/tifu_by_sending_a_call_from_the_international/")


# createAndPost("AmItheAsshole", TopOfEnum().AllTime)

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