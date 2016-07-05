
class Equip():
    life_points = 0
    properties = {}
    resistence = {}
    attack = 0
    defense = 0

class LeatherArmor(Equip):

    equip_type = 'armor'

    def __init__(self, life_points=500, properties={}, resistence={}, attack=0, defense=40):
        self.life_points = life_points
        self.attack = attack
        self.defense = defense
        self.resistence = resistence
        self.properties = properties


class WoodSword(Equip):

    equip_type = 'sword'

    def __init__(self, life_points=20, properties={}, resistence={'water': 50}, attack=150, defense=10):
        self.life_points = life_points
        self.attack = attack
        self.defense = defense
        self.resistence = resistence
        self.properties = properties
