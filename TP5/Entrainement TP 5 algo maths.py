# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 17:36:04 2022

@author: Romain
"""

"""    EXERCICE 1     """

def evalpoly ( listecoeff ,x):
    s =0.
    px =1
    for a in listecoeff :
        s=s+a*px
        px=px*x
    return s


def primitivepoly(liste_coeff):#ex:[8,2,-5,1]
    result=[0]
    for i in range(len(liste_coeff)):
        result.append(liste_coeff[i]/(i+1))
    return result

print(primitivepoly([8,2,-5,1])) 

def integralepoly(a,b,liste_coeff): #fonctionne pas
    Fb=0
    Fa=0
    for i in range(len(liste_coeff)):
        Fb=Fb+liste_coeff[i]*(b**i)
        Fa=Fa+liste_coeff[i]*(a**i)
    
    return Fb-Fa

print(integralepoly(0,1,[8,2,-5,1]))


"""    EXERCICE 2     """

def f(x):
    return x/(x**2+1)


def riemanngauche(n):#Question 1
    pas=1/n
    som=0
    liste_abs=[(1/n)*i for i in range(0,n+1)] #liste des xi
    for i in range(len(liste_abs)-1):
        som+=(liste_abs[i+1]-liste_abs[i])*f(liste_abs[i])#calcul de la somme
    return som



def riemann2(n,epsilon):#Question 2
    pas=1/n
    liste_abs=[(1/n)*i for i in range(0,n+1)] #liste des xi
    som=[liste_abs[1]*f(0)]#creation de la liste de termes
    som.append(pas*f(pas))
    i=0
    
    while abs(som[i]-som[i+1])>epsilon and i<1000:
        som.append((liste_abs[i+1]-liste_abs[i])*f(liste_abs[i]))#ajout du terme
        i+=1
    return i#nombre de tours de boucle
#print(riemann2(21,0.0001))



def riemannmilieu(n):#Question 3
    pas=1/n
    som=0
    liste_abs=[(1/n)*i for i in range(0,n+1)] #liste des xi
    for i in range(len(liste_abs)-1):
        moy=(f(liste_abs[i])+f(liste_abs[i+1]))/2
        som+=(liste_abs[i+1]-liste_abs[i])*moy#calcul de la somme
    return som



def riemann4(n,epsilon):#Question 4
    pas=1/n
    liste_abs=[(1/n)*i for i in range(0,n+1)] #liste des xi
    som=[liste_abs[1]*f(0)]#creation de la liste de termes
    som.append(pas*f(pas))
    i=0
    
    while abs(som[i]-som[i+1])>epsilon and i<1000:
        moy=(f(liste_abs[i])+f(liste_abs[i+1]))/2
        som.append((liste_abs[i+1]-liste_abs[i])*moy)#ajout du terme
        i+=1
    return i#nombre de tours de boucle
#print(riemann2(21,0.0001))



"""    EXERCICE 3     """

def trapezes(a,b,n):
    h=(b-a)/n
    x=a
    u=(h/2)*f(x)
    
    for i in range(1,n-1):
        u=h*f(x)+u
        x=x+h
    
    u=(h/2)*f(x)+u
    return u
 













     