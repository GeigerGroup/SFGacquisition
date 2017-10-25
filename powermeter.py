# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:09:47 2017

@author: Geiger
"""
#serial communications
import serial

#extracting number
import re


class PowerMeter():

    def __init__(self):
        
        #initialize serial port
        ser = serial.Serial()
        
        #port on computer
        ser.port = 'COM1'
        
        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
        ser.baudrate = 9600
        
        #timeout after 1 second so don't wait forever
        ser.timeout = 0.3
        
        #open serial port
        ser.open()
        
        self.ser = ser
        
    #get power from meter and return a float
    def getPower(self):
        self.ser.write(b'ch query\r')
        string = self.ser.readline()
        return float(re.findall(r"[-+]?\d*\.\d+|\d+",string.decode())[0])
    
    #close serial port
    def close(self):
        self.ser.close()
