from turtle import pos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RedditPost import RedditPost
from moviepy.editor import *
from Picture import Picture
from Manager import Manager

m = Manager()
link = "https://www.reddit.com/r/AmItheAsshole/comments/awyi8k/aita_for_despising_my_mentally_handicap_sister/"
m.createTikTok(link)


#TODO sanaitize the text for text to speech, AITA -> Am i the asshole
#TODO add ability to read comments