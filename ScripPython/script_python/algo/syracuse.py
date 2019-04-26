
un=input("Quel est votre premier terme de la suite de Syracuse ??? ---> ")
un=int(un)
compteur=0
print(un, end="  ")
while (un!=1):
    if un%2==0:
        un=int(un/2)
    else:
        un=int(3*un+1)
    print(un, end="  ")
    compteur=compteur+1
print("\nLa suite a convergé en ",compteur, "itérations !")
