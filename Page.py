from fileinput import filename


class Webpage:
    def __init__(self, driver):  
        self.driver = driver
    
    def screenShotOfElement(self, element, fileName):
        screenshot_as_bytes = element.screenshot_as_png
        with open(fileName + '.png', 'wb') as f:
            f.write(screenshot_as_bytes)
    
    def screenShotOfElements(self, elements, fileName):
        i = 1
        for element in elements:
            self.screenShotOfElement(element, fileName + str(i))
            i += 1