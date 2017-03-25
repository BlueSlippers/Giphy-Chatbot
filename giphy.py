import giphypop      #giphypop is a class that accesses the giphy api
import random


def getgifurl(gifkeyword):      #takes in the key word and returns the url of the related gif
    i = random.randint(0,5)
    g = giphypop.Giphy()
    results=[x for x in g.search(gifkeyword)]     #creates a list of
    t = str(results[i])       #taking a random gif in the given list
    n = t.find('-')
    while True:                 #finding the id of gif
        if t.find('-',n+1)==-1:
            break
        n = t.find('-',n+1)
    length = len(t)
    url = "https://media.giphy.com/media/"+t[n-length+1:]+"/giphy.gif"
    return url