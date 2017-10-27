#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:13:48 2017

@author: pohno
"""
#load winspec definition
from winspec import WinSpec

#load topas definition
from topas import TOPAS

#load flipmirror definition
from flipmirror import FlipMirror

#load power meter object
from powermeter import PowerMeter

#load acquisition data type 
from acquisition import Acquisition

#import time
import time

#create single winspec object to interact with detector
winspec = WinSpec()

#create single topas object to interact with TOPAS
topas = TOPAS()

#create single flipmirror object to interact with the flip mirror
flipmirror = FlipMirror()

#create single powermeter object to interact with the power meter
powermeter = PowerMeter()

