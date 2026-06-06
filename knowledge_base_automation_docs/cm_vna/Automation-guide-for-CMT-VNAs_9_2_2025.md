# Automation-guide-for-CMT-VNAs_9_2_2025

**Source:** Automation-guide-for-CMT-VNAs_9_2_2025.pdf

---

## Page 1


### AUTOMATION GUIDE FOR

09/22/2021
CMT VNAs
Table of Contents
Important concepts for automating CMT USB VNAs ................. 2
What are SCPI commands? ...................................................... 2
Why SCPI Automation? ............................................................. 2
How to automate VNAs .............................................................. 3
VISA vs TCP Client ..................................................................... 3
Where to find programming manuals .......................................... 4
Where to find programming examples ........................................ 4
Tricks to find SCPI commands ................................................... 4
Hide the VNA software user interface ......................................... 4
Binary data transfer .................................................................... 5
Programmatically launch VNA software ..................................... 5
Automate multiple VNAs by assigning serial numbers ............... 5
Assign serial numbers using commandline command ........ 6
Assign serial numbers using SCPI command ..................... 6
What is COM (Component Object Model) automation? ............. 7
Troubleshooting COM automation .............................................. 7
Conclusion .................................................................................. 7
1
www.coppermountaintech.com

### Tables

## Page 2

AUTOMATION GUIDE FOR CMT VNAs 09/22/2021
Important concepts for automating CMT USB VNAs
CMT VNAs are USB-based and do not have built-in computers. There are a few benefits to having the VNA

### measurement module separate from the processing module. When they are separated, the user isn’t stuck

with an obsolete built-in PC in a few years. It also means that the VNA can be smaller in size, making it
more lightweight and portable.
The VNAs must run with an external PC and the VNA software (RVNA, TRVNA, S2VNA or S4VNA) to
work. You can consider the VNA software as the driver for VNAs. When you write code to automate VNAs,
you are communicating with the VNA software, which then communicates with the physical VNA through
USB connection.
This means even if automating the VNA with code, the VNA software must still be running, and it should not
be closed during automation. The VNA software user interface can be hidden, but it must always be
running in the background. This can be confusing because other VNA manufacturers have built-in PCs in
the VNAs, and a separate instance of the VNA software isn’t necessary on the computer automating the
network analyzer. Because of this, if you want to automate the entire measurement process without using
the VNA software’s user interface, you must programmatically run the VNA software.
There are two methods for automating CMT VNAs. One is using SCPI commands and the other is using
COM (Component Object Model) functions. Our new CMTVNA software only supports automation through
SCPI commands.
What are SCPI commands?
SCPI, pronounced “skippy”, stands for "Standard Commands for Programmable Instruments". It is an
industry standard for text commands used to control test instruments. Automating a VNA with SCPI refers
to establishing a connection between the code and the VNA software. Once connected, SCPI commands
are sent to the VNA software to automate it. An example of a SCPI command looks like this:
"SENS:FREQ:STAR 1000000". This command tells the VNA to set the STARt FREQuency of

### measurement to 1MHz. The SCPI command typically gives context for how it is used. If you don't know the


### command for a specific action, you won't be able to come up with it easily. This is when the programming

manual is especially useful; to find the SCPI commands and build your code.
Why SCPI Automation?
Automating VNAs with SCPI commands is recommended because:
1) SCPI commands are clearer than COM object functions. The syntax to use COM object functions may
not be obvious in some languages (like Python and MATLAB), but SCPI commands will always be the
same for any programming language.
2) SCPI gives you a more stable data transfer speed. This result is based on experiments.
2
www.coppermountaintech.com

### Tables

## Page 3

AUTOMATION GUIDE FOR CMT VNAs 09/22/2021
3) Only one VNA can be automated on a single computer with COM. SCPI commands can run multiple
instances of the VNA software and automate multiple VNAs connected to the same PC by assigning
different socket server numbers to each instance.
How to automate VNAs
To send SCPI commands to a VNA, you need to establish a connection to the VNA software from your
code. The connection can be either TCP/IP socket connection or TCP\IP Hislip connection. The connection
can be established in one of two ways:

