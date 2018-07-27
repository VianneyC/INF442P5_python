#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:26:41 2018

@author: vianney
"""

train_images_integral = [[] for k in range(len_train_dataset)]
fichier = open("train_images_integral.txt","w")
fichier.write(str(train_images_integral))
fichier.close()

classifiers = [[1,0] for k in range(len_vec_features)]
fichier = open("classifiers.txt","w")
fichier.write(str(classifiers))
fichier.close()

features_patterns = []
for x_origin in range(0, 112, 4) :
        for y_origin in range(0, 92, 4) :
            for width in range(8, 112 + 1, 4) :
                for height in range(8, 92 + 1, 4) :
                    
                    #feature 1
                    if(x_origin + 2 * width < 112 and y_origin + height < 92) :
                        features_patterns.append([1,[x_origin,y_origin,width,height]])
                    #feature 2
                    if(x_origin + width < 112 and y_origin + 2 * height < 92) :
                        features_patterns.append([2,[x_origin,y_origin,width,height]])
                    #feature 3
                    if(x_origin + 3 * width < 112 and y_origin + height < 92) :
                        features_patterns.append([3,[x_origin,y_origin,width,height]])
                    #feature 4
                    if(x_origin + 2 * width < 112 and y_origin + 2 * height < 92) :
                        features_patterns.append([4,[x_origin,y_origin,width,height]])
fichier = open("features_patterns.txt","w")
fichier.write(str(features_patterns))
fichier.close()