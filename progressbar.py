#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:06:29 2018

@author: vianney
"""

import sys

class ProgressBar:
    def __init__(self, iterations):
        self.iterations = float(iterations)
        self.fill_char = '-'
        self.width = 50
        self.animate(0)
        self.pct_place = int(self.width / 2.) - 2
        
    def animate(self, iter):
        percent_done = int(iter / self.iterations * 100.0)
        str_pct = "{0} %".format(percent_done)
        num_char = int((self.width - 2) * percent_done / 100.)
        self.prog_bar = '['+ self.fill_char * num_char + ' ' * (self.width - 2 - num_char) + '] ' + str_pct
        print '\r', self,
        sys.stdout.flush()

    def __str__(self):
        return str(self.prog_bar)
    
    def ciao(self) :
        self.animate(self.iterations)
        print '\r'