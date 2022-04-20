"""

    TP1 - 3.Fonctions

"""

def test_premier(a):
    cpt=1;
    for n in range(1,(a//2)+1) :
        if(a%n==0): cpt+=1
    if(cpt==2): return True
    return False

a=int(input("Entrez un nombre :"))
print("Test premier de",a,":",test_premier(a))