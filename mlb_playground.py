import datetime
import mlbgame

game = mlbgame.day(2016, 4, 11, home="Cubs")[0]
new_date = game.date.replace(hour=0, minute=0)
stats = mlbgame.player_stats(game.game_id)

season_hr = 0

#import pdb; pdb.set_trace()
while 1:
    stats = mlbgame.player_stats(game.game_id)
    for i in stats['home_batting']:
        if i.name_display_first_last == "Kris Bryant":
            if i.hr:
                season_hr += i.hr
            break
    if new_date == datetime.datetime(2016, 9, 25):
        break

    try:
        game = mlbgame.day(new_date.year, new_date.month, new_date.day, home="Cubs")[1]
    except IndexError:
        while 1:
            new_date = new_date + datetime.timedelta(days=1)
            try:
                game = mlbgame.day(new_date.year, new_date.month, new_date.day, home="Cubs")[0]
            except IndexError:
                continue
            else:
                if not game.w_team:
                    continue
                else:
                    break

print(season_hr)
