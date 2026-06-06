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

rm = pyvisa.ResourceManager('@py') # use pyvisa-py as backend, must install pyvisa-py 
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # use ni visa 32 bit as backend, must install NI VISA
#rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa64.dll')  # use ni visa 64 bit as backend, must install NI VISA

#Connect to a Socket on the local machine at 5025
try:
    CMT = rm.open_resource('TCPIP0::127.0.0.1::5025::SOCKET')
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

#CMT.write('SYST:PRESET')

''' set up the VNA '''
CMT.write('DISP:WIND:SPL 2') # allocate 2 trace windows 
CMT.write('CALC1:PAR:COUN 2') # 2 Traces

CMT.write('CALC1:PAR1:DEF S11') #Choose S11 for trace 1
CMT.write('CALC1:PAR2:DEF S11') #Choose S11 for trace 2

CMT.write('CALC1:PAR1:SEL')
CMT.write('CALC1:FORM MLOG')  #log Mag format

# select the trace first and then choose a measurement format
CMT.write('CALC1:PAR2:SEL')
CMT.write('CALC1:FORM PHAS') # phase format

CMT.write('TRIG:SOUR BUS')

# Always end an *OPC? command after all the VNA setups to make sure the setups are 
# complete before making measurement
CMT.query('*OPC?')

''' start VNA measurement, put this section inside a loop to measure continuously '''
# Trigger a measurement
CMT.write('TRIG:SING') #Trigger a single sweep
CMT.query('*OPC?') #Wait for measurement to complete

# Read frequency data
Freq = CMT.query_ascii_values("SENS1:FREQ:DATA?")

# Read log mag data
CMT.write('CALC1:PAR1:SEL')
M = CMT.query_ascii_values("CALC1:DATA:FDAT?")

# Read phase data
CMT.write('CALC1:PAR2:SEL')
P = CMT.query_ascii_values("CALC1:DATA:FDAT?")

''' VNA measurement section ends here '''

''' change the trigger source back to internal after automation '''
CMT.write('TRIG:SOUR INT')

''' print results '''

# remove all the 0s from the data (every other number)
# Note: this is only needed when FDAT is queried when the trace format is not 
#       one of the polar formats because every other number is zero
P = P[::2] 
M = M[::2]

# display data in the python console
print("frequency=")
print(Freq)

print("Log mag=")
print(M)

print("Phase=")
print(P)






