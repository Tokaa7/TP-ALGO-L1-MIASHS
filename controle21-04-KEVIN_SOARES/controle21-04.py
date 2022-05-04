"""

Contrôle 21/01/2022 Algo-Info
Kevin SOARES 41001212

"""

from PIL import Image
import numpy as np


def change_pixels(mat,seuil):
    
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            moy = (mat[i,j,0] + mat[i,j,1] + mat[i,j,2])/3
            if(moy<seuil):
                mat[i,j,0]=0
                mat[i,j,1]=0
                mat[i,j,2]=0
            else:
                mat[i,j,0]=255
                mat[i,j,1]=255
                mat[i,j,2]=255
    return mat
    
image1=Image.open("chat.png")
mon_image=np.asarray(image1)
nb_lignes,nb_colonnes,_=mon_image.shape

mon_image=change_pixels(mon_image,35) #seuil a 112 avec mon numéro étudiant(41001212) mais rend une image noire

Image.fromarray(mon_image).save("chat_v2.png")
