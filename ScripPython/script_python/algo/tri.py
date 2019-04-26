import random
import time

def permutation(a,b):
    a=a+b
    b=a-b
    a=a-b
    return a,b

def triBulle(tab):
    print("Tri à bulles !")
    for i in range(len(tab)-1,1,-1):
        for j in range(0,i,1):
            if (tab[j+1]<tab[j]):
                tab[j+1],tab[j]=permutation(tab[j+1],tab[j])
    print(tab)

def triFusion(tab):
    if len(tab)<=1:
        return tab
    else:
        return fusion(triFusion(tab[:int(len(tab)/2)]),triFusion(tab[int(len(tab)/2):]))

def fusion(A,B):
    if not A:
        return B
    elif not B:
        return A
    elif A[0]<=B[0]:
        return [A[0]]+fusion(A[1:],B)
    elif B[0]<=A[0]:
        return [B[0]]+fusion(A,B[1:])



limite=1500
tab=[random.randint(0,100) for i in range(0,limite,1)]

print(tab)
second1=time.time()
triBulle(tab)
second2=time.time()
print("Temps de tri : ", second2-second1)

second3=time.time()
print("Tri Fusion !")
tab_tri=triFusion(tab)
print(tab_tri)
second4=time.time()
print("Temps de tri : ", second4-second3)
