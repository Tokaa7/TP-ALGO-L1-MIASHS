# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 17:06:53 2022

@author: vdi41005717
"""

from PIL import Image
import numpy as np



def fonction(tab_image,seuil):
    nb_lignes,nb_colonnes,_=tab_image.shape
    
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            
            moy=(tab_image[i,j,0]+tab_image[i,j,1]+tab_image[i,j,2])/3
            if moy<seuil:
                tab_image[i,j,0]=0
                tab_image[i,j,1]=0
                tab_image[i,j,2]=0
            else:
                tab_image[i,j,0]=255
                tab_image[i,j,1]=255
                tab_image[i,j,2]=255
        
    return tab_image
        
image=Image.open("fraise.jpg")
mon_image=np.asarray(image)

mon_image=fonction(mon_image,45)

Image.fromarray(mon_image).save("image Romain.jpg")