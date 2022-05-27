from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RedditPost import RedditPost
from moviepy.editor import *
from Picture import Picture
from Manager import Manager
from RedditManager import *

def listToFile(list):
    with open('stories.txt', 'w') as fp:
        for item in list:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Done')

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

links = getTopOfAllTimeLinks("AmItheAsshole")
# print(links)
# listToFile(links)
# list2 = fileToList("stories.txt")

# print(list2)
m = Manager()
for link in links:
    print(f"Now creating video for: {link}")
    m.createTikTok(link)
print(f"During the operation there were: {m.errorCount} deletion problems")

#TODO sanaitize the text for text to speech, AITA -> Am i the asshole
#TODO add ability to read comments