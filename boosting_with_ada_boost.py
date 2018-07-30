#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:01:37 2018

@author: vianney
"""

import numpy as np
import array_from_string

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

#error function
def E(h,c) :
    return int(h != c)

def eps(i) :
    res = 0
    for j in range(len_train_dataset) :
        res+=lambda_list[j]*E(h(i, calc_1feature(j,i)), train_labels[j])
    return res

#returns the i_k such that h_i_k minimizes the sum    
def choose_minimizing_classifier(k) :
    i_k = 0
    epsilon_k = eps(i_k)
    min_epsilon_k = epsilon_k
    for i in range(1, len_vec_features) :
        epsilon_k = eps(i)
        if epsilon_k < min_epsilon_k :
            min_epsilon_k = epsilon_k
            i_k = i
    return i_k

print("**** getting lambda_list from lambda_list.txt ****")
fichier = open("lambda_list.txt","r")
lambda_list = fichier.read()
fichier.close()
lambda_list = array_from_string.arrayFromStringLambda(lambda_list)
N = int(lambda_list[0])
lambda_list = lambda_list[1]
print("---- done ----")

print("**** boosting weak classifiers with N = {0} ****".format(N))    
old_lambda_list = [0 for j in range(len_train_dataset)]
lambda_list = [1./len_train_dataset for j in range(len_train_dataset)]
alpha_list = []

for k in range(N) :
    print(k)
    i_k = choose_minimizing_classifier(k)
    print("minimized")
    epsilon_k = eps(i_k)
    alpha_list.append( 1/2. * np.log( (1.-epsilon_k) / float(epsilon_k) ) )
    som = 0
    for j in range(len_train_dataset) :
        old_lambda_list[j] = lambda_list[j]
    for j in range(len_train_dataset) :
        lambda_list[j] = old_lambda_list[j] * np.exp( - train_labels[j] * alpha_list[k] * h(i_k, calc_1feature(j, i_k)))
        som += lambda_list[j]
    for j in range(len_train_dataset) :
        lambda_list *= 1./som
print("---- done ----")

print("**** saving N and lambda_list in .txt ****")
fichier = open("lambda_list.txt","w")
fichier.write(str([N,lambda_list]))
fichier.close()
print("---- done ----")