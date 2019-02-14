#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 09:31:04 2017

@author: pohno
"""

powerDFGs = [3600,3500,3400,3300,3200,3100,3000,2900,2800,2700,2600]

#create a file to store powers
powerPath = folder + '/powers1433PM.txt'
powerFile = open(powerPath,'w')
powerFile.write('dfg\tpower\tstd\n')

#make sure shutter is open
topas.openShutter

for dfg in powerDFGs:
    
    #set wavelength
    topas.setWavelength(dfg)
    
    #get powers
    (ave, std) = pm.getMultPowers(20)
    powerFile.write(str(dfg) + '\t' + str(ave) + '\t' + str(std) + '\n')
    print('Power at ' + str(dfg) + ' = ' + str(ave) + ' +- ' + str(std))
powerFile.close()
