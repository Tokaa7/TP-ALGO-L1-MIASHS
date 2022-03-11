# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt

def suite(a,E) :
    u=a
    u1=(2/3)*u+(a/(3*u))
    liste=[u,u1]
    while(abs(u1-u)>E) :
        u=u1
        u1=(2/3)*u+(a/(3*u))
        liste.append(u)
            
    return liste

##########################################

# debut programme principal

a=89
E=int(input("Choissisez un Epsilon > 0 :"))

print("Resultat :", suite(a,E))

y=suite(a,E)
x=range(len(y))

plt.axvline(0)
plt.axhline(0)

plt.plot(x,y,'ro')
plt.show
