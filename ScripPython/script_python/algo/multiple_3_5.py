n=input("Donnez un n maximum :")
n=int(n)

for i in range(1,n,1):
    if (i%3==0 and i%5==0):
        print(i, "multiple de 3 et 5")
    elif (i%3==0):
        print(i, "multiple de 3" )
    elif (i%5==0):
        print(i, "multiple de 5")

