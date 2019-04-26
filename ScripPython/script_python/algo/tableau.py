import random

n=input("Quelle taille pour votre tableau ??? ")
n=int(n)
tab=[0 for i in range(n)]
for i in range(0,n,1):
    tab[i]=random.randint(0,10)
print(tab)

somme=0
for i in tab:
    somme = somme+ i

print("La somme du tableau vaut ",somme)
print("La moyenne vaut ",somme/n)

tab_tri=sorted(tab)
print(tab_tri)
if n%2==0:
    print("La médiane est " ,int((tab_tri[int(n/2)]+tab_tri[int(n/2-1)])/2))
else:
    print("La médiane est " ,tab_tri[int((n-1)/2)])

