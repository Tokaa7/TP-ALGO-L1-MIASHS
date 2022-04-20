"""

    TP3 - 0.Premiers Exemples

"""

import matplotlib.pyplot as plt

def termesu(q,alpha,epsilon):
    u=q**(0**alpha)
    uu=q**(1**alpha)
    liste=[u,uu]
    n=2;cpt=0
    while(abs(uu-u)>epsilon):
        if(cpt>100):return liste
        u=uu
        uu=q**(n**alpha)
        n+=1
        liste.append(uu)
        cpt+=1
    return liste

def termesu2(q,alpha,epsilon):
    u=q**(alpha**0)
    uu=q**(alpha**1)
    liste=[u,uu]
    n=2;cpt=0
    while(abs(uu-u)>epsilon):
        if(cpt>100):return liste
        u=uu
        uu=q**(alpha**n)
        n+=1
        liste.append(uu)
        cpt+=1
    return liste

eps=0.01

print("\nTermesu 1 :",termesu(0.9,3,eps))
y1=termesu(0.9,3,eps)
x1=range(len(y1))
"""
print("\n",termesu(0.9,3,eps))
print("\n",termesu(0.3,3,eps))
print("\n",termesu(0.3,1.1,eps))
"""

print("\nTermesu 2 :",termesu2(0.9,3,eps))
y2=termesu2(0.9,3,eps)
x2=range(len(y2))

plt.plot(x1,y1,'b')
plt.plot(x2,y2,'r')