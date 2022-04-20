"""

    TP1 - 2.Structures de contrôle

"""

a = int(input("Entrez un nombre : "))


"""    Diviseurs dans l'ordre
i=2
while(i <= a//2):
    if (a%i==0): print(i,"divise",a)
    else : print(i,"ne divise pas",a)
    i+=1
    
"""

"""    Diviseurs dans l'odre inverse
i=a//2
while(i >= 2):
    if (a%i==0): print(i,"divise",a)
    else : print(i,"ne divise pas",a)
    i-=1
"""

"""     Diviseurs avec un for
for n in range(2, (a//2)+1) :
    if (a%n==0): print(n,"divise",a)
    else : print(n,"ne divise pas",a)
"""

"""     Compte les diviseurs """
cpt=1
for n in range(1, (a//2)+1) :
    if(a%n==0) :
        print(n,"divise",a)
        cpt+=1
    else : print(n,"ne divise pas",a)
    
if(cpt==2):print(a,"est premier")
else:
    if(cpt%2==0):print("nb diviseurs pairs")
    else:print("nb diviseurs impairs")