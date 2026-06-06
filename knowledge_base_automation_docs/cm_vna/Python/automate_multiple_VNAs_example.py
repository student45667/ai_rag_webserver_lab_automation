# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 15:54:24 2021

@author: Patrick.l

OVERVIEW:
    This example demonstrates how to automate two CMT VNAs connected to the same 
    PC. For more than two VNAs, the concept is the same. This example assumes two 
    copies of VNA software have been installed under:
    C:/VNA/RVNA_copy1 and C:/VNA/RVNA_copy2
    
    This example uses subprocess module to run the VNA software and assign different
    socket number and serial number to each VNA software instance. This is to keep track
    of which VNA is connected which software instance. The key concept of automating 
    multiple VNAs is to run multiple VNA software instances and assign different socket 
    numbers to them.
"""

import subprocess
import pyvisa
from time import sleep

# VISA connection
def connect_to_vna_socket(IP_address = "127.0.0.1", socket_number = 5025, timeout = 10000):
    rm = pyvisa.ResourceManager()  # uses pyvisa-py
    #rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa32.dll')  # uses ni visa 32 bit
    #rm = pyvisa.ResourceManager('C:/WINDOWS/system32/visa64.dll')  # uses ni visa 64 bit
    
    #Connect to a Socket on the local machine at 5025
    #Use the IP address of a remote machine to connect to it instead
    try:
        CMT = rm.open_resource("TCPIP0::" + IP_address + "::" + str(socket_number) + "::SOCKET")
    except:
        print("Failure to connect to VNA!")
        print("Check network settings")
    #The VNA ends each line with this. Reads will time out without this
    CMT.read_termination='\n'
    
    #Set a really long timeout period for slow sweeps
    CMT.timeout = timeout
    return CMT

if __name__ == "__main__":
    # # For S2 and S4 VNA, to hide the VNA software UI change /visible:on to /visible:off
    # subprocess.Popen(['C:/VNA/S2VNA_copy1/S2VNA.exe', ' /SocketServer:on /SocketPort:5025 /SerialNumber:12345678 /visible:on'])
    # subprocess.Popen(['C:/VNA/S2VNA_copy2/S2VNA.exe', ' /SocketServer:on /SocketPort:5026 /SerialNumber:87654321 /visible:on'])
    
    # # For RVNA and TRVNA, assigning serial number and hiding the VNA software UI
    # subprocess.Popen(['C:/VNA/RVNA_copy1/RVNA.exe', ' EnableSocket:5025 SerialNumber:12345678 InvisibleMode'])
    # subprocess.Popen(['C:/VNA/RVNA_copy2/RVNA.exe', ' EnableSocket:5026 SerialNumber:87654321 InvisibleMode'])
    
    # For RVNA and TRVNA, not assigning serial number and showing the VNA software UI 
    subprocess.Popen(['C:/VNA/RVNA_copy1/RVNA.exe', ' EnableSocket:5025'])
    subprocess.Popen(['C:/VNA/RVNA_copy2/RVNA.exe', ' EnableSocket:5026'])
    
    
    sleep(5)
    CMT1 = connect_to_vna_socket(socket_number = 5025)
    CMT2 = connect_to_vna_socket(socket_number = 5026)

    # send SCPI commands to RVNA copy 1
    CMT1.write("SENS:FREQ:STAR 1e9")
    # send SCPI commands to RVNA copy 2
    CMT2.write("SENS:FREQ:STAR 1e9")