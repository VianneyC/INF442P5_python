#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 14:38:45 2018

@author: vianney
"""
import numpy as np
import matplotlib.pyplot as plt

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

#initializes the confusion matrix
true_positive = 0
false_positive = 0
false_negative = 0
true_negative = 0


print("**** testing weak classifiers on test_dataset ****")
for n in range(len_test_dataset) :
    print("testing image {0} out of {1}".format(n, len_test_dataset))
    tot_n = 0
    for i in range(len_vec_features) :
        feature_i_n = calc_1feature(n,i)
        tot_n += h(i, feature_i_n)

    tot_n = float(tot_n) / len_vec_features
    Y.append(tot_n)    
    if tot_n > 0 and test_labels[n] == 1 :
        true_positive += 1
    if tot_n < 0 and test_labels[n] == 1 :
        false_negative += 1
    if tot_n > 0 and test_labels[n] == -1 :
        false_positive+=1
    if tot_n < 0 and test_labels[n] == -1 :
        true_negative += 1
    if int(tot_n > 0) *2 - 1 == test_labels[n] :
        accuracy += 1


if(float(true_positive + false_negative) != 0) :
    detection_rate = true_positive / float(true_positive + false_negative)
else :
    detection_rate = "NaN"
if(float(true_positive + false_positive) != 0) :
    precision = true_positive / float(true_positive + false_positive)
else :
    precision = "NaN"
if(float(false_positive + true_negative) != 0) :
    false_alarm_rate = false_positive / float(false_positive + true_negative)
else :
    false_alarm_rate = "NaN"
if(float(precision + detection_rate) != 0) :
    f_score = 2 * precision * detection_rate / float(precision + detection_rate)
else :
    f_score = "NaN"
    
print("---- done ----")

print("detection_rate = " + str(detection_rate))
print("precision = " + str(precision))
print("false_alarm_rate = " + str(false_alarm_rate))
print("f_score = " + str(f_score))

#accuracy = float(accuracy) / len_test_dataset
#print("accuracy = " + str(accuracy))