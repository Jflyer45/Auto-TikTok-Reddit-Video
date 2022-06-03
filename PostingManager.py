from Webscrapping.RedditManager import *
from Manager import *
from TikTokUploadManager import UploadManager
from Utls.FileManager import *

class TopOfEnum:
    def __init__(self):
        self.Today = "Today"
        self.Week = "Week"
        self.Month = "Month"
        self.Year = "Year"
        self.AllTime = "AllTime"

def TopOfLinkGetter(subreddit, TopEnum=TopOfEnum().Today):
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
    return link

def createAndPost(link, commentsMode=False, limit=5, DONOTPOST=False):    
    # Create video
    m = Manager()
    m.createTikTok(link, commentsMode=commentsMode, limit=limit)
    absolutePath = os.path.abspath(m.currentVideoPath)

    # Upload Video
    um = UploadManager()
    um.uploadVideo(absolutePath, f"{m.currentTitle} #Reddit #{m.subReddit} #jeremyreddit", DONOTPOST=DONOTPOST)

    # Once uploaded move video to posted folder
    m.moveToPosted()
    addToDoneVideos(link)

# NEEDS BREAKING UP AND REFACTORING
def makeMany(subreddit):
    linkStorage = f"{subreddit}_Stories.txt"

    if not os.path.exists(linkStorage):
        links = getTopOfTodayLinks(subreddit)
        links = removeDoneLinks(links)
        listToFile(links, linkStorage)
    else:
        if isFileEmpty(linkStorage):
            os.remove(linkStorage)
            links = getTopOfTodayLinks(subreddit, Level().Default)
            links = removeDoneLinks(links)
            listToFile(links, linkStorage)
        else:
            links = fileToList(linkStorage)

    m = Manager()
    for link in links:
        print(f"Now creating video for: {link}")
        didWork = m.createTikTok(link)
        if didWork:
            deleteFromFile(linkStorage, link)
            addToDoneVideos(link)
    print(f"During the operation there were: {m.errorCount} deletion problems")