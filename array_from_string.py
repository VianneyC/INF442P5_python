#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:46:53 2018

@author: vianney
"""

#returns an array created from the image_integral_list string
def arrayFromStringTrainImageIntegral(image_integral_list) :
    array = []
    i = 1
    j = 0
    while i < len(image_integral_list) - 1 :
        #print(image_integral_list[i] == "[")
        i += 1
        temp_array = []
        while(image_integral_list[i] != "]") :
            #print(image_integral_list[i] == "[")
            i += 1
            temp_temp_array = []
            while(image_integral_list[i] != "]") :
                int_str = ""
                while image_integral_list[i] != "]" and image_integral_list[i] != "," :
                    int_str += image_integral_list[i]
                    i += 1
                if int_str :
                    temp_temp_array.append(float(int_str))
                if image_integral_list[i] == "," :
                    i += 1
                    #print(image_integral_list[i] == " ")
                    i += 1    
            temp_array.append(temp_temp_array)
            #print(image_integral_list[i] == "]")
            i += 1
            if image_integral_list[i] == "," :
                i += 1
                #print(image_integral_list[i] == " ")
                i += 1
        #print(array)
        array.append(temp_array)
        #print(image_integral_list[i] == "]")
        i += 1
        if image_integral_list[i] == "," :
            #print(image_integral_list[i] == ",")
            i += 1
            #print(image_integral_list[i] == " ")
            i += 1
    return array



#creates the features_patterns_list from features_patterns.txt
def arrayFromStringFeaturesList(features_list) :
    array = []
    i = 1
    j = 0
    while i < len(features_list)-1 :
        temp_array = []
        #print(features_list[i] == "[")
        i+=1
        temp_array.append(float(features_list[i]))
        i+=1
        #print(features_list[i] == ",")
        i+=1
        #print(features_list[i] == " ")
        i+=1
        #print(features_list[i] == "[")
        i+=1
        int_str = ""
        while(features_list[i] != ",") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array = [float(int_str)]
        #print(features_list[i] == ",")
        i+=1
        #print(features_list[i] == " ")
        i+=1
        int_str = ""
        while(features_list[i] != ",") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array.append(float(int_str))
        #print(features_list[i] == ",")
        i+=1
        #print(features_list[i] == " ")
        i+=1
        int_str = ""
        while(features_list[i] != ",") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array.append(float(int_str))
        #print(features_list[i] == ",")
        i+=1
        #print(features_list[i] == " ")
        i+=1
        int_str = ""
        while(features_list[i] != "]") :
            int_str+=features_list[i]
            i+=1
        temp_temp_array.append(float(int_str))
        temp_array.append(temp_temp_array)
        #print(features_list[i] == "]")
        i+=1
        #print(features_list[i] == "]")
        i+=1
        #print(features_list[i] == ",")
        i+=1
        #print(features_list[i] == " ")
        i+=1
        #print(temp_array)
        array.append(temp_array)
        j += 1
        #print(j)
    return array

#creates classifiers array from classifieurs.txt
def arrayFromStringClassifieurs(classifiers_list) :
    array = []
    i = 1
    j = 0
    while i < len(classifiers_list)-1 :
        temp_array = []
        #print(classifiers_list[i] == "[")
        i+=1
        int_str = ""
        while(classifiers_list[i] != ",") :
            int_str+=classifiers_list[i]
            i+=1
        temp_array = [float(int_str)]
        #print(classifiers_list[i] == ",")
        i+=1
        int_str = ""
        while(classifiers_list[i] != "]") :
            int_str+=classifiers_list[i]
            i+=1
        temp_array.append(float(int_str))
        #print(classifiers_list[i] == "]")
        i+=1
        #print(classifiers_list[i] == ",")
        i+=1
        #print(classifiers_list[i] == " ")
        i+=1
        #print(temp_array)
        array.append(temp_array)
        j += 1
        #print(j)
    return array


"""
Other functions that can be used if needed
"""

#returns an array created from the image_features_list string
def arrayFromStringTrainImageFeatures(image_features_list) :
    array = []
    i = 1
    j = 0
    while i < len(image_features_list)-1 :
        #print(image_features_list[i] == "[")
        i+=1
        temp_array_1 = []
        #print(image_features_list[i] == "[")
        i+=1
        while image_features_list[i] != "]" :
            int_str = ""
            while image_features_list[i] != "," and image_features_list[i] != "]" :
                int_str += image_features_list[i]
                i += 1
            if int_str :
                temp_array_1.append(float(int_str))
            #print(image_features_list[i] == ",")
            if image_features_list[i] == "," :
                i+=1
            
        #print(image_features_list[i] == "]")
        i += 1
        #print(image_features_list[i] == ",")
        i += 1        
        #print(image_features_list[i] == " ")
        i += 1
        temp_array_2 = []
        #print(image_features_list[i] == "[")
        i+=1
        while image_features_list[i] != "]" :
            int_str = ""
            while image_features_list[i] != "," and image_features_list[i] != "]" :
                int_str += image_features_list[i]
                i += 1
            temp_array_2.append(float(int_str))
            #print(image_features_list[i] == ",")
            if image_features_list[i] == "," :
                i+=1
        #print(image_features_list[i] == "]")
        i += 1
        #print(image_features_list[i] == "]")
        i += 1
        #print(image_features_list[i] == ",")
        i += 1
        if i < len(image_features_list) :
            #print(image_features_list[i] == " ")
            i += 1
        array.append([temp_array_1, temp_array_2])
        #print(j)
        j += 1
    return array