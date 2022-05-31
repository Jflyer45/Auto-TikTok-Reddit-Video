from time import sleep
import os, shutil
from selenium import webdriver

class TTSMP3Page:  
    def __init__(self, driver):  
        self.driver = driver
        self.textBoxXPATH = "//textarea"
        self.downloadButton = "//input[@id='downloadenbutton']"

    def newest(self, path):
        files = os.listdir(path)
        paths = [os.path.join(path, basename) for basename in files]
        return max(paths, key=os.path.getctime)

    def setVoice(self):
        xpath = "//option[@value='Matthew']"
        self.driver.find_element_by_xpath(xpath).click()

    def clickDownload(self, fileName):
        ele = self.driver.find_element_by_xpath(self.downloadButton)
        ele.click()
        sleep(3)
        home = os.path.expanduser('~')
        path = os.path.join(home, 'Downloads')
        latest_file = self.newest(path)

        # time = 0
        # while not os.path.exists(latest_file):
        #     if time > timeout:
        #         raise Exception(f"Issue with finding narration file that was going to be named: {fileName}")
        #     sleep(1)

        new_file = os.path.join(path, fileName)
        print(latest_file)
        os.rename(latest_file, new_file)
        shutil.move(new_file, os.getcwd())
        sleep(1)

    def typeText(self, text):
        textbox = self.driver.find_element_by_xpath(self.textBoxXPATH)
        textbox.send_keys(text)

    def clearText(self):
        textbox = self.driver.find_element_by_xpath(self.textBoxXPATH)
        textbox.clear()

driver = webdriver.Chrome()
driver.get("https://ttsmp3.com/")
tts = TTSMP3Page(driver)
tts.typeText("Hello this is jeremy fischer with some test text!")
tts.setVoice()
tts.clickDownload("audio.mp3")