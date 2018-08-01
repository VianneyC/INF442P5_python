#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:30:45 2018

@author: vianney
"""

import array_from_string
import progressbar
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


#where i is the number of the classifier and f
#the f-th feature of image x
def h(i, f) :
    if(classifiers[i][0] * f + classifiers[i][1] >= 0) :
        return 1
    return -1


print("**** getting alpha_list from alpha_list.txt ****")
fichier = open("alpha_list.txt","r")
alpha_list = fichier.read()
fichier.close()
alpha_list = array_from_string.arrayFromStringAlpha(alpha_list)
N = len(alpha_list)
print("---- done ----")

#initializes the confusion matrix
true_positive = 0
false_positive = 0
false_negative = 0
true_negative = 0

#accuracy = 0

theta = .1
sum_alpha = np.sum([elt[1] for elt in alpha_list])
threshold = theta * sum_alpha
two_len_theta = 100
precision_theta = 10
threshold_array = np.array([the / float(two_len_theta) * sum_alpha for the in range(-two_len_theta,two_len_theta,precision_theta)])
false_negative_array = np.array([0 for k in range(len(threshold_array))])
false_positive_array = np.array([0 for k in range(len(threshold_array))])

print("**** testing boosted classifiers on test_dataset ****")
p = progressbar.ProgressBar(len_test_dataset)
old_n = 0
for n in range(len_test_dataset) :
    #print("testing image {0} out of {1}".format(n, len_test_dataset))
    tot_n = 0
    for tab in alpha_list :
        i = int( tab[0] )
        feature_i_n = calc_1feature(n,i)
        tot_n += tab[1] * h(i, feature_i_n)

    for i in range(len(threshold_array)) :
        if 2*int(tot_n >= threshold_array[i])-1 == -1 and test_labels[n] == 1 :
            false_negative_array[i]+=1
        if 2*int(tot_n >= threshold_array[i])-1 == 1 and test_labels[n] == -1 :
            false_positive_array[i]+=1
    
    predicted_label_n = 2*int(tot_n >= threshold)-1
    
    if predicted_label_n == 1 and test_labels[n] == 1 :
        true_positive += 1
    if predicted_label_n == -1 and test_labels[n] == 1 :
        false_negative += 1
    if predicted_label_n == 1 and test_labels[n] == -1 :
        false_positive+=1
    if predicted_label_n == -1 and test_labels[n] == -1 :
        true_negative += 1
    
    #if int(tot_n > 0) *2 - 1 == test_labels[n] :
    #    accuracy += 1
    if(n - old_n > len_test_dataset / 100.) :
        p.animate(n)
        old_n = n
p.ciao()
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
if(float(2 * true_positive + false_negative + false_positive) != 0) :
    f_score = 2 / float(2 * true_positive + false_negative + false_positive)
else :
    f_score = "NaN"
    
print("---- done ----")

print("detection_rate = " + str(detection_rate))
print("precision = " + str(precision))
print("false_alarm_rate = " + str(false_alarm_rate))
print("f_score = " + str(f_score))

print("mean on negative = " + str(np.mean(Y[:415])))
print("mean on positive = " + str(np.mean(Y[415:])))

plt.plot(threshold_array, false_negative_array / false_positive_array)
plt.show()

#accuracy = float(accuracy) / len_test_dataset
#print("accuracy = " + str(accuracy))