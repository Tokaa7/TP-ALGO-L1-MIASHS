"""

    TP3 - 1.1 Calcul de valeurs remarquables

"""

from numpy import exp

def suiteVn(x,epsilon):
    v=1
    n=1
    frac=(x**n)/n
    vv= v + frac
    while(abs(vv-v)>epsilon):
        v=vv
        n+=1
        frac*=x/n
        vv+=frac
    return vv

print("Suite e^1:",suiteVn(1,0.000000001))
print("Numpy e^1:",exp(1))
print("Suite e^2 :",suiteVn(2,0.000000001))
print("Numpy e^2:",exp(2))

