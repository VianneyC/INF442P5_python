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
import load_train_data
import train_classifiers


image = load_train_data.load_picture("INF442P5_python/data/train/pos/im0.jpg")

integral_image = train_classifiers.integral_image(image)
print(str(integral_image))