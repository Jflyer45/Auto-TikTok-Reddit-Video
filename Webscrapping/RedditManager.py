from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SeleniumUtls import *


class Level:
    def __init__(self):
        self.Default = 0
        self.Low = 1
        self.Medium = 5
        self.High = 10
        self.Custom = 0

def getTopOfTodayLinks(subreddit, amount=Level().Default):
    extention = "top/?t=day"
    return getFromReddit(getTopOfHelper(subreddit, extention), amount)

def getTopOfWeekLinks(subreddit, amount=Level().Default):
    extention = "top/?t=week"
    return getFromReddit(getTopOfHelper(subreddit, extention), amount)

def getTopOfMonthLinks(subreddit, amount=Level().Default):
    extention = "top/?t=month"
    return getFromReddit(getTopOfHelper(subreddit, extention), amount)

def getTopOfYearLinks(subreddit, amount=Level().Default):
    extention = "top/?t=year"
    return getFromReddit(getTopOfHelper(subreddit, extention), amount)

def getTopOfAllTimeLinks(subreddit, amount=Level().Default):
    extention = "top/?t=all"
    return getFromReddit(getTopOfHelper(subreddit, extention), amount)

def getTopOfHelper(subreddit, extention):
    base =  f"https://www.reddit.com/r/{subreddit}/"
    link = base + extention
    return link

def pageDown(driver, times):
    html = driver.find_element_by_tag_name('html')
    for i in range(0, times):
        html.send_keys(Keys.END)
        sleep(.5)

def getFromReddit(link, amount=Level().Default):
    driver = getHeadlessDriver()
    driver.get(link)
    pageDown(driver, amount)
    # gets the a tag
    postsXPATH = "//h3/../../../../..//span[contains(text(), 'Posted by')]/../../../..//h3/../../../a"
    aTags = driver.find_elements_by_xpath(postsXPATH)
    postLinks = []
    for a in aTags:
        postLinks.append(""+a.get_attribute("href"))
    return postLinks