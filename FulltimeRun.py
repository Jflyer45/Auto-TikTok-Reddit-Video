import time
import datetime
from Webscrapping.RedditManager import *
from PostingManager import *
from TikTokUploadManager import *

schedule = {"AskReddit": datetime.time(hour=9, minute=0),
            "TruthOffMyChest": datetime.time(hour=12, minute=0),
            "AmItheAsshole": datetime.time(hour=15, minute=0),
            "YouShouldKnow": datetime.time(hour=18, minute=0)}
subredditVideoTypeDic = {"TruthOffMyChest": "TP", "AmItheAsshole": "TP", "AskReddit": "TC", "YouShouldKnow": "TP"}


print("Now wating")
print(schedule["AskReddit"])

today = datetime.datetime.now().day

print(today)

while True:
    for key in schedule.keys():
        nowTime = datetime.datetime.now()
        while datetime.time(hour=nowTime.hour, minute=nowTime.minute) < schedule[key]:
            print("Waiting")
            sleep(600)
            nowTime = datetime.datetime.now()
        
        try:
            # Waiting is now done, time to post
            link = getTopOfTodayLinks(key)[0]
            
            if subredditVideoTypeDic[key] == "TC":
                createAndPost(link, True, 8)
            else:
                createAndPost(link)
        except Exception as e:
            print("Error: " + str(e))
    while datetime.datetime.now().day == today:
        print("Waiting till tomorrow")
        sleep(60*60)
    today = datetime.datetime.now().day

# link = getTopOfTodayLinks("AskReddit")[0]
# createAndPost(link, True, 8, True)
# UploadManager().uploadVideo("test.mp4", "test test test", True)