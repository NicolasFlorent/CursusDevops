print("Vous allez dessiner un rectangle d'étoile !")
longueur = input("Combien d'étoile pour la longueur?? ")
longueur=int(longueur)
largeur = input("Combien d'étoile pour la largeur?? ")
largeur=int(largeur)
print("")

for i in range(0,largeur,1):
    for j in range(0,longueur,1):
        print("*",end='')
    print("")

print("")