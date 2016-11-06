import random
class Warrior:
    health = 100
    strength = 0
    dexterity = 0
    stamina = 0

class Human(Warrior):
    name = "human"
    sword = [10, 30, 50]
    def __init__(self):
        self.strength= int(random.randrange(0, 100))
        self.dexterity=int(random.randrange(0, 100))
        self.stamina=int(random.randrange(0, 100))
        self.weapon = random.choice(Human.sword)

class Elf(Warrior):
    name = "elf"
    bow = [5, 20, 60]
    def __init__(self):
        self.strength= int(random.randrange(0, 100))
        self.dexterity=int(random.randrange(0, 100))
        self.stamina=int(random.randrange(0, 100))
        self.weapon = random.choice(Elf.bow)

class dwarf(Warrior):
    name = "dwarf"
    axe = [5, 30, 40]
    def __init__(self):
        self.strength= int(random.randrange(0, 100))
        self.dexterity=int(random.randrange(0, 100))
        self.stamina=int(random.randrange(0, 100))
        self.weapon = random.choice(dwarf.axe)

team1 = [Human(), Elf(), dwarf()]
team2 = [Human(), Elf(), dwarf()]

winner = False
turn = 0
while winner == False:
    turn = turn + 1
    print "Turn= ", turn
    alive = False
    while alive == False:
        war1 = random.choice(team1)
        if war1.health <= 0:
            alive = False
        else:
            alive = True
    alive = False
    while alive == False:
        war2 = random.choice(team2)
        if war2.health <= 0:
            alive = False
        else:
            alive = True

    total1 = war1.strength + war1.dexterity + war1.stamina + war1.weapon
    total2 = war2.strength + war2.dexterity + war2.stamina + war2.weapon
    print "Warrior of team 1 is ", war1.name, " and total power of warrior is ", total1," and healt is", war1.health
    print "Warrior of team 2 is ", war2.name, " and total power of warrior is ", total2," and healt is", war2.health

    if total1 > total2:
        war2.health = war2.health - (total1 - total2)
    elif total2 > total1:
        war1.health = war1.health - (total2 - total1)
    else:
        war1.health = war1.health
        war2.health = war2.health

    if team1[0].health<=0 and team1[1].health<=0 and team1[2].health<=0:
        print "team 2 is winner"
        winner=True
    elif team2[0].health <= 0 and team2[1].health <= 0 and team2[2].health <= 0:
        print "team 1 is winner"
        winner=True
    else:
        print "war continiues"
        winner=False