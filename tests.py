#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 11:26:52 2018

@author: vianney
"""

"""
Viola & Jones applied to face detection in images
implemented in Python
"""

# import des modules
import os
import skimage.data
import numpy as np
import module as md

#variables utiles

len_vec_car = 107988
len_train_dataset = 5233


print(classifieurs[0])
md.train_classifieurs(classifieurs, K, epsilon, len_vec_car, len_train_dataset, train_integral_images, train_images, train_car_images, train_labels)
print(classifieurs[0])
"""
"""
image = md.load_picture("INF442P5_python/data/dev/pos/im0.jpg")

integral_image = md.integral_image(image)
rect_car = "["
vec_car = md.calc_car(integral_image,rect_car)


print(len(vec_car))
"""