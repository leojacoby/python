import datetime
#https://en.wikipedia.org/wiki/November_5

def wiki(x):
    date = datetime.datetime.strptime(x, '%m/%d')
    return date.strftime('https://en.wikipedia.org/wiki/%B_%d')

printwiki('9/11')
