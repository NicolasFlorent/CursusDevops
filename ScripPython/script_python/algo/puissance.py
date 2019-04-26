def puissance(a,b):
    result=a
    for i in range(0,b-1,1):
        result=result*a
    return result


a=input("Quelle est la valeur de a ??? ")
a=int(a)
b=input("Quelle est la valeur de la puissance b ??? " )
b=int(b)

print("Le résultat est ",puissance(a,b))