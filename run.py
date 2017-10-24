#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:21:05 2017

@author: pohno
"""
#from acquisition import Acquisition


#set path- if folder doesn't exist, create it
#fullpath = "C:Users\\Solstice

#define length (in seconds)
length = 60
winspec.setExposureTime(length)

#create empty list
acqs = []

#create each individual acquisition
acqs.append(Acquisition('3600',3600,655,False))
acqs.append(Acquisition('3600_bg',3600,655,True))
acqs.append(Acquisition('3500',3500,655,False))
acqs.append(Acquisition('3400',3400,645,False))
acqs.append(Acquisition('3400_bg',3400,645,True))
acqs.append(Acquisition('3300',3300,645,False))
acqs.append(Acquisition('3200',3200,645,False))
acqs.append(Acquisition('3100',3100,640,False))
acqs.append(Acquisition('3100_bg',3100,640,True))
acqs.append(Acquisition('3000',3000,635,False))
acqs.append(Acquisition('3000_bg',3000,635,True))
acqs.append(Acquisition('2900',2900,630,False))
acqs.append(Acquisition('2900_bg',2900,630,True))
acqs.append(Acquisition('2800',2800,625,False))
acqs.append(Acquisition('2800_bg',2800,625,True))

for acq in acqs:
    
    #set topas wavelength
    topas.setWavelength(acq.dfg)
    
    #set detector
    winspec.setWavelength(acq.detector)
    
    #turn up flip mirror if background, or put down
    if acq.bg:
        flipmirror.setPosUp
    else:
        flipmirror.setPosDown
    
    #should wait ~5 seconds to make sure everything has completed
    
    #then start acquisition
    winspec.startAcquisition
    
    
    if not acq.bg:
        for i in range(length):
            #get power readings
            #wait 1 sec
    else:
        #wait length of time
        #wait = length
    
    #save acquisition
    winspec.saveAcquisition(fullpath +  '\\' + name)

        
    




