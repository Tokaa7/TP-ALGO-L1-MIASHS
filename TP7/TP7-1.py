"""

    TP7 - 1.Algorithme de Gauss

"""

def descente(A):
    nb_lignes=A.shape[0]
    for j in range(nb_lignes-1):
        pivot=A[j,j]
        
        for k in range(j+1,nb_lignes):
            A[k]-=(A[k,j]/pivot)*A[j]
        
        i=j
        while(A[i,j]==0 and i<nb_lignes-1):
            i+=1
            
        if(i!=nb_lignes): A[[j,i]]=A[[i,j]]
        else: return ("erreur")
        