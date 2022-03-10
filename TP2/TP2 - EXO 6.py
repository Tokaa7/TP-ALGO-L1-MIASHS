# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 23:26:19 2022

@author: Kevin Soares
"""

import matplotlib.pyplot as plt
import numpy as np

def heron(A,n) :
    liste=[]
    u=A
    for i in range(n) :
        u = (1/2)*(u+(A/u))
        liste.append(u)
    return liste


#

A = int(input("Entrez un nombre :"))
n = int(input("Entrez un rang n :"))

heronA=heron(A,n)

x=range(len(heronA))
y=heron(A,n)
print(y[len(heronA)-1])
print(np.sqrt(A))


plt.plot(x,y,'ro')
plt.show
