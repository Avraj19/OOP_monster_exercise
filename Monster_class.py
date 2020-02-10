class Monster:

    def __init__(self, name, strength_level, scary_skill, limbs):
        self.name = name
        self.strength_level = strength_level
        self.scary_skill = scary_skill
        self.limbs = limbs

    def sleep(self):
        return 'zzzzzzzz'
    def eat(self):  # To make args optional (arg = '')
        return 'nom nom nom nom'
    def pay_taxes(self):
        return 'Where my money Brian'
    def shout_strength(self):
        return 'RRRRRRRRRRRRRRRAAAAAAAAAAAAAAAAAA!!!, mmmeeuuuu'
    def strength_level(self):
        return self.strength_level




