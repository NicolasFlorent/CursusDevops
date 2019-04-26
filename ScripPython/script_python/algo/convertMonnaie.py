import math
somme=input("Quelle est la somme d'argent que vous avez ??? ")
somme=int(somme)


billets=[500,200,100,50,20,10,5,2,1]
convert=[0,0,0,0,0,0,0,0,0,]

j=0
for i in billets:
    convert[j]=math.floor(somme/i)
    somme=somme-convert[j]*i
    j=j+1

print("Vous allez recevoir :")

for i in range(0,9,1):
    print(convert[i], " nombre de billets/pieces de ",billets[i])

# nbbillets500=0
# nbbillets200=0
# nbbillets100=0
# nbbillets50=0
# nbbillets20=0
# nbbillets10=0
# nbbillets5=0
# nbbillets2=0
# nbbillets1=0

# while(somme>0):
#     if math.floor(somme/500)!=0:
#         nbbillets500=math.floor(somme/500)
#         somme=somme-nbbillets500*500
#     elif math.floor(somme/200)!=0:
#         nbbillets200=math.floor(somme/200)
#         somme=somme-nbbillets200*200
#     elif math.floor(somme/100)!=0:
#         nbbillets100=math.floor(somme/100)
#         somme=somme-nbbillets100*100
#     elif math.floor(somme/50)!=0:
#         nbbillets50=math.floor(somme/50)
#         somme=somme-nbbillets50*50
#     elif math.floor(somme/20)!=0:
#         nbbillets20=math.floor(somme/20)
#         somme=somme-nbbillets20*20
#     elif math.floor(somme/10)!=0:
#         nbbillets10=math.floor(somme/10)
#         somme=somme-nbbillets10*10
#     elif math.floor(somme/5)!=0:
#         nbbillets5=math.floor(somme/5)
#         somme=somme-nbbillets5*5
#     elif math.floor(somme/2)!=0:
#         nbbillets2=math.floor(somme/2)
#         somme=somme-nbbillets2*2
#     elif math.floor(somme/1)!=0:
#         nbbillets1=math.floor(somme/1)
#         somme=somme-nbbillets1*1

# print("Vous allez recevoir :")
# print(nbbillets500," billets de 500")
# print(nbbillets200," billets de 200")
# print(nbbillets100," billets de 100")
# print(nbbillets50," billets de 50")
# print(nbbillets20," billets de 20")
# print(nbbillets10," billets de 10")
# print(nbbillets5," billets de 5")
# print(nbbillets2," pieces de 2")
# print(nbbillets1," pieces de 1")