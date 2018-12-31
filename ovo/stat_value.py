#!/usr/bin/env python3

from data_collector import Player
from peewee import *

db = SqliteDatabase('ovo.db')
db.connect()

players = Player.select().where(Player.plate_appearances > 50)

class Ovo(Model):
    name = CharField()

    ovo = FloatField()

    class Meta:
        database = db

db.drop_tables([Ovo])
db.create_tables([Ovo], safe=True)

best_hr = 0.0
best_h = 0.0
best_d = 0.0
best_t = 0.0
best_bb = 0.0
best_so = 0.0
best_rbi = 0.0
best_sb = 0.0
best_sb_avg = 0.0
best_r = 0.0
best_obp = 0.0
best_slg = 0.0


for player in players:
    if player.hr/player.plate_appearances > best_hr:
        decimal = player.hr/player.atbats
        best_hr = decimal

    if player.hits/player.plate_appearances > best_h:
        best_h = player.hits/player.plate_appearances

    if player.bb/player.plate_appearances > best_bb:
        best_bb = player.bb/player.plate_appearances

    if player.plate_appearances/player.so > best_so:
        best_so = player.plate_appearances/player.so

    if player.rbi/player.plate_appearances > best_rbi:
        best_rbi = player.rbi/player.plate_appearances

    if player.sb/player.games > best_sb:
        best_sb = player.rbi/player.games

    if player.runs/player.plate_appearances > best_r:
        best_r = player.runs/player.plate_appearances

    obp = (player.hits + player.bb + player.hit_by_pitch)/player.plate_appearances
    if obp > best_obp:
        best_obp = obp

    slg = ((player.hits-(player.doubles+player.triples+player.hr)) + 2*player.doubles + 3*player.triples + 4*player.hr)/player.atbats
    if slg > best_slg:
        best_slg = slg

for player in players:
    hr_pct = player.hr/player.plate_appearances
    h_pct = player.hits/player.plate_appearances
    d_pct = player.hits/player.plate_appearances
    t_pct = player.hits/player.plate_appearances
    bb_pct = player.hits/player.plate_appearances
    so_pct = player.hits/player.plate_appearances
    rbi_pct = player.hits/player.plate_appearances
    sb_pct = player.hits/player.plate_appearances
    try:
        sb_succ_pct = player.sb/(player.sb + player.cs)
    except ZeroDivisionError:
        sb_succ_pct = 0.0
    r_pct = player.hits/player.plate_appearances
    obp_pct = player.hits/player.plate_appearances
    slg_pct = ((player.hits-(player.doubles+player.triples+player.hr)) + 2*player.doubles + 3*player.triples + 4*player.hr)/player.atbats

    player_ovo = float(str(((hr_pct/best_hr)*0.82 +
                    (h_pct/best_h)*1 +
                    (bb_pct/best_bb)*0.85 +
                    (so_pct/best_so)*1.2 +
                    (rbi_pct/best_rbi)*0.7 +
                    (sb_pct/best_sb)*0.4 +
                    (sb_succ_pct)*0.5 +
                    (obp_pct/best_obp)*2.5 +
                    (slg_pct/best_slg)*2.57)/10)[:5])

    db.begin()
    Ovo.create(name=player.name,
                    ovo=player_ovo)
    db.commit()

db.close()



