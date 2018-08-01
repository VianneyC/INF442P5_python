#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:27:16 2018

@author: vianney
"""


lambda_list = [1./len_test_dataset for j in range(len_test_dataset)]

print("**** saving lambda_list in .txt ****")
fichier = open("lambda_list.txt","w")
fichier.write(str(lambda_list))
fichier.close()
print("---- done ----")

alpha_list = []
print("**** saving alpha_list in .txt ****")
fichier = open("alpha_list.txt","w")
fichier.write(str(alpha_list))
fichier.close()
print("---- done ----")