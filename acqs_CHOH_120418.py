#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:54:35 2017

Defines the individual parameters of a run: length of an acquisiiton in
seconds, acqs is a list of each individual acquisiiton, and folder is the 
folder where the power file and each spectra is stored.

@author: pohno
"""
#folder to store files in
#folder = "C:/Users/Solstice/My Documents/SFG DATA/Michael/2018-11-15/Au_reference/run1"
#define length (in seconds)
length = 2




#create empty list (LEAVE AS IS!)
acqs = []

wl = [3600, 3500, 3400, 3300, 3200, 3100, 3000, 2900, 2800, 2700, 2600, 2500]
sp = [655,  655,  645,  645,  645,  640,  640, 635, 630, 625, 625, 625]



#wl = [3000, 2900, 2800, 2700
#sp = [630,  630,  630,  630]

assert len(wl) == len(sp)

did_take_bg = False
i = 0
while i < len(wl):
    if not did_take_bg and (i == 0 or sp[i] != sp[i-1]):
        # Take a background spectrum
        bg = True
        name = str(wl[i]) + '_bg'
        did_take_bg = True
        acqs.append(Acquisition(name, wl[i], sp[i], bg))
        i = i - 1
    else:
        bg = False
        name = str(wl[i])
        did_take_bg = False
        acqs.append(Acquisition(name, wl[i], sp[i], bg))
        
    i = i+1
    