#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 09:21:47 2018

@author: vianney
"""

import os
import skimage.data
import array_from_string

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
len_train_dataset = len(train_images)
print("**** creating train_images_integral from train_images_integral.txt ****")
fichier = open("train_images_integral.txt","r")
train_images_integral = fichier.read()
fichier.close()
train_images_integral = array_from_string.arrayFromStringTrainImageIntegral(train_images_integral)
print("---- done ----")
print("**** creating train_images_features from train_images_features.txt ****")
fichier = open("train_images_features.txt","r")
train_images_features = fichier.read()
fichier.close()
train_images_features = array_from_string.arrayFromStringTrainImageFeatures(train_images_features)
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