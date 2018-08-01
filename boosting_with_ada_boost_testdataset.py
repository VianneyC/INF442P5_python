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
    res = test_images_integral[n][y][x]
    res += test_images_integral[n][y+h][x+w]
    res -= test_images_integral[n][y][x+w]
    res -= test_images_integral[n][y+h][x]
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

def eps(i) :
    res = 0
    for j in test_wrong_classified_lists[i] :
        res+=lambda_list_test[j]
    return float(res)

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


num_epochs = 10

print("**** boosting weak classifiers from N = {0} to N = {1} ****".format(N, N + num_epochs))
for k in range(N, N+num_epochs) :
    print(k)
    
    i_k = choose_minimizing_classifier(k)
    epsilon_i_k = eps(i_k)
    print("minimized")
        
    alpha_k =  1/2. * np.log( (1.-epsilon_i_k) / float(epsilon_i_k) )
    alpha_list_test.append([i_k, alpha_k ] )
    
    normalized = float(epsilon_i_k * (np.exp( alpha_k) - np.exp(- alpha_k)) + np.exp(- alpha_k))
    for j in range(len_test_dataset) :
        if(j in test_wrong_classified_lists[i_k]) :
            lambda_list_test[j] *= np.exp( alpha_k) / normalized
        else :
            lambda_list_test[j] *= np.exp(- alpha_k) / normalized
N+=num_epochs
print("---- done ----")

print("**** saving lambda_list_test in .txt ****")
fichier = open("lambda_list_test.txt","w")
fichier.write(str(lambda_list_test))
fichier.close()
print("---- done ----")

print("**** saving alpha_list_test in .txt ****")
fichier = open("alpha_list_test.txt","w")
fichier.write(str(alpha_list_test))
fichier.close()
print("---- done ----")