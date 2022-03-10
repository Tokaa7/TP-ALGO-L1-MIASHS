# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 19:12:48 2022

@author: Kevin Soares
"""
##################GOOD##############################

def test_premier(nb) : 
    div=2
    for i in range(2,nb//2) :
        if nb%i==0 :
            div+=1
    
    if div==2 :
        return True
    else :
        return False
    
################################################

def listpremier(u) :
    Liste=[]
    for i in range(2, u//2+1,1) :
        if (test_premier(i)==True) :
            Liste.append(i)
    return Liste

################################################

x=int(input("Entrez un nombre :"))
result=str(x) + ' = '
indice = 0
pui = 0
premiers=listpremier(x)
Liste_nbpremiers=[]
Liste_pui=[]
 
print("\n Nombres premiers qui précèdent",x,"/ 2 : \n", premiers, "\n")

while (x!=1) :
    pui=0
    while (x % premiers[indice]==0) :
        pui+=1
        x=x//premiers[indice]
    if (pui!=0) :
       Liste_nbpremiers.append(premiers[indice])
       Liste_pui.append(pui)
    indice+=1


print("Nombres premiers :",Liste_nbpremiers)
print("       Puissances:",Liste_pui)
