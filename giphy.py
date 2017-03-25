import giphypop
import random


def getgifurl(gifkeyword):
    i = random.randint(0,5+)
    g = giphypop.Giphy()
    results=[x for x in g.search(gifkeyword)]
    s = str(results[i])[-13:]

    return results[i]