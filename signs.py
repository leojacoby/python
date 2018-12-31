import random
import time

abbrv_dict = {
    "NO": "Nothing",
    "S3": "Sac 3",
    "S5": "Sac 5",
    "BH": "Bunt for a hit",
    "BR": "Bunt and run",
    "SS": "Safety squeeze",
    "SL": "Slash",
    "SR": "Slash and run",
    "FB": "Fake bunt steal",
    "HR": "Hit and run",
    "TK": "Take",
    "ST": "Steal",
    "ES": "Early steal",
    "DS": "Delay steal",
    "EX": "Extended lead"
    }

correct = 0
terms = len(abbrv_dict)
while True:
    if not abbrv_dict:
        time.sleep(1)
        print("Thats all of 'em!")
        time.sleep(0.5)
        print("You answered {}/{} questions correctly.".format(correct, terms))
        if correct/terms >= 0.92:
            time.sleep(0.5)
            print("atta babe")
        else if correct/terms < 0.92 and correct/terms >= 0.8:
            print("developmental team material")
        else:
            print("you're cut! (even at branson)")
        break
    abbrv = random.choice(list(abbrv_dict.keys()))
    answer = input(abbrv + ': ')
    if answer.lower() == abbrv_dict[abbrv].lower():
        print("correct")
        correct = correct + 1
    else:
        print("incorrect")
        print('the correct answer was "{}"'.format(abbrv_dict[abbrv]))

    abbrv_dict.pop(abbrv, 0)
    
