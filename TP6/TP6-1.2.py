"""

    TP6 - 1.2 Les matrices avec numpy

"""

from PIL import Image
import numpy as np

########################################################################

image_1=Image.open("chat_v1.png")
mon_image=np.asarray(image_1)
nb_lignes ,nb_colonnes,_= mon_image.shape

for i in range(nb_lignes): #on met le bleu et vert de chaque pixel a 0
    for j in range(nb_colonnes):
        mon_image[i][j][1]=0
        mon_image[i][j][2]=0
        
Image.fromarray(mon_image).save("chat_v2.png") #image sans bleu et vert

########################################################################

image_2=Image.open("chat_v1.png")
mon_image2=np.asarray(image_2)
nb_lignes2, nb_colonnes2, _2= mon_image.shape

j=nb_lignes2-1
for i in range(nb_lignes2//2): #on s'arrete a la moitie car sinon on va echanger 2 fois
    mon_image2[[i,j]] = mon_image2[[j,i]]#on echange chaque ligne 
    j-=1
    
Image.fromarray(mon_image2).save("chat_v3.png") # image inversée horizontalement

########################################################################

image_3=Image.open("chat_v1.png")
mon_image3=np.asarray(image_3)
nb_lignes3, nb_colonnes3, _3= mon_image3.shape

j=nb_colonnes3-1
for i in range(nb_colonnes3//2) :
    mon_image3[:,[i,j]] = mon_image3[:,[j,i]]
    j-=1
    
Image.fromarray(mon_image3).save("chat_v4.png") # image inversée verticalement

########################################################################

image_4=Image.open("chat_v1.png")
mon_image4=np.asarray(image_4)
nb_lignes4, nb_colonnes4, _4= mon_image4.shape

j=nb_lignes4-1
for i in range(nb_lignes4//2):
    mon_image4[[i,j]] = mon_image4[[j,i]]
    j-=1

j=nb_colonnes4-1
for i in range(nb_colonnes4//2) :
    mon_image4[:,[i,j]] = mon_image4[:,[j,i]]
    j-=1
    
Image.fromarray(mon_image4).save("chat_v5.png") # image inversée diagolament

########################################################################

image_5=Image.open("chat_v1.png")
mon_image5=np.asarray(image_5)
nb_lignes5, nb_colonnes5, _5= mon_image5.shape

for i in range(nb_lignes5):
    for j in range(nb_colonnes5):
        moy=(mon_image5[i,j,0]+mon_image5[i,j,1]+mon_image5[i,j,2])/3
        mon_image5[i,j,0]=moy
        mon_image5[i,j,1]=moy
        mon_image5[i,j,2]=moy

Image.fromarray(mon_image5).save("chat_v6.png") # image gris 1

########################################################################

image_6=Image.open("chat_v1.png")
mon_image6=np.asarray(image_6)
nb_lignes6, nb_colonnes6, _6= mon_image6.shape

for i in range(nb_lignes6):
    for j in range(nb_colonnes6):
        moy=(299*mon_image6[i,j,0]+587*mon_image6[i,j,1]+114*mon_image6[i,j,2])/1000
        mon_image6[i,j,0]=moy
        mon_image6[i,j,1]=moy
        mon_image6[i,j,2]=moy
        
Image.fromarray(mon_image6).save("chat_v7.png") # image gris 2
