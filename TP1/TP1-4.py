"""

    TP1 - 4.Listes

"""

a=int(input("Entrez un nombre :"))

listediv=[]
for n in range(1, (a//2)+1) :
    if (a%n==0): listediv.append(n)
listediv.append(a)
print(listediv)