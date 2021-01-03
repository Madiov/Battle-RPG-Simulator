from Classes.battle import Person, Bcolors, Magic, Inventory

# Spells
magic_missle = Magic('magic missle', 10, 100, 'Evocation', 'no')
fire_bolt = Magic('fire bolt', 7, 80, 'Evocation', 'no')
entangle = Magic('entangle', 15, 180, 'Conjuration', 'no')
blight = Magic('blight', 30, 400, 'Necromancy', 'no')
cure_wounds = Magic('cure_wounds', 10, 200, 'Evocation', 'yes')
dragons_breath = Magic('dragons breath', 20, 230, 'Transmutation', 'no')
web = Magic('web', 13, 140, 'Conjuration', 'no')

# Items
healing_potion = Inventory('Healing Potion', 'potion', 'Heals you for 100 hp', 100, 3)
super_healing_potion = Inventory('Super healing potion', 'potion', 'heals you for 200 hp', 200, 2)
elixir = Inventory('Elixir', 'elixir', 'Fully restores HP and MP', 9999, 1)
alchemist_fire = Inventory('Alchemist fire', 'grenade', 'Deals 150 damage', 150, 4)

# Magics And Items
player_magics = [magic_missle, fire_bolt, entangle, blight, cure_wounds, dragons_breath, web]
player_items = [healing_potion, super_healing_potion, elixir, alchemist_fire]

# Player And Enemy Objects
player = Person(1000, 65, 60, 50, player_magics, player_items)
enemy = Person(1500, 65, 120, 30, player_magics, elixir)

# Start of Fight
running = True
elixier = True
print(
    Bcolors.OKGREEN + "You are wandering in the trollbark woods." + Bcolors.WARNING + " Suddenly you hear something approaching." + Bcolors.Red + 'something menacing and fearsome.' + Bcolors.ENDC)
print(Bcolors.FAIL + Bcolors.BOLD + 'AN ENEMY ATTACKS!' + Bcolors.ENDC)
while running:

    player.status()
    print('\n\n')
    enemy.boss_status()
    print('\n\n')

    print('=======================')
    player.choose_action()
    choice = input(Bcolors.Yellow + "Choose action :" + Bcolors.ENDC)
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage() - enemy.defence()
        enemy.takedmg(dmg)
        print('    ', 'You attacked for : ', Bcolors.OKBLUE, dmg, 'points of damage.' + Bcolors.ENDC)
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input(Bcolors.Yellow + "Choose magic: " + Bcolors.ENDC)) - 1
        spell = player.magic[magic_choice]
        spell_dmg = spell.generate_spelldamage()
        current_mp = player.get_mp()
        if spell.cost > current_mp:
            print(Bcolors.FAIL + '\n     Not enough MP' + Bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)
        if spell.heal == 'no':
            enemy.takedmg(spell_dmg)
            print(Bcolors.OKBLUE + '\n' + '     ' + spell.name + ' deals', str(spell_dmg),
                  'poitns of damage.' + Bcolors.ENDC)
        else:
            player.heal(spell_dmg)
            print(Bcolors.OKBLUE + '\n' + '     ' + spell.name + ' heals you for', str(spell_dmg), 'HP.' + Bcolors.ENDC)
    elif index == 2:
        player.choose_items()
        item_choice = int(input(Bcolors.Yellow + "Choose item: " + Bcolors.ENDC)) - 1
        item = player.items[item_choice]
        if item.amount == 0:
            print('    ', Bcolors.FAIL, 'you are out of ', item.name, Bcolors.ENDC)
            continue
        if item.type == 'grenade':
            item.amount -= 1
            enemy.takedmg(item.effect)
            print(Bcolors.OKBLUE + '\n' + '     ' + item.name + ' deals', str(item.effect),
                  'poitns of damage.' + Bcolors.ENDC)
        elif item.type == 'elixir':
            item.amount -= 1
            player.hp = player.maxhp
            player.mp = player.maxmp

        else:
            item.amount -= 1
            player.heal(item.effect)
            print(Bcolors.OKBLUE + '\n' + '     ' + item.name + ' heals you for', str(item.effect),
                  'HP.' + Bcolors.ENDC)
    if enemy.hp < enemy.maxhp // 5:
        while elixier:
            print(Bcolors.Red + '     Wicked demon is drinking an Elixir' + Bcolors.ENDC)
            enemy.hp = enemy.maxhp
            elixier = False
            continue

    enemy_dmg = enemy.generate_damage() - player.defence()
    player.takedmg(enemy_dmg)
    print('    ', 'Enemy attacked for : ' + Bcolors.FAIL, enemy_dmg, 'points of damage. ' + Bcolors.ENDC)
    print('_____________________')
    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + 'YOU WON!!' + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + 'YOU DIED!' + Bcolors.ENDC)
        running = False
