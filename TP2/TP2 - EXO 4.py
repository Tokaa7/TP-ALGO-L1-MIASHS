# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:55:17 2022

@author: Kevin Soares
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x) :
    y=x**3-5*x**2+2*x+8
    
    return y

a=int(input("Entrez la première borne :"))
b=int(input("Entrez la deuxième borne :"))


x1=np.linspace(a, b,len(range(a,b))+1)
y1=f(x1)

plt.plot(x1,y1,'ro')
plt.xlabel("x")
plt.ylabel("f (x)")
plt.title("x^3 - 5x^2 + 2x + 8")

plt.axvline(0)
plt.axhline(0)
plt.show
