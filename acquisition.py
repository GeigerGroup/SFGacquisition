#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:07:41 2017

Creates acquisition object to hold data for one spectrum acquired by winspec
with specific TOPAS/detector settings as well as if it is a background or not.

@author: pohno
"""

class Acquisition():
    
    def __init__(self,name,dfg,detector,bg,length):
        self.name = name
        self.dfg = dfg
        self.detector = detector
        self.bg = bg
        self.length = length
        
