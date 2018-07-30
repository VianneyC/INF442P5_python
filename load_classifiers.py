#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:06:09 2018

@author: vianney
"""

import array_from_string
        

#creates classifiers (array containing weights) 
print("**** creating classifiers array from classifiers.txt ****")
fichier = open("classifiers.txt","r")
classifiers = fichier.read()
fichier.close()
classifiers = array_from_string.arrayFromStringClassifieurs(classifiers)
len_vec_features = len(classifiers)
print("---- done ----")