pSeuil=2.3
vSeuil=7.41

pression=input("Quelle est votre valeur de pression ? ")
pression=int(pression)

volume=input("Quelle est votre valeur de volume ? ")
volume=int(volume)

if (pression>pSeuil and volume > vSeuil):
    print("Les deux seuils sont dépassés! Arrêt immédiat !")
elif (pression<pSeuil and volume > vSeuil):
    print("Diminuer le volume de l'enceinte !")
elif (pression>pSeuil and volume<vSeuil):
    print("Augmenter le volume de l'enceinte !")
else:
    print("Tout va bien !")