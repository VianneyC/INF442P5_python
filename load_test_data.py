#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:24:16 2018

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



#loads test_images and test_labels
print("**** loading train_images, train_labels ****")
test_images, test_labels = load_data(os.path.join("/home/vianney/Documents","INF442P5_python/data/test/"))
len_test_dataset = len(test_images)
print("---- done ----")