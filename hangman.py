#!/bin/sh

#  python hangman.py
#  
#
#  Created by Leo Jacoby on 8/28/16.
#

import random
import string
import time

words = ["cathedral", "dinosaur", "Jupiter", "trombone", "geometry", "mountain", "Mercury", "swimming", "element", "Germany", "basketball", "migration", "identity", "energy", "inequality", "substitution", "combination", "dialogue", "rhythm", "percussion", "cashmere", "Honduras", "computer", "trophy", "sharpener"]
alphabet = string.ascii_lowercase + string.ascii_uppercase

def reset():
    global myword
    myword = random.choice(words)
    global guess
    guess = ""
    global revealed_word
    revealed_word = '_'*len(myword)
    global bad_guesses
    bad_guesses = []

def consent_check():
    time.sleep(0.7)
    consent = raw_input("Do you wanna play again? ")
    if "yes" in consent.lower() or "ya" in consent.lower() or "yeah" in consent.lower() or "yup" in consent.lower()  or "yep" in consent.lower() or "sure" in consent.lower():
        time.sleep(0.7)
        print("Great! Let's play again.")
        reset()
        main()
    elif "no" in consent.lower() or "nah" in consent.lower():
        time.sleep(0.7)
        print("Okay. It's sure been fun playing with you though!")
        quit()
    else:
        print("Sorry, I didn't get that.")
        consent_check()


def guesser():
    global guess
    guess = raw_input("Guess a letter: ")
    if guess in revealed_word or guess in bad_guesses:
        print("You've already guessed '{}'".format(guess))
        guesser()
    elif not guess.isalpha():
        print("Please guess a letter in the alphabet.")
        guesser()
    elif len(guess) != 1 and guess.lower() != "guess":
        print("Please only guess single letters.")
        guesser()
    else:
        check()


def check():
    global guess
    global revealed_word
    global bad_guesses
    if guess == "GUESS" or guess == "guess":
        time.sleep(0.7)
        big_guess = raw_input("Try and guess the whole word: ")
        if big_guess.lower() == myword.lower():
            time.sleep(0.7)
            print("You got it! My word was {}.".format(myword))
            consent_check()
        else:
            time.sleep(0.7)
            print("Sorry, that guess was incorrect.")
            time.sleep(0.7)
            print("The word was, '{}'.".format(myword))
            consent_check()


    else:
        if guess in myword.lower() or guess in myword.upper():
            time.sleep(0.7)
            print("'{}' is in my word.".format(guess))
            revealed_word = list(revealed_word)
                
            try:
                revealed_word[myword.index(guess.lower())] = myword[myword.index(guess.lower())]
                if myword.count(guess.lower()) > 1:
                    i = myword.index(guess.lower())
                    revealed_word[myword.index(guess.lower(), i + 1)] = myword[myword.index(guess.lower(), i + 1)]
            except ValueError:
                revealed_word[myword.index(guess.upper())] = myword[myword.index(guess.upper())]
                if myword.count(guess.upper()) > 1:
                    i = myword.index(guess.upper())
                    revealed_word[myword.index(guess.upper(), i + 1)] = myword[myword.index(guess.upper(), i + 1)]
            
            revealed_word = "".join(revealed_word)
        
            if '_' in revealed_word:
                time.sleep(0.7)
                print("Here is what you have:")
                print(revealed_word)
            else:
                time.sleep(0.7)
                print("You got it! My word was {}.".format(myword))
                consent_check()
    
        else:
            time.sleep(0.7)
            print("Nope.")
            bad_guesses.append(guess)
            if len(bad_guesses) == 8:
                time.sleep(0.7)
                print("Sorry, you're out of guesses.")
                time.sleep(0.7)
                print("The word was, '{}'.".format(myword))
                consent_check()
            else:
                time.sleep(0.7)
                print("You have {} more incorrect guesses left.".format(8-len(bad_guesses)))

def main():
    reset()
    print("Here is my word: {}".format(revealed_word))
    while 1:
        guesser()


print("Let's play Hangman!")
time.sleep(1.7)
print("I'll think of a random word and you try to guess letters in it.")
time.sleep(2.3)
print("If you guess 8 letters incorrectly then you lose")
time.sleep(2)
print("The more letters you guess, the closer you get to guessing the whole word.")
time.sleep(2.5)
print("If you think you know the whole word, type 'GUESS', and then guess the word.")
time.sleep(2.5)
print("Be careful though, if you guess it wrong, then you lose the game.")
time.sleep(2.3)
print("If you don't feel like trying to guess the whole word, continue guessing letters until you get them all.")
time.sleep(3.5)
print("You win once you guess the word.")
time.sleep(2)
print("Enough about the rules, let's play!")
time.sleep(2)

main()

