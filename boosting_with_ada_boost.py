#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 15:01:37 2018

@author: vianney
"""

import numpy as np

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


def E(h,c) :
    return int(h == c)

def eps(i) :
    res = 0
    for j in range(len_train_dataset) :
        res+=lambda_list[i][j]*int( (h(i, calc_1feature(j,i)) == train_labels[j]) )
    return res    
    
def choose_minimizing_classifier(k) :
    i_k = 0
    epsilon_k = eps(i_k)
    min_epsilon_k = epsilon_k
    for i in range(lev_vec_feature) :
        epsilon_k = eps(i)
        if epsilon_k < min_epsilon_k :
            min_epsilon_k = epsilon_k
            i_k = i
    return i_k
    
N = 20

lambda_list = [[1./len_train_dataset for j in range(len_train_dataset)] for k in range(N)]
alpha_list = []

for k in range(N) :
    i_k = choose_minimizing_classifier(k)
    epsilon_k = eps(i_k)
    alpha_list.append( 1/2. * np.log( (1.-epsilon_k) / epsilon_k ) )
    
    som = 0
    for j in range(len_train_dataset) :
        lambda_list[k+1][j] = lambda_list[k][j] * np.exp( - train_labels[j] * alpha_list[k] * h(k, calc_1feature(j, k)))
        som += lambda_list[k+1][j]
    for j in range(len_train_dataset) :
        lambda_list[k+1][j] *= 1./som

fichier = open("alpha_list.txt","w")
fichier.write(str(alpha_list))
fichier.close()
        
    
    