"""def letter_count(x):
    x.lower()
    appeared = {}
    for i in x:
        if i in appeared:
            appeared.update({i: appeared[i]+1})
        else:
            appeared[i] = 1
    return appeared

#print letter_count("mississippi")


def word_count(x):
    words = x.lower().split()
    appeared = {}
    for i in words:
        if not i.isalpha():
            i = i[:-1]
        if i in appeared:
            appeared.update({i: appeared[i]+1})
        else:
            appeared[i] = 1
    return appeared

#print word_count("Practice? We talking bout practice? Not a game! Not a game. But practice man?")"""

import datetime

starter = datetime.datetime(2015, 10, 21, 16, 29)

def time_machine(x, y):
    new = datetime.datetime(2015, 10, 21, 16, 29)
    
    if y == 'years':
        x = 365
        return starter + datetime.timedelta(days = x)
    elif y == 'days':
        return starter + datetime.timedelta(days = x)
    elif y == 'minutes':
        return starter + datetime.timedelta(minutes = x)
    elif y == 'hours':
        return starter + datetime.timedelta(hours = x)

#print(time_machine(10, 'hours'))
import re
def find_words(count, stry):
    return re.findall(r'[a-z]*{' + str(count) + ',}', stry)
    #return re.findall(r'\w{{{},}}'.format(count), stry)
    #return re.findall(r"\w{%d,}" % count, stry)

stry = 'superamazingness'
#print(re.findall(r'\w*[^nes]+', stry))

#print(find_words(5, 'hola, meamo leo gracias senora'))

import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.match(r'''
   ^(?P<last_name>[-\w ]+),\s
    (?P<first_name>[-\w ]+):\s
    (?P<score>[\d]+)$
''', string, re.X|re.M)

#print(players)
class Player:
    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score
import pdb;pdb.set_trace()
leo = Player(**players.groupdict())


