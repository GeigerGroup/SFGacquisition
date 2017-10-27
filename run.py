#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:21:05 2017

@author: pohno
"""

winspec.setExposureTime(length)

for acq in acqs:
    
    #set topas wavelength
    topas.setWavelength(acq.dfg)
    
    #set detector
    winspec.setWavelength(acq.detector)
    
    #turn up flip mirror if background, or put down
    if acq.bg:
        topas.closeShutter
    else:
        topas.openShutter
    
    
    #then start acquisition
    winspec.startAcquisition
    
    #wait until acquisition is done
    time.sleep(length+5)

    
    
    if not acq.bg:
        powermeter.getMultPowers(20)

    else:
        #wait length of time
        #wait = length
    
    #save acquisition
    winspec.saveAcquisition(fullpath +  '\\' + name)

        
    




