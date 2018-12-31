import random, time
from combat import Combat
from weapon import Weapon, Sword, Axe, Bow

class Character(Combat):
    experience = 0
    base_hit_points = 10
    exper_goal = 5
    rests_remaining = 3

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 4
        print(roll)
        
    def get_weapon(self):
        weapon_choice = input("{}, select thy weapon: (Sword, Axe, Bow) ".format(self.name)).lower()
        if weapon_choice in 'sword':
            return Sword()
        elif weapon_choice in 'axe':
            return Axe()
        elif weapon_choice in 'bow':
            return Bow()
        else:
            return self.get_weapon()
            
                
    def __init__(self):
        #gets name; greets player
        print("Good morrow young warrior...")
        time.sleep(1)
        self.name = input("What is thy name? ")
        time.sleep(1)
        print("'Tis my pleasure to meet you, noble {}.".format(self.name))
        #explains weapons
        time.sleep(1)
        print("Now please read thy weapon options...")
        time.sleep(1.5)
        print(Sword())
        time.sleep(6.2)
        print(Axe())
        time.sleep(6.7)
        print(Bow())
        print('-'*20)
        time.sleep(6.7)
        #gets weapon
        self.weapon = self.get_weapon()
        time.sleep(1.5)
        #sets game vars
        self.hit_points = self.base_hit_points
        self.attack_limit = self.weapon.accuracy
        self.dodge_limit = 13 - self.weapon.exposure

    def __str__(self):
        return '{}, weapon: {}, HP: {}, XP: {}'.format(self.name, self.weapon.__class__.__name__, int(self.hit_points), self.experience)

    def rest(self):
        if self.hit_points < self.base_hit_points and self.rests_remaining > 0:
            self.hit_points += 1
            self.rests_remaining -= 1
            return True
        elif self.rests_remaining == 0:
            print("Thou hast expended all of thine rests.")
            return False
        else:
            print("Thou art at thy max hit points. Rest doth nought.")
            return False

    def leveled_up(self):
        global exper_goal
        if self.experience >= self.exper_goal:
            self.exper_goal *= 2
            return True
