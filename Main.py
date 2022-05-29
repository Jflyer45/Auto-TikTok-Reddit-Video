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

def deleteFromFile(file, item):
    items = fileToList(file)
    index = -1
    for i in range(0, len(items)):
        if items[i] == item:
            index = i
    with open(file, 'r') as fr:
        # reading line by line
        lines = fr.readlines()
         
        # pointer for position
        ptr = 1
     
        # opening in writing mode
        with open('stories.txt', 'w') as fp:
            for itemm in list:
                # write each item on a new line
                fp.write("%s\n" % itemm)

links = getTopOfAllTimeLinks("AmItheAsshole")
print(links)
listToFile(links)
list2 = fileToList("stories.txt")

deleteFromFile("stories.txt", "https://www.reddit.com/r/AmItheAsshole/comments/ocx94s/aita_for_telling_my_wife_the_lock_on_my_daughters/")
deleteFromFile("stories.txt", "https://www.reddit.com/r/AmItheAsshole/comments/d6xoro/meta_this_sub_is_moving_towards_a_value_system/")
deleteFromFile("stories.txt", "https://www.reddit.com/r/AmItheAsshole/comments/hvcvtt/aita_for_switching_to_regular_milk_to_prove_my/")


# print(list2)
# m = Manager()
# m.createTikTok("https://www.reddit.com/r/TrueOffMyChest/comments/qld4ns/six_years_ago_i_switched_my_wifes_cat_with_a_more/")
# for link in links:
#     print(f"Now creating video for: {link}")
#     m.createTikTok(link)
# print(f"During the operation there were: {m.errorCount} deletion problems")

#TODO sanaitize the text for text to speech, AITA -> Am i the asshole
#TODO add ability to read comments