### 1. Use standard TCP client library offered by each programming language.


### 2. Use VISA.

Before establishing a TCP connection from the code to the VNA software, the VNA software must be
running, the correct socket number must be used, and the socket server must be turned on. The IP address

### 127.0.0.1 should be used when automating VNAs connected to the same PC running the code. This is

because 127.0.0.1 is a special IP address that represents the local PC. You will see this address used in all
the examples on our website and you typically should not change this IP address. It can be confusing
because every machine has a different IP address and logically it would seem that the same IP address
should not be used.
To turn on socket server in RVNA, go to "system" -> "network setup" -> "socket server on".
To turn on socket server in S2VNA/S4VNA/TRVNA, go to "system" -> "misc setup" -> "network remote
control settings" -> "socket server on"
The complete process for VNA automation using SCPI commands is as follows:
1) In the VNA software, turn on TCP/IP socket server, remember the socket number used. Make sure the
VNA software continues running.
2) In the code, establish a connection to the VNA software through TCP/IP socket.
3) In the code, set up the VNA stimulus (frequency, IFBW, number of points) using SCPI commands.
4) In the code, set up formats for traces and software UI display using SCPI commands.
5) In the code, trigger VNA and capture measurement data using SCPI commands. For continuous

### measurement, set up a loop.

VISA and TCP Client
VISA stands for “Virtual Instrument Software Architecture”. It is an API (Application Programming Interface)
for controlling test and measurement instruments. There are many implementations of VISA, like NI-VISA,
Keysight VISA, and pyvisa-py for Python which all function very similarly. We use NI-VISA and pyvisa-
py(for python) to automate CMT VNAs because these are both free to use and easily obtainable. NI VISA
can be downloaded here: https://www.ni.com/en-us/support/downloads/drivers/download.ni-
visa.html#346210.
Programming languages usually have standard TCP client libraries that allow you to start a TCP\IP

### connection. When choosing TCP Client instead of VISA to automate VNAs using SCPI commands, special

3
www.coppermountaintech.com

### Tables

## Page 4

AUTOMATION GUIDE FOR CMT VNAs 09/22/2021
attention is needed for the reading function. In the reading function, data must be constantly read until the
newline character (“\n”) is received. This is the termination character for a VNA response message. If the
reading function is not properly set up when the VNA stimulus is set up to sweep more than 1601 points,
the data may not be completely read. This can then cause a bigger problem of the leftover data appearing
in the next query response. A wrong response will then be received for all other queries. In the examples
that use TCP client, like the C# simple example and MATLAB example, the reading function already takes
care of this issue. Thus, it is recommended to copy and paste the reading functions shown in the examples
to the code.
Where to find programming manuals
Programming manuals are located inside the “Doc” folder under the VNA software directory. The VNA
software can be installed in any directory during the installation process. By default, the VNA software is
installed to C:\VNA\RVNA or TRVNA or S2VNA or S4VNA\.
Where to find programming examples
CMT is constantly uploading more and more helpful programming examples in various programming
languages to the website. All topics mentioned in this app note are demonstrated in those examples. To
download programming examples, go to our website’s automation page:
https://coppermountaintech.com/automation/.
Most of our plug-ins are open source. The source code of these plug-ins can be reviewed and referred to
as examples: https://github.com/Copper-Mountain-Technologies.
Tricks to find SCPI commands
1) In the programming manual, most of the SCPI commands have their equivalent softkeys noted under the

### commands. Knowing what buttons would be used in the software user interface helps determine how to

automate that sequence of actions. To find commands, use Ctrl+F to search for the buttons in the
programming manual.
2) The programming manual groups related SCPI commands, and they typically have the same keyword in
them. For example, when automating marker-related actions, use Ctrl+F and search for "mark" and it will
show a list of marker-related SCPI commands. For another example, when automating ACM-related
actions, search for "ecal" because all ACM-related SCPI commands have "ecal" in them. When using the
‘find’ function in the manual, do the search at the beginning of the programming manual because that is
where there is a list of all available SCPI commands.
Hide the VNA software user interface
Without manually starting the software before running code, the VNA software can be launched by using

