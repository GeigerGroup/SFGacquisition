# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 15:20:43 2018

@author: Solstice
"""

import os
import datetime


samplename = 'bcaryO3flow_highRH'
measurementname = 'afterozone_20min_30s'
numruns = 2
rootfolder = "C:/Users/Solstice/My Documents/SFG DATA/Ariana/"


# Create Folders
date = datetime.datetime.now()
datestring = str(date.year) + '-' + str(date.month) + '-' + str(date.day)
datefolder = os.path.join(rootfolder, datestring)
samplefolder = os.path.join(datefolder, samplename)

if not os.path.exists(samplefolder):
    os.makedirs(samplefolder)

numfolders = sum(os.path.isdir(os.path.join(samplefolder, i)) for i in os.listdir(samplefolder))
print(numfolders)

measurementfolder = os.path.join(samplefolder, str(numfolders) + '_' + measurementname)

if not os.path.exists(measurementfolder):
    os.makedirs(measurementfolder)

exec(open("C:/Users/Solstice/Documents/Python Scripts/SFGacquisition/acqs_CH_113018.py").read())

for i in range(numruns):
    runfolder = 'run' + str(i+1)
    folder = os.path.join(measurementfolder, runfolder)
    exec(open("C:/Users/Solstice/Documents/Python Scripts/SFGacquisition/run.py").read())

    