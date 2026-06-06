# -*- coding: utf-8 -*-
"""
Created 5/21/2021
Modified 10/24/2022

@author: CMT

OVERVIEW:
    This script allocates 2 traces of S11 and captures log mag and phase 
    measurement data into arrays of numbers. Eventually printing them
    
    The VNA software has to be running always when automating the VNA. The VNA 
    software is the driver for the VNA

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

import pyvisa   
import time
import timeit

def delay_ms(ms):
    start_time = timeit.default_timer()
    while (timeit.default_timer() - start_time) * 1000 < ms:
        pass

rm = pyvisa.ResourceManager('@py') # use pyvisa-py as backend, must install pyvisa-py 
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # use ni visa 32 bit as backend, must install NI VISA
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa64.dll')  # use ni visa 64 bit as backend, must install NI VISA

#Connect to a Socket on the local machine at 5025
try:
    CMT = rm.open_resource('TCPIP0::127.0.0.1::5025::SOCKET')
    # CMT = rm.open_resource('TCPIP0::127.0.0.1::hislip0::INSTR')
    
except:
    print("Failure to connect to VNA!")
    print("Check network settings")
#The VNA ends each line with this. Reads will time out without this
CMT.read_termination='\n'
#Set longer timeout period for slower sweeps
CMT.timeout = 10000

###########################################
###########################################
###### start sending commands here ########
###########################################
###########################################

CMT.write('TRIG:OUTP:STAT OFF') # on some VNAs, for example R60, trigger output must be off before trigger source can be changed
CMT.write("TRIG:SOUR EXT") # set trigger source to external
CMT.write('TRIG:OUTP:POL POS') # set trigger output polarity to positive
CMT.write('TRIG:OUTP:FUNC RTRG') # set trigger function to Ready for Trigger
CMT.write('TRIG:OUTP:STAT ON')
# CMT.write('SYST:HIDE') # hide VNA software UI. This slightly improves sweep speed
# CMT.write('SYST:SHOW') # if want to show software UI again after it's hidden, send this command
CMT.query("*OPC?") # make sure all above commands finished executing

# for i in range(500):
while True:
    CMT.query('TRIG:WAIT MEAS;*OPC?') # block code until a sweep starts
    CMT.query('TRIG:WAIT WAIT;*OPC?') # block code until a sweep finishes
    
    failed = CMT.query("CALC:LIM:FAIL?")
    if failed != "1": # when limit test passes
        CMT.write('TRIG:OUTP:POL NEG')
        delay_ms(20) # unit is ms, adjust this as desired, signal stays high for this amount of time
        CMT.write('TRIG:OUTP:POL POS')
        CMT.write('TRIG:OUTP:STAT OFF')
        
CMT.write('SYST:SHOW')



