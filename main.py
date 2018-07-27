#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:19:10 2018

@author: vianney
"""

#will load train_data_set from data/train
execfile("load_train_data.py")

#will load classifiers from classifiers.txt
execfile("load_classifiers.py")

K = 5
#do not change espilon
epsilon = 0.05

need_to_update_train_images_integral_on_drive = False
#will train classifiers with parameters (K,epsilon)
execfile("train_classifiers.py")
if(need_to_update_train_images_integral_on_drive) :
    print("train_images_integral.txt needs to be updated on drive.")