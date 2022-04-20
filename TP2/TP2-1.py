"""

    TP2 - 1.Visualiser une suite de valeurs discrètes

"""

import matplotlib.pyplot as plt

def fibo_liste(n):
    f=1
    ff=1
    fiboliste=[ff,f]
    for i in range(2,n+1) :
        aux=f
        f+=ff
        fiboliste.append(f)
        ff=aux
    return fiboliste

def suiteV(n):
    fibo=fibo_liste(n+1)
    suite=[]
    for i in range(0,n+1) :
        V=fibo[i+1]/fibo[i]
        suite.append(V)
    return suite

def fsuiteV(n):
    liste_suitev=suiteV(n)
    liste_f=[]
    for i in range(0,n+1):
        x=liste_suitev[i]
        x=x**2-x-1
        liste_f.append(x)
    return liste_f


n=int(input("Entrez une valeur pour n :"))

# Graphique suite Fibonacci
plt.subplot(131) # = 1 ligne / 3 colonnes / graphe 1
x_fibo=range(n+1)
y_fibo=fibo_liste(n)
print(y_fibo)

plt.plot(x_fibo,y_fibo,'y-.')
plt.title("Fibonacci")
plt.xlabel("n")
plt.ylabel("F_n")

# Graphique suiteV
plt.subplot(132)
x_suiteV=range(n+1)
y_suiteV=suiteV(n)
print(suiteV(n))

plt.plot(x_suiteV,y_suiteV,'bo')
plt.title("SuiteV")
plt.xlabel("n")

# Graphique fsuiteV
plt.subplot(133)
x_fsuiteV=range(n+1)
y_fsuiteV=fsuiteV(n)
print(fsuiteV(n))

plt.plot(x_fsuiteV,y_fsuiteV,'bo')
plt.title("fsuiteV")
plt.xlabel("n")
