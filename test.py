from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from TTSPage import TTSPage

driver = webdriver.Chrome()
driver.get("https://ttstool.com/")

page = TTSPage(driver)
page.clickMicrosoft()
page.clickEnglish()
page.clickDavid()

###
page.typeText("Hello world!")
page.clickDownload("audio1.mp3")
page.clearText()

page.typeText("Hello world! This si here jeremy hello")
page.clickDownload("audio2.mp3")
page.clearText()

page.typeText(" world! this is that")
page.clickDownload("audio3.mp3")
page.clearText()

driver.close()

