import random
import math

def jeu_solo_illimited():
    choix_limite=False
    while(not choix_limite):
        limitemin=input("Quelle est la limite basse que vous voulez fixer ?? ")
        limitemax=input("Quelle est la limite haute que vous voulez fixer ?? ")
        limitemin=int(limitemin)
        limitemax=int(limitemax)
        if limitemin>limitemax:
            print("Le choix des limites n'a pas de sens ! Vous devez refaire le choix")
        else:
            print("Pas de souci pour l'intervalle !")
            choix_limite=True
    nbmystere=random.randint(limitemin,limitemax)
    print("Le nombre Mystère a été choisi entre ",limitemin, " et ",limitemax )
    choix_nb=limitemin-1
    stop=False
    while(choix_nb!=nbmystere or not stop):
        choix_nb=input("Votre hypothèse de nombre ? (pour quitter choisissez 'q') ---> ")
        if choix_nb=='q':
            print("Vous avez decidé d'arrêter le jeu... Dommage pour vous... le nombre à trouver était ", nbmystere)
            break
        choix_nb=int(choix_nb)
        if choix_nb>limitemax or choix_nb<limitemin:
            print("Le nombre choisi n'est pas dans l'intervalle !")
        elif choix_nb<nbmystere:
            print("Votre nombre est trop petit ! Essayer encore !")
        elif choix_nb>nbmystere:
            print("Votre nombre est trop grand ! Essayer encore ")
        elif choix_nb==nbmystere:
            print("Bravo ! Vous avez trouvé !! \o/")
            stop=True


def jeu_solo_limited():
    choix_limite=False
    while(not choix_limite):
        limitemin=input("Quelle est la limite basse que vous voulez fixer ?? ")
        limitemax=input("Quelle est la limite haute que vous voulez fixer ?? ")
        limitemin=int(limitemin)
        limitemax=int(limitemax)
        if limitemin>limitemax:
            print("Le choix des limites n'a pas de sens ! Vous devez refaire le choix")
        else:
            print("Pas de souci pour l'intervalle !")
            choix_limite=True
    nbmystere=random.randint(limitemin,limitemax)
    print("Le nombre Mystère a été choisi entre ",limitemin, " et ",limitemax )
    choix_nb=limitemin-1
    stop=False

    nb_essai=5
    print("Vous avez droit à ",nb_essai," !")

    while(choix_nb!=nbmystere or not stop or nb_essai>0 ):
        print("Il vous reste ", nb_essai," !")
        choix_nb=input("Votre hypothèse de nombre ? (pour quitter choisissez 'q') ---> ")

        if nb_essai<=1:
            print("Vous n'avez plus d'essai ! le nombre mystère était ", nbmystere)
            break

        if choix_nb=='q':
            print("Vous avez decidé d'arrêter le jeu... Dommage pour vous... le nombre à trouver était ", nbmystere)
            break
        choix_nb=int(choix_nb)
        if choix_nb>limitemax or choix_nb<limitemin:
            print("Le nombre choisi n'est pas dans l'intervalle !")
        elif choix_nb<nbmystere:
            print("Votre nombre est trop petit ! Essayer encore !")
        elif choix_nb>nbmystere:
            print("Votre nombre est trop grand ! Essayer encore ")
        elif choix_nb==nbmystere:
            print("Bravo ! Vous avez trouvé !! \o/")
            stop=True
            nb_essai=0
            
        nb_essai=nb_essai-1



