# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import usb drivers
import ftd2xx
import ftd2xx.defines as constants

#import time so it waits
import time

class FlipMirror():

    # Raw byte commands for "MGMSG_MOT_MOVE_JOG".
    _up_position = b"\x6A\x04\x00\x01\x21\x01"
    _down_position = b"\x6A\x04\x00\x02\x21\x01"
    

    def __init__(self):
        #serial number for this motor flipper
        #if have more than one modify to take as argument)
        serial = b"37874729"
        
        #recommended d2xx setup instructions from Thorlabs
        motor = ftd2xx.openEx(serial)
        motor.setBaudRate(115200)
        motor.setDataCharacteristics(constants.BITS_8, constants.STOP_BITS_1, constants.PARITY_NONE)
        time.sleep(.05)
        motor.purge()
        time.sleep(.05)
        motor.resetDevice()
        motor.setFlowControl(constants.FLOW_RTS_CTS, 0, 0)
        motor.setRts()
        
        #set its motor as the motor
        self.motor = motor


    def setPosUp(self):
        #send raw bites to driver
        self.motor.write(self._up_position)
        
        #wait 1.5 seconds to make sure it is up
        time.sleep(1.5)
        
    
    def setPosDown(self):
        #send raw bites to driver
        self.motor.write(self._down_position)
        
        #wait 1.5 seconds to make sure it is down
        time.sleep(1.5)
        
        
    def close(self):
        self.motor.close()
