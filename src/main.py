import random

from heroes import Paladin
from enemies import Murlock
from equips import WoodSword, LeatherArmor

class Battle():
    def __init__(self):
        self.hero = Paladin()
        self.hero.check_equip(WoodSword())
        self.hero.check_equip(LeatherArmor())

        self.enemy = Murlock()

    def combat(self, left, right):
        if random.uniform(0.0, 1.0) >= 0.15:
            damage = left.attack
            for equip in left.equips:
                damage += equip.attack
            # TODO: Equips property resistence on attack
            for key in ['water', 'fire', 'light', 'dark']:
                if left.properties.get(key):
                    damage += (left.properties[key] - right.resistence.get(key, 0.00))
            damage -= right.defense
            for equip in right.equips:
                damage -= equip.defense
            # TODO: Equips property resistence on defense
            damage = damage if damage > 0 else random.randint(1, 5)
            right.life_points -= damage
            message = '{0} made {1} points of damage!'.format(left.name, damage)
        else:
            message = '{0} miss the attack!'.format(left.name)
        return message

def main():
    battle = Battle()
    win = False
    lose = False
    end = False
    while not end:
        print('You', battle.hero.name, '| LP:', str(battle.hero.life_points))
        print('Enemy', battle.enemy.name, '| LP:', str(battle.enemy.life_points))
        print("""Choose an option:
Attack - press(a)
        """)
        choose = input()
        if choose.lower() == 'a':
            print(battle.combat(battle.hero, battle.enemy))
        win = battle.enemy.life_points <= 0
        if win:
            break
        print(battle.combat(battle.enemy, battle.hero))
        lose = battle.hero.life_points <= 0
        if lose:
            break
        print('-' * 30)
    message = 'You win!' if win else 'You lose'
    print(message)

if __name__ == "__main__":
    main()
