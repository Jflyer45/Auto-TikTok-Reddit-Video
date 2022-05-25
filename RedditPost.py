from Page import Webpage
class RedditPost(Webpage):
    
    def __init__(self, driver):  
        self.driver = driver
        self.titleXPATH = "//div[@data-test-id='post-content']//h1"   

    def getTitle(self):
        element = self.driver.find_element_by_xpath(self.titleXPATH)
        return element.text

    def getParagraphs(self):
        paraXPATH = "//div[@data-test-id='post-content']//p"
        elements = self.driver.find_elements_by_xpath(paraXPATH)
        p = []
        for e in elements:
            p.append(e.text)
        return p

    def screenShotTitle(self, fileName):
        element = self.driver.find_element_by_xpath(self.titleXPATH)
        self.screenShotOfElement(element, fileName)

    def getCommentsElements(self):
        xpath = "//div[@id='AppRouter-main-content']/div[@tabindex='-1']/div/div[2]/div[5]/div/div/div"
        self.driver.find_elements_by_xpath(xpath)
