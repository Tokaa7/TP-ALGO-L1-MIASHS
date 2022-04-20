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

eps=0.01

print("\n",termesu(0.9,1.1,eps))
y1=termesu(0.9,1.1,eps)
x1=range(len(y1))

print("\n",termesu(0.9,3,eps))
y2=termesu(0.9,3,eps)
x2=range(len(y2))

print("\n",termesu(0.3,3,eps))
y3=termesu(0.3,3,eps)
x3=range(len(y3))

print("\n",termesu(0.3,1.1,eps))
y4=termesu(0.3,1.1,eps)
x4=range(len(y4))

plt.plot(x1,y1,'r')
plt.plot(x2,y2,'b')
plt.plot(x3,y3,'g')
plt.plot(x4,y4,'y')

#q5