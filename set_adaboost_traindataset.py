#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:12:40 2018

@author: vianney
"""

import array_from_string
import progressbar

#returns the pixels sum in the given rectangle on the n-th image
def sum_rect(x, y, w, h, n) :
    x, y, w, h = int(x), int(y), int(w), int(h)
    res = train_images_integral[n][y][x]
    res += train_images_integral[n][y+h][x+w]
    res -= train_images_integral[n][y][x+w]
    res -= train_images_integral[n][y+h][x]
    return res

#computes and returns the i-th feature of the n-th image
def calc_1feature(n,i) :
    feature_pattern = features_patterns_list[i]
    feature = feature_pattern[0]
    x_origin = feature_pattern[1][0]
    y_origin = feature_pattern[1][1]
    width = feature_pattern[1][2]
    height = feature_pattern[1][3] 
    if(feature == 1) :
        res = sum_rect(x_origin+width,y_origin,width,height,n)
        res -= sum_rect(x_origin,y_origin,width,height,n)
    if(feature == 2) :
        res = sum_rect(x_origin,y_origin,width,height,n)
        res -= sum_rect(x_origin,y_origin+height,width,height,n)
    if(feature == 3) :
        res = sum_rect(x_origin+width,y_origin,width,height,n)
        res -= sum_rect(x_origin,y_origin,width,height,n)
        res -= sum_rect(x_origin+2*width,y_origin,width,height,n)
    if(feature == 4) :
        res = sum_rect(x_origin+width,y_origin,width,height,n)
        res += sum_rect(x_origin,y_origin+height,width,height,n)
        res -= sum_rect(x_origin,y_origin,width,height,n)
        res -= sum_rect(x_origin+width,y_origin+height,width,height,n)
    return res

#computes and returns the value of h(i,c) = h_i(x)
#where i is the number of the classifier and f
#the f-th feature of image x
def h(i, f) :
        if(classifiers[i][0] * f + classifiers[i][1] >= 0) :
            return 1
        return -1



print("**** getting lambda_list_train from lambda_list_train.txt ****")
fichier = open("lambda_list_train.txt","r")
lambda_list_train = fichier.read()
fichier.close()
lambda_list_train = array_from_string.arrayFromStringLambdaTrain(lambda_list_train)
print("---- done ----")

print("**** getting alpha_list_train from alpha_list_train.txt ****")
fichier = open("alpha_list_train.txt","r")
alpha_list_train = fichier.read()
fichier.close()
alpha_list_train = array_from_string.arrayFromStringAlphaTrain(alpha_list_train)
N = len(alpha_list_train)
print("---- done ----")


print("**** computing train_wrong_classified_lists ****")
train_wrong_classified_lists = []
p = progressbar.ProgressBar(len_vec_features)
old_i = 0
for i in range(len_vec_features) :
    array = []
    for j in range(len_train_dataset) :
        if h(i, calc_1feature(j, i)) != train_labels[j] :
            array.append(j)
    train_wrong_classified_lists.append(array)
    if(i - old_i > len_vec_features / 100.) :
        p.animate(i)
        old_i = i
p.ciao()
print("---- done ----")