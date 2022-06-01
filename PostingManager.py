from RedditManager import *
from Manager import *
from TikTokUploadManager import UploadManager
from FileManager import *

class TopOfEnum:
    def __init__(self):
        self.Today = "Today"
        self.Week = "Week"
        self.Month = "Month"
        self.Year = "Year"
        self.AllTime = "AllTime"

def createAndPost(subreddit, TopEnum=TopOfEnum().Today):
    if TopEnum == TopOfEnum().Today:
        link = getTopOfTodayLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().Week:
        link = getTopOfWeekLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().Month:
        link = getTopOfWeekLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().Year:
        link = getTopOfYearLinks(subreddit)[0]
    elif TopEnum == TopOfEnum().AllTime:
        link = getTopOfAllTimeLinks(subreddit)[0]
    else:
        link = getTopOfTodayLinks(subreddit)[0]
    
    m = Manager()
    m.createTikTok(link)
    absolutePath = os.path.abspath(m.currentVideoPath)
    um = UploadManager()
    um.uploadVideo(absolutePath, f"{m.currentTitle} #Reddit #{subreddit}")
    # Once uploaded move video to posted folder
    m.moveToPosted()
    addToDoneVideos(link)
