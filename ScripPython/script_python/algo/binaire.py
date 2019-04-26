a=1101
b=13


def BinToTen(a):
    longueurNB=len(str(a))
    a_str=str(a)
    nb_base10=0
    j=0
    for i in range(longueurNB,0,-1):
        nb_base10=nb_base10+int(a_str[j])*(2**(i-1))
        j=j+1
    print(nb_base10)


def TenToBin(b):
    i=0
    tab=[]
    while (b>(2**i)):
        tab.append(0)
        i=i+1
    taille=len(tab)
    result=[]
    for i in range(taille,0,-1):
        result.append(int(b/(2**(i-1))))
        b=b%(2**(i-1))
    print(result)



BinToTen(a)
TenToBin(b)