# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from Webscrapping.RedditPost import RedditPost
# from moviepy.editor import *
# from Utls.Picture import Picture
from Manager import Manager
from PostingManager import *
from TikTokUploadManager import UploadManager
# from Webscrapping.RedditManager import *
# from Utls.FileManager import *
# from PostingManager import *
subredditList = ["TruthOffMyChest", "AmItheAsshole"]
subredditVideoTypeDic = {"TruthOffMyChest": "TP", "AmItheAsshole": "TP", "AskReddit": "TC"}

# link = getTopOfTodayLinks("AmItheAsshole")[0]
# createAndPost(link, DONOTPOST=True)

Manager().createTikTok("https://www.reddit.com/r/AmItheAsshole/comments/v5r6pf/aita_for_getting_upset_and_telling_my_dad_his/", maxLength=180)

# UploadManager().uploadVideo("C:\\Users\\Jeremy\\Documents\\GitHub\Auto-TikTok-Reddit-Video\\Final_Videos\\what moment made you say yep, i'm definitely dead, but survived with no major injuries.mp4",
# "Hello World")

# Manager().createVideo(["Title.png", "Comment2.png", "Comment3.png", "Comment4.png"], ["audio1.mp3", "audio2.mp3", "audio3.mp3", "audio4.mp3"], "AHHH.mp3")

# NSFW
# https://www.reddit.com/r/AskReddit/comments/uxbh5a/what_were_the_conspiracy_theorists_right_about/

# Short
# "https://www.reddit.com/r/TrueOffMyChest/comments/v3gs5i/i_paid_off_my_credit_cards/"

# createAndPost("AmItheAsshole", TopOfEnum().AllTime)

#TODO sanaitize the text for text to speech, AITA -> Am i the asshole

#TODO CALLS TO AWS should stop when we pass maxLength. It is fine to have that check in createVideo
# but we do not want waste!