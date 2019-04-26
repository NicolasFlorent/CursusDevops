import random

def creationTriplet(n,max):
    triplet=[random.randint(1,max-2)]
    j=1
    for i in range(1,n,1):
        triplet.append(random.randint(triplet[i-1]+1,max-j))
        j=j-1
    for i in range(0,n,1):
        if (random.randint(0,1)==1):
            triplet[i]=triplet[i]*-1
    return triplet


def testSolution(triplets, possibilite):
    compteur=0
    for triplet in triplets:
        for i in triplet:
            if i not in possibilite:
                compteur=compteur+1
        if compteur>=len(triplets[0]):
            return False
    return True



nbtriplet=2
max=10
n=3

triplets=[]
for i in range(0,nbtriplet,1):
    triplets.append(creationTriplet(n,max))

print(triplets)





# test=[i for i in range(1,max+1,1)]
# multi=[-1 for i in range (0,max,1)]
# print([x*y for x,y in zip(test,multi)])


possibility=[]
# possibility.append(test)

for i in range(0,max,1):
    print("retour")
    possibility.append("retour")
    temp=[i for i in range(1,max+1,1)]
    temp[i]=temp[i]*-1
    # for triplet in triplets:
    if testSolution(triplets,temp):
        print(temp)
    for j in range(i+1,max,1):
        temp[j]=temp[j]*-1
        # for triplet in triplets:
        if testSolution(triplets,temp):
            print(temp)
        # possibility.append(temp)
        # print(temp)
        # print(possibility)




