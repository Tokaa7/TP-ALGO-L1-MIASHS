"""

    TP4 - 1.1 Algorithme de Newton

"""

import matplotlib.pyplot as plt

def fonction(x,A):
    return x**2-A

def fp(x):
    return 2*x

def Newtonracine(a,epsilon,A) :
    err=1
    listeu=[]
    while(err>epsilon): 
        x=a-fonction(a,A)/fp(a)
        err=abs(x-a)
        a=x
        listeu.append(x)
    
    return listeu

A=int(input("Nombre dont vous cherchez la racine :"))

y=Newtonracine(1, 0.00000001, A)
x=range(len(y))
  
print(y) 

plt.axvline(0)
plt.axhline(0)
plt.xlabel("x")
plt.ylabel("f (x)")

plt.title(label="Calcul de la racine de A",fontsize=15,color="purple")

plt.plot(x,y,'r')
plt.show

#MANQUE LE 5)