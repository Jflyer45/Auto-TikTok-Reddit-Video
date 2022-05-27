import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import *
from webdriver_manager.chrome import ChromeDriverManager

class UploadManager:  
    def __init__(self, driver):
        self.loginInfo = ["jflyer45.gaming@gmail.com", "Deltafire2952#"]

        self.driver = driver
        self.usernameBoxXPATH = "//input[@name='username']"
        self.passwordBoxXPATH = "//input[@type='password']"
        self.loginButtonXPATH = "//button[contains(text(), 'Log in')]"

    def login(self):
        # TODO if can upload button, skip this  

        passwordBox = self.driver.find_element_by_xpath(self.passwordBoxXPATH)
        passwordBox.send_keys(self.loginInfo[1])
        usernameBox = self.driver.find_element_by_xpath(self.usernameBoxXPATH)
        usernameBox.send_keys(self.loginInfo[0])
        self.driver.find_element_by_xpath(self.loginButtonXPATH).click()

    def existsElement(self, xpath):
        try:
            self.driver.find_element_by_xpath(xpath)
        except:
            return False
        return True

option = webdriver.ChromeOptions()
option.add_argument("--profile-directory=Default")
option.add_argument("--user-data-dir=C:\\Users\\Jeremy\\AppData\\Local\\Google\\Chrome\\User Data")
option.add_argument('--disable-blink-features=AutomationControlled')
option.add_argument("window-size=1920,1000")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36")
driver = webdriver.Chrome(options=option, executable_path= ChromeDriverManager().install())
driver.get('https://www.tiktok.com/login/phone-or-email/email')

# driver = webdriver.Chrome()
# driver.get("https://www.tiktok.com/login/phone-or-email/email")
um = UploadManager(driver)
sleep(10)
um.login()
sleep(5)