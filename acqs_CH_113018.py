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
length = 30

#create empty list (LEAVE AS IS!)
acqs = []

#adjust here
wl = [3600, 3500, 3400, 3300, 3200, 3100, 3000]
sp = [655,  655,  645,  645,  645,  640,  640]

#set individual lengths
lengths = [5, 5, 5, 10, 10, 10, 10]

#OR HAVE them all be the same
#lengths = [10]*len(wl)


#wl = [3000, 2900, 2800, 2700]
#sp = [630,  630,  630,  630]

#make sure the wl, sp, and lengths have the same number of elements
assert len(wl) == len(sp)
assert len(wl) == len(lengths)

#boolean to store whether a bg has been taken for this sp position
did_take_bg = False

#iterate through individual spectra
i = 0
while i < len(wl):
    #if you haven't taken a bg and its the first or a new sp position
    if not did_take_bg and (i == 0 or sp[i] != sp[i-1]):
        # Take a background spectrum
        bg = True
        name = str(wl[i]) + '_bg'
        #mark that you've taken a background
        did_take_bg = True
        acqs.append(Acquisition(name, wl[i], sp[i], bg, lengths[i]))
        #go back and test this dfg again
        i = i - 1
    #if you have already taken a bg on this one or it isn't a new position
    else:
        bg = False
        name = str(wl[i])
        did_take_bg = False
        acqs.append(Acquisition(name, wl[i], sp[i], bg, lengths[i]))
        
    i = i+1
    