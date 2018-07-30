#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:24:16 2018

@author: vianney
"""

import os
import skimage.data
import array_from_string
import numpy as np
import progressbar

#loads images and labels from parent directory
def load_data(data_directory):
    directories = [d for d in os.listdir(data_directory) 
                   if os.path.isdir(os.path.join(data_directory, d))]
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(data_directory, d)
        file_names = [os.path.join(label_directory, f) 
                      for f in os.listdir(label_directory) 
                      if f.endswith(".jpg")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append((1 if str(label_directory)[-4:] == "/pos" else -1))
    return images, labels

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

#loads test_images and test_labels
print("**** loading test_images, test_labels ****")
test_images, test_labels = load_data(os.path.join("/home/vianney/Documents","INF442P5_python/data/test/"))
len_test_dataset = len(test_images)
print("---- done ----")

#reads arrays for test_images_integral
print("**** creating test_images_integral from test_images_integral.txt ****")
fichier = open("test_images_integral.txt","r")
test_images_integral = fichier.read()
fichier.close()
test_images_integral = array_from_string.arrayFromStringTrainImageIntegral(test_images_integral)
print("---- done ----")

#check if test_images_integral is complete and compute if not
print("**** checking test_images_integral ****")
compute = True
need_to_update_test_images_integral_on_drive = False
p = progressbar.ProgressBar(len_test_dataset)
old_n = 0
p.animate(0)
for n in range(len_test_dataset) :
    if(test_images_integral[n] == []) :
        if compute :
            compute = False
            print("**** computing missing test_images_integral ****")
        test_images_integral[n] = list(integral_image(test_images[n]))
        need_to_update_test_images_integral_on_drive = True
    if(n - old_n > len_test_dataset /100.) :
        p.animate(n)
        old_n = n
p.ciao()

if not compute :
    print("---- done ----")
print("---- done ----")

#saves test_images_integral to .txt if needed
if(need_to_update_test_images_integral_on_drive) :
    print("**** saving test_images_integral.txt ****")
    fichier = open("test_images_integral.txt","w")
    fichier.write("[")
    p = progressbar.ProgressBar(len(test_images_integral))
    old_i = 0
    p.animate(0)
    for i in range(len(test_images_integral)) :
        arr = test_images_integral[i]
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
        
        if i < len(test_images_integral) - 1 :
            fichier.write(", ")
        if(i- old_i > len(test_images_integral) /100.) :
            p.animate(i)
            old_i = i
    fichier.write("]")
    fichier.close()
    p.ciao()
    print("---- done ----")
    
#creates features_patterns_list from features_patterns.txt
print("**** creating features_patterns_list from features_patterns.txt ****")
fichier = open("features_patterns.txt","r")
features_patterns_list = fichier.read()
fichier.close()
features_patterns_list = array_from_string.arrayFromStringFeaturesList(features_patterns_list)
len_vec_features = len(features_patterns_list)
print("---- done ----")
