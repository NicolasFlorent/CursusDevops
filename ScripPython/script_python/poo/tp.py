import random

class Personnage():

    def __init__(self,name,attack,pv,vitesse):
        self.name=name
        self.attack=attack
        self.pv=pv
        self.vitesse=vitesse

    def enVie(self):
        return self.pv>=0

    def firstAttack(self):
        chance=random.randint(0,10)/10
        return chance*self.vitesse

    
    def attaquer(self,personnage):
        print(self.name,"(",self.pv,") attaque ",personnage.name,"(",personnage.pv,") ! Il perd ", self.attack," points de vie !")
        personnage.pv-=self.attack
    
    def mort(self,personnage):
        print(self.name," est mort... RIP... Le vainqueur est ",personnage.name)






mario=Personnage("Mario", 20, 150, 15)
donk=Personnage("Donkey Kong", 2, 190, 8)

while(mario.enVie() and donk.enVie()):
    if(mario.firstAttack() > donk.firstAttack()):
        mario.attaquer(donk)
        if donk.enVie():
            donk.attaquer(mario)
    else:
        donk.attaquer(mario)
        if mario.enVie():
            mario.attaquer(donk)
    if not mario.enVie():
        mario.mort(donk)
    else:
        donk.mort(mario)