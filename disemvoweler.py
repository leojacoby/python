#!/bin/sh

#  disemvoweler.py
#  
#
#  Created by Leo Jacoby on 9/9/16.
#

subjects = ["Geometry, Physics, Spanish, Roots, English, Music and Performance"]
vowels = list('aeiou')

def no_vowels():
    global subjects
    
    for word in subjects:
        word = list(word)
        for vowel in vowels:
            while 1:
                try:
                    word.remove(vowel)
                except:
                    subjects.remove(word)
                    break
        
        
    subjects.append(''.join(word))
    return subjects

for i in no_vowels():
    print i