# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:40:39 2022

@author: Kevin Soares
"""

import matplotlib.pyplot as plt

def f(x):
    liste=[]
    
    for i in range(x):
        liste.append(i**2-i-1)
    return liste

def fsuiteV(n) :
    suiteVlist=[]
    for i in range(1,len(n)) :
        suiteVlist.append(n[i]/n[i-1])
        
    return suiteVlist

x=int(input("Entrez un nombre :"))

x1=range(0,x-1)
y=fsuiteV(f(x))

plt.plot(x1,y,'ro')
plt.show
