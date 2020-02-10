from Monster_class import Monster


class Student_Monster(Monster):
    def __init__(self, name, strength, limbs, scary_skill=[]):
        super().__init__(name, strength, limbs, scary_skill)
        self.__debt = 0 # The double underscore, hides and does not let u access
        self.__scary_subject = 'Jump Scare'

    def uni_id(self):
        return 'u1612865'

    def debt(self, amount):
        self.__debt = amount  # This is classed a setter, by using the double underscore,
        # it lets you access the hidden

    def get_debt(self):  # you can set conditions befor you access information.
        input('Username: ')
        input('Password: ')
        return self.__debt

    def shout_strength(self):
        return 'Low'

    def scary_subject(self):
        self.__scary_subject = 'Jump Scare'
        
    def get_scary_subject(self):
        input('Username: ')
        input('Password: ')
        return self.__scary_subject

    def scare_strat(self):
        return 'RUN at you, quiet bell around my arm, \n' \
               'that you start hearing when in close enough,\n' \
               'a knife in one hand and a gun in the other.'

    def stealth_level(self):
        return 'stealth level'
