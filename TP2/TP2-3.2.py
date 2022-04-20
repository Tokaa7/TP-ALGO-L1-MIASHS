"""

    TP2 - 3.2 Approfondissement 

"""

import matplotlib.pyplot as plt
from numpy import sqrt

def heron(A,n):
    u=A
    liste=[u]
    for i in range(n-1):
        u=(u+(A/u))/2
        liste.append(u)
    return liste

nb=int(input("Nombre dont la racine est souhaitée :"))
n=int(input("N terme de la suite souhaité :"))

x=range(n)
y=heron(nb,n)
plt.title("Algorithme d'Heron")
plt.xlabel("n")
plt.ylabel("sqrt(nb)")
plt.plot(x,y,'r')

print("\nAvec l'algorithme d'Heron :",y)
print("\nAvec sqrt de numpy :",sqrt(nb))