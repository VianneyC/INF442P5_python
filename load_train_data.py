#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:21:47 2018

@author: vianney
"""

import os
import skimage.data
import array_from_string
import numpy as np

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
            labels.append((1 if str(os.path.basename(data_directory)) == "pos" else -1))
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


#loads train_images and train_labels
print("**** loading train_images, train_labels ****")
train_images, train_labels = load_data(os.path.join("/home/vianney/Documents","INF442P5_python/data/train/"))
print("---- done ----")


#reads arrays for train_images_integral
len_train_dataset = len(train_images)
print("**** creating train_images_integral from train_images_integral.txt ****")
fichier = open("train_images_integral.txt","r")
train_images_integral = fichier.read()
fichier.close()
train_images_integral = array_from_string.arrayFromStringTrainImageIntegral(train_images_integral)
print("---- done ----")

#check if train_images_integral is complete and compute if not
print("**** checking train_images_integral ****")
compute = True
need_to_update_train_images_integral_on_drive = False
for n in range(len_train_dataset) :
    if(train_images_integral[n] == []) :
        if compute :
            compute = False
            print("**** computing missing train_images_integral ****")
        train_images_integral[n] = list(integral_image(train_images[n]))
        need_to_update_train_images_integral_on_drive = True
if not compute :
    print("---- done ----")
print("---- done ----")

#saves train_images_integral to .txt if needed
if(need_to_update_train_images_integral_on_drive) :
    print("**** saving train_images_integral.txt ****")
    fichier = open("train_images_integral.txt","w")
    fichier.write("[")
    for i in range(len(train_images_integral)) :
        arr = train_images_integral[i]
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
        
        if i < len(train_images_integral) - 1 :
            fichier.write(", ")
    fichier.write("]")
    fichier.close()
    print("---- done ----")

#creates features_patterns_list from features_patterns.txt
print("**** creating features_patterns_list from features_patterns.txt ****")
fichier = open("features_patterns.txt","r")
features_patterns_list = fichier.read()
fichier.close()
features_patterns_list = array_from_string.arrayFromStringFeaturesList(features_patterns_list)
len_vec_features = len(features_patterns_list)
print("---- done ----")





"""
Other functions than can be used if needed
"""

def load_data_from_directory(data_directory):
    labels = []
    images = []
    file_names = [os.path.join(data_directory, f) 
                  for f in os.listdir(data_directory) 
                  if f.endswith(".jpg")]
    for f in file_names:
        images.append(skimage.data.imread(f))
        labels.append(1 if str(os.path.basename(data_directory)) == "pos" else -1)
    return images, labels

def load_picture(string_path) :
    path = os.path.join("/home/vianney/Documents",string_path)
    return skimage.data.imread(path)