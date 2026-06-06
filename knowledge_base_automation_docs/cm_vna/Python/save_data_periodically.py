# -*- coding: utf-8 -*-
'''
Created on 10/1/2020
Modified on 5/29/2024

OVERVIEW:
    This script saves csv/touchstone/screenshot files periodically under the same directory as this script.
    The VNA software has to be running always when automating the VNA. The VNA software
    is the driver for the VNA

Before running the code:
    1. Make sure S2VNA software is running
    2. Go to system -> Misc setup -> network remote settings -> turn on socket server
    3. make sure socket server is 5025

Additional information:
    1. The SCPI programming manual is intalled with the VNA software. By default:
        C:\VNA\S2VNA\Doc\
    
'''

import pyvisa    #PyVisa is required along with NIVisa
from time import sleep
import os 


rm = pyvisa.ResourceManager('@py')
#Connect to a Socket on the local machine at 5025
#Use the IP address of a remote machine to connect to it instead
try:
    CMT = rm.open_resource('TCPIP0::127.0.0.1::5025::SOCKET')
except:
    print("Failure to connect to VNA!")
    print("Check network settings")
#The VNA ends each line with this. Reads will time out without setting the termination character
CMT.read_termination='\n'
#Set a really long timeout period for slow sweeps
CMT.timeout = 10000

###########################################
###########################################
##### start sending SCPI commands here ####
###########################################
###########################################

# get the directory where this python script is located, the csv file will be saved in the same folder
file_path = os.path.dirname(os.path.realpath(__file__))
for i in range(100):

    CMT.write("TRIG:SOUR BUS")
    CMT.write("TRIG:SING")
    CMT.query("*OPC?")
    
    # save a csv file of all traces
    CMT.write("MMEM:STOR:FDAT:SCOP ALL")
    command = 'MMEM:STOR:FDAT ' + '"' + file_path + '/measurement' + '{}'.format(i) + '.csv"'
    CMT.write(command)
    
    # save an s2p file for port 1, 2
    CMT.write("MMEM:STOR:SNP:TYPE:S2P 1,2")
    command = 'MMEM:STOR:SNP ' + '"' + file_path + '/measurement' + '{}'.format(i) + '"'
    CMT.write(command)
    
    # save a screenshot
    CMT.write("HCOP:IMAG NORM")
    CMT.write("HCOP:PAIN COL")
    command = 'MMEM:STOR:IMAG ' + '"' + file_path + '/measurement' + '{}'.format(i) + '.png"'
    CMT.write(command)
    
    # set trigger source back to internal to keep the VNA sweeping and warm
    CMT.write("TRIG:SOUR INT")
    sleep(60 * 10)   # unit is in seconds
 
# before the program finishes, set trigger source back to internal
CMT.write("TRIG:SOUR INT\n")



