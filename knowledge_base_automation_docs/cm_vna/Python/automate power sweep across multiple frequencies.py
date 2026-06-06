# -*- coding: utf-8 -*-
"""
Created 10/30/2025

@author: CMT

OVERVIEW:
    This script allocates S21 on the upper window and B(1) receiver on the lower window.
    It does several power sweeps, each at a different frequency and prints the result in text.
    Make sure at the highest power during the power sweep the power into the VNA port is 
    below damage level before running this script
    
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

''' set up the VNA display'''
CMT.write('DISP:WIND:SPL 2') # allocate 2 trace windows 
CMT.write('CALC1:PAR:COUN 2') # 2 Traces

CMT.write('CALC1:PAR1:DEF S21') # choose S21 for trace 1
CMT.write('CALC1:PAR2:DEF B') # choose test receiver on port 2 for trace 2
CMT.write("CALC:PAR2:SPOR 1") # choose port 1 as source port for trace 2

# select the trace first and then choose a measurement format
CMT.write('CALC1:PAR1:SEL')
CMT.write('CALC1:FORM MLOG')  #log Mag format
CMT.write('CALC1:PAR2:SEL')
CMT.write('CALC1:FORM MLOG')

''' set up power sweep '''
CMT.write("SENS:SWE:TYPE POW") # select power sweep
CMT.write("SOUR:POW:STOP -10") # power sweep stop power level dbm
CMT.write("SOUR:POW:STAR -55") # power sweep start power level dbm

#CMT.write("OUTP 0") # turn off RF output before measurement for safety

CMT.write('TRIG:SOUR BUS')

# Always send an *OPC? command after all the VNA setups to make sure the setups are 
# complete before making measurement
CMT.query('*OPC?')

''' start power sweep measurement for a list of frequencies'''
freq_list = [1e9, 2e9, 3e9, 4e9, 5e9] # list of frequencies the power sweep should loop through, in Hz

for freq in freq_list:
    CMT.write("SENS:FREQ " + str(freq)) # set the power sweep's frequency    
    #CMT.write("OUTP 1") # turn on RF output
    
    # Trigger a measurement
    CMT.write('TRIG:SING') # trigger a single sweep
    CMT.query('*OPC?') # wait for measurement to complete

    # Read power data
    power = CMT.query_ascii_values("CALC:DATA:XAX?")
    
    # Read log mag data
    CMT.write('CALC1:PAR1:SEL')
    S21 = CMT.query_ascii_values("CALC1:DATA:FDAT?")
    
    # Read B1 absolute power data
    CMT.write('CALC1:PAR2:SEL')
    B1 = CMT.query_ascii_values("CALC1:DATA:FDAT?")

    # remove all the 0s from the data (every other number)
    # Note: this is only needed when FDAT is queried when the trace format is not 
    #       one of the polar formats because every other number is zero
    S21 = S21[::2]
    B1 = B1[::2]
    
    # Print results
    current_freq = CMT.query("SENS:FREQ?")
    print("Frequency = " + current_freq + " Hz")
    
    print("Power=")
    print(power)

    print("S21 Log mag=")
    print(S21)

    print("B1 receiver=")
    print(B1)    
''' VNA measurement section ends here '''

''' change the trigger source back to internal after automation '''
CMT.write('TRIG:SOUR INT')







