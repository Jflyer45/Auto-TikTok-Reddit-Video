import sys
from PostingManager import *

# subreddit = "AskReddit"
try:
    subreddit = str(sys.argv[1])
    if subreddit is None:
        raise Exception("Subreddit arguement required")
    print(f"Creating video for {subreddit}")

    # use logic to take the subreddit and fill in the params for createAndPost 

    link = TopOfLinkGetter(subreddit, TopOfEnum().Today)
    createAndPost(link, True, 8, True)
except Exception as e:
    with open('ERROrs.txt', 'w') as f:
        f.write("Trying to put error")
        f.write(e)
