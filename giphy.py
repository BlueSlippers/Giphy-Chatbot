import giphypop
import random


def getgifurl(gifkeyword):
    i = random.randint(0,5)
    g = giphypop.Giphy()
    results=[x for x in g.search(gifkeyword)]
    t = str(results[i])
    n = t.find('-')
    while True:
        if t.find('-',n+1)==-1:
            break
        n = t.find('-',n+1)
    length = len(t)
    url = "https://media.giphy.com/media/"+t[:n-length+1]+"/giphy.gif"
    return url