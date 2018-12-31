#!/usr/bin/env python3
print("start")
import datetime
from collections import Counter

import mlbgame
from mlbgame.game import GameScoreboard
from pymongo import MongoClient
client = MongoClient("mongodb://leojacoby:ttp@ds123050.mlab.com:23050/ovodb")
db = client.ovodb
players = db.players_2017
print(players);

def data_storage():
    print("data_storage")
    '''Iterate through each player's statistics from each game
        from each day in the 2016 regular season and add them to the db'''
##    season = [mlbgame.day(2016, 4, 3, home='Pirates') +
##              mlbgame.day(2016, 4, 3, home='Rays') +
##              mlbgame.day(2016, 4, 3, home='Royals')] + \
##             mlbgame.games(2016, [4], list(range(4, 31))) + \
    season = mlbgame.games(2018, [5, 6, 7, 8, 9], list(range(1, 32))) + \
               mlbgame.games(2018, [10], [1, 2])

    for day in season:
        print('in day')
        for game in day:
            print('in game')
            if game.w_team:
                stats = mlbgame.player_stats(game.game_id)
                for player in (stats['home_batting'] + stats['away_batting']):
                    ## all players in each game
                    player_pa = player.ab + player.bb + player.sac + player.sf + player.hbp
                    ## check for any plate appearances
                    if player_pa:
                        player_in_db = players.find_one({"_id": player.id})
                        ## will be false if player has not yet been added to db
                        if player_in_db:
                            ## update player in db
                            updated_player = players.update_one({
                                    "_id": player.id
                                }, {'$inc': {
                                    "pa": player_pa,
                                    "ab": player.ab,
                                    "h": player.h,
                                    "bb": player.bb,
                                    "hr": player.hr,
                                    "tb": (player.hr * 4) + (player.t * 3) + (player.d * 2) + (player.h-player.hr-player.t-player.d),
                                    "rbi": player.rbi,
                                    "r": player.r,
                                    "hbp": player.hbp,
                                    "so": player.so,
                                    "sb": player.sb,
                                    "cs": player.cs,
                                    "sac": player.sac + player.sf
                                }})
                        else:
                            ## add player to db
                            new_player = players.insert_one({
                                    "_id": player.id,
                                    "name": player.name_display_first_last,
                                    "position": player.pos,
                                    "pa": player.ab + player.bb + player.sac + player.sf + player.hbp,
                                    "ab": player.ab,
                                    "h": player.h,
                                    "bb": player.bb,
                                    "hr": player.hr,
                                    "tb": (player.hr * 4) + (player.t * 3) + (player.d * 2) + (player.h-player.hr-player.t-player.d),
                                    "rbi": player.rbi,
                                    "r": player.r,
                                    "hbp": player.hbp,
                                    "so": player.so,
                                    "sb": player.sb,
                                    "cs": player.cs,
                                    "sac": player.sac + player.sf
                                })


if __name__ == '__main__':
    data_storage()
