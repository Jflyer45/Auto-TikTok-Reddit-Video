from importlib.resources import path
from pickle import FALSE
from random import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import *
from webdriver_manager.chrome import ChromeDriverManager

class UploadManager:  
    def __init__(self):
        self.loginInfo = ["jeremyreddit", "Deltafire2952#"]

        self.driver = None
        self.usernameBoxXPATH = "//input[@name='email']"
        self.passwordBoxXPATH = "//input[@type='password']"
        self.loginButtonXPATH = "//button[contains(text(), 'Log in')]"
        self.uploadURL = "https://www.tiktok.com/upload?lang=en"

    def login(self):
        # TODO if can upload button, skip this  

        passwordBox = self.driver.find_element_by_xpath(self.passwordBoxXPATH)
        # passwordBox.send_keys(self.loginInfo[1])
        self.slowType(passwordBox, self.loginInfo[1])
        usernameBox = self.driver.find_element_by_xpath(self.usernameBoxXPATH)
        sleep(1)
        self.slowType(usernameBox, self.loginInfo[0])
        # usernameBox.send_keys(self.loginInfo[0])
        self.driver.find_element_by_xpath(self.loginButtonXPATH).click()

    def existsElement(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True
    
    def slowType(self, el, text):
        for character in text:
            el.send_keys(character)
            sleep(.3) # pause for 0.3 seconds

    def typeCaption(self, text):
        xpath = "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']"
        captionBox = self.driver.find_element_by_xpath(xpath)
        self.slowType(captionBox, text)
    
    def clickPost(self):
        xpath = "//div[contains(text(), 'Post')]"
        self.driver.find_element_by_xpath(xpath).click()

    def selectFile(self, filePath):
        xpath = "//input[@type='file']"
        self.driver.find_element_by_xpath(xpath).send_keys(filePath)

    def waitTillDoneUploading(self):
        xpath = "//div[contains(text(), 'Change video')]"
        times = 0
        while not self.existsElement(xpath):
            if times == 20:
                raise Exception("Could not upload video!")
            sleep(5)
            times += 1

    def uploadVideo(self, videoPath, caption, DONOTPOST=False):
        option = webdriver.ChromeOptions()
        option.add_argument("--profile-directory=Default")
        option.add_argument("--user-data-dir=C:\\Users\\Jeremy\\AppData\\Local\\Google\\Chrome\\User Data")
        option.add_argument('--disable-blink-features=AutomationControlled')
        option.add_argument("window-size=1920,1000")
        option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
        self.driver = webdriver.Chrome(options=option, executable_path= ChromeDriverManager().install())
        self.driver.get('https://www.tiktok.com/upload?lang=en')
        sleep(3)

        iframe = self.driver.find_element_by_xpath("//iframe")
        self.driver.switch_to.frame(iframe)

        self.typeCaption(caption)
        self.selectFile(videoPath)
        self.waitTillDoneUploading()
        if not DONOTPOST:
            self.clickPost()
        sleep(5)

# option = webdriver.ChromeOptions()
# option.add_argument("--profile-directory=Default")
# option.add_argument("--user-data-dir=C:\\Users\\Jeremy\\AppData\\Local\\Google\\Chrome\\User Data")
# option.add_argument('--disable-blink-features=AutomationControlled')
# option.add_argument("window-size=1920,1000")
# option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
# driver = webdriver.Chrome(options=option, executable_path= ChromeDriverManager().install())
# driver.get('https://www.tiktok.com/upload?lang=en')
# # driver.get('https://www.tiktok.com/login/phone-or-email/email')
# # driver = webdriver.Chrome()
# sleep(3)
# um = UploadManager(driver)

# iframe = driver.find_element_by_xpath("//iframe")

# driver.switch_to.frame(iframe)

# um.typeCaption("I secretly set up an emergency fund from my friend’s money he owed me #Reddit #TruthOffMyChest")
# path = r"C:\Users\Jeremy\Documents\GitHub\Auto-TikTok-Reddit-Video\Final_Videos\I secretly set up an emergency fund from my friend’s money he owed me.mp4"
# um.selectFile(path)
# um.waitTillDoneUploading()
# um.clickPost()
# sleep(10)
