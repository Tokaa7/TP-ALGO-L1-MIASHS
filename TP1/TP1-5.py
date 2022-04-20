"""

    TP1 - 5.Approfondissement

"""

a=3150

def test_premier(a):
    cpt=1;
    for n in range(1,(a//2)+1) :
        if(a%n==0): cpt+=1
        if(cpt>2): return False
    return True

def facteurs_premiers(u) :
    i=2
    x=u
    nb=str(x) + ' = '
    while(x!=1) :
        pui=0
        if(test_premier(i)==True):
            while(x%i==0):
                pui+=1
                x//=i
            if(pui!=0):
                nb+= str(i)+"^"+str(pui) + ' * '
        i+=1
    nb=nb[:-2]
    print(nb)

facteurs_premiers(a)



#Autre solutions avec des listes :    
    
    
def listepremiers(u) :
    Liste=[]
    for i in range(2, u//2+1,1) :
        if (test_premier(i)==True) :
            Liste.append(i)
    return Liste

def facteurs_premiers2(u):
    indice=0
    x=u
    premiers=listepremiers(x)
    listeprem=[]
    listepui=[]
    
    while(x!=1):
        pui=0
        while(x%premiers[indice]==0):
            pui+=1
            x//=premiers[indice]
        if(pui!=0):
            listeprem.append(premiers[indice])
            listepui.append(pui)
        indice+=1
    
    return listeprem,listepui

facteurs,pui=facteurs_premiers2(a)

print('\n',a,'= ',end=" ")

for i in range(len(pui)) :
    if(i<len(pui)-1): print(facteurs[i],"^",pui[i],'*',end=" ")
else: print(facteurs[i],"^",pui[i])
print('\n\nNombres :\t',facteurs,'\nPuissances:\t',pui)