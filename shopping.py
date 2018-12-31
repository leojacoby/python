#!/bin/sh

#  shopping.py
#  
#
#  Created by Leo Jacoby on 8/21/16.
#


shopping = []

def helper():
    print("""Add items to the list.
    Seperate each item with a comma.
    Type 'SHOW' to see your current list.
    When you are done, type 'DONE' in all caps.
    If you are confused about any of these comands, type 'HELP'.\n""")


def shower():
    count = 1
    for i in shopping:
        print("{}: {}".format(count, i))
        count += 1
            
def adder(x):
    shopping.append(x)
    print("You added {} to your list, which now has {} items.".format(x, len(shopping)))

helper()

while 1:
    current = raw_input("> ")
    
    if current == "DONE":
        print("Here's your list:")
        shower()
        break
    elif current == "SHOW":
        shower()
        continue
    elif current == "HELP":
        helper()
        continue
    else:
        new = current.split(',')
        try:
            index = raw_input("Add this at at a certain spot? Press enter for the end of the list, or give me a number. Currently {} items in list. ".format(len(shopping)))
        except ValueError:
            
        if index:
            spot = int(index) - 1
            for item in new:
                shopping.insert(spot, item.strip())
                spot += 1
        else:
            for item in new:
                shopping.append(item.strip())



