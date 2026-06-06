# -*- coding: utf-8 -*-
"""
Created on 06/08/2022

OVERVIEW:
    This example shows how to measure VNA sweep time, data transfer time and cycle
    time one trace (active trace) in the VNA software. The number of test sweeps
    is selected by setting "num_sweep" variable(defaulted to 10).

Before running the code:
    1. Make sure VNA software is running
    2. S2,S4VNA:
       Go to system -> Misc setup -> network remote settings -> turn on 
       socket server
       R,TRVNA:
       Go to system -> network setup -> interface state (on)
    3. make sure socket server is 5025

Additional information:
    1. The SCPI programming manual is intalled with the VNA software. By default:
        C:\VNA\RVNA or TRVNA or S2VNA or S4VNA\Doc
"""

import pyvisa    #PyVisa is required along with NIVisa
from time import sleep
from statistics import median
import time

rm = pyvisa.ResourceManager('@py') # use pyvisa-py as backend, must install pyvisa-py 
# rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # use ni visa 32 bit as backend, must install NI VISA
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa64.dll')  # use ni visa 64 bit as backend, must install NI VISA

#Connect to a Socket on the local machine at 5025
try:
    # 127.0.0.1 is the local loopback IP address. Don't change this IP address if 
    # the VNA is connected to the same PC which runs this code
    CMT = rm.open_resource('TCPIP0::127.0.0.1::5025::SOCKET')
    # CMT = rm.open_resource('TCPIP0::127.0.0.1::hislip0::INSTR')
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

# input parameter
num_sweep = 100 # number of sweeps to measure

# set trigger source
CMT.write("TRIG:SOUR BUS") # BUS trigger means trigger by program
# CMT.write("TRIG:SOUR EXT") # EXTernal trigger

CMT.write('FORM:DATA ASC') # ASCII format
# CMT.write('FORM:DATA REAL32') # 32 bit float
# CMT.write('FORM:DATA REAL') # 64 bit float

# select binary data endianess, has no effect when uisng ASCII data format
# NORM means big endian
# SWAP means little endian
CMT.write('FORM:BORD SWAP')
CMT.write('DISP:ENAB OFF') # turn display update off to have faster measurement
# CMT.write('SYST:HIDE') # hide software UI to have faster measurement
                         # this achieves pretty much the same as display update off
                         # send "SYST:SHOW" to show the UI
CMT.query("*OPC?")

# initialize empties arrays for VNA measurement data, cycle time data and data transfer time data
all_data = []
all_sweep_time = []
all_data_transfer_time = []
all_cycle_time = []

################################################
# measurement loop
################################################
for i in range(0, num_sweep):
    t_before_trigger = time.perf_counter()
    
    # send single trigger and wait until sweep finishes
    CMT.write("TRIG:SING")
    CMT.query("*OPC?")

    # for external trigger
    # NOTICE: this method will measure a shorter sweep time than actual sweep
    #         time because there's a delay between when a trigger is sent and 
    #         when the trigger is detected by the VNA
    # CMT.query("TRIG:WAIT MEAS;*OPC?") # when trigger state goes to MEASure, it 
    #                                   # means an external trigger is detected
    # t_before_trigger = time.perf_counter()
    # CMT.query("TRIG:WAIT WAIT;*OPC?") # when trigger state goes to WAIT, it means
    #                                   # the sweep has finished
    
    t_before_data_transfer = time.perf_counter()
    
    # capture data from trace 1, response is a list of float numbers
    trace_data = CMT.query_ascii_values('CALC1:DATA:FDAT?') # ASCII format
    # trace_data = CMT.query_binary_values('CALC1:DATA:FDAT?') # 32 bit float
    # trace_data = CMT.query_binary_values('CALC1:DATA:FDAT?',datatype='d') # 64 bit float
    
    t_end_of_cycle = time.perf_counter()

    all_data.append(trace_data)
    sweep_time = t_before_data_transfer - t_before_trigger
    all_sweep_time.append(sweep_time) # seconds
    
    data_transfer_time = t_end_of_cycle - t_before_data_transfer
    all_data_transfer_time.append(data_transfer_time)
    
    cycle_time = t_end_of_cycle - t_before_trigger
    all_cycle_time.append(cycle_time) 
    
    print("Sweep time: {} ms, data transfer time: {} ms, cycle time: {} ms".format(
        round(sweep_time*1000,2), round(data_transfer_time*1000,2), 
        round(cycle_time*1000,2)))
    sleep(0.01)
    
# show median sweep time
median_sweep_time = median(all_sweep_time)
print("Median sweep time: {} ms".format(round(median_sweep_time * 1000, 2)))

# show median data transfer time
median_data_transfer_time = median(all_data_transfer_time)
print("Median data transfer time: {} ms".format(round(median_data_transfer_time * 1000, 2)))
    
# show median cycle time
median_cycle_time = median(all_cycle_time)
print("Median cycle time: {} ms".format(round(median_cycle_time * 1000, 2)))

# return to internal trigger
CMT.write("TRIG:SOUR INT")
CMT.write('DISP:ENAB ON') # turn display update back on
# CMT.write('SYST:SHOW')









