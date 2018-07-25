#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:21:47 2018

@author: vianney
"""

import os
import skimage.data

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

#
def arrayFromStringTrainImageIntegral(image_integral_list) :
    return 1

#
def arrayFromStringTrainImageFeatures(image_features_list) :
    return 1

#creates the features_patterns_list from features_patterns.txt
def arrayFromStringFeaturesList(features_list) :
    array = []
    i = 1
    j = 0
    while i < len(features_list)-1 :
        temp_array = []
        #print(features_list[i] == "[")
        i+=1
        temp_array.append(int(features_list[i]))
        i+=1
        #print(features_list[i] == ",")
        i+=1
        #print(features_list[i] == "[")
        i+=1
        int_str = ""
        while(features_list[i] != ",") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array = [int(int_str)]
        #print(features_list[i] == ",")
        i+=1
        int_str = ""
        while(features_list[i] != ",") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array.append(int(int_str))
        #print(features_list[i] == ",")
        i+=1
        int_str = ""
        while(features_list[i] != ",") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array.append(int(int_str))
        #print(features_list[i] == ",")
        i+=1
        int_str = ""
        while(features_list[i] != "]") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array.append(int(int_str))
        temp_array.append(temp_temp_array)
        #print(features_list[i] == "]")
        i+=1
        #print(features_list[i] == "]")
        i+=1
        #print(features_list[i] == ",")
        i+=1
        #print(temp_array)
        array.append(temp_array)
        j += 1
        #print(j)
    return array
        

#loads train_images and train_labels
print("**** loading train_images, train_labels ****")
train_images, train_labels = load_data(os.path.join("/home/vianney/Documents","INF442P5_python/data/train/"))
print("---- done ----")


#reads arrays for train_images_integral and train_images_features from .txt
#
#train_images_features = [ ...
#                          ...
#                          [[i1, i2, ...], [feature_i1_n, feature_i2_n, ...]],
#                          ...
#                          ... ]
#with line n containing features of image n
#
len_data_set = len(train_images)
print("**** creating train_images_integral from train_images_integral.txt ****")
fichier = open("train_images_integral.txt","r")
train_images_integral = fichier.read()
fichier.close()
train_images_integral = arrayFromStringTrainImageIntegral(train_images_integral)
print("---- done ----")
print("**** creating train_images_features from train_images_features.txt ****")
fichier = open("train_images_features.txt","r")
train_images_features = fichier.read()
fichier.close()
train_images_features = arrayFromStringTrainImageFeatures(train_images_features)
print("---- done ----")


#creates features_patterns_list from features_patterns.txt
print("**** creating features_patterns_list from features_patterns.txt ****")
fichier = open("features_patterns.txt","r")
features_patterns_list = fichier.read()
fichier.close()
features_patterns_list = arrayFromStringFeaturesList(features_patterns_list)
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