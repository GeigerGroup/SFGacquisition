# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:31:21 2019

@author: Paul Ohno and Yangdongling Liu
"""

#add .NET library
import clr
clr.AddReference(r"C:\Users\Solstice\Documents\Topas4PublicAPI-master\NET_SDK\Topas4Lib")

import time

from Topas4Lib import TopasDevice

class TOPAS():
    
    def __init__(self):       
        serialNumber = "10777" #enter serial number or your own device here
        self.topas = TopasDevice.FindTopasDevice(serialNumber)
        
        if self.topas is None:
            print ('Device with serial number %s not found' % serialNumber)
            
    def closeShutter(self):
        self.topas.ShutterService.SetOpenCloseShutter(False) 
        time.sleep(0.5)
        
    def openShutter(self):
        self.topas.ShutterService.SetOpenCloseShutter(True) 
        time.sleep(0.5)

    def setWavelength(self,wavelength):
       #get all interactions; DFG1 = interactions[8], DFG2 = interactions[9]
       interactions = self.topas.WavelengthService.GetExpandedInteractions()
       
       #select DFG1
       interaction = interactions[8]
       
       #set it
       print("setting wavelength %.4f nm using interaction %s" % (wavelength, interaction.Type))
       self.topas.SetWavelength(wavelength, interaction.Type)
       
       #wait until its done
       self.waitTillSet()

    def waitTillSet(self):
        #loop to check if wavelength has been set
        while(True):
            #get status
            s = self.topas.WavelengthService.GetOutput()
            if s.IsWavelengthSettingInProgress == False:
                break
            time.sleep(0.05)
        print("Done setting wavelength")
