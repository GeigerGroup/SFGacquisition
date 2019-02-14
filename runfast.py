#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:21:05 2017

Executes in variable space after loadobjects.py has create the necessary
objects to communicate with the power meter, detector, TOPAS, and flip y
mirror, and acqs.py has created the folder, length, and acqs variables that 
define the individual run.

@author: pohno
"""

#functions to perform a set of acquisitions stored in acqs
def startRun():
    
    #create a file to store powers
    powerPath = folder + '/powers.txt'
    powerFile = open(powerPath,'w')
    powerFile.write('dfg\tpower\tstd\n')
    
    #set the length of each acquisitionf
    winspec.setExposureTime(length)
    
    #iterate through each acq in acqs
    for acq in acqs:
        
        #set topas wavelength
        topas.setWavelength(acq.dfg)
        
        #set detector wavelength
        winspec.setWavelength(acq.detector)
        
        #shutter open or closed depending on background
        if acq.bg:
            topas.closeShutter()
        else:
            topas.openShutter()
        
        
        #start acquisition recording data
        winspec.startAcquisition()
        print("Starting acq '" + acq.name + 
              "' with TOPAS @ " + str(acq.dfg) +
              " nm and detector @ " + str(acq.detector) + " nm.")
        
        #wait until acquisition is done (with some buffer)
        time.sleep(length+0.5)
        
        #save acquisition
        winspec.saveAcquisition(folder + '/' + acq.name)
        
        #if its not a bg, record power and write to file
        if not acq.bg:
            flip.setPosUp()
            time.sleep(0.2)
            (ave, std) = pm.getMultPowers(3)
            powerFile.write(str(acq.dfg) + '\t' + str(ave) + '\t' + str(std) + '\n')
            flip.setPosDown()

        
#    powerFile.close()
    print('Acquisitions complete.')
    
#check to see if folder exists and send warning if it does
if os.path.isdir(folder):
    response = input("Folder '" + folder + 
        "' already exists. You may overwrite something. Proceed? (y/n): ")
    if response == 'y':
        print('Acquisition starting.')
        startRun()
    else:
        print('Acquisition not started.')
else:
    os.mkdir(folder)
    print("Folder '" + folder + "'created. Starting Acquisitions.")
    startRun()
    #start acquisition
        
    




