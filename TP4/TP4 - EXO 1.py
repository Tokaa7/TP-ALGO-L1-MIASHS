# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
  
print(Newtonracine(1,0.00000001,A)) 

y=Newtonracine(1, 0.00000001, 10)
x=range(len(y))

plt.plot(x,y,'r')
plt.show
