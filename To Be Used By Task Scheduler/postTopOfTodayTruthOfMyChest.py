import sys
sys.path.append('../Auto-TikTok-Reddit-Video')
from PostingManager import * 

link = TopOfLinkGetter("TruthOffMyChest", TopOfEnum().Today)
createAndPost(link)