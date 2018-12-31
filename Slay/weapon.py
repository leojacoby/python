class Weapon:
    accuracy = 12
    damage = 50
    exposure = 6
    description = None

    def __str__(self):
        return '-'*20 + '\n{}\nAccuracy: {}\nDamage: {}\nExposure: {}\n{}'.format(self.__class__.__name__, self.accuracy, self.damage, self.exposure, self.description)


class Sword(Weapon):
    description = """The sword is an overall impressive weapon
with solid accuracy, damage, and low exposure."""

class Axe(Weapon):
    accuracy = 9
    damage = 75
    exposure = 8
    description = """The axe will'st not hit oft, but when it dost,
t'will not end well for thy foe.
But beware, the axe will leave you quite exposed to attacks."""

class Bow(Weapon):
    accuracy = 100
    damage = 25
    exposure = 1
    description = """Thou can count on successful attacks from the bow,
but thou art going to need a lot of them to make a dent
in thy foe's HP.  Because it is a long distance weapon, thou art very safe from enemy
attacks."""

