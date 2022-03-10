# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:36:03 2022

@author: Kevin Soares
"""
import matplotlib.pyplot as plt

################################################

def calculfibo (n) :
    f=1
    ff =1
    fiboliste =[ff ,f]
    for i in range (3 ,n+1) :
        aux =f
        f=f+ff
        fiboliste . append (f)
        ff= aux
    return fiboliste

def suiteV(n) :
    suiteVlist=[]
    for i in range(1,len(n)) :
        suiteVlist.append(n[i]/n[i-1])
        
    return suiteVlist

################################################

n=int ( input ("Entrez un entier positif :") )

x1 = range(0,n)
y1 = calculfibo (n)


print ("Les",n,"premiers termes de la suite de fibonacci sont :")
print (y1,"\n")

x2=range(0,len(suiteV(y1)))
y2=suiteV(y1)

plt.plot(x1,y1,'ro')
plt.plot(x2,y2,'bo')
plt.title("R : Suite de Fibonacci | B : Suite V")

print(y2)

plt.show
