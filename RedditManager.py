from lib2to3.pgen2 import driver
from os import link
from xml.dom.minidom import Element
from selenium import webdriver

def getTopOfTodayLinks(subreddit):
    base =  f"https://www.reddit.com/r/{subreddit}"
    extention = "/top/?t=day"
    link = base + extention

    driver = webdriver.Chrome()
    driver.get(link)

    # gets the a tag
    postsXPATH = "//h3/../../../../..//span[contains(text(), 'Posted by')]/../../../..//h3/../../../a"
    aTags = driver.find_elements_by_xpath(postsXPATH)
    postLinks = []
    for a in aTags:
        postLinks.append(""+a.get_attribute("href"))

    return postLinks

links = getTopOfTodayLinks("AmItheAsshole")
