import time, sys
from combat import Combat
from character import Character
from monster import Dragon, Goblin, Troll, Shrek
from consent import Consent
 

class Game:
    def setup(self):
        self.player = Character()
        self.monsters = [
            Troll(),
            Goblin(),
            Shrek(),
            Dragon()
            ]
        self.monster = self.get_next_monster()
        self.dodge = Consent(question = "Dost thou will to dodge the attack? ")
        
    def get_next_monster(self):
        try:
            return self.monsters.pop(0)
        except IndexError:
            return None

    def monster_turn(self):
        #check if monster attacks
        time.sleep(0.4)
        if self.monster.attack():
        #if so tell player
            print("Hark! The {} is attacking...".format(self.monster.__class__.__name__))
            #check if player wants to dodge
            time.sleep(1)
            if self.dodge.consent_check():
                #if so, see if dodge works
                if self.player.dodge():
                    #if so, move on
                    print("Thou hast dodged the attack.")
                #if not, remove one player_hit point
                else:
                    print("Thy dodge hath falied")
                    time.sleep(1)
                    print("The {} hath hurt thee.".format(self.monster.__class__.__name__))
                    self.player.hit_points -= (self.monster.damage/25)
            else:
                print("The {} hath hurt thee.".format(self.monster.__class__.__name__))
                self.player.hit_points -= (self.monster.damage/25)
        #if monster doesn't attack tell player
        else:
            print("The {}'s attack failed.".format(self.monster.__class__.__name__))
        
    def player_turn(self):
        #let player attack, rest, quit
        time.sleep(0.4)
        if self.player.rests_remaining:
            choice = input("Would'st thou like to attack, rest, or quit the game? ").lower()
        else:
            choice = input("Would'st thou like to attack or quit the game? ").lower()           
        #if attack
        if choice in "attack":
            #if attack success
            if self.player.attack():
                time.sleep(1)
                print("Thy attack hath worked")
                #if monster dodge
                if self.monster.dodge():
                    #if dodge works
                        #print
                    time.sleep(1)
                    print("The {} dodged thy attack".format(self.monster.__class__.__name__))
                    #if dodge doesn't work
                else:
                    #print
                    time.sleep(1)
                    print("The {} was unable to dodge thy attack".format(self.monster.__class__.__name__))
                        #subtract hit_points from monster
                    self.monster.hit_points -= (self.player.weapon.damage/25)
                    
            #if attack fails
            else:
                #print
                time.sleep(1)
                print("Thy attack hath failed")
        #if rest
        elif choice in "rest":
            #add hit point to player (player.rest())
            if self.player.rest():
                time.sleep(1)
                print("Thy hit points hath been increased by 1.")
                time.sleep(1.2)
                print("Thou hast {} hit points.".format(int(self.player.hit_points)))
                time.sleep(1)
                print("Thou hast {} rest remaining.".format(self.player.rests_remaining))
            else:
                self.player_turn()
        #if quit
        elif choice in "quit":
            #exit
            time.sleep(1)
            print("Good effort, {}. It hast truly been a pleasure. Adieu.".format(self.player.name))
            sys.exit()
        #else
        else:
            self.player_turn()
            #rerun method

    def cleanup(self):
        #if monster runs out of hit points
        if self.monster.hit_points <= 0:
            #up player exper
            self.player.experience += self.monster.experience
            #print
            time.sleep(1)
            print("Thou hast defeated the {}!".format(self.monster.__class__.__name__))
            time.sleep(1.2)
            print("Thy experience is now {}".format(self.player.experience))
            time.sleep(1.2)
            if self.player.leveled_up():
                self.player.weapon.damage += 25
                print("Thou hast leveled up!")
                time.sleep(1.5)
                print("Thy {}'s damage hath been increased to {}".format(self.player.weapon.__class__.__name__, self.player.weapon.damage))
                time.sleep(2)
            self.monster = self.get_next_monster()
            #new monster
            if len(self.monsters) > 0:
                print("Thou next challenge shall be...")
                time.sleep(1.5)
                self.monster.intro()
            #final monster
            elif not len(self.monsters):
                print("Thy final challenge shall be...")
                time.sleep(1.5)
                self.monster.intro()
                time.sleep(1.5)
                print('-'*20)
                print("Thy hit points has been increased by 3 to prepare you for thy final battle!")
                self.player.hit_points += 3
                time.sleep(2)
                print("Thou now hast {} hit points.".format(int(self.player.hit_points)))
                
            

    def __init__(self):
        self.setup()
        print("Here is thy first challenge...")
        time.sleep(1.7)
        self.monster.intro()
        while (self.player.hit_points >= 0) and ((self.monster.hit_points >= 0) or len(self.monsters)):
            self.cleanup()
            
            print('='*20)
            time.sleep(1.5)
            print(self.monster)
            self.monster_turn()
            if self.player.hit_points <= 0:
                break
            print('-'*20)
            time.sleep(1.5)
            print(self.player)
            self.player_turn()
            


        if self.player.hit_points > 0:
            time.sleep(1)
            print("Thou hast succeeded in killing the {}!".format(self.monster.__class__.__name__))
            time.sleep(1.6)
            print ("Thou hath won!")
        elif self.monsters or self.monster.hit_points > 0:
            time.sleep(1)
            print("Thou hath lost!")
        sys.exit()


Game()
        
        
        
