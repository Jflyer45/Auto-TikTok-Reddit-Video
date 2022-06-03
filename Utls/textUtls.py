from cleantext import clean

#TODO replace words with alternitives

replacementDic = {
    "fuck": "frick"
}

def sanitize(text):
    return clean(text, no_emoji=True, no_urls=True)

def sanitizeList(textList):
    sanList = []
    for text in textList:
        sanList.append(sanitize(text))
    return sanList