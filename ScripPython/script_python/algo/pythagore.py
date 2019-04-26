import math

def isRectangle(a,b,c):
    return a**2+b**2==c**2


side=[0 for i in range(0,3,1)]
for i in range(0,3,1):
    print("Quelle est la valeur du coté ",i+1," ?")
    side[i]=input()
    side[i]=int(side[i])

side.sort()
if isRectangle(side[0],side[1],side[2]):
    print("Le triangle est rectangle !!!")
else:
    print("Le triangle n'est pas rectangle !!!")
