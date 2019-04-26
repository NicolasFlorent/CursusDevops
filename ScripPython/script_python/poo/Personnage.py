class Personnage():

    def __init__(self, nom, sexe, taille, poids):
        self.nom=nom
        self.sexe=sexe
        self.taille=taille
        self.poids=poids
    
    def whatSex(self):
        if self.sexe=='H':
            print("Ooh vous êtes un homme ! Bonjour Monsieur !")
        elif self.sexe=='F':
            print("Ooh vous êtes une femme ! Bonjour Madame !")
        else:
            print("désolé je ne connais pas ce sexe encore... il faut que je me mette à jour")
        
    def changeNom(self,newName):
        self.nom=newName
        print("Votre nouveau nom est ",self.nom)



moi = Personnage("Nicolas", "H", 1.78, 78)
moi.whatSex()
moi.changeNom("Florent")
        