doors = []
for i in range(99):
    doors.append(False)

for divider in range(99):
    for current in range(99):
        if (current + 1)%(divider + 1) == 0:
            if doors[current] == False:
                doors[current] = True
            else:
                doors[current] = False

for i in range(99):
    if doors[i] == True:
        print("Door {} is {}".format((i+1), "open"))
    else:
        print("Door {} is {}".format((i+1), "closed"))
