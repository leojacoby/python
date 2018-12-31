#!/bin/sh

#  num_guesser.py
#  
#
#  Created by Leo Jacoby on 8/26/16.
#

import time
high = 20
low = 1


def main():
    print("Let's play a game.")
    time.sleep(1)
    print("Think of a number 1-20 in your head and then I'll try to guess it")
    time.sleep(2.5)
    consent_check()
    time.sleep(1.5)
    guess()


def guess():
    global guess
    while 1:
        guess = int(low + (high - low)/2)
        time.sleep(1.5)
        print("I guess {}.".format(guess))
        if feedback():
            return True
            break


def feedback():
    global high
    global low
    while 1:
        response = raw_input("Type 'higher', 'lower', or 'correct': ")
        if 'higher' in response.lower():
            low = guess + 1
            break
        elif 'lower' in response.lower():
            high = guess - 1
            break
        elif 'correct' in response.lower():
            print("Yay, I got it!")
            return True
            break
    return False


def consent_check():
    consent = raw_input("You ready? ")
    if "yes" in consent.lower() or "ya" in consent.lower() or "yeah" in consent.lower() or "yup" in consent.lower()  or "yep" in consent.lower() or "sure" in consent.lower():
        print("okay...")
        return True
    elif "no" in consent.lower() or "nah" in consent.lower():
        print("Okay. Let me know when you are")
        consent_check()
    else:
        print("Sorry, I didn't get that.")
        consent_check()



main()



