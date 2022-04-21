# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 08:48:36 2022

@author: Romain
"""
from PIL import Image
import numpy as np

"""EXERCICE 1"""


# A=np.array([[1,-1,0],[0,1,-1],[1,1,1]],dtype=float)
# B=np.array([[1,1,1,-3],[2,-2,2,5],[1,2,3,1],[-1,2,-2,-4]],dtype=float)

# #Q1##################
# A_diag=np.diag([1,-1,1])
# B_diag=np.diag([1,-1,1,-1])


# #Q2###################
# A=A+A_diag
# B=B+B_diag
# #print(A,"\n\n",B)


# #Q3###################
# A2=np.copy(A*2)
# B2=np.copy(B*2)
# #print(A2,"\n\n",B2)


# #Q4###################
# for i in range(len(A2)):
#     A2[i]=A2[i]*(i+1)
   
# for i in range(len(B2)):
#     B2[i]=B2[i]*(i+1)
    
# #print(A2,"\n\n",B2) 


# #Q5###################
# A2[1]=A2[1]/3
# B2[1]=B2[1]/3
# #print(A2,"\n\n",B2) 


# #Q6###################
# A2[[0,2]]=A2[[2,0]] #echange des lignes 0 et 2
# B2[[0,2]]=B2[[2,0]]

# A2[:,[0,2]]=A2[:,[2,0]]#echange des colonnes 0  et 2
# B2[:,[0,2]]=B2[:,[2,0]]

# #print(A2,"\n\n",B2) 




"""EXERCICE 2"""

# #Q1###################
# image=Image.open("chat.png")
# tab_image=np.array(image)#tableau avec les couleurs 

# nb_lignes,nb_colonnes, _ =tab_image.shape

# for i in range(nb_lignes):#on met le bleu et vert de chaque pixel a 0
#     for j in range(nb_colonnes):
#         tab_image[i][j][1]=0
#         tab_image[i][j][2]=0

# Image.fromarray(tab_image).save("resultat1.png")#on sauvegarde l'image dans le meme dossier pr voir le resultat


# #Q2###################
# image2=Image.open("chat.png")
# tab_image2=np.asarray(image2)
# nb_lignes2,nb_colonnes2, _ =tab_image2.shape

# j=nb_lignes2-1
# for i in range(nb_lignes2//2):#on s'arrete a la moitie car sinon on va echanger 2 fois
#     tab_image2[[i,j]]=tab_image2[[j,i]]#on echange chaque ligne 
#     j=j-1
    
# Image.fromarray(tab_image2).save("resultat2.png")


# #Q3####################
# image3=Image.open("chat.png")
# tab_image3=np.asarray(image3)
# nb_lignes3,nb_colonnes3, _ =tab_image3.shape

# j=nb_colonnes3-1
# for i in range(nb_colonnes3//2):
#     tab_image3[:,[i,j]]=tab_image3[:,[j,i]]
#     j=j-1
# Image.fromarray(tab_image3).save("resultat3.png")


# #Q4####################
# image4=Image.open("chat.png")
# tab_image4=np.asarray(image4)
# nb_lignes4,nb_colonnes4, _ =tab_image4.shape
   
# #pour inverser selon une diagonale il suffit d'inverser d'abord les lignes puis les colonnes
# j=nb_lignes3-1
# for i in range(nb_lignes4//2):#echange des lignes
#     tab_image4[[i,j]]=tab_image4[[j,i]]
#     j=j-1
    
# j=nb_colonnes4-1
# for i in range(nb_colonnes4//2):#echange des colonnes
#     tab_image4[:,[i,j]]=tab_image4[:,[j,i]]
#     j=j-1
    
        
# Image.fromarray(tab_image4).save("resultat4.png")


# #Q5################♣####
# image5=Image.open("chat.png")
# tab_image5=np.asarray(image5)
# nb_lignes5,nb_colonnes5, _ =tab_image5.shape

# for i in range(nb_lignes5):
#     for j in range(nb_colonnes5):
#         moy=(tab_image5[i,j,0]+tab_image5[i,j,1]+tab_image5[i,j,2])/3
#         tab_image5[i,j,0]=moy
#         tab_image5[i,j,1]=moy
#         tab_image5[i,j,2]=moy
        
# Image.fromarray(tab_image5).save("resultat5.png")


# image6=Image.open("chat.png")
# tab_image6=np.asarray(image6)
# nb_lignes6,nb_colonnes6, _ =tab_image6.shape

# for i in range(nb_lignes6):
#     for j in range(nb_colonnes6):
#         moy=(299*tab_image6[i,j,0]+587*tab_image6[i,j,1]+114*tab_image6[i,j,2])/1000
#         tab_image6[i,j,0]=moy
#         tab_image6[i,j,1]=moy
#         tab_image6[i,j,2]=moy
        
# Image.fromarray(tab_image6).save("resultat6.png")




"""EXERCICE 3"""

def convolution(M,noy):
    convo=0
    n=len(M)
    for i in range(n):
        for j in range(n):
            convo+=M[i][j]*noy[n-i-1][n-j-1]
    return convo

# A=np.array([[1,2,4],[-1,0,1],[1,-2,3]])
# noy=np.array([[-1,2,0],[4,0,0],[2,3,1]])


def image_filtree(image,tab_pixel,noy):
    for i in range(1,len(tab_pixel)-1):
        for j in range(1,len(tab_pixel(0)-1)):
            A=np.array([[]])


    