import random

class Combat:
    dodge_limit = 7
    attack_limit = 8

    def dodge(self):
        roll = random.randint(1, self.dodge_limit)
        return roll > 5

    def attack(self):
        roll = random.randint(1, self.attack_limit)
        return roll > 3
