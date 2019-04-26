def creation_email(P,N,F):
    if not P and not N:
        print("Impossible !! il faut au moins un prénom ou un nom ! Tant pis pour vous ! Ciao !")
        exit()
    elif not F:
        print("Le fournisseur d'accès n'est pas renseigné !!! Impossible de créer l'adresse ! Dommage pour vous ! A plus !")
        exit()
    elif not P:
        E=N[:-1]+['@']+F[:-1]+['.','f','r','-1']
    elif not N:
        E=P[:-1]+['@']+F[:-1]+['.','f','r','-1']
    else:
        E=P[:-1]+['.']+N[:-1]+['@']+F[:-1]+['.','f','r','-1']
    return E


print("Vous allez rentrer votre adresse mail ! Attention a bien suivre les instructions sinon vous recommencerez au début !!!!!")
print("Règles à suivre:\n1. Minimum un prenom ou un nom\n2. Obligatoirement un fournisseur !\n3. Prenom + nom de taille inférieur à 15 !")

prenom=input("Un prénom ??? ---> ")
nom=input("Un nom ??? ---> ")
fournisseur=input("Votre fournisseur ??? ---> ")

P=[]
N=[]
F=[]

for i in prenom:
    P.append(i)
if P:
    P.append('-1')

for i in nom:
    N.append(i)
if N:
    N.append('-1')

for i in fournisseur:
    F.append(i)
if F:
    F.append('-1')


if len(P[:-1]+N[:-1])>15:
    print("Votre adresse est trop longue et donc invalide ! Recommencez.... du début ! (héhéhé)")
else:
    print("Bravo votre adresse respecte les règles !!! La voici : ",creation_email(P,N,F))

