#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 16:27:16 2018

@author: vianney
"""


lambda_list_test = [1./len_test_dataset for j in range(len_test_dataset)]

print("**** saving lambda_list_test in .txt ****")
fichier = open("lambda_list_test.txt","w")
fichier.write(str(lambda_list_test))
fichier.close()
print("---- done ----")

alpha_list_test = []
print("**** saving alpha_list_test in .txt ****")
fichier = open("alpha_list_test.txt","w")
fichier.write(str(alpha_list_test))
fichier.close()
print("---- done ----")