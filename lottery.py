teams = {
    "Celtics": 28,
    "Nets": 59,
    "Knicks": 48,
    "76ers": 50,
    "Raptors": 31, #4
    "Bulls": 40,
    "Cavaliers": 27,
    "Pistons": 43,
    "Pacers": 40, #8
    "Bucks": 38,
    "Hawks": 38,
    "Hornets": 43,
    "Heat": 40, #12
    "Magic": 51,
    "Wizards": 31,
    "Mavericks": 46,
    "Rockets": 25,#16
    "Grizzlies": 37,
    "Pelicans": 45,
    "Spurs": 18,
    "Nuggets": 41, #20
    "Timberwolves": 46,
    "Trailblazers": 40,
    "Thunder": 33,
    "Jazz": 30, #24
    "Warriors": 14,
    "Clippers": 31,
    "Lakers": 55,
    "Suns": 57, #28
    "Kings": 47
}

rev_teams = {
    28: "Celtics",
    59: "Nets",
    48: "Knicks",
    50: "76ers",
    31: "Raptors", #4
    40: "Bulls",
    27: "Cavaliers",
    43: "Pistons",
    40: "Pacers", #8
    38: "Bucks",
    38: "Hawks",
    43: "Hornets",
    40: "Heat", #12
    51: "Magic",
    31: "Wizards",
    46: "Mavericks",
    25: "Rockets",#16
    37: "Grizzlies",
    45: "Pelicans",
    18: "Spurs",
    41: "Nuggets", #20
    46: "Timberwolves",
    40: "Trailblazers",
    33: "Thunder",
    30: "Jazz", #24
    14: "Warriors",
    31: "Clippers",
    55: "Lakers",
    57: "Suns", #28
    47: "Kings"
}

games = [
    [teams["Bulls"], teams["76ers"]],
[teams["Nets"], teams["Magic"]],
[teams["Bucks"], teams["Pacers"]],
[teams["Wizards"], teams["Knicks"]],
[teams["Celtics"], teams["Hawks"]],
[teams["Timberwolves"], teams["Trailblazers"]],

[teams['Hawks'], teams['Cavaliers']],
[teams['Heat'], teams['Raptors']],
[teams['Knicks'], teams['Grizzlies']],
[teams['Pistons'], teams['Rockets']],
[teams['Spurs'], teams['Mavericks']],
[teams['Pelicans'], teams['Nuggets']],
[teams['Timberwolves'], teams['Jazz']],
[teams['Thunder'], teams['Suns']],
[teams['Kings'], teams['Lakers']],

[teams['Raptors'], teams['Knicks']],
[teams['Cavaliers'], teams['Raptors']],
[teams['Thunder'], teams['Nuggets']],
[teams['Mavericks'], teams['Suns']],
[teams['Rockets'], teams['Kings']],
[teams['Pistons'], teams['Grizzlies']],
[teams['Timberwolves'], teams['Lakers']],

[teams['Pacers'], teams['76ers']],
[teams['Nets'], teams['Celtics']],
[teams['Cavaliers'], teams['Heat']],
[teams['Magic'], teams['Bulls']],
[teams['Hornets'], teams['Bucks']],
[teams['Wizards'], teams['Pistons']],
[teams['Spurs'], teams['Trailblazers']],
[teams['Rockets'], teams['Clippers']],
[teams['Jazz'], teams['Warriors']],

[teams['Hornets'], teams['Hawks']],
[teams['Thunder'], teams['Timberwolves']],
[teams['Nuggets'], teams['Mavericks']],
[teams['Pelicans'], teams['Lakers']],
[teams['Suns'], teams['Kings']],

[teams['Pistons'], teams['Magic']],
[teams['Raptors'], teams['Cavaliers']],
[teams['Bucks'], teams['Celtics']],
[teams['76ers'], teams['Knicks']],
[teams['Wizards'], teams['Heat']],
[teams['Nets'], teams['Bulls']],
[teams['Grizzlies'], teams['Mavericks']],
[teams['Timberwolves'], teams['Rockets']],
[teams['Nuggets'], teams['Thunder']],
[teams["Hawks"], teams['Pacers']],
[teams['Spurs'], teams['Jazz']],
[teams['Kings'], teams['Clippers']],
[teams['Lakers'], teams['Warriors']],
[teams['Pelicans'], teams['Timberwolves']]
]

print("I am going to ask you to predict the outcome of the remaining NBA games.")
print("Respond with the number (1 or 2) that is next to the team that you believe will win.")

for game in games:
    choice = input("Will the {} (1) or the {} (2) win?  ".format(rev_teams[game[0]], rev_teams[game[1]]))

    if choice == "1":
        teams[rev_teams[game[0]]] = teams[rev_teams[game[0]]] + 1
    else:
        teams[rev_teams[game[1]]] = teams[rev_teams[game[1]]] + 1


ordered_losses = []
for i in teams.keys():
    ordered_losses.append(teams[i])

ordered_losses = sorted(ordered_losses, key=int, reverse=True)

ordered_teams_losses = []
team_names = list(teams.keys())

for loss_amount in ordered_losses:
    print(loss_amount)
    for team in team_names:
        if loss_amount == teams[team]:
            ordered_teams_losses.append([team, loss_amount])
            if team == "Lakers":
                print("The Lakers have {} losses.".format(loss_amount))
            team_names.remove(team)
            break

seed = 1
for i in ordered_teams_losses:
    i[1] = seed
    seed = seed + 1

seed_team_dict = {}

for i in ordered_teams_losses:
    seed_team_dict[i[0]] = i[1]
not_top_three_probs = [
    "X",
    0.48,
    0.54,
    0.60,
    0.67,
    0.74,
    0.80,
    0.86,
    0.90,
    0.94,
    0.96,
    0.97,
    0.98,
    0.98,
    0.98
    ]

prob = "{}%".format(not_top_three_probs[seed_team_dict["Lakers"]]*100)

print("The Lakers got the {} seed in the lottery".format(seed_team_dict["Lakers"]))
    
print("The Lakers have a {} chance of not getting a top three draft pick".format(prob))

        


    
