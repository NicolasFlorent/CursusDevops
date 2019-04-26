import random

print("SHIFUMI !!!!")
print("Vous allez jouer contre l'IA")

coups=['Pierre','Feuille','Ciseaux']


game_off=False
while(not game_off):
    print("-----------------------------------------")
    print("1. Pierre\n2. Feuille\n3. Ciseaux")
    bool_choix=False
    while(not bool_choix):
        choix=input("Faites votre choix ! (L'IA ne le connait pas, ne vous inquiétez pas...) ---> ")
        if choix=='1' or choix=='2' or choix=='3':
            choix_joueur=coups[int(choix)-1]
            bool_choix=True
        elif choix=='q':
            print("Le jeu est fini...")
            break
        else:
            print("Ce n'est pas une commande acceptée.... ")
    if choix!='q':
        choix_IA=coups[random.randint(0,2)]
        print(choix_joueur," vs ",choix_IA)
        if choix_IA==choix_joueur:
            print("Egalité !!!")
        elif (choix_IA=='Pierre' and choix_joueur=='Ciseaux') or (choix_IA=='Ciseaux' and choix_joueur=='Feuille') or (choix_IA=='Feuille' and choix_joueur=='Pierre'):
            print("L'IA a gagné !!! ")
        elif (choix_joueur=='Pierre' and choix_IA=='Ciseaux') or (choix_joueur=='Ciseaux' and choix_IA=='Feuille') or (choix_joueur=='Feuille' and choix_IA=='Pierre'):
            print("Vous avez gagné !!!")
    else:
        break


