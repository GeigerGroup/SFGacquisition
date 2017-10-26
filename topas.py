# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 16:01:41 2017

@author: Geiger
"""
import serial

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
        
        ser.open()
        
        self.ser = ser
        
    def getStatus(self):
        self.ser.write(b'GetStatus\r')
        return self.ser.readline()
        
        
    def getWavelength(self):
        self.ser.write(b'GetWavelength\r')
        return self.ser.readline()
    
    def setWavelength(self,wl):
        self.ser.write(b'SetWavelength '+ str(wl).encode() + b'\r')
        return self.ser.readline()
    
    def getInteraction(self):
        self.ser.write(b'GetInteraction\r')
        return self.ser.readline()
    
    def setWavelengthEx(self,wl):
        #numbers should set interaction as DFG1
        self.ser.write(b'SetWavelengthEx ' + str(wl).encode() + b', 1,0,0,6\r' )
        return self.ser.readline()
    
    def closeShutter(self):
        self.ser.write(b'CloseShutter\r')
        return self.ser.readline()
        
    def openShutter(self):
        self.ser.write(b'OpenShutter\r')
        return self.ser.readline()