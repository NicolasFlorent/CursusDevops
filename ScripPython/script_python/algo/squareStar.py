print("Vous allez dessiner un carré d'étoile !")
side = input("Combien d'étoile pour un coté ?? ")
side=int(side)

print("")

for i in range(0,side,1):
    for j in range(0,side,1):
        print("*",end='')
    print("")

print("")