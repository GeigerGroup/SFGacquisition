# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 17:12:48 2017

@author: Solstice
"""
folder = 'C:\\Users\\Solstice\\Documents\\SFG Data\\Paul\\test'


#define length (in seconds)
length = 1

#create empty list
acqs = []

#create each individual acquisition
acqs.append(Acquisition('2950',2950,630,False))
acqs.append(Acquisition('2950_bg',2950,630,True))
acqs.append(Acquisition('2900',2900,625,False))
acqs.append(Acquisition('2900_bg',2900,625,True))
