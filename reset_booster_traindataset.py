#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:27:16 2018

@author: vianney
"""


lambda_list_train = [1./len_train_dataset for j in range(len_train_dataset)]

print("**** saving lambda_list_train in .txt ****")
fichier = open("lambda_list_train.txt","w")
fichier.write(str(lambda_list_train))
fichier.close()
print("---- done ----")

alpha_list_train = []
print("**** saving alpha_list_train in .txt ****")
fichier = open("alpha_list_train.txt","w")
fichier.write(str(alpha_list_train))
fichier.close()
print("---- done ----")