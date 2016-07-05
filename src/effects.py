class Buff():
    self.attrib = {}

class Stun(Buff):

    def __init__(self, attrib={'stun': {'time': 1}}):
        self.attrib = attrib

class AtkUp(Buff):

    def __init__(self, attrib={'attack': {'amount': 40}}):
        self.attrib = attrib

class DefUp(Buff):

    def __init__(self, attrib={'defense': {'amount': 40}}):
        self.attrib = attrib
