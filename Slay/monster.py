import random, time

Colors = ['yellow', 'red', 'blue', 'green', 'purple', 'orange']


from combat import Combat

class Monster(Combat):
    hit_points = 1
    experience = 1
    damage = 25
    
    def __init__(self):
        self.color = random.choice(Colors)
 
    def __str__(self):
        return '{} {}, HP: {}, XP: {}, Damage: {}'.format(self.color.title(), self.__class__.__name__, int(self.hit_points), self.experience, self.damage)

    def intro(self):
        print('-'*20)
        print(self.color.title() + ' ' + self.__class__.__name__)
        time.sleep(1)
        print('Hit Points: {}'.format(self.hit_points))
        time.sleep(1)
        print('Experience: {}'.format(self.experience))
        time.sleep(1)
        print('Damage: {}'.format(self.damage))
        time.sleep(1)
        print(self.description)
        time.sleep(4.5)
    def battlecry(self):
        return self.sound.upper()

class Troll(Monster):
    hit_points = 3
    experience = 2
    damage = 25
    description = """This annoying monster hath one purpose:
to knock off a few of thy hit points before it is killed."""

class Goblin(Monster):
    hit_points = 6
    experience = 3
    damage = 25
    description = """More skilled and experienced than the Troll;
the Goblin will'st prove thy first true challenge!"""

class Shrek(Monster):
    hit_points = 8
    experience = 5
    damage = 50
    description = """If thou art not cautious, thou might get Shrek'd."""
    def __init__(self):
        self.color = 'green'
        
class Dragon(Monster):
    hit_points = 10
    experience = 10
    damage = 75
    description = """The dragon is the boss monster.
Many hit points and imense damage doth make it quite dangerous."""




