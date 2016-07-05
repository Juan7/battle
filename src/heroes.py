import equips


class BaseHero():
    life_points = 0
    properties = {}
    resistence = {}
    attack = 0
    defense = 0
    equips = []

    def get_equip_by_type(self, equip_type):
        current_equip_type = [equip for equip in self.equips if equip.equip_type == equip_type]
        return current_equip_type, bool(current_equip_type)

    def check_equip(self, equip):
        current_equip, exist = self.get_equip_by_type(equip.equip_type)
        if exist:
            self.remove_equip(current_equip_type[0])
        self.add_equip(equip)

    def add_equip(self, equip):
        self.equips.append(equip)
        self.life_points += equip.life_points
        for element, amount in equip.resistence.items():
            if self.resistence.get(element):
                self.resistence[element] += amount
            else:
                self.resistence.update({element: amount})
        for element, amount in equip.properties.items():
            if self.properties.get(element):
                self.properties[element] += amount
            else:
                self.properties.update({element: amount})

    def remove_equip(self, equip):
        self.equips.remove(equip)
        self.life_points -= equip.life_points
        for element, amount in equip.resistence.items():
            if self.resistence.get(element):
                self.resistence[element] += amount
            else:
                self.resistence.update({element: amount})
        for element, amount in equip.properties.items():
            if self.properties.get(element):
                self.properties[element] += amount
            else:
                self.properties.update({element: amount})


class Paladin(BaseHero):

    name = 'Paladin'

    def __init__(self, life_points=100, properties={'light': 20}, resistence={'light': 40}, attack=30, defense=20):
        self.life_points = life_points
        self.attack = attack
        self.defense = defense
        self.resistence = resistence
        self.properties = properties
