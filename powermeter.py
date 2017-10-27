# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:09:47 2017

Creates object to interact with Molectron EPM 1000 power meter.

@author: pohno
"""
#serial communications
import serial

#extracting number
import re

#timing
import time

#array
import numpy as np


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
    def getSinglePower(self):
        self.ser.write(b'ch query\r')
        
        #wait for 300 ms to give it time to recover
        time.sleep(0.3)
        
        #get response and extract float
        string = self.ser.readline()
        return float(re.findall(r"[-+]?\d*\.\d+|\d+",string.decode())[0])
    
    def getMultPowers(self,n):
        #array to hold powers
        pwrs = np.zeros(n)
        
        for i in range(n):
            pwrs[i] = self.getSinglePower()
        
        ave = pwrs.mean()
        std = pwrs.std()
        
        return (ave,std)
    
    
    #close serial port
    def close(self):
        self.ser.close()
