#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:47:21 2020
@author: Benoit Lemieux
----
This script will read output files from the StreamMLX.py script on the 
BeagleBone Black device and will graph data on 4 figures, one for each 
channel.  Use this script to test MLX temperature readings with manual
heating.
----
NOTE:  The files read need to be in an MLXStream_Tests directory one level
lower than where this script is located.  Simply replace the "MLXStream_Tests"
folder with the one generated on the BeagleBone when running a test.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

data0= np.load(os.path.join('MLXStream_Tests','MLXStream_CH0.npy'))
data1= np.load(os.path.join('MLXStream_Tests','MLXStream_CH1.npy'))
data2= np.load(os.path.join('MLXStream_Tests','MLXStream_CH2.npy'))
data3= np.load(os.path.join('MLXStream_Tests','MLXStream_CH3.npy'))
data_optocon = np.load(os.path.join('MLXStream_Tests','MLXStream_REF.npy'))

time_vals= []
tobj= []
tamb= []
tref = []

for i in range(len(data0)):
    time_vals.append(data0[i,2])
    tobj.append(data0[i,0])
    tamb.append(data0[i,1])
    tref.append(data_optocon[i,0])

plt.figure(1)
plt.plot(time_vals, tobj, 'r') 
plt.plot(time_vals, tamb, 'b') 
plt.plot(time_vals, tref, 'g') 
plt.xlabel('time (s)')
plt.ylabel('temperature (c)')
plt.show()      

i = 0
list.clear(time_vals)
list.clear(tobj)
list.clear(tamb)

for i in range(len(data1)):
    time_vals.append(data1[i,2])
    tobj.append(data1[i,0])
    tamb.append(data1[i,1])
   
plt.figure(2)
plt.plot(time_vals, tobj, 'r') 
plt.plot(time_vals, tamb, 'b') 
plt.plot(time_vals, tref, 'g') 
plt.xlabel('time (s)')
plt.ylabel('temperature (c)')
plt.show()         

i = 0
list.clear(time_vals)
list.clear(tobj)
list.clear(tamb)

for i in range(len(data2)):
    time_vals.append(data2[i,2])
    tobj.append(data2[i,0])
    tamb.append(data2[i,1])
   
plt.figure(3)
plt.plot(time_vals, tobj, 'r') 
plt.plot(time_vals, tamb, 'b') 
plt.plot(time_vals, tref, 'g') 
plt.xlabel('time (s)')
plt.ylabel('temperature (c)')
plt.show()      

i = 0
list.clear(time_vals)
list.clear(tobj)
list.clear(tamb)

for i in range(len(data3)):
    time_vals.append(data3[i,2])
    tobj.append(data3[i,0])
    tamb.append(data3[i,1])
   
plt.figure(4)
plt.plot(time_vals, tobj, 'r') 
plt.plot(time_vals, tamb, 'b') 
plt.plot(time_vals, tref, 'g') 
plt.xlabel('time (s)')
plt.ylabel('temperature (c)')
plt.show()      

i = 0
