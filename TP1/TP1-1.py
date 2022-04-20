"""

    TP1 - 1.Environnement de programmation

"""

a = int(input("Entrez un nombre : "))   # Demande d'entrer une valeur et l'affecte à a
i=2                                     #initialise i à 2
while(i <= a//2):                       # Tant que i <= //2 (division entière)
    if (a%i==0): print(i,"divise",a)    #si reste de a/i =0, ecrire...
    i=i+1                               #rajoute 1 a i