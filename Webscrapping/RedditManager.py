from time import sleep
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