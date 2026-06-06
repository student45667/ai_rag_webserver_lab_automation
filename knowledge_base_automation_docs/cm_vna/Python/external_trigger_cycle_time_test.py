# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 11:16:14 2020

@author: CMT
"""

# -*- coding: utf-8 -*-
"""
Created on 10/24/2022

OVERVIEW:
    This example shows how to measure VNA cycle time and data transfer time for capturing 
    one trace in the VNA software with EXTERNAL trigger source. The result is 
    averaged time for selected number of sweeps which is set by "num_sweep" variable.

Before running the code:
    1. Make sure VNA software is running
    2. Go to system -> Misc setup -> network remote settings -> turn on socket server
    3. make sure socket server is 5025

Additional information:
    1. The SCPI programming manual is intalled with the VNA software. By default:
        C:\VNA\RVNA or TRVNA or S2VNA or S4VNA\Doc
    
"""

import pyvisa    #PyVisa is required along with NIVisa
from time import sleep
import os
import time
import csv
import matplotlib.pyplot as plt

rm = pyvisa.ResourceManager('@py') # use pyvisa-py as backend, must install pyvisa-py 
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # use ni visa 32 bit as backend, must install NI VISA
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa64.dll')  # use ni visa 64 bit as backend, must install NI VISA

#Connect to a Socket on the local machine at 5025
try:
    # 127.0.0.1 is the local loopback IP address. Don't change this IP address if 
    # the VNA is connected to the same PC which runs this code
    CMT = rm.open_resource('TCPIP0::127.0.0.1::5025::SOCKET')
    
except:
    print("Failure to connect to VNA!")
    print("Check network settings")
#The VNA ends each line with this. Reads will time out without this
CMT.read_termination='\n'
#Set a really long timeout period for slow sweeps
CMT.timeout = 10000

###########################################
###########################################
###### SCPI commands start here ###########
###########################################
###########################################

num_sweep = 1 # number of sweeps


# set trigger source to External
CMT.write("TRIG:SOUR EXT")

CMT.write('FORM:DATA ASC') # ASCII format
# CMT.write('FORM:DATA REAL32') # 32 bit float
# CMT.write('FORM:DATA REAL') # 64 bit float

# NORM means big endian format for S2VNA S4VNA
# NORM means little endian format for RVNA and TRVNA
CMT.write('FORM:BORD SWAP')
CMT.write('DISP:ENAB 0') # turn display update off to have faster measurement
CMT.query("*OPC?")

# initialize empties arrays for VNA measurement data, cycle time data and data transfer time data
all_data = []
cycle_time_array = []
data_transfer_time_array = []

################################################
# measurement loop
################################################
for i in range(0,num_sweep):
    t_before_trigger = time.perf_counter()
    
    # send single trigger
    CMT.write("TRIG:SING")
    # CMT.query("*OPC?")
    
    # CMT.write("TRIG:WAIT ENDM")
    # CMT.query("*OPC?")
    
    while 1:
        if CMT.query("TRIG:STAT?") == 'WAIT':
            break
        
    t_before_data_transfer = time.perf_counter()
    
    # capture data from trace 1, response is a list of float numbers
    s11_data = CMT.query('CALC1:DATA:FDAT?') # ASCII format
    # s11_data = CMT.query_binary_values('CALC1:DATA:FDAT?') # 32 bit float
    # s11_data = CMT.query_binary_values('CALC1:DATA:FDAT?',datatype='d') # 64 bit float
    
    all_data.append(s11_data)
    
    t_after_sweep = time.perf_counter()
    
    cycle_time = t_after_sweep - t_before_trigger
    cycle_time_array.append(cycle_time) # seconds
    
    data_transfer_time = t_after_sweep - t_before_data_transfer
    data_transfer_time_array.append(data_transfer_time)
    
# show average cycle time
average_cycle_time = sum(cycle_time_array) / len(cycle_time_array)
print("average cycle time is: {} ms".format(round(average_cycle_time * 1000, 2)))

# show average data transfer time
average_data_transfer_time = sum(data_transfer_time_array) / len(data_transfer_time_array)
print("average data transfer time is: {} ms".format(round(average_data_transfer_time * 1000, 2)))

# return to internal trigger
CMT.write("TRIG:SOUR INT")
CMT.write('DISP:ENAB 1') # turn display update back on










