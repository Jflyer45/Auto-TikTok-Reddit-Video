import imp
from turtle import pos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from RedditPost import RedditPost
import io; from PIL import Image; 

driver = webdriver.Chrome()
driver.get("https://www.reddit.com/r/AmItheAsshole/comments/uvwzoj/aita_for_disinviting_my_siblings_from_my_wedding/")

post = RedditPost(driver)
print(post.getParagraphs())
post.screenShotTitle("Jeremy")

driver.close()