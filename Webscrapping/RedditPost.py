import sys
from unicodedata import name
sys.path.append('../Auto-TikTok-Reddit-Video/Webscrapping')
from PIL import Image
from Page import Webpage
from selenium import webdriver

# class Comment(Webpage):
#     def __init__(self, element): 
#         self.element = element
#         self.username = self.element.find_elements_by_xpath("/div[1]").text
#         self.paragraphs = self.element.find_elements_by_xpath("//p").text

#         def getCommentsFullText(self):
#             fullPara = ""
#             for para in self.paragraphs:
#                 fullPara += para + " \n"
#             return fullPara


class RedditPost(Webpage):
    def __init__(self, driver):  
        self.driver = driver
        self.titleXPATH = "//div[@data-test-id='post-content']//h1"
        self.paragraphXPATH = "//div[@data-test-id='post-content']//p"
        self.awardsXPATH = "//div[@data-test-id='post-content']//span[contains(text(), 'Posted')]/../../.."   
        self.upvotesXPATH = "//div[@data-test-id='post-content']//i[contains(@class, 'icon-upvote')]/../../../.."
        self.commentsXPATH = "//span[contains(text(), 'level 1')]/..//div[@data-testid='comment']"
        self.wholeCommentXPATH = "//span[contains(text(), 'level 1')]/.."

    # def getComments(self):
    #     elements = self.driver.find_elements_by_xpath(self.commentsXPATH)
    #     comments = []
    #     for e in elements:
    #         print(e)
    #         comments.append(Comment(e))
    #         print(Comment(e).username)
    #         print(Comment(e).paragraphs)
    #     return comments

    def getTitle(self):
        element = self.driver.find_element_by_xpath(self.titleXPATH)
        return element.text

    def getParagraphs(self):
        elements = self.driver.find_elements_by_xpath(self.paragraphXPATH)
        p = []
        for e in elements:
            p.append(e.text)
        return p

    def getCommentsParagraphs(self, limit=5):
        elements = self.driver.find_elements_by_xpath(self.commentsXPATH)
        comments = []
        i = 0
        for element in elements:
            if i == limit:
                break
            paragraphs = []
            paragraphElements = element.find_elements_by_xpath("./div/p")
            for pe in paragraphElements:
                paragraphs.append(pe.text)
            comments.append(paragraphs)
            i += 1
        return comments

    def getCommentsFullText(self, limit=5):
        comments = self.getCommentsParagraphs(limit)
        completeComments = []
        for comment in comments:
            fullPara = ""
            for para in comment:
                fullPara += para + " "
            completeComments.append(fullPara + "\n")
        return completeComments

    def getUsernames(self):
        xpath = "//span[contains(text(), 'level 1')]/../div[1]"
        names = []
        elements = self.driver.find_elements_by_xpath(xpath)
        for e in elements:
            names.append(e.text)
        return names

    def screenShotTitle(self):
        element = self.driver.find_element_by_xpath(self.titleXPATH)
        self.screenShotOfElement(element, "Title")

    def screenShotAwards(self):
        element = self.driver.find_element_by_xpath(self.awardsXPATH)
        self.screenShotOfElement(element, "Award")

    def screenShotUpvotes(self):
        element = self.driver.find_element_by_xpath(self.upvotesXPATH)
        self.screenShotOfElement(element, "Upvotes")

    def screenShotOfParagraphs(self):
        elements = self.driver.find_elements_by_xpath(self.paragraphXPATH)
        self.screenShotOfElements(elements, "Paragraph")
    
    def screenShotOfComments(self, limit=5):
        comments = self.driver.find_elements_by_xpath(self.wholeCommentXPATH)
        if len(comments) > limit:
            shortenList = []
            for i in range(0, limit):
                shortenList.append(comments[i])
            comments = shortenList
        self.screenShotOfElements(comments, "Comment")

# driver = webdriver.Chrome()
# driver.get("https://www.reddit.com/r/AskReddit/comments/v4euvx/serious_what_do_you_think_is_the_creepiestmost/")

# rp = RedditPost(driver)
# cs = rp.getComments()
# print("done")