#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:54:35 2017

Defines the individual parameters of a run: length of an acquisiiton in
seconds, acqs is a list of each individual acquisiiton, and folder is the 
folder where the power file and each spectra is stored.

@author: pohno
"""
#folder to store files in
folder = 'C:/Users/Solstice/My Documents/SFG DATA/Merve/02222018/low salt_ flow/run5 flow'

#define length (in seconds)
length =120



#create empty list (LEAVE AS IS!)
acqs = []

#create each individual acquisition
acqs.append(Acquisition('3600',3600,655,False))
acqs.append(Acquisition('3600_bg',3600,655,True))
acqs.append(Acquisition('3500',3500,655,False))
acqs.append(Acquisition('3400',3400,645,False))
acqs.append(Acquisition('3400_bg',3400,645,True))
acqs.append(Acquisition('3300',3300,645,False))
acqs.append(Acquisition('3200',3200,645,False))
acqs.append(Acquisition('3100',3100,635,False))
acqs.append(Acquisition('3100_bg',3100,635,True))
acqs.append(Acquisition('3000',3000,635,False))
acqs.append(Acquisition('2900',2900,625,False))
acqs.append(Acquisition('2900_bg',2900,625,True))
acqs.append(Acquisition('2800',2800,625,False))
acqs.append(Acquisition('2700',2700,615,False))
acqs.append(Acquisition('2700_bg',2700,615,True))
acqs.append(Acquisition('2600',2600,615,False))
