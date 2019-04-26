from tkinter import *
from random import *

def NouveauLancer():
    nb = randint(1,6)
    Texte.set('Resultat -->'+str(nb))


Mafenetre =Tk()
Mafenetre.geometry("500x500")
Mafenetre.title('Dé a 6 faces')
BoutonLancer = Button(Mafenetre, text = 'Lancer', command = NouveauLancer)


BoutonLancer.pack(side = LEFT,padx=5,pady=5)

BoutonQuitter = Button(Mafenetre,text='Quitter',command =Mafenetre.destroy)
BoutonQuitter.pack(side=LEFT,padx=5,pady=5)
Texte = StringVar()

NouveauLancer()

LabelResultat = Label(Mafenetre, textvariable = Texte, fg ='red',bg='white')
LabelResultat.pack(side =LEFT, padx=5, pady=5)

Mafenetre.mainloop()


