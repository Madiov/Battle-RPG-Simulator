import random


class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Yellow = "\033[33m"
    Cyan = "\033[36m"
    Red = "\033[31m"


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ['Physycal Attack', 'Magic', 'items']
        self.items = items

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def heal(self, heal):
        self.hp += heal
        if self.hp > self.maxhp:
            self.hp = self.maxhp
        return self.hp

    def takedmg(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def defence(self):
        return random.randrange(1,self.df)

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        print(Bcolors.OKBLUE + Bcolors.BOLD + 'Actions : ' + Bcolors.ENDC)
        i = 1
        for action in self.actions:
            print('    ', str(i) + ' : ', action)
            i += 1

    def choose_magic(self):
        print('_____________________')
        i = 1
        for spell in self.magic:
            if spell.heal == 'no':
                print('    ', str(i) + ' : ', spell.name, ', Cost :', spell.cost, ', Damage :', spell.dmg, ', Type :',
                      spell.type)
            else:
                print('    ', str(i) + ' : ', spell.name, ', Cost :', spell.cost, ', Heal :', spell.dmg, ', Type :',
                      spell.type)
            i += 1

    def choose_items(self):
        print('_____________________')
        i = 1
        for item in self.items:
            print('    ', str(i) + ' : ', item.name, ':', Bcolors.Cyan, item.description, Bcolors.ENDC, Bcolors.OKBLUE,
                  '. You currently have :', item.amount, Bcolors.ENDC)

            i += 1

    def status(self):

        mp_string = len(str(self.mp) + '/' + str(self.maxmp))
        spaces_mp = mp_string * ' '

        hp_string = len(str(self.hp) + '/' + str(self.maxhp))
        spaces = hp_string * ' '

        hbar = ''
        bar_ticks = (self.hp / self.maxhp) * 25
        mbar = ''
        mbar_tick = (self.mp / self.maxmp) * 10
        while mbar_tick > 0:
            mbar += '█'
            mbar_tick -= 1
        while len(mbar) < 10:
            mbar += ' '

        while bar_ticks > 0:
            hbar += '█'
            bar_ticks -= 1
        while len(hbar) < 25:
            hbar += ' '
        print('\n\n')
        print('Name                           HP                                      MP              ')
        print(spaces + '                         _________________________',
              Bcolors.OKBLUE + spaces_mp + '          __________ ', Bcolors.ENDC)
        print('Sir WhoWinsALot:', self.hp, '/', self.maxhp, '    |' + Bcolors.OKGREEN + hbar + '|  ', Bcolors.ENDC,
              self.mp, '/', self.maxmp, '  |' + Bcolors.OKBLUE + mbar + '|  ', Bcolors.ENDC)

    def boss_status(self):
        hp_string = len(str(self.hp) + '/' + str(self.maxhp))
        spaces = hp_string * ' '
        bbar = ''
        boss_ticks = (self.hp / self.maxhp) * 50
        while boss_ticks > 0:
            bbar += '█'
            boss_ticks -= 1
        while len(bbar) < 50:
            bbar += ' '
        print('Name                         HP')
        print(
            Bcolors.FAIL + spaces + '                      __________________________________________________ ' + Bcolors.ENDC)
        print(
            'Th wicked Demon', self.hp, '/', self.maxhp, '  |' + Bcolors.FAIL + bbar + '|  ' + Bcolors.ENDC)


class Magic:
    def __init__(self, name, cost, dmg, type, heal):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type
        self.heal = heal

    def generate_spelldamage(self):
        mgl = self.dmg - 15
        mgh = self.dmg + 15
        return random.randrange(mgl, mgh)


class Inventory:
    def __init__(self, name, type, description, effect, amount):
        self.name = name
        self.description = description
        self.amount = amount
        self.type = type
        self.effect = effect
