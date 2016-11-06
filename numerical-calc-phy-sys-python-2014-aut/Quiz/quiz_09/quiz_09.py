from random import *

class warrior:
    health=100
    strength=0
    dexterity=0
    stamina=0
    def pro(self):
        self.health=100
        self.strength=randrange(1,101,1)
        self.dexterity=randrange(1,101,1)
        self.stamina=randrange(1,101,1)
        print "Health: ", self.health, "Strength: ", self.strength, "Dexterity: ", self.dexterity, "Stamina: ", self.stamina
    def hr(self):
        return self.health
class human(warrior):
    def __init__(self):
        self.weapon=choice([10,30,50])
    def weapon_1(self):
        if self.weapon == 10:
            print "Dagger"
        elif self.weapon ==30:
            print "Short Sword"
        else:
            print "Long Sword"
    def tot(self):
        return self.health+self.strength+self.stamina+self.dexterity
class elf(warrior):
    def __init__(self):
        self.weapon=choice([5,20,60])
    def weapon_1(self):
        if self.weapon == 5:
            print "Sling"
        elif self.weapon ==20:
            print "Scimitar"
        else:
            print "Long Bow"
    def tot(self):
        return self.health+self.strength+self.stamina+self.dexterity

class dwarf(warrior):
    def __init__(self):
        self.weapon=choice([5,30,40])
    def weapon_1(self):
        if self.weapon == 5:
            print "Her/His Head!"
        elif self.weapon ==20:
            print "Metal Hammer"
        else:
            print "Vengeance Hammer"
    def tot(self):
        return self.health+self.strength+self.stamina+self.dexterity

g1_h=human()
print "Human of the Group One has properties of..."
g1_h.pro()
print "and weapon of choice..."
g1_h.weapon_1()
print " "

g1_e=elf()
print "Elf of the Group One has properties of..."
g1_e.pro()
print "and weapon of choice..."
g1_e.weapon_1()
print " "

g1_d=dwarf()
print "Dwarf of the Group One has properties of..."
g1_d.pro()
print "and weapon of choice..."
g1_d.weapon_1()
print " "

g2_h=human()
print "Human of the Group Two has properties of..."
g2_h.pro()
print "and weapon of choice..."
g2_h.weapon_1()
print " "

g2_e=elf()
print "Elf of the Group Two has properties of..."
g2_e.pro()
print "and weapon of choice..."
g2_e.weapon_1()
print " "

g2_d=dwarf()
print "Dwarf of the Group Two has properties of..."
g2_d.pro()
print "and weapon of choice..."
g2_d.weapon_1()
print " "

h1=[g1_h.tot(),g1_h.hr()]
e1=[g1_e.tot(),g1_e.hr()]
d1=[g1_d.tot(),g1_d.hr()]
h2=[g2_h.tot(),g2_h.hr()]
e2=[g2_e.tot(),g2_e.hr()]
d2=[g2_d.tot(),g2_d.hr()]


g1=[h1[0],e1[0],d1[0]]
g2=[h2[0],e2[0],d2[0]]
f1t=choice(g1)
f2t=choice(g2)
f1h,f2h=1,1
while f1h!=0 or f2h!=0:
    if f1t==h1[0]:
        f1h=h1[1]
    elif f1t==e1[0]:
        f1h=e1[1]
    else:
        f1h=d1[1]

    if f2t==h2[0]:
        f2h=h2[1]
    elif f2t==e2[0]:
        f2h=e2[1]
    else:
        f2h=d2[1]

    if f2h > 0 or f1h > 0:
        if f1t>f2t:
            f2h=f2h-(f1t-f2t)
        elif f2t>f1t:
            f1h=f1h-(f2t-f1t)
    else:
        if f1h>f2h:
            print "Fighter of the first team wins!"
        else:
            print "Fighter of the second team wins!"

#Isin icinden cikamadim hocam ¯\_(ツ)_/¯
