# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from Webscrapping.RedditPost import RedditPost
# from moviepy.editor import *
# from Utls.Picture import Picture
from Manager import Manager
# from TikTokUploadManager import UploadManager
# from Webscrapping.RedditManager import *
# from Utls.FileManager import *
# from PostingManager import *
subredditList = ["TruthOffMyChest", "AmItheAsshole"]
subredditVideoTypeDic = {"TruthOffMyChest": "TP", "AmItheAsshole": "TP", "AskReddit": "TC"}

Manager().createTikTok("https://www.reddit.com/r/AskReddit/comments/uncedt/what_rules_were_put_in_place_because_of_you/", True, 20, 90)

# NSFW
# https://www.reddit.com/r/AskReddit/comments/uxbh5a/what_were_the_conspiracy_theorists_right_about/

# createAndPost("AmItheAsshole", TopOfEnum().AllTime)

#TODO sanaitize the text for text to speech, AITA -> Am i the asshole
#TODO add ability to read comments
#TODO Create a txt to store all the videos that were created before

#TODO CALLS TO AWS should stop when we pass maxLength. It is fine to have that check in createVideo
# but we do not want waste!