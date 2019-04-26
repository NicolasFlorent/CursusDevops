print("Vous allez dessiner un triangle d'étoiles !")
base=input("Combien d'étoiles voulez-vous pour la base du triangle? ")
base=int(base)

print("")

for i in range(0,base+1,1):
    for j in range(0,i,1):
        print("*",end='')
    print("")

print("")