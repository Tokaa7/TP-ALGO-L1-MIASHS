def premier (a) :
    div=2
    
    for i in range(3,a//2,1):
        if a%i==0 :
            div+=1
    if div==2:
        return True
    else:
        return False
    

a=(input("Entrez un nombre :"))

print(premier(a))
