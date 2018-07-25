#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:05:13 2018

@author: vianney
"""

import numpy as np

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

#returns the pixels sum in the given rectangle on the n-th image
def sum_rect(x, y, w, h, n) :
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

#trains K times the classifier number i
def train_1classifier(i) :
    for k in range(K) :
        n = np.random.randint(len_train_dataset)
        if not(i in train_images_features[n][0]) :
            train_images_integral[n] = integral_image(train_images[n])
            feature_i_n = calc_1feature(n,i)
            train_images_features[n][0].append(i)
            train_images_features[n][1].append(feature_i_n)
        else :
            feature_i_n = train_images_features[n][1][train_images_features[n][0].index(i)]
        label_n = train_labels[n]
        classifiers[i][0] -= epsilon * ( h(i,feature_i_n) - label_n) * feature_i_n
        classifiers[i][1] -= epsilon * ( h(i,feature_i_n) - label_n)


#trains every classifier K times with epsilon
def train_classifiers() :    
    for i in range(len_vec_features) :
        print("classifier {0} out of {1} is being trained".format(str(i),str(len_vec_features)))
        train_1classifier(i)


#trains every classifier K times with epsilon over the train_dataset
print("**** training classifiers with K = {0} and epsilon = {1}".format(str(K), str(epsilon)))
train_classifiers()
print("---- done ----")

#saves every new weight of our classifiers in classifiers.txt
print("*** saving every new weights in classifiers.txt ****")
fichier = open("classifiers.txt","w")
fichier.write(str(classifiers))
fichier.close()
print("---- done ----")

#saves train_images_integral and train_images_features to .txt
print("**** saving train_images_integral .txt ****")
fichier = open("train_images_integral.txt","w")
fichier.write(str(train_images_integral))
fichier.close()
print("---- done ----")
print("**** saving train_images_features .txt ****")
fichier = open("train_images_features.txt","w")
fichier.write(str(train_images_features))
fichier.close()
print("---- done ----")






"""
Other functions that can be used if needed
"""

def calc_feature(integral_pict) :
    vec_car = []
    # retourne la somme des pixels dans le rectangle
    # de coin haut gauche (x,y)
    # de largeur w et de hauteur h
    def somme_rect(x, y, w, h) :
        res = integral_pict[y][x]
        res += integral_pict[y+h][x+w]
        res -= integral_pict[y][x+w]
        res -= integral_pict[y+h][x]
        return res
    
    for x_origin in range(0, 112, 4) :
        for y_origin in range(0, 92, 4) :
            for width in range(8, 112 + 1, 4) :
                for height in range(8, 92 + 1, 4) :
                    
                    #feature 1
                    if(x_origin + 2 * width < 112 and y_origin + height < 92) :
                        res = somme_rect(x_origin+width,y_origin,width,height)
                        res -= somme_rect(x_origin,y_origin,width,height)
                        vec_car.append(res) 
                    
                    #feature 2
                    if(x_origin + width < 112 and y_origin + 2 * height < 92) :
                        res = somme_rect(x_origin,y_origin,width,height)
                        res -= somme_rect(x_origin,y_origin+height,width,height)
                        vec_car.append(res)
                    
                    #feature 3
                    if(x_origin + 3 * width < 112 and y_origin + height < 92) :
                        res = somme_rect(x_origin+width,y_origin,width,height)
                        res -= somme_rect(x_origin,y_origin,width,height)
                        res -= somme_rect(x_origin+2*width,y_origin,width,height)
                        vec_car.append(res)
                        
                    #feature 4
                    if(x_origin + 2 * width < 112 and y_origin + 2 * height < 92) :
                        res = somme_rect(x_origin+width,y_origin,width,height)
                        res += somme_rect(x_origin,y_origin+height,width,height)
                        res -= somme_rect(x_origin,y_origin,width,height)
                        res -= somme_rect(x_origin+width,y_origin+height,width,height)
                        vec_car.append(res)
    return vec_car