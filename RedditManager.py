from lib2to3.pgen2 import driver
from os import link
from xml.dom.minidom import Element
from selenium import webdriver

def getTopOfTodayLinks(subreddit):
    extention = "top/?t=day"
    return getFromReddit(getTopOfHelper(subreddit, extention))

def getTopOfWeekLinks(subreddit):
    extention = "top/?t=week"
    return getFromReddit(getTopOfHelper(subreddit, extention))

def getTopOfMonthLinks(subreddit):
    extention = "top/?t=month"
    return getFromReddit(getTopOfHelper(subreddit, extention))

def getTopOfYearLinks(subreddit):
    extention = "top/?t=year"
    return getFromReddit(getTopOfHelper(subreddit, extention))

def getTopOfAllTimeLinks(subreddit):
    extention = "top/?t=all"
    return getFromReddit(getTopOfHelper(subreddit, extention))

def getTopOfHelper(subreddit, extention):
    base =  f"https://www.reddit.com/r/{subreddit}/"
    link = base + extention
    return link

def getFromReddit(link):
    driver = webdriver.Chrome()
    driver.get(link)

    # gets the a tag
    postsXPATH = "//h3/../../../../..//span[contains(text(), 'Posted by')]/../../../..//h3/../../../a"
    aTags = driver.find_elements_by_xpath(postsXPATH)
    postLinks = []
    for a in aTags:
        postLinks.append(""+a.get_attribute("href"))

    return postLinks