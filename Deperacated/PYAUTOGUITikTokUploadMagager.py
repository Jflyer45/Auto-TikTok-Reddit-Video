from time import sleep
import pyautogui, os

imageFolder = os.getcwd() +  "\\Pyautogui"
# searchbar = pyautogui.screenshot(imageFolder + "searchbar.png")
# upload = pyautogui.screenshot(imageFolder + "upload.png")
# caption = pyautogui.screenshot(imageFolder + "caption.png")
# scheduleButton = pyautogui.screenshot(imageFolder + "schedule.png")

def getToUploadPage():
    pyautogui.press("win")
    sleep(3)

    searchbar = pyautogui.screenshot(imageFolder + "searchbar.png")
    locateAndClick(searchbar)
    pyautogui.typewrite("tiktok")
    pyautogui.press("enter")
    sleep(10)
    # pyautogui.click(x=2266, y=66)
    upload = pyautogui.screenshot(imageFolder + "upload.png")
    location = pyautogui.locateOnScreen(upload, grayscale = True, confidence=.8)
    pyautogui.moveTo(pyautogui.center(location))
    # locateAndClick(upload)
    # pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(upload, confidence=.8)))

def typeCaption(text):
    if len(text) > 150:
        raise Exception("Caption is too large")
    else:
        caption = pyautogui.screenshot(imageFolder + "caption.png")
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(caption, confidence=.8)))
        pyautogui.typewrite(text)

def setSchedule(time):
    scheduleButton = pyautogui.screenshot(imageFolder + "schedule.png")
    pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(scheduleButton, confidence=.8)))

def locateAndClick(pic):
    r = pyautogui.locateOnScreen(pic, grayscale = True)
    con = 1
    while r is None:
        r = pyautogui.locateOnScreen(pic, grayscale = True, confidence=con)
        con -= .01
    pyautogui.click(pyautogui.center(r))
    print(f"To find: {pic}, need confidence: {con}")

# getToUploadPage()
print("now typing caption")
typeCaption("Lol!")
setSchedule("hmm")
# pyautogui.screenshot('num7_.png', region=(260,360, 110, 100))