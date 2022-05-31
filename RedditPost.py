from PIL import Image
from Page import Webpage
class RedditPost(Webpage):
    
    def __init__(self, driver):  
        self.driver = driver
        self.titleXPATH = "//div[@data-test-id='post-content']//h1"
        self.paragraphXPATH = "//div[@data-test-id='post-content']//p"
        self.awardsXPATH = "//div[@data-test-id='post-content']//span[contains(text(), 'Posted')]/../../.."   
        self.upvotesXPATH = "//div[@data-test-id='post-content']//i[contains(@class, 'icon-upvote')]/../../../.."

    def getTitle(self):
        element = self.driver.find_element_by_xpath(self.titleXPATH)
        return element.text

    def getParagraphs(self):
        elements = self.driver.find_elements_by_xpath(self.paragraphXPATH)
        p = []
        for e in elements:
            p.append(e.text)
        return p

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
