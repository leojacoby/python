class Lists:

    #list of 14 dictionaries; each corresponds to a seed; key = pick, value = odds
    seed_odds = [
        250,
        199,
        156,
        104,
        103,
        63,
        36,
        35,
        17,
        11,
        8,
        7,
        6,
        5
        ]

    #Current tankathon seeding (worst is #1)
    current_seeding = [
        "Nets",
        "Suns",
        "Lakers",
        "*76ers*",
        "Magic",
        "Timberwolves",
        "Knicks",
        "Kings",
        "Mavericks",
        "Pelicans",
        "Pistons",
        "Hornets",
        "Nuggets",
        "Pacers"
        ]

    def __init__(seed_odds, name):
        self.seed_odds = seed_odds
        self.current_seeding = current_seeding

