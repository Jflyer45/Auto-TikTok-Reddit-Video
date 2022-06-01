from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def getHeadlessDriver():
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
        return webdriver.Chrome(executable_path= ChromeDriverManager().install(), chrome_options=options)

def getHeadlessDriverFireFox():
        opts = webdriver.FirefoxOptions()
        opts.headless = True
        return webdriver.Firefox(options=opts)