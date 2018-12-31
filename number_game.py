#!/bin/sh

#  number_game.py
#  
#
#  Created by Leo Jacoby on 8/26/16.
#

import random
import time

num = random.randint(1, 20)
frst_guess = ""
user = 0
guesses = 0
last_guess = False

def ask():
    global guesses
    global last_guess
    
    if last_guess:
        print("Nope! That's not it.")
        print("Sorry, your out of guesses.")
        consent_check()
    if guesses == 4:
        time.sleep(1)
        print("This is your last guess.")
        time.sleep(1)
        print("Use it wisely.")
        last_guess = True
    while 1:
        frst_guess = raw_input("Take a guess: ")
        guesses += 1
        try:
            global user
            user = int(frst_guess)
            break
        except ValueError:
            print("Please guess numbers only.")
            time.sleep(1.5)

def got_it():
    time.sleep(2)
    print("Okay, I have my number.")

def consent_check():
    consent = raw_input("Do you wanna play again? ")
    if "yes" in consent.lower() or "ya" in consent.lower() or "yeah" in consent.lower() or "yup" in consent.lower()  or "yep" in consent.lower() or "sure" in consent.lower():
        time.sleep(1)
        print("Great! Let's play again.")
        got_it()
        check()
    elif "no" in consent.lower() or "nah" in consent.lower():
        time.sleep(1)
        print("Okay. It's sure been fun playing with you though!")
        time.sleep(3)
        quit()
    else:
        time.sleep(0.5)
        print("Sorry, I didn't get that.")
        consent_check()

def check():
    num = random.randint(1, 20)
    global guesses
    guesses = 0
    last_guess = False
    while 1:
        time.sleep(0.2)
        ask()
        if num == user:
            time.sleep(1)
            print("You got it! Great job.")
            time.sleep(1.5)
            consent_check()
        elif user < 1 or user > 20:
            time.sleep(1)
            print("Try guessing numbers from 1-20.")
        elif num > user:
            time.sleep(1)
            if last_guess == False:
                print("Try higher")
        else:
            time.sleep(1)
            if last_guess == False:
                print("Try lower")

def main():
    time.sleep(1.5)
    print("Let's play a game!")
    time.sleep(2)
    print("I'll think of a number 1 to 20 in my head, and then you have 5 guesses to try and guess it!")
    got_it()

    check()

main()