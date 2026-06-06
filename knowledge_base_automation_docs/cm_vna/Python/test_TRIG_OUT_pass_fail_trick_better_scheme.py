# -*- coding: utf-8 -*-
"""
Created 5/21/2021
Modified 10/24/2022

@author: CMT

"""

import pyvisa   

#rm = pyvisa.ResourceManager('@py') # use pyvisa-py as backend, must install pyvisa-py 
rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # use ni visa 32 bit as backend, must install NI VISA
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
CMT.timeout = 100000

# app = win32com.client.Dispatch("S2VNA.application")

###########################################
###########################################
###### start sending commands here ########
###########################################
###########################################

CMT.write('TRIG:OUTP:STAT OFF') # turn off trigger output
CMT.write("TRIG:SOUR EXT") # set trigger source to external
CMT.write('TRIG:OUTP:POL POS') # set trigger output polarity to positive
CMT.write('TRIG:OUTP:FUNC RTRG') # set trigger function to Ready for Trigger
# CMT.write('TRIG:OUTP:STAT ON')
#CMT.write('SYST:HIDE')
# CMT.write('SYST:SHOW')
# CMT.write('TRIG:OUTP:STAT ON')
CMT.write("INIT:CONT OFF") # set continuous trigger off
CMT.query("*OPC?") # wait until all commands are executed

output_stat = 0
while True:
    
    CMT.write("TRIG:OUTP:STAT " + str(output_stat))
    CMT.write("INIT")
    
    # check if VNA USB connection is ready, if not, stop the loop
    if int(CMT.query("SYST:READ?")) == 0:
        # send signal to PLC here if desired 
        break
    # check if VNA reported error codes, if yes, stop the loop
    if (CMT.query("SYST:ERR?"))[0] != "0":
        # send signal to PLC here if desired 
        break
    
    CMT.query('TRIG:WAIT HOLD;*OPC?')
    failed = CMT.query("CALC:LIM:FAIL?")
    output_stat = 1 - int(failed) # invert 1 to 0 and 0 to 1 because when fail we want OUTP off
        
# CMT.write('SYST:SHOW')



