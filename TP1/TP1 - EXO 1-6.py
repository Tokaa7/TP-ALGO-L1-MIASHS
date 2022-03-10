# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 18:14:12 2022

@author: Tokaa
"""

def divs(a) :
    div=2
    listdiv=[1]

    for n in range(2,a//2) :
        if a%n==0 :
            listdiv.append(n)
            div+=1
            
    listdiv.append(a)
    return listdiv


a=int(input("Entrez un nombre :"))

"""
div=2
listdiv=[1]

for n in range(2,a//2) :
    if a%n==0:
        print(n,"divise",a)
        div+=1
        listdiv.append(n)
    else:
        print(n,"ne divise pas",a)

print("\n")    

if div%2==0 :
    print("Nombre div pair")
    
if div%2!=0 :
    print("Nombre div impair")
    
if div==2 :
    print(a,"est premier")
else:
    print(a,"n'est pas premier")
    
listdiv.append(a)

print("Diviseurs de",a,":",listdiv)
"""

print("Diviseurs de",a,":",divs(a))
