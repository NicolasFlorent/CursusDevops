import math
print("Vous allez dessiner un triangle d'étoiles !")
base=input("Combien d'étoiles voulez-vous pour la base du triangle? ")
base=int(base)

print("")

for i in range(base,0,-2):
    for j in range(0,math.floor(i/2),1):
        print(" ",end='')
    for k in range(math.floor(i/2),math.floor(base/2),1):
        print("*",end='')
    print("*",end='')
    for k in range(math.floor(i/2),math.floor(base/2),1):
        print("*",end='')
    print("")