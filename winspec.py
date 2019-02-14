#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:01:22 2017

winspec.py, COM wrapper for use with Roper Scientific's Winspec, modified by
Paul Ohno from code originally written by Reinier Heeres (qtlab).

@author: pohno
"""

from comtypes.client import CreateObject, Constants


class WinSpec():
    
    def __init__(self):
        '''
        Initialize communications with winspec program using Microsoft COM.
        Create objects. Associated constants will be available in the _const
        object. Note that it's not possible to request the contents of that;
        one has to look in the Python file generated with gen_py.
        '''
        
        self.exp = CreateObject('WinX32.ExpSetup.2')
        self.app = CreateObject('WinX32.Winx32App.2')
        self.const = Constants(self.exp)
        self.spec_mgr = CreateObject('WinX32.SpectroObjMgr')
        self.spec = self.spec_mgr.Current
        self.spec.Process(self.const.SPTP_INST_LOADCONFIGURATION)
        
    #get center wavelength of specrograph
    def getWavelength(self):
        return self.spec.GetParam(self.const.SPT_CUR_POSITION)[1]
    
    #set center wavleenght of spectrograph
    def setWavelength(self,val):
        self.spec.SetParam(self.const.SPT_NEW_POSITION, float(val))
        self.spec.Move()
        return self.getWavelength()

    #get exposure time for acquisition/focus
    def getExposureTime(self):
        return round(self.exp.SGetParam(self.const.EXP_EXPOSURE)[1],2)
    
    #set exposure time for acquisition/focus
    def setExposureTime(self,val):
        return self.exp.SetParam(self.const.EXP_EXPOSURE, val)
    
    #get temperature of ccd
    def getTemperature(self):
        return self.exp.SGetParam(self.const.EXP_ACTUAL_TEMP)[1]
    
    #start acquisition, will create new file if old one has been saved
    def startAcquisition(self):
        return self.exp.Start2()
    
    #stop acquisition
    def stopAcquisition(self):
        return self.exp.Stop()
    
    # Close all windows
#    def close(self):
#        doc = self.exp.GetDocument()
#        return self.exp.DocFile.Close()
    
    #save most recent acquisition
    def saveAcquisition(self,fullname):
        doc = self.exp.GetDocument()
        doc.SaveAs(fullname)
        #doc.Close()