def jeu_multi_illimited():
    choix_limite=False
    players=['' for i in range(0,2,1)]
    for i in range(0,2,1):
        print("Quel est le nom du joueur ",i," ?")
        players[i]=input()

    while(not choix_limite):
        limitemin=input("Quelle est la limite basse que vous voulez fixer ?? ")
        limitemax=input("Quelle est la limite haute que vous voulez fixer ?? ")
        limitemin=int(limitemin)
        limitemax=int(limitemax)
        if limitemin>limitemax:
            print("Le choix des limites n'a pas de sens ! Vous devez refaire le choix")
        else:
            print("Pas de souci pour l'intervalle !")
            choix_limite=True
    nbmystere=random.randint(limitemin,limitemax)
    print("Le nombre Mystère a été choisi entre ",limitemin, " et ",limitemax )
    choix_nb=limitemin-1
    stop=False
    compteur=0
    while(choix_nb!=nbmystere or not stop):
        print("Tour du joueur ", players[compteur%2])
        choix_nb=input("Votre hypothèse de nombre ? (pour quitter choisissez 'q') ---> ")
        if choix_nb=='q':
            print("Vous avez decidé d'arrêter le jeu... Dommage pour vous joueur ",players[compteur%2],"... le nombre à trouver était ", nbmystere)
            break
        choix_nb=int(choix_nb)
        if choix_nb>limitemax or choix_nb<limitemin:
            print("Le nombre choisi n'est pas dans l'intervalle !")
        elif choix_nb<nbmystere:
            print("Votre nombre est trop petit ! Essayer encore !")
        elif choix_nb>nbmystere:
            print("Votre nombre est trop grand ! Essayer encore ")
        elif choix_nb==nbmystere:
            print("Bravo ! Vous avez trouvé ",players[compteur%2]," !! \o/")
            stop=True
        compteur=compteur+1


def jeu_multi_limited():
    choix_limite=False
    players=['' for i in range(0,2,1)]
    for i in range(0,2,1):
        print("Quel est le nom du joueur ",i," ?")
        players[i]=input()
    while(not choix_limite):
        limitemin=input("Quelle est la limite basse que vous voulez fixer ?? ")
        limitemax=input("Quelle est la limite haute que vous voulez fixer ?? ")
        limitemin=int(limitemin)
        limitemax=int(limitemax)
        if limitemin>limitemax:
            print("Le choix des limites n'a pas de sens ! Vous devez refaire le choix")
        else:
            print("Pas de souci pour l'intervalle !")
            choix_limite=True
    nbmystere=random.randint(limitemin,limitemax)
    print("Le nombre Mystère a été choisi entre ",limitemin, " et ",limitemax )
    choix_nb=limitemin-1
    stop=False

    nb_essai=10
    print("Vous avez droit à ",math.floor(nb_essai/2)," !")
    compteur=0
    while(choix_nb!=nbmystere or not stop or nb_essai>0 ):
        print("Tour du joueur ", players[compteur%2])
        print("Il vous reste ", math.ceil(nb_essai/2)," !")
        choix_nb=input("Votre hypothèse de nombre ? (pour quitter choisissez 'q') ---> ")

        if nb_essai<=1:
            print("Vous n'avez plus d'essai ! le nombre mystère était ", nbmystere)
            break

        if choix_nb=='q':
            print("Vous avez decidé d'arrêter le jeu... Dommage pour vous joueur ",players[compteur%2],"... le nombre à trouver était ", nbmystere)
            break
        choix_nb=int(choix_nb)
        if choix_nb>limitemax or choix_nb<limitemin:
            print("Le nombre choisi n'est pas dans l'intervalle !")
        elif choix_nb<nbmystere:
            print("Votre nombre est trop petit ! Essayer encore !")
        elif choix_nb>nbmystere:
            print("Votre nombre est trop grand ! Essayer encore ")
        elif choix_nb==nbmystere:
            print("Bravo ! Vous avez trouvé ",players[compteur%2],"!! \o/")
            stop=True
            nb_essai=0
            
        nb_essai=nb_essai-1
        compteur=compteur+1



print("Jeu du nombre Mystère !!!")

choix_mode_bool=True
while choix_mode_bool:
    print("Quel mode vous intéresse ???? \n1. Mode solo illimité\n2. Mode solo limité\n3. Mode multi illimité\n4. Mode multijoueur limité\n5. Ne pas jouer")
    choix_mode=input("Votre choix --->")
    if choix_mode=='1':
        jeu_solo_illimited()
    elif choix_mode=='2':
        jeu_solo_limited()
    elif choix_mode=='3':
        jeu_multi_illimited()
    elif choix_mode=='4':
        jeu_multi_limited()
    elif choix_mode=='5':
        print("A plus !")
        choix_mode_bool=False
    else:
        print("Je ne comprends pas ! Recommencez ! ;)")
    