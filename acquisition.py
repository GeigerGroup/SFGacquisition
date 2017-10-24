#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:07:41 2017

@author: pohno
"""

class Acquisition():
    
    def __init__(self,name,dfg,detector,bg):
        self.name = name
        self.dfg = dfg
        self.detector = detector
        self.bg = bg
        
