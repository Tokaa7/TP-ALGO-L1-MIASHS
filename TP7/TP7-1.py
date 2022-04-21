"""

    TP7 - 1.Algorithme de Gauss

"""

def descente(A):
    nblignes=A.shape[0]
    for j in range(nblignes-1):
        pivot=A[j,j]
        for k in range(j+1,nblignes):
            A[k]-=(1[k,j]/pivot)*A[j]
