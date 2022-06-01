import shutil
from time import sleep
import os
import glob

class TTSPage:  
    def __init__(self, driver):  
        self.driver = driver
        self.textBoxXPATH = "//textarea"

    def clickOption(self, option):
        xpath = f"//option[contains(text(), '{option}')]"
        ele = self.driver.find_element_by_xpath(xpath)
        ele.click()
    def clickMicrosoft(self):
        self.clickOption("Microsoft")
    def clickEnglish(self):
        self.clickOption("English")
    def clickDavid(self):
        self.clickOption("David")
    def clickFast(self):
        self.clickOption("fast")
    def clickFast(self):
        self.clickOption("fast")
    def clickMedium(self):
        xpath = "//option[contains(text(), 'x-fast')]/../option[contains(text(), 'medium')]"
        ele = self.driver.find_element_by_xpath(xpath)
        ele.click()
    
    # def clickDownload(self):
    #     xpath = "//i[contains(text(), 'file_download')]"
    #     ele = self.driver.find_element_by_xpath(xpath)
    #     ele.click()
    #     sleep(1)

    def clickDownload(self, fileName, timeout=10):
        xpath = "//i[contains(text(), 'file_download')]"
        ele = self.driver.find_element_by_xpath(xpath)
        ele.click()
        sleep(3)
        home = os.path.expanduser('~')
        path = os.path.join(home, 'Downloads')
        latest_file = os.path.join(path, "narration.mp3")

        time = 0
        while not os.path.exists(latest_file):
            if time > timeout:
                raise Exception(f"Issue with finding narration file that was going to be named: {fileName}")
            sleep(1)

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