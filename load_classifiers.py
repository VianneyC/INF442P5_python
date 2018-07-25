#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:06:09 2018

@author: vianney
"""

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
        temp_array = [int(int_str)]
        #print(classifiers_list[i] == ",")
        i+=1
        int_str = ""
        while(classifiers_list[i] != "]") :
            int_str+=classifiers_list[i]
            i+=1
        temp_array.append(int(int_str))
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
        

#creates classifiers (array containing weights) 
print("**** creating classifiers array from classifiers.txt ****")
len_vec_features = 107988
fichier = open("classifiers.txt","r")
classifiers = fichier.read()
fichier.close()
classifiers = arrayFromStringClassifieurs(classifiers)
print("---- done ----")