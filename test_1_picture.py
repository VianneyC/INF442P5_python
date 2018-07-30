#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 16:52:41 2018

@author: vianney
"""

import numpy as np
import skimage.data
from skimage import transform
from skimage.color import rgb2gray
import os

#returns the pixels sum in the given rectangle on the n-th image
def sum_rect(x, y, w, h) :
    x, y, w, h = int(x), int(y), int(w), int(h)
    res = image_integral[y][x]
    res += image_integral[y+h][x+w]
    res -= image_integral[y][x+w]
    res -= image_integral[y+h][x]
    return res

#computes and returns the i-th feature of the n-th image
def calc_1feature(i) :
    feature_pattern = features_patterns_list[i]
    feature = feature_pattern[0]
    x_origin = feature_pattern[1][0]
    y_origin = feature_pattern[1][1]
    width = feature_pattern[1][2]
    height = feature_pattern[1][3] 
    if(feature == 1) :
        res = sum_rect(x_origin+width,y_origin,width,height)
        res -= sum_rect(x_origin,y_origin,width,height)
    if(feature == 2) :
        res = sum_rect(x_origin,y_origin,width,height)
        res -= sum_rect(x_origin,y_origin+height,width,height)
    if(feature == 3) :
        res = sum_rect(x_origin+width,y_origin,width,height)
        res -= sum_rect(x_origin,y_origin,width,height)
        res -= sum_rect(x_origin+2*width,y_origin,width,height)
    if(feature == 4) :
        res = sum_rect(x_origin+width,y_origin,width,height)
        res += sum_rect(x_origin,y_origin+height,width,height)
        res -= sum_rect(x_origin,y_origin,width,height)
        res -= sum_rect(x_origin+width,y_origin+height,width,height)
    return res

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

#computes and returns the value of h(i,c) = h_i(x)
#where i is the number of the classifier and f
#the f-th feature of image x
def h(i, f) :
        if(classifiers[i][0] * f + classifiers[i][1] >= 0) :
            return 1
        return -1
"""
string = input("Name to picture to test : ")
string+=".jpg"
string_path = os.path.join("/home/vianney/Documents/",string)
print(string_path)
"""
string_path = os.path.join("/home","vianney/Documents/visage.jpeg")
picture = skimage.data.imread(string_path)
picture_final = rgb2gray(np.array(transform.resize(picture, (92,112))))
image_integral = integral_image(picture_final)

print("**** testing picture ****")
tot = 0
for i in range(len_vec_features) :
    feature_i = calc_1feature(i)
    tot += h(i, feature_i)
tot = float(tot) / len_vec_features
if int(tot > 0) *2 - 1 == 1 :
    print("There is a visage with probability {0}".format(((tot+1.)/2.)))
else :
    print("There is no visage with probability {0}".format(((tot+1.)/2.)))
print("---- done ----")
