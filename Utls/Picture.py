from importlib.resources import path
import cv2
from PIL import Image

class Picture:
    def __init__(self, path):
        self.path = path
        
    def resize(self, multiplier):
        print(f"Resizing {self.path}")
        img = cv2.imread(self.path, 1)
        img_scale_up = cv2.resize(img, (0, 0), fx=multiplier, fy=multiplier)
        cv2.imwrite(self.path, img_scale_up)

    # Where amount is a %
    def makeTransparent(self, amount):
        img = Image.open(self.path)

        img.putalpha(255*amount)  # Half alpha; alpha argument must be an int
        img.save(self.path)