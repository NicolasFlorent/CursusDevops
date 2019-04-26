import random

class Personnage():

    def __init__(self,name,attack,pv,vitesse,arme,capacite):
        self.name=name
        self.attack=attack
        self.pv=pv
        self.vitesse=vitesse
        self.arme=arme
        self.capacite=capacite


    def enVie(self):
        return self.pv>=0

    def firstAttack(self):
        chance=random.randint(0,10)/10
        return chance*self.vitesse

    
    def attaquer(self,personnage):
        chanceArme=random.randint(0,100)
        chanceCapacité=random.randint(0,100)

        if chanceArme<=30:
            print(self.name," utilise son arme ",self.arme.name)
            print(self.name,"(",self.pv,") attaque ",personnage.name,"(",personnage.pv,") ! Il perd ", self.attack*self.arme.multi," points de vie !")
            personnage.pv-=self.attack*self.arme.multi
        elif chanceCapacité<=20:
            print(self.name," utilise sa capacité ",self.capacite.name)
            print(self.name,"(",self.pv,") attaque ",personnage.name,"(",personnage.pv,") ! Il perd ", self.capacite.attack," points de vie !")
            personnage.pv-=self.capacite.attack
        else:
            print(self.name,"(",self.pv,") attaque ",personnage.name,"(",personnage.pv,") ! Il perd ", self.attack," points de vie !")
            personnage.pv-=self.attack
    
    def mort(self,personnage):
        print(self.name," est mort... RIP... Le vainqueur est ",personnage.name)

    def renseignementArme(self):
        print(self.name," possède l'arme suivante : ",self.arme.name)
        print("Elle lui accorde un multiplicateur de ", self.arme.multi)

    def renseignementCapacite(self):
        print(self.name," possède la capacité suivante : ",self.capacite.name)
        print("Elle a une attaque de ", self.capacite.attack)

class Arme():

    def __init__(self, name, multi):
        self.name=name
        self.multi=multi
    


class Capacite():

    def __init__(self, name, attack):
        self.name=name
        self.attack=attack


class Combat():

    def __init__(self, perso1, perso2):
        self.perso1=perso1
        self.perso2=perso2

    def begin(self):
        print("Combat : ",self.perso1.name," vs ",self.perso2.name)
        print()
        self.perso1.renseignementArme()
        self.perso1.renseignementCapacite()
        print()
        self.perso2.renseignementArme()
        self.perso2.renseignementCapacite()
        print()
        print("------------------------------------------------------------")
        while(self.perso1.enVie() and self.perso2.enVie()):
            if(self.perso1.firstAttack() > self.perso2.firstAttack()):
                self.perso1.attaquer(self.perso2)
                if self.perso2.enVie():
                    self.perso2.attaquer(self.perso1)
            else:
                self.perso2.attaquer(self.perso1)
                if self.perso1.enVie():
                    self.perso1.attaquer(self.perso2)
            if not self.perso1.enVie():
                self.perso1.mort(self.perso2)
            elif not self.perso2.enVie():
                self.perso2.mort(self.perso1)
            print("------------------------------------------------------------")



capacite1=Capacite("Boule de feu",100)
capacite2=Capacite("Tam Tam dans ta gueule",120)

arme1=Arme("Casquette du héro", 3)
arme2=Arme("Gant de la jungle", 2)


mario=Personnage("Mario", 21, 1000, 15, arme1,capacite1)
donk=Personnage("Donkey Kong", 26, 900, 8,arme2, capacite2)



battle=Combat(mario,donk)
battle.begin()