### commandline command. This way the entire process can be automated, including launching the VNA

software. Socket server can also be started with the commandline prompt. To turn socket port 5025 on:
4
www.coppermountaintech.com

### Tables

## Page 5

AUTOMATION GUIDE FOR CMT VNAs 09/22/2021
For S2VNA and S4VNA: C:\VNA\S2VNA.exe /SocketServer:on /SocketPort:5025
For RVNA and TRVNA: C:\VNA\RVNA.exe EnableSocket:5025
Note that turning socket server on and hiding the software UI can be combined in one line, like this:
For S2VNA and S4VNA: C:\VNA\S2VNA.exe /SocketServer:on /SocketPort:5025 /visible:off
For RVNA and TRVNA: C:\VNA\RVNA.exe EnableSocket:5025 InvisibleMode
Also, note these commands are assuming the VNA software is installed to the default location. If that is not
the case, the command needs to be modified with the actual VNA software location or the VNA software
path can be added to the command prompt's PATH variable and directly call the VNA software executable.
These commandline options also work with CMT’s VNA software for Linux.
For S2VNA and S4VNA, you can explore more interesting commandline options by running
C:\VNA\S2VNA\S2VNA.exe /?.
If using SCPI to automate the VNA, send command "SYST:HIDE" and "SYST:SHOW" to hide and show the
user interface. Use command “SYST:TERM” to terminate the VNA software after the measurement is
completed.
If using COM to automate the VNA, call function app.SCPI.SYSTem.Hide and app.SCPI.SYSTem.Show to
hide and show the user interface.
Binary data transfer
CMT VNAs offer the ability to transfer measurement data in binary format. When the VNA is not configured
to do binary data transfer, the data response from the VNA is sent back in ASCII text format. If the VNA is
configured to do binary data transfer, either 32-bit float or 64-bit float can be chosen. For example, if the
VNA wants to send a number 1e9(1GHz) as a response to a query, it will be sent to the code as string
"+1.0000000000E+09" which is 17 characters. Each character is 1 byte so each number is 17 bytes long. If
the VNA is configured to transfer data in binary format and select 32-bit float format, then the number 1e9
will be sent to your code as 01001110011011100110101100101000 in binary or 0x4e6e6b28 in hex. Each
number is only 4 bytes. Because the VNA is now sending 13 bytes less for each number, the data transfer
speed will be faster. Typically, binary data transfer is not necessary because the speed difference is not
that significant for a typical application.
Automate multiple VNAs by assigning serial numbers
For automating multiple VNAs, the recommended method is to install multiple copies of the VNA software
on the machine and assign a VNA to each copy using serial numbers. Run the VNA software installer
multiple times and install the software to a different directory each time. This will install multiple copies of
the same software. For example, folders can be named as such:
5
www.coppermountaintech.com

### Tables

## Page 6

AUTOMATION GUIDE FOR CMT VNAs 09/22/2021
Running the same copy of VNA software multiple times to connect to multiple VNAs is an option but
installing multiple copies of VNA software is recommended over this. It is less confusing because each
software copy can be dedicated to a physical VNA. Then save state files, touchstone files, or screenshots
for VNAs separately by saving them to their own folders in the individual software copies.
A serial number can be assigned to a copy of VNA software during the installation process. However, there
are more flexible options for after installation.
Assign serial numbers using commandline command
When programmatically launching the VNA software, serial numbers can be assigned, a specific socket
port number turned on, and the VNA software UI hidden in the same line of code for launching the VNA
software. This is achieved by using commandline option strings.
Starting from version 21.1.7, for S2VNA and S4VNA software, serial numbers can be assigned using

### commandline command and SCPI command. The option strings are ‘/SerialNumber:<num>’,

‘/SocketServer:on /SocketPort:<num>’ and ‘/visible:off’. For example:
In python:
import subprocess
# note the space in front of /SocketServer:on. It must have this space.
subprocess.run(['C:/VNA/S2VNA_copy1/S2VNA.exe', ' /SocketServer:on /SocketPort:5026
/SerialNumber:12345678 /visible:off'])
In C#:
using System.Diagnostics;
Process.Start("C:\\VNA\\S2VNA_copy1\\S2VNA.exe", "/SocketServer:on /SocketPort:5025
/SerialNumber:12345678 /visible:off");
Starting from RVNA 21.3.0 and TRVNA 21.3.1 software, serial number can be assigned using

### commandline command and SCPI command. The option strings are “SerialNumber:<num>”,

“EnableSocket:<num>” and “InvisibleMode”.
Before the program is finished, make sure to send SCPI command “SYST:TERM” to terminate the
software. Otherwise, many software instances could be launched to run in the background.
Assign serial numbers using SCPI command
Serial numbers can be assigned to VNA software using a SCPI command. The SCPI command is
“SYST:CONN:SER:NUMB <>”. This command also allows query “SYST:CONN:SER:NUMB?”. This query
6
www.coppermountaintech.com

### Tables

## Page 7

AUTOMATION GUIDE FOR CMT VNAs 09/22/2021
can be used to determine which VNA is connected to which copy of software to avoid manually assigning
serial numbers.
What is COM (Component Object Model) automation?
COM stands for Microsoft "Component Object Model". This should not be confused with serial
communication port COM; they are not related. The saying of "automating a VNA with COM", means to use
the functions contained inside the COM object of the VNA software to tell the VNA to do different actions.
An example of a COM object function looks like this: app.SCPI.SENSe(Ch).FREQuency.STARt = 1000000.
Notice this achieves the same action of setting the VNA start frequency to 1MHz as in the previous SCPI

### example. However, this time a command is not being sent in text form to the VNA. Instead, a function

contained in the COM object of the VNA software is being called. The function name has SCPI included. It
can be confusing, but the reason the COM object functions are named in this way is to stay consistent with
the corresponding SCPI commands. The manual for COM functions is located under the same folder as the
SCPI programming manual. If only one programming manual is available in the \Doc\ folder, the SCPI and
COM manuals are combined into one.
To use COM object functions to automate a VNA, it is necessary to make sure the checkbox that says
"register COM server" is checked in the last step of the VNA software installer. A message will appear
saying "COM server registered successfully" after you install the software with the checkbox selected.
Troubleshooting COM automation
If the COM automation does not work and gives strange error messages, first try re-registering the COM
server. It has been commonly found that unexpected changes occur, and the COM server is unexpectedly
not registered. To register the COM server after installation:
1) Run cmd.exe as administrator. It must be run as admin, otherwise it does not work. It may still show
"COM server registered successfully", but that will not always be true.
2) For all VNA software versions: C:\VNA\RVNA.exe /regserver
C:\VNA\TRVNA.exe /regserver
C:\VNA\S2VNA.exe /regserver
C:\VNA\S4VNA.exe /regserver
If the code is using COM to automate the VNA, it is not necessary to run the VNA software before running
code. When the COM object is first created in the code, if it is identified that the VNA software is not
running, it will run automatically. If the VNA software is already launched before running the code, another
copy of the software will not be launched. Because of this, it is not necessary to close the VNA software
before running your COM code.
7
www.coppermountaintech.com

### Tables

## Page 8

AUTOMATION GUIDE FOR CMT VNAs 09/22/2021
Conclusion
CMT VNAs are very easy to automate. CMT offers a well-documented programming manual for all
available SCPI commands, many helpful examples, and open-source plugins. To automate VNAs, the
correct SCPI command from the programming manual needs to be identified and then sent through a
TCP/IP connection with the VNA software. The VNA software must be running during automation but there
are ways to hide the user interface if desired. For more questions about automation or support in finding
errors in code, please email us at support@coppermountaintech.com. We are always happy to help.
8
www.coppermountaintech.com

### Tables

