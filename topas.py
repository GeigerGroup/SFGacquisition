# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:01:41 2017

@author: Geiger
"""
import serial
import time

class TOPAS():

    def __init__(self):
        
        #initialize serial port
        ser = serial.Serial()
        
        #port on computer
        ser.port = 'COM5'
        
        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
        ser.baudrate = 9600
        
        #timeout after 1 second so don't wait forever
        ser.timeout = 1
        
        #open serial port
        ser.open()
        
        #set serial port property
        self.ser = ser
    
    
    #verifies that topas is there    
    def getStatus(self):
        self.ser.write(b'GetStatus\r')
        return self.ser.readline()
        
    
    #gets the current wavelength setting    
    def getWavelength(self):
        self.ser.write(b'GetWavelength\r')
        return self.ser.readline()
 
    
    #sets wavelength with DFG1, diff TOPAS config may need diff interaction code
    def setWavelength(self,wl):
        self.ser.write(b'SetWavelengthEx ' + str(wl).encode() + b', 1,0,0,6\r' )
        
        #wait for 3 seconds to give it time to move
        time.sleep(3)
        return self.ser.readline()
    
    
    #close TOPAS shutter
    def closeShutter(self):
        self.ser.write(b'CloseShutter\r')
        
        #wait for 1 second to give it time to close
        time.sleep(1)
        return self.ser.readline()
    
    
    #open TOPAS shutter
    def openShutter(self):
        self.ser.write(b'OpenShutter\r')
        
        #wait for 1 second to give it time to open
        time.sleep(1)
        return self.ser.readline()