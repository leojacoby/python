#!/usr/bin/env python3

from stat_value import Value
from peewee import *

db = SqliteDatabase('ovo.db')
db.connect()

players = Value.select()

class Ovo(Model):
    name = CharField()

    ovo = FloatField(default=0.0)

    class Meta:
        database = db

#db.drop_tables([Ovo])
import pdb; pdb.set_trace()
db.create_tables([Ovo], safe=True)

for player in players:
    player_ovo = (player.obp_value +
                 player.slg_value +
                 player.h_value +
                 player.bb_value +
                 player.so_value +
                 player.sb_value +
                 player.sb_avg_value +
                 player.hr_value +
                 player.rbi_value)/10
    db.begin()
    Ovo.create(name=player.name, ovo=player_ovo)
    db.commit()

db.close()