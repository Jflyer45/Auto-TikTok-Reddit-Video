from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

def getHeadlessDriver():
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        return webdriver.Chrome(executable_path= ChromeDriverManager().install(), chrome_options=options)

def getHeadlessDriverFireFox():
        opts = webdriver.FirefoxOptions()
        opts.headless = True
        return webdriver.Firefox(options=opts)

def pageDown(driver, times):
    html = driver.find_element_by_tag_name('html')
    for i in range(0, times):
        html.send_keys(Keys.END)
        sleep(.5)