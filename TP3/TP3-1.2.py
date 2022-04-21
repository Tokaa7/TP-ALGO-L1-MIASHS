"""

    TP3 - 1.2 Calcul de valeurs remarquables

"""

import matplotlib.pyplot as plt
from numpy import exp

def suiteUn(a,epsilon):
    u=1
    n=1
    uu=(1+a/n)**n
    liste=[u,uu]
    while((abs(uu-u)) / (abs(u))>epsilon):
        u=uu
        n+=1
        uu=(1+a/n)**n
        liste.append(uu)
    return liste

print("Suite e^1 :",suiteUn(2,0.000000000001))
print("Numpy e^1:",exp(1))

y=suiteUn(2,0.0001)
x=range(len(y))
plt.plot(x,y,'r')

#Beaucoup plus lent que l'algorithme de TP3-1.1.py