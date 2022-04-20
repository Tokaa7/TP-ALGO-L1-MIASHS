"""

    TP2 - 3.1 Approfondissement 

"""

import numpy as np
import matplotlib.pyplot as plt

def evalpoly(listecoeff, x):
    somme=0
    x_pui=1
    for a in listecoeff:
        somme+=a*x_pui 
        x_pui*=x
    return somme

coeffs=[]
degre=int(input("Entrer degré du polynome :"))
print("Entrer",degre+1,"coeffs du polynome un à un :")
for i in range(degre+1) :
    a=int(input())
    coeffs.append(a)

x=np.linspace(-10,10)
y=evalpoly(coeffs,x)
plt.plot(x,y,'r')
plt.title("f(x)")
plt.xlabel("x")
plt.ylabel("x^3 - 5x^2 + 2x + 8")
plt.axvline(0,0)
plt.axhline(0,0)