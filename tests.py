#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:26:52 2018

@author: vianney
"""

"""
Viola & Jones applied to face detection in images
implemented in Python
"""

# import des modules
import os
import skimage.data
import numpy as np

def load_picture(string_path) :
    path = os.path.join("/home/vianney/Documents",string_path)
    return skimage.data.imread(path)

#computes integral_image of a given picture
def integral_image(picture) :
    integral_image = np.zeros(picture.shape)
    supp_image = np.zeros(picture.shape)
    
    nb_rows = picture.shape[0]
    nb_cols = picture.shape[1]
    
    for x in range(nb_cols) :
        for y in range(nb_rows) :
            supp_image[y][x] = picture[y][x] if (y==0) else supp_image[y-1][x] + picture[y][x]
            integral_image[y][x] = supp_image[y][x] if (x==0) else integral_image[y][x-1] + supp_image[y][x]
            
    return integral_image

image = load_picture("INF442P5_python/data/train/pos/im0.jpg")

integral_image = [[], [], integral_image(image), []]

fichier = open("ttttt.txt","w")
fichier.write("[")
for i in range(len(integral_image)) :
    arr = integral_image[i]
    if arr == [] :
        fichier.write("[]")
    else :
        fichier.write("[")
        for j in range(len(arr)) :
            array = arr[j]
            fichier.write(str(list(array)))
            if j < len(arr) - 1 :
                fichier.write(", ")
        fichier.write("]")
    if i < len(integral_image) - 1 :
        fichier.write(", ")
fichier.write("]")
fichier.close()
