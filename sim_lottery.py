from random import randint
from collections import Counter
from tankathon_class import Lists

#to keep track of which teams already recieved picks
seeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

recieved_picks = {}

#go through the three lottery picks
for pick in range(3):
    #will only run once except if team with a pick gets another,
    #in which case it will start over with a new random number
    while 1:
        #last_one is the sum of the odds of prior teams who didn't get the pick
        last_one = 0

        rand_num = randint(0, 1000)

        #runs through each team and checks if they got pick
        for team in Lists.seed_odds:
            #if team gets pick
            if rand_num <= last_one + team:
                    #if team already has one
                    if Lists.seed_odds.index(team) + 1 not in seeds:
                        #get out of for loop and try again with a new rand_num
                        break

                    #give them the pick and take them out of list of seeds who haven't gotten a pick
                    recieved_picks[Lists.seed_odds.index(team)+1] = pick+1
                    seeds.remove(Lists.seed_odds.index(team)+1)
                    break
            else:
                #increase last_one by the teams odds at that pick
                last_one += team
            
        #if necessary because team would get 2 picks, restarts loop which generates a new rand_num
        if len(recieved_picks) == pick + 1:
            break
        else:
            continue
        
#assign picks to remaining 11 teams
for pick, seed in zip(range(4, 15), seeds):
    recieved_picks[seed] = pick


team_pick_dict = {}
#assign team names to seeds
for team in Lists.current_seeding:
    team_pick_dict[team] = recieved_picks[Lists.current_seeding.index(team)+1]


#order picks in a list rather than a dictionary
draft = []

for order in range(15):
    for team in team_pick_dict:
        if team_pick_dict[team] == order:
            draft.append(str(team))


#If the Lakers fall out of the top 3 ==> Sixers get pick
if draft.index("Lakers") > 2:
    draft[draft.index("Lakers")] = "Lakers -> *76ers*"

#Celtics get Nets pick;  Kings get Pelicans pick  (both unconditional)
draft[draft.index("Nets")] = "Nets -> Celtics"
draft[draft.index("Pelicans")] = "Pelicans -> Kings"


#If the Kings get a better pick than the Sixers ==> pick swap
if draft.index("*76ers*") > draft.index("Kings"):
    draft[draft.index("*76ers*")] = "76ers -> Kings"
    draft[draft.index("Kings")] = "Kings -> *76ers*"

#print results
for pick, team in zip(range(1, 15), draft):
    if pick < 10:
        print(str(pick) + "   " + team)
    else:
        print(str(pick) + "  " + team)

