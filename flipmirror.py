# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import ftd2xx
import ftd2xx.defines as constants
import time

class FlipMirror():

    # Raw byte commands for "MGMSG_MOT_MOVE_JOG".
    _down_position = b"\x6A\x04\x00\x01\x21\x01"
    _up_position = b"\x6A\x04\x00\x02\x21\x01"
    

    def __init__(self):
        #serial number for this motor flipper (modify to take as argument)
        serial = b"37874729"
        
  
        # Recommended d2xx setup instructions from Thorlabs.
        motor = ftd2xx.openEx(serial)
        #print(motor.getDeviceInfo())
        motor.setBaudRate(115200)
        motor.setDataCharacteristics(constants.BITS_8, constants.STOP_BITS_1, constants.PARITY_NONE)
        time.sleep(.05)
        motor.purge()
        time.sleep(.05)
        motor.resetDevice()
        motor.setFlowControl(constants.FLOW_RTS_CTS, 0, 0)
        motor.setRts()
        
        self.motor = motor

    def setPosUp(self):
        # Send raw bytes to USB driver.
        self.motor.write(self._up_position)
    
    def setPosDown(self):
        self.motor.write(self._down_position)
        
    def close(self):
        self.motor.close()
