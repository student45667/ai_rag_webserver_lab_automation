# PDF Extracted Markdown

**Source:** Keysight_InfiniiVision6000XSeries_usermanual.pdf

**Pages:** 540

**Extraction Date:** 2026-05-26T02:03:52.820848

---

Keysight InfiniiVision
6000 X-Series Oscilloscopes
User's Guide

---
**[Page 1]**

2 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide
Notices
© Keysight Technologies, Inc. 2005-2015 terms in the separate agreement shall the DFARS and are set forth specifically in
control. writing elsewhere in the EULA. Keysight shall
No part of this manual may be reproduced in
be under no obligation to update, revise or
any form or by any means (including
Technology License otherwise modify the Software. With respect
electronic storage and retrieval or translation
to any technical data as defined by FAR
into a foreign language) without prior The hardware and/or software described in
2.101, pursuant to FAR 12.211 and 27.404.2
agreement and written consent from this document are furnished under a license
and DFARS 227.7102, the U.S. government
Keysight Technologies, Inc. as governed by and may be used or copied only in
acquires no greater than Limited Rights as
United States and international copyright accordance with the terms of such license.
defined in FAR 27.401 or DFAR 227.7103-5
laws.
(c), as applicable in any technical data.
U.S. Government Rights
Manual Part Number
Safety Notices
The Software is "commercial computer
54609-97012 software," as defined by Federal Acquisition
Regulation ("FAR") 2.101. Pursuant to FAR
Edition 12.212 and 27.405-3 and Department of CAUTION
Defense FAR Supplement ("DFARS")
Second edition, September 2015
227.7202, the U.S. government acquires A CAUTION notice denotes a hazard.
Printed in Malaysia commercial computer software under the
It calls attention to an operating
Published by: same terms by which the software is
procedure, practice, or the like that,
Keysight Technologies, Inc. customarily provided to the public.
1900 Garden of the Gods Road Accordingly, Keysight provides the Software if not correctly performed or
Colorado Springs, CO 80907 USA to U.S. government customers under its adhered to, could result in damage
standard commercial license, which is
to the product or loss of important
Print History embodied in its End User License Agreement
(EULA), a copy of which can be found at data. Do not proceed beyond a
54609-97000, April 2014 www.keysight.com/find/sweula. The CAUTION notice until the indicated
54609-97012, September 2015 license set forth in the EULA represents the conditions are fully understood and
exclusive authority by which the U.S.
met.
Warranty government may use, modify, distribute, or
disclose the Software. The EULA and the
The material contained in this document is license set forth therein, does not require or
provided "as is," and is subject to being permit, among other things, that Keysight: (1)
WARNING
changed, without notice, in future editions. Furnish technical information related to
Further, to the maximum extent permitted commercial computer software or
by applicable law, Keysight disclaims all commercial computer software A WARNING notice denotes a
warranties, either express or implied, with documentation that is not customarily hazard. It calls attention to an
regard to this manual and any information provided to the public; or (2) Relinquish to, or
operating procedure, practice, or
contained herein, including but not limited otherwise provide, the government rights in
to the implied warranties of merchantability excess of these rights customarily provided the like that, if not correctly
and fitness for a particular purpose. to the public to use, modify, reproduce, performed or adhered to, could
Keysight shall not be liable for errors or for release, perform, display, or disclose result in personal injury or death.
incidental or consequential damages in commercial computer software or
Do not proceed beyond a WARNING
connection with the furnishing, use, or commercial computer software
performance of this document or of any documentation. No additional government notice until the indicated
information contained herein. Should requirements beyond those set forth in the conditions are fully understood and
Keysight and the user have a separate EULA shall apply, except to the extent that met.
written agreement with warranty terms those terms, rights, or licenses are explicitly
covering the material in this document that required from all providers of commercial
conflict with these terms, the warranty computer software pursuant to the FAR and
|  |
|---|
|  |
|  |
|---|
|  |

---
**[Page 2]**

Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide 3
InfiniiVision 6000 X-Series Oscilloscopes—At a Glance
Table 1 6000 X-Series Model Numbers, Bandwidths, Sample Rates
Model Analog Digital Bandwidth Options Sample Rate (interleaved,
Channels Channels non-interleaved)
DSO-X 6002A 2 • (none) = 1 GHz 20 GSa/s, 10 GSa/s
• BW250 = 2.5 GHz
DSO-X 6004A 4
• BW400 = 4 GHz
MSO-X 6002A 2 16 • BW600 = 6 GHz
MSO-X 6004A 4 16
The Keysight InfiniiVision 6000 X-Series oscilloscopes deliver these features:
• 1 GHz, 2.5 GHz, 4 GHz, and 6 GHz bandwidth options.
|  |
|---|
|  |
| Model | Analog
Channels | Digital
Channels | Bandwidth Options | Sample Rate (interleaved,
non-interleaved) |
|---|---|---|---|---|
| DSO-X 6002A | 2 |  | • (none) = 1 GHz
• BW250 = 2.5 GHz
• BW400 = 4 GHz
• BW600 = 6 GHz | 20 GSa/s, 10 GSa/s |
| DSO-X 6004A | 4 |  |  |  |
| MSO-X 6002A | 2 | 16 |  |  |
| MSO-X 6004A | 4 | 16 |  |  |

---
**[Page 3]**

4 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide
• 2- and 4-channel digital storage oscilloscope (DSO) models.
• 2+16-channel and 4+16-channel mixed-signal oscilloscope (MSO) models.
An MSO lets you debug your mixed-signal designs using analog signals and
tightly correlated digital signals simultaneously. The 16 digital channels have a
1 GSa/s sample rate, with a 250 MHz toggle rate.
• 12.1 inch SVGA capacitive touchscreen display. The touchscreen makes the
oscilloscope easier to use:
• You can use the pinch and flick multi-touch gestures on waveforms to
change a channel's V/div setting, the time/div setting, or the delay time.
• You can "touch" inside alpha-numeric keypad dialogs to enter file, label,
network, and printer names, etc., instead of using softkeys and the
Entry knob.
• You can drag a finger across the screen to draw rectangular boxes for
zooming in on waveforms or setting up Zone triggers.
• You can touch the blue menu icon in the sidebar to display information or
control dialogs. You can drag (undock) these dialogs out of the sidebar, for
example, to view cursor values and measurements at the same time.
• You can touch other areas of the screen as substitutes for using front panel
keys, softkeys, and knobs.
• Voice control commands for hands-free operation.
• Interleaved 4 Mpts or non-interleaved 2 Mpts MegaZoom IV memory for the
fastest waveform update rates.
• All knobs are pushable for making quick selections.
• Trigger types: edge, edge then edge, pulse width, pattern, OR, rise/fall time,
Nth edge burst, runt, setup & hold, video, and zone.
• Math waveforms: add, subtract, multiply, divide, FFT, d/dt, integrate, square
root, Ax+B, square, absolute value, common logarithm, natural logarithm,
exponential, base 10 exponential, low pass filter, high pass filter, averaged
value, smoothing, magnify, max/min hold, measurement trend, chart logic bus
timing, chart logic bus state, and clock recovery.
• Reference waveform locations (4) for comparing with other channel or math
waveforms.
• Many built-in measurements and a measurement statistics display.

---
**[Page 4]**

Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide 5
• Serial decode/trigger options for: CAN/LIN, FlexRay, I2C/SPI, I2S,
UART/RS232, MIL-STD-1553/ARINC 429, SENT, and USB. There is a Lister for
displaying serial decode packets.
• Jitter measurement analysis and real-time eye analysis option.
• Analysis features/options including: Color grade waveform analysis, digital
voltmeter (DVM) and counter option, histogram display/statistics, mask testing
option, power measurements and analysis option, and precision measurements
and math functions.
• Built-in, license-enabled 2-channel waveform generator with: arbitrary, sine,
square, ramp, pulse, DC, noise, sine cardinal, exponential rise, exponential fall,
cardiac, and Gaussian pulse. Modulated waveforms on WaveGen1 except for
arbitrary, pulse, DC, and noise waveforms.
• USB and LAN ports make printing, saving, and sharing data easy.
• VGA port for displaying the screen on a different monitor.
• A Quick Help system is built into the oscilloscope. Press and hold any key to
display Quick Help. Complete instructions for using the quick help system are
given in “Access the Built-In Quick Help" on page 62.
For more information about InfiniiVision oscilloscopes, see:
www.keysight.com/find/scope

---
**[Page 5]**

6 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide
In This Guide
This guide shows how to use the InfiniiVision 6000 X-Series oscilloscopes.
When unpacking and using the • Chapter 1, “Getting Started,” starting on page 27
oscilloscope for the first time, see:
When displaying waveforms and • Chapter 2, “Horizontal Controls,” starting on page 65
acquired data, see: • Chapter 3, “Vertical Controls,” starting on page 81
• Chapter 4, “Math Waveforms,” starting on page 91
• Chapter 5, “Reference Waveforms,” starting on page
127
• Chapter 6, “Digital Channels,” starting on page 131
• Chapter 7, “Serial Decode,” starting on page 149
• Chapter 8, “Display Settings,” starting on page 155
• Chapter 9, “Labels,” starting on page 165
When setting up triggers or changing • Chapter 10, “Triggers,” starting on page 171
how data is acquired, see: • Chapter 11, “Trigger Mode/Coupling,” starting on
page 209
• Chapter 12, “Acquisition Control,” starting on page
217
Making measurements and analyzing • Chapter 13, “Cursors,” starting on page 235
data: • Chapter 14, “Measurements,” starting on page 245
• Chapter 15, “Histogram,” starting on page 277
• Chapter 16, “Color Grade Waveform,” starting on page
287
• Chapter 17, “Jitter and Real-Time Eye Analysis,”
starting on page 291
• Chapter 18, “Mask Testing,” starting on page 303
• Chapter 19, “Digital Voltmeter and Counter,” starting
on page 317
When using the built-in license • Chapter 20, “Waveform Generator,” starting on page
enabled waveform generator, see: 323
When saving, recalling, or printing, • Chapter 21, “Save/Email/Recall (Setups, Screens,
see: Data),” starting on page 343
• Chapter 22, “Print (Screens),” starting on page 357
When using the oscilloscope's utility • Chapter 23, “Utility Settings,” starting on page 363
functions or web interface, see: • Chapter 24, “Web Interface,” starting on page 383
| When unpacking and using the
oscilloscope for the first time, see: | • Chapter 1, “Getting Started,” starting on page 27 |
|---|---|
| When displaying waveforms and
acquired data, see: | • Chapter 2, “Horizontal Controls,” starting on page 65
• Chapter 3, “Vertical Controls,” starting on page 81
• Chapter 4, “Math Waveforms,” starting on page 91
• Chapter 5, “Reference Waveforms,” starting on page
127
• Chapter 6, “Digital Channels,” starting on page 131
• Chapter 7, “Serial Decode,” starting on page 149
• Chapter 8, “Display Settings,” starting on page 155
• Chapter 9, “Labels,” starting on page 165 |
| When setting up triggers or changing
how data is acquired, see: | • Chapter 10, “Triggers,” starting on page 171
• Chapter 11, “Trigger Mode/Coupling,” starting on
page 209
• Chapter 12, “Acquisition Control,” starting on page
217 |
| Making measurements and analyzing
data: | • Chapter 13, “Cursors,” starting on page 235
• Chapter 14, “Measurements,” starting on page 245
• Chapter 15, “Histogram,” starting on page 277
• Chapter 16, “Color Grade Waveform,” starting on page
287
• Chapter 17, “Jitter and Real-Time Eye Analysis,”
starting on page 291
• Chapter 18, “Mask Testing,” starting on page 303
• Chapter 19, “Digital Voltmeter and Counter,” starting
on page 317 |
| When using the built-in license
enabled waveform generator, see: | • Chapter 20, “Waveform Generator,” starting on page
323 |
| When saving, recalling, or printing,
see: | • Chapter 21, “Save/Email/Recall (Setups, Screens,
Data),” starting on page 343
• Chapter 22, “Print (Screens),” starting on page 357 |
| When using the oscilloscope's utility
functions or web interface, see: | • Chapter 23, “Utility Settings,” starting on page 363
• Chapter 24, “Web Interface,” starting on page 383 |

---
**[Page 6]**

Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide 7
For reference information, see: • Chapter 25, “Reference,” starting on page 399
When using licensed serial bus • Chapter 26, “CAN/LIN Triggering and Serial Decode,”
triggering and decode features, see: starting on page 419
• Chapter 27, “FlexRay Triggering and Serial Decode,”
starting on page 441
• Chapter 28, “I2C/SPI Triggering and Serial Decode,”
starting on page 451
• Chapter 29, “I2S Triggering and Serial Decode,”
starting on page 471
• Chapter 30, “MIL-STD-1553/ARINC 429 Triggering
and Serial Decode,” starting on page 481
• Chapter 31, “SENT Triggering and Serial Decode,”
starting on page 497
• Chapter 32, “UART/RS232 Triggering and Serial
Decode,” starting on page 511
• Chapter 33, “USB 2.0 Triggering and Serial Decode,”
starting on page 521
Abbreviated instructions for pressing a series of keys and softkeys
NOTE
Instructions for pressing a series of keys are written in an abbreviated manner. Instructions for
pressing [Key1], then pressing Softkey2, then pressing Softkey3 are abbreviated as follows:
Press [Key1] > Softkey2 > Softkey3.
The keys may be a front panel [Key] or a Softkey. Softkeys are the six keys located directly
below the oscilloscope display.
| For reference information, see: | • Chapter 25, “Reference,” starting on page 399 |
|---|---|
| When using licensed serial bus
triggering and decode features, see: | • Chapter 26, “CAN/LIN Triggering and Serial Decode,”
starting on page 419
• Chapter 27, “FlexRay Triggering and Serial Decode,”
starting on page 441
• Chapter 28, “I2C/SPI Triggering and Serial Decode,”
starting on page 451
• Chapter 29, “I2S Triggering and Serial Decode,”
starting on page 471
• Chapter 30, “MIL-STD-1553/ARINC 429 Triggering
and Serial Decode,” starting on page 481
• Chapter 31, “SENT Triggering and Serial Decode,”
starting on page 497
• Chapter 32, “UART/RS232 Triggering and Serial
Decode,” starting on page 511
• Chapter 33, “USB 2.0 Triggering and Serial Decode,”
starting on page 521 |
| NOTE |
|---|
|  |

---
**[Page 7]**

8 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide

---
**[Page 8]**

Contents
InfiniiVision 6000X-Series Oscilloscopes—At a Glance / 3
In This Guide / 6
1 Getting Started
Inspect the Package Contents / 27
Tilt the Oscilloscope for Easy Viewing / 30
Power-On the Oscilloscope / 30
Connect Probes to the Oscilloscope / 31
Maximum input voltage at analog inputs / 31
Do not float the oscilloscope chassis / 32
Input a Waveform / 32
Recall the Default Oscilloscope Setup / 32
Use Autoscale / 33
Compensate Passive Probes / 35
Learn the Front Panel Controls and Connectors / 36
Front Panel Overlays for Different Languages / 43
Learn the Touchscreen Controls / 45
Draw Rectangles for Waveform Zoom or Zone Trigger Set
Up / 46
Pinch, Flick, or Drag to Scale, Position, and Change Offset / 47
Select Sidebar Information or Controls / 49
Undock Sidebar Dialogs by Dragging / 50
Select Dialog Menus and Close Dialogs / 51
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 9
|  |  |  |
|---|---|---|
|  |  |  |
|---|---|---|

---
**[Page 9]**

Drag Cursors / 51
Touch Softkeys and Menus On the Screen / 51
Enter Names Using Alpha-Numeric Keypad Dialogs / 52
Change Waveform Offsets By Dragging Ground Reference
Icons / 53
Access Controls and Menus Using the Spark Icon / 54
Turn Channels On/Off and Open Scale/Offset Dialogs / 56
Access the Horizontal Menu and Open the Scale/Delay
Dialog / 56
Access the Trigger Menu, Change the Trigger Mode, and Open the
Trigger Level Dialog / 57
Use a USB Mouse and/or Keyboard for Touchscreen
Controls / 58
Learn the Voice Controls / 58
Learn the Rear Panel Connectors / 59
Learn the Oscilloscope Display / 60
Access the Built-In Quick Help / 62
2 Horizontal Controls
To adjust the horizontal (time/div) scale / 66
To adjust the horizontal delay (position) / 67
Panning and Zooming Single or Stopped Acquisitions / 68
To change the horizontal time mode (Normal, XY, or Roll) / 69
XY Time Mode / 70
To display the zoomed time base / 73
To change the horizontal scale knob's coarse/fine adjustment
setting / 74
To position the time reference (left, center, right) / 75
Searching for Events / 75
To set up searches / 76
10 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 10]**

To copy search setups / 76
Navigating the Time Base / 77
To navigate time / 77
To navigate search events / 78
To navigate segments / 78
3 Vertical Controls
To turn waveforms on or off (channel or math) / 82
To adjust the vertical scale / 83
To adjust the vertical position / 83
To specify channel coupling / 84
To specify channel input impedance / 85
To specify bandwidth limiting / 85
To change the vertical scale knob's coarse/fine adjustment
setting / 86
To invert a waveform / 87
Setting Analog Channel Probe Options / 87
To specify the channel units / 88
To specify the probe attenuation / 88
To specify the probe skew / 89
To calibrate a probe / 89
4 Math Waveforms
To display math waveforms / 91
To adjust the math waveform scale and offset / 93
Units for Math Waveforms / 93
Math Operators / 94
Add or Subtract / 94
Multiply or Divide / 95
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 11

---
**[Page 11]**

Math Transforms / 96
Differentiate / 97
Integrate / 98
FFT Spectrum / 101
Square Root / 109
Ax + B / 109
Square / 110
Absolute Value / 111
Common Logarithm / 111
Natural Logarithm / 112
Exponential / 112
Base 10 Exponential / 113
Math Filters / 113
High Pass and Low Pass Filter / 114
Averaged Value / 115
Smoothing / 115
Envelope / 116
Math Visualizations / 116
Magnify / 116
Max/Min Hold / 117
Measurement Trend / 118
Chart Logic Bus Timing / 119
Chart Logic Bus State / 120
Clock Recovery / 122
The Measurement Record and Waveform Math / 123
5 Reference Waveforms
To save a waveform to a reference waveform location / 127
To display a reference waveform / 128
To scale and position reference waveforms / 129
To adjust reference waveform skew / 130
12 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 12]**

To display reference waveform information / 130
To save/recall reference waveform files to/from a USB storage
device / 130
6 Digital Channels
To connect the digital probes to the device under test / 131
Probe cable for digital channels / 132
Acquiring waveforms using the digital channels / 135
To display digital channels using Autoscale / 135
Interpreting the digital waveform display / 136
To change the displayed size of the digital channels / 137
To switch a single channel on or off / 138
To switch all digital channels on or off / 138
To switch groups of channels on or off / 138
To change the logic threshold for digital channels / 139
To reposition a digital channel / 139
To display digital channels as a bus / 140
Digital channel signal fidelity: Probe impedance and
grounding / 143
Input Impedance / 144
Probe Grounding / 146
Best Probing Practices / 148
7 Serial Decode
Serial Decode Options / 149
Lister / 151
Searching Lister Data / 153
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 13
|  |  |  |
|---|---|---|

---
**[Page 13]**

8 Display Settings
To adjust waveform intensity / 155
To set or clear persistence / 157
To clear the display / 159
To select the grid type / 159
To adjust the grid intensity / 159
To add an annotation / 160
To display waveforms as vectors or dots / 162
To disable/enable antialiasing / 163
To freeze the display / 164
9 Labels
To turn the label display on or off / 165
To assign a predefined label to a channel / 166
To define a new label / 167
To load a list of labels from a text file you create / 168
To reset the label library to the factory default / 169
10 Triggers
Adjusting the Trigger Level / 172
Forcing a Trigger / 173
Edge Trigger / 174
Edge then Edge Trigger / 176
Pulse Width Trigger / 178
Pattern Trigger / 181
Hex Bus Pattern Trigger / 183
14 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 14]**

OR Trigger / 184
Rise/Fall Time Trigger / 185
Nth Edge Burst Trigger / 187
Runt Trigger / 188
Setup and Hold Trigger / 191
Video Trigger / 192
To set up Generic video triggers / 197
To trigger on a specific line of video / 198
To trigger on all sync pulses / 199
To trigger on a specific field of the video signal / 200
To trigger on all fields of the video signal / 201
To trigger on odd or even fields / 202
Serial Trigger / 205
Zone Qualified Trigger / 206
11 Trigger Mode/Coupling
To select the Auto or Normal trigger mode / 210
To select the trigger coupling / 211
To enable or disable trigger noise rejection / 213
To enable or disable trigger HF Reject / 213
To set the trigger holdoff / 214
External Trigger Input / 214
Maximum voltage at oscilloscope external trigger input / 215
12 Acquisition Control
Running, Stopping, and Making Single Acquisitions (Run
Control) / 217
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 15
|  |  |  |
|---|---|---|

---
**[Page 15]**

Overview of Sampling / 218
Sampling Theory / 219
Aliasing / 219
Oscilloscope Bandwidth and Sample Rate / 219
Oscilloscope Rise Time / 221
Oscilloscope Bandwidth Required / 222
Memory Depth and Sample Rate / 223
Selecting the Acquisition Mode / 223
Normal Acquisition Mode / 224
Peak Detect Acquisition Mode / 224
Averaging Acquisition Mode / 227
High Resolution Acquisition Mode / 229
Data Acquisition (Sampling) Mode / 230
Realtime Sampling and Oscilloscope Bandwidth / 231
Acquiring to Segmented Memory / 232
Navigating Segments / 233
Measurements, Statistics, and Infinite Persistence with
Segmented Memory / 233
Segmented Memory Re-Arm Time / 234
Saving Data from Segmented Memory / 234
13 Cursors
To make cursor measurements / 236
Cursor Examples / 239
14 Measurements
To make automatic measurements / 246
Measurements Summary / 248
Snapshot All / 251
Voltage Measurements / 252
16 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 16]**

Peak-Peak / 253
Maximum / 253
Minimum / 253
Amplitude / 253
Top / 254
Base / 255
Overshoot / 255
Preshoot / 256
Average / 257
DC RMS / 257
AC RMS / 258
Ratio / 259
Time Measurements / 259
Period / 260
Frequency / 261
Counter / 262
+ Width / 263
– Width / 263
Burst Width / 263
Duty Cycle / 263
Bit Rate / 264
Rise Time / 264
Fall Time / 264
Delay / 264
Phase / 265
X at Min Y / 267
X at Max Y / 267
Count Measurements / 268
Positive Pulse Count / 268
Negative Pulse Count / 268
Rising Edge Count / 269
Falling Edges Count / 269
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 17

---
**[Page 17]**

Mixed Measurements / 269
Area / 269
Measurement Thresholds / 270
Measurement Window / 272
Measurement Statistics / 272
Precision Measurements and Math / 275
15 Histogram
Waveform Histogram Set Up / 278
Defining the Histogram Limits Window / 280
Measurement Histogram Set Up / 282
Histogram Data Graph / 283
Histogram Data Statistics / 284
16 Color Grade Waveform
Enabling a Color Grade Waveform / 288
Color Grade Themes / 290
17 Jitter and Real-Time Eye Analysis
Setting Up Jitter Analysis / 292
Jitter Measurements / 295
Data TIE / 295
Clock TIE / 296
N-Period / 296
Period-Period / 297
+Width to +Width / 298
-Width to -Width / 298
Real-Time Eye Analysis / 299
18 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 18]**

18 Mask Testing
To create a mask from a "golden" waveform (Automask) / 303
Mask Test Setup Options / 305
Mask Statistics / 308
To manually modify a mask file / 309
Building a Mask File / 312
How is mask testing done? / 315
19 Digital Voltmeter and Counter
Digital Voltmeter / 318
Counter / 320
20 Waveform Generator
To select generated waveform types and settings / 323
To edit arbitrary waveforms / 327
Creating New Arbitrary Waveforms / 328
Editing Existing Arbitrary Waveforms / 329
Capturing Other Waveforms to the Arbitrary Waveform / 333
To output the waveform generator sync pulse / 334
To specify the expected output load / 334
To use waveform generator logic presets / 335
To add noise to the waveform generator output / 335
To add modulation to the waveform generator output / 336
To set up Amplitude Modulation (AM) / 337
To set up Frequency Modulation (FM) / 338
To set up Frequency-Shift Keying Modulation (FSK) / 340
To restore waveform generator defaults / 341
To set up dual channel tracking / 341
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 19

---
**[Page 19]**

21 Save/Email/Recall (Setups, Screens, Data)
Saving Setups, Screen Images, or Data / 343
To save setup files / 345
To save BMP or PNG image files / 346
To save CSV, ASCII XY, or BIN data files / 346
Length Control / 348
To save Lister data files / 349
To save reference waveform files to a USB storage device / 350
To save masks / 350
To save arbitrary waveforms / 351
To navigate storage locations / 351
To enter file names / 351
Emailing Setups, Screen Images, or Data / 352
Recalling Setups, Masks, or Data / 353
To recall setup files / 354
To recall mask files / 354
To recall reference waveform files from a USB storage
device / 354
To recall arbitrary waveforms / 355
Recalling Default Setups / 355
Performing a Secure Erase / 356
22 Print (Screens)
To print the oscilloscope's display / 357
To set up network printer connections / 359
To specify the print options / 360
To specify the palette option / 361
23 Utility Settings
I/O Interface Settings / 363
20 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 20]**

Setting up the Oscilloscope's LAN Connection / 364
To establish a LAN connection / 365
Stand-alone (Point-to-Point) Connection to a PC / 366
File Explorer / 366
Setting Oscilloscope Preferences / 369
To choose "expand about" center or ground / 369
To disable/enable transparent backgrounds / 370
To set voice recognition and speaker options / 370
To set up the screen saver / 371
To set Autoscale preferences / 372
Jitter-Free Trigger / 373
Setting the Oscilloscope's Clock / 373
Setting the Rear Panel TRIG OUT Source / 374
Setting the Reference Signal Mode / 375
To supply a sample clock to the oscilloscope / 375
Maximum input voltage at 10 MHz REF connector / 375
To synchronize the timebase of two or more instruments / 376
Enabling Remote Command Logging / 377
Performing Service Tasks / 378
To perform user calibration / 378
To perform hardware self test / 379
To perform front panel self test / 379
To display oscilloscope information / 380
To display the user calibration status / 380
To clean the oscilloscope / 380
To check warranty and extended services status / 380
To contact Keysight / 381
To return the instrument / 381
Configuring the [Quick Action] Key / 381
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 21
|  |  |  |
|---|---|---|

---
**[Page 21]**

24 Web Interface
Accessing the Web Interface / 384
Browser Web Control / 385
Full Scope Remote Front Panel / 386
Screen Only Remote Front Panel / 387
Tablet Remote Front Panel / 388
Remote Programming via the Web Interface / 389
Remote Programming with Keysight IO Libraries / 390
Save/Recall / 391
Saving Files via the Web Interface / 391
Recalling Files via the Web Interface / 392
Get Image / 393
Identification Function / 394
Instrument Utilities / 394
Setting a Password / 397
25 Reference
Specifications and Characteristics / 399
Measurement Category / 399
Oscilloscope Measurement Category / 400
Measurement Category Definitions / 400
Transient Withstand Capability / 400
Maximum input voltage at analog inputs / 400
Maximum input voltage at digital channels / 401
Environmental Conditions / 401
Probes and Accessories / 401
Passive Probes / 402
22 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
|  |  |  |
|---|---|---|
|  |  |  |
|---|---|---|

---
**[Page 22]**

Single-Ended Active Probes / 403
Differential Probes / 404
Current Probes / 405
Accessories Available / 405
Loading Licenses and Displaying License Information / 406
Licensed Options Available / 407
Other Options Available / 408
Upgrading to an MSO / 409
Software and Firmware Updates / 409
Binary Data (.bin) Format / 409
Binary Data in MATLAB / 410
Binary Header Format / 410
Example Program for Reading Binary Data / 413
Examples of Binary Files / 413
CSV and ASCII XY files / 416
CSV and ASCII XY file structure / 417
Minimum and Maximum Values in CSV Files / 417
Acknowledgements / 418
26 CAN/LIN Triggering and Serial Decode
Setup for CAN/CAN FD Signals / 419
Loading and Displaying CAN Symbolic Data / 422
CAN/CAN FD Triggering / 423
CAN/CAN FD Serial Decode / 426
Interpreting CAN/CAN FD Decode / 427
CAN Totalizer / 428
Interpreting CAN Lister Data / 430
Searching for CAN Data in the Lister / 431
Setup for LIN Signals / 432
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 23

---
**[Page 23]**

Loading and Displaying LIN Symbolic Data / 433
LIN Triggering / 434
LIN Serial Decode / 436
Interpreting LIN Decode / 438
Interpreting LIN Lister Data / 439
Searching for LIN Data in the Lister / 440
27 FlexRay Triggering and Serial Decode
Setup for FlexRay Signals / 441
FlexRay Triggering / 442
Triggering on FlexRay Frames / 443
Triggering on FlexRay Errors / 444
Triggering on FlexRay Events / 444
FlexRay Serial Decode / 445
Interpreting FlexRay Decode / 446
FlexRay Totalizer / 447
Interpreting FlexRay Lister Data / 448
Searching for FlexRay Data in the Lister / 449
28 I2C/SPI Triggering and Serial Decode
Setup for I2C Signals / 451
I2C Triggering / 452
I2C Serial Decode / 456
Interpreting I2C Decode / 457
Interpreting I2C Lister Data / 459
Searching for I2C Data in the Lister / 459
Setup for SPI Signals / 460
SPI Triggering / 464
SPI Serial Decode / 466
24 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 24]**

Interpreting SPI Decode / 467
Interpreting SPI Lister Data / 468
Searching for SPI Data in the Lister / 469
29 I2S Triggering and Serial Decode
Setup for I2S Signals / 471
I2S Triggering / 474
I2S Serial Decode / 477
Interpreting I2S Decode / 478
Interpreting I2S Lister Data / 479
Searching for I2S Data in the Lister / 480
30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
Setup for MIL-STD-1553 Signals / 481
MIL-STD-1553 Triggering / 483
MIL-STD-1553 Serial Decode / 484
Interpreting MIL-STD-1553 Decode / 485
Interpreting MIL-STD-1553 Lister Data / 486
Searching for MIL-STD-1553 Data in the Lister / 487
Setup for ARINC429 Signals / 488
ARINC429 Triggering / 489
ARINC429 Serial Decode / 491
Interpreting ARINC429 Decode / 493
ARINC429 Totalizer / 494
Interpreting ARINC429 Lister Data / 495
Searching for ARINC429 Data in the Lister / 496
31 SENT Triggering and Serial Decode
Setup for SENT Signals / 497
SENT Triggering / 502
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 25

---
**[Page 25]**

SENT Serial Decode / 504
Interpreting SENT Decode / 505
Interpreting SENT Lister Data / 507
Searching for SENT Data in the Lister / 509
32 UART/RS232 Triggering and Serial Decode
Setup for UART/RS232 Signals / 511
UART/RS232 Triggering / 513
UART/RS232 Serial Decode / 515
Interpreting UART/RS232 Decode / 516
UART/RS232 Totalizer / 517
Interpreting UART/RS232 Lister Data / 518
Searching for UART/RS232 Data in the Lister / 518
33 USB 2.0 Triggering and Serial Decode
Setup for USB 2.0 Signals / 521
USB 2.0 Triggering / 523
USB 2.0 Serial Decode / 525
Interpreting USB 2.0 Decode / 526
Interpreting USB 2.0 Lister Data / 528
Searching for USB 2.0 Data in the Lister / 529
Index
26 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 26]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
27
1 Getting Started
Inspect the Package Contents / 27
Tilt the Oscilloscope for Easy Viewing / 30
Power-On the Oscilloscope / 30
Connect Probes to the Oscilloscope / 31
Input a Waveform / 32
Recall the Default Oscilloscope Setup / 32
Use Autoscale / 33
Compensate Passive Probes / 35
Learn the Front Panel Controls and Connectors / 36
Learn the Touchscreen Controls / 45
Learn the Voice Controls / 58
Learn the Rear Panel Connectors / 59
Learn the Oscilloscope Display / 60
Access the Built-In Quick Help / 62
This chapter describes the steps you take when using the oscilloscope for the first
time.
Inspect the Package Contents
• Inspect the shipping container for damage.
If your shipping container appears to be damaged, keep the shipping container
or cushioning material until you have inspected the contents of the shipment
for completeness and have checked the oscilloscope mechanically and
electrically.

---
**[Page 27]**

1 Getting Started
28 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Verify that you received the following items and any optional accessories you
may have ordered:
• InfiniiVision 6000X-Series oscilloscope.
• Power cord (country of origin determines specific type).
• Oscilloscope probes:
• Two probes for 2-channel models.
• Four probes for 4-channel models.
• Digital probe kit (MSO models only).
• Documentation CD-ROM.

---
**[Page 28]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 29
InfiniiVision 6000 X-Series oscilloscope
N2894A probes
(Qty 2 or 4)
Documentation CD
Power cord
(Based on country
of origin)
N2756-60001
Digital Probe Kit
(MSO models only)
See Also • “Accessories Available"on page405
| InfiniiVision 6000 X-Series oscilloscope
N2894A probes
(Qty 2 or 4)
Documentation CD
Power cord
(Based on country
of origin)
N2756-60001
Digital Probe Kit
(MSO models only) |
|---|
|  |
|  |  |  |
|---|---|---|

---
**[Page 29]**

1 Getting Started
30 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Tilt the Oscilloscope for Easy Viewing
There are tabs under the oscilloscope's front feet that can be flipped out to tilt the
oscilloscope.
Power-On the Oscilloscope
Power Line voltage, frequency, and power:
Requirements
• 100-120 Vac, 50/60/400Hz
• 100-240Vac, 50/60Hz
• 200W max
Ventilation The air intake and exhaust areas must be free from obstructions. Unrestricted air
Requirements flow is required for proper cooling. Always ensure that the air intake and exhaust
areas are free from obstructions.
The fan draws air in from the left side and bottom of the oscilloscope and pushes it
out behind the oscilloscope.

---
**[Page 30]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 31
When using the oscilloscope in a bench-top setting, provide at least 2" clearance
at the sides and 4" (100mm) clearance above and behind the oscilloscope for
proper cooling.
To power-on the 1 Connect the power cord to the rear of the oscilloscope, then to a suitable AC
oscilloscope voltage source. Route the power cord so the oscilloscope's feet and legs do not
pinch the cord.
2 The oscilloscope automatically adjusts for input line voltages in the range 100
to 240 VAC. The line cord provided is matched to the country of origin.
Always use a grounded power cord. Do not defeat the power cord ground.
WARNING
3 Press the power switch.
The power switch is located on the lower left corner of the front panel. The
oscilloscope will perform a self-test and will be operational in a few seconds.
Connect Probes to the Oscilloscope
1 Connect the oscilloscope probe to an oscilloscope channel BNC connector.
2 Connect the probe's retractable hook tip to the point of interest on the circuit or
device under test. Be sure to connect the probe ground lead to a ground point
on the circuit.
Maximum input voltage at analog inputs
CAUTION
300Vrms, 400Vpk; transient overvoltage 1.6kVpk
50Ω input: 5Vrms Input protection is enabled in 50Ω mode and the 50Ω load will
disconnect if greater than 5Vrms is detected. However the inputs could still be damaged,
depending on the time constant of the signal. The 50Ω input protection only functions
when the oscilloscope is powered on.
| WARNING |
|---|
|  |
| CAUTION |
|---|
|  |

---
**[Page 31]**

1 Getting Started
32 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Do not float the oscilloscope chassis
CAUTION
Defeating the ground connection and "floating" the oscilloscope chassis will probably
result in inaccurate measurements and may also cause equipment damage. The probe
ground lead is connected to the oscilloscope chassis and the ground wire in the power
cord. If you need to measure between two live points, use a differential probe with
sufficient dynamic range.
Do not negate the protective action of the ground connection to the oscilloscope. The
WARNING
oscilloscope must remain grounded through its power cord. Defeating the ground
creates an electric shock hazard.
Input a Waveform
The first signal to input to the oscilloscope is the Demo2, Probe Comp signal. This
signal is used for compensating probes.
1 Connect an oscilloscope probe from channel 1 to the Demo 2 (Probe Comp)
terminal on the front panel.
2 Connect the probe's ground lead to the ground terminal (next to the Demo 2
terminal).
Recall the Default Oscilloscope Setup
To recall the default oscilloscope setup:
1 Press [Default Setup].
The default setup restores the oscilloscope's default settings. This places the
oscilloscope in a known operating condition. The major default settings are:
| CAUTION |
|---|
|  |
| WARNING |
|---|
|  |

---
**[Page 32]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 33
Table 2 Default Configuration Settings
Horizontal Normal mode, 100µs/div scale, 0s delay, center time reference.
Vertical (Analog) Channel 1 on, 5V/div scale, DC coupling, 0V position, 1M Ω impedance.
Trigger Edge trigger, Auto trigger mode, 0V level, channel 1 source, DC coupling, rising
edge slope, 40ns holdoff time.
Display Persistence off, 20% grid intensity, 50% waveform intensity.
Other Acquire mode normal, [Run/Stop] to Run, cursors and measurements off.
Labels All custom labels that you have created in the Label Library are preserved (not
erased), but all channel labels will be set to their original names.
In the Save/Recall Menu, there are also options for restoring the complete factory
settings (see “Recalling Default Setups"on page355) or performing a secure
erase (see “Performing a Secure Erase"on page356).
Use Autoscale
Use [Auto Scale] to automatically configure the oscilloscope to best display the
input signals.
1 Press [Auto Scale].
You should see a waveform on the oscilloscope's display similar to this:
| Horizontal | Normal mode, 100µs/div scale, 0s delay, center time reference. |
|---|---|
| Vertical (Analog) | Ω
Channel 1 on, 5V/div scale, DC coupling, 0V position, 1M impedance. |
| Trigger | Edge trigger, Auto trigger mode, 0V level, channel 1 source, DC coupling, rising
edge slope, 40ns holdoff time. |
| Display | Persistence off, 20% grid intensity, 50% waveform intensity. |
| Other | Acquire mode normal, [Run/Stop] to Run, cursors and measurements off. |
| Labels | All custom labels that you have created in the Label Library are preserved (not
erased), but all channel labels will be set to their original names. |

---
**[Page 33]**

1 Getting Started
34 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 If you want to return to the oscilloscope settings that existed before, press Undo
Autoscale.
3 If you want to enable "fast debug" autoscaling, change the channels
autoscaled, or preserve the acquisition mode during autoscale, press Fast
Debug, Channels, or Acq Mode.
These are the same softkeys that appear in the Autoscale Preferences Menu.
See “To set Autoscale preferences"on page372.
If you see the waveform, but the square wave is not shaped correctly as shown
above, perform the procedure “Compensate Passive Probes"on page35.
If you do not see the waveform, make sure the probe is connected securely to the
front panel channel input BNC and to the left side, Demo2, Probe Comp terminal.
How Autoscale Auto Scale analyzes any waveforms present at each channel and at the external
Works trigger input. This includes the digital channels, if connected.
|  |  |
|---|---|

---
**[Page 34]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 35
Auto Scale finds, turns on, and scales any channel with a repetitive waveform that
has a frequency of at least 25Hz, a duty cycle greater than 0.5%, and an
amplitude of at least 10mV peak-to-peak. Any channels where no signal is found
are turned off.
The trigger source is selected by looking for the first valid waveform starting with
external trigger, then continuing with the lowest number analog channel up to the
highest number analog channel, and finally (if digital probes are connected) the
highest number digital channel.
During Autoscale, the delay is set to 0.0 seconds, the horizontal time/div (sweep
speed) setting is a function of the input signal (about 2 periods of the triggered
signal on the screen), and the triggering mode is set to Edge.
Compensate Passive Probes
Each oscilloscope passive probe must be compensated to match the input
characteristics of the oscilloscope channel to which it is connected. A poorly
compensated probe can introduce significant measurement errors.
1 Input the Probe Comp signal (see “Input a Waveform"on page32).
2 Press [Default Setup] to recall the default oscilloscope setup (see “Recall the
Default Oscilloscope Setup"on page32).
3 Press [Auto Scale] to automatically configure the oscilloscope for the Probe
Comp signal (see “Use Autoscale"on page33).
4 Press the channel key to which the probe is connected ([1], [2], etc.).
5 In the Channel Menu, press Probe.
6 In the Channel Probe Menu, press Probe Check; then, follow the instructions
on-screen.
If necessary, use a nonmetallic tool (supplied with the probe) to adjust the
trimmer capacitor on the probe for the flattest pulse possible.
On N2894A probes, the trimmer capacitor is located on the probe BNC
connector.

---
**[Page 35]**

1 Getting Started
36 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Perfectly compensated
Over compensated
Under compensated
7 Connect probes to all other oscilloscope channels (channel 2 of a 2-channel
oscilloscope, or channels 2, 3, and 4 of a 4-channel oscilloscope).
8 Repeat the procedure for each channel.
Learn the Front Panel Controls and Connectors
On the front panel, key refers to any key (button) you can press.
Softkey specifically refers to the six keys that are directly below the display. The
legend for these keys is directly above them, on the display. Their functions
change as you navigate through the oscilloscope's menus.
For the following figure, refer to the numbered descriptions in the table that
follows.
| Perfectly compensated
Over compensated
Under compensated | Perfectly compensated
Over compensated
Under compensated |  |
|---|---|---|

---
**[Page 36]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 37
5. Waveform keys 6. Trigger controls 7. Horizontal controls 8. Run Control keys
9. [Default Setup] key
10. [Auto Scale] key
11. Additional
4. Entry knob
waveform controls
3. [Intensity] key
12. Measure controls
13. File keys
14. Tools keys
2. Softkeys 15. [Help] key
1. Power switch 16. Vertical controls
21. Waveform 20. EXT TRIG IN 19. USB 18. Demo 2, Ground, 17. Analog
generator connector Host and Demo 1 channel
outputs ports terminals inputs
1. Power switch Press once to switch power on; press again to switch power off. See
“Power-On the Oscilloscope"on page30.
2. Softkeys The functions of these keys change based upon the menus shown on the
display directly above the keys.
The Back Back/Up key moves up in the softkey menu hierarchy. At the top
of the hierarchy, the Back Back/Up key turns the menus off, and
oscilloscope information is shown instead.
3. [Intensity] key Press the key to illuminate it. When illuminated, turn the Entry knob to
adjust waveform intensity.
You can vary the intensity control to bring out signal detail, much like an
analog oscilloscope.
Digital channel waveform intensity is not adjustable.
More details about using the Intensity control to view signal detail are on
“To adjust waveform intensity"on page155.
| 5. Waveform keys 6. Trigger controls 7. Horizontal controls 8. Run Control keys
9. [Default Setup] key
10. [Auto Scale] key
11. Additional
4. Entry knob
waveform controls
3. [Intensity] key
12. Measure controls
13. File keys
14. Tools keys
2. Softkeys 15. [Help] key
1. Power switch 16. Vertical controls
21. Waveform 20. EXT TRIG IN 19. USB 18. Demo 2, Ground, 17. Analog
generator connector Host and Demo 1 channel
outputs ports terminals inputs |
|---|
|  |
| 1. | Power switch | Press once to switch power on; press again to switch power off. See
“Power-On the Oscilloscope"on page30. |
|---|---|---|
| 2. | Softkeys | The functions of these keys change based upon the menus shown on the
display directly above the keys.
The Back Back/Up key moves up in the softkey menu hierarchy. At the top
of the hierarchy, the Back Back/Up key turns the menus off, and
oscilloscope information is shown instead. |
| 3. | [Intensity] key | Press the key to illuminate it. When illuminated, turn the Entry knob to
adjust waveform intensity.
You can vary the intensity control to bring out signal detail, much like an
analog oscilloscope.
Digital channel waveform intensity is not adjustable.
More details about using the Intensity control to view signal detail are on
“To adjust waveform intensity"on page155. |

---
**[Page 37]**

1 Getting Started
38 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
4. Entry knob The Entry knob is used to select items from menus and to change values.
The function of the Entry knob changes based upon the current menu and
softkey selections.
Note that the curved arrow symbol above the entry knob illuminates
whenever the entry knob can be used to select a value. Also, note that
when the Entry knob symbol appears on a softkey, you can use the
Entry knob, to select values.
Often, rotating the Entry knob is enough to make a selection. Sometimes,
you can push the Entry knob to enable or disable a selection. Pushing the
Entry knob also makes popup menus disappear.
5. Waveform keys [Analyze] key — Press this key to access analysis features like:
• Trigger level setting.
• Measurement threshold setting.
• The DSOX6USBSQ USB 2.0 signal quality analysis application.
• Video trigger automatic set up and display.
• Color grade waveform display (see Chapter16, “Color Grade
Waveform,” starting on page 287).
• Counter (DVMCTR) (see “Counter"on page320).
• Digital voltmeter (DVMCTR) (see “Digital Voltmeter"on page318).
• Histogram of waveforms or measurements (see Chapter15,
“Histogram,” starting on page 277).
• Mask testing (see Chapter18, “Mask Testing,” starting on page 303).
• The DSOX6PWR power measurement and analysis application.
• Precision measurements and math functions (see “Precision
Measurements and Math"on page275).
• Real-time eye analysis (included with the DSOX6JITTER jitter analysis
application, see “Real-Time Eye Analysis"on page299).
The [Acquire] key lets you select Normal, Peak Detect, Averaging, or High
Resolution acquisition modes (see “Selecting the Acquisition
Mode"on page223) and use segmented memory (see “Acquiring to
Segmented Memory"on page232).
The [Jitter] key lets you set up jitter analysis (see Chapter17, “Jitter and
Real-Time Eye Analysis,” starting on page 291).
[Clear Display] key — Press this key to clear acquisition data from the
oscilloscope display.
The [Display] key lets you access the menu where you can enable
persistence (see “To set or clear persistence"on page157), clear the
display, and adjust the display grid (graticule) intensity (see “To adjust
the grid intensity"on page159).
| 4. | Entry knob | The Entry knob is used to select items from menus and to change values.
The function of the Entry knob changes based upon the current menu and
softkey selections.
Note that the curved arrow symbol above the entry knob illuminates
whenever the entry knob can be used to select a value. Also, note that
when the Entry knob symbol appears on a softkey, you can use the
Entry knob, to select values.
Often, rotating the Entry knob is enough to make a selection. Sometimes,
you can push the Entry knob to enable or disable a selection. Pushing the
Entry knob also makes popup menus disappear. |
|---|---|---|
| 5. | Waveform keys | [Analyze] key — Press this key to access analysis features like:
• Trigger level setting.
• Measurement threshold setting.
• The DSOX6USBSQ USB 2.0 signal quality analysis application.
• Video trigger automatic set up and display.
• Color grade waveform display (see Chapter16, “Color Grade
Waveform,” starting on page 287).
• Counter (DVMCTR) (see “Counter"on page320).
• Digital voltmeter (DVMCTR) (see “Digital Voltmeter"on page318).
• Histogram of waveforms or measurements (see Chapter15,
“Histogram,” starting on page 277).
• Mask testing (see Chapter18, “Mask Testing,” starting on page 303).
• The DSOX6PWR power measurement and analysis application.
• Precision measurements and math functions (see “Precision
Measurements and Math"on page275).
• Real-time eye analysis (included with the DSOX6JITTER jitter analysis
application, see “Real-Time Eye Analysis"on page299).
The [Acquire] key lets you select Normal, Peak Detect, Averaging, or High
Resolution acquisition modes (see “Selecting the Acquisition
Mode"on page223) and use segmented memory (see “Acquiring to
Segmented Memory"on page232).
The [Jitter] key lets you set up jitter analysis (see Chapter17, “Jitter and
Real-Time Eye Analysis,” starting on page 291).
[Clear Display] key — Press this key to clear acquisition data from the
oscilloscope display.
The [Display] key lets you access the menu where you can enable
persistence (see “To set or clear persistence"on page157), clear the
display, and adjust the display grid (graticule) intensity (see “To adjust
the grid intensity"on page159). |

---
**[Page 38]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 39
6. Trigger controls These controls determine how the oscilloscope triggers to capture data.
See Chapter10, “Triggers,” starting on page 171 and Chapter11,
“Trigger Mode/Coupling,” starting on page 209.
7. Horizontal The Horizontal controls consist of:
controls • Horizontal scale knob — Turn the knob in the Horizontal section that is
marked to adjust the time/div (sweep speed) setting. The
symbols under the knob indicate that this control has the effect of
spreading out or zooming in on the waveform using the horizontal scale.
• Horizontal position knob — Turn the knob marked to pan through
the waveform data horizontally. You can see the captured waveform
before the trigger (turn the knob clockwise) or after the trigger (turn the
knob counterclockwise). If you pan through the waveform when the
oscilloscope is stopped (not in Run mode) then you are looking at the
waveform data from the last acquisition taken.
• [Horiz] key — Press this key to open the Horizontal Menu where you can
select XY and Roll modes, enable or disable Zoom, enable or disable
horizontal time/division fine adjustment, and select the trigger time
reference point.
• Zoom key — Press the zoom key to split the oscilloscope
display into Normal and Zoom sections without opening the Horizontal
Menu.
• [Search] key — Lets you search for events in the acquired data.
• [Navigate] keys — Press these keys to navigate through captured data
via time, search events, or segmented memory acquisition. See
“Navigating the Time Base"on page77.
For more information see Chapter2, “Horizontal Controls,” starting on
page 65.
8. Run Control When the [Run/Stop] key is green, the oscilloscope is running, that is,
keys acquiring data when trigger conditions are met. To stop acquiring data,
press [Run/Stop].
When the [Run/Stop] key is red, data acquisition is stopped. To start
acquiring data, press [Run/Stop].
To capture and display a single acquisition (whether the oscilloscope is
running or stopped), press [Single]. The [Single] key is yellow until the
oscilloscope triggers.
For more information, see “Running, Stopping, and Making Single
Acquisitions (Run Control)"on page217.
9. [Default Setup] Press this key to restore the oscilloscope's default settings (details on
key “Recall the Default Oscilloscope Setup"on page32).
| 6. | Trigger controls | These controls determine how the oscilloscope triggers to capture data.
See Chapter10, “Triggers,” starting on page 171 and Chapter11,
“Trigger Mode/Coupling,” starting on page 209. |
|---|---|---|
| 7. | Horizontal
controls | The Horizontal controls consist of:
• Horizontal scale knob — Turn the knob in the Horizontal section that is
marked to adjust the time/div (sweep speed) setting. The
symbols under the knob indicate that this control has the effect of
spreading out or zooming in on the waveform using the horizontal scale.
• Horizontal position knob — Turn the knob marked to pan through
the waveform data horizontally. You can see the captured waveform
before the trigger (turn the knob clockwise) or after the trigger (turn the
knob counterclockwise). If you pan through the waveform when the
oscilloscope is stopped (not in Run mode) then you are looking at the
waveform data from the last acquisition taken.
• [Horiz] key — Press this key to open the Horizontal Menu where you can
select XY and Roll modes, enable or disable Zoom, enable or disable
horizontal time/division fine adjustment, and select the trigger time
reference point.
• Zoom key — Press the zoom key to split the oscilloscope
display into Normal and Zoom sections without opening the Horizontal
Menu.
• [Search] key — Lets you search for events in the acquired data.
• [Navigate] keys — Press these keys to navigate through captured data
via time, search events, or segmented memory acquisition. See
“Navigating the Time Base"on page77.
For more information see Chapter2, “Horizontal Controls,” starting on
page 65. |
| 8. | Run Control
keys | When the [Run/Stop] key is green, the oscilloscope is running, that is,
acquiring data when trigger conditions are met. To stop acquiring data,
press [Run/Stop].
When the [Run/Stop] key is red, data acquisition is stopped. To start
acquiring data, press [Run/Stop].
To capture and display a single acquisition (whether the oscilloscope is
running or stopped), press [Single]. The [Single] key is yellow until the
oscilloscope triggers.
For more information, see “Running, Stopping, and Making Single
Acquisitions (Run Control)"on page217. |
| 9. | [Default Setup]
key | Press this key to restore the oscilloscope's default settings (details on
“Recall the Default Oscilloscope Setup"on page32). |
|  |  |
|---|---|

---
**[Page 39]**

1 Getting Started
40 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
10. [Auto Scale] When you press the [Auto Scale] key, the oscilloscope will quickly
key determine which channels have activity, and it will turn these channels on
and scale them to display the input signals. See “Use Autoscale"on
page33.
11. Additional The additional waveform controls consist of:
waveform • [Math] key — provides access to math (add, subtract, etc.) waveform
controls functions. See Chapter4, “Math Waveforms,” starting on page 91.
• [Ref] key — provides access to reference waveform functions. Reference
waveforms are saved waveforms that can be displayed and compared
against other analog channel or math waveforms. Also, measurements
can be made on reference waveforms. See Chapter5, “Reference
Waveforms,” starting on page 127.
• [Digital] key — Press this key to turn the digital channels on or off (the
arrow to the left will illuminate).
When the arrow to the left of the [Digital] key is illuminated, the upper
multiplexed knob selects (and highlights in red) individual digital
channels, and the lower multiplexed knob positions the selected digital
channel.
If a trace is repositioned over an existing trace the indicator at the left
edge of the trace will change from Dnndesignation (where nn is a one
or two digit channel number from 0 to 15) to D*. The "*" indicates that
two or more channels are overlaid.
You can rotate the upper knob to select an overlaid channel, then rotate
the lower knob to position it just as you would any other channel.
For more information on digital channels see Chapter6, “Digital
Channels,” starting on page 131.
• [Serial] key — This key is used to enable serial decode. The multiplexed
scale and position knobs are not used with serial decode. For more
information on serial decode, see Chapter7, “Serial Decode,” starting
on page 149.
• Multiplexed scale knob — This scale knob is used with Math, Ref, or
Digital waveforms, whichever has the illuminated arrow to the left. For
math and reference waveforms, the scale knob acts like an analog
channel vertical scale knob.
• Multiplexed position knob — This position knob is used with Math, Ref,
or Digital waveforms, whichever has the illuminated arrow to the left.
For math and reference waveforms, the position knob acts like an
analog channel vertical position knob.
| 10. | [Auto Scale]
key | When you press the [Auto Scale] key, the oscilloscope will quickly
determine which channels have activity, and it will turn these channels on
and scale them to display the input signals. See “Use Autoscale"on
page33. |
|---|---|---|
| 11. | Additional
waveform
controls | The additional waveform controls consist of:
• [Math] key — provides access to math (add, subtract, etc.) waveform
functions. See Chapter4, “Math Waveforms,” starting on page 91.
• [Ref] key — provides access to reference waveform functions. Reference
waveforms are saved waveforms that can be displayed and compared
against other analog channel or math waveforms. Also, measurements
can be made on reference waveforms. See Chapter5, “Reference
Waveforms,” starting on page 127.
• [Digital] key — Press this key to turn the digital channels on or off (the
arrow to the left will illuminate).
When the arrow to the left of the [Digital] key is illuminated, the upper
multiplexed knob selects (and highlights in red) individual digital
channels, and the lower multiplexed knob positions the selected digital
channel.
If a trace is repositioned over an existing trace the indicator at the left
edge of the trace will change from Dnndesignation (where nn is a one
or two digit channel number from 0 to 15) to D*. The "*" indicates that
two or more channels are overlaid.
You can rotate the upper knob to select an overlaid channel, then rotate
the lower knob to position it just as you would any other channel.
For more information on digital channels see Chapter6, “Digital
Channels,” starting on page 131.
• [Serial] key — This key is used to enable serial decode. The multiplexed
scale and position knobs are not used with serial decode. For more
information on serial decode, see Chapter7, “Serial Decode,” starting
on page 149.
• Multiplexed scale knob — This scale knob is used with Math, Ref, or
Digital waveforms, whichever has the illuminated arrow to the left. For
math and reference waveforms, the scale knob acts like an analog
channel vertical scale knob.
• Multiplexed position knob — This position knob is used with Math, Ref,
or Digital waveforms, whichever has the illuminated arrow to the left.
For math and reference waveforms, the position knob acts like an
analog channel vertical position knob. |

---
**[Page 40]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 41
12. Measure The measure controls consist of:
controls • Cursors knob — Push this knob to select cursors from a popup menu.
Then, after the popup menu closes (either by timeout or by pushing the
knob again), rotate the knob to adjust the selected cursor position.
• [Cursors] key — Press this key to open a menu that lets you select the
cursors mode and source.
• [Meas] key — Press this key to access a set of predefined
measurements. See Chapter14, “Measurements,” starting on page
245.
13. File keys Press the [Save/Recall] key to save or recall a waveform or setup. See
Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on
page 343.
The [Print] key opens the Print Configuration Menu so you can print the
displayed waveforms. See Chapter22, “Print (Screens),” starting on page
357.
14. Tools keys The Tools keys consist of:
• [Utility] key — Press this key to access the Utility Menu, which lets you
configure the oscilloscope's I/O settings, use the file explorer, set
preferences, access the service menu, and choose other options. See
Chapter23, “Utility Settings,” starting on page 363.
• [Quick Action] key — Press this key to perform the selected quick
action: measure all snapshot, print, save, recall, freeze display, and
more. See “Configuring the [Quick Action] Key"on page381.
• [Wave Gen1], [Wave Gen2] keys — Press these keys to access
waveform generator functions. See Chapter20, “Waveform
Generator,” starting on page 323.
15. [Help] key Opens the Help Menu where you can display overview help topics and
select the Language. See also “Access the Built-In Quick Help"on
page62.
| 12. | Measure
controls | The measure controls consist of:
• Cursors knob — Push this knob to select cursors from a popup menu.
Then, after the popup menu closes (either by timeout or by pushing the
knob again), rotate the knob to adjust the selected cursor position.
• [Cursors] key — Press this key to open a menu that lets you select the
cursors mode and source.
• [Meas] key — Press this key to access a set of predefined
measurements. See Chapter14, “Measurements,” starting on page
245. |
|---|---|---|
| 13. | File keys | Press the [Save/Recall] key to save or recall a waveform or setup. See
Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on
page 343.
The [Print] key opens the Print Configuration Menu so you can print the
displayed waveforms. See Chapter22, “Print (Screens),” starting on page
357. |
| 14. | Tools keys | The Tools keys consist of:
• [Utility] key — Press this key to access the Utility Menu, which lets you
configure the oscilloscope's I/O settings, use the file explorer, set
preferences, access the service menu, and choose other options. See
Chapter23, “Utility Settings,” starting on page 363.
• [Quick Action] key — Press this key to perform the selected quick
action: measure all snapshot, print, save, recall, freeze display, and
more. See “Configuring the [Quick Action] Key"on page381.
• [Wave Gen1], [Wave Gen2] keys — Press these keys to access
waveform generator functions. See Chapter20, “Waveform
Generator,” starting on page 323. |
| 15. | [Help] key | Opens the Help Menu where you can display overview help topics and
select the Language. See also “Access the Built-In Quick Help"on
page62. |

---
**[Page 41]**

1 Getting Started
42 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
16. Vertical The Vertical controls consist of:
controls • Analog channel on/off keys — Use these keys to switch a channel on or
off, or to access a channel's menu in the softkeys. There is one channel
on/off key for each analog channel.
• Vertical scale knob — There are knobs marked for each
channel. Use these knobs to change the vertical sensitivity (gain) of
each analog channel.
• Vertical position knobs — Use these knobs to change a channel's
vertical position on the display. There is one Vertical Position control for
each analog channel.
• [Label] key — Press this key to access the Label Menu, which lets you
enter labels to identify each trace on the oscilloscope display. See
Chapter9, “Labels,” starting on page 165.
• [Touch] key — Press this key to disable/enable the touchscreen.
For more information, see Chapter3, “Vertical Controls,” starting on page
81.
17. Analog channel Attach oscilloscope probes or BNC cables to these BNC connectors.
inputs With the InfiniiVision 6000X-Series oscilloscopes, you can set the input
Ω Ω
impedance of the analog channels to either 50 or 1M . See “To
specify channel input impedance"on page85.
The InfiniiVision 6000X-Series oscilloscopes also provide the AutoProbe
interface. The AutoProbe interface uses a series of contacts directly below
the channel's BNC connector to transfer information between the
oscilloscope and the probe. When you connect a compatible probe to the
oscilloscope, the AutoProbe interface determines the type of probe and
sets the oscilloscope's parameters (units, offset, attenuation, coupling, and
impedance) accordingly.
18. Demo 2, • Demo 2 terminal — This terminal outputs the Probe Comp signal which
Ground, and helps you match a probe's input capacitance to the oscilloscope
Demo 1 channel to which it is connected. See “Compensate Passive
terminals Probes"on page35. With certain licensed features, the oscilloscope
can also output demo or training signals on this terminal.
• Ground terminal — Use the ground terminal for oscilloscope probes
connected to the Demo 1 or Demo 2 terminals.
• Demo 1 terminal — With certain licensed features, the oscilloscope can
output demo or training signals on this terminal.
| 16. | Vertical
controls | The Vertical controls consist of:
• Analog channel on/off keys — Use these keys to switch a channel on or
off, or to access a channel's menu in the softkeys. There is one channel
on/off key for each analog channel.
• Vertical scale knob — There are knobs marked for each
channel. Use these knobs to change the vertical sensitivity (gain) of
each analog channel.
• Vertical position knobs — Use these knobs to change a channel's
vertical position on the display. There is one Vertical Position control for
each analog channel.
• [Label] key — Press this key to access the Label Menu, which lets you
enter labels to identify each trace on the oscilloscope display. See
Chapter9, “Labels,” starting on page 165.
• [Touch] key — Press this key to disable/enable the touchscreen.
For more information, see Chapter3, “Vertical Controls,” starting on page
81. |
|---|---|---|
| 17. | Analog channel
inputs | Attach oscilloscope probes or BNC cables to these BNC connectors.
With the InfiniiVision 6000X-Series oscilloscopes, you can set the input
Ω Ω
impedance of the analog channels to either 50 or 1M . See “To
specify channel input impedance"on page85.
The InfiniiVision 6000X-Series oscilloscopes also provide the AutoProbe
interface. The AutoProbe interface uses a series of contacts directly below
the channel's BNC connector to transfer information between the
oscilloscope and the probe. When you connect a compatible probe to the
oscilloscope, the AutoProbe interface determines the type of probe and
sets the oscilloscope's parameters (units, offset, attenuation, coupling, and
impedance) accordingly. |
| 18. | Demo 2,
Ground, and
Demo 1
terminals | • Demo 2 terminal — This terminal outputs the Probe Comp signal which
helps you match a probe's input capacitance to the oscilloscope
channel to which it is connected. See “Compensate Passive
Probes"on page35. With certain licensed features, the oscilloscope
can also output demo or training signals on this terminal.
• Ground terminal — Use the ground terminal for oscilloscope probes
connected to the Demo 1 or Demo 2 terminals.
• Demo 1 terminal — With certain licensed features, the oscilloscope can
output demo or training signals on this terminal. |

---
**[Page 42]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 43
19. USB Host ports These ports are for connecting a USB mass storage device, printer, mouse,
or keyboard to the oscilloscope.
Connect a USB compliant mass storage device (flash drive, disk drive, etc.)
to save or recall oscilloscope setup files and reference waveforms or to
save data and screen images. See Chapter21, “Save/Email/Recall
(Setups, Screens, Data),” starting on page 343.
To print, connect a USB compliant printer. For more information about
printing see Chapter22, “Print (Screens),” starting on page 357.
You can also use the USB port to update the oscilloscope's system
software when updates are available.
You do not need to take special precautions before removing the USB mass
storage device from the oscilloscope (you do not need to "eject" it). Simply
unplug the USB mass storage device from the oscilloscope when the file
operation is complete.
CAUTION: Do not connect a host computer to the oscilloscope's USB
host port. Use the device port. A host computer sees the oscilloscope as a
device, so connect the host computer to the oscilloscope's device port (on
the rear panel). See “I/O Interface Settings"on page363.
There is a third USB host port on the back panel.
20. EXT TRIG IN External trigger input BNC connector. See “External Trigger Input"on
connector page214 for an explanation of this feature.
21. Waveform Built-in, license-enabled 2-channel waveform generator can output
generator arbitrary, sine, square, ramp, pulse, DC, noise, sine cardinal, exponential
outputs rise, exponential fall, cardiac, or Gaussian pulse waveforms on the
GenOut1 or GenOut2 BNC connectors. Modulated waveforms are
available on WaveGen1 except for arbitrary, pulse, DC, and noise
waveforms. Press the [Wave Gen1] or [Wave Gen2] keys to set up the
waveform generator. See Chapter20, “Waveform Generator,” starting on
page 323.
Front Panel Overlays for Different Languages
Front panel overlays, which have translations for the English front panel keys and
label text, are available in 10 languages. The appropriate overlay is included when
the localization option is chosen at time of purchase.
To install a front panel overlay:
1 Gently pull on the front panel knobs to remove them.
2 Insert the overlay's side tabs into the slots on the front panel.
| 19. | USB Host ports | These ports are for connecting a USB mass storage device, printer, mouse,
or keyboard to the oscilloscope.
Connect a USB compliant mass storage device (flash drive, disk drive, etc.)
to save or recall oscilloscope setup files and reference waveforms or to
save data and screen images. See Chapter21, “Save/Email/Recall
(Setups, Screens, Data),” starting on page 343.
To print, connect a USB compliant printer. For more information about
printing see Chapter22, “Print (Screens),” starting on page 357.
You can also use the USB port to update the oscilloscope's system
software when updates are available.
You do not need to take special precautions before removing the USB mass
storage device from the oscilloscope (you do not need to "eject" it). Simply
unplug the USB mass storage device from the oscilloscope when the file
operation is complete.
CAUTION: Do not connect a host computer to the oscilloscope's USB
host port. Use the device port. A host computer sees the oscilloscope as a
device, so connect the host computer to the oscilloscope's device port (on
the rear panel). See “I/O Interface Settings"on page363.
There is a third USB host port on the back panel. |
|---|---|---|
| 20. | EXT TRIG IN
connector | External trigger input BNC connector. See “External Trigger Input"on
page214 for an explanation of this feature. |
| 21. | Waveform
generator
outputs | Built-in, license-enabled 2-channel waveform generator can output
arbitrary, sine, square, ramp, pulse, DC, noise, sine cardinal, exponential
rise, exponential fall, cardiac, or Gaussian pulse waveforms on the
GenOut1 or GenOut2 BNC connectors. Modulated waveforms are
available on WaveGen1 except for arbitrary, pulse, DC, and noise
waveforms. Press the [Wave Gen1] or [Wave Gen2] keys to set up the
waveform generator. See Chapter20, “Waveform Generator,” starting on
page 323. |

---
**[Page 43]**

1 Getting Started
44 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Reinstall the front panel knobs.
Front panel overlays may be ordered from www.parts.keysight.com using the
following part numbers:
|  |  |
|---|---|

---
**[Page 44]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 45
Language 2 Channel Overlay 4 Channel Overlay
French 54608-94314 54609-94314
German 54608-94313 54609-94313
Italian 54608-94315 54609-94315
Japanese 54608-94317 54609-94317
Korean 54608-94312 54609-94312
Portuguese 54608-94318 54609-94318
Russian 54608-94319 54609-94319
Simplified Chinese 54608-94310 54609-94310
Spanish 54608-94316 54609-94316
Traditional Chinese 54608-94311 54609-94311
Learn the Touchscreen Controls
When the [Touch] key is lit, you can control the oscilloscope by touching different
areas of the screen. You can:
• “Draw Rectangles for Waveform Zoom or Zone Trigger Set Up"on page46
• “Pinch, Flick, or Drag to Scale, Position, and Change Offset"on page47
• “Select Sidebar Information or Controls"on page49
• “Undock Sidebar Dialogs by Dragging"on page50
• “Select Dialog Menus and Close Dialogs"on page51
• “Drag Cursors"on page51
• “Touch Softkeys and Menus On the Screen"on page51
• “Enter Names Using Alpha-Numeric Keypad Dialogs"on page52
• “Change Waveform Offsets By Dragging Ground Reference Icons"on page53
• “Access Controls and Menus Using the Spark Icon"on page54
• “Turn Channels On/Off and Open Scale/Offset Dialogs"on page56
• “Access the Horizontal Menu and Open the Scale/Delay Dialog"on page56
| Language | 2 Channel Overlay | 4 Channel Overlay |
|---|---|---|
| French | 54608-94314 | 54609-94314 |
| German | 54608-94313 | 54609-94313 |
| Italian | 54608-94315 | 54609-94315 |
| Japanese | 54608-94317 | 54609-94317 |
| Korean | 54608-94312 | 54609-94312 |
| Portuguese | 54608-94318 | 54609-94318 |
| Russian | 54608-94319 | 54609-94319 |
| Simplified Chinese | 54608-94310 | 54609-94310 |
| Spanish | 54608-94316 | 54609-94316 |
| Traditional Chinese | 54608-94311 | 54609-94311 |

---
**[Page 45]**

1 Getting Started
46 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• “Access the Trigger Menu, Change the Trigger Mode, and Open the Trigger
Level Dialog"on page57
• “Use a USB Mouse and/or Keyboard for Touchscreen Controls"on page58
Draw Rectangles for Waveform Zoom or Zone Trigger Set Up
1 Touch the upper-right corner to select the rectangle draw mode.
2 Drag your finger across the screen to draw a rectangle.
3 Take your finger off the screen.
4 Touch the desired option from the popup menu.
|  |  |
|---|---|

---
**[Page 46]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 47
Pinch, Flick, or Drag to Scale, Position, and Change Offset
1 Touch the upper-right corner to select the waveform drag mode.
2 When the waveform drag mode is selected, you can use these touch gestures:
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 47]**

1 Getting Started
48 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Pinch — used to zoom in on a waveform of interest. A horizontal pinch
adjusts the oscilloscope's time/div and delay settings at once — for "off
center zooming", this is more efficient than using knobs. A vertical pinch
adjusts a waveform's V/div and offset settings at once.
To select waveforms, tap them. The waveform closest horizontally to the tap
location is selected. The selected waveform is indicated by the ground
marker with the filled background (channel 1 in the following example).
|  |  |
|---|---|

---
**[Page 48]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 49
• Flick — allows very fast browsing of waveforms. It is similar to browsing on
tablets and smartphones. It is much easier to flick than to continually turn a
knob.
• Drag — drag your finger across the screen to change the horizontal delay.
Select Sidebar Information or Controls
1 Touch the blue menu icon in the sidebar.
2 In the popup menu, touch the type of information or controls you want to see in
the sidebar.
|  |  |
|---|---|

---
**[Page 49]**

1 Getting Started
50 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Undock Sidebar Dialogs by Dragging
Sidebar dialogs can be undocked and placed anywhere on the screen.
1 Drag the sidebar dialog title wherever you like.
This lets you view multiple types of information or controls at the same time.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 50]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 51
Select Dialog Menus and Close Dialogs
• Touch the blue menu icon in the dialog for options.
• Touch the red "X" icon to close a dialog.
Drag Cursors
When cursors are displayed, you can drag the name handles to position them.
Touch Softkeys and Menus On the Screen
• Touch onscreen softkey labels to select them.
This is the same as pressing the softkey keys.
|  |  |
|---|---|
|  |
|---|
|  |

---
**[Page 51]**

1 Getting Started
52 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• When softkeys provide menus, double-touch to select a menu item.
This may be an easier than selecting a menu item via the Entry knob.
Enter Names Using Alpha-Numeric Keypad Dialogs
Some softkeys open alpha-numeric dialogs that let you touch to enter names.
|  |  |
|---|---|

---
**[Page 52]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 53
Change Waveform Offsets By Dragging Ground Reference Icons
When the waveform drag mode is selected, you can drag waveforms up or down
to change the vertical offset.
You can always change waveform vertical offsets by dragging ground markers and
labels, even when in the rectangle draw mode.
|  |
|---|
|  |

---
**[Page 53]**

1 Getting Started
54 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Access Controls and Menus Using the Spark Icon
1 Touch the upper-left spark icon to open the main menu.
2 Touch left side controls to perform oscilloscope operations.
|  |
|---|
|  |
|  |  |
|---|---|

---
**[Page 54]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 55
3 Touch menu items and submenu items to access menus and additional
controls.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 55]**

1 Getting Started
56 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Turn Channels On/Off and Open Scale/Offset Dialogs
• Touch channel numbers to turn them on or off.
• When channels are on, touch the scale and offset values to access a dialog for
changing them.
Access the Horizontal Menu and Open the Scale/Delay Dialog
• Touch "H" to access the Horizontal Menu.
• Touch the horizontal scale and delay values to access a dialog for changing
them.
|  |  |
|---|---|
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 56]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 57
Access the Trigger Menu, Change the Trigger Mode, and Open the
Trigger Level Dialog
• Touch "T" to access the Trigger Menu.
• Touch the trigger level value(s) to access a dialog for changing the level(s).
• Touch "Auto" or "Trig'd" to quickly toggle the trigger mode.
|  |  |
|---|---|
|  |  |
|---|---|
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 57]**

1 Getting Started
58 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Use a USB Mouse and/or Keyboard for Touchscreen Controls
Connecting a USB mouse gives you a mouse pointer on the display. Mouse clicks
and drags behave the same as screen touches and finger drags.
If you connect a USB keyboard, you can use it to enter values in alpha-numeric
keypad dialogs.
Learn the Voice Controls
Voice control is a valuable feature when browsing signals in your device under test
and using your hands to hold down probes. The set of voice commands is limited
so they are easy to remember.
On the upper right corner of the display is an icon that describes the state of voice
recognition:
• means voice recognition is not running at all.
• means voice recognition is running but it is only listening for the wakeup
command.
• means voice recognition is listening for commands.
To enable voice recognition, tap the icon and (in the Audio Menu) press the Voice
Recognition softkey.
The initial screen shows the list of commands and includes a few brief
explanations. There is also a smaller help screen that simply lists the commands.
The best way to recall the list of voice commands is to say the command "Help".
Notes on Voice Most equipment noise will not bother recognition but other people speaking will.
Recognition Use a USB headset if other people are speaking nearby.
It is best to speak at a normal speed. Speaking slowly or with long pauses will
make recognition worse just like speaking too quickly.
The voice recognition uses Speaker Adaption. This is reset each time a different
person speaks, so it is best if only one person speaks to the oscilloscope.

---
**[Page 58]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 59
The recognition is best when using the accent of the selected language. See “To
select the language"on page63.
Learn the Rear Panel Connectors
For the following figure, refer to the numbered descriptions in the table that
follows.
3. TRIG OUT connector
6. Digital channel inputs 4. 10 MHz REF connector 5. Calibration protect switch
8. USB Host port
9. USB Device port
10. LAN port
7. VGA Video Out
2. Kensington lock hole 1. Power cord connector
1. Power cord Attach the power cord here.
connector
2. Kensington lock This is where you can attach a Kensington lock for securing the instrument.
hole
3. TRIG OUT Trigger output BNC connector. See “Setting the Rear Panel TRIG OUT
connector Source"on page374.
| 3. TRIG OUT connector
6. Digital channel inputs 4. 10 MHz REF connector 5. Calibration protect switch
8. USB Host port
9. USB Device port
10. LAN port
7. VGA Video Out
2. Kensington lock hole 1. Power cord connector |
|---|
|  |
|  |  |  |
|---|---|---|
|  |  |  |
|  |  |  |
|  |
|---|
|  |
| Power cord
connector | Attach the power cord here. |
|---|---|
| Kensington lock
hole | This is where you can attach a Kensington lock for securing the instrument. |
| TRIG OUT
connector | Trigger output BNC connector. See “Setting the Rear Panel TRIG OUT
Source"on page374. |

---
**[Page 59]**

1 Getting Started
60 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
4. 10 MHz REF For synchronizing the timebase of multiple instruments. See “Setting the
connector Reference Signal Mode"on page375.
5. Calibration See “To perform user calibration"on page378.
protect switch
6. Digital channel Connect the digital probe cable to this connector (MSO models only). See
inputs Chapter6, “Digital Channels,” starting on page 131.
7. VGA video Lets you connect an external monitor or projector to provide a larger
output display or to provide a display at a viewing position away from the
oscilloscope.
The oscilloscope's built-in display remains on even when an external
display is connected. The video output connector is always active.
For optimal video quality and performance, we recommend you use a
shielded video cable with ferrite cores.
8. USB Host port This port functions identically to the USB host port on the front panel. USB
Host Port is used for saving data from the oscilloscope and loading
software updates. See also USB Host port (see page43).
9. USB Device This port is for connecting the oscilloscope to a host PC. You can issue
port remote commands from a host PC to the oscilloscope via the USB device
port. See “Remote Programming with Keysight IO Libraries"on
page390.
10. LAN port Lets you print to network printers (see Chapter22, “Print (Screens),”
starting on page 357) and access the oscilloscope's built-in web server.
See Chapter24, “Web Interface,” starting on page 383 and “Accessing
the Web Interface"on page384.
Learn the Oscilloscope Display
The oscilloscope display contains acquired waveforms, setup information,
measurement results, and the softkey definitions.
| 4. | 10 MHz REF
connector | For synchronizing the timebase of multiple instruments. See “Setting the
Reference Signal Mode"on page375. |
|---|---|---|
| 5. | Calibration
protect switch | See “To perform user calibration"on page378. |
| 6. | Digital channel
inputs | Connect the digital probe cable to this connector (MSO models only). See
Chapter6, “Digital Channels,” starting on page 131. |
| 7. | VGA video
output | Lets you connect an external monitor or projector to provide a larger
display or to provide a display at a viewing position away from the
oscilloscope.
The oscilloscope's built-in display remains on even when an external
display is connected. The video output connector is always active.
For optimal video quality and performance, we recommend you use a
shielded video cable with ferrite cores. |
| 8. | USB Host port | This port functions identically to the USB host port on the front panel. USB
Host Port is used for saving data from the oscilloscope and loading
software updates. See also USB Host port (see page43). |
| 9. | USB Device
port | This port is for connecting the oscilloscope to a host PC. You can issue
remote commands from a host PC to the oscilloscope via the USB device
port. See “Remote Programming with Keysight IO Libraries"on
page390. |
| 10. | LAN port | Lets you print to network printers (see Chapter22, “Print (Screens),”
starting on page 357) and access the oscilloscope's built-in web server.
See Chapter24, “Web Interface,” starting on page 383 and “Accessing
the Web Interface"on page384. |

---
**[Page 60]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 61
Analog Trigger point, Delay Time/ Run/Stop Trigger Trigger Trigger level or
channel time reference time div status type source digital threshold
sensitivity
Voice recognition
Status line
Draw/drag
touch mode
Trigger level
Sidebar
information and
Analog
controls area
channels
and ground
levels Measurements
Digital channels
Cursors defining
measurement
Measurement
statistics
Menu line
Softkey labels
Figure 1 Interpreting the oscilloscope display
Status line The top line of the display contains vertical, horizontal, and trigger setup
information, as well as the voice recognition icon and the rectangle draw mode
or waveform drag mode selector.
Display area The display area contains the waveform acquisitions, channel identifiers, and
analog trigger, and ground level indicators. Each analog channel's information
appears in a different color.
Signal detail is displayed using 256 levels of intensity. For more information
about viewing signal detail see “To adjust waveform intensity"on
page155.
For more information about display modes see Chapter8, “Display Settings,”
starting on page 155.
| Analog Trigger point, Delay Time/ Run/Stop Trigger Trigger Trigger level or
channel time reference time div status type source digital threshold
sensitivity
Voice recognition
Status line
Draw/drag
touch mode
Trigger level
Sidebar
information and
Analog
controls area
channels
and ground
levels Measurements
Digital channels
Cursors defining
measurement
Measurement
statistics
Menu line
Softkey labels |
|---|
|  |
| Status line | The top line of the display contains vertical, horizontal, and trigger setup
information, as well as the voice recognition icon and the rectangle draw mode
or waveform drag mode selector. |
|---|---|
| Display area | The display area contains the waveform acquisitions, channel identifiers, and
analog trigger, and ground level indicators. Each analog channel's information
appears in a different color.
Signal detail is displayed using 256 levels of intensity. For more information
about viewing signal detail see “To adjust waveform intensity"on
page155.
For more information about display modes see Chapter8, “Display Settings,”
starting on page 155. |

---
**[Page 61]**

1 Getting Started
62 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Sidebar The sidebar information area can contain summary, cursors, measurements, or
information and digital voltmeter information dialogs or it can contain navigation and other
controls area control dialogs.
For more information, see:
• “Select Sidebar Information or Controls"on page49
• “Undock Sidebar Dialogs by Dragging"on page50
Menu line This line normally contains menu name or other information associated with the
selected menu.
Softkey labels These labels describe softkey functions. Typically, softkeys let you set up
additional parameters for the selected mode or menu.
Pressing the Back Back/Up key at the top of the menu hierarchy turns off softkey
labels and displays additional status information describing channel offset and
other configuration parameters.
Access the Built-In Quick Help
To view Quick Help 1 Press and hold the key or softkey for which you would like to view help.
| Sidebar
information and
controls area | The sidebar information area can contain summary, cursors, measurements, or
digital voltmeter information dialogs or it can contain navigation and other
control dialogs.
For more information, see:
• “Select Sidebar Information or Controls"on page49
• “Undock Sidebar Dialogs by Dragging"on page50 |
|---|---|
| Menu line | This line normally contains menu name or other information associated with the
selected menu. |
| Softkey labels | These labels describe softkey functions. Typically, softkeys let you set up
additional parameters for the selected mode or menu.
Pressing the Back Back/Up key at the top of the menu hierarchy turns off softkey
labels and displays additional status information describing channel offset and
other configuration parameters. |

---
**[Page 62]**

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 63
Quick Help
message
Press and hold front panel key or softkey
(or right-click softkey when using web browser remote front panel).
Quick Help remains on the screen until another key is pressed or a knob is turned.
To select the To select the language of the user interface, Quick Help, and voice control:
language
1 Press [Help], then press the Language (Voice) softkey.
2 Repeatedly press and release the Language (Voice) softkey or rotate the Entry
knob until the desired language is selected.
The "Voice" in parentheses specifies the accent of the selected language for voice
recognition. See “Learn the Voice Controls"on page58.
| Quick Help
message
Press and hold front panel key or softkey
(or right-click softkey when using web browser remote front panel). | Quick Help
message
Press and hold front panel key or softkey
(or right-click softkey when using web browser remote front panel). |
|---|---|

---
**[Page 63]**

1 Getting Started
64 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 64]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
65
2 Horizontal Controls
To adjust the horizontal (time/div) scale / 66
To adjust the horizontal delay (position) / 67
Panning and Zooming Single or Stopped Acquisitions / 68
To change the horizontal time mode (Normal, XY, or Roll) / 69
To display the zoomed time base / 73
To change the horizontal scale knob's coarse/fine adjustment setting / 74
To position the time reference (left, center, right) / 75
Searching for Events / 75
Navigating the Time Base / 77
The horizontal controls include:
• Touchscreen controls for setting the horizontal scale and position (delay),
accessing the Horizontal Menu, and navigating (see “Pinch, Flick, or Drag to
Scale, Position, and Change Offset"on page47 and “Access the Horizontal
Menu and Open the Scale/Delay Dialog"on page56).
• The horizontal scale and position knobs.
• The [Horiz] key for accessing the Horizontal Menu.
• The zoom key for quickly enabling/disabling the split-screen zoom display.
• The [Search] key for finding events on analog channels or in serial decode.
• The [Navigate] keys for navigating time, search events, or segmented memory
acquisitions.
The following figure shows the Horizontal Menu which appears after pressing the
[Horiz] key.

---
**[Page 65]**

2 Horizontal Controls
66 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Trigger Time Delay Time/ Trigger Trigger level
point reference time div source or threshold
Sample rate
XY or Roll
mode
Normal Zoomed Fine Time
time mode time base control reference
Figure 2 Horizontal Menu
The Horizontal Menu lets you select the time mode (Normal, XY, or Roll), enable
Zoom, set the time base fine control (vernier), and specify the time reference.
The current sample rate is displayed in the right-side information area.
To adjust the horizontal (time/div) scale
You can:
| Trigger Time Delay Time/ Trigger Trigger level
point reference time div source or threshold
Sample rate
XY or Roll
mode
Normal Zoomed Fine Time
time mode time base control reference |
|---|
|  |

---
**[Page 66]**

Horizontal Controls 2
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 67
• Use the touchscreen pinch gesture (see “Pinch, Flick, or Drag to Scale,
Position, and Change Offset"on page47).
• Use the touchscreen controls to open a horizontal scale/delay dialog (see
“Access the Horizontal Menu and Open the Scale/Delay Dialog"on page56).
• Turn the large horizontal scale (sweep speed) knob marked to
change the horizontal time/div setting.
Notice how the time/div information in the status line changes.
The ∇ symbol at the top of the display indicates the time reference point.
The horizontal scale knob works (in the Normal time mode) while acquisitions are
running or when they are stopped. When running, adjusting the horizontal scale
knob changes the sample rate. When stopped, adjusting the horizontal scale knob
lets you zoom into acquired data. See “Panning and Zooming Single or Stopped
Acquisitions"on page68.
Note that the horizontal scale knob has a different purpose in the Zoom display.
See “To display the zoomed time base"on page73.
To adjust the horizontal delay (position)
You can:
• Use the touchscreen flick and drag gestures (see “Pinch, Flick, or Drag to
Scale, Position, and Change Offset"on page47).
• Use the touchscreen controls to open a horizontal scale/delay dialog (see
“Access the Horizontal Menu and Open the Scale/Delay Dialog"on page56).
• Turn the horizontal delay (position) knob ( ).
The trigger point moves horizontally, pausing at 0.00s (mimicking a
mechanical detent), and the delay value is displayed in the status line.
Changing the delay time moves the trigger point (solid inverted triangle)
horizontally and indicates how far it is from the time reference point (hollow
inverted triangle ∇). These reference points are indicated along the top of the
display grid.
|  |  |
|---|---|

---
**[Page 67]**

2 Horizontal Controls
68 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure2 shows the trigger point with the delay time set to 200µs. The delay time
number tells you how far the time reference point is located from the trigger point.
When delay time is set to zero, the delay time indicator overlays the time reference
indicator.
All events displayed left of the trigger point happened before the trigger occurred.
These events are called pre-trigger information, and they show events that led up
to the trigger point.
Everything to the right of the trigger point is called post-trigger information. The
amount of delay range (pre-trigger and post-trigger information) available
depends on the time/div selected and memory depth.
The horizontal position knob works (in the Normal time mode) while acquisitions
are running or when they are stopped. When running, adjusting the horizontal
scale knob changes the sample rate. When stopped, adjusting the horizontal scale
knob lets you zoom into acquired data. See “Panning and Zooming Single or
Stopped Acquisitions"on page68.
Note that the horizontal position knob has a different purpose in the Zoom display.
See “To display the zoomed time base"on page73.
Panning and Zooming Single or Stopped Acquisitions
When the oscilloscope is stopped, use the touchscreen pinch, flick, and drag
gestures or use the horizontal scale and position knobs to pan and zoom your
waveform. The stopped display may contain several acquisitions worth of
information, but only the last acquisition is available for pan and zoom.
The ability to pan (move horizontally) and scale (expand or compress horizontally)
an acquired waveform is important because of the additional insight it can reveal
about the captured waveform. This additional insight is often gained from seeing
the waveform at different levels of abstraction. You may want to view both the big
picture and the specific little picture details.
The ability to examine waveform detail after the waveform has been acquired is a
benefit generally associated with digital oscilloscopes. Often this is simply the
ability to freeze the display for the purpose of measuring with cursors or printing
the screen. Some digital oscilloscopes go one step further by including the ability
to further examine the signal details after acquiring them by panning through the
waveform and changing the horizontal scale.

---
**[Page 68]**

Horizontal Controls 2
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 69
There is no limit imposed on the scaling ratio between the time/div used to
acquire the data and the time/div used to view the data. There is, however, a
useful limit. This useful limit is somewhat a function of the signal you are
analyzing.
Zooming into stopped acquisitions
NOTE
The screen will still contain a relatively good display if you zoom-in horizontally by a factor of
1000 and zoom-in vertically by a factor of 10 to display the information from where it was
acquired. Remember that you can only make automatic measurements on displayed data.
To change the horizontal time mode (Normal, XY, or Roll)
1 Press [Horiz].
2 In the Horizontal Menu, press TimeMode; then, select:
• Normal — the normal viewing mode for the oscilloscope.
In the Normal time mode, signal events occurring before the trigger are
plotted to the left of the trigger point (▼ ) and signal events after the trigger
plotted to the right of the trigger point.
• XY — XY mode changes the display from a volts-versus-time display to a
volts-versus-volts display. The time base is turned off. Channel 1 amplitude
is plotted on the X-axis and Channel 2 amplitude is plotted on the Y-axis.
You can use XY mode to compare frequency and phase relationships
between two signals. XY mode can also be used with transducers to display
strain versus displacement, flow versus pressure, volts versus current, or
voltage versus frequency.
Use the cursors to make measurements on XY mode waveforms.
For more information about using XY mode for measurements, refer to “XY
Time Mode"on page70.
• Roll — causes the waveform to move slowly across the screen from right to
left. It only operates on time base settings of 50ms/div and slower. If the
current time base setting is faster than the 50ms/div limit, it will be set to
50ms/div when Roll mode is entered.
| NOTE |
|---|
|  |

---
**[Page 69]**

2 Horizontal Controls
70 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
In Roll mode there is no trigger. The fixed reference point on the screen is the
right edge of the screen and refers to the current moment in time. Events
that have occurred are scrolled to the left of the reference point. Since there
is no trigger, no pre-trigger information is available.
If you would like to pause the display in Roll mode press the [Single] key. To
clear the display and restart an acquisition in Roll mode, press the [Single]
key again.
Use Roll mode on low-frequency waveforms to yield a display much like a
strip chart recorder. It allows the waveform to roll across the display.
XY Time Mode
The XY time mode converts the oscilloscope from a volts-versus-time display to a
volts-versus-volts display using two input channels. Channel 1 is the X-axis input,
channel 2 is the Y-axis input. You can use various transducers so the display could
show strain versus displacement, flow versus pressure, volts versus current, or
voltage versus frequency.
Example This exercise shows a common use of the XY display mode by measuring the
phase difference between two signals of the same frequency with the Lissajous
method.
1 Connect a sine wave signal to channel 1, and a sine wave signal of the same
frequency but out of phase to channel 2.
2 Press the [Auto Scale] key, press the [Horiz] key; then, press Time Mode and select
"XY".
3 Center the signal on the display with the channel 1 and 2 position ( ) knobs.
Use the channel 1 and 2 volts/div knobs and the channel 1 and 2 Fine softkeys
to expand the signal for convenient viewing.
The phase difference angle (θ) can be calculated using the following formula
(assuming the amplitude is the same on both channels):
A C
sinθ = or
B D
|  |
|---|
|  |
| A C
sinθ = or
B D | A C
sinθ = or
B D |
|---|---|

---
**[Page 70]**

Horizontal Controls 2
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 71
Signal must
be centered in
“X”
D A B
C
Measuring Signals 90 degrees Signals
phase difference out of phase in phase
Figure 3 XY time mode signals, centered on display
4 Press the [Cursors] key.
5 Set the Y2 cursor to the top of the signal, and set Y1 to the bottom of the
signal.
Note the Δ Y value at the bottom of the display. In this example, we are using
the Y cursors, but you could have used the X cursors instead.
6 Move the Y1 and Y2 cursors to the intersection of the signal and the Y axis.
Again, note the Δ Y value.
| Signal must
be centered in
“X”
D A B
C
Measuring Signals 90 degrees Signals
phase difference out of phase in phase |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  | Signal must
be centered in
“X” |  |  |  |
|---|---|---|---|---|
|  | D |  |  | A B |
|  |  |  |  |  |
|  |  | C |  |  |
|  |  |
|---|---|
|  |  |

---
**[Page 71]**

2 Horizontal Controls
72 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 4 Phase difference measurements, automatic and using cursors
7 Calculate the phase difference using the formula below.
For example, if the first Δ Y value is 2.297 and the second Δ Y value is 1.319:
secondΔY 1.319
sinθ = = ; θ = 35.05 degrees of phase shift
firstΔY 2.297
Z-Axis Input in XY Display Mode (Blanking)
NOTE
When you select the XY display mode, the time base is turned off. Channel 1 is the X-axis
input, channel 2 is the Y-axis input, and the EXTTRIGIN is the Z-axis input. If you only want to
see portions of the Y versus X display, use the Z-axis input. Z-axis turns the trace on and off
(analog oscilloscopes called this Z-axis blanking because it turned the beam on and off).
When Z is low (<1.4 V), Y versus X is displayed; when Z is high (>1.4 V), the trace is turned off.
|  |  |
|---|---|
| secondΔY 1.319
sinθ = = ; θ = 35.05 degrees of phase shift
firstΔY 2.297 | secondΔY 1.319
sinθ = = ; θ = 35.05 degrees of phase shift
firstΔY 2.297 |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 72]**

Horizontal Controls 2
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 73
To display the zoomed time base
Zoom, formerly called Delayed sweep mode, is a horizontally expanded version of
the normal display. When Zoom is selected, the display divides in half. The top
half of the display shows the normal time/div window and the bottom half
displays a faster Zoom time/div window.
The Zoom window is a magnified portion of the normal time/div window. You can
use Zoom to locate and horizontally expand part of the normal window for a more
detailed (higher-resolution) analysis of signals.
To turn on (or off) Zoom:
1 Press the zoom key (or press the [Horiz] key and then the Zoom softkey).
These markers show the Time/div Time/div Delay time
beginning and end of the for normal for zoomed momentarily displays
Zoom window window window when the Horizontal
position knob is turned
Normal
window
Signal
anomaly
expanded
in zoom
window
Zoom
window
Select
Zoom
| These markers show the Time/div Time/div Delay time
beginning and end of the for normal for zoomed momentarily displays
Zoom window window window when the Horizontal
position knob is turned
Normal
window
Signal
anomaly
expanded
in zoom
window
Zoom
window
Select
Zoom | These markers show the Time/div Time/div Delay time
beginning and end of the for normal for zoomed momentarily displays
Zoom window window window when the Horizontal
position knob is turned
Normal
window
Signal
anomaly
expanded
in zoom
window
Zoom
window
Select
Zoom |
|---|---|

---
**[Page 73]**

2 Horizontal Controls
74 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The area of the normal display that is expanded is outlined with a box and the rest
of the normal display is ghosted. The box shows the portion of the normal sweep
that is expanded in the lower half.
To change the time/div for the Zoom window, turn the horizontal scale (sweep
speed) knob. As you turn the knob, the zoomed window time/div is highlighted in
the status line above the waveform display area. The Horizontal scale (sweep
speed) knob controls the size of the box.
The Horizontal position (delay time) knob sets the left-to-right position of the
zoom window. The delay value, which is the time displayed relative to the trigger
point) is momentarily displayed in the upper-right portion of the display when the
delay time ( ) knob is turned.
Negative delay values indicate you're looking at a portion of the waveform before
the trigger event, and positive values indicate you're looking at the waveform after
the trigger event.
To change the time/div of the normal window, turn off Zoom; then, turn the
horizontal scale (sweep speed) knob.
For information about using zoom mode for measurements, refer to “To isolate a
pulse for Top measurement"on page254 and “To isolate an event for frequency
measurement"on page261.
To change the horizontal scale knob's coarse/fine adjustment
setting
1 Push the horizontal scale knob (or press [Horiz] > Fine) to toggle between fine
and coarse adjustment of the horizontal scale.
When Fine is enabled, turning the horizontal scale knob changes the time/div
(displayed in the status line at the top of the display) in smaller increments. The
time/div remains fully calibrated when Fine is on.
When Fine is turned off, the Horizontal scale knob changes the time/div setting in
a 1-2-5 step sequence.
|  |  |
|---|---|

---
**[Page 74]**

Horizontal Controls 2
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 75
To position the time reference (left, center, right)
Time reference is the reference point on the display for delay time (horizontal
position).
1 Press [Horiz].
2 In the Horizontal Menu, press TimeRef; then, select:
• Left — the time reference is set to one major division from the left edge of the
display.
• Center — the time reference is set to the center of the display.
• Right — the time reference is set to one major division from the right edge of
the display.
A small hollow triangle (∇) at the top of the display grid marks the position of the
time reference. When delay time is set to zero, the trigger point indicator (▼ )
overlays the time reference indicator.
The time reference position sets the initial position of the trigger event within
acquisition memory and on the display, with delay set to 0.
Turning the Horizontal scale (sweep speed) knob expands or contracts the
waveform about the time reference point (∇). See “To adjust the horizontal
(time/div) scale"on page66.
Turning the Horizontal position ( )knob in Normal mode (not Zoom) moves the
trigger point indicator (▼ ) to the left or right of the time reference point (∇). See
“To adjust the horizontal delay (position)"on page67.
Searching for Events
You can use the [Search] key and menu to search for Edge, Pulse Width, Rise/Fall
Time, Runt, Frequency Peaks, and Serial events on the analog channels.
Setting up searches (see “To set up searches"on page76) is similar to setting up
triggers. In fact, except for Frequency Peaks and Serial events, you can copy
search setups to trigger setups and vice-versa (see “To copy search setups"on
page76).
Searches are different than triggers in that they use the measurement threshold
settings instead of trigger levels.
|  |  |
|---|---|

---
**[Page 75]**

2 Horizontal Controls
76 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Found search events are marked with white triangles at the top of the graticule,
and the number of events found is displayed in the menu line just above the
softkey labels.
To set up searches
1 Press [Search].
2 In the Search Menu, press Search; then, turn the Entry knob to select the search
type.
3 Use the remaining softkeys to set up the selected search type.
In most cases, setting up searches is similar to setting up triggers:
• For setting up Edge searches, see “Edge Trigger"on page174.
• For setting up Pulse Width searches, see “Pulse Width Trigger"on
page178.
• For setting up Rise/Fall Time searches, see “Rise/Fall Time Trigger"on
page185.
• For setting up Runt searches, see “Runt Trigger"on page188.
• For setting up Frequency Peak searches, see “Searching for FFT Peaks"on
page105.
• For setting up Serial searches, see “Serial Trigger"on page205 and
“Searching Lister Data"on page153.
Remember that searches use the measurement threshold settings instead of
trigger levels. Use the Thresholds softkey in the Search Menu to access the
Measurement Threshold Menu. See “Measurement Thresholds"on page270.
To copy search setups
Except for Frequency Peak and Serial event search setups, you can copy search
setups to trigger setups and vice-versa.
1 Press [Search].
2 In the Search Menu, press Search; then, turn the Entry knob to select the search
type.
3 Press Copy.
4 In the Search Copy Menu:

---
**[Page 76]**

Horizontal Controls 2
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 77
• Press Copy to Trigger to copy the setup for the selected search type to the
same trigger type. For example, if the current search type is Pulse Width,
pressing Copy to Trigger copies the search settings to the Pulse Width trigger
settings and selects the Pulse Width trigger.
• Press Copy from Trigger to copy the trigger setup for the selected search type
to the search setup.
• To undo a copy, press Undo Copy.
The softkeys in the Search Copy Menu may not be available when one of the
settings cannot be copied or there is no trigger type that corresponds to the
search type.
Navigating the Time Base
You can use the [Navigate] key and controls to navigate through:
• Captured data (see “To navigate time"on page77).
• Search events (see “To navigate search events"on page78).
• Segments, when segmented memory acquisitions are turned on (see “To
navigate segments"on page78).
You can also access navigation controls on the touchscreen. See “Select Sidebar
Information or Controls"on page49.
To navigate time
When acquisitions are stopped, you can use the navigation controls to play
through the captured data.
1 Press [Navigate].
2 In the Navigate Menu, press Navigate; then, select Time.
3 Press the navigation keys to play backward, stop, or play forward in
time. You can press the or keys multiple times to speed up the
playback. There are three speed levels.
You can also access navigation controls on the touchscreen. See “Select Sidebar
Information or Controls"on page49.
|  |  |  |
|---|---|---|

---
**[Page 77]**

2 Horizontal Controls
78 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To navigate search events
When acquisitions are stopped, you can use the navigation controls to go to found
search events (set using the [Search] key and menu, see “Searching for Events"on
page75).
1 Press [Navigate].
2 In the Navigate Menu, press Navigate; then, select Search.
3 Press the back and forward keys to go to the previous or next search
event.
When searching Serial decode:
• The Autozoom softkey specifies whether the waveform display is automatically
zoomed to fit the marked row as you navigate.
• Pressing the Scroll Lister softkey lets you use the Entry knob to scroll through
data rows in the Lister display.
You can also access navigation controls on the touchscreen. See “Select Sidebar
Information or Controls"on page49.
To navigate segments
When the segmented memory acquisition is enabled and acquisitions are stopped,
you can use the navigation controls to play through the acquired segments.
1 Press [Navigate].
2 In the Navigate Menu, press Navigate; then, select Segments.
3 Press Play Mode; then, select:
• Manual — to play through segments manually.
In the Manual play mode:
• Press the back and forward keys to go to the previous or next
segment.
• Press the softkey to go to the first segment.
• Press the softkey to go to the last segment.
• Auto — to play through segments in an automated fashion.
In the Auto play mode:
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 78]**

Horizontal Controls 2
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 79
• Press the navigation keys to play backward, stop, or play
forward in time. You can press the or keys multiple times to speed
up the playback. There are three speed levels.
You can also access navigation controls on the touchscreen. See “Select Sidebar
Information or Controls"on page49.
|  |  |  |
|---|---|---|

---
**[Page 79]**

2 Horizontal Controls
80 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 80]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
81
3 Vertical Controls
To turn waveforms on or off (channel or math) / 82
To adjust the vertical scale / 83
To adjust the vertical position / 83
To specify channel coupling / 84
To specify channel input impedance / 85
To specify bandwidth limiting / 85
To change the vertical scale knob's coarse/fine adjustment setting / 86
To invert a waveform / 87
Setting Analog Channel Probe Options / 87
The vertical controls include:
• Touchscreen controls for setting the vertical scale and position (offset) and
accessing the Channel menus (see “Pinch, Flick, or Drag to Scale, Position,
and Change Offset"on page47 and “Turn Channels On/Off and Open
Scale/Offset Dialogs"on page56).
• The vertical scale and position knobs for each analog channel.
• The channel keys for turning a channel on or off and accessing the channel's
softkey menu.
The following figure shows the Channel 1 Menu that appears after pressing the [1]
channel key.

---
**[Page 81]**

3 Vertical Controls
82 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Channel, Trigger Trigger level
Volts/div source or threshold
Channel 1
ground
level
Channel 2
ground
level
The ground level of the signal for each displayed analog channel is identified by
the position of the icon at the far-left side of the display.
To turn waveforms on or off (channel or math)
You can:
• Use the touchscreen controls to turn channels on or off (see “Turn Channels
On/Off and Open Scale/Offset Dialogs"on page56).
• Press an analog channel key turn the channel on or off (and to display the
channel's menu).
When a channel is on, its key is illuminated.
| Channel, Trigger Trigger level
Volts/div source or threshold
Channel 1
ground
level
Channel 2
ground
level |
|---|
|  |
|  |  |
|---|---|

---
**[Page 82]**

Vertical Controls 3
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 83
Turning channels off
NOTE
You must be viewing the menu for a channel before you can turn it off. For example, if channel
1 and channel 2 are turned on and the menu for channel 2 is being displayed, to turn channel
1 off, press [1] to display the channel 1 menu; then, press [1] again to turn channel 1 off.
To adjust the vertical scale
You can:
• Use the touchscreen pinch gesture (see “Pinch, Flick, or Drag to Scale,
Position, and Change Offset"on page47).
• Use the touchscreen controls to open a vertical scale/offset dialog (see “Turn
Channels On/Off and Open Scale/Offset Dialogs"on page56).
• Turn the large knob above the channel key marked to set the vertical
scale (volts/division) for the channel.
The vertical scale knob changes the analog channel scale in a 1-2-5 step
sequence (with a 1:1 probe attached) unless fine adjustment is enabled (see “To
change the vertical scale knob's coarse/fine adjustment setting"on page86).
The analog channel Volts/Div value is displayed in the status line.
The default mode for expanding the signal when you turn the volts/division knob
is vertical expansionabout the ground level of the channel; however, you can
change this to expand about the center of the display. See “To choose "expand
about" center or ground"on page369.
To adjust the vertical position
You can:
• Use the touchscreen pinch and drag gestures (see “Pinch, Flick, or Drag to
Scale, Position, and Change Offset"on page47).
• Use the touchscreen controls to open a vertical scale/offset dialog (see “Turn
Channels On/Off and Open Scale/Offset Dialogs"on page56).
| NOTE |
|---|
|  |

---
**[Page 83]**

3 Vertical Controls
84 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Turn the small vertical position knob ( ) to move the channel's waveform up or
down on the display.
The offset voltage value represents the voltage difference between the vertical
center of the display and the ground level ( ) icon. It also represents the voltage
at the vertical center of the display if vertical expansion is set to expand about
ground (see “To choose "expand about" center or ground"on page369).
To specify channel coupling
Coupling changes the channel's input coupling to either AC (alternating current)
or DC (direct current).
If the channel is DC coupled, you can quickly measure the DC component of the signal by
TIP
simply noting its distance from the ground symbol.
If the channel is AC coupled, the DC component of the signal is removed, allowing you to use
greater sensitivity to display the AC component of the signal.
1 Press the desired channel key.
2 In the Channel Menu, press the Coupling softkey to select the input channel
coupling:
• DC — DC coupling is useful for viewing waveforms as low as 0Hz that do not
have large DC offsets.
• AC — AC coupling is useful for viewing waveforms with large DC offsets.
When AC coupling is chosen, you cannot select 50Ω mode. This is done to
prevent damage to the oscilloscope.
AC coupling places a 10Hz high-pass filter in series with the input waveform
that removes any DC offset voltage from the waveform.
Note that Channel Coupling is independent of Trigger Coupling. To change trigger
coupling see “To select the trigger coupling"on page211.
|  |
|---|
|  |
|  |  |
|---|---|
| TIP |
|---|
|  |

---
**[Page 84]**

Vertical Controls 3
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 85
To specify channel input impedance
When you connect an AutoProbe, self-sensing probe, or a compatible InfiniiMax probe, the
NOTE
oscilloscope automatically configures the analog input channels to the correct impedance.
1 Press the desired channel key.
2 In the Channel Menu, press Imped (impedance); then, select either:
• 50Ohm — matches 50ohm cables commonly used in making high frequency
measurements, and 50ohm active probes.
When 50Ohm input impedance is selected, it is displayed with the channel
information on-screen.
When AC coupling is selected (see “To specify channel coupling"on
page84) or excessive voltage is applied to the input, the oscilloscope
automatically switches to 1MOhm mode to prevent possible damage.
• 1MOhm — is for use with many passive probes and for general-purpose
measurements. The higher impedance minimizes the loading effect of the
oscilloscope on the device under test.
This impedance matching gives you the most accurate measurements because
reflections are minimized along the signal path.
See Also • For more information on probing, visit: www.keysight.com/find/scope_probes
• Information about selecting a probe can be found in document number
Keysight Oscilloscope Probes and Accessories Selection Guide (part number
5989-6162EN), available at www.keysight.com.
To specify bandwidth limiting
1 Press the desired channel key.
2 In the Channel Menu, press the BW Limit softkey to specify the channel's
bandwidth limit or to turn off the bandwidth limit.
For waveforms with frequencies below the bandwidth limit, turning the bandwidth
limit on removes unwanted high frequency noise from the waveform.
| NOTE |
|---|
|  |

---
**[Page 85]**

3 Vertical Controls
86 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The bandwidth limit also limits the trigger signal path of any channel that has BW
Limit turned on.
The limits that can be selected depend on the bandwidth of oscilloscope, the
channel's input impedance setting, and the channel's V/div setting:
Input Impedance V/div Oscilloscope Limits Available
Bandwidth
1MOhm >2mV/ (all) 20MHz
div
<=2mV (all) 20MHz or 200MHz
/div
50Ohm (all) 1GHz 20MHz or 200MHz
2.5GHz 20MHz, 200MHz, or 1.5GHz
4GHz 20MHz, 200MHz, 1.5GHz, or 3GHz
6GHz 20MHz, 200MHz, 1.5GHz, or 3GHz
To change the vertical scale knob's coarse/fine adjustment setting
1 Push the channel's vertical scale knob (or press the channel key and then the
Fine softkey in the Channel Menu) to toggle between fine and coarse
adjustment of the vertical scale.
You can also do this using the touchscreen. See “Turn Channels On/Off and
Open Scale/Offset Dialogs"on page56.
When Fine adjustment is selected, you can change the channel's vertical
sensitivity in smaller increments. The channel sensitivity remains fully calibrated
when Fine is on.
The vertical scale value is displayed in the status line at the top of the display.
When Fine is turned off, turning the volts/division knob changes the channel
sensitivity in a 1-2-5 step sequence.
| Input Impedance | V/div | Oscilloscope
Bandwidth | Limits Available |
|---|---|---|---|
| 1MOhm | >2mV/
div | (all) | 20MHz |
|  | <=2mV
/div | (all) | 20MHz or 200MHz |
| 50Ohm | (all) | 1GHz | 20MHz or 200MHz |
|  |  | 2.5GHz | 20MHz, 200MHz, or 1.5GHz |
|  |  | 4GHz | 20MHz, 200MHz, 1.5GHz, or 3GHz |
|  |  | 6GHz | 20MHz, 200MHz, 1.5GHz, or 3GHz |

---
**[Page 86]**

Vertical Controls 3
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 87
To invert a waveform
1 Press the desired channel key.
2 In the Channel Menu, press the Invert softkey to invert the selected channel.
When Invert is selected, the voltage values of the displayed waveform are inverted.
Invert affects how a channel is displayed. However, when using basic triggers, the
oscilloscope attempts to maintain the same trigger point by changing trigger
settings.
Inverting a channel also changes the result of any math function selected in the
Waveform Math Menu or any measurement.
Setting Analog Channel Probe Options
1 Press the probe's associated channel key.
2 In the Channel Menu, press the Probe softkey to display the Channel Probe
Menu.
This menu lets you select additional probe parameters such as attenuation
factor and units of measurement for the connected probe.
The Channel Probe Menu changes depending on the type of probe connected.
For passive probes, the Probe Check softkey appears; it guides you through the
process of compensating probes.
For some active probes (such as InfiniiMax probes), the oscilloscope can
accurately calibrate its analog channels for the probe. When you connect a
probe that can be calibrated, the Calibrate Probe softkey appears (and the probe
attenuation softkey may change). See “To calibrate a probe"on page89.
See Also • “To specify the channel units"on page88
• “To specify the probe attenuation"on page88
• “To specify the probe skew"on page89
|  |  |
|---|---|

---
**[Page 87]**

3 Vertical Controls
88 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To specify the channel units
1 Press the probe's associated channel key.
2 In the Channel Menu, press Probe.
3 In the Channel Probe Menu, press Units; then, select:
• Volts — for a voltage probe.
• Amps — for a current probe.
Channel sensitivity, trigger level, measurement results, and math functions will
reflect the measurement units you have selected.
To specify the probe attenuation
This is set automatically if the oscilloscope can identify the connected probe. See
Analog channel inputs (see page42).
The probe attenuation factor must be set properly for accurate measurement
results.
If you connect a probe that is not automatically identified by the oscilloscope, you
can manually set the attenuation factor as follows:
1 Press the channel key.
2 Press the Probe softkey until you have selected how you want to specify the
attenuation factor, choosing either Ratio or Decibels.
3 Turn the Entry knob to set the attenuation factor for the connected probe.
When measuring voltage values, the attenuation factor can be set from 0.1:1 to
10000:1 in a 1-2-5 sequence.
When measuring current values with a current probe, the attenuation factor can
be set from 10V/A to 0.0001V/A.
When specifying the attenuation factor in decibels, you can select values from
-20dB to 80dB.
If Amps is chosen as the units and a manual attenuation factor is chosen, then the
units as well as the attenuation factor are displayed above the Probe softkey.

---
**[Page 88]**

Vertical Controls 3
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 89
To specify the probe skew
When measuring time intervals in the nanoseconds (ns) range, small differences in
cable length can affect the measurement. Use Skew to remove cable-delay errors
between any two channels.
1 Probe the same point with both probes.
2 Press one of the probes associated channel key.
3 In the Channel Menu, press Probe.
4 In the Channel Probe Menu, press Skew; then, select the desired skew value.
Each analog channel can be adjusted ±100ns in 10ps increments for a total of
200ns difference.
The skew setting is not affected by pressing [Default Setup] or [Auto Scale].
To calibrate a probe
The Calibrate Probe softkey guides you through the process of calibrating probes.
For certain active probes, such as InfiniiMax probes, the oscilloscope can
accurately calibrate its analog channels for the probe. When you connect a probe
that can be calibrated, the Calibrate Probe softkey in the Channel Probe Menu
becomes active.
To calibrate one of these probes:
1 First, plug your probe into one of the oscilloscope channels.
This could be, for example, an InfiniiMax probe amplifier/probe head with
attenuators attached.
2 Connect the probe to the left side, Demo2, Probe Comp terminal, and the
probe ground to the ground terminal.
|  |
|---|
|  |

---
**[Page 89]**

3 Vertical Controls
90 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
When calibrating a differential probe, connect the positive lead to the Probe Comp terminal
NOTE
and the negative lead to the ground terminal. You may need to connect an alligator clip to the
ground lug to allow a differential probe to span between the Probe Comp test point and
ground. A good ground connection ensures the most accurate probe calibration.
3 Press the Channel on/off key to turn the channel on (if the channel is off).
4 In the Channel Menu, press the Probe softkey.
5 In the Channel Probe Menu, the second softkey from the left is for specifying
your probe head (and attenuation). Repeatedly press this softkey until the
probe head selection matches the attenuator you are using.
The choices are:
• 10:1 single-ended browser (no attenuator).
• 10:1 differential browser (no attenuator).
• 10:1 (+6 dB Atten) single-ended browser.
• 10:1 (+6 dB Atten) differential browser.
• 10:1 (+12 dB Atten) single-ended browser.
• 10:1 (+12 dB Atten) differential browser.
• 10:1 (+20 dB Atten) single-ended browser.
• 10:1 (+20 dB Atten) differential browser.
6 Press the Calibrate Probe softkey and follow the instructions on the display.
For more information on InfiniiMax probes and accessories, see the probe's User's
Guide.
| NOTE |
|---|
|  |

---
**[Page 90]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
91
4 Math Waveforms
To display math waveforms / 91
To adjust the math waveform scale and offset / 93
Units for Math Waveforms / 93
Math Operators / 94
Math Transforms / 96
Math Filters / 113
Math Visualizations / 116
The Measurement Record and Waveform Math / 123
You can define and display up to four math functions. Math function waveforms
display in shades of light purple.
Math functions can be performed on analog channels or they can be performed on
lower math functions when using operators other than add, subtract, multiply, or
divide.
To display math waveforms
1 Press the [Math] key on the front panel to display the Waveform Math Menu.
2 Press the Display Math softkey and turn the Entry knob to select the math
function you want to display. Then, either push the Entry knob or press the
Display Math softkey again to display the selected math function.
|  |  |
|---|---|

---
**[Page 91]**

4 Math Waveforms
92 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Use the Operator softkey to select an operator, transform, filter, or visualization.
For more information on the operators, see:
• “Math Operators"on page94
• “Math Transforms"on page96
• “Math Filters"on page113
• “Math Visualizations"on page116
4 Use the Source 1 softkey to select the analog channel (or lower math function)
on which to perform math. You can rotate the Entry knob or repetitively press
the Source 1 softkey to make your selection.
Higher math functions can operate on lower math functions. For example, if
Math 1 is set up as a subtract operation between channels 1 and 2, the Math 2
function could be set up as a FFT operation on the Math 1 function. These are
called cascaded math functions.
To cascade math functions, select the lower math function using the Source 1
softkey.
When cascading math functions, to get the most accurate results, be sure to vertically scale
TIP
lower math functions so that their waveforms take up the full screen without being clipped.
5 If you selected an arithmetic operator for the math function, use the Source 2
softkey to select the second source for the arithmetic operation.
6 To re-size and re-position the math waveform, see “To adjust the math
waveform scale and offset"on page93.
Math Operating Hints
TIP
If the analog channel or math function is clipped (not fully displayed on screen) the resulting
displayed math function will also be clipped.
Once the function is displayed, the analog channel(s) may be turned off for better viewing of
the math waveform.
The vertical scaling and offset of each math function can be adjusted for ease of viewing and
measurement considerations.
The math function waveform can be measured using [Cursors] and/or [Meas].
| TIP |
|---|
|  |
| TIP |
|---|
|  |

---
**[Page 92]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 93
To adjust the math waveform scale and offset
1 Make sure the multiplexed scale and position knobs above and below the [Math]
key are selected for the math waveform.
If the arrow to the left of the [Math] key is not illuminated, press the key.
2 Use the multiplexed scale and position knobs above and below the [Math] key to
re-size and re-position the math waveform.
Math Scale and Offset are Set Automatically
NOTE
Any time the currently displayed math function definition is changed, the function is
automatically scaled for optimum vertical scale and offset. If you manually set scale and offset
for a function, select a new function, then select the original function, the original function will
be automatically rescaled.
See Also • “Units for Math Waveforms"on page93
Units for Math Waveforms
Units for each input channel can be set to Volts or Amps using the Units softkey in
the channel's Probe Menu. Units for math function waveforms are:
Math function Units
add or subtract V or A
multiply V2, A2, or W (Volt-Amp)
d/dt V/s or A/s (V/second or A/second)
dt Vs or As (V-seconds or A-seconds)
FFT dB* (decibels). See also “FFT Units"on
page107.
√ (square root) V1/2, A1/2, or W1/2 (Volt-Amp)
| NOTE |
|---|
|  |
| Math function | Units |
|---|---|
| add or subtract | V or A |
| multiply | V2, A2, or W (Volt-Amp) |
| d/dt | V/s or A/s (V/second or A/second) |
| dt | Vs or As (V-seconds or A-seconds) |
| FFT | dB* (decibels). See also “FFT Units"on
page107. |
| √
(square root) | V1/2, A1/2, or W1/2 (Volt-Amp) |

---
**[Page 93]**

4 Math Waveforms
94 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Math function Units
* When the FFT source is channel 1, 2, 3 or 4, FFT units will be displayed in dBV when channel units
Ω
is set to Volts and channel impedance is set to 1M . FFT units will be displayed in dBm when
Ω
channel units is set to Volts and channel impedance is set to 50 . FFT units will be displayed as dB
for all other FFT sources or when a source channel's units has been set to Amps.
A scale unit of U (undefined) will be displayed for math functions when two source
channels are used and they are set to dissimilar units and the combination of units
cannot be resolved.
Math Operators
Math operators perform arithmetic operations (like add, subtract, or multiply) on
analog input channels.
• “Add or Subtract"on page94
• “Multiply or Divide"on page95
Add or Subtract
When you select add or subtract, the Source 1 and Source 2 values are added or
subtracted point by point, and the result is displayed.
You can use subtract to make a differential measurement or to compare two
waveforms.
If your waveforms' DC offsets are larger than the dynamic range of the
oscilloscope's input channels you will need to use a differential probe instead.
| Math function | Units |
|---|---|
| * When the FFT source is channel 1, 2, 3 or 4, FFT units will be displayed in dBV when channel units
Ω
is set to Volts and channel impedance is set to 1M . FFT units will be displayed in dBm when
Ω
channel units is set to Volts and channel impedance is set to 50 . FFT units will be displayed as dB
for all other FFT sources or when a source channel's units has been set to Amps. |  |

---
**[Page 94]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 95
Figure 5 Example of Subtract Channel 2 from Channel 1
See Also • “Units for Math Waveforms"on page93
Multiply or Divide
When you select the multiply or divide math function, the Source 1 and Source 2
values are multiplied or divided point by point, and the result is displayed.
The divide by zero case places holes (that is, zero values) in the output waveform.
Multiply is useful for seeing power relationships when one of the channels is
proportional to the current.
|  |
|---|
|  |

---
**[Page 95]**

4 Math Waveforms
96 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 6 Example of Multiply Channel 1 by Channel 2
See Also • “Units for Math Waveforms"on page93
Math Transforms
Math transforms perform a transform function (like differentiate, integrate, FFT, or
square root) on an analog input channel or on the result of an arithmetic
operation.
• “Differentiate"on page97
• “Integrate"on page98
• “FFT Spectrum"on page101
• “Square Root"on page109
• “Ax + B"on page109
|  |
|---|
|  |

---
**[Page 96]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 97
• “Square"on page110
• “Absolute Value"on page111
• “Common Logarithm"on page111
• “Natural Logarithm"on page112
• “Exponential"on page112
• “Base 10 Exponential"on page113
Differentiate
d/dt (differentiate) calculates the discrete time derivative of the selected source.
You can use differentiate to measure the instantaneous slope of a waveform. For
example, the slew rate of an operational amplifier may be measured using the
differentiate function.
Because differentiation is very sensitive to noise, it is helpful to set acquisition
mode to Averaging (see “Selecting the Acquisition Mode"on page223).
d/dt plots the derivative of the selected source using the "average slope estimate
at 4 points" formula. The equation is:
y +2y −2y − y
d = i+4 i+2 i−2 i−4
i 8Δt
Where:
• d = differential waveform.
• y = channel 1, 2, 3, 4, or Math 1, Math 2, Math 3 (lower math function) data
points.
• i = data point index.
• Δ t = point-to-point time difference.
| y +2y −2y − y
d = i+4 i+2 i−2 i−4
i 8Δt |
|---|
|  |

---
**[Page 97]**

4 Math Waveforms
98 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 7 Example of Differentiate Function
See Also • “Units for Math Waveforms"on page93
Integrate
dt (integrate) calculates the integral of the selected source. It shows the
accumulated amount of change.
You can use integrate to calculate the energy of a pulse in volt-seconds or
measure the area under a waveform by measuring the difference in the integrate
function value across the pulse or waveform.
dt plots the integral of the source using the "Trapezoidal Rule". The equation is:
|  |
|---|
|  |

---
**[Page 98]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 99
n
I = c + Δt∑y
n o i
i=0
Where:
• I = integrated waveform.
• Δ t = point-to-point time difference.
• y = channel 1, 2, 3, 4, or Math 1, Math 2, Math 3 (lower math function) data
points.
• c = arbitrary constant.
o
• i = data point index.
The integrate operator provides an Offset softkey that lets you enter a DC offset
correction factor for the input signal. Small DC offset in the integrate function
input (or even small oscilloscope calibration errors) can cause the integrate
function output to "ramp" up or down. This DC offset correction lets you level the
integrate waveform.
| n
I = c + Δt∑y
n o i
i=0 |
|---|
|  |

---
**[Page 99]**

4 Math Waveforms
100 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Integrate
without
DC offset
correction
0 V level
Figure 8 Integrate Without Signal Offset
| Integrate
without
DC offset
correction
0 V level |
|---|
|  |

---
**[Page 100]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 101
Integrate
with DC offset
correction
Figure 9 Integrate With Signal Offset
See Also • “Units for Math Waveforms"on page93
FFT Spectrum
FFT is used to compute the fast Fourier transform using analog input channels or a
lower math function. FFT takes the digitized time record of the specified source
and transforms it to the frequency domain. When the FFT function is selected, the
FFT spectrum is plotted on the oscilloscope display as magnitude in dBV versus
frequency. The readout for the horizontal axis changes from time to frequency
(Hertz) and the vertical readout changes from volts to dB.
Use the FFT function to find crosstalk problems, to find distortion problems in
analog waveforms caused by amplifier non-linearity, or for adjusting analog filters.
To display a FFT waveform:
| Integrate
with DC offset
correction |
|---|
|  |

---
**[Page 101]**

4 Math Waveforms
102 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
1 Press the Display Math softkey and turn the Entry knob to select the math
function you want to display. Then, either push the Entry knob or press the
Display Math softkey again to display the selected math function.
2 Press the [Math] key. Then, press the Display Math softkey and select the math
function you want to use. Then, press the Operator softkey and select FFT.
• Source 1 — selects the source for the FFT.
• Span/Center or Start Freq/Stop Freq — this pair of softkeys let you define the
displayed frequency range. Press the softkeys to toggle between:
• Span/Center — Span specifies the frequency range represented by the
width of the display. Divide span by 10 to calculate the frequency scale
per division. Center specifies the frequency at the center vertical grid line
of the display.
• Start Freq/Stop Freq — Start Freq specifies the frequency at the left side of
the display. Stop Freq specifies the frequency at the right side of the
display.
To set desired values, tap the softkey label on screen for a keypad entry
dialog or turn the Entry knob.
• Scale — lets you set your own vertical scale factors for FFT expressed in
dB/div (decibels/division). See “To adjust the math waveform scale and
offset"on page93.
• Offset — lets you set your own offset for the FFT. The offset value is in dB and
is represented by the center horizontal grid line of the display. See “To
adjust the math waveform scale and offset"on page93.
• More FFT — displays the More FFT Settings Menu.
3 Press the More FFT softkey to display additional FFT settings.
• Window— selects a window to apply to your FFT input signal:
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 102]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 103
• Hanning — window for making accurate frequency measurements or for
resolving two frequencies that are close together.
• Flat Top — window for making accurate amplitude measurements of
frequency peaks.
• Rectangular — good frequency resolution and amplitude accuracy, but use
only where there will be no leakage effects. Use on self-windowing
waveforms such as pseudo-random noise, impulses, sine bursts, and
decaying sinusoids.
• BlackmanHarris — window reduces time resolution compared to a
rectangular window, but improves the capacity to detect smaller impulses
due to lower secondary lobes.
• Vertical Units — lets you select Decibels or V RMS as the units for the FFT
vertical scale.
• Auto Setup — sets the frequency Span and Center to values that will cause
the entire available spectrum to be displayed. The maximum available
frequency is half the FFT sample rate, which is a function of the time per
division setting. The FFT resolution is the quotient of the sampling rate and
the number of FFT points (f /N). The current FFT Resolution is displayed
S
above the softkeys.
Scale and offset considerations
NOTE
If you do not manually change the FFT scale or offset settings, when you turn the horizontal
scale knob, the span and center frequency settings will automatically change to allow
optimum viewing of the full spectrum.
If you do manually set scale or offset, turning the horizontal scale knob will not change the
span or center frequency settings, allowing you see better detail around a specific frequency.
Pressing the FFT Auto Setup softkey will automatically rescale the waveform and span and
center will again automatically track the horizontal scale setting.
4 To make cursor measurements, press the [Cursors] key and set the Source
softkey to Math N.
Use the X1 and X2 cursors to measure frequency values and difference between
two frequency values (Δ X). Use the Y1 and Y2 cursors to measure amplitude in
dB and difference in amplitude (Δ Y).
| NOTE |
|---|
|  |

---
**[Page 103]**

4 Math Waveforms
104 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
5 To make other measurements, press the [Meas] key and set the Source softkey to
Math N.
You can make peak-to-peak, maximum, minimum, and average dB
measurements on the FFT waveform. You can also find the frequency value at
the first occurrence of the waveform maximum by using the X at Max Y
measurement.
The following FFT spectrum was obtained by connecting a 2.5V, 100kHz square
wave to channel 1. Set the horizontal scale to 50µs/div, vertical sensitivity to
1V/div, Units/div to 20dBV, Offset to -40.0dBV, Center frequency to 500kHz,
frequency Span to 1MHz, and window to Hanning.
See Also • “Searching for FFT Peaks"on page105
• “FFT Measurement Hints"on page105
• “FFT Units"on page107
• “FFT DC Value"on page107
• “FFT Aliasing"on page107
|  |
|---|
|  |

---
**[Page 104]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 105
• “FFT Spectral Leakage"on page108
• “Units for Math Waveforms"on page93
Searching for FFT Peaks
To search for FFT math function frequency peaks:
1 Press [Search].
2 In the Search Menu, press Search; then, turn the Entry knob to select Frequency
Peaks.
3 Press Source and select the FFT math function waveform to search.
4 Press Max # Peaks and specify the maximum number of FFT peaks to find.
5 Press Threshold and turn the Entry knob to specify the threshold level necessary
to be considered a peak.
6 Press Excursion to specify the amplitude above the FFT waveform's noise floor
necessary to be recognized as a peak.
Note that the FFT waveform's noise floor level differs when additional math
functions are applied to the FFT:
• When Averaged Value, Max Hold, or Min Hold are applied, the FFT waveform's
noise floor is more stable, and excursion level settings are more accurate.
• When no additional math functions are applied (normal), the FFT waveform's
noise floor is less stable and excursion level settings are less accurate.
White arrowheads at the top of the graticule show where FFT peaks are found.
When acquisitions are stopped, you can use the [Navigate] keys and cursors to look
at the search events found.
FFT Measurement Hints
The number of points acquired for the FFT record can be up to 65,536, and when
frequency span is at maximum, all points are displayed. Once the FFT spectrum is
displayed, the frequency span and center frequency controls are used much like
the controls of a spectrum analyzer to examine the frequency of interest in greater
detail. Place the desired part of the waveform at the center of the screen and
decrease frequency span to increase the display resolution. As frequency span is
decreased, the number of points shown is reduced, and the display is magnified.
While the FFT spectrum is displayed, use the [Math] and [Cursors] keys to switch
between measurement functions and frequency domain controls in FFT Menu.

---
**[Page 105]**

4 Math Waveforms
106 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
FFT Resolution
NOTE
The FFT resolution is the quotient of the sampling rate and the number of FFT points (f /N).
S
With a fixed number of FFT points (up to 65,536), the lower the sampling rate, the better the
resolution.
Decreasing the effective sampling rate by selecting a greater time/div setting will
increase the low frequency resolution of the FFT display and also increase the
chance that an alias will be displayed. The resolution of the FFT is the effective
sample rate divided by the number of points in the FFT. The actual resolution of
the display will not be this fine as the shape of the window will be the actual
limiting factor in the FFTs ability to resolve two closely space frequencies. A good
way to test the ability of the FFT to resolve two closely spaced frequencies is to
examine the sidebands of an amplitude modulated sine wave.
For the best vertical accuracy on peak measurements:
• Make sure the probe attenuation is set correctly. The probe attenuation is set
from the Channel Menu if the operand is a channel.
• Set the source sensitivity so that the input signal is near full screen, but not
clipped.
• Use the Flat Top window.
• Set the FFT sensitivity to a sensitive range, such as 2dB/division.
For best frequency accuracy on peaks:
• Use the Hanning window.
• Use Cursors to place an X cursor on the frequency of interest.
• Adjust frequency span for better cursor placement.
• Return to the Cursors Menu to fine tune the X cursor.
For more information on the use of FFTs please refer to Keysight Application Note
243, The Fundamentals of Signal Analysis at
http://literature.cdn.keysight.com/litweb/pdf/5952-8898E.pdf. Additional
information can be obtained from Chapter 4 of the book Spectrum and Network
Measurements by Robert A. Witte.
| NOTE |
|---|
|  |

---
**[Page 106]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 107
FFT Units
0 dBV is the amplitude of a 1 Vrms sinusoid. When the FFT source is channel 1 or
channel 2 (or channel 3 or 4 on 4-channel models), FFT units will be displayed in
dBV when channel units is set to Volts and channel impedance is set to 1MΩ .
FFT units will be displayed in dBm when channel units is set to Volts and channel
impedance is set to 50Ω .
FFT units will be displayed as dB for all other FFT sources or when a source
channel's units has been set to Amps.
FFT DC Value
The FFT computation produces a DC value that is incorrect. It does not take the
offset at center screen into account. The DC value is not corrected in order to
accurately represent frequency components near DC.
FFT Aliasing
When using FFTs, it is important to be aware of frequency aliasing. This requires
that the operator have some knowledge as to what the frequency domain should
contain, and also consider the sampling rate, frequency span, and oscilloscope
vertical bandwidth when making FFT measurements. The FFT resolution (the
quotient of the sampling rate and the number of FFT points) is displayed directly
above the softkeys when the FFT Menu is displayed.
Nyquist Frequency and Aliasing in the Frequency Domain
NOTE
The Nyquist frequency is the highest frequency that any real-time digitizing oscilloscope can
acquire without aliasing. This frequency is half of the sample rate. Frequencies above the
Nyquist frequency will be under sampled, which causes aliasing. The Nyquist frequency is also
called the folding frequency because aliased frequency components fold back from that
frequency when viewing the frequency domain.
Aliasing happens when there are frequency components in the signal higher than
half the sample rate. Because the FFT spectrum is limited by this frequency, any
higher components are displayed at a lower (aliased) frequency.
The following figure illustrates aliasing. This is the spectrum of a 990Hz square
wave, which has many harmonics. The horizontal time/div setting for the square
wave sets the sample rate and results in a FFT resolution of 1.91Hz. The displayed
| NOTE |
|---|
|  |

---
**[Page 107]**

4 Math Waveforms
108 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
FFT spectrum waveform shows the components of the input signal above the
Nyquist frequency to be mirrored (aliased) on the display and reflected off the right
edge.
Figure 10 Aliasing
Because the frequency span goes from ≈0 to the Nyquist frequency, the best way
to prevent aliasing is to make sure that the frequency span is greater than the
frequencies of significant energy present in the input signal.
FFT Spectral Leakage
The FFT operation assumes that the time record repeats. Unless there is an
integral number of cycles of the sampled waveform in the record, a discontinuity is
created at the end of the record. This is referred to as leakage. In order to minimize
spectral leakage, windows that approach zero smoothly at the beginning and end
of the signal are employed as filters to the FFT. The FFT Menu provides four
windows: Hanning, Flat Top, Rectangular, and Blackman-Harris. For more
|  |
|---|
|  |

---
**[Page 108]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 109
information on leakage, see Keysight Application Note 243, The Fundamentals of
Signal Analysis at
http://literature.cdn.keysight.com/litweb/pdf/5952-8898E.pdf.
Square Root
Square root (√) calculates the square root of the selected source.
Where the transform is undefined for a particular input, holes (zero values) appear
in the function output.
Figure 11 Example of √ (Square Root)
See Also • “Units for Math Waveforms"on page93
Ax + B
The Ax + B function lets you apply a gain and offset to an existing input source.
|  |
|---|
|  |

---
**[Page 109]**

4 Math Waveforms
110 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 12 Example of Ax + B
Use the Gain (A) softkey to specify the gain.
Use the Offset (B) softkey to specify the offset.
The Ax + B function differs from the Magnify math visualization function in that the
output is likely different than the input.
See Also • “Magnify"on page116
Square
The square function calculates the square of the selected source, point by point,
and displays the result.
Press the Source softkey to select the signal source.
See Also • “Square Root"on page109
|  |
|---|
|  |

---
**[Page 110]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 111
Absolute Value
The absolute value function changes negative values in the input to positive values
and displays the resulting waveform.
Figure 13 Example of Absolute Value
See Also • “Square"on page110
Common Logarithm
The Common Logarithm (log) function performs a transform of the input source.
Where the transform is undefined for a particular input, holes (zero values) appear
in the function output.
See Also • “Natural Logarithm"on page112
|  |
|---|
|  |

---
**[Page 111]**

4 Math Waveforms
112 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Natural Logarithm
The Natural Logarithm (ln) function performs a transform of the input source.
Where the transform is undefined for a particular input, holes (zero values) appear
in the function output.
Figure 14 Example of Natural Logarithm
See Also • “Common Logarithm"on page111
Exponential
The Exponential (e^x) function performs a transform of the input source.
See Also • “Base 10 Exponential"on page113
|  |
|---|
|  |

---
**[Page 112]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 113
Base 10 Exponential
The Base 10 Exponential (10^x) function performs a transform of the input source.
Figure 15 Example of Base 10 Exponential
See Also • “Exponential"on page112
Math Filters
You can use math filters to create a waveform that is the result of a the filter on an
analog input channel or on the result of an arithmetic operation.
• “High Pass and Low Pass Filter"on page114
• “Averaged Value"on page115
• “Smoothing"on page115
|  |
|---|
|  |

---
**[Page 113]**

4 Math Waveforms
114 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• “Envelope"on page116
High Pass and Low Pass Filter
The high-pass or low-pass filter functions apply the filter to the selected source
waveform and display the result in the math waveform.
The high-pass filter is a single-pole high-pass filter.
The low-pass filter is a 4th order Bessel-Thompson filter.
Use the Bandwidth softkey to select the filter's -3dB cutoff frequency.
The ratio of the input signal's Nyquist frequency and the selected -3dB cutoff frequency
NOTE
affects how many points are available in the output, and under some circumstances, there are
no points in the output waveform.
Figure 16 Example of Low Pass Filter
| NOTE |
|---|
|  |
|  |
|---|
|  |

---
**[Page 114]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 115
Averaged Value
When the Averaged Value operator is selected, the math waveform becomes the
selected source waveform, averaged the selected number of times.
The source waveform can be one of the analog input channels or one of the
previous math function waveforms.
Unlike acquisition averaging, the math averaging operator can be used to average
the data on a single analog input channel or math function.
If acquisition averaging is also used, the analog input channel data is averaged
and the math function averages it again. You can use both types of averaging to
get a certain number of averages on all waveforms and an increased number of
averages on a particular waveform.
As with acquisition averaging, averages are calculated using a "decaying average"
approximation, where:
next_average = current_average + (new_data - current_average)/N
Where N starts at 1 for the first acquisition and increments for each following
acquisition until it reaches the selected number of averages, where it holds.
Press the Reset Count softkey to clear the number of waveforms evaluated.
See Also • “Averaging Acquisition Mode"on page227
Smoothing
The resulting math waveform is the selected source with a normalized rectangular
(boxcar) FIR filter applied.
The boxcar filter is a moving average of adjacent waveform points, where the
number of adjacent points is specified by the Smoothing Points softkey. You can
choose an odd number of points, from 3 up to half of the measurement record or
precision analysis record.
The smoothing operator limits the bandwidth of the source waveform. The
smoothing operator can be used, for example, to smooth measurement trend
waveforms.

---
**[Page 115]**

4 Math Waveforms
116 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Envelope
The resulting math waveform shows the amplitude envelope for an amplitude
modulated (AM) input signal.
This function uses a Hilbert transform to get the real (in-phase, I) and imaginary
(quadrature, Q) parts of the input signal and then performs a square root of the
sum of the real and imaginary parts to get the demodulated amplitude envelope
waveform.
Math Visualizations
You can apply visualization math functions that give you different ways of viewing
captured data and measurement values.
• “Magnify"on page116
• “Max/Min Hold"on page117
• “Measurement Trend"on page118
• “Chart Logic Bus Timing"on page119
• “Chart Logic Bus State"on page120
• “Clock Recovery"on page122
Magnify
The magnify math function lets you display an existing input source at different
vertical settings to provide more vertical detail.

---
**[Page 116]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 117
Figure 17 Example of Magnify
See Also • “Ax + B"on page109
Max/Min Hold
The Max Hold operator records the maximum vertical values found at each
horizontal bucket across multiple analysis cycles and uses those values to build a
waveform.
The Min Hold operator is the same, except it records the minimum vertical values.
When not used in a frequency analysis domain, these functions are often referred
to as Max Envelope and Min Envelope.
Press the Reset Count softkey to clear the number of waveforms evaluated.
|  |
|---|
|  |

---
**[Page 117]**

4 Math Waveforms
118 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Measurement Trend
The measurement trend math function shows measurement values for a waveform
(based on measurement threshold settings) as the waveform progresses across
the screen. For every cycle, a measurement is made, and the value is displayed on
the screen for the cycle.
Figure 18 Example of Measurement Trend
Press the Measurement softkey to select the previously added measurement whose
trend you want to look at. You can display trend values for these measurements:
• Average
• RMS - AC
• Ratio
• Period
• Frequency
|  |
|---|
|  |

---
**[Page 118]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 119
• +Width
• -Width
• Duty Cycle
• Rise Time
• Fall Time
Use the Thresholds softkey to access the Measurement Threshold Menu. See
“Measurement Thresholds"on page270.
If a measurement cannot be made for part of a waveform, the trend function
output is a hole (that is, no value) until a measurement can be made.
Chart Logic Bus Timing
The Chart Logic Bus Timing function displays bus data values as an analog
waveform (like a D/A conversion). When the bus value is transitioning, the
function output is the bus's last stable state.

---
**[Page 119]**

4 Math Waveforms
120 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 19 Example of Chart Logic Bus Timing
Use the Units/Code softkey to specify the analog value equivalent of each
increment in the bus data value.
Use the 0 Offset softkey to specify the analog value equivalent of a bus data value
of zero.
Use the Units softkey to specify the type of values the bus data represents (volts,
amps, etc.).
See Also • “Chart Logic Bus State"on page120
Chart Logic Bus State
The Chart Logic Bus State function displays bus data values, sampled on a clock
signal's edge, as an analog waveform (like a D/A conversion).
|  |
|---|
|  |

---
**[Page 120]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 121
Figure 20 Example of Chart Logic Bus State
Use the Clock softkey to select the clock signal.
Use the Slope softkey to select the edge of the clock signal to be used.
Use the More Chart softkey to open a submenu for specifying the analog value
equivalent of each bus value increment, the analog equivalent of a zero bus value,
and the type of values the charted bus data represents (volts, amps, etc.).
Use the Units/Code softkey to specify the analog value equivalent of each
increment in the bus data value.
Use the 0 Offset softkey to specify the analog value equivalent of a bus data value
of zero.
|  |
|---|
|  |
|  |
|---|
|  |

---
**[Page 121]**

4 Math Waveforms
122 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Use the Units softkey to specify the type of values the bus data represents (volts,
amps, etc.).
See Also • “Chart Logic Bus Timing"on page119
Clock Recovery
Clock recovery is a feature that provides an ideal clock for comparison to actual
signal edges. Clock recovery is used, for example, in Clock TIE and Data TIE (Time
Interval Error) jitter measurements. You can also set up clock recovery and display
the recovered ideal clock as a math function waveform.
Use the Setup softkey to open a dialog where you can set up clock recovery
options. See “Setting Up Clock Recovery"on page122.
Setting Up Clock Recovery
The Clock Recovery dialog is used to select the clock recovery method and specify
its options.
|  |
|---|
|  |

---
**[Page 122]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 123
You can choose:
• Constant Frequency — The clock is assumed to be a constant frequency, and the
data rate recovery options are:
• Fully Automatic — The clock is recovered using the signal edge database only.
The narrowest pulse is presumed to be an isolated one or zero.
• Semi Automatic — The clock is recovered using the expected Nominal Data Rate
as a "seed" and the signal edge database.
• Manual — The expected Nominal Data Rate you enter is used. It should be the
reciprocal of the signal's unit interval.
• First Order PLL — The clock is recovered using the DSP-modeled response of an
ideal first-order hardware PLL. Enter these parameters:
• Nominal Data Rate — The signal's expected bits/second data rate.
• Loop Bandwidth — The -3dB bandwidth specification of the PLL.
• Second Order PLL — The clock is recovered using the DSP-modeled response of
an ideal Type II, second-order hardware PLL. Enter these parameters:
• Nominal Data Rate — The signal's expected bits/second data rate.
• Loop Bandwidth — The -3dB bandwidth specification of the PLL.
• Damping Factor — The damping factor of the PLL's observed jitter transfer
function (OJTF).
Typical damping factor values are 1.0, which is critically damped, and 0.707,
which is considered ideal or optimal because of its fast settling time
(optimally flat) and Butterworth type response. Values less than 1 are
underdamped, and values greater than 1 are overdamped.
• Explicit — The clock is recovered from a second signal in your device under test,
with a multiplier from 1 to 1000 applied.
The Measurement Record and Waveform Math
Keysight InfiniiVision oscilloscopes are designed to provide high waveform update
rates which give you an increased probability of capturing infrequent events. With
high waveform update rates, there is less "dead time" between acquisitions.
To provide high waveform update rates, there are some things the oscilloscope
does with memory:

---
**[Page 123]**

4 Math Waveforms
124 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• When running, acquisition memory is split into two memories so that the
processing of one acquisition can take place while another acquisition is being
captured. For single acquisitions, the full memory is used. Waveform data in
acquisition memory is called the raw acquisition record.
• There is a separate 65536 (64K) points maximum of eavesdrop memory that is
used for making measurements and for calculating math functions. Data in this
memory is a reduced-sample decimation of the data in the raw acquisition
record. When a math function is turned on, eavesdrop memory is limited to
62500 points maximum. Waveform data in eavesdrop memory is called the
measurement record.
(If you want to calculate math functions on a longer record, you can save the
raw acquisition record and use programs like Excel or MATLAB to perform the
analysis.)
• On 6000X-Series oscilloscopes, there is a third memory used to enable
precision measurements and math functions at the expense of waveform
update rate. The depth of this memory is user-selectable from 100k points to
1M points. Using this "precision analysis" memory gives you better resolution
on measurements and math waveforms (including FFT). Waveform data in this
memory is called the precision analysis record.
Waveform data for the acquisition time (that is, the time per division setting
multiplied by 10 divisions across the display) is saved to the memories. When the
oscilloscope analog-to-digital converter's (ADC, or digitizer) sample period yields
more data points than can be stored in the memory, some samples are thrown
away (decimated), and the effective (or actual) sample rate is reduced. This is why,
at greater time/div settings, the displayed sample rate decreases.
For example, suppose an oscilloscope's digitizer has a sample period of 1ns
(maximum sample rate of 1GSa/s) and a 1M memory depth. At that rate, memory
is filled in 1ms. If the acquisition time is 100ms (10ms/div), only 1 of every 100
samples is needed to fill memory. The effective sample rate becomes 10MSa/s.
The decimator is configured to provide a best-estimate of all the samples that
each point in the record represents. There is no filtering in the decimation.
FFT (Spectral) When the FFT operator is turned on, the decimation from the raw acquisition
Analysis of record to the measurement record works on integer rate down-sampling. For
Measurement example, a raw acquisition record of 2000000 points and a measurement record of
Record Data 62500 points are already set up with an integer rate decimation of 32 (2000000/32
= 62500).

---
**[Page 124]**

Math Waveforms 4
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 125
For FFT analysis, the decimated record is then zero-padded to 2(X+1) where 2X >=
record length. For the above example, the power of 2 greater than the record
length is 65536, so the record is zero-padded to 131072 points.
You can look at the FFT math function results on the oscilloscope to work
backward and find the un-zero-padded decimated record length as well as the
FFT length used after the zero-padding:
• First, we know:
• The FFT algorithm translates a time record of N equally spaced samples into
N/2 equally spaced lines in the frequency domain.
• The width of the FFT on the display is the maximum frequency in the FFT.
The maximum FFT frequency is also f /2, where f is the effective sample
S S
rate of the decimated data. (Use the center/span or start/stop frequency
controls to display the maximum FFT frequency.)
• The FFT Resolution is displayed in the FFT menu. FFT resolution is also
known as the FFT bin width or a line in the frequency domain.
• Therefore, the un-zero-padded decimated record length is: f x the acquisition
S
time (or 2 x max FFT freq x acquisition time).
• Also, the FFT length used after the zero-padding is: 2 x (maximum FFT
frequency)/(FFT Resolution).
All this works the same with the precision analysis record, except that, instead of a
62500 point record length, the record length is user-selectable between 100k
points and 1M points.
For more information on FFT transformation, see Keysight Application Note 243,
The Fundamentals of Signal Analysis at
http://literature.cdn.keysight.com/litweb/pdf/5952-8898E.pdf.

---
**[Page 125]**

4 Math Waveforms
126 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 126]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
127
5 Reference Waveforms
To save a waveform to a reference waveform location / 127
To display a reference waveform / 128
To scale and position reference waveforms / 129
To adjust reference waveform skew / 130
To display reference waveform information / 130
To save/recall reference waveform files to/from a USB storage device / 130
Analog channel or math waveforms can be saved to one of four reference
waveform locations in the oscilloscope. Then, reference waveforms can be
displayed and compared against other waveforms.
When the multiplexed knobs are assigned to reference waveforms (this happens
when you press the [Ref] key and the LED to the left of it is lit), you can use the
knobs to scale and position reference waveforms. There is also a skew adjustment
for reference waveforms. Reference waveform scale, offset, and skew information
can optionally be included on the oscilloscope display.
Analog channel, math, or reference waveforms can be saved to a reference
waveform file on a USB storage device. You can recall a reference waveform file
from a USB storage device into one of the reference waveform locations.
To save a waveform to a reference waveform location
1 Press the [Ref] key to turn on reference waveforms.
2 In the Reference Waveform Menu, press the Display Ref softkey and turn the
Entry knob to select the desired reference waveform location you want to
display. Then, either push the Entry knob or press the Display Ref softkey again
to display the selected reference waveform location.

---
**[Page 127]**

5 Reference Waveforms
128 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Press the Source softkey and turn the Entry knob to select the source waveform.
4 Press the Save to R1/R2/R3/R4 softkey to save the waveform to the reference
waveform location.
Reference waveforms are non-volatile — they remain after power cycling or performing a
NOTE
default setup.
To clear a 1 Press the [Ref] key to turn on reference waveforms.
reference
2 In the Reference Waveform Menu, press the Ref softkey and turn the Entry knob
waveform location
to select the desired reference waveform location.
3 Press the Clear R1/R2/R3/R4 softkey to clear the reference waveform location.
Reference waveforms are also cleared by a Factory Default or Secure Erase (see
Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on page 343).
To display a reference waveform
1 Press the [Ref] key to turn on reference waveforms.
2 In the Reference Waveform Menu, press the Ref softkey and turn the Entry knob
to select the desired reference waveform location.
3 Then, press the Ref softkey again to enable/disable the reference waveform
display.
| NOTE |
|---|
|  |

---
**[Page 128]**

Reference Waveforms 5
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 129
Reference waveforms are always drawn as vectors (that is, lines between
waveform data points) and may look different than waveforms drawn as dots (if
that option is available in your oscilloscope).
See Also • “To display reference waveform information"on page130
To scale and position reference waveforms
1 Make sure the multiplexed scale and position knobs above and below the [Ref]
key are selected for the reference waveform.
If the arrow to the left of the [Ref] key is not illuminated, press the key.
2 Turn the upper multiplexed knob to adjust the reference waveform scale.
3 Turn the lower multiplexed knob to adjust the reference waveform position.
|  |
|---|
|  |

---
**[Page 129]**

5 Reference Waveforms
130 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To adjust reference waveform skew
Once reference waveforms are displayed, you can adjust their skew.
1 Display the desired reference waveform (see “To display a reference
waveform"on page128).
2 Press the Skew softkey and turn the Entry knob to adjust the reference
waveform skew.
To display reference waveform information
1 Press the [Ref] key to turn on reference waveforms.
2 In the Reference Waveform Menu, press the Options softkey.
3 In the Reference Waveform Options Menu, press the Display Info softkey to
enable or disable reference waveform information on the oscilloscope display.
To save/recall reference waveform files to/from a USB storage
device
Analog channel, math, or reference waveforms can be saved to a reference
waveform file on a USB storage device. See “To save reference waveform files to a
USB storage device"on page350.
You can recall a reference waveform file from a USB storage device into one of the
reference waveform locations. See “To recall reference waveform files from a USB
storage device"on page354.

---
**[Page 130]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
131
6 Digital Channels
To connect the digital probes to the device under test / 131
Acquiring waveforms using the digital channels / 135
To display digital channels using Autoscale / 135
Interpreting the digital waveform display / 136
To switch all digital channels on or off / 138
To switch groups of channels on or off / 138
To switch a single channel on or off / 138
To change the displayed size of the digital channels / 137
To reposition a digital channel / 139
To change the logic threshold for digital channels / 139
To display digital channels as a bus / 140
Digital channel signal fidelity: Probe impedance and grounding / 143
This chapter describes how to use the digital channels of a Mixed-Signal
Oscilloscope (MSO).
The digital channels are enabled on MSOX6000X-Series models and
DSOX6000X-Series models that have the MSO upgrade license installed.
To connect the digital probes to the device under test
1 If necessary, turn off the power supply to the device under test.
Turning off power to the device under test would only prevent damage that
might occur if you accidentally short two lines together while connecting
probes. You can leave the oscilloscope powered on because no voltage appears
at the probes.

---
**[Page 131]**

6 Digital Channels
132 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Off
2 Connect the digital probe cable to the DIGITAL Dn - D0 connector on the
mixed-signal oscilloscope. The digital probe cable is keyed so you can connect
it only one way. You do not need to power-off the oscilloscope.
Probe cable for digital channels
CAUTION
Use only the Keysight logic probe and accessory kit supplied with the mixed-signal
oscilloscope (see “Accessories Available"on page405).
3 Connect the ground lead on each set of channels (each pod), using a probe
grabber. The ground lead improves signal fidelity to the oscilloscope, ensuring
accurate measurements.
Channel
Pod Ground
Circuit
Ground
| Off | Off |  | Off |  |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
| CAUTION |
|---|
|  |
| Channel
Pod Ground
Circuit
Ground | Channel
Pod Ground
Circuit
Ground |
|---|---|

---
**[Page 132]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 133
4 Connect a grabber to one of the probe leads. (Other probe leads are omitted
from the figure for clarity.)
Grabber
5 Connect the grabber to a node in the circuit you want to test.
6 For high-speed signals, connect a ground lead to the probe lead, connect a
grabber to the ground lead, and attach the grabber to ground in the device
under test.
| Grabber | Grabber |
|---|---|
|  |  |
|---|---|

---
**[Page 133]**

6 Digital Channels
134 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Signal
Ground
Grabber
7 Repeat these steps until you have connected all points of interest.
Signals
Ground
| Signal
Ground
Grabber | Signal
Ground
Grabber |
|---|---|
| Signals
Ground | Signals
Ground |
|---|---|

---
**[Page 134]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 135
Acquiring waveforms using the digital channels
When you press [Run/Stop] or [Single] to run the oscilloscope, the oscilloscope
examines the input voltage at each input probe. When the trigger conditions are
met the oscilloscope triggers and displays the acquisition.
For digital channels, each time the oscilloscope takes a sample it compares the
input voltage to the logic threshold. If the voltage is above the threshold, the
oscilloscope stores a 1 in sample memory; otherwise, it stores a 0.
To display digital channels using Autoscale
When signals are connected to the digital channels — be sure to connect the
ground leads — Autoscale quickly configures and displays the digital channels.
• To configure the instrument quickly, press the [Auto Scale] key.

---
**[Page 135]**

6 Digital Channels
136 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 21 Example: Autoscale of digital channels (MSO models only)
Any digital channel with an active signal will be displayed. Any digital channels
without active signals will be turned off.
• To undo the effects of Autoscale, press the Undo Autoscale softkey before
pressing any other key.
This is useful if you have unintentionally pressed the [Auto Scale] key or do not like
the settings Autoscale has selected. This will return the oscilloscope to its previous
settings. See also: “How Autoscale Works"on page34.
To set the instrument to the factory-default configuration, press the [Default Setup]
key.
Interpreting the digital waveform display
The following figure shows a typical display with digital channels.
|  |
|---|
|  |

---
**[Page 136]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 137
Delay Time/ Trigger Trigger
time div mode or type and
run status source
Digital Activity
channel indicators
identifiers
Waveform Turn Turn Threshold
size individual groups of menu key
channels channels
on/off on/off
Activity indicator When any digital channels are turned on, an activity indicator is displayed in the
status line at the bottom of the display. A digital channel can be always high ( ),
always low ( ), or actively toggling logic states ( ).
To change the displayed size of the digital channels
1 Press the [Digital] key.
| Delay Time/ Trigger Trigger
time div mode or type and
run status source
Digital Activity
channel indicators
identifiers
Waveform Turn Turn Threshold
size individual groups of menu key
channels channels
on/off on/off |
|---|
|  |

---
**[Page 137]**

6 Digital Channels
138 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 Press the size ( ) softkey to select how the digital channels are
displayed.
The sizing control lets you spread out or compress the digital traces vertically on
the display for more convenient viewing.
To switch a single channel on or off
1 With the Digital Channel Menu displayed, rotate the Entry knob to select the
desired channel from the popup menu.
2 Push the Entry knob or press the softkey that is directly below the popup menu
to switch the selected channel on or off.
To switch all digital channels on or off
1 Press the [Digital] key to toggle the display of digital channels. The Digital
Channel Menu is displayed above the softkeys.
If you want to switch the digital channels off, and the Digital Channel Menu is not
already displayed, you must push the [Digital] key twice to switch the digital
channels off. The first push displays the Digital Channel Menu, and the second
push switches the channels off.
To switch groups of channels on or off
1 Press the [Digital] key on the front panel if the Digital Channel Menu is not
already displayed.
2 Press the Turn off (or Turn on) softkey for the D15 - D8 group or the D7 - D0 group.
Each time you press the softkey, the softkey's mode toggles between Turn on and
Turn off.
|  |  |
|---|---|

---
**[Page 138]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 139
To change the logic threshold for digital channels
1 Press the [Digital] key so that the Digital Channel Menu is displayed.
2 Press the Thresholds softkey
3 Press the D15-D8 or D7-D0 softkey, then select a logic family preset or select
User to define your own threshold.
Logic family Threshold Voltage
TTL +1.4 V
CMOS +2.5 V
ECL –1.3 V
User Variable from –8 V to +8 V
The threshold you set applies to all channels within the selected D15-D8 or
D7-D0 group. Each of the two channel groups can be set to a different threshold
if desired.
Values greater than the set threshold are high (1) and values less than the set
threshold are low (0).
If the Thresholds softkey is set to User, press the User softkey for the channel group,
then turn the Entry knob to set the logic threshold. There is one User softkey for
each group of channels.
To reposition a digital channel
1 Make sure the multiplexed scale and position knobs above and below the key
are selected for digital channels.
If the arrow to the left of the [Digital] key is not illuminated, press the key.
2 Use the multiplexed Select knob to select the channel.
The selected waveform is highlighted in red.
3 Use the multiplexed Position knob to move the selected channel waveform.
| Logic family | Threshold Voltage |
|---|---|
| TTL | +1.4 V |
| CMOS | +2.5 V |
| ECL | –1.3 V |
| User | Variable from –8 V to +8 V |

---
**[Page 139]**

6 Digital Channels
140 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If a channel waveform is repositioned over another channel waveform, the
indicator at the left edge of the trace will change from Dnn designation (where
nn is a one or two digit channel number) to D*. The "*" indicates that multiple
channels are overlaid.
To display digital channels as a bus
Digital channels may be grouped and displayed as a bus, with each bus value
displayed at the bottom of the display in hex or binary. You can create up to two
buses. To configure and display each bus, press the [Digital] key on the front panel.
Then press the Bus softkey.
Next, select a bus. Rotate the Entry knob, then press the Entry knob or the
Bus1/Bus2 softkey to switch it on.
Use the Channel softkey and the Entry knob to select individual channels to be
included in the bus. You can rotate the Entry knob and push it or push the softkey
to select channels. You can also press the Select/Deselect D15-D8 and
Select/Deselect D7-D0 softkeys to include or exclude groups of eight channels in
each bus.
If the bus display is blank, completely white, or if the display includes "...", you
need to expand the horizontal scale to allow space for the data to be shown, or
use the cursors to display the values (see “Using cursors to read bus values"on
page141).
The Base softkey lets you choose to display the bus values in hex or binary.
The buses are shown at the bottom of the display.
|  |
|---|
|  |
|  |
|---|
|  |

---
**[Page 140]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 141
Bus values can be shown in hex or binary.
Using cursors to To read the digital bus value at any point using the cursors:
read bus values
1 Turn on Cursors (by pressing the [Cursors] key on the front panel)
2 Press the cursor Mode softkey and change the mode to Hex or Binary.
3 Press the Source softkey and select Bus1 or Bus2.
4 Use the Entry knob and the X1 and X2 softkeys to position the cursors where
you want to read the bus values.
|  |
|---|
|  |

---
**[Page 141]**

6 Digital Channels
142 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
X1 cursor
X2 cursor
Bus values
Set cursors Select Bus1 Bus values
mode to or Bus2 source at cursors
Binary or Hex shown here
Bus values are The bus values are also displayed when using the Pattern trigger function. Press
displayed when the [Pattern] key on the front panel to display the Pattern Trigger Menu and the bus
using Pattern values will be displayed on the right, above the softkeys.
trigger
The dollar sign ($) will be displayed in the bus value when the bus value cannot be
displayed as a hex value. This occurs when one or more "don't cares" (X) are
combined with low (0) and high (1) logic levels in the pattern specification, or
when a transition indicator — rising edge ( ) or falling edge ( ) — are included in
the pattern specification. A byte that consists of all don't cares (X) will be
displayed in the bus as a don't care (X).
| X1 cursor
X2 cursor
Bus values
Set cursors Select Bus1 Bus values
mode to or Bus2 source at cursors
Binary or Hex shown here | X1 cursor
X2 cursor
Bus values
Set cursors Select Bus1 Bus values
mode to or Bus2 source at cursors
Binary or Hex shown here |
|---|---|
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 142]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 143
Trigger Bus values Analog Digital
pattern displayed channel channel
definition values values
at cursor at cursor
See “Pattern Trigger"on page181 for more information on Pattern triggering.
Digital channel signal fidelity: Probe impedance and grounding
When using the mixed-signal oscilloscope you may encounter problems that are
related to probing. These problems fall into two categories: probe loading and
probe grounding. Probe loading problems generally affect the device under test,
while probe grounding problems affect the accuracy of the data to the
measurement instrument. The design of the probes minimizes the first problem,
while the second is easily addressed by good probing practices.
| Trigger Bus values Analog Digital
pattern displayed channel channel
definition values values
at cursor at cursor |
|---|
|  |

---
**[Page 143]**

6 Digital Channels
144 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Input Impedance
The logic probes are passive probes, which offer high input impedance and high
bandwidths. They usually provide some attenuation of the signal to the
oscilloscope, typically 20 dB.
Passive probe input impedance is generally specified in terms of a parallel
capacitance and resistance. The resistance is the sum of the tip resistor value and
the input resistance of the test instrument (see the following figure). The
capacitance is the series combination of the tip compensating capacitor and the
cable, plus instrument capacitance in parallel with the stray tip capacitance to
ground. While this results in an input impedance specification that is an accurate
model for DC and low frequencies, the high-frequency model of the probe input is
more useful (see the following figure). This high-frequency model takes into
account pure tip capacitance to ground as well as series tip resistance, and the
cable's characteristic impedance(Z ).
o
Figure 22 DC and Low-Frequency Probe Equivalent Circuit
|  |
|---|
|  |

---
**[Page 144]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 145
Figure 23 High-Frequency Probe Equivalent Circuit
The impedance plots for the two models are shown in these figures. By comparing
the two plots, you can see that both the series tip resistor and the cable's
characteristic impedance extend the input impedance significantly. The stray tip
capacitance, which is generally small (1pF), sets the final break point on the
impedance chart.
|  |
|---|
|  |

---
**[Page 145]**

6 Digital Channels
146 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
100 k
10 k High
Frequency
Model
1 k
Typical
100 Model
10
1
10 kHz 100 kHz 1 MHz 10 MHz 100 MHz 1 GHz
Frequency
Figure 24 Impedance versus Frequency for Both Probe Circuit Models
The logic probes are represented by the high-frequency circuit model shown
above. They are designed to provide as much series tip resistance as possible.
Stray tip capacitance to ground is minimized by the proper mechanical design of
the probe tip assembly. This provides the maximum input impedance at high
frequencies.
Probe Grounding
A probe ground is the low-impedance path for current to return to the source from
the probe. Increased length in this path will, at high frequencies, create large
common mode voltages at the probe input. The voltage generated behaves as if
this path were an inductor according to the equation:
ecnadepmI
di
V = L
dt
| 100 k
10 k High
Frequency
Model ecnadepmI
1 k
Typical
100 Model
10
1
10 kHz 100 kHz 1 MHz 10 MHz 100 MHz 1 GHz
Frequency |
|---|
|  |
| di
V = L
dt |
|---|
|  |

---
**[Page 146]**

Digital Channels 6
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 147
Increasing the ground inductance (L), increasing the current (di) or decreasing the
transition time (dt), will all result in increasing the voltage (V). When this voltage
exceeds the threshold voltage defined in the oscilloscope, a false data
measurement will occur.
Sharing one probe ground with many probes forces all the current that flows into
each probe to return through the same common ground inductance of the probe
whose ground return is used. The result is increased current (di) in the above
equation, and, depending on the transition time (dt), the common mode voltage
may increase to a level that causes false data generation.
Probe 1 Zin
i
1
L (GND)
Probe Vn (Common Mode)
Ground
i
1
+ i
2
+ i
n
i
2
+ i
n
Probe 2 Zin
i
n
Probe N Zin
Figure 25 Common Mode Input Voltage Model
In addition to the common mode voltage, longer ground returns also degrade the
pulse fidelity of the probe system. Rise time is increased, and ringing, due to the
undamped LC circuit at the input of the probe, is also increased. Because the
digital channels display reconstructed waveforms, they do not show ringing and
perturbations. You will not find ground problems through examination of the
| Probe 1 Zin
i
1
L (GND)
Probe Vn (Common Mode)
i + i + i
Ground 1 2 n
i + i
2 n
Probe 2 Zin
i
n
Probe N Zin |
|---|
|  |
|  |
|---|
| Zin |
| i
1
Vn (Common Mode)
i + i
2 n |
|---|
|  |
| i
n |
|  |
|---|
| Zin |
|  |
|---|
| Zin |

---
**[Page 147]**

6 Digital Channels
148 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
waveform display. In fact, it is likely you will discover the problem through random
glitches or inconsistent data measurements. Use the analog channels to view
ringing and perturbations.
Best Probing Practices
Because of the variables L, di, and dt, you may be unsure how much margin is
available in your measurement setup. The following are guidelines for good
probing practices:
• The ground lead from each digital channel group (D15–D8 and D7–D0) should
be attached to the ground of the device under test if any channel within the
group is being used for data capture.
• When capturing data in a noisy environment, every third digital channel probe's
ground should be used in addition to the channel group's ground.
• High-speed timing measurements (rise time < 3ns) should make use of each
digital channel probe's own ground.
When designing a high-speed digital system, you should consider designing
dedicated test ports that interface directly to the instrument's probe system. This
will ease measurement setup and ensure a repeatable method for obtaining test
data. The 01650-61607 16-channel logic probe cable and the 01650-63203
termination adapter are designed to make it easy to connect to industry-standard,
20-pin board connectors. The cable is a 2m logic analyzer probe cable, and the
termination adapter provides the proper RC networks in a very convenient
package. These parts, as well as the 1251-8106 20-pin, low-profile, straight board
connector, can be ordered from Keysight Technologies.

---
**[Page 148]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
149
7 Serial Decode
Serial Decode Options / 149
Lister / 151
Searching Lister Data / 153
Triggering on In some cases, such as when triggering on a slow serial signal (for example, I2C,
Serial Data SPI, CAN, LIN, etc.) it may be necessary to switch from the Auto trigger mode to
the Normal trigger mode to prevent the oscilloscope from Auto-triggering and
stabilize the display. You can select the trigger mode by:
• Touching "Auto" or "Trig'd" onscreen to quickly toggle the trigger mode. See
“Access the Trigger Menu, Change the Trigger Mode, and Open the Trigger
Level Dialog"on page57.
• Pressing the [Mode/Coupling] key, then the Mode softkey.
Also, the threshold voltage level must be set appropriately for each source
channel. The threshold level for each serial signal can be set in the Signals Menu.
Press the [Serial] key, then the Signals softkey.
Serial Decode Options
Keysight's hardware-accelerated serial decode options can be installed when the
oscilloscope is manufactured, or added later. The following serial decode licenses
are available:

---
**[Page 149]**

7 Serial Decode
150 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Serial Decode License See:
DSOX6AUTO — you can decode CAN (Controller • “CAN/CAN FD Serial Decode"on
Area Network) and LIN (Local Interconnect page426.
Network) serial buses. • “LIN Serial Decode"on page436.
DSOX6FLEX — you can decode FlexRay serial • “FlexRay Serial Decode"on page445.
buses.
DSOX6EMBD — you can decode I2C (Inter-IC) • “I2C Serial Decode"on page456.
and SPI (Serial Peripheral Interface) serial buses. • “SPI Serial Decode"on page466.
DSOX6AUDIO — you can decode I2S (Inter-IC • “I2S Serial Decode"on page477.
Sound or Integrated Interchip Sound) serial
buses.
DSOX6COMP — you can decode many UART • “UART/RS232 Serial Decode"on
(Universal Asynchronous Receiver/Transmitter) page515.
protocols including RS232 (Recommended
Standard 232).
DSOX6AERO — you can decode MIL-STD-1553 • “MIL-STD-1553 Serial Decode"on
and ARINC429 serial buses. page484.
• “ARINC429 Serial Decode"on page491.
DSOX6SENSOR — you can decode SENT (Single • “SENT Serial Decode"on page504.
Edge Nibble Transmission) serial buses.
DSOX6USBFL or DSOX6USBH — you can decode • “USB 2.0 Serial Decode"on page525.
USB Full/Low Speed or USB High Speed serial
buses.
To determine whether these licenses are installed on your oscilloscope, see “To
display oscilloscope information"on page380.
To order serial decode licenses, go to www.keysight.com and search for the
product number (for example, DSOX6AUTO) or contact your local Keysight
Technologies representative (see www.keysight.com/find/contactus).
| Serial Decode License | See: |
|---|---|
| DSOX6AUTO — you can decode CAN (Controller
Area Network) and LIN (Local Interconnect
Network) serial buses. | • “CAN/CAN FD Serial Decode"on
page426.
• “LIN Serial Decode"on page436. |
| DSOX6FLEX — you can decode FlexRay serial
buses. | • “FlexRay Serial Decode"on page445. |
| DSOX6EMBD — you can decode I2C (Inter-IC)
and SPI (Serial Peripheral Interface) serial buses. | • “I2C Serial Decode"on page456.
• “SPI Serial Decode"on page466. |
| DSOX6AUDIO — you can decode I2S (Inter-IC
Sound or Integrated Interchip Sound) serial
buses. | • “I2S Serial Decode"on page477. |
| DSOX6COMP — you can decode many UART
(Universal Asynchronous Receiver/Transmitter)
protocols including RS232 (Recommended
Standard 232). | • “UART/RS232 Serial Decode"on
page515. |
| DSOX6AERO — you can decode MIL-STD-1553
and ARINC429 serial buses. | • “MIL-STD-1553 Serial Decode"on
page484.
• “ARINC429 Serial Decode"on page491. |
| DSOX6SENSOR — you can decode SENT (Single
Edge Nibble Transmission) serial buses. | • “SENT Serial Decode"on page504. |
| DSOX6USBFL or DSOX6USBH — you can decode
USB Full/Low Speed or USB High Speed serial
buses. | • “USB 2.0 Serial Decode"on page525. |

---
**[Page 150]**

Serial Decode 7
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 151
Lister
Lister is a powerful tool for investigating protocol failures. You can use Lister to
view large amounts of packet level serial data in a tabular format, including time
tags and specific decoded values. After pressing the [Single] key, you can press the
Scroll Lister softkey and then rotate the Entry knob to select an event and press the
Zoom to Selection softkey to jump to the event.
To use the Lister:
1 Set up trigger and decode on the serial data signals to be analyzed.
2 Press [Serial] > Lister.
3 Press Window; then, turn the Entry knob to select the size of the Lister window
(Half-Screen or Full-Screen).
When the touchscreen is enabled, you can touch the Lister down or up
chevrons at the top right of the graticule to select the size of the Lister window.
4 Press Display; then, turn the Entry knob to select the serial slot (Serial1 or
Serial2) on which the serial bus signals are being decoded. (If you select All, the
decode information for different buses is interleaved in time.)

---
**[Page 151]**

7 Serial Decode
152 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Before you can select a row or navigate through the Lister data, oscilloscope
acquisitions must be stopped.
5 Press the [Single] key (in the Run Control group on the front panel) to stop the
acquisition.
Pressing [Single] instead of [Stop] fills the maximum memory depth.
When zoomed out and viewing a large number of packets, the Lister may not
be able to display information for all packets. However, when you press the
[Single] key the Lister will contain all on-screen serial decode information.
6 Press the Scroll Lister softkey and use the Entry knob to scroll through the data.
Time tags in the Time column indicate the event time relative to the trigger
point by default, and can optionally be configured to be relative to the previous
row, as described in step 9 that follows. The time tags of events that are shown
in the waveform display area are displayed with a dark background.
7 Press the Zoom to Selection softkey (or push the Entry knob) to center the
waveform display at the time associated with the selected Lister row and
automatically set the horizontal scale setting.
|  |  |
|---|---|

---
**[Page 152]**

Serial Decode 7
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 153
8 Press the Undo Zoom softkey to return to the horizontal scale and delay settings
before the last Zoom to Selection.
9 Press the Options softkey to open the Lister Options Menu. In this menu, you
can:
• Enable or disable the Track Time option. When enabled, as you select
different Lister rows (using the Entry knob while acquisitions are stopped),
the horizontal delay changes to the Time of the selected row. Also, changing
the horizontal delay will scroll the Lister.
• Press the Scroll Lister softkey and use the Entry knob to scroll though data
rows in the Lister display.
• Press the Time Ref softkey and use the Entry knob to select whether the Time
column in the Lister display shows times relative to the trigger or relative to
the previous packet row.
Searching Lister Data
When serial decode is enabled, you can use the [Search] key to find and place
marks on rows in the Lister.
The Search softkey lets you specify events to find. It is similar to specifying protocol
triggers.
Events found are marked in orange in the far left Lister column. The total number
of events found is displayed above the softkeys.

---
**[Page 153]**

7 Serial Decode
154 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Each serial decode option lets you find protocol-specific headers, data, errors, etc.
See:
• “Searching for ARINC429 Data in the Lister"on page496
• “Searching for CAN Data in the Lister"on page431
• “Searching for FlexRay Data in the Lister"on page449
• “Searching for I2C Data in the Lister"on page459
• “Searching for I2S Data in the Lister"on page480
• “Searching for LIN Data in the Lister"on page440
• “Searching for MIL-STD-1553 Data in the Lister"on page487
• “Searching for SENT Data in the Lister"on page509
• “Searching for SPI Data in the Lister"on page469
• “Searching for UART/RS232 Data in the Lister"on page518
• “Searching for USB 2.0 Data in the Lister"on page529
|  |
|---|
|  |

---
**[Page 154]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
155
8 Display Settings
To adjust waveform intensity / 155
To set or clear persistence / 157
To clear the display / 159
To select the grid type / 159
To adjust the grid intensity / 159
To add an annotation / 160
To display waveforms as vectors or dots / 162
To disable/enable antialiasing / 163
To freeze the display / 164
To adjust waveform intensity
You can adjust the intensity of displayed waveforms to account for various signal
characteristics, such as fast time/div settings and low trigger rates.
Increasing the intensity lets you see the maximum amount of noise and
infrequently occurring events.
Reducing the intensity can expose more detail in complex signals as shown in the
following figures.
1 Press the [Intensity] key to illuminate it.
This key is located just below the Entry knob.
2 Turn the Entry knob to adjust the waveform intensity.
Waveform intensity adjustment affects analog channel waveforms only (not math
waveforms, reference waveforms, digital waveforms, etc.).

---
**[Page 155]**

8 Display Settings
156 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 26 Amplitude Modulation Shown at 100% Intensity
|  |
|---|
|  |

---
**[Page 156]**

Display Settings 8
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 157
Figure 27 Amplitude Modulation Shown at 40% Intensity
To set or clear persistence
With persistence, the oscilloscope updates the display with new acquisitions, but
does not immediately erase the results of previous acquisitions. All previous
acquisitions are displayed with reduced intensity. New acquisitions are shown in
their normal color with normal intensity.
Waveform persistence is kept only for the current display area; you cannot pan
and zoom the persistence display.
To use persistence:
1 Press the [Display] key; then, press the Persistence softkey.
|  |
|---|
|  |

---
**[Page 157]**

8 Display Settings
158 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 In the Waveform Persistence Menu, press Persistence; then, turn the Entry knob
to select between:
• Off — turns off persistence.
When persistence is off, you can press the Capture Waveforms softkey to
perform a single-shot infinite persistence. A single acquisition's data is
displayed with reduced intensity, and it remains on the display until you
clear persistence or clear the display.
Included in the persistence data are active analog channels and digital
channels.
• ∞Persistence — (infinite persistence) Results of previous acquisitions are
never erased.
Use infinite persistence to measure noise and jitter, to see the worst-case
extremes of varying waveforms, to look for timing violations, or to capture
events that occur infrequently.
• Variable Persistence — Results of previous acquisitions are erased after a
certain amount of time.
Variable persistence gives you a view of acquired data that is similar to
analog oscilloscopes.
When variable persistence is selected, press the Time softkey and use the
Entry knob to specify the amount of time that previous acquisitions are to be
displayed.
The display will begin accumulating multiple acquisitions.
3 To erase the results of previous acquisitions from the display, press the Clear
Persistence softkey.
The oscilloscope will start to accumulate acquisitions again.
4 To return the oscilloscope to the normal display mode, turn off persistence;
then, press the Clear Persistence softkey.
Turning off persistence does not clear the display. The display is cleared if you
press the Clear Display softkey or if you press the [Auto Scale] key (which also
turns off persistence).
|  |  |
|---|---|

---
**[Page 158]**

Display Settings 8
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 159
For another method of seeing worst-case extremes of varying waveforms, see
“Glitch or Narrow Pulse Capture"on page225.
To clear the display
1 Press [Clear Display] (or press [Display] > Clear Display).
You can also configure the [Quick Action] key to clear the display. See “Configuring
the [Quick Action] Key"on page381.
To select the grid type
When the Video trigger type is selected (see “Video Trigger"on page192), and the
vertical scaling of at least one displayed channel is 140mV/div, the Grid softkey
lets you select from these grid types:
• Full — the normal oscilloscope grid.
• mV — shows vertical grids, labeled on the left, from -0.3V to 0.8V.
• IRE — (Institute of Radio Engineers) shows vertical grids in IRE units, labeled on
the left, from -40 to 100IRE. The 0.35V and 0.7V levels from the mV grid are
also shown and labeled at the right. When the IRE grid is selected, cursor values
are also shown in IRE units. (Cursor values via the remote interface are not in
IRE units.)
The mV and IRE grid values are accurate (and match Y cursor values) when the
vertical scaling is 140mV/division and the vertical offset is 245mV.
To select the grid type:
1 Press the [Display] key; then, press the Grid softkey.
2 In the Grid Menu, press the Grid softkey; then, turn the Entry knob to select
the grid type.
To adjust the grid intensity
To adjust the display grid (graticule) intensity:

---
**[Page 159]**

8 Display Settings
160 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
1 Press the [Display] key; then, press the Grid softkey.
2 In the Grid Menu, press the Grid Intensity softkey; then, turn the Entry knob
to change the intensity of the displayed grid.
The intensity level is shown in the Grid Intensity softkey and is adjustable from 0 to
100%.
Each major vertical division in the grid corresponds to the vertical sensitivity
shown in the status line at the top of the display.
Each major horizontal division in the grid corresponds to the time/div shown in the
status line at the top of the display.
To add an annotation
You can add annotations to the oscilloscope's display. Annotations are useful for
documentation purposes, to add notes before capturing screens.
To add an annotation:
1 On the oscilloscope's front panel, press [Display].
2 In the Display Menu, press Annotations.
3 In the Annotations Menu, press the Display softkey and turn the Entry knob to
select the desired annotation.
4 Then, press the Display softkey again to enable/disable the annotation display.
When enabled, you can drag the annotation anywhere in the graticule using the
touchscreen, a USB mouse, or the X1 and Y1 softkeys.
5 Press Edit.
6 In the Edit keypad dialog, you can enter text using:

---
**[Page 160]**

Display Settings 8
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 161
• The touch screen (when the front panel [Touch] key is lit).
• The Entry knob. Turn the knob to select a key in the dialog; then, push
the Entry knob to enter it.
• A connected USB keyboard.
• A connected USB mouse — you can click anything on the screen that can be
touched.
7 When you are done entering text, select the dialog's Enter or OK key or press
the Edit softkey again.
The annotation text appears in the softkey.
8 Press the Text Color softkey and turn the Entry knob to select the annotation
color.
You can choose white, red, or colors that match analog channels, digital
channels, math waveforms, reference waveforms, or markers.
|  |  |
|---|---|

---
**[Page 161]**

8 Display Settings
162 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
9 Press the Background softkey and turn the Entry knob to select the annotation
background:
• Opaque — the annotation has a solid background.
• Inverted — the annotation's foreground and background colors are switched.
• Transparent — the annotation has a transparent background.
See Also • “To save BMP or PNG image files"on page346
• “To print the oscilloscope's display"on page357
To display waveforms as vectors or dots
Keysight InfiniiVision 6000X-Series oscilloscopes are designed to operate
optimally with vectors (connect the dots) on. This mode produces the most
insightful waveforms for most situations.
|  |
|---|
|  |

---
**[Page 162]**

Display Settings 8
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 163
On the 6GHz bandwidth model, you can disable vectors to view just waveform
data points.
To disable or re-enable vectors:
1 Press the [Display] key; then, press the Waveforms softkey.
2 Press Vectors.
When enabled, Vectors draws a line between consecutive waveform data points.
• Vectors give an analog look to a digitized waveform. Complex analog signals
like video and modulated signals show analog-like intensity information with
vectors on.
• Vectors allow you to see steep edges on waveforms, such as square waves.
• Vectors allow subtle detail of complex waveforms to be viewed, much like an
analog oscilloscope trace, even when the detail is just a small number of pixels
in size.
You may want to turn vectors off when highly complex or multivalued waveforms
are displayed. Turning vectors off may aid the display of multivalued waveforms
such as eye diagrams.
Having vectors on does not slow down the display rate.
Digital channels on a mixed-signal oscilloscope are not affected by the Vectors
setting. They are always displayed with vectors on. They also only contain one
acquisition worth of information.
To disable/enable antialiasing
At slower sweep speeds, the sample rate is reduced and a proprietary display
algorithm is used to minimize the likelihood of aliasing.
By default, Antialiasing is enabled. You should leave Antialiasing enabled unless
there is a specific reason to switch it off.
Anti-aliasing is turned off automatically, even though the Antialiasing softkey
appears to be enabled, when FFTs are on, when the Envelope or Differentiate math
functions are on, or when Jitter analysis is turned on.
If you need to switch Antialiasing off, press [Display] > Waveforms and press the
Antialiasing softkey to switch the feature off. The displayed waveforms will be more
susceptible to aliasing.

---
**[Page 163]**

8 Display Settings
164 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To freeze the display
To freeze the display without stopping running acquisitions, you must configure
the [Quick Action] key. See “Configuring the [Quick Action] Key"on page381.
1 Once the [Quick Action] key has been configured, press it to freeze the display.
2 To un-freeze the display, press [Quick Action] again.
Manual cursors can be used on the frozen display.
Many activities, such as adjusting the trigger level, adjusting vertical or horizontal
settings, or saving data will un-freeze the display.

---
**[Page 164]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
165
9 Labels
To turn the label display on or off / 165
To assign a predefined label to a channel / 166
To define a new label / 167
To load a list of labels from a text file you create / 168
To reset the label library to the factory default / 169
You can define labels and assign them to each analog input channel, or you can
turn labels off to increase the waveform display area. Labels can also be applied to
digital channels on MSO models.
To turn the label display on or off
1 Press the [Label] key on the front panel.
This turns on labels for the displayed analog and digital channels. Labels are
displayed at the left edge of the displayed traces.
The Offset softkey lets you adjust the vertical Y position of the label with respect
to the reference level.
The figure below shows an example of displayed labels.

---
**[Page 165]**

9 Labels
166 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 To turn the labels off, press the [Label] key again.
To assign a predefined label to a channel
1 Press the [Label] key.
2 Press the Channel softkey, then turn the Entry knob or successively press the
Channel softkey to select a channel for label assignment.
|  |  |
|---|---|

---
**[Page 166]**

Labels 9
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 167
The figure above shows the list of channels and their default labels. The
channel does not have to be turned on to have a label assigned to it.
3 Press the Library softkey, then turn the Entry knob or successively press the
Library softkey to select a predefined label from the library.
4 Press the Apply New Label softkey to assign the label to your selected channel.
5 Repeat the above procedure for each predefined label you want to assign to a
channel.
To define a new label
1 Press the [Label] key.
2 Press the Channel softkey; then, turn the Entry knob or successively press the
softkey to select a channel for label assignment.
The channel does not have to be turned on to have a label assigned to it. If the
channel is turned on, its current label will be highlighted.
|  |  |
|---|---|

---
**[Page 167]**

9 Labels
168 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Press the New Label softkey.
4 In the New Label keypad dialog, you can enter text using:
• The touch screen (when the front panel [Touch] key is lit).
• The Entry knob. Turn the knob to select a key in the dialog; then, push
the Entry knob to enter it.
• A connected USB keyboard.
• A connected USB mouse — you can click anything on the screen that can be
touched.
5 When you are done entering text, select the dialog's Enter or OK key or press
the New Label softkey again.
The new label appears in the softkey.
6 Press the Apply New Label softkey to assign the new label to the selected
channel and to save the new label to the Library.
When you define a new label, it is added to the nonvolatile label list.
Label Assignment When you assign a label ending in a digit, such as ADDR0 or DATA0, the
Auto-Increment oscilloscope automatically increments the digit and displays the modified label in
the "New label" field after you press the Apply New Label softkey. Therefore, you
only need to select a new channel and press the Apply New Label softkey again to
assign the label to the channel. Only the original label is saved in the label list. This
feature makes it easier to assign successive labels to numbered control lines and
data bus lines.
To load a list of labels from a text file you create
It may be convenient to create a list of labels using a text editor, then load the
label list into the oscilloscope. The list can have up to 75 labels. When loaded,
labels are added to the beginning of the oscilloscope's list. If more than 75 labels
are loaded, only the first 75 are stored.
To load labels from a text file into the oscilloscope:
1 Use a text editor to create each label. Each label can be up to 32 characters in
length. Separate each label with a line feed.
2 Name the file labellist.txt and save it on a USB mass storage device such as a
thumb drive.

---
**[Page 168]**

Labels 9
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 169
3 Load the list into the oscilloscope using the File Explorer (press [Utility] > File
Explorer).
Label List Management
NOTE
When you press the Library softkey, you will see a list of the last 75 labels used. The list does
not save duplicate labels. Labels can end in any number of trailing digits. As long as the base
string is the same as an existing label in the library, the new label will not be put in the library.
For example, if label A0 is in the library and you make a new label called A12345, the new
label is not added to the library.
When you save a new user-defined label, the new label will replace the oldest label in the list.
Oldest is defined as the longest time since the label was last assigned to a channel. Any time
you assign any label to a channel, that label will move to the newest in the list. Thus, after you
use the label list for a while, your labels will predominate, making it easier to customize the
instrument display for your needs.
When you reset the label library list (see next topic), all of your custom labels will be deleted,
and the label list will be returned to its factory configuration.
To reset the label library to the factory default
Pressing the Reset Library softkey will remove all user-defined labels from the library and set
NOTE
the labels back to the factory default. Once deleted, these user-defined labels cannot be
recovered.
1 Press [Utility] >Options >Preferences.
2 Press the Reset Library softkey.
This will delete all user-defined labels from the library and set the labels in the
library back to the factory default. However, this does not default the labels
currently assigned to the channels (those labels that appear in the waveform
area).
Defaulting labels without erasing the default library
NOTE
Pressing [Default Setup] sets all channel labels back to the default labels but does not erase
the list of user-defined labels in the library.
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |

---
**[Page 169]**

9 Labels
170 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 170]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
171
10 Triggers
Adjusting the Trigger Level / 172
Forcing a Trigger / 173
Edge Trigger / 174
Edge then Edge Trigger / 176
Pulse Width Trigger / 178
Pattern Trigger / 181
OR Trigger / 184
Rise/Fall Time Trigger / 185
Nth Edge Burst Trigger / 187
Runt Trigger / 188
Setup and Hold Trigger / 191
Video Trigger / 192
Serial Trigger / 205
Zone Qualified Trigger / 206
A trigger setup tells the oscilloscope when to acquire and display data. For
example, you can set up to trigger on the rising edge of the analog channel 1 input
signal.
You can adjust the vertical level used for analog channel edge detection by
turning the Trigger Level knob.
In addition to the edge trigger type, you can also set up triggers on rise/fall times,
Nth edge bursts, patterns, pulse widths, runt pulses, setup and hold violations, TV
signals, and serial signals (if option licenses are installed).
You can use any input channel or the “External Trigger Input"on page214 BNC as
the source for most trigger types.

---
**[Page 171]**

10 Triggers
172 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Changes to the trigger setup are applied immediately. If the oscilloscope is
stopped when you change a trigger setup, the oscilloscope uses the new
specification when you press [Run/Stop] or [Single]. If the oscilloscope is running
when you change a trigger setup, it uses the new trigger definition when it starts
the next acquisition.
You can use the [Force Trigger] key to acquire and display data when triggers are
not occurring.
You can use the [Mode/Coupling] key to set options that affect all trigger types (see
Chapter11, “Trigger Mode/Coupling,” starting on page 209).
You can save trigger setups along with the oscilloscope setup (see Chapter21,
“Save/Email/Recall (Setups, Screens, Data),” starting on page 343).
Triggers - General A triggered waveform is one in which the oscilloscope begins tracing (displaying)
Information the waveform, from the left side of the display to the right, each time a particular
trigger condition is met. This provides stable display of periodic signals such as
sine waves and square waves, as well as nonperiodic signals such as serial data
streams.
The figure below shows the conceptual representation of acquisition memory. You
can think of the trigger event as dividing acquisition memory into a pre-trigger
and post-trigger buffer. The position of the trigger event in acquisition memory is
defined by the time reference point and the delay (horizontal position) setting (see
“To adjust the horizontal delay (position)"on page67).
Trigger Event
Pre-Trigger Buffer Post-Trigger Buffer
Acquisition Memory
Adjusting the Trigger Level
You can adjust the trigger level for a selected analog channel by turning the
Trigger Level knob.
| Trigger Event |  |
|---|---|
| Pre-Trigger Buffer | Post-Trigger Buffer |
| Acquisition Memory |  |
|  |  |

---
**[Page 172]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 173
You can also adjust the trigger level using the touchscreen. See “Access the
Trigger Menu, Change the Trigger Mode, and Open the Trigger Level Dialog"on
page57.
You can push the Trigger Level knob to set the level of all displayed analog
channels to the waveform's 50% value. If AC coupling is used, pushing the Trigger
Level knob sets the trigger level to about 0V.
When High and Low (dual) trigger levels are used (as with the Rise/Fall Time and
Runt triggers, for example), pushing the Level knob toggles between high and low
level adjustment.
The position of the trigger level for the analog channel is indicated by the trigger
level icon T (if the analog channel is on) at the far left side of the display. The
value of the analog channel trigger level is displayed in the upper-right corner of
the display.
The trigger level for a selected digital channel is set using the threshold menu in
the Digital Channel Menu. Press the [Digital] key on the front panel, then press the
Thresholds softkey to set the threshold level (TTL, CMOS, ECL, or user defined) for
the selected digital channel group. The threshold value is displayed in the
upper-right corner of the display.
The line trigger level is not adjustable. This trigger is synchronized with the power
line supplied to the oscilloscope.
You can also change the trigger level of all channels by pressing [Analyze] > Features and
NOTE
then selecting Trigger Levels.
Forcing a Trigger
The [Force Trigger] key causes a trigger (on anything) and displays the acquisition.
This key is useful in the Normal trigger mode where acquisitions are made only
when the trigger condition is met. In this mode, if no triggers are occurring (that is,
the "Trig'd?" indicator is displayed), you can press [Force Trigger] to force a trigger
and see what the input signals look like.
In the Auto trigger mode, when the trigger condition is not met, triggers are forced
and the "Auto?" indicator is displayed.
| T |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 173]**

10 Triggers
174 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Edge Trigger
The Edge trigger type identifies a trigger by looking for a specified edge (slope)
and voltage level on a waveform. You can define the trigger source and slope in
this menu. The trigger type, source, and level are displayed in the upper-right
corner of the display.
1 On the front panel, in the Trigger section, press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey, and use the Entry knob to select
Edge.
3 Select the trigger source:
• Analog channel, 1 to the number of channels
• Digital channel (on mixed-signal oscilloscopes), D0 to the number of digital
channels minus one.
• External — triggers on the EXTTRIGIN signal.
• Line — triggers at the 50% level of the rising or falling edge of the AC power
source signal.
• WaveGen 1/2 — triggers at the 50% level of the rising edge of the waveform
generator output signal. (Not available when the DC, Noise, or Cardiac
waveforms are selected.)
• WaveGen Mod (FSK/FM) — when waveform generator FSK or FM modulation is
used, triggers at the 50% level of the rising edge of the modulating signal.
You can choose a channel that is turned off (not displayed) as the source for the
edge trigger.
The selected trigger source is indicated in the upper-right corner of the display
next to the slope symbol:
• 1 through 4 = analog channels.
• D0 through Dn = digital channels.
• E = External trigger input.
• L = Line trigger.
• W = Waveform generator.
4 Press the Slope softkey and select rising edge, falling edge, alternating edges,
or either edge (depending on the selected source). The selected slope is
displayed in the upper-right corner of the display.

---
**[Page 174]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 175
Alternating edge mode is useful when you want to trigger on both edges of a clock (for
NOTE
example, DDR signals).
Either edge mode is useful when you want to trigger on any activity of a selected source.
All modes operate up to the bandwidth of the oscilloscope except Either edge mode, which
has a limitation. Either edge mode will trigger on Constant Wave signals up to 100MHz, but
can trigger on isolated pulses down to 1/(2*oscilloscope's bandwidth).
Using Autoscale to The easiest way to set up an Edge trigger on a waveform is to use Autoscale.
Set Up Edge Simply press the [Auto Scale] key and the oscilloscope will attempt to trigger on the
Triggers waveform using a simple Edge trigger type. See “Use Autoscale"on page33.
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 175]**

10 Triggers
176 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
MegaZoom Technology Simplifies Triggering
NOTE
With the built-in MegaZoom technology, you can simply Autoscale the waveforms, then stop
the oscilloscope to capture a waveform. You can then pan and zoom through the data using
the Horizontal and Vertical knobs to find a stable trigger point. Autoscale often produces a
triggered display.
Edge then Edge Trigger
The Edge then Edge trigger mode triggers when the Nth edge occurs after an
arming edge and a delay period.
The arm and trigger edges can be specified as (Rising) or (Falling) edges on
analog or digital channels.
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Edge then Edge.
| NOTE |
|---|
|  |
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 176]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 177
3 Press the Sources softkey.
4 In the Edge then edge Sources Menu:
a Press the ArmA softkey, and turn the Entry knob to select the channel on
which the arming edge will occur.
b Press the SlopeA softkey to specify which edge of the Arm A signal will arm
the oscilloscope.
c Press the TriggerB softkey, and turn the Entry knob to select the channel on
which the trigger edge will occur.
d Press the SlopeB softkey to specify which edge of the Trigger B signal will
trigger the oscilloscope.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 177]**

10 Triggers
178 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Adjust the trigger level for the selected analog channel by turning the Trigger
Level knob. Press the [Digital] key and select Thresholds to set the threshold level
for digital channels. The value of the trigger level or digital threshold is
displayed in the upper-right corner of the display.
5 Press the Back Back/Up key to return to the Trigger Menu.
6 Press the Delay softkey; then, turn the Entry knob to enter the delay time
between the ArmA edge and the TriggerB edge.
7 Press the NthEdgeB softkey; then, turn the Entry knob to select the Nth edge of
the Trigger B signal to trigger on.
Pulse Width Trigger
Pulse Width (glitch) triggering sets the oscilloscope to trigger on a positive or
negative pulse of a specified width. If you want to trigger on a specific timeout
value, use Pattern trigger in the Trigger Menu (see “Pattern Trigger"on page181).
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Pulse Width.

---
**[Page 178]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 179
3 Press the Source softkey; then, rotate the Entry knob to select a channel source
for the trigger.
The channel you select is shown in the upper-right corner of the display next to
the polarity symbol.
The source can be any analog or digital channel available on your oscilloscope.
4 Adjust the trigger level:
• For analog channels, turn the Trigger Level knob.
• For digital channels, press the [Digital] key and select Thresholds to set the
threshold level.
The value of the trigger level or digital threshold is displayed in the upper-right
corner of the display.
5 Press the pulse polarity softkey to select positive ( ) or negative ( ) polarity
for the pulse width you want to capture.
|  |  |
|---|---|

---
**[Page 179]**

10 Triggers
180 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The selected pulse polarity is displayed in the upper-right corner of the display.
A positive pulse is higher than the current trigger level or threshold and a
negative pulse is lower than the current trigger level or threshold.
When triggering on a positive pulse, the trigger will occur on the high to low
transition of the pulse if the qualifying condition is true. When triggering on a
negative pulse, the trigger will occur on the low to high transition of the pulse if
the qualifying condition is true.
6 Press the qualifier softkey (< > ><) to select the time qualifier.
The Qualifier softkey can set the oscilloscope to trigger on a pulse width that is:
• Less than a time value (<).
For example, for a positive pulse, if you set t<10ns:
10 ns 10 ns Trigger
• Greater than a time value (>).
For example, for a positive pulse, if you set t>10ns:
10 ns 10 ns Trigger
• Within a range of time values (><).
For example, for a positive pulse, if you sett>10ns and t<15ns:
10 ns 15 ns 12 ns Trigger
7 Select the qualifier time set softkey (< or >), then rotate the Entry knob to set
the pulse width qualifier time.
The qualifiers can be set as follows:
• 2ns to 10s for > or < qualifier.
• 10ns to 10s for >< qualifier, with minimum difference of 5ns between upper
and lower settings.
| 10 ns 10 ns Trigger | 10 ns 10 ns Trigger |
|---|---|
| 10 ns 10 ns Trigger | 10 ns 10 ns Trigger |
|---|---|
| 10 ns 15 ns 12 ns Trigger | 10 ns 15 ns 12 ns Trigger |
|---|---|

---
**[Page 180]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 181
Pulse width • When the less than (<) qualifier is selected, the Entry knob sets the oscilloscope
trigger < qualifier to trigger on a pulse width less than the time value displayed on the softkey.
time set softkey
• When the time range (><) qualifier is selected, the Entry knob sets the upper
time range value.
Pulse width • When the greater than (>) qualifier is selected, the Entry knob sets the
trigger > qualifier oscilloscope to trigger on a pulse width greater than the time value displayed
time set softkey on the softkey.
• When the time range (><) qualifier is selected, the Entry knob sets the lower
time range value.
Pattern Trigger
The Pattern trigger identifies a trigger condition by looking for a specified pattern.
This pattern is a logical AND combination of the channels. Each channel can have
a value of 0 (low), 1 (high), or don't care (X). A rising or falling edge can be
specified for one channel included in the pattern.
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Pattern.
3 Press the Qualifier softkey; then, turn the Entry knob to select from the pattern
duration qualifier options:
• Entered – when the pattern is entered.
• < (Less Than) – when the pattern is present for less than a time value.
• > (Greater Than) – when the pattern is present for greater than a time value.
The trigger occurs when the pattern exits (not when the > softkey time value
is exceeded).
• Timeout – when the pattern is present for greater than a time value. In this
case, the trigger occurs when the > softkey time value is exceeded (not when
the pattern exits).
• >< (In Range) – when the pattern is present for a time within a range of values.
• <> (Out of Range) – when the pattern is present for a time outside of range of
values.

---
**[Page 181]**

10 Triggers
182 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Pattern durations are evaluated using a timer. The timer starts on the last edge
that makes the pattern (logical AND) true. Except when the Timeout qualifier is
selected, the trigger occurs on the first edge that makes the pattern false,
provided the time qualifier criteria has been met.
The time values for the selected qualifier are set using the qualifier time set
softkeys (< and >) and the Entry knob.
4 To set the analog or digital channel patterns, press the Analog softkey or the
Digital softkey and use the binary keypad dialog to enter:
• 0 sets the pattern to zero (low) on the selected channel. A low is a voltage
level that is less than the channel's trigger level or threshold level.
• 1 sets the pattern to 1 (high) on the selected channel. A high is a voltage
level that is greater than the channel's trigger level or threshold level.
• X sets the pattern to don't care on the selected channel. Any channel set to
don't care is ignored and is not used as part of the pattern. However, if all
channels in the pattern are set to don't care, the oscilloscope will not trigger.
|  |  |
|---|---|

---
**[Page 182]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 183
• The rising edge ( ) or falling edge ( ) softkey sets the pattern to an edge
on the selected channel. Only one rising or falling edge can be specified in
the pattern. When an edge is specified, the oscilloscope will trigger at the
edge specified if the pattern set for the other channels is true.
If no edge is specified, the oscilloscope will trigger on the last edge that
makes the pattern true.
Specifying an Edge in a Pattern
NOTE
You are allowed to specify only one rising or falling edge term in the pattern. If you define an
edge term, then select a different channel in the pattern and define another edge term, the
previous edge definition is changed to a don't care.
You can also specify patterns for digital channels using the Bus1 and Bus2
softkeys and entering hexadecimal values. See “Hex Bus Pattern Trigger"on
page183.
The specified pattern is shown in the "Pattern=" line directly above the
softkeys.
5 Adjust the trigger levels for analog and digital channels by using the softkeys in
the Analyze Menu after pressing [Analyze] > Features and selecting Trigger Levels.
You can also set the threshold levels for digital channels by pressing [Digital] >
Thresholds.
Hex Bus Pattern Trigger
You can specify a bus value on which to trigger. To do this, first define the bus. See
“To display digital channels as a bus"on page140 for details. You can trigger on
a bus value whether you are displaying the bus or not.
To trigger on a bus value:
1 Select the pattern trigger type and qualifier as described in “Pattern
Trigger"on page181.
2 Press the Bus1 or Bus2 softkey and use the hex keypad dialog to enter nibble
(hex character) values.
|  |  |
|---|---|
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 183]**

10 Triggers
184 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If a digit is made up of less than four bits, the value of the digit is limited to the greatest
NOTE
number that can be represented by the number of bits.
When a hex bus digit contains one or more don't care (X) bits and one or more bits
with a value or 0 or 1, the "$" sign will be displayed for the digit.
For information regarding digital bus display when Pattern triggering see “Bus
values are displayed when using Pattern trigger"on page142.
OR Trigger
The OR trigger mode triggers when any one (or more) of the specified edges on
analog or digital channels is found.
1 On the front panel, in the Trigger section, press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey, and use the Entry knob to select
OR.
3 Press the Slope softkey and select rising edge, falling edge, either edge, or don't
care. The selected slope is displayed in the upper-right corner of the display.
4 For each analog or digital channel you want to include in the OR trigger, press
the Channel softkey to select the channel.
As you press the Channel softkey (or rotate the Entry knob), the channel you
select is highlighted in the OR= line directly above the softkeys and in the
upper-right corner of the display next to the OR gate symbol.
Adjust the trigger level for the selected analog channel by turning the Trigger
Level knob. Press the [Digital] key and select Thresholds to set the threshold level
for digital channels. The value of the trigger level or digital threshold is
displayed in the upper-right corner of the display.
5 For each channel you select, press the Slope softkey and select (Rising),
(Falling), (Either), or X (Don't Care). The selected slope is displayed above the
softkeys.
| NOTE |
|---|
|  |
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 184]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 185
If all channels in the OR trigger are set to don't care, the oscilloscope will not
trigger.
6 To set all analog and digital channels to the edge selected by the Slope softkey,
press the Set all Edges softkey.
Rise/Fall Time Trigger
The Rise/Fall Time trigger looks for a rising or falling transition from one level to
another level in greater than or less than a certain amount of time.
|  |  |
|---|---|

---
**[Page 185]**

10 Triggers
186 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
High level
Low level
Rising edge time Falling edge time
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Rise/Fall Time.
3 Press the Source softkey, and turn the Entry knob to select the input channel
source.
4 Press the Rising Edge or Falling Edge softkey to toggle between edge types.
| High level
Low level
Rising edge time Falling edge time |
|---|
|  |
|  |  |  |
|---|---|---|
|  |  |
|---|---|

---
**[Page 186]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 187
5 Press the LevelSelect softkey to select High; then, turn the Trigger Level knob to
adjust the high level.
6 Press the LevelSelect softkey to select Low; then, turn the Trigger Level knob to
adjust the low level.
You can also push the Trigger Level knob to toggle between High and Low
selection.
7 Press the Qualifier softkey to toggle between "greater than" or "less than".
8 Press the Time softkey, and turn the Entry knob to select the time.
Nth Edge Burst Trigger
The Nth Edge Burst trigger lets you trigger on the Nth edge of a burst that occurs
after an idle time.
Nth Edge Burst trigger set up consists of selecting the source, the slope of the
edge, the idle time, and the number of the edge:
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Nth Edge Burst.
|  |
|---|
|  |

---
**[Page 187]**

10 Triggers
188 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Press the Source softkey, and turn the Entry knob to select the input channel
source.
4 Press the Slope softkey to specify the slope of the edge.
5 Press the Idle softkey; then, turn the Entry knob to specify the idle time.
6 Press the Edge softkey; then, turn the Entry knob to which edge number to
trigger on.
Runt Trigger
The Runt trigger looks for pulses that cross one threshold but not another.
|  |  |
|---|---|

---
**[Page 188]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 189
High level
Low level
Positive runt pulse Negative runt pulse
• A positive runt pulse crosses through a lower threshold but not an upper
threshold.
• A negative runt pulse crosses through an upper threshold but not a lower
threshold.
To trigger on runt pulses:
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Runt.
| High level
Low level
Positive runt pulse Negative runt pulse |
|---|
|  |
|  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |

---
**[Page 189]**

10 Triggers
190 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Press the Source softkey, and turn the Entry knob to select the input channel
source.
4 Press the Positive, Negative, or Either Runt Pulse softkey to toggle between pulse
types.
5 Press the LevelSelect softkey to select High; then, turn the Trigger Level knob to
adjust the high level.
6 Press the LevelSelect softkey to select Low; then, turn the Trigger Level knob to
adjust the low level.
You can also push the Trigger Level knob to toggle between High and Low
selection.
7 Press the Qualifier softkey to toggle between "less than", "greater than", or
None.
This lets you specify that a runt pulse be less than or greater than a certain
width.
8 If you selected the "less than" or "greater than" Qualifier, press the Time softkey;
then, turn the Entry knob to select the time.
|  |  |
|---|---|

---
**[Page 190]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 191
Setup and Hold Trigger
The Setup and Hold trigger looks for setup and hold violations.
Data
Clock
(rising
edge)
Setup time Hold time
One oscilloscope channel probes the clock signal and another channel probes the
data signal.
To trigger on setup and hold violations:
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Setup and Hold.
3 Press the Clock softkey; then, turn the Entry knob to select the input channel
with the clock signal.
4 Set the appropriate trigger level for the clock signal using the Trigger Level
knob.
5 Press the Rising Edge or Falling Edge softkey to specify the clock edge being used.
6 Press the Data softkey; then, turn the Entry knob to select the input channel
with the data signal.
7 Set the appropriate trigger level for the data signal using the Trigger Level
knob.
8 Press the <Setup softkey, and turn the Entry knob to select the setup time.
| Data
Clock
(rising
edge)
Setup time Hold time |
|---|
|  |

---
**[Page 191]**

10 Triggers
192 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
9 Press the <Hold softkey, and turn the Entry knob to select the hold time.
Video Trigger
Video triggering can be used to capture the complicated waveforms of most
standard analog video signals. The trigger circuitry detects the vertical and
horizontal interval of the waveform and produces triggers based on the video
trigger settings you have selected.
The oscilloscope's MegaZoomIV technology gives you bright, easily viewed
displays of any part of the video waveform. Analysis of video waveforms is
simplified by the oscilloscope's ability to trigger on any selected line of the video
signal.
It is important, when using a 10:1 passive probe, that the probe is correctly compensated. The
NOTE
oscilloscope is sensitive to this and will not trigger if the probe is not properly compensated,
especially for progressive formats.
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 192]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 193
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Video.
3 Press the Source softkey and select any analog channel as the video trigger
source.
The selected trigger source is displayed in the upper-right corner of the display.
Turning the Trigger Level knob does not change the trigger level because the
trigger level is automatically set to the sync pulse. Trigger coupling is
automatically set to TV in the Trigger Mode and Coupling Menu.
Provide Correct Matching
NOTE
Many video signals are produced from 75Ω sources. To provide correct matching to these
sources, a 75Ω terminator (such as a Keysight 11094B) should be connected to the
oscilloscope input.
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 193]**

10 Triggers
194 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
4 Press the sync polarity softkey to set the Video trigger to either positive ( ) or
negative ( ) sync polarity.
5 Press the Settings softkey.
6 In the Video Trigger Menu, press the Standard softkey to set the video standard.
The oscilloscope supports triggering on the following television (TV) and video
standards.
Standard Type Sync Pulse
NTSC Interlaced Bi-level
PAL Interlaced Bi-level
PAL-M Interlaced Bi-level
SECAM Interlaced Bi-level
With the DSOX6VID extended video triggering license, the oscilloscope
additionally supports these standards:
|  |  |
|---|---|
| Standard | Type | Sync Pulse |
|---|---|---|
| NTSC | Interlaced | Bi-level |
| PAL | Interlaced | Bi-level |
| PAL-M | Interlaced | Bi-level |
| SECAM | Interlaced | Bi-level |

---
**[Page 194]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 195
Standard Type Sync Pulse
Generic Interlaced/Progressive Bi-level/Tri-level
EDTV 480p/60 Progressive Bi-level
EDTV 567p/50 Progressive Bi-level
HDTV 720p/50 Progressive Tri-level
HDTV 720p/60 Progressive Tri-level
HDTV 1080p/24 Progressive Tri-level
HDTV 1080p/25 Progressive Tri-level
HDTV 1080p/30 Progressive Tri-level
HDTV 1080p/50 Progressive Tri-level
HDTV 1080p/60 Progressive Tri-level
HDTV 1080i/50 Interlaced Tri-level
HDTV 1080i/60 Interlaced Tri-level
The Generic selection lets you trigger on custom bi-level and tri-level sync video
standards. See “To set up Generic video triggers"on page197.
7 Press the AutoSetup softkey to automatically set up the oscilloscope for the
selected Source and Standard:
• Source channel vertical scaling is set to 140mV/div.
• Source channel offset is set to 245mV.
• Source channel is turned on.
• Trigger type is set to Video.
• Video trigger mode is set to All Lines (but left unchanged if Standard is
Generic).
• Display Grid type is set to IRE (when Standard is NTSC) or mV (see “To select
the grid type"on page159).
• Horizontal time/division is set to 10µs/div for NTSC/PAL/SECAM standards
or 4µs/div for EDTV or HDTV standards (unchanged for Generic).
• Horizontal delay is set so that trigger is at first horizontal division from the
left (unchanged for Generic).
| Standard | Type | Sync Pulse |
|---|---|---|
| Generic | Interlaced/Progressive | Bi-level/Tri-level |
| EDTV 480p/60 | Progressive | Bi-level |
| EDTV 567p/50 | Progressive | Bi-level |
| HDTV 720p/50 | Progressive | Tri-level |
| HDTV 720p/60 | Progressive | Tri-level |
| HDTV 1080p/24 | Progressive | Tri-level |
| HDTV 1080p/25 | Progressive | Tri-level |
| HDTV 1080p/30 | Progressive | Tri-level |
| HDTV 1080p/50 | Progressive | Tri-level |
| HDTV 1080p/60 | Progressive | Tri-level |
| HDTV 1080i/50 | Interlaced | Tri-level |
| HDTV 1080i/60 | Interlaced | Tri-level |

---
**[Page 195]**

10 Triggers
196 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You can also press [Analyze]> Features and then select Video to quickly access the
video triggering automatic set up and display options.
8 Press the Mode softkey to select the portion of the video signal that you would
like to trigger on.
The Video trigger modes available are:
• Field1 and Field2 — Trigger on the rising edge of the first serration pulse of
field 1 or field 2 (interlaced standards only).
• All Fields — Trigger on the rising edge of the first pulse in the vertical sync
interval.
• All Lines — Trigger on all horizontal sync pulses.
• Line — Trigger on the selected line number (EDTV and HDTV standards only).
• Line: Field1 and Line:Field2 — Trigger on the selected line # in field 1 or field 2
(interlaced standards only).
• Line: Alternate — Alternately trigger on the selected line # in field 1 and field 2
(NTSC, PAL, PAL-M, and SECAM only).
9 If you select a line # mode, press the Line # softkey, then rotate the Entry knob
to select the line number on which you want to trigger.
The following table lists the line (or count) numbers per field for each video
standard.
Video standard Field 1 Field 2 Alt Field
NTSC 1 to 263 1 to 262 1 to 262
PAL 1 to 313 314 to 625 1 to 312
PAL-M 1 to 263 264 to 525 1 to 262
SECAM 1 to 313 314 to 625 1 to 312
The following table lists the line numbers for each EDTV/HDTV video standard
(available with the DSOX6VID extended video triggering license).
| Video standard | Field 1 | Field 2 | Alt Field |
|---|---|---|---|
| NTSC | 1 to 263 | 1 to 262 | 1 to 262 |
| PAL | 1 to 313 | 314 to 625 | 1 to 312 |
| PAL-M | 1 to 263 | 264 to 525 | 1 to 262 |
| SECAM | 1 to 313 | 314 to 625 | 1 to 312 |

---
**[Page 196]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 197
EDTV 480p/60 1 to 525
EDTV 567p/50 1 to 625
HDTV 720p/50, 720p/60 1 to 750
HDTV 1080p/24, 1080p/25, 1080p/30, 1 to 1125
1080p/50, 1080p/60
HDTV 1080i/50, 1080i/60 1 to 1125
Video Triggering The following are exercises to familiarize you with video triggering. These exercises
Examples use the NTSC video standard.
• “To trigger on a specific line of video"on page198
• “To trigger on all sync pulses"on page199
• “To trigger on a specific field of the video signal"on page200
• “To trigger on all fields of the video signal"on page201
• “To trigger on odd or even fields"on page202
To set up Generic video triggers
When Generic (available with the DSOX6VID extended video triggering license) is
selected as the Video trigger Standard, you can trigger on custom bi-level and
tri-level sync video standards. The Video Trigger Menu changes as follows.
1 Press the Time> softkey; then, turn the Entry knob to set the time to
greater-than the sync-pulse width so that the oscilloscope synchronizes to the
vertical sync.
2 Press the Edge# softkey; then, turn the Entry knob to select the Nth edge after
after vertical sync to trigger on.
3 To enable or disable the horizontal sync control, press the first HorizSync
softkey.
| EDTV 480p/60 | 1 to 525 |
|---|---|
| EDTV 567p/50 | 1 to 625 |
| HDTV 720p/50, 720p/60 | 1 to 750 |
| HDTV 1080p/24, 1080p/25, 1080p/30,
1080p/50, 1080p/60 | 1 to 1125 |
| HDTV 1080i/50, 1080i/60 | 1 to 1125 |
|  |
|---|
|  |

---
**[Page 197]**

10 Triggers
198 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• For interleaved video, enabling the HorizSync control and setting the
HorizSync adjustment to the sync time of the probed video signal allows the
Edge# function to count only lines and not double count during equalization.
Additionally, the FieldHoldoff can be adjusted so that the oscilloscope
triggers once per frame.
• Similarly, for progressive video with a tri-level sync, enabling the HorizSync
control and setting the HorizSync adjustment to the sync time of the probed
video signal allows the Edge# function to count only lines and not double
count during vertical sync.
When the horizontal sync control is enabled, press the second HorizSync
softkey; then, turn the Entry knob to set the minimum time the horizontal sync
pulse must be present to be considered valid.
To trigger on a specific line of video
Video triggering requires greater than 1/2 division of sync amplitude with any
analog channel as the trigger source. Turning the trigger Level knob in Video
trigger does not change the trigger level because the trigger level is automatically
set to the sync pulse tips.
One example of triggering on a specific line of video is looking at the vertical
interval test signals (VITS), which are typically in line 18. Another example is
closed captioning, which is typically in line 21.
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Video.
3 Press the Settings softkey, then press the Standard softkey to select the
appropriate TV standard (NTSC).
4 Press the Mode softkey and select the TV field of the line you want to trigger on.
You can choose Line:Field1, Line:Field2, or Line:Alternate.
5 Press the Line # softkey and select the number of the line you want to examine.
Alternate Triggering
NOTE
If Line:Alternateis selected, the oscilloscope will alternately trigger on the selected line
number in Field 1 and Field 2. This is a quick way to compare the Field 1 VITS and Field 2 VITS
or to check for the correct insertion of the half line at the end of Field1.
| NOTE |
|---|
|  |

---
**[Page 198]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 199
Figure 28 Example: Triggering on Line 136
To trigger on all sync pulses
To quickly find maximum video levels, you could trigger on all sync pulses. When
All Lines is selected as the Video trigger mode, the oscilloscope will trigger on all
horizontal sync pulses.
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Video.
3 Press the Settings softkey, then press the Standard softkey to select the
appropriate TV standard.
4 Press the Mode softkey and select All Lines.
|  |
|---|
|  |

---
**[Page 199]**

10 Triggers
200 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 29 Triggering on All Lines
To trigger on a specific field of the video signal
To examine the components of a video signal, trigger on either Field 1 or Field 2
(available for interleaved standards). When a specific field is selected, the
oscilloscope triggers on the rising edge of the first serration pulse in the vertical
sync interval in the specified field (1 or 2).
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Video.
3 Press the Settings softkey, then press the Standard softkey to select the
appropriate TV standard.
4 Press the Mode softkey and select Field1 or Field2.
|  |
|---|
|  |

---
**[Page 200]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 201
Figure 30 Triggering on Field 1
To trigger on all fields of the video signal
To quickly and easily view transitions between fields, or to find the amplitude
differences between the fields, use the All Fields trigger mode.
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Video.
3 Press the Settings softkey, then press the Standard softkey to select the
appropriate TV standard.
4 Press the Mode softkey and select All Fields.
|  |
|---|
|  |

---
**[Page 201]**

10 Triggers
202 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 31 Triggering on All Fields
To trigger on odd or even fields
To check the envelope of your video signals, or to measure worst case distortion,
trigger on the odd or even fields. When Field 1 is selected, the oscilloscope
triggers on color fields 1 or 3. When Field 2 is selected, the oscilloscope triggers
on color fields 2 or 4.
1 Press the [Trigger] key.
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select Video.
3 Press the Settings softkey, then press the Standard softkey to select the
appropriate TV standard.
4 Press the Mode softkey and select Field1 or Field2.
|  |
|---|
|  |

---
**[Page 202]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 203
The trigger circuits look for the position of the start of Vertical Sync to determine
the field. But this definition of field does not take into consideration the phase of
the reference subcarrier. When Field 1 is selected, the trigger system will find any
field where the vertical sync starts on Line 4. In the case of NTSC video, the
oscilloscope will trigger on color field 1 alternating with color field 3 (see the
following figure). This setup can be used to measure the envelope of the reference
burst.
Figure 32 Triggering on Color Field 1 Alternating with Color Field 3
If a more detailed analysis is required, then only one color field should be selected
to be the trigger. You can do this by using the FieldHoldoff softkey in the Video
Trigger Menu. Press the FieldHoldoff softkey and use the Entry knob to adjust the
holdoff in half-field increments until the oscilloscope triggers on only one phase of
the color burst.
A quick way to synchronize to the other phase is to briefly disconnect the signal
and then reconnect it. Repeat until the correct phase is displayed.
|  |
|---|
|  |

---
**[Page 203]**

10 Triggers
204 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
When holdoff is adjusted using the FieldHoldoff softkey and the Entry knob, the
corresponding holdoff time will be displayed in the Trigger Mode and Coupling
Menu.
Table 3 Half-field holdoff time
Standard Time
NTSC 8.35ms
PAL 10ms
PAL-M 10ms
SECAM 10ms
Generic 8.35ms
EDTV 480p/60 8.35ms
EDTV 567p/50 10ms
HDTV 720p/50 10ms
HDTV 720p/60 8.35ms
HDTV 1080p/24 20.835ms
HDTV 1080p/25 20ms
HDTV 1080p/30 20ms
HDTV 1080p/50 16.67ms
HDTV 1080p/60 8.36ms
HDTV 1080i/50 10ms
HDTV 1080i/60 8.35ms
| Standard | Time |
|---|---|
| NTSC | 8.35ms |
| PAL | 10ms |
| PAL-M | 10ms |
| SECAM | 10ms |
| Generic | 8.35ms |
| EDTV 480p/60 | 8.35ms |
| EDTV 567p/50 | 10ms |
| HDTV 720p/50 | 10ms |
| HDTV 720p/60 | 8.35ms |
| HDTV 1080p/24 | 20.835ms |
| HDTV 1080p/25 | 20ms |
| HDTV 1080p/30 | 20ms |
| HDTV 1080p/50 | 16.67ms |
| HDTV 1080p/60 | 8.36ms |
| HDTV 1080i/50 | 10ms |
| HDTV 1080i/60 | 8.35ms |

---
**[Page 204]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 205
Figure 33 Using Field Holdoff to Synchronize to Color Field 1 or 3 (Field 1 mode)
Serial Trigger
With serial decode option licenses (see “Serial Decode Options"on page149),
you can enable serial trigger types. To set up these triggers, see:
• “ARINC429 Triggering"on page489
• “CAN/CAN FD Triggering"on page423
• “FlexRay Triggering"on page442
• “I2C Triggering"on page452
• “I2S Triggering"on page474
• “LIN Triggering"on page434
• “MIL-STD-1553 Triggering"on page483
• “SENT Triggering"on page502
|  |
|---|
|  |

---
**[Page 205]**

10 Triggers
206 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• “SPI Triggering"on page464
• “UART/RS232 Triggering"on page513
• “USB 2.0 Triggering"on page523
Zone Qualified Trigger
The zone qualified trigger feature gives you one or two rectangular areas, Zone 1
and Zone 2, that a waveform must either intersect or not intersect in order for an
acquisition to be displayed and stored in memory.
The zone qualified trigger feature works on top of the oscilloscope's hardware
trigger, which determines the acquisitions whose waveforms are evaluated for
zone intersection.
To set up a zone qualified trigger:
1 Touch the upper-right corner to select the rectangle draw mode.
2 Drag your finger (or connected USB mouse pointer) across the screen to draw a
rectangular zone that the waveform must either intersect or not intersect.
3 Take your finger off the screen (or release the mouse button).
4 In the popup menu, select whether the rectangle is Zone1 or Zone2 and
whether it is a "Must Intersect" or "Must Not Intersect" zone.
|  |  |
|---|---|

---
**[Page 206]**

Triggers 10
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 207
The [Zone] key becomes lit to show the zone qualified trigger feature is enabled.
5 In the Zone Qualified Trigger Menu, press the Source softkey and select the
analog channel input source that both zones are associated with.
Zone colors match the selected analog input channel. "Must Not Intersect"
zones are shaded differently than the solid "Must Intersect" zones.
The zone qualified trigger source does not have to be the same as the hardware
trigger source.
6 You can use the Zone1On and Zone2On softkeys to disable or enable zones,
and you can use the Zone1 and Zone2 softkeys to toggle between the "Must
Intersect" and "Must Not Intersect" conditions.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 207]**

10 Triggers
208 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Disabling both zones disables the zone qualified trigger feature. When the zone
qualified trigger feature is enabled, at least one zone must be enabled.
You can press the [Zone] key to disable or re-enable the zone qualified trigger.
When two non-overlapping zones are used, their conditions are ANDed to become
the final qualifying condition.
When two overlapping zones have the must intersect condition, the zones are
ORed. When two overlapping zones have different conditions, Zone 1 takes
precedence and Zone 2 is not used. In this case, Zone 2 will have no fill (that is,
neither solid nor shaded) to indicate that it is not being used.
The zone qualified trigger feature is incompatible with, and will disable, the XY and
Roll horizontal time modes and the Averaging acquisition mode.
Keep in mind that the TRIG OUT signal comes from the oscilloscope's hardware trigger. The
NOTE
TRIG OUT signal indicates when there is a trigger (acquisition) that is evaluated for zone
intersection, not when an acquisition meets the zone qualification and is plotted on the
oscilloscope's display.
| NOTE |
|---|
|  |

---
**[Page 208]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
209
11 Trigger Mode/Coupling
To select the Auto or Normal trigger mode / 210
To select the trigger coupling / 211
To enable or disable trigger noise rejection / 213
To enable or disable trigger HF Reject / 213
To set the trigger holdoff / 214
External Trigger Input / 214
To access the Trigger Mode and Coupling Menu:
• In the Trigger section of the front panel, press the [Mode/Coupling] key.
Noisy Signals If the signal you are probing is noisy, you can set up the oscilloscope to reduce the
noise in the trigger path and on the displayed waveform. First, stabilize the
displayed waveform by removing the noise from the trigger path. Second, reduce
the noise on the displayed waveform.
1 Connect a signal to the oscilloscope and obtain a stable display.
2 Remove the noise from the trigger path by turning on high-frequency rejection
(“To enable or disable trigger HF Reject"on page213), low-frequency
rejection (“To select the trigger coupling"on page211), or “To enable or
disable trigger noise rejection"on page213.
3 Use “Averaging Acquisition Mode"on page227 to reduce noise on the
displayed waveform.
|  |  |
|---|---|

---
**[Page 209]**

11 Trigger Mode/Coupling
210 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To select the Auto or Normal trigger mode
When the oscilloscope is running, the trigger mode tells the oscilloscope what to
do when triggers are not occurring.
In the Auto trigger mode (the default setting), if the specified trigger conditions are
not found, triggers are forced and acquisitions are made so that signal activity is
displayed on the oscilloscope.
In the Normal trigger mode, triggers and acquisitions only occur when the
specified trigger conditions are found.
To select the trigger mode:
1 Press the [Mode/Coupling] key.
2 In the Trigger Mode and Coupling Menu, press the Mode softkey; then select
either Auto or Normal.
You can also make this selection using the touchscreen. See “Access the
Trigger Menu, Change the Trigger Mode, and Open the Trigger Level
Dialog"on page57.
See the following “When to Use Auto Trigger Mode"on page211 and “When
to Use Normal Trigger Mode"on page211 descriptions.
You can also configure the [Quick Action] key to toggle between the Auto and
Normal trigger modes. See “Configuring the [Quick Action] Key"on page381.
Triggering and the After the oscilloscope starts running (after pressing [Run] or [Single] or changing
Pre- and the trigger condition), the oscilloscope first fills the pre-trigger buffer. Then, after
Post-Trigger the pre-trigger buffer is filled, the oscilloscope starts searching for a trigger, and
Buffers sampled data continues to flow data through the pre-trigger buffer in a first-in
first-out (FIFO) manner.
When a trigger is found, the pre-trigger buffer contains the events that occurred
just before the trigger. Then, the oscilloscope fills the post-trigger buffer and
displays the acquisition memory. If the acquisition was initiated by [Run/Stop], the
process repeats. If the acquisition was initiated by pressing [Single], the acquisition
stops (and you can Pan and Zoom the waveform).
In either Auto or Normal trigger mode, a trigger may be missed if the event occurs
while the pre-trigger buffer is being filled. This may be more likely, for example,
when the horizontal scale knob is set to a slow time/div setting, such as
500ms/div.

---
**[Page 210]**

Trigger Mode/Coupling 11
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 211
Trigger Indicator The trigger indicator at the top right of the display shows whether triggers are
occurring.
In the Auto trigger mode, the trigger indicator can show:
• Auto?— the trigger condition is not found (after the pre-trigger buffer has filled),
and forced triggers and acquisitions are occurring.
• Auto — the trigger condition is found (or the pre-trigger buffer is being filled).
In the Normal trigger mode, the trigger indicator can show:
• Trig'd?— the trigger condition is not found (after the pre-trigger buffer has
filled), and no acquisitions are occurring.
• Trig'd— trigger condition is found (or pre-trigger buffer is being filled).
When the oscilloscope is not running, the trigger indicator area shows Stop.
When to Use Auto The Auto trigger mode is appropriate when:
Trigger Mode
• Checking DC signals or signals with unknown levels or activity.
• When trigger conditions occur often enough that forced triggers are
unnecessary.
When to Use The Normal trigger mode is appropriate when:
Normal Trigger
• You only want to acquire specific events specified by the trigger settings.
Mode
• Triggering on an infrequent signal from a serial bus (for example, I2C, SPI, CAN,
LIN, etc.) or another signal that arrives in bursts. The Normal trigger mode lets
you stabilize the display by preventing the oscilloscope from auto-triggering.
• Making single-shot acquisitions with the [Single] key.
Often with single-shot acquisitions, you must initiate some action in the device
under test, and you don't want the oscilloscope to auto-trigger before that
happens. Before initiating the action in the circuit, wait for the trigger condition
indicator Trig'd? to display (this tells you the pre-trigger buffer is filled).
See Also • “Forcing a Trigger"on page173
• “To set the trigger holdoff"on page214
• “To position the time reference (left, center, right)"on page75
To select the trigger coupling
1 Press the [Mode/Coupling] key.

---
**[Page 211]**

11 Trigger Mode/Coupling
212 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 In the Trigger Mode and Coupling Menu, press the Coupling softkey; then, turn
the Entry knob to select:
• DC coupling — allows DC and AC signals into the trigger path.
• AC coupling — places a 10Hz high-pass filter in the trigger path removing
any DC offset voltage from the trigger waveform.
The high-pass filter in the External Trigger input path is 50Hz for all models.
Use AC coupling to get a stable edge trigger when your waveform has a
large DC offset.
• LF (low frequency) Reject coupling — adds a high-pass filter with the 3-dB
point at 50kHz in series with the trigger waveform.
0 dB
3 dB down point
Pass
Band
DC 50 kHz
Low frequency reject removes any unwanted low frequency components
from a trigger waveform, such as power line frequencies, etc., that can
interfere with proper triggering.
Use LF Reject coupling to get a stable edge trigger when your waveform has
low frequency noise.
• Video coupling — is normally grayed-out, but is automatically selected when
Video trigger is enabled in the Trigger Menu.
Note that Trigger Coupling is independent of Channel Coupling (see “To specify
channel coupling"on page84).

---
**[Page 212]**

Trigger Mode/Coupling 11
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 213
To enable or disable trigger noise rejection
Noise Rej adds additional hysteresis to the trigger circuitry. By increasing the
trigger hysteresis band, you reduce the possibility of triggering on noise. However,
this also decreases the trigger sensitivity so that a slightly larger signal is required
to trigger the oscilloscope.
1 Press the [Mode/Coupling] key.
2 In the Trigger Mode and Coupling Menu, press the Noise Rej softkey to enable or
disable.
To enable or disable trigger HF Reject
HF Reject adds a 50kHz low-pass filter in the trigger path to remove high
frequency components from the trigger waveform.
0 dB
-3 dB
Pass
Band
DC 50 kHz
You can use HF Reject to remove high-frequency noise, such as AM or FM
broadcast stations or noise from fast system clocks, from the trigger path.
1 Press the [Mode/Coupling] key.
2 In the Trigger Mode and Coupling Menu, press the HF Reject softkey to enable
or disable.
| 0 dB | Pass
Band |
|---|---|

---
**[Page 213]**

11 Trigger Mode/Coupling
214 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To set the trigger holdoff
Trigger holdoff sets the amount of time the oscilloscope waits after a trigger
before re-arming the trigger circuitry.
Use the holdoff to trigger on repetitive waveforms that have multiple edges (or
other events) between waveform repetitions. You can also use holdoff to trigger on
the first edge of a burst when you know the minimum time between bursts.
For example, to get a stable trigger on the repetitive pulse burst shown below, set
the holdoff time to be >200ns but <600ns.
Holdoff Oscilloscope triggers here
200 ns 600 ns
To set the trigger holdoff:
1 Press the [Mode/Coupling] key.
2 In the Trigger Mode and Coupling Menu, press the Holdoff softkey; then, turn
the Entry knob to increase or decrease the trigger holdoff time.
Trigger Holdoff The correct holdoff setting is typically slightly less than one repetition of the
Operating Hints waveform. Set the holdoff to this time to generate a unique trigger point for a
repetitive waveform.
Changing the time base settings does not affect the trigger holdoff time.
With Keysight's MegaZoom technology, you can press [Stop], then pan and zoom
through the data to find where the waveform repeats. Measure this time using
cursors; then, set the holdoff.
External Trigger Input
The external trigger input can be used as a source in several of the trigger types.
The external trigger BNC input is labeled EXTTRIGIN.
| Holdoff Oscilloscope triggers here
200 ns 600 ns |
|---|
|  |
|  |  |
|---|---|

---
**[Page 214]**

Trigger Mode/Coupling 11
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 215
Maximum voltage at oscilloscope external trigger input
CAUTION
300Vrms, 400Vpk; transient overvoltage 1.6kVpk
1Mohm input: For steady-state sinusoidal waveforms derate at 20dB/decade above
100kHz to a minimum of 5Vpk
The external trigger input impedance is 1MOhm. This lets you use passive probes
for general-purpose measurements. The higher impedance minimizes the loading
effect of the oscilloscope on the device under test.
To set the EXTTRIGIN units and probe attenuation:
1 Press the [Mode/Coupling] key in the Trigger section of the front panel.
2 In the Trigger Mode and Coupling Menu, press the External softkey.
3 In the External Trigger Menu, press the Units softkey to select between:
• Volts — for a voltage probe.
• Amps — for a current probe.
Measurement results, channel sensitivity, and the trigger level will reflect the
measurement units you have selected.
4 Press the Probe softkey; then, turn the Entry knob to specify the probe
attenuation.
The attenuation factor can be set from 0.1:1 to 10000:1 in a 1-2-5 sequence.
The probe attenuation factor must be set properly for measurements to be
made correctly.
5 Press the Range softkey; then, turn the Entry knob to set the External Trigger
input signal range.
The range is either 1.6V or 8V when you are using a 1:1 probe.
| CAUTION |
|---|
|  |
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 215]**

11 Trigger Mode/Coupling
216 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The range is automatically recalculated when a different External Trigger probe
attenuation factor is chosen.

---
**[Page 216]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
217
12 Acquisition Control
Running, Stopping, and Making Single Acquisitions (Run Control) / 217
Overview of Sampling / 218
Selecting the Acquisition Mode / 223
Data Acquisition (Sampling) Mode / 230
Acquiring to Segmented Memory / 232
This chapter shows how to use the oscilloscope's acquisition and run controls.
Running, Stopping, and Making Single Acquisitions (Run Control)
There are two front panel keys for starting and stopping the oscilloscope's
acquisition system: [Run/Stop] and [Single].
• When the [Run/Stop] key is green, the oscilloscope is running, that is, acquiring
data when trigger conditions are met.
To stop acquiring data, press [Run/Stop]. When stopped, the last acquired
waveform is displayed.
• When the [Run/Stop] key is red, data acquisition is stopped.
"Stop" is displayed next to the trigger type in the status line at the top of the
display.
To start acquiring data, press [Run/Stop].
• To capture and display a single acquisition (whether the oscilloscope is running
or stopped), press [Single].

---
**[Page 217]**

12 Acquisition Control
218 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The [Single] run control lets you view single-shot events without subsequent
waveform data overwriting the display. Use [Single] when you want maximum
memory depth for pan and zoom.
When you press [Single], the trigger mode is temporarily set to Normal (to keep
the oscilloscope from auto-triggering immediately), the trigger circuitry is
armed, the [Single] key is illuminated, and the oscilloscope waits until a trigger
condition occurs before it displays a waveform.
When the oscilloscope triggers, the single acquisition is displayed and the
oscilloscope is stopped (the [Run/Stop] key is illuminated in red). Press [Single]
again to acquire another waveform.
If the oscilloscope doesn't trigger, you can press the [Force Trigger] key to trigger
on anything and make a single acquisition.
To display the results of multiple acquisitions, use persistence. See “To set or
clear persistence"on page157.
Single vs. Running Data record lengths are usually different for single and running acquisitions:
and Record Length
• Single — Single acquisitions use the maximum memory available — usually twice
as much as acquisitions captured when running. At slower time/div settings,
because there is more memory available for a single acquisition, the acquisition
has a higher effective sample rate.
• Running — When running (versus taking a single acquisition), the memory is
usually divided in half. This lets the acquisition system acquire one record while
processing the previous acquisition, dramatically improving the number of
waveforms per second processed by the oscilloscope. When running, a high
waveform update rate provides the best representation of your input signal.
To acquire data with the longest possible record length, press the [Single] key.
For more information on settings that affect record length, see “Length
Control"on page348.
Overview of Sampling
To understand the oscilloscope's sampling and acquisition modes, it is helpful to
understand sampling theory, aliasing, oscilloscope bandwidth and sample rate,
oscilloscope rise time, oscilloscope bandwidth required, and how memory depth
affects sample rate.

---
**[Page 218]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 219
Sampling Theory
The Nyquist sampling theorem states that for a limited bandwidth (band-limited)
signal with maximum frequency f , the equally spaced sampling frequency f
MAX S
must be greater than twice the maximum frequency f , in order to have the
MAX
signal be uniquely reconstructed without aliasing.
f = f /2 = Nyquist frequency (f ) = folding frequency
MAX S N
Aliasing
Aliasing occurs when signals are under-sampled (f < 2f ). Aliasing is the signal
S MAX
distortion caused by low frequencies falsely reconstructed from an insufficient
number of sample points.
Figure 34 Aliasing
Oscilloscope Bandwidth and Sample Rate
An oscilloscope's bandwidth is typically described as the lowest frequency at
which input signal sine waves are attenuated by 3dB (-30% amplitude error).
|  |
|---|
|  |
|  |

---
**[Page 219]**

12 Acquisition Control
220 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
At the oscilloscope bandwidth, sampling theory says the required sample rate is f
S
= 2f . However, the theory assumes there are no frequency components above
BW
f (f in this case) and it requires a system with an ideal brick-wall frequency
MAX BW
response.
-3dB
fN fS
Figure 35 Theoretical Brick-Wall Frequency Response
However, digital signals have frequency components above the fundamental
frequency (square waves are made up of sine waves at the fundamental frequency
and an infinite number of odd harmonics), and the oscilloscope's frequency
response is not ideal — it can be more like the following Gaussian frequency
response.
noitaunettA
0dB
Frequency
| 0dB
-3dB
noitaunettA
fN fS
Frequency |  |  |  |
|---|---|---|---|
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

---
**[Page 220]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 221
-3dB
fS/4 fN fS
Limiting oscilloscope bandwidth (fBW) to 1/4 the sample rate (fS/4)
reduces frequency components above the Nyquist frequency (fN).
Figure 36 Sample Rate and Oscilloscope Bandwidth
So, in practice, an oscilloscope's sample rate should be four or more times its
bandwidth: f = 4f . This way, there is less aliasing, and aliased frequency
S BW
components have a greater amount of attenuation.
Note that some oscilloscope models (typically higher bandwidth) have more of a
brick-wall type frequency response than the Gaussian response of other
oscilloscope models (typically lower bandwidth). To understand the
characteristics of each type of oscilloscope frequency response, see
Understanding Oscilloscope Frequency Response and Its Effect on Rise-Time
Accuracy, Keysight Application Note 1420
(http://literature.cdn.keysight.com/litweb/pdf/5988-8008EN.pdf).
See Also Evaluating Oscilloscope Sample Rates vs. Sampling Fidelity: How to Make the
Most Accurate Digital Measurements, Keysight Application Note 1587
(http://literature.cdn.keysight.com/litweb/pdf/5989-5732EN.pdf)
Oscilloscope Rise Time
Closely related to an oscilloscope's bandwidth specification is its rise time
specification. Oscilloscopes with a Gaussian-type frequency response have an
approximate rise time of 0.35/f based on a 10% to 90% criterion.
BW
noitaunettA
0dB
Aliased frequency
components
Frequency
| 0dB
-3dB
noitaunettA
Aliased frequency
components
fS/4 fN fS
Frequency
Limiting oscilloscope bandwidth (fBW) to 1/4 the sample rate (fS/4)
reduces frequency components above the Nyquist frequency (fN). |
|---|
|  |
|  |  |  |  |
|---|---|---|---|
| Aliased fr
compon | equency
ents |  |  |

---
**[Page 221]**

12 Acquisition Control
222 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
An oscilloscope's rise time is not the fastest edge speed that the oscilloscope can
accurately measure. It is the fastest edge speed the oscilloscope can possibly
produce.
Oscilloscope Bandwidth Required
The oscilloscope bandwidth required to accurately measure a signal is primarily
determined by the signal's rise time, not the signal's frequency. You can use these
steps to calculate the oscilloscope bandwidth required:
1 Determine the fastest edge speeds.
You can usually obtain rise time information from published specifications for
devices used in your designs.
2 Compute the maximum "practical" frequency component.
From Dr. Howard W. Johnson's book, High-Speed Digital Design – A
Handbook of Black Magic, all fast edges have an infinite spectrum of frequency
components. However, there is an inflection (or "knee") in the frequency
spectrum of fast edges where frequency components higher than f are
knee
insignificant in determining the shape of the signal.
f = 0.5 / signal rise time (based on 10% - 90% thresholds)
knee
f = 0.4 / signal rise time (based on 20% - 80% thresholds)
knee
3 Use a multiplication factor for the required accuracy to determine the
oscilloscope bandwidth required.
Required accuracy Oscilloscope bandwidth required
20% f = 1.0 x f
BW knee
10% f = 1.3 x f
BW knee
3% f = 1.9 x f
BW knee
See Also Choosing an Oscilloscope with the Right Bandwidth for your Application, Keysight
Application Note 1588
(http://literature.cdn.keysight.com/litweb/pdf/5989-5733EN.pdf)
| Required accuracy | Oscilloscope bandwidth required |
|---|---|
| 20% | f = 1.0 x f
BW knee |
| 10% | f = 1.3 x f
BW knee |
| 3% | f = 1.9 x f
BW knee |

---
**[Page 222]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 223
Memory Depth and Sample Rate
The number of points of oscilloscope memory is fixed, and there is a maximum
sample rate associated with oscilloscope's analog-to-digital converter; however,
the actual sample rate is determined by the time of the acquisition (which is set
according to the oscilloscope's horizontal time/div scale).
sample rate = number of samples / time of acquisition
For example, when storing 50µs of data in 50,000 points of memory, the actual
sample rate is 1GSa/s.
Likewise, when storing 50ms of data in 50,000 points of memory, the actual
sample rate is 1MSa/s.
The actual sample rate is displayed in the Summary box in the right-side
information area.
The oscilloscope achieves the actual sample rate by throwing away (decimating)
unneeded samples.
Selecting the Acquisition Mode
When selecting the oscilloscope acquisition mode, keep in mind that samples are
normally decimated at slower time/div settings.
At slower time/div settings, the effective sample rate drops (and the effective
sample period increases) because the acquisition time increases and the
oscilloscope's digitizer is sampling faster than is required to fill memory.
For example, suppose an oscilloscope's digitizer has a sample period of 1ns
(maximum sample rate of 1GSa/s) and a 1M memory depth. At that rate, memory
is filled in 1ms. If the acquisition time is 100ms (10ms/div), only 1 of every 100
samples is needed to fill memory.
To select the acquisition mode:
1 Press the [Acquire] key on the front panel.
2 In the Acquire Menu, press the Acq Mode softkey; then, turn the Entry knob to
select the acquisition mode.
The InfiniiVision oscilloscopes have the following acquisition modes:

---
**[Page 223]**

12 Acquisition Control
224 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Normal — at slower time/div settings, normal decimation occurs, and there is
no averaging. Use this mode for most waveforms. See “Normal Acquisition
Mode"on page224.
• Peak Detect — at slower time/div settings, the maximum and minimum
samples in the effective sample period are stored. Use this mode for
displaying narrow pulses that occur infrequently. See “Peak Detect
Acquisition Mode"on page224.
• Averaging — at all time/div settings, the specified number of triggers are
averaged together. Use this mode for reducing noise and increasing
resolution of periodic signals without bandwidth or rise time degradation.
See “Averaging Acquisition Mode"on page227.
• High Resolution — at slower time/div settings, all samples in the effective
sample period are averaged and the average value is stored. Use this mode
for reducing random noise. See “High Resolution Acquisition Mode"on
page229.
Normal Acquisition Mode
In Normal mode at slower time/div settings, extra samples are decimated (in other
words, some are thrown away). This mode yields the best display for most
waveforms.
Peak Detect Acquisition Mode
In Peak Detect mode at slower time/div settings, minimum and maximum samples
are kept in order to capture infrequent and narrow events (at the expense of
exaggerating any noise). This mode displays all pulses that are at least as wide as
the sample period.
For InfiniiVision 6000X-Series oscilloscopes, which have a maximum sample rate
of 20GSa/s, a sample is taken every 50ps (sample period).
See Also • “Glitch or Narrow Pulse Capture"on page225
• “Using Peak Detect Mode to Find a Glitch"on page226

---
**[Page 224]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 225
Glitch or Narrow Pulse Capture
A glitch is a rapid change in the waveform that is usually narrow as compared to
the waveform. Peak detect mode can be used to more easily view glitches or
narrow pulses. In peak detect mode, narrow glitches and sharp edges are
displayed more brightly than when in Normal acquire mode, making them easier
to see.
To characterize the glitch, use the cursors or the automatic measurement
capabilities of the oscilloscope.
Figure 37 Sine With Glitch, Normal Mode
|  |
|---|
|  |

---
**[Page 225]**

12 Acquisition Control
226 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 38 Sine With Glitch, Peak Detect Mode
Using Peak Detect Mode to Find a Glitch
1 Connect a signal to the oscilloscope and obtain a stable display.
2 To find the glitch, press the [Acquire] key; then, press the AcqMode softkey until
Peak Detect is selected.
3 Press the [Display] key then press the ∞Persistence (infinite persistence) softkey.
Infinite persistence updates the display with new acquisitions but does not
erase previous acquisitions. New sample points are shown at normal intensity
while previous acquisitions are displayed at reduced intensity. Waveform
persistence is not kept beyond the display area boundary.
Press the Clear Display softkey to erase previously acquired points. The display
will accumulate points until ∞Persistence is turned off.
|  |
|---|
|  |

---
**[Page 226]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 227
4 Characterize the glitch with Zoom mode:
a Press the zoom key (or press the [Horiz] key and then the Zoom softkey).
b To obtain a better resolution of the glitch, expand the time base.
Use the horizontal position knob ( ) to pan through the waveform to set the
expanded portion of the normal window around the glitch.
Averaging Acquisition Mode
The Averaging mode lets you average multiple acquisitions together to reduce
noise and increase vertical resolution (at all time/div settings). Averaging requires
a stable trigger.
The number of averages can be set from 2 to 65536 in power-of-2 increments.
A higher number of averages reduces noise more and increases vertical resolution.
# Avgs Bits of resolution
2 8
4 9
16 10
64 11
≥ 256 12
The higher the number of averages, the slower the displayed waveform responds
to waveform changes. You must compromise between how quickly the waveform
responds to changes and how much you want to reduce the displayed noise on
the signal.
To use the Averaging mode:
1 Press the [Acquire] key, then press the Acq Mode softkey until the Averaging
mode is selected.
2 Press the #Avgs softkey and turn the Entry knob to set the number of averages
that best eliminates the noise from the displayed waveform. The number of
acquisitions being averaged is displayed in the # Avgs softkey.
|  |  |
|---|---|
| # Avgs | Bits of resolution |
|---|---|
| 2 | 8 |
| 4 | 9 |
| 16 | 10 |
| 64 | 11 |
| ≥
256 | 12 |

---
**[Page 227]**

12 Acquisition Control
228 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 39 Random noise on the displayed waveform
|  |
|---|
|  |

---
**[Page 228]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 229
Figure 40 128 Averages used to reduce random noise
See Also • Chapter11, “Trigger Mode/Coupling,” starting on page 209
• “Averaged Value"on page115
High Resolution Acquisition Mode
In High Resolution mode, at slower time/div settings extra samples are averaged
in order to reduce random noise, produce a smoother trace on the screen, and
effectively increase vertical resolution.
High Resolution mode averages sequential sample points within the same
acquisition. An extra bit of vertical resolution is produced for every factor of 2
averages. Random noise is reduced by ½ for every factor of 4 averages. The
number of extra bits of vertical resolution is dependent on the time per division
setting (sweep speed) of the oscilloscope.
|  |
|---|
|  |

---
**[Page 229]**

12 Acquisition Control
230 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The slower the time/div setting, the greater the number of samples that are
averaged together for each display point.
High Resolution mode can be used on both single-shot and repetitive signals and
it does not slow waveform update because the computation is done in the
MegaZoom custom ASIC. High Resolution mode limits the oscilloscope's real-time
bandwidth because it effectively acts like a low-pass filter.
Sweep speed Bits of resolution
≤ 1µs/div 8
2µs/div 9
5µs/div 10
10µs/div 11
≥ 20µs/div 12
Data Acquisition (Sampling) Mode
The Data Acq Mode softkey lets you select the type of sampling used by the
oscilloscope:
• Realtime — Specifies that the oscilloscope produce the waveform display from
samples collected during one trigger event (that is, one acquisition). At fast
sweep speeds, when not enough samples can be collected for a waveform, a
sophisticated reconstruction filter is used to fill-in sample points and enhance
the waveform display.
In Realtime mode, to accurately reproduce a sampled waveform, the sample
rate should be at least 2.5 times the highest frequency component of the
waveform. If not, it is possible for the reconstructed waveform to be distorted or
aliased. Aliasing is most commonly seen as jitter on fast digital edges.
Use Realtime sampling to capture infrequent triggers, unstable triggers, or
complex changing waveforms, such as eye diagrams.
• Realtime (Max Update Rate) — This is the same as Realtime except that in order to
provide maximum update rate (trigger rates), the sample rate drops from
20GSa/s to 2GSa/s at a faster time/div setting than normal.
| Sweep speed | Bits of resolution |
|---|---|
| ≤
1µs/div | 8 |
| 2µs/div | 9 |
| 5µs/div | 10 |
| 10µs/div | 11 |
| ≥
20µs/div | 12 |

---
**[Page 230]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 231
This mode is ideal for finding glitches and infrequent events in waveforms that
do not require the full 20GSa/s sample rate (and associated bandwidth).
This mode is not allowed in single, roll, segmented, or mask test.
• Equivalent Time — Available in 6GHz bandwidth models, this option gives you
another way to fill-in sample points at fast sweep speeds — it is used only when
sweep speeds are 20ns/div or faster. In this case, instead of a reconstruction
filter, a technique known as random repetitive sampling is used to build-up and
draw one waveform using multiple triggers (acquisitions).
At slower sweep speeds, there are enough sample points in a trigger
(acquisition, in other words) to render a waveform on the display.
Equivalent time sampling mode requires a repetitive waveform with a stable
trigger.
See Also • “Realtime Sampling and Oscilloscope Bandwidth"on page231
Realtime Sampling and Oscilloscope Bandwidth
To accurately reproduce a sampled waveform, the sample rate should be at least
2.5 times the highest frequency component of the waveform. If not, it is possible
for the reconstructed waveform to be distorted or aliased. Aliasing is most
commonly seen as jitter on fast edges.
The maximum sample rate for the 6000X-Series oscilloscopes is 20GSa/s for a
single channel in a channel pair. Channels 1 and 2 constitute a channel pair, and
channels 3 and 4 constitute another channel pair. For example, the sample rate of
a 4-channel oscilloscope is 20GSa/s when channels 1 and 3, 1 and 4, 2 and 3, or
2 and 4 are on.
Whenever both channels in a channel pair are on, the sample rate for all channels
is halved. For example, when channels 1, 2, and 3 are on, the sample rate for all
channels is 10GSa/s.
When Realtime sampling is on, the bandwidth of the oscilloscope is limited
because the bandwidth of the reconstruction filter is set to fs/4. For example, a
6GHz MSOX600xA oscilloscope with channels 1 and 2 on has a bandwidth of
2.5MHz when Realtime sampling on and 6GHz when Realtime sampling is off.
The sample rate is displayed in the sidebar Summary dialog.

---
**[Page 231]**

12 Acquisition Control
232 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Acquiring to Segmented Memory
When capturing multiple infrequent trigger events it is advantageous to divide the
oscilloscope's memory into segments. This lets you capture signal activity without
capturing long periods of signal inactivity.
Each segment is complete with all analog channel, digital channel (on MSO
models), and serial decode data.
When using segmented memory, use the Analyze Segments feature (see
“Measurements, Statistics, and Infinite Persistence with Segmented Memory"on
page233) to show infinite persistence across all acquired segments. See also “To
set or clear persistence"on page157 for details.
To acquire to 1 Set up a trigger condition. (See Chapter10, “Triggers,” starting on page 171
segmented for details.)
memory
2 Press the [Acquire] key in the Waveform section of the front panel.
3 Press the Segmented softkey.
4 In the Segmented Memory Menu, press the Segmented softkey to enable
segmented memory acquisitions.
5 Press the #ofSegs softkey and turn the Entry knob to select the number of
segments into which you would like to divide the oscilloscope's memory.
Memory can be divided into as few as two segments and as many as 1000
segments.
6 Press the [Run] or [Single] key.
The oscilloscope runs and fills a memory segment for each trigger event. When
the oscilloscope is busy acquiring multiple segments, the progress is displayed on
screen. The oscilloscope continues to trigger until memory is filled, then the
oscilloscope stops.
If the signal you are measuring has more than about 1s of inactivity, consider
selecting the Normal trigger mode to prevent AutoTriggering. See “To select the
Auto or Normal trigger mode"on page210.
See Also • “Navigating Segments"on page233
• “Measurements, Statistics, and Infinite Persistence with Segmented
Memory"on page233
• “Segmented Memory Re-Arm Time"on page234
• “Saving Data from Segmented Memory"on page234

---
**[Page 232]**

Acquisition Control 12
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 233
Navigating Segments
1 Press the CurrentSeg softkey and turn the Entry knob to display the desired
segment along with a time tag indicating the time from the first trigger event.
You can also navigate segments using the [Navigate] key and controls. See “To
navigate segments"on page78.
Measurements, Statistics, and Infinite Persistence with Segmented
Memory
To perform measurements and view statistical information, press [Meas] and set up
your desired measurements (see Chapter14, “Measurements,” starting on page
245). Then, press Analyze Segments. Statistical data will be accumulated for the
measurements you have chosen.
The Analyze Segments softkey appears when the acquisition is stopped and the
segmented memory feature is on or when the serial Lister or Histogram is enabled.
|  |
|---|
|  |

---
**[Page 233]**

12 Acquisition Control
234 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You can also turn on infinite persistence (in the Display Menu) and press the
Analyze Segments softkey to create an infinite persistence display.
Segmented Memory Re-Arm Time
After each segment fills, the oscilloscope re-arms and is ready to trigger in about
1µs.
Remember though, for example: if the horizontal time per division control is set to
5µs/div, and the Time Reference is set to Center, it will take at least 50µs to fill all
ten divisions and re-arm. (That is 25µs to capture pre-trigger data and 25µs to
capture post-trigger data.)
Saving Data from Segmented Memory
You can save either the currently displayed segment (Save Segment - Current), or all
segments (Save Segment - All) in the following data formats: CSV, ASCII XY, and
BIN.
Be sure to set the Length control to capture enough points to accurately represent
the captured data. When the oscilloscope is busy saving multiple segments,
progress is displayed in the upper right area of the display.
For more information, see “To save CSV, ASCII XY, or BIN data files"on page346.

---
**[Page 234]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
235
13 Cursors
To make cursor measurements / 236
Cursor Examples / 239
Cursors are horizontal and vertical markers that indicate X-axis values and Y-axis
values on a selected waveform source. You can use cursors to make custom
voltage, time, phase, or ratio measurements on oscilloscope signals.
Cursor information is displayed in the right-side information area.
Cursors are not always limited to the visible display. If you set a cursor, then pan
and zoom the waveform until the cursor is off screen, its value will not be changed.
It will still be there when you return to its original location.
X Cursors X cursors are vertical dashed lines that adjust horizontally and can be used to
measure time (s), frequency (1/s), phase (°), and ratio (%).
The X1 cursor is the short-dashed vertical line, and the X2 cursor is the
long-dashed vertical line.
When used with the FFT math function as a source, the X cursors indicate
frequency.
In XY horizontal mode, the X cursors display channel 1 values (Volts or Amps).
The X1 and X2 cursor values for the selected waveform source are displayed in the
softkey menu area.
The difference between X1 and X2 (Δ X) and 1/Δ X are displayed in the Cursors box
in the right-side information area.
Y Cursors Y cursors are horizontal dashed lines that adjust vertically and can be used to
measure Volts or Amps, dependent on the channel Probe Units setting, or they can
measure ratios (%). When math functions are used as a source, the measurement
units correspond to that math function.

---
**[Page 235]**

13 Cursors
236 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The Y1 cursor is the short-dashed horizontal line and the Y2 cursor is the
long-dashed horizontal line.
The Y cursors adjust vertically and typically indicate values relative to the
waveform's ground point, except math FFT where the values are relative to 0dB.
In XY horizontal mode, the Y cursors display channel 2 values (Volts or Amps).
When active, the Y1 and Y2 cursor values for the selected waveform source are
displayed in the softkey menu area.
The difference between Y1 and Y2 (Δ Y) is displayed in the Cursors box in the
right-side information area.
To make cursor measurements
1 Connect a signal to the oscilloscope and obtain a stable display.
2 Press the [Cursors] key.
The Cursors box in the right-side information area appears, indicating that
cursors are "on". (Press the [Cursors] key again when you want to turn cursors
off.)
3 In the Cursors Menu, press Mode; then, select the desired mode:
• Manual — Δ X, 1/Δ X, and Δ Y values are displayed. Δ X is the difference
between the X1 and X2 cursors and Δ Y is the difference between the Y1 and
Y2 cursors.
• Track Waveform — As you move a marker horizontally, the vertical amplitude
of the waveform is tracked and measured. The time and voltage positions
are shown for the markers. The vertical (Y) and horizontal (X) differences
between the markers are shown as Δ X and Δ Y values.
• Measure — When measurements are displayed, this mode shows the cursor
locations used to make the measurement. When you add a measurement, it
becomes the one that cursors are displayed for. You can use the Measurement
softkey or touch in the Meas sidebar dialog to select the measurement
whose cursor locations are displayed.
|  |  |
|---|---|

---
**[Page 236]**

Cursors 13
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 237
• Binary — Logic levels of displayed waveforms at the current X1 and X2 cursor
positions are displayed in the Cursor sidebar dialog in binary. The display is
color coded to match the color of the related channel's waveform.
• Hex — Logic levels of displayed waveforms at the current X1 and X2 cursor
positions are displayed in the Cursor sidebar dialog in hexadecimal.
Manual and Track Waveform modes can be used on waveforms that are displayed
on the analog input channels (including math functions).
Binary and Hex modes apply to digital signals (of MSO oscilloscope models).
In Hex and Binary modes, a level can be displayed as 1 (higher than trigger
level), 0 (lower than trigger level), indeterminate state (-), or X (don't care).
In Binary mode, X is displayed if the channel is turned off.
In Hex mode, the channel is interpreted as 0 if turned off.
4 Press Source (or X1Source, X2Source in the Track Waveform mode); then, select
the input source for cursor values.
5 To select and adjust cursors:
• Using the touchscreen, select cursors by touching their handles, and adjust
them by dragging their handles. See “Drag Cursors"on page51.
You can use the Cursors knob after that to make precise adjustments.
• Using the Cursors knob, you can select the cursor(s) to be adjusted by
pushing the knob, turning the knob to make the selection, and pushing the
knob again (or waiting about five seconds for the popup menu to disappear)
to finalize the selection.
The X1X2linked and Y1Y2linked selections let you adjust both cursors at the
same time, while the delta value remains the same. This can be useful, for
example, for checking pulse width variations in a pulse train.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 237]**

13 Cursors
238 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To adjust the selected cursor(s), turn the Cursors knob.
• Using the Cursors softkey, you select cursors by pressing the softkey and
then turning the Entry knob.
To adjust the selected cursor(s), turn the Cursors knob.
The currently selected cursor(s) display brighter than the other cursors.
6 To change the cursor units, press the Units softkey.
In the Cursor Units Menu:
You can press the XUnits softkey to select:
• Seconds (s).
• Hz (1/s).
• Phase (°) — when selected, use the UseXCursors softkey to set the current X1
location as 0 degrees and the current X2 location as 360 degrees.
• Ratio (%) — when selected, use the UseXCursors softkey to set the current X1
location as 0% and the current X2 location as 100%.
You can press the YUnits softkey to select:
• Base — the same units used for the source waveform.
• Ratio (%) — when selected, use the Use YCursors softkey to set the current Y1
location as 0% and the current Y2 location as 100%.
For phase or ratio units, once the 0 and 360 degree or 0 and 100% locations are
set, adjusting cursors will display measurements relative to the set locations.
|  |  |
|---|---|

---
**[Page 238]**

Cursors 13
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 239
Cursor Examples
Figure 41 Cursors used to measure pulse widths other than middle threshold points
|  |
|---|
|  |

---
**[Page 239]**

13 Cursors
240 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 42 Cursors measure frequency of pulse ringing
Expand the display with Zoom mode, then characterize the event of interest with
the cursors.
|  |
|---|
|  |

---
**[Page 240]**

Cursors 13
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 241
Figure 43 Cursors track Zoom window
Put the X1 cursor on one side of a pulse and the X2 cursor on the other side of the
pulse.
|  |
|---|
|  |

---
**[Page 241]**

13 Cursors
242 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 44 Measuring pulse width with cursors
Press the X1X2linked softkey and move the cursors together to check for pulse
width variations in a pulse train.
|  |
|---|
|  |

---
**[Page 242]**

Cursors 13
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 243
Figure 45 Moving the cursors together to check pulse width variations
|  |
|---|
|  |

---
**[Page 243]**

13 Cursors
244 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 244]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
245
14 Measurements
To make automatic measurements / 246
Measurements Summary / 248
Voltage Measurements / 252
Time Measurements / 259
Count Measurements / 268
Mixed Measurements / 269
Measurement Thresholds / 270
Measurement Window / 272
Measurement Statistics / 272
Precision Measurements and Math / 275
The [Meas] key lets you make automatic measurements on waveforms. Some
measurements can only be made on analog input channels.
The results of the last 10 selected measurements are displayed in the
Measurements list dialog (which can be selected from the right-hand sidebar
menu — see “Select Sidebar Information or Controls"on page49 and “Undock
Sidebar Dialogs by Dragging"on page50).
When you add a measurement, it appears at the bottom of the Measurements list
dialog, and cursors that show the portion of the waveform being measured are
automatically displayed. You can change the measurement for which cursors are
displayed by touching the measurement in the list and choosing Track With Cursors
in the popup menu or by selecting the measurement in the Cursors Menu.

---
**[Page 245]**

14 Measurements
246 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Post Acquisition Processing
NOTE
In addition to changing display parameters after the acquisition, you can perform all of the
measurements and math functions after the acquisition. Measurements and math functions
will be recalculated as you pan and zoom and turn channels on and off. As you zoom in and out
on a signal using the horizontal scale knob and vertical volts/division knob, you affect the
resolution of the display. Because measurements and math functions are performed on
displayed data, you affect the resolution of functions and measurements.
To make automatic measurements
1 Press the [Meas] key to display the Measurement Menu.
2 Press the Source softkey to select the channel, running math function, or
reference waveform to be measured.
Only channels, math functions, or reference waveforms that are displayed are
available for measurements.
If a portion of the waveform required for a measurement is not displayed or
does not display enough resolution to make the measurement, the result will
display "No Edges", "Clipped", "Low Signal", "< value", or "> value", or a similar
message to indicate that the measurement may not be reliable.
3 Press the Type: softkey; then, rotate the Entry knob to select a measurement to
be made.
| NOTE |
|---|
|  |
|  |  |
|---|---|

---
**[Page 246]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 247
You can also use the touchscreen to select measurements. You can touch the
"+" in the Measurements sidebar dialog to open the measurement type menu.
See also “Touch Softkeys and Menus On the Screen"on page51.
For more information on the types of measurements, see “Measurements
Summary"on page248.
4 The Settings softkey will be available to make additional measurement settings
on some measurements.
5 Press the Add Measurement softkey or push the Entry knob to display the
measurement.
Cursors are turned on to show the portion of the waveform being measured for
the most recently added measurement (bottom-most on the display). To view
the cursors for a previously added measurement (but not the last one), add the
measurement again.
By default, measurement statistics are displayed. See “Measurement
Statistics"on page272.
6 To turn off measurements, press the [Meas] key again.
|  |  |
|---|---|

---
**[Page 247]**

14 Measurements
248 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Measurements are erased from the display.
7 To stop making one or more measurements, press the Clear Meas softkey and
choose the measurement to clear, or press Clear All.
After all measurements have been cleared, when [Meas] is pressed again, the
default measurements will be Frequency and Peak-Peak.
Measurements Summary
The automatic measurements provided by the oscilloscope are listed in the
following table. All measurements are available for analog channel waveforms. All
measurements except Counter are available for reference waveforms and math
waveforms other than FFT. A limited set of measurements is available for math FFT
waveforms and for digital channel waveforms (as described in the following table).
Measurement Valid Valid for Notes
for Digital
Math Channels
FFT*
“Snapshot All"on page251
“Amplitude"on page253
“Area"on page269
“Average"on page257 Yes, Full
Screen
“Base"on page255
“Bit Rate"on page264 Yes
“Burst Width"on page263
“Counter"on page262 Yes Not valid for math waveforms.
|  |  |
|---|---|
| Measurement | Valid
for
Math
FFT* | Valid for
Digital
Channels | Notes |
|---|---|---|---|
| “Snapshot All"on page251 |  |  |  |
| “Amplitude"on page253 |  |  |  |
| “Area"on page269 |  |  |  |
| “Average"on page257 | Yes, Full
Screen |  |  |
| “Base"on page255 |  |  |  |
| “Bit Rate"on page264 |  | Yes |  |
| “Burst Width"on page263 |  |  |  |
| “Counter"on page262 |  | Yes | Not valid for math waveforms. |

---
**[Page 248]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 249
Measurement Valid Valid for Notes
for Digital
Math Channels
FFT*
“Delay"on page264 Measures between two sources.
Press Settings to specify the second
source.
“Duty Cycle"on page263 Yes
“Fall Time"on page264
“Frequency"on page261 Yes
“Maximum"on page253 Yes
“Minimum"on page253 Yes
“Rising Edge Count"on
page269
“Falling Edges Count"on
page269
“Positive Pulse Count"on
page268
“Negative Pulse Count"on
page268
“Overshoot"on page255
“Peak-Peak"on page253 Yes
“Period"on page260 Yes
“Phase"on page265 Measures between two sources.
Press Settings to specify the second
source.
“Preshoot"on page256
“Ratio"on page259 Measures between two sources.
Press Settings to specify the second
source.
“Rise Time"on page264
“DC RMS"on page257
| Measurement | Valid
for
Math
FFT* | Valid for
Digital
Channels | Notes |
|---|---|---|---|
| “Delay"on page264 |  |  | Measures between two sources.
Press Settings to specify the second
source. |
| “Duty Cycle"on page263 |  | Yes |  |
| “Fall Time"on page264 |  |  |  |
| “Frequency"on page261 |  | Yes |  |
| “Maximum"on page253 | Yes |  |  |
| “Minimum"on page253 | Yes |  |  |
| “Rising Edge Count"on
page269 |  |  |  |
| “Falling Edges Count"on
page269 |  |  |  |
| “Positive Pulse Count"on
page268 |  |  |  |
| “Negative Pulse Count"on
page268 |  |  |  |
| “Overshoot"on page255 |  |  |  |
| “Peak-Peak"on page253 | Yes |  |  |
| “Period"on page260 |  | Yes |  |
| “Phase"on page265 |  |  | Measures between two sources.
Press Settings to specify the second
source. |
| “Preshoot"on page256 |  |  |  |
| “Ratio"on page259 |  |  | Measures between two sources.
Press Settings to specify the second
source. |
| “Rise Time"on page264 |  |  |  |
| “DC RMS"on page257 |  |  |  |

---
**[Page 249]**

14 Measurements
250 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Measurement Valid Valid for Notes
for Digital
Math Channels
FFT*
“AC RMS"on page258
“Top"on page254
“+ Width"on page263 Yes
“– Width"on page263 Yes
“X at Max Y"on page267 Yes The resultant units are in Hertz.
“X at Min Y"on page267 Yes The resultant units are in Hertz.
* Use the cursors to make other measurements on FFT.
Power App Note that additional Power App measurements are available when the
Measurements DSOX6PWR power measurement and analysis license is installed and the Power
Application is enabled. For more information, see the DSOX6PWR Power
Measurement Application User's Guide at
www.keysight.com/find/6000X-Series-manual or on the Documentation CD.
Jitter and Note that additional Jitter and Real-Time Eye Analysis measurements are
Real-time Eye available when the DSOX6JITTER license is installed and the features are enabled.
Analysis See “Jitter Measurements"on page295 and “Real-Time Eye Analysis"on
Measurements page299.
Dual-Channel Note that additional measurements are available with the N2820A high-sensitivity
(N2820A Probe) current probe when both the Primary and Secondary probe cables are used.
Measurements ZoomIn waveform data below the probe's clamp level is joined with ZoomOut
waveform data above the probe's clamp level to create the waveform on which the
measurement is made. These measurements are only valid for analog input
channels.
Dual-Channel (N2820A Probe) Notes
Measurement
Amplitude See “Amplitude"on page253.
Charge Charge (in Amp-hours) is the measured area under
the waveform. See “Area"on page269.
| Measurement | Valid
for
Math
FFT* | Valid for
Digital
Channels | Notes |
|---|---|---|---|
| “AC RMS"on page258 |  |  |  |
| “Top"on page254 |  |  |  |
| “+ Width"on page263 |  | Yes |  |
| “– Width"on page263 |  | Yes |  |
| “X at Max Y"on page267 | Yes |  | The resultant units are in Hertz. |
| “X at Min Y"on page267 | Yes |  | The resultant units are in Hertz. |
| * Use the cursors to make other measurements on FFT. |  |  |  |
| Dual-Channel (N2820A Probe)
Measurement | Notes |
|---|---|
| Amplitude | See “Amplitude"on page253. |
| Charge | Charge (in Amp-hours) is the measured area under
the waveform. See “Area"on page269. |

---
**[Page 250]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 251
Dual-Channel (N2820A Probe) Notes
Measurement
Average See “Average"on page257.
Base See “Base"on page255.
Peak-Peak See “Peak-Peak"on page253.
DC RMS See “DC RMS"on page257.
AC RMS See “AC RMS"on page258.
When using the N2820A probe to make measurements on a battery-powered
(floating) device, always connect the supplied ground lead between ground on
your device and the probe's ground connector as shown in the following figure.
Simply snap the end of the ground lead onto the probe's connector. Without the
ground connection, the probe's common-mode input amplifier cannot properly
display waveforms.
Figure 46 Measurements on Battery Powered Devices Using the N2820A Probe
Snapshot All
The Snapshot All measurement type displays a popup containing a snapshot of all
the single waveform measurements.
| Dual-Channel (N2820A Probe)
Measurement | Notes |
|---|---|
| Average | See “Average"on page257. |
| Base | See “Base"on page255. |
| Peak-Peak | See “Peak-Peak"on page253. |
| DC RMS | See “DC RMS"on page257. |
| AC RMS | See “AC RMS"on page258. |
|  |
|---|
|  |

---
**[Page 251]**

14 Measurements
252 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You can also configure the [Quick Action] key to display the Snapshot All popup.
See “Configuring the [Quick Action] Key"on page381.
Voltage Measurements
The following figure shows the voltage measurement points.
Maximum
Top
Amplitude Peak-Peak
Base
Minimum
Measurement units for each input channel can be set to Volts or Amps using the
channel Probe Units softkey. See “To specify the channel units"on page88.
|  |
|---|
|  |
| Maximum
Top
Amplitude Peak-Peak
Base
Minimum |
|---|
|  |

---
**[Page 252]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 253
The units of math waveforms are described in “Units for Math Waveforms"on
page93.
• “Peak-Peak"on page253
• “Maximum"on page253
• “Minimum"on page253
• “Amplitude"on page253
• “Top"on page254
• “Base"on page255
• “Overshoot"on page255
• “Preshoot"on page256
• “Average"on page257
• “DC RMS"on page257
• “AC RMS"on page258
• “Ratio"on page259
Peak-Peak
The peak-to-peak value is the difference between Maximum and Minimum values.
The Y cursors show the values being measured.
Maximum
Maximum is the highest value in the waveform display. The Y cursor shows the
value being measured.
Minimum
Minimum is the lowest value in the waveform display. The Y cursor shows the
value being measured.
Amplitude
The Amplitude of a waveform is the difference between its Top and Base values.
The Y cursors show the values being measured.

---
**[Page 253]**

14 Measurements
254 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Top
The Top of a waveform is the mode (most common value) of the upper part of the
waveform, or if the mode is not well defined, the top is the same as Maximum. The
Y cursor shows the value being measured.
See Also • “To isolate a pulse for Top measurement"on page254
To isolate a pulse for Top measurement
The following figure shows how to use Zoom mode to isolate a pulse for a Top
measurement.
You may need to change the measurement window setting so that the
measurement is made in the lower, Zoom window. See “Measurement
Window"on page272.
Figure 47 Isolating area for Top measurement
|  |
|---|
|  |

---
**[Page 254]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 255
Base
The Base of a waveform is the mode (most common value) of the lower part of the
waveform, or if the mode is not well defined, the base is the same as Minimum.
The Y cursor shows the value being measured.
Overshoot
Overshoot is distortion that follows a major edge transition expressed as a
percentage of Amplitude. The X cursors show which edge is being measured (edge
closest to the trigger reference point).
local Maximum − D Top
Rising edge overshοot = × 100
Amplitude
Base − D local Minimum
Falling edge overshοot = × 100
Amplitude
Overshoot
local Maximum
Top
Base
local Minimum Overshoot
| local Maximum − D Top
Rising edge overshοot = × 100
Amplitude |
|---|
|  |
| Base − D local Minimum
Falling edge overshοot = × 100
Amplitude |
|---|
|  |
| Overshoot
local Maximum
Top
Base
local Minimum Overshoot |
|---|
|  |

---
**[Page 255]**

14 Measurements
256 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 48 Automatic Overshoot measurement
Preshoot
Preshoot is distortion that precedes a major edge transition expressed as a
percentage of Amplitude. The X cursors show which edge is being measured (edge
closest to the trigger reference point).
local Maximum − D Top
Rising edge preshοot = × 100
Amplitude
Base − D local Minimum
Falling edge preshοot = × 100
Amplitude
|  |
|---|
|  |
| local Maximum − D Top
Rising edge preshοot = × 100
Amplitude |
|---|
|  |
| Base − D local Minimum
Falling edge preshοot = × 100
Amplitude |
|---|
|  |

---
**[Page 256]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 257
Preshoot
local Maximum
Top
Base
Preshoot local Minimum
Average
Average is the sum of the levels of the waveform samples divided by the number
of samples.
∑x
i
Average = n
Where x = value at ith point being measured, n = number of points in
i
measurement interval.
The Full Screen measurement interval variation measures the value on all
displayed data points.
The N Cycles measurement interval variation measures the value on an integral
number of periods of the displayed signal. If less than three edges are present, the
measurement shows "No edges".
The X cursors show what interval of the waveform is being measured.
DC RMS
DC RMS is the root-mean-square value of the waveform over one or more full
periods.
∑n
x2
i
RMS (dc) = i= n 1
Where x = value at ith point being measured, n = number of points in
i
measurement interval.
The Full Screen measurement interval variation measures the value on all
displayed data points.
| Preshoot
local Maximum
Top
Base
Preshoot local Minimum |
|---|
|  |
| ∑x
i
Average = n |
|---|
|  |
| ∑n
x2
i
RMS (dc) = i= n 1 |
|---|
|  |

---
**[Page 257]**

14 Measurements
258 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The N Cycles measurement interval variation measures the value on an integral
number of periods of the displayed signal. If less than three edges are present, the
measurement shows "No edges".
The X cursors show the interval of the waveform being measured.
AC RMS
AC RMS is the root-mean-square value of the waveform, with the DC component
removed. It is useful, for example, for measuring power supply noise.
The N Cycles measurement interval measures the value on an integral number of
periods of the displayed signal. If less than three edges are present, the
measurement shows "No edges".
The X cursors show the interval of the waveform being measured.
The Full Screen (Std Deviation) measurement interval variation is an RMS
measurement across the full screen with the DC component removed. It shows the
standard deviation of the displayed voltage values.
The standard deviation of a measurement is the amount that a measurement
varies from the mean value. The Mean value of a measurement is the statistical
average of the measurement.
The following figure graphically shows the mean and standard deviation. Standard
deviation is represented by the Greek letter sigma: σ. For a Gaussian distribution,
two sigma (± 1σ) from the mean, is where 68.3 percent of the measurement results
reside. Six sigma (± 3σ) from is where 99.7 percent of the measurement results
reside.
mean
-3σ-2σ -1σ 0 1σ 2σ 3σ
68.3%
95.4%
99.7%
| mean |
|---|
| -3σ-2σ -1σ 0 1σ 2σ 3σ
68.3%
95.4%
99.7% |
|  |

---
**[Page 258]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 259
The mean is calculated as follows:
∑N x
i
¯x = i=1
N
where:
• x = the mean.
• N = the number of measurements taken.
• x = the ith measurement result.
i
The standard deviation is calculated as follows:
∑N (x −¯x)2
i
σ = i=1
N
where:
• σ = the standard deviation.
• N = the number of measurements taken.
• x = the ith measurement result.
i
• x = the mean.
Ratio
The Ratio measurement displays the ratio of the AC RMS voltages of two sources,
expressed in dB. Press the Settings softkey to select the source channels for the
measurement.
Time Measurements
The following figure shows time measurement points.
| ∑N x
i
¯x = i=1
N |
|---|
|  |
| ∑N (x −¯x)2
i
σ = i=1
N |
|---|
|  |

---
**[Page 259]**

14 Measurements
260 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Rise Time Fall Time
Thresholds
Upper
Middle
Lower
+ Width - Width
Period
The default lower, middle, and upper measurement thresholds are 10%, 50%, and
90% between Top and Base values. See “Measurement Thresholds"on page270
for other percentage threshold and absolute value threshold settings.
• “Period"on page260
• “Frequency"on page261
• “Counter"on page262
• “+ Width"on page263
• “– Width"on page263
• “Burst Width"on page263
• “Duty Cycle"on page263
• “Bit Rate"on page264
• “Rise Time"on page264
• “Fall Time"on page264
• “Delay"on page264
• “Phase"on page265
• “X at Min Y"on page267
• “X at Max Y"on page267
Period
Period is the time period of the complete waveform cycle. The time is measured
between the middle threshold points of two consecutive, like-polarity edges. A
middle threshold crossing must also travel through the lower and upper threshold
levels which eliminates runt pulses. The X cursors show what portion of the
waveform is being measured. The Y cursor shows the middle threshold point.
| Rise Time Fall Time
Thresholds
Upper
Middle
Lower
+ Width - Width
Period |
|---|
|  |

---
**[Page 260]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 261
Frequency
Frequency is defined as 1/Period. Period is defined as the time between the
middle threshold crossings of two consecutive, like-polarity edges. A middle
threshold crossing must also travel through the lower and upper threshold levels
which eliminates runt pulses. The X cursors show what portion of the waveform is
being measured. The Y cursor shows the middle threshold point.
See Also • “To isolate an event for frequency measurement"on page261
To isolate an event for frequency measurement
The following figure shows how to use Zoom mode to isolate an event for a
frequency measurement.
You may need to change the measurement window setting so that the
measurement is made in the lower, Zoom window. See “Measurement
Window"on page272.
If the waveform is clipped, it may not be possible to make the measurement.

---
**[Page 261]**

14 Measurements
262 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Figure 49 Isolating an event for Frequency measurement
Counter
The InfiniiVision 6000X-Series oscilloscopes have an integrated hardware
frequency counter which counts the number of cycles that occur within a period of
time (known as the gate time) to measure the frequency of a signal.
The gate time is the horizontal range of the oscilloscope but is limited to >= 0.1s
and <= 10s. Unlike other measurements, the Zoom horizontal timebase window
does not gate the Counter measurement.
The Counter measurement can measure frequencies up to 1GHz (1.2GHz
typical). The minimum frequency supported is 2.0/gateTime.
The hardware counter uses the trigger comparator output. Therefore, the counted
channel's trigger level (or threshold for digital channels) must be set correctly. The
Y cursor shows the threshold level used in the measurement.
Analog and digital channels can be selected as the source.
|  |
|---|
|  |

---
**[Page 262]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 263
Only one Counter measurement can be displayed at a time.
This counter is different than the one that comes with the DVM (see “Counter"on
page320).
+ Width
+ Width is the time from the middle threshold of the rising edge to the middle
threshold of the next falling edge. The X cursors show the pulse being measured.
The Y cursor shows the middle threshold point.
– Width
– Width is the time from the middle threshold of the falling edge to the middle
threshold of the next rising edge. The X cursors show the pulse being measured.
The Y cursor shows the middle threshold point.
Burst Width
The Burst Width measurement is the time from the first edge to the last edge on
screen.
Burst width
Duty Cycle
The duty cycle of a repetitive pulse train is the ratio of the pulse width to the
period, expressed as a percentage. The X cursors show the time period being
measured. The Y cursor shows the middle threshold point.
+ Width − Width
+ Duty cycle = × 100 − Duty cycle = × 100
Period Period
| Burst width |
|---|
|  |
| + Width − Width
+ Duty cycle = × 100 − Duty cycle = × 100
Period Period |
|---|
|  |

---
**[Page 263]**

14 Measurements
264 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Bit Rate
The bit rate measurement measures all positive and negative pulse widths on the
waveform, takes the minimum value found of either width type and inverts that
minimum width to give a value in Hertz.
Rise Time
The rise time of a signal is the time difference between the crossing of the lower
threshold and the crossing of the upper threshold for a positive-going edge. The X
cursor shows the edge being measured. For maximum measurement accuracy, set
the horizontal time/div as fast as possible while leaving the complete rising edge
of the waveform on the display. The Y cursors show the lower and upper threshold
points.
Fall Time
The fall time of a signal is the time difference between the crossing of the upper
threshold and the crossing of the lower threshold for a negative-going edge. The X
cursor shows the edge being measured. For maximum measurement accuracy, set
the horizontal time/div as fast as possible while leaving the complete falling edge
of the waveform on the display. The Y cursors show the lower and upper threshold
points.
Delay
Delay measures the time difference from the specified source 1 edge that is
closest to the center of the screen and the nearest specified source 2 edge using
the middle threshold points on the waveforms.
Negative delay values indicate that the selected edge of source 1 occurred after
the selected edge of source 2.
Source 1
Delay
Source 2
1 Press the [Meas] key to display the Measurement Menu.
2 Press the Source softkey; then turn the Entry knob to select the first analog
channel source.
| Source 1
Delay
Source 2 |
|---|
|  |

---
**[Page 264]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 265
3 Press the Type: softkey; then, turn the Entry knob to select Delay.
4 Press the Settings softkey to select the second analog channel source and slope
for the delay measurement.
The default Delay settings measure from the rising edge of channel 1 to the
rising edge of channel 2.
5 Press the Back Back/Up key to return to the Measurement Menu.
6 Press the Add Measurement softkey to make the measurement.
The example below shows a delay measurement between the rising edge of
channel 1 and the rising edge of channel 2.
Phase
Phase is the calculated phase shift from source 1 to source 2, expressed in
degrees. Negative phase shift values indicate that the rising edge of source 1
occurred after the rising edge of source 2.
|  |
|---|
|  |

---
**[Page 265]**

14 Measurements
266 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Delay
Phase = × 360
Source 1 Period
Period
Source 1
Delay
Source 2
1 Press the [Meas] key to display the Measurement Menu.
2 Press the Source softkey; then turn the Entry knob to select the first analog
channel source.
3 Press the Type: softkey; then, turn the Entry knob to select Delay.
4 Press the Settings softkey to select the second analog channel source for the
phase measurement.
The default Phase settings measure from channel 1 to channel 2.
5 Press the Back Back/Up key to return to the Measurement Menu.
6 Press the Add Measurement softkey to make the measurement.
The example below shows a phase measurement between the channel 1 and the
math d/dt function on channel 1.
| Delay
Phase = × 360
Source 1 Period |
|---|
|  |
| Period
Source 1
Delay
Source 2 |
|---|
|  |

---
**[Page 266]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 267
X at Min Y
X at Min Y is the X axis value (usually time) at the first displayed occurrence of the
waveform Minimum, starting from the left-side of the display. For periodic signals,
the position of the minimum may vary throughout the waveform. The X cursor
shows where the current X at Min Y value is being measured.
X at Max Y
X at Max Y is the X axis value (usually time) at the first displayed occurrence of the
waveform Maximum, starting from the left-side of the display. For periodic signals,
the position of the maximum may vary throughout the waveform. The X cursor
shows where the current X at Max Y value is being measured.
See Also • “To measure the peak of an FFT"on page267
To measure the peak of an FFT
1 Select FFT as the Operator in the Waveform Math Menu.
|  |
|---|
|  |

---
**[Page 267]**

14 Measurements
268 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 Choose Math N as the source in the Measurement Menu.
3 Choose Maximum and X at Max Y measurements.
Maximum units are in dB and X at Max Y units are in Hertz for FFT.
See Also • “Searching for FFT Peaks"on page105
Count Measurements
• “Positive Pulse Count"on page268
• “Negative Pulse Count"on page268
• “Rising Edge Count"on page269
• “Falling Edges Count"on page269
Positive Pulse Count
The Positive Pulse Count measurement is a pulse count for the selected waveform
source.
Positive pulse count
This measurement is available for analog channels.
Negative Pulse Count
The Negative Pulse Count measurement is a pulse count for the selected waveform
source.
| Positive pulse count |
|---|
|  |

---
**[Page 268]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 269
Negative pulse count
This measurement is available for analog channels.
Rising Edge Count
The Rising Edge Count measurement is an edge count for the selected waveform
source.
This measurement is available for analog channels.
Falling Edges Count
The Falling Edges Count measurement is an edge count for the selected waveform
source.
This measurement is available for analog channels.
Mixed Measurements
• “Area"on page269
Area
Area measures the area between the waveform and the ground level. Area below
the ground level is subtracted from area above the ground level.
| Negative pulse count |
|---|
|  |

---
**[Page 269]**

14 Measurements
270 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Positive area
T
N cycles
Negative area
The Full Screen measurement interval variation measures the value on all
displayed data points.
The N Cycles measurement interval variation measures the value on an integral
number of periods of the displayed signal. If less than three edges are present, the
measurement shows "No edges".
The X cursors show what interval of the waveform is being measured.
Measurement Thresholds
Setting measurement thresholds defines the vertical levels where measurements
will be taken on an analog channel or math waveform.
Changing default thresholds may change measurement results
NOTE
The default lower, middle, and upper threshold values are 10%, 50%, and 90% of the value
between Top and Base. Changing these threshold definitions from the default values may
change the returned measurement results for Average, Delay, Duty Cycle, Fall Time,
Frequency, Overshoot, Period, Phase, Preshoot, Rise Time, +Width, and -Width.
1 From the Measurement Menu, press the Settings softkey; then, press the
Thresholds softkey to set analog channel measurement thresholds.
You can also open the Measurement Threshold Menu by pressing [Analyze] >
Features and then selecting Measurement Thresholds.
2 Press the Source softkey to select the analog channel or math waveform source
for which you want to change measurement thresholds.
| Positive area
T
N cycles
Negative area |
|---|
|  |
| NOTE |
|---|
|  |

---
**[Page 270]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 271
Each analog channel and the math waveform can be assigned unique threshold
values.
3 Press the Type softkey to set the measurement threshold to % (percentage of
Top and Base value) or to Absolute (absolute value).
• Percentage thresholds can be set from 0% to 100%.
• The units for absolute threshold for each channel is set in the channel probe
menu.
Absolute threshold hints
TIP
• Absolute thresholds are dependent on channel scaling, probe attenuation, and probe units. Always
set these values first before setting absolute thresholds.
• The minimum and maximum threshold values are limited to on-screen values.
• If any of the absolute threshold values are above or below the minimum or maximum waveform
values, the measurement may not be valid.
4 Press the Lower softkey; then, turn the Entry knob to set the lower measurement
threshold value.
Increasing the lower value beyond the set middle value will automatically
increase the middle value to be more than the lower value. The default lower
threshold is 10% or 800mV.
If threshold Type is set to %, the lower threshold value can be set from 0% to
98%.
5 Press the Middle softkey; then, turn the Entry knob to set the middle
measurement threshold value.
The middle value is bounded by the values set for lower and upper thresholds.
The default middle threshold is 50% or 1.20V.
• If threshold Type is set to %, the middle threshold value can be set from 1% to
99%.
6 Press the Upper softkey; then, turn the Entry knob to set the upper
measurement threshold value.
|  |  |
|---|---|
| TIP |
|---|
|  |

---
**[Page 271]**

14 Measurements
272 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Decreasing the upper value below the set middle value will automatically
decrease the middle value to be less than the upper value. The default upper
threshold is 90% or 1.50V.
• If threshold Type is set to %, the upper threshold value can be set from 2% to
100%.
Measurement Window
You can choose whether measurements are made in the Main window portion of
the display, the Zoom window portion of the display (when the zoomed time base
is displayed), or gated by the X1 and X2 cursors.
1 Press the [Meas] key.
2 In the Measurement Menu, press the Settings softkey.
3 In the Measurement Settings Menu, press the Meas Window softkey; then, turn
the Entry knob to select from:
• Auto Select — When the zoomed time base is displayed, the measurement is
attempted in the lower, Zoom window; if it cannot be made there, or if the
zoomed time base is not displayed, the Main window is used.
• Main — The measurement window is the Main window.
• Zoom — The measurement window is the lower, Zoom window.
• Gated by Cursors — The measurement window is between the X1 and X2
cursors. When the zoomed time base is displayed, the X1 and X2 cursors in
the Zoom window portion of the display are used.
Measurement Statistics
To display measurement statistics:
1 Press the [Meas] key to enter the Measurement Menu. By default frequency and
peak-to-peak voltage are measured on channel 1.
2 Select the measurements you desire for the channels you are using (see
“Measurements Summary"on page248).
3 From the Measurement Menu, press the Statistics softkey to enter the Statistics
Menu.

---
**[Page 272]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 273
4 Press the Display On softkey to enable the measurement statistics display.
The source channel of the measurement is shown in parenthesis after the
measurement name. For example: "Freq(1)" indicates a frequency measurement
on channel 1.
The following statistics are shown: Name of the measurement, current
measured value, mean, minimum measured value, maximum measured value,
standard deviation, and the number of times the measurement has been made
(count). Statistics are based on the total number of captured waveforms
(count).
The standard deviation shown in Statistics is calculated using the same formula
used for calculating the standard deviation measurement. The formula is shown
in the section titled “AC RMS"on page258.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 273]**

14 Measurements
274 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You can press the Display On softkey again to disable the measurement statistics
display. Statistics continue to accumulate even when the statistics display is
disabled.
5 To reset the statistics measurements, press the Reset Statistics softkey. This
resets all statistics and begins recording statistical data again.
Each time a new measurement (for example: frequency, period, or amplitude) is
added the statistics are reset and accumulation of statistical data begins again.
6 To enable a relative standard deviation, press the Relativeσ softkey.
When enabled, the standard deviation shown in measurement statistics
becomes the standard deviation/mean.
7 To specify the number of values used when calculating measurement statistics,
press the Max Count softkey and enter the desired value.
Other things to know about measurement statistics:
• When the [Single] key is pressed, statistics are reset and a single measurement
is done (count = 1). Successive [Single] acquisitions accumulate statistical data
(and the count is incremented).
• The Increment Statistics softkey only appears when the acquisition is stopped
and the optional segmented memory feature is off. Press the [Single] or
[Run/Stop] key to stop the acquisition. You can use the horizontal position
control (in the Horizontal control section of the front panel) to pan through the
waveform. Active measurements will stay on screen, allowing you to measure
various aspects of the captured waveforms. Press Increment Statistics to add the
currently measured waveform to the collected statistical data.
• The Analyze Segments softkey only appears when the acquisition is stopped and
the optional segmented memory feature is on. After an acquisition has
completed (and the oscilloscope is stopped), you can press the Analyze
Segments softkey to accumulate measurement statistics for the acquired
segments.
You can also turn on infinite persistence (in the Display Menu) and press the
Analyze Segments softkey to create an infinite persistence display.

---
**[Page 274]**

Measurements 14
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 275
Precision Measurements and Math
Normally, after pressing [Default Setup], the oscilloscope performs measurements
and generates math waveforms using a 65535-point (maximum) measurement
record. This measurement record is purposely small in order to provide high
waveform update rates and minimal "dead time" between acquisitions to improve
the probability of capturing infrequent events.
However, at the expense of waveform update rate, you can enable precision
measurements and math waveforms that use a user-selectable 100k-point to
1M-point (maximum) record. This mode gives you better resolution on
measurements and math waveforms (including FFT).
To enable precision measurements and math:
1 Press the [Analyze] key.
2 Press Features; then, select Precision.
3 Press Features again to enable precision measurements and math waveforms.
4 Press the RecLength softkey and turn the Entry knob (or press the softkey again
for a keypad entry dialog) to specify the length of the precision analysis record.
You can specify between 100k and 1M points.
Precision measurements and math are disabled in the same way, or you can
disable them by pressing the [Default Setup] key.

---
**[Page 275]**

14 Measurements
276 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 276]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
277
15 Histogram
Waveform Histogram Set Up / 278
Measurement Histogram Set Up / 282
Histogram Data Graph / 283
Histogram Data Statistics / 284
The histogram analysis feature provides a statistical view of a waveform or a
measurement's results.
Waveform histograms show the number of times a waveform crosses into (or hits)
a row or column of a user-defined window. For vertical histograms, the window is
divided into rows. For horizontal histograms, the window is divided into columns.
Measurement histograms show the distribution of a measurement's results similar
to ordinary measurement statistics.
As waveforms are acquired and displayed, or as measurements are made, a
counter database accumulates the total number of hits (or measurements), and
the histogram data is displayed as a bar graph on the graticule.
When the oscilloscope is stopped, that counter database remains intact until the
acquired data display is modified, usually horizontally or vertically. At that time,
the database is reset and the last displayed acquisition is used to start a new
database.
Histogram results statistics are displayed in a sidebar Hist dialog.
The following screen shows a horizontal histogram looking at edge times:

---
**[Page 277]**

15 Histogram
278 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Histogram When you enable a histogram, horizontal zoom, XY time mode, or roll time mode
Interaction With are automatically disabled.
Other Oscilloscope
When using segmented memory acquisitions, histograms perform similarly to
Features
math waveforms and measurements. The histogram is reset at the start of a
segmented acquisition and all segments are histogrammed at the end of the
acquisition.
Because it is not possible to histogram every waveform, be aware that persistence
can show a peak or glitch that does not show up in the histogram data.
Histograms do not wait for the specified number of averaged acquisitions to be
acquired before starting analysis, so intermediate results could be erratic.
Waveform Histogram Set Up
To set up a waveform histogram:
1 Press the [Analyze] key.
|  |
|---|
|  |

---
**[Page 278]**

Histogram 15
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 279
2 Press Features; then, select Histogram.
3 Press Features again to enable the histogram.
4 Press the Type softkey and turn the Entry knob to select:
• Horizontal — the limits window is divided into columns, and the number of
hits in each column is displayed in a histogram bar graph at the bottom of
the graticule.
• Vertical — the limits window is divided into rows, and the number of hits in
each row is displayed in a histogram bar graph at the left of the graticule.
5 Press the Source softkey to select the analog channel, running math function,
reference waveform, or color grade analysis to analyze.
6 Define the limits window in which waveform crossings (hits) are measured. See
“Defining the Histogram Limits Window"on page280.
7 Press the Histogram Size softkey and specify the number of divisions the
histogram bar graph should use:
• For horizontal histograms, you can choose whole and half divisions from 1 to
4.
• For vertical histograms, you can choose whole and half divisions from 1 to 5.
You can press the Reset Histogram softkey to zero the histogram counters.
The following screen shows a vertical histogram of auto-triggered noise — note
the Gaussian distribution:
|  |  |
|---|---|

---
**[Page 279]**

15 Histogram
280 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Defining the Histogram Limits Window
You can define the histogram limits window by drawing a rectangle on the screen:
1 Touch the upper-right corner to select the rectangle draw mode.
2 Drag your finger (or connected USB mouse pointer) across the screen to draw a
rectangular zone that the waveform must either intersect or not intersect.
3 Take your finger off the screen (or release the mouse button).
4 Choose Histogram from the popup menu.
|  |
|---|
|  |
|  |  |
|---|---|

---
**[Page 280]**

Histogram 15
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 281
You can also define the histogram limits window by selecting the default window
(which is six divisions tall and eight divisions wide, centered on the graticule):
1 First, set up the horizontal and vertical scaling so that the waveform of interest
is centered in the graticule.
2 Press [Analyze] > Features; then, select and enable Histogram.
3 Press the Limits softkey.
The Limits softkey is active when the Type is Horizontal or Vertical.
4 In the Histogram Limits Menu, press the Default Window softkey.
When the Histogram Limits Menu is being displayed, you can adjust the limits
window by dragging its touch handles. The upper left corner touch handle moves
the window, and the lower right corner touch handle changes the size of the
window.
|  |  |
|---|---|

---
**[Page 281]**

15 Histogram
282 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You can also adjust the size and location of the limits window by using the Top
Limit, Bottom Limit, Left Limit, or Right Limit softkeys and the Entry knob or keypad
dialogs.
Measurement Histogram Set Up
To set up a measurement histogram:
1 First, add the measurement whose results you want to display as a histogram.
See “To make automatic measurements"on page246.
2 Press the [Analyze] key.
3 Press Features; then, select Histogram.
4 Press Features again to enable the histogram.
|  |
|---|
|  |

---
**[Page 282]**

Histogram 15
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 283
5 Press the Type softkey and turn the Entry knob to select:
• Measurements — shows the distribution of a measurement's results similar to
ordinary measurement statistics.
6 Press the Measurement softkey to select the measurement to analyze.
7 Press the Histogram Size softkey and specify the number of divisions the
histogram bar graph should use. You can choose whole and half divisions from
1 to 4.
For measurement histograms, information about the scale of the bar graph
appears above the softkeys. This scale is automatically determined.
You can press the Reset Histogram softkey to zero the histogram counters.
Histogram Data Graph
The visual component of a histogram is the bar graph on the display.
This graph appears on the left side of the graticule area for a vertical waveform
histogram or on the graticule bottom for a horizontal waveform histogram or a
measurement histogram.
For measurement histograms, information about the scale of the bar graph
appears above the softkeys. This scale is automatically determined.
As waveforms are acquired and displayed, or as measurements are made, the bar
graph scale changes so that the peak number of hits is displayed at the histogram
size specified.
The Reset Histogram softkey zeros the histogram counters.
Cursors on When the histogram analysis feature is enabled and when cursors are in Manual or
Histogram Data Track Waveform mode, Histogram is added to the list of sources you can select for
cursors.
If you are doing a measurement on a histogram, cursors track that measurement
on the histogram waveform.
|  |  |
|---|---|

---
**[Page 283]**

15 Histogram
284 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
When cursors are in the Track Waveform mode, the X or the Y cursor is moveable
depending on whether the histogram type is horizontal, vertical, or measurement.
Histogram Data Statistics
Histogram data results are displayed in the Hist sidebar dialog (which can be
selected from the right-hand sidebar menu — see “Select Sidebar Information or
Controls"on page49 and “Undock Sidebar Dialogs by Dragging"on page50).
There are several standard results that can be derived from the histogram
database.
The basic units of histograms are hits, and there are some results that are
expressed as hits:
• Hits — The sum of all bins (buckets) in the histogram.
• Peak — Maximum number of hits in any single bin.
|  |
|---|
|  |

---
**[Page 284]**

Histogram 15
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 285
Some results are expressed in the source's (vertical, horizontal or measurement)
units:
• Max — The value corresponding to the maximum bin that has any hits.
• Min — The value corresponding to the minimum bin that has any hits.
• Pk-Pk — Delta between the Max and Min.
• Mean — Mean of the histogram.
• Median — Median of the histogram.
• Mode — Mode of the histogram.
• Bin Width — The width of each bin (bucket) in the histogram.
• Std Dev — Standard deviation of the histogram.
Some results are derived from other results:
• u±1σ — Percentage of histogram hits that lie within ±1 Std Dev of the mean.
• u±2σ — Percentage of histogram hits that lie within ±2 Std Dev of the mean.
• u±3σ — Percentage of histogram hits that lie within ±3 Std Dev of the mean.
You can touch any of the individual entries in the sidebar and reset the histogram results.
NOTE
| NOTE |
|---|
|  |

---
**[Page 285]**

15 Histogram
286 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 286]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
287
16 Color Grade Waveform
Enabling a Color Grade Waveform / 288
Color Grade Themes / 290
The color grade analysis feature shows how often a waveform crosses into (or hits)
pixels on the display. As waveforms are acquired and displayed, a counter
database accumulates the number of hits, and pixels in the color grade analysis
waveform are displayed using one of seven graduated colors that indicate a
relative number of hits. You can choose temperature or intensity color grade
scales (themes).
When the oscilloscope is stopped, the counter database remains intact until the
acquired data display is modified, usually horizontally or vertically. At that time,
the database is reset and the last displayed acquisition is used to start a new
database.
The following screen shows a color grade analysis waveform for channel 2:

---
**[Page 287]**

16 Color Grade Waveform
288 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The color grade analysis display is updated every second or so.
Over time, you can see the nominal waveform as well as the waveform's envelope.
When any of the database counters saturate, the message The color grade database
is saturated is displayed above the softkeys in the in the color grade analysis menu.
Color grade analysis works best on repetitive waveforms.
Color Grade When you enable a color grade waveform display, horizontal zoom, XY time mode,
Interaction With or roll time mode are automatically disabled.
Other Oscilloscope
Features
Enabling a Color Grade Waveform
To set up color grade analysis of a waveform:
1 Press the [Analyze] key.
|  |
|---|
|  |

---
**[Page 288]**

Color Grade Waveform 16
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 289
2 Press Features; then, select Color Grade.
3 Press Features again to enable the color grade waveform display.
4 Press the Source softkey to select the analog channel, running math function, or
reference waveform to analyze.
5 Press the Show Color Key softkey to see the color grade theme's seven colors
and the range of database counts that each color represents.
6 Press the Theme softkey and select Intensity or Temperature. For a description of
the colors used in these themes, see “Color Grade Themes"on page290.
You can press the Reset Color Grade softkey to zero the color grade counters.
Changing the horizontal time/div or delay settings, or the channel's vertical V/div
or offset settings, or the source waveform will also zero the color grade counters.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 289]**

16 Color Grade Waveform
290 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Color Grade Themes
When color grade analysis is enabled, a database is created that has the same
number of memory locations as there are pixel locations in the waveform viewing
area. Each database memory location is a counter. These counters are
incremented when sampled waveform data crosses (or "hits") the associated pixel.
The color grade theme specifies seven colors that represent the ranges of counter
values (hits) in the database. The color used for the greatest number of hits (white
in both themes) represents pixels with the greatest number to about half that
number. The next color represents half as many hits, and so on, until the last range
(green in the "intensity" theme or dark blue in the "temperature" theme) represents
the remaining range of hits.
The following table shows the approximate counter ranges of each color in the
Intensity and Temperature color grade themes.
Color Grade Theme Range (MH = most hits)
Intensity Temperature Upper Limit to Lower Limit (0 if Upper
Limit is 0, Else)
MH to MH/2
MH/2 to MH/4
MH/4 to MH/8
MH/8 to MH/16
MH/16 to MH/32
MH/32 to MH/64
MH/64 to 1
| Color Grade Theme |  | Range (MH = most hits) |  |  |
|---|---|---|---|---|
| Intensity | Temperature | Upper Limit | to | Lower Limit (0 if Upper
Limit is 0, Else) |
|  |  | MH | to | MH/2 |
|  |  | MH/2 | to | MH/4 |
|  |  | MH/4 | to | MH/8 |
|  |  | MH/8 | to | MH/16 |
|  |  | MH/16 | to | MH/32 |
|  |  | MH/32 | to | MH/64 |
|  |  | MH/64 | to | 1 |

---
**[Page 290]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
291
17 Jitter and Real-Time Eye
Analysis
Setting Up Jitter Analysis / 292
Jitter Measurements / 295
Real-Time Eye Analysis / 299
Jitter analysis measures the variance of a measurement over time. The principal
measurement used with jitter analysis is time interval error (TIE), but several other
measurements can be analyzed as well.
The TIE measurement recovers an ideal clock frequency from the source waveform
and compares it against measured transitions to generate error statistics. Several
different clock recovery methods are available.
Jitter measurements can be visualized in these ways:
• Meas Histogram — Shows the distribution of jitter measurement results.
Gaussian distributions indicate random jitter. Non-Gaussian distributions
usually indicate that the jitter has deterministic components. Measurement
statistics are displayed along with the histogram.
• Meas Trend — Shows the trend of jitter measurement results. The trend
waveform over a greater time can show shapes or patterns that indicate what
might be affecting jitter.
• Jitter Spectrum — Shows the jitter measurement trend in the frequency
domain. Spikes in the FFT show frequencies of what might be affecting jitter.

---
**[Page 291]**

17 Jitter and Real-Time Eye Analysis
292 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
For more information, see Measuring Jitter in Digital Systems, Application Note
(http://literature.cdn.keysight.com/litweb/pdf/5988-9109EN.pdf)
Setting Up Jitter Analysis
To set up jitter analysis:
1 Press the [Jitter] key.
2 In the Jitter Configuration dialog, select Enable Jitter Analysis.
When jitter analysis is enabled, the [Jitter] key is lit, and these oscilloscope
settings are forced on:
• Precision measurements with a 1M precision analysis record length (see
“Precision Measurements and Math"on page275), which gives better
accuracy.
|  |
|---|
|  |

---
**[Page 292]**

Jitter and Real-Time Eye Analysis 17
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 293
• All edges in each acquisition are measured (instead of a single edge per
acquisition, as is normally the case). For each acquisition, the measurement
count increases by the number of edges in the acquisition. This applies to all
measurements that look at edges, not just jitter analysis measurements.
3 To change the measurement thresholds settings, touch Measurement
Thresholds... and use the softkeys in the Measurement Threshold Menu to
change the settings (see “Measurement Thresholds"on page270).
It is important to set up absolute thresholds for the integrity of jitter measurements from
NOTE
acquisition to acquisition.
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 293]**

17 Jitter and Real-Time Eye Analysis
294 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
4 To add a jitter measurement:
a Touch Add Measurement...; then, select the jitter measurement you want from
the popup menu.
b In the Measurement dialog, select the Source to be measured and select any
other measurement options (see “Jitter Measurements"on page295 or
“Duty Cycle"on page263).
The source can be analog channels, math waveforms, or reference
waveforms.
c Touch OK.
When jitter analysis is enabled, you can also add or modify jitter measurements
using the [Meas] key and the Measurement Menu (see “To make automatic
measurements"on page246).
5 Back in the Jitter Configuration dialog, touch the Analysis Measurement
drop-down and choose the jitter measurement you want to analyze.
6 In the Auto Setup & Configuration area, set up the jitter measurement visualization
options using these controls:
• Meas Histogram — The Auto Setup control enables a histogram on the selected
jitter analysis measurement. The settings control opens the softkey
histogram analysis menu (see “Measurement Histogram Set Up"on
page282).
• Meas Trend — The Auto Setup control sets up a measurement trend waveform
on the selected jitter analysis measurement. The settings control opens the
softkey menu for the measurement trend math waveform (see
“Measurement Trend"on page118).
• Jitter Spectrum — The Auto Setup control sets up an FFT of the measurement
trend waveform on the selected jitter measurement. The settings control
opens the softkey menu for the FFT math waveform (see “FFT Spectrum"on
page101).
Note that another math function is set up to perform smoothing on the
measurement trend waveform. You can change the FFT's source to be the
smoothed trend waveform if you like.
7 When you are done setting up the jitter analysis options, press the [Jitter] key
again to close the Jitter Configuration dialog.
To disable jitter analysis:

---
**[Page 294]**

Jitter and Real-Time Eye Analysis 17
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 295
1 In the Jitter Configuration dialog (press the [Jitter] key if the dialog is not
currently displayed), deselect Enable Jitter Analysis.
When jitter analysis is disabled:
• The light behind the [Jitter] key is turned off.
• The "precision measurements" and 1M precision analysis record length
settings are returned to the settings present when jitter analysis was
enabled.
• The oscilloscope returns to measuring a specific edge in each acquisition
(generally around the horizontal time reference) and ignoring all other edges
in the acquisition, as is normally the case. For each acquisition, the
measurement count increases by one.
Jitter Measurements
• “Data TIE"on page295
• “Clock TIE"on page296
• “N-Period"on page296
• “Period-Period"on page297
• “+Width to +Width"on page298
• “-Width to -Width"on page298
Data TIE
The Data TIE (Time Interval Error) jitter measurement compares edges in a data
signal with the edges in an ideal data signal determined by the clock recovery
feature (see “Setting Up Clock Recovery"on page122).
Once the ideal data rate is determined, all of the data intervals are measured with
respect to the ideal data rate and the error statistics are computed. The following
figure shows how the Data TIE is measured on rising edges of the data.

---
**[Page 295]**

17 Jitter and Real-Time Eye Analysis
296 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Data TIE
Measured Data
t1 t2 t3
Ideal Clock
The measurement is made on all the cycles of the waveform. Even in Zoom mode,
all the cycles of the waveform in the Main window will be measured.
Clock TIE
The Clock TIE (Time Interval Error) jitter measurement compares edges in a clock
signal with the edges in an ideal clock signal determined by the clock recovery
feature (see “Setting Up Clock Recovery"on page122). You can measure rising,
falling, or both rising and falling edges.
Once the ideal clock frequency is determined, all of the cycles of your waveform
are compared to the ideal clock frequency and the error statistics are computed.
The following figure shows how the Clock TIE is measured on rising edges of the
clock.
Clock TIE
Measured Clock
t1 t2 t3 t4 t5 t6
Ideal Clock
The measurement is made on all the cycles of the waveform. Even in Zoom mode,
all the cycles of the waveform in the Main window will be measured.
N-Period
The N-Period jitter measurement measures the time span of N consecutive
periods. Then, it shifts ahead one period and measures the time span of the next N
consecutive periods, and so on.
| Data TIE
Measured Data
t1 t2 t3
Ideal Clock |  |
|---|---|
|  |  |
|  |  |
|  |  |
| Clock TIE
Measured Clock
t1 t2 t3 t4 t5 t6
Ideal Clock |  |
|---|---|
|  |  |
|  |  |
|  |  |

---
**[Page 296]**

Jitter and Real-Time Eye Analysis 17
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 297
N = 3
Period 1
Period 2
Period-Period
The Period-Period jitter measurement takes a group of cycles and measures the
period from the first edge of the first cycle of the group to the final edge of the last
cycle of the group. The N-period of the first group is measured and subtracted
from the N-period of the second group. After shifting ahead one cycle the next
measurement is made. The following figure shows how an N-cycle jitter
measurement is made for N=3.
N = 3
Period 1 Period 2
1st Measurement = Period 2 - Period 1
Period 3 Period 4
2nd Measurement = Period 4 - Period 3
Once all of the groups of cycles of the waveform are measured, the statistics are
calculated. The statistics are the values accumulated over all of the trigger cycles
that have occurred.
To perform a cycle-cycle jitter measurement, use Period-Period and set N=1.
The measurement is made on all the cycles of the waveform. Even in Zoom mode,
all the cycles of the waveform in the Main window will be measured.
| N = 3
Period 1
Period 2 |
|---|
|  |
| N = 3
Period 1 Period 2
1st Measurement = Period 2 - Period 1
Period 3 Period 4
2nd Measurement = Period 4 - Period 3 |
|---|
|  |

---
**[Page 297]**

17 Jitter and Real-Time Eye Analysis
298 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
+Width to +Width
The +Width to +Width jitter measurement subtracts the first cycle's positive pulse
width from the second cycle's positive pulse width for the first measurement
result. Then, the second cycle's positive pulse width is subtracted from the third
cycle's positive pulse width for the second measurement result, and so on, until all
of the cycles of the waveform have been measured. The following figure shows the
first two +Width to +Width measurements.
+Width1 +Width2
1st Measurement = +Width2 - +Width1
+Width2 +Width3
2nd Measurement = +Width3 - +Width2
All of the measurement results are used to compute the statistics. The statistics
are the values accumulated over all of the trigger cycles that have occurred.
The measurement is made on all the cycles of the waveform. Even in Zoom mode,
all the cycles of the waveform in the Main window will be measured.
-Width to -Width
The -Width to -Width jitter measurement subtracts the first cycle's negative pulse
width from the second cycle's negative pulse width for the first measurement
result. Then, the second cycle's negative pulse width is subtracted from the third
cycle's negative pulse width for the second measurement result, and so on, until
all of the cycles of the waveform have been measured. The following figure shows
the first two -Width to -Width measurements.

---
**[Page 298]**

Jitter and Real-Time Eye Analysis 17
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 299
-Width1 -Width2
1st Measurement = -Width2 - -Width1
-Width2 -Width3
2nd Measurement = -Width3 - -Width2
All of the measurement results are used to compute the statistics. The statistics
are the values accumulated over all of the trigger cycles that have occurred.
The measurement is made on all the cycles of the waveform. Even in Zoom mode,
all the cycles of the waveform in the Main window will be measured.
Real-Time Eye Analysis
When the jitter analysis feature is licensed, you can also perform real-time eye
analysis.
An eye diagram is a view of a signal in which the waveform is triggered using its
data rate. A real-time eye accomplishes this by acquiring data, performing clock
recovery, then superimposing (folding) successive unit intervals within a single
plot. This is a statistical view in the form of a color grade.
When real-time eye analysis is enabled, the color grade analysis feature is no
longer available.
Mask testing and unfolding the real-time eye (features available with real-time
eyes on other Keysight oscilloscopes) are not available on this oscilloscope.
To set up real-time eye analysis of a waveform:
1 Press the [Analyze] key.
2 Press Features; then, select Real-Time Eye.
3 Press Features again to enable the real-time eye display.

---
**[Page 299]**

17 Jitter and Real-Time Eye Analysis
300 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
4 Press the Source softkey to select the analog channel to analyze.
5 Press the Clock Recovery... softkey to open a dialog where you can set up the
clock recovery feature (see “Setting Up Clock Recovery"on page122).
6 Press the Thresholds softkey and use the softkeys in the Measurement Threshold
Menu to change the settings (see “Measurement Thresholds"on page270).
7 Press the Color Grade softkey and use the softkeys in the Color Grade Setup
Menu to change the settings (see Chapter16, “Color Grade Waveform,”
starting on page 287).
8 Adjust the oscilloscope's horizontal scale.
9 To begin making acquisitions, press the Auto Setup softkey.
When building the real-time eye, full-length acquisitions are used to get the
largest acquisition record possible, resulting in the most accurate clock
recovery and eye measurements possible.
|  |  |
|---|---|

---
**[Page 300]**

Jitter and Real-Time Eye Analysis 17
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 301
10To stop real-time eye analysis acquisitions, press the [Stop] front panel key.
When real-time eye analysis is enabled, you can press the [Meas] key, select Color
Grade as the measurement source, and add these real-time eye measurements
(made using the color grade database):
• Eye Height — the vertical opening of an eye diagram. The opening at the center
time reference is reported.
• Eye Width — the horizontal opening of an eye diagram. The largest opening
within the crossings is reported.
To clear the real-time eye analysis, press the Reset Color Grade softkey in the Color
Grade Setup Menu.
|  |  |
|---|---|

---
**[Page 301]**

17 Jitter and Real-Time Eye Analysis
302 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 302]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
303
18 Mask Testing
To create a mask from a "golden" waveform (Automask) / 303
Mask Test Setup Options / 305
Mask Statistics / 308
To manually modify a mask file / 309
Building a Mask File / 312
One way to verify a waveform's compliance to a particular set of parameters is to
use mask testing. A mask defines a region of the oscilloscope's display in which
the waveform must remain in order to comply with chosen parameters.
Compliance to the mask is verified point-by-point across the display. Mask test
operates on displayed analog channels; it does not operate on channels that are
not displayed.
To enable mask test order Option LMT at time of oscilloscope purchase, or order
DSOX6MASK as a stand-alone item after oscilloscope purchase.
To create a mask from a "golden" waveform (Automask)
A golden waveform meets all chosen parameters, and it is the waveform to which
all others will be compared.
1 Configure the oscilloscope to display the golden waveform.
2 Press the [Analyze] key.
3 Press Features; then, select Mask Test.
4 Press Features again to enable mask testing.

---
**[Page 303]**

18 Mask Testing
304 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
5 Press Automask.
6 In the Automask Menu, press the Source softkey and ensure the desired analog
channel is selected.
7 Adjust the mask's horizontal tolerance (±Y) and vertical tolerance (±X). These
are adjustable in graticule divisions or in absolute units (volts or seconds),
selectable using the Units softkey.
8 Press the Create Mask softkey.
The mask is created and testing begins.
Whenever the Create Mask softkey is pressed the old mask is erased and a new
mask is created.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 304]**

Mask Testing 18
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 305
9 To clear the mask and switch off mask testing, press the Back Back/Up key to
return to the Mask Test Menu, then press the Clear Mask softkey.
If infinite persistence display mode (see “To set or clear persistence"on page157)
is "on" when mask test is enabled, it stays on. If infinite persistence is "off" when
mask test is enabled, it is switched on when mask test is switched on, then infinite
persistence is switched off when mask test is switched off.
Troubleshooting If you press Create Mask and the mask appears to cover the entire screen, check the
Mask Setup ±Y and ±X settings in the Automask Menu. If these are set to zero the resulting
mask will be extremely tight around the waveform.
If you press Create Mask and it appears that no mask was created, check the ±Y
and ±X settings. They may be set so large that the mask is not visible.
Mask Test Setup Options
From the Mask Test Menu, press the Setup softkey to enter the Mask Setup Menu.
|  |  |
|---|---|

---
**[Page 305]**

18 Mask Testing
306 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Run Until The Run Until softkey lets you specify a condition on which to terminate testing.
• Forever — The oscilloscope runs continuously. However, if an error occurs the
action specified using the OnError softkey will occur.
• Minimum # of Tests — Choose this option and then use the #ofTests softkey
to select the number of times the oscilloscope will trigger, display the
waveform(s), and compare them to the mask. The oscilloscope will stop after
the specified number of tests have been completed. The specified minimum
number of tests may be exceeded. If an error occurs the action specified
using the OnError softkey will occur. The actual number of tests completed
is displayed above the softkeys.
• Minimum Time — Choose this option and then use the TestTime softkey to
select how long the oscilloscope will run. When the selected time has passed
the oscilloscope will stop. The specified time may be exceeded. If an error
occurs the action specified using the OnError softkey will occur. The actual
test time is displayed above the softkeys.
• Minimum Sigma — Choose this option and then use the Sigma softkey to
select a minimum sigma. The mask test runs until enough waveforms are
tested to achieve a minimum test sigma. (If an error occurs the oscilloscope
will perform the action specified by the OnError softkey.) Note that this is a
test sigma (the max achievable process sigma, assuming no defects, for a
certain number of tested waveforms) as opposed to a process sigma (which is
tied to the amount of failures per test). The sigma value may exceed the
selected value when a small sigma value is chosen. The actual sigma is
displayed.
| Run Until | The Run Until softkey lets you specify a condition on which to terminate testing.
• Forever — The oscilloscope runs continuously. However, if an error occurs the
action specified using the OnError softkey will occur.
• Minimum # of Tests — Choose this option and then use the #ofTests softkey
to select the number of times the oscilloscope will trigger, display the
waveform(s), and compare them to the mask. The oscilloscope will stop after
the specified number of tests have been completed. The specified minimum
number of tests may be exceeded. If an error occurs the action specified
using the OnError softkey will occur. The actual number of tests completed
is displayed above the softkeys.
• Minimum Time — Choose this option and then use the TestTime softkey to
select how long the oscilloscope will run. When the selected time has passed
the oscilloscope will stop. The specified time may be exceeded. If an error
occurs the action specified using the OnError softkey will occur. The actual
test time is displayed above the softkeys.
• Minimum Sigma — Choose this option and then use the Sigma softkey to
select a minimum sigma. The mask test runs until enough waveforms are
tested to achieve a minimum test sigma. (If an error occurs the oscilloscope
will perform the action specified by the OnError softkey.) Note that this is a
test sigma (the max achievable process sigma, assuming no defects, for a
certain number of tested waveforms) as opposed to a process sigma (which is
tied to the amount of failures per test). The sigma value may exceed the
selected value when a small sigma value is chosen. The actual sigma is
displayed. |
|---|---|

---
**[Page 306]**

Mask Testing 18
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 307
On Error The On Error setting specifies the action(s) to take when the input waveform
does not conform to the mask. This setting supersedes the Run Until setting.
• Stop — The oscilloscope will stop when the first error is detected (on the first
waveform that does not conform to the mask). This setting supersedes the
Minimum # of Tests and Minimum Time settings.
• Save — The oscilloscope saves the screen image when an error is detected. In
the Save Menu (press [Save/Recall] > Save), select an image format (*.bmp
or *.png), destination (on a USB storage device), and file name (which can be
auto-incrementing). If errors occur too frequently and the oscilloscope
spends all its time saving images, press the [Stop] key to stop acquisitions.
• Print — The oscilloscope prints the screen image when an error is detected.
This option is only available when a printer is connected as described in “To
print the oscilloscope's display"on page357.
• Measure — Measurements (and measurement statistics if your oscilloscope
supports them) run only on waveforms that contain a mask violation.
Measurements are not affected by passing waveforms. This mode is not
available when the acquisition mode is set to Averaging.
Note that you can choose to Print or Save, but you cannot select both at the
same time. All other actions may be selected at the same time. For example, you
can select both Stop and Measure to cause the oscilloscope to measure and
stop on the first error..
You can also output a signal on the rear panel TRIGOUT BNC connector when
there is a mask test failure. See “Setting the Rear Panel TRIG OUT
Source"on page374.
Source Lock When you turn on Source Lock using the Source Lock softkey, the mask is
redrawn to match the source whenever you move the waveform. For example, if
you change the horizontal timebase or the vertical gain the mask is redrawn with
the new settings.
When you turn off Source Lock, the mask is not redrawn when horizontal or
vertical settings are changed.
Source If you change the Source channel, the mask is not erased. It is re-scaled to the
vertical gain and offset settings of the channel to which it is assigned. To create
a new mask for the selected source channel, go back up in the menu hierarchy;
then, press Automask, and press Create Mask.
The Source softkey in the Mask Setup Menu is the same as the Source softkey in
the Automask Menu.
Test All When enabled, all displayed analog channels are included in the mask test.
When disabled, just the selected source channel is included in the test.
| On Error | The On Error setting specifies the action(s) to take when the input waveform
does not conform to the mask. This setting supersedes the Run Until setting.
• Stop — The oscilloscope will stop when the first error is detected (on the first
waveform that does not conform to the mask). This setting supersedes the
Minimum # of Tests and Minimum Time settings.
• Save — The oscilloscope saves the screen image when an error is detected. In
the Save Menu (press [Save/Recall] > Save), select an image format (*.bmp
or *.png), destination (on a USB storage device), and file name (which can be
auto-incrementing). If errors occur too frequently and the oscilloscope
spends all its time saving images, press the [Stop] key to stop acquisitions.
• Print — The oscilloscope prints the screen image when an error is detected.
This option is only available when a printer is connected as described in “To
print the oscilloscope's display"on page357.
• Measure — Measurements (and measurement statistics if your oscilloscope
supports them) run only on waveforms that contain a mask violation.
Measurements are not affected by passing waveforms. This mode is not
available when the acquisition mode is set to Averaging.
Note that you can choose to Print or Save, but you cannot select both at the
same time. All other actions may be selected at the same time. For example, you
can select both Stop and Measure to cause the oscilloscope to measure and
stop on the first error..
You can also output a signal on the rear panel TRIGOUT BNC connector when
there is a mask test failure. See “Setting the Rear Panel TRIG OUT
Source"on page374. |
|---|---|
| Source Lock | When you turn on Source Lock using the Source Lock softkey, the mask is
redrawn to match the source whenever you move the waveform. For example, if
you change the horizontal timebase or the vertical gain the mask is redrawn with
the new settings.
When you turn off Source Lock, the mask is not redrawn when horizontal or
vertical settings are changed. |
| Source | If you change the Source channel, the mask is not erased. It is re-scaled to the
vertical gain and offset settings of the channel to which it is assigned. To create
a new mask for the selected source channel, go back up in the menu hierarchy;
then, press Automask, and press Create Mask.
The Source softkey in the Mask Setup Menu is the same as the Source softkey in
the Automask Menu. |
| Test All | When enabled, all displayed analog channels are included in the mask test.
When disabled, just the selected source channel is included in the test. |

---
**[Page 307]**

18 Mask Testing
308 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Mask Statistics
From the Mask Test Menu, press the Statistics softkey to enter the Mask Statistics
Menu.
Show Stats When you enable Show Statistics the following information is displayed:
• Current mask, name of mask, Channel number, date and time.
• # of Tests (total number of mask tests executed).
• Status (Passing, Failing, or Untested).
• Accumulated test time (in hours, minutes, seconds, and tenths of seconds).
And for each analog channel:
• Number of failures (acquisitions in which the signal excursion went beyond
the mask).
• Failure rate (percentage of failures).
• Sigma (the ratio of process sigma to maximum achievable sigma, based on
number of waveforms tested).
|  |
|---|
|  |
| Show Stats | When you enable Show Statistics the following information is displayed:
• Current mask, name of mask, Channel number, date and time.
• # of Tests (total number of mask tests executed).
• Status (Passing, Failing, or Untested).
• Accumulated test time (in hours, minutes, seconds, and tenths of seconds).
And for each analog channel:
• Number of failures (acquisitions in which the signal excursion went beyond
the mask).
• Failure rate (percentage of failures).
• Sigma (the ratio of process sigma to maximum achievable sigma, based on
number of waveforms tested). |
|---|---|

---
**[Page 308]**

Mask Testing 18
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 309
Reset Statistics Note that statistics are also reset when:
• Mask Test is switched on after being switched off.
• Clear Mask softkey is pressed.
• An Automask is created.
Additionally, the accumulated time counter is reset whenever the oscilloscope
is run after the acquisition was stopped.
Clear Display Clears acquisition data from the oscilloscope display.
To manually modify a mask file
You can manually modify a mask file that you created using the Automask
function.
1 Follow the steps 1-7 in “To create a mask from a "golden" waveform
(Automask)"on page303. Do not clear the mask after creating it.
2 Attach a USB mass storage device to the oscilloscope.
3 Press the [Save/Recall] key.
4 Press the Save softkey.
5 Press the Format softkey and select Mask.
6 Press the second softkey and select a destination folder on your USB mass
storage device.
7 Press the Press to Save softkey. This creates an ASCII text file that describes the
mask.
8 Remove the USB mass storage device and connect it to a PC.
9 Open the .msk file your created using a text editor (such as Wordpad).
10Edit, save, and close the file.
The mask file contains the following sections:
• Mask File Identifier.
• Mask Title.
• Mask Violation Regions.
• Oscilloscope Setup Information.
Mask File Identifier The Mask File Identifier is MASK_FILE_548XX.
| Reset Statistics | Note that statistics are also reset when:
• Mask Test is switched on after being switched off.
• Clear Mask softkey is pressed.
• An Automask is created.
Additionally, the accumulated time counter is reset whenever the oscilloscope
is run after the acquisition was stopped. |
|---|---|
| Clear Display | Clears acquisition data from the oscilloscope display. |

---
**[Page 309]**

18 Mask Testing
310 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Mask Title The Mask Title is a string of ASCII characters. Example: autoMask CH1 OCT 03
09:40:26 2008
When a mask file contains the keyword "autoMask" in the title, the edge of the
mask is passing by definition. Otherwise, the edge of the mask is defined as a
failure.
Mask Violation
Regions
Region 1
Region 2
Up to 8 regions can be defined for a mask. They can be numbered 1-8. They can
appear in any order in the .msk file. The numbering of the regions must go from
top to bottom, left to right.
An Automask file contains two special regions: the region "glued" to the top of the
display, and the region that is "glued" to the bottom. The top region is indicated by
y-values of "MAX" for the first and last points. The bottom region is indicated by
y-values of "MIN" for the first and last points.
The top region must be the lowest numbered region in the file. The bottom region
must be the highest numbered region in the file.
| Region 1
Region 2 |
|---|
|  |

---
**[Page 310]**

Mask Testing 18
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 311
Region number 1 is the top mask region. The vertices in Region 1 describe points
along a line; that line is the bottom edge of the top portion of the mask.
Similarly, the vertices in Region 2 describe the line that forms the top of the
bottom part of the mask.
The vertices in a mask file are normalized. There are four parameters that define
how values are normalized:
• X1
• Δ X
• Y1
• Y2
These four parameters are defined in the Oscilloscope Setup portion of the mask
file.
The Y-values (normally voltage) are normalized in the file using the following
equation:
Y = (Y - Y1)/Δ Y
norm
where Δ Y = Y2 - Y1
To convert the normalized Y-values in the mask file to voltage:
Y = (Y * Δ Y) + Y1
norm
where Δ Y = Y2 - Y1
The X-values (normally time) are normalized in the file using the following
equation:
X = (X - X1)/Δ X
norm
To convert the normalized X-values to time:
X = (X * Δ X) + X1
norm
Oscilloscope The keywords "setup" and "end_setup" (appearing alone on a line) define the
Setup Information beginning and end of the oscilloscope setup region of the mask file. The
oscilloscope setup information contains remote programming language
commands that the oscilloscope executes when the mask file is loaded.
Any legal remote programming command can be entered in this section.

---
**[Page 311]**

18 Mask Testing
312 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The mask scaling controls how the normalized vectors are interpreted. This in turn
controls how the mask is drawn on the display. The remote programming
commands that control mask scaling are:
:MTES:SCAL:BIND 0
:MTES:SCAL:X1 -400.000E-06
:MTES:SCAL:XDEL +800.000E-06
:MTES:SCAL:Y1 +359.000E-03
:MTES:SCAL:Y2 +2.35900E+00
Building a Mask File
The following display shows a mask that uses all eight regions.
This mask is created by recalling the following mask file:
MASK_FILE_548XX
"All Regions"
/* Region Number */ 1
/* Number of vertices */ 4
|  |
|---|
|  |

---
**[Page 312]**

Mask Testing 18
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 313
-12.50, MAX
-10.00, 1.750
10.00, 1.750
12.50, MAX
/* Region Number */ 2
/* Number of vertices */ 5
-10.00, 1.000
-12.50, 0.500
-15.00, 0.500
-15.00, 1.500
-12.50, 1.500
/* Region Number */ 3
/* Number of vertices */ 6
-05.00, 1.000
-02.50, 0.500
02.50, 0.500
05.00, 1.000
02.50, 1.500
-02.50, 1.500
/* Region Number */ 4
/* Number of vertices */ 5
10.00, 1.000
12.50, 0.500
15.00, 0.500
15.00, 1.500
12.50, 1.500
/* Region Number */ 5
/* Number of vertices */ 5
-10.00, -1.000
-12.50, -0.500
-15.00, -0.500
-15.00, -1.500
-12.50, -1.500
/* Region Number */ 6
/* Number of vertices */ 6
-05.00, -1.000
-02.50, -0.500
02.50, -0.500
05.00, -1.000
02.50, -1.500
-02.50, -1.500
/* Region Number */ 7
/* Number of vertices */ 5
10.00, -1.000
12.50, -0.500
15.00, -0.500
15.00, -1.500
12.50, -1.500
/* Region Number */ 8
/* Number of vertices */ 4
-12.50, MIN
-10.00, -1.750
10.00, -1.750
12.50, MIN

---
**[Page 313]**

18 Mask Testing
314 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
setup
:CHANnel1:RANGe +8.00E+00
:CHANnel1:OFFSet +2.0E+00
:CHANnel1:DISPlay 1
:TIMebase:MODE MAIN
:TIMebase:REFerence CENTer
:TIMebase:RANGe +50.00E-09
:TIMebase:POSition +10.0E-09
:MTESt:SOURce CHANnel1
:MTESt:ENABle 1
:MTESt:LOCK 1
:MTESt:SCALe:X1 +10.0E-09
:MTESt:SCALe:XDELta +1.0000E-09
:MTESt:SCALe:Y1 +2.0E+00
:MTESt:SCALe:Y2 +4.00000E+00
end_setup
In a mask file, all region definitions need to be separated by a blank line.
Mask regions are defined by a number of (x,y) coordinate vertices (as on an
ordinary x,y graph). A "y" value of "MAX" specifies the top of the graticule, and a
"y" value of "MIN" specifies the bottom of the graticule.
The mask x,y graph is related to the oscilloscope graticule using the
:MTESt:SCALe setup commands.
The oscilloscope's graticule has a time reference location (at the left, center, or
right of the screen) and a trigger (t=0) position/delay value relative to the
reference. The graticule also has a vertical ground 0V reference (offset relative to
the center of the screen) location.
The X1 and Y1 setup commands relate the mask region's x,y graph origin to the
oscilloscope graticule's t=0 and V=0 reference locations, and the XDELta and Y2
setup commands specify the size of the graph's x and y units.
• The X1 setup command specifies the time location of the x,y graph's x origin.
• The Y1 setup command specifies the vertical location of the x,y graph's y origin.
• The XDELta setup command specifies the amount of time associated with each
x unit.
• The Y2 setup command is the vertical location of the x,y graph's y=1 value (so
in effect, Y2 – Y1 is the YDELta value).
For example:
• With a graticule whose trigger position is 10ns (before a center screen
reference) and whose ground reference (offset) is 2V below the center of the
screen, to place the mask region's x,y graph's origin at center screen, you would
set X1 = 10ns and Y1 = 2V.

---
**[Page 314]**

Mask Testing 18
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 315
• If the XDELta parameter is set to 5ns and Y2 is set to 4V, a mask region whose
vertices are (-1, 1), (1, 1), (1, -1), and (-1, -1) goes from 5ns to 15ns and from
0V to 4V.
• If you move the mask region's x,y graph origin to the t=0 and V=0 location by
setting X1 = 0 and Y1 = 0, the same vertices define a region that goes from
-5ns to 5ns and from -2V to 2V.
Although a mask can have up to 8 regions, in any given vertical column, it is only possible to
NOTE
define 4 regions. When there are 4 regions in a vertical column, one region must be tied to the
top (using the MAX y value) and one must be tied to the bottom (using the MIN y value).
How is mask testing done?
InfiniiVision oscilloscopes start mask testing by creating a database that is 200 x
640 for the waveform viewing area. Each location in the array is designated as
either a violation or a pass area. Each time a data point from a waveform occurs in
a violation area a failure is logged. If Test All was selected, every active analog
channel is tested against the mask database for each acquisition. Over 2billion
failures can be logged per-channel. The number of acquisitions tested is also
logged and displayed as "# of Tests".
The mask file allows greater resolution than the 200 X 640 database. Some
quantization of data occurs to reduce the mask file data for display on-screen.
| NOTE |
|---|
|  |

---
**[Page 315]**

18 Mask Testing
316 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 316]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
317
19 Digital Voltmeter and
Counter
Digital Voltmeter / 318
Counter / 320
To enable the Digital Voltmeter (DVM) and Counter analysis features, order Option
DVMCTR at time of oscilloscope purchase, or order DSOXDVMCTR as a
stand-alone item after oscilloscope purchase.

---
**[Page 317]**

19 Digital Voltmeter and Counter
318 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Digital Voltmeter
The digital voltmeter (DVM) analysis feature provides 3-digit voltage
measurements on any analog channel. DVM measurements are asynchronous
from the oscilloscope's acquisition system and are always acquiring.
The DVM display is a seven-segment readout like you would see on a digital
voltmeter. It shows the selected mode as well as the units. Units are selected
using the Units softkey in the channel's Probe Menu.
The DVM display also has a scale that is determined by the channel's vertical scale
and reference level. The scale's blue triangle pointer shows the most recent
measurement. The white bar above that shows the measurement extrema over the
last 3 seconds.
|  |
|---|
|  |

---
**[Page 318]**

Digital Voltmeter and Counter 19
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 319
The DVM makes accurate RMS measurements when the signal frequency is
between 20Hz and 2kHz. When the signal frequency is outside this range, "<BW
Limit?" or ">BW Limit?" appears in the DVM display to caution you about
inaccurate RMS measurement results.
To use the digital voltmeter:
1 Press the [Analyze] key.
2 Press Features; then, select Digital Voltmeter.
3 Press Features again to enable the DVM measurements.
4 Press the Source softkey and turn the Entry knob to select the analog channel
on which digital voltmeter (DVM) measurements are made.
The selected channel does not have to be on (displaying a waveform) in order
for DVM measurements to be made.
5 Press the Mode softkey and turn the Entry knob to select the digital voltmeter
(DVM) mode:
• AC RMS — displays the root-mean-square value of the acquired data, with
the DC component removed.
• DC — displays the DC value of the acquired data.
• DC RMS — displays the root-mean-square value of the acquired data.
6 If the selected source channel is not used in oscilloscope triggering, press Auto
Range to disable or enable automatic adjustment of the DVM channel's vertical
scale, vertical (ground level) position, and trigger (threshold voltage) level (used
for the counter frequency measurement).
When enabled, Auto Range overrides attempted adjustments of the channel's
vertical scale and position knobs.
When disabled, you can use the channel's vertical scale and position knobs
normally.
7 Press the Limits softkey to open the DVM Beep Limit Menu where you can
specify voltage reading limits that will cause the oscilloscope to beep.
|  |  |
|---|---|

---
**[Page 319]**

19 Digital Voltmeter and Counter
320 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Press the Beep softkey to enable/disable beeps when the specified digital
voltmeter reading limits occur.
• Press the Beep When softkey to select whether the oscilloscope should beep
when Within Limits or Outside Limits.
• Press the Lower Limit and Upper Limit softkeys and use the Entry knob to
adjust the lower limit of the DVM reading range. You can press these
softkeys again for a keypad entry dialog that lets you enter an exact value.
Counter
The counter analysis feature provides frequency, period, or edge event (totalize)
counter measurements on any analog channel.
The counter counts trigger level crossings within a certain amount of time (gate
time) and displays the results on a seven-segment readout (like you would see on
a standalone counter instrument).
For frequency and period counter measurements:
• The gate time is specified indirectly by the selected number of digits of
resolution, from 3 to 10. For higher resolutions, the gate time is greater.
• Up to 3.2GHz (4GHz typical) frequencies can be measured, unless high-speed
USB decoding is active, in which case, up to 1GHz (1.2GHz typical)
frequencies can be measured.
For totalize measurements:
• A running count of edges is kept. You can choose whether to count positive or
negative edges, and when edge triggering on any analog channel, you can gate
the count with a positive or negative pulse on a second analog channel.
• Edge events with up to 1GHz (1.2GHz typical) frequencies can be counted.
• When gating the count, the gating signal setup time is 500ps typical and the
hold time is 500ps typical when using similar probes for the totalize source and
the gate source.
The counter is asynchronous from the oscilloscope's acquisition system and is
always acquiring.
|  |  |
|---|---|

---
**[Page 320]**

Digital Voltmeter and Counter 19
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 321
To use the counter:
1 Press the [Analyze] key.
2 Press Features; then, select Counter.
3 Press Features again to enable the counter.
4 Press the Source softkey and turn the Entry knob to select the analog channel or
Trigger Qualified Event signal to make counter measurements on.
With the Trigger Qualified Event source, you can see how often trigger events are
detected. This can be more often than when triggers actually occur, due to the
oscilloscope's acquisition time or update rate capabilities. The TRIG OUT signal
shows when triggers actually occur. Remember that the oscilloscope's trigger
circuitry does not re-arm until the holdoff time occurs and that the minimum
holdoff time is 40ns; therefore, the maximum trigger qualified event frequency
that can be counted is 25MHz.
The selected channel does not have to be on (displaying a waveform) in order
for counter measurements to be made.
5 Press Auto Setup Threshold softkey to have the oscilloscope automatically
determine and set the threshold voltage (trigger) level for the selected analog
channel source.
6 Press the Measure softkey and turn the Entry knob to select what the counter
measures:
• Frequency — the cycles per second (Hz, kHz, or MHz) of the signal.
• Period — the time periods of the signal's cycles.
• Totalize — the count of edge events on the signal.
Frequency and For frequency and period measurements, press the #ofDigits softkey to specify the
Period Counter resolution of the counter. You can choose from 3 to 10 digit resolutions.
Higher resolutions require longer gate times, which cause the measurement times
to be longer as well.
Totalize Counter For (edge event) totalize measurements, press the Clear Count softkey to zero the
edge event counter.
Press the Totalize softkey to open the Counter Totalize Menu where you can:
|  |  |
|---|---|

---
**[Page 321]**

19 Digital Voltmeter and Counter
322 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Press the Source softkey and turn the Entry knob to change the analog channel
on which counter measurements are made.
• Press the Event Slope softkey to choose whether positive or negative edge
events are counted.
• Press the Gate softkey to enable or disable gating of the edge event count using
a positive or negative level on a second analog channel.
When gating is enabled:
a Press the Gate Source softkey and turn the Entry knob to select the analog
channel that will supply the gating signal.
The selected channel does not have to be on (displaying a waveform).
b Press the polarity softkey to choose whether positive or negative levels are
used to gate the edge event count.
The trigger level for the selected analog channel is used to determine the
polarity of the signal.
|  |
|---|
|  |

---
**[Page 322]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
323
20 Waveform Generator
To select generated waveform types and settings / 323
To edit arbitrary waveforms / 327
To output the waveform generator sync pulse / 334
To specify the expected output load / 334
To use waveform generator logic presets / 335
To add noise to the waveform generator output / 335
To add modulation to the waveform generator output / 336
To restore waveform generator defaults / 341
To set up dual channel tracking / 341
A waveform generator is built into the oscilloscope. It is enabled by Option WGN
or the DSOX6WAVEGEN2 upgrade. The waveform generator gives you an easy
way to provide input signals when testing circuitry with the oscilloscope.
Waveform generator settings can be saved and recalled with oscilloscope setups.
See Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on page
343.
To select generated waveform types and settings
1 To access the Waveform Generator Menu and enable or disable the waveform
generator output on the front panel Gen Out BNC, press the [Wave Gen] key.
When waveform generator output is enabled, the [Wave Gen] key is illuminated.
When waveform generator output is disabled, the [Wave Gen] key is off.
The waveform generator output is always disabled when the instrument is first
turned on.

---
**[Page 323]**

20 Waveform Generator
324 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The waveform generator output is automatically disabled if excessive voltage is
applied to the Gen Out BNC.
2 In the Waveform Generator Menu, press the Waveform softkey and turn the
Entry knob to select the waveform type.
3 Depending on the selected waveform type, use the remaining softkeys and the
Entry knob to set the waveform's characteristics.
Waveform Characteristics Frequency Max. Offset2
Type Range Amplitude2 (High-Z)1
(High-Z)?1
Arbitrary Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±5.00V
Fine, Amplitude/High-Level, and Offset/Low-Level 12MHz 10Vpp
softkeys to set the arbitrary waveform signal
parameters.
Use the Edit Waveform softkey to define the
arbitrary waveform shape. See “To edit arbitrary
waveforms"on page327.
|  |  |
|---|---|
| Waveform
Type | Characteristics | Frequency
Range | Max.
Amplitude2
(High-Z)?1 | Offset2
(High-Z)1 |
|---|---|---|---|---|
| Arbitrary | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude/High-Level, and Offset/Low-Level
softkeys to set the arbitrary waveform signal
parameters.
Use the Edit Waveform softkey to define the
arbitrary waveform shape. See “To edit arbitrary
waveforms"on page327. | 100mHz to
12MHz | 20mVpp to
10Vpp | ±5.00V |

---
**[Page 324]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 325
Waveform Characteristics Frequency Max. Offset2
Type Range Amplitude2 (High-Z)1
(High-Z)?1
Sine Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±4.00V
Fine, Amplitude/High-Level, and Offset/Low-Level 20MHz 10Vpp
softkeys to set the sine signal parameters.
Square Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±5.00V
Fine, Amplitude/High-Level, Offset/Low-Level, and 10MHz 10Vpp
DutyCycle softkeys to set the square wave signal
parameters.
The duty cycle can be adjusted from 20% to 80%.
Ramp Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±5.00V
Fine, Amplitude/High-Level, Offset/Low-Level, and 200kHz 10Vpp
Symmetry softkeys to set the ramp signal
parameters.
Symmetry represents the amount of time per cycle
that the ramp waveform is rising and can be
adjusted from 0% to 100%.
Pulse Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±5.00V
Fine, Amplitude/High-Level, Offset/Low-Level, and 10MHz. 10Vpp
Width/Width Fine softkeys to set the pulse signal
parameters.
The pulse width can be adjusted from 20ns to the
period minus 20ns.
DC Use the Offset softkey to set the DC level. n/a n/a ±10.00V
Noise Use the Amplitude/High-Level and n/a 20mVpp to ±5.00V
Offset/Low-Level to set the noise signal parameters. 10Vpp
Sine Cardinal Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±2.50V
Fine, Amplitude, and Offset softkeys to set the sinc 1MHz 9Vpp
signal parameters.
Exponential Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±5.00V
Rise Fine, Amplitude/High-Level, and Offset/Low-Level 5MHz 10Vpp
softkeys to set the exponential rise signal
parameters.
Exponential Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±5.00V
Fall Fine, Amplitude/High-Level, and Offset/Low-Level 5MHz 10Vpp
softkeys to set the exponential fall signal
parameters.
| Waveform
Type | Characteristics | Frequency
Range | Max.
Amplitude2
(High-Z)?1 | Offset2
(High-Z)1 |
|---|---|---|---|---|
| Sine | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude/High-Level, and Offset/Low-Level
softkeys to set the sine signal parameters. | 100mHz to
20MHz | 20mVpp to
10Vpp | ±4.00V |
| Square | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude/High-Level, Offset/Low-Level, and
DutyCycle softkeys to set the square wave signal
parameters.
The duty cycle can be adjusted from 20% to 80%. | 100mHz to
10MHz | 20mVpp to
10Vpp | ±5.00V |
| Ramp | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude/High-Level, Offset/Low-Level, and
Symmetry softkeys to set the ramp signal
parameters.
Symmetry represents the amount of time per cycle
that the ramp waveform is rising and can be
adjusted from 0% to 100%. | 100mHz to
200kHz | 20mVpp to
10Vpp | ±5.00V |
| Pulse | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude/High-Level, Offset/Low-Level, and
Width/Width Fine softkeys to set the pulse signal
parameters.
The pulse width can be adjusted from 20ns to the
period minus 20ns. | 100mHz to
10MHz. | 20mVpp to
10Vpp | ±5.00V |
| DC | Use the Offset softkey to set the DC level. | n/a | n/a | ±10.00V |
| Noise | Use the Amplitude/High-Level and
Offset/Low-Level to set the noise signal parameters. | n/a | 20mVpp to
10Vpp | ±5.00V |
| Sine Cardinal | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude, and Offset softkeys to set the sinc
signal parameters. | 100mHz to
1MHz | 20mVpp to
9Vpp | ±2.50V |
| Exponential
Rise | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude/High-Level, and Offset/Low-Level
softkeys to set the exponential rise signal
parameters. | 100mHz to
5MHz | 20mVpp to
10Vpp | ±5.00V |
| Exponential
Fall | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude/High-Level, and Offset/Low-Level
softkeys to set the exponential fall signal
parameters. | 100mHz to
5MHz | 20mVpp to
10Vpp | ±5.00V |

---
**[Page 325]**

20 Waveform Generator
326 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Waveform Characteristics Frequency Max. Offset2
Type Range Amplitude2 (High-Z)1
(High-Z)?1
Cardiac Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±2.50V
Fine, Amplitude, and Offset softkeys to set the 200kHz 9Vpp
cardiac signal parameters.
Gaussian Pulse Use the Frequency/Frequency Fine/Period/Period 100mHz to 20mVpp to ±2.50V
Fine, Amplitude, and Offset softkeys to set the 5MHz 7.5Vpp
Gaussian pulse signal parameters.
1When the output load is 50 Ω , these values are halved.
2The minimum amplitude is limited to 40mVpp if the offset is greater than 500mV or less than -500mV. Likewise, the offset is
limited to +/-500mV if the amplitude is less than 40mVpp.
Pressing a signal parameter softkey can open a menu for selecting the type of
adjustment. For example, you can choose to enter amplitude and offset values,
or you can choose to enter high-level and low-level values. Or, you can choose
to enter frequency values or period values. Keep pressing the softkey to select
the type of adjustment. Turn the Entry knob to adjust the value.
Also note that you can set up the other waveform generator output to track
frequency, amplitude, offset, and duty cycle adjustments. See “To set up dual
channel tracking"on page341.
The Settings softkey opens the Waveform Generator Settings Menu which lets you
make other settings related to the waveform generator.
See:
• “To output the waveform generator sync pulse"on page334
• “To specify the expected output load"on page334
• “To use waveform generator logic presets"on page335
• “To set up dual channel tracking"on page341
• “To add modulation to the waveform generator output"on page336
• “To add noise to the waveform generator output"on page335
| Waveform
Type | Characteristics | Frequency
Range | Max.
Amplitude2
(High-Z)?1 | Offset2
(High-Z)1 |
|---|---|---|---|---|
| Cardiac | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude, and Offset softkeys to set the
cardiac signal parameters. | 100mHz to
200kHz | 20mVpp to
9Vpp | ±2.50V |
| Gaussian Pulse | Use the Frequency/Frequency Fine/Period/Period
Fine, Amplitude, and Offset softkeys to set the
Gaussian pulse signal parameters. | 100mHz to
5MHz | 20mVpp to
7.5Vpp | ±2.50V |
| 1When the output load is 50 Ω , these values are halved.
2The minimum amplitude is limited to 40mVpp if the offset is greater than 500mV or less than -500mV. Likewise, the offset is
limited to +/-500mV if the amplitude is less than 40mVpp. |  |  |  |  |
|  |
|---|
|  |

---
**[Page 326]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 327
• “To restore waveform generator defaults"on page341
To edit arbitrary waveforms
1 When Arbitrary is selected as the generated waveform type (see “To select
generated waveform types and settings"on page323), press the EditWaveform
softkey to open the Edit Waveform Menu.
When you open the Edit Waveform Menu, you see the existing arbitrary
waveform definition. The voltage and time period you see in the diagram are
the bounding parameters — they come from the frequency and amplitude
settings in the main Waveform Generator Menu.
2 Use the softkeys in the Edit Waveform Menu to define the shape of the arbitrary
waveform:
|  |  |
|---|---|

---
**[Page 327]**

20 Waveform Generator
328 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Softkey Description
Create New Opens the New Waveform Menu. See “Creating New Arbitrary Waveforms"on page328.
Edit Existing Opens the Edit Waveform Points Menu. See “Editing Existing Arbitrary Waveforms"on
page329.
Interpolate Specifies how lines are drawn between arbitrary waveform points.
When enabled, lines are drawn between points in the waveform editor. Voltage levels change
linearly between one point and the next.
When disabled, all line segments in the waveform editor are horizontal. The voltage level of
one point remains until the next point.
Source Selects the analog channel or reference waveform to be captured and stored to the arbitrary
waveform. See “Capturing Other Waveforms to the Arbitrary Waveform"on
page333.
Store Source to Arb Captures the selected waveform source and copy it to the arbitrary waveform. See
“Capturing Other Waveforms to the Arbitrary Waveform"on page333.
You can use the [Save/Recall] key and menu to save arbitrary waveforms to one of four
NOTE
internal storage locations or to a USB storage device, and you can recall them later. See “To
save arbitrary waveforms"on page351 and “To recall arbitrary waveforms"on
page355.
Creating New Arbitrary Waveforms
The New Waveform Menu is opened by pressing Create New in the Edit Waveform
Menu.
To create a new arbitrary waveform:
1 In the New Waveform Menu, press Initial Pts; then, use the Entry knob to select
the initial number of points in the new waveform.
The new waveform will be a square wave with the number of points you specify.
The points are evenly spaced over the time period.
| Softkey | Description |
|---|---|
| Create New | Opens the New Waveform Menu. See “Creating New Arbitrary Waveforms"on page328. |
| Edit Existing | Opens the Edit Waveform Points Menu. See “Editing Existing Arbitrary Waveforms"on
page329. |
| Interpolate | Specifies how lines are drawn between arbitrary waveform points.
When enabled, lines are drawn between points in the waveform editor. Voltage levels change
linearly between one point and the next.
When disabled, all line segments in the waveform editor are horizontal. The voltage level of
one point remains until the next point. |
| Source | Selects the analog channel or reference waveform to be captured and stored to the arbitrary
waveform. See “Capturing Other Waveforms to the Arbitrary Waveform"on
page333. |
| Store Source to Arb | Captures the selected waveform source and copy it to the arbitrary waveform. See
“Capturing Other Waveforms to the Arbitrary Waveform"on page333. |
| NOTE |
|---|
|  |
|  |
|---|
|  |

---
**[Page 328]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 329
2 Use the Frequency/Frequency Fine/Period/Period Fine softkey to set the time period
bounding parameter (repetition frequency) of the arbitrary waveform.
3 Use the Amplitude/High-Level and Offset/Low-Level softkeys to set the voltage
bounding parameter of the arbitrary waveform.
4 When you are ready to create the new arbitrary waveform, press Apply & Edit.
When you create a new arbitrary waveform, the existing arbitrary waveform definition is
CAUTION
overwritten. Note that you can use the [Save/Recall] key and menu to save arbitrary
waveforms to one of four internal storage locations or to a USB storage device, and you
can recall them later. See “To save arbitrary waveforms"on page351 and “To
recall arbitrary waveforms"on page355.
The new waveform is created and the Edit Waveform Points menu is opened.
See “Editing Existing Arbitrary Waveforms"on page329.
Note that you can also create a new arbitrary waveform by capturing another
waveform. See “Capturing Other Waveforms to the Arbitrary Waveform"on
page333.
Editing Existing Arbitrary Waveforms
Using the To select a point, touch or drag in the upper, full waveform display:
Touchscreen to
Edit Existing
Waveforms
For fine points selection, touch the previous point or next point arrows:
| CAUTION |
|---|
|  |
|  |
|---|
|  |

---
**[Page 329]**

20 Waveform Generator
330 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To adjust the value of a point, drag the voltage level handle up or down:
To select a points region, drag across the upper or lower waveform display:
For fine adjustment of the region selection (or to clear the selection), use the
Selected Region controls:
|  |
|---|
|  |
|  |
|---|
|  |
|  |
|---|
|  |

---
**[Page 330]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 331
To perform points operations, touch the Operation controls drop-down, select the
operation, and use the controls for the selected operation:
• Cut/Copy selected points regions to the clipboard and Paste points from the
clipboard.
When pasting points from the clipboard, you can paste at the beginning, end,
cursor location (currently selected point), or you can replace the currently
selected points region.
• Insert New points.
You can specify the number of new points and their voltage.
• Replace a selected points region with new points.
• Delete a selected points region.
To navigate the arbitrary waveform (and select points), drag the point selection
handle left or right across the display area:
|  |
|---|
|  |
|  |
|---|
|  |

---
**[Page 331]**

20 Waveform Generator
332 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Using Softkeys to The Edit Waveform Points Menu is opened by pressing Edit Existing in the Edit
Edit Existing Waveform Menu or by pressing Apply&Edit when creating a new arbitrary
Waveforms waveform.
To specify the voltage values of points:
1 Press Point#; then, use the Entry knob to select the point whose voltage value
you wish to set.
|  |
|---|
|  |
|  |
|---|
|  |

---
**[Page 332]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 333
2 Press Voltage; then, use the Entry knob to set the point's voltage value.
To insert a point:
1 Press Point#; then, use the Entry knob to select the point after which the new
point will be inserted.
2 Press Insert Point.
All points are adjusted to maintain uniform time spacing between points.
To remove a point:
1 Press Point#; then, use the Entry knob to select the point you want to remove.
2 Press Remove Point.
All points are adjusted to maintain uniform time spacing between points.
Capturing Other Waveforms to the Arbitrary Waveform
The Edit Waveform Menu is opened by pressing EditWaveform in the main
Waveform Generator Menu.
To capture another waveform to the arbitrary waveform:
1 Press Source; then, use the Entry knob to select the analog channel, math, or
reference location whose waveform you wish to capture.
2 Press Store Source to Arb.
When you create a new arbitrary waveform, the existing arbitrary waveform definition is
CAUTION
overwritten. Note that you can use the [Save/Recall] key and menu to save arbitrary
waveforms to one of four internal storage locations or to a USB storage device, and you
can recall them later. See “To save arbitrary waveforms"on page351 and “To
recall arbitrary waveforms"on page355.
The source waveform is decimated into 8192 (maximum) or fewer arbitrary
waveform points.
|  |
|---|
|  |
| CAUTION |
|---|
|  |

---
**[Page 333]**

20 Waveform Generator
334 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If the source waveform frequency and/or voltage exceed the capabilities of the waveform
NOTE
generator, the arbitrary waveform will be limited to the capabilities of the waveform
generator. For example, a 20MHz waveform captured as the arbitrary waveform, becomes a
12MHz waveform.
To output the waveform generator sync pulse
1 If the Waveform Generator Menu is not currently displayed on the
oscilloscope's softkeys, press the [Wave Gen] key.
2 In the Waveform Generator Menu, press the Settings softkey.
3 In the Waveform Generator Settings Menu, press the Trig Out softkey and turn
the Entry knob to select Waveform Generator Sync Pulse.
Waveform Type Sync Signal Characteristics
All waveforms except The Sync signal is a TTL positive pulse that occurs when the waveform
DC, Noise, and rises above zero volts (or the DC offset value).
Cardiac
DC, Noise, and N/A
Cardiac
To specify the expected output load
1 If the Waveform Generator Menu is not currently displayed on the
oscilloscope's softkeys, press the [Wave Gen] key.
2 In the Waveform Generator Menu, press the Settings softkey.
3 In the Waveform Generator Settings Menu, press the Out Load softkey and turn
the Entry knob to select:
• 50Ω
• High-Z
The output impedance of the Gen Out BNC is fixed at 50 ohms. However, the
output load selection lets the waveform generator display the correct amplitude
and offset levels for the expected output load.
| NOTE |
|---|
|  |
| Waveform Type | Sync Signal Characteristics |
|---|---|
| All waveforms except
DC, Noise, and
Cardiac | The Sync signal is a TTL positive pulse that occurs when the waveform
rises above zero volts (or the DC offset value). |
| DC, Noise, and
Cardiac | N/A |

---
**[Page 334]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 335
If the actual load impedance is different than the selected value, the displayed
amplitude and offset levels will be incorrect.
To use waveform generator logic presets
With logic level presets, you can easily set the output voltage to TTL, CMOS
(5.0V), CMOS (3.3V), CMOS (2.5V), or ECL compatible Low and High levels.
1 If the Waveform Generator Menu is not currently displayed on the
oscilloscope's softkeys, press the [Wave Gen] key.
2 In the Waveform Generator Menu, press the Settings softkey.
3 In the Waveform Generator Settings Menu, press the Logic Presets softkey.
4 In the Waveform Generator Logic Level Presets Menu, press one of the softkeys
to set the generated signal's Low and High voltages to logic compatible levels:
Softkey (logic levels) Low level High level
TTL 0V +5V (or a TTL-compatible
high level if +5V cannot
be reached)
CMOS (5.0V) 0V +5V
CMOS (3.3V) 0V +3.3V
CMOS (2.5V) 0V +2.5V
ECL -1.7V -0.9V
To add noise to the waveform generator output
1 If the Waveform Generator Menu is not currently displayed on the
oscilloscope's softkeys, press the [Wave Gen] key.
2 In the Waveform Generator Menu, press the Settings softkey.
3 In the Waveform Generator Settings Menu, press the Add Noise softkey and turn
the Entry knob to select the amount of white noise to add to the waveform
generator output.
| Softkey (logic levels) | Low level | High level |
|---|---|---|
| TTL | 0V | +5V (or a TTL-compatible
high level if +5V cannot
be reached) |
| CMOS (5.0V) | 0V | +5V |
| CMOS (3.3V) | 0V | +3.3V |
| CMOS (2.5V) | 0V | +2.5V |
| ECL | -1.7V | -0.9V |

---
**[Page 335]**

20 Waveform Generator
336 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Note that adding noise affects edge triggering on the waveform generator source
(see “Edge Trigger"on page174) as well as the waveform generator sync pulse
output signal (which can be sent to TRIG OUT, see “Setting the Rear Panel TRIG
OUT Source"on page374). This is because the trigger comparator is located after
the noise source.
To add modulation to the waveform generator output
Modulation is where an original carrier signal is modified according to the
amplitude of a second modulating signal. The modulation type (AM, FM, or FSK)
specifies how the carrier signal is modified.
Modulated waveforms are available on the WaveGen1 output.
To enable and set up modulation for the waveform generator output:
1 If the Waveform Generator Menu is not currently displayed on the
oscilloscope's softkeys, press the [Wave Gen] key.
2 In the Waveform Generator Menu, press the Settings softkey.
3 In the Waveform Generator Settings Menu, press the Modulation softkey.
4 In the Waveform Generator Modulation Menu:
• Press the Modulation softkey to enable or disable modulated waveform
generator output.
You can enable modulation for all waveform generator function types except
arbitrary, square, pulse, DC, noise, and Gaussian pulse.
Modulation is not available when waveform generator dual channel tracking
is being used.
• Press the Type softkey and turn the Entry knob to select the modulation type:
• Amplitude Modulation (AM) — the amplitude of the original carrier signal is
modified according to the amplitude of the modulating signal. See “To
set up Amplitude Modulation (AM)"on page337.
|  |  |
|---|---|

---
**[Page 336]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 337
• Frequency Modulation (FM) — the frequency of the original carrier signal is
modified according to the amplitude of the modulating signal. See “To
set up Frequency Modulation (FM)"on page338.
• Frequency-Shift Keying Modulation (FSK) — the output frequency "shifts"
between the original carrier frequency and a "hop frequency" at the
specified FSK rate. The FSK rate specifies a digital square wave
modulating signal. See “To set up Frequency-Shift Keying Modulation
(FSK)"on page340.
To set up Amplitude Modulation (AM)
In the Waveform Generator Modulation Menu (under [Wave Gen] > Settings >
Modulation):
1 Press the Type softkey and turn the Entry knob to select Amplitude Modulation
(AM).
2 Press the Waveform softkey and turn the Entry knob to select the shape of the
modulating signal:
• Sine
• Square
• Ramp
When the Ramp shape is selected, a Symmetry softkey appears so that you can
specify the amount of time per cycle that the ramp waveform is rising.
3 Press the AM Freq softkey and turn the Entry knob to specify the frequency of
the modulating signal.
4 Press the AM Depth softkey and turn the Entry knob to specify the amount of
amplitude modulation.
AM Depth refers to the portion of the amplitude range that will be used by the
modulation. For example, a depth setting of 80% causes the output amplitude
to vary from 10% to 90% (90% – 10% = 80%) of the original amplitude as the
modulating signal goes from its minimum to maximum amplitude.
The following screen shows an AM modulation of a 100kHz sine wave carrier
signal.

---
**[Page 337]**

20 Waveform Generator
338 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To set up Frequency Modulation (FM)
In the Waveform Generator Modulation Menu (under [Wave Gen] > Settings >
Modulation):
1 Press the Type softkey and turn the Entry knob to select Frequency Modulation
(FM).
2 Press the Waveform softkey and turn the Entry knob to select the shape of the
modulating signal:
• Sine
• Square
• Ramp
When the Ramp shape is selected, a Symmetry softkey appears so that you can
specify the amount of time per cycle that the ramp waveform is rising.
3 Press the FM Freq softkey and turn the Entry knob to specify the frequency of the
modulating signal.
|  |
|---|
|  |

---
**[Page 338]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 339
4 Press the FM Dev softkey and turn the Entry knob to specify the frequency
deviation from the original carrier signal frequency.
When the modulating signal is at its maximum amplitude, the output frequency
is the carrier signal frequency plus the deviation amount, and when the
modulating signal is at its minimum amplitude, the output frequency is the
carrier signal frequency minus the deviation amount.
The frequency deviation cannot be greater than the original carrier signal
frequency.
Also, the sum of the original carrier signal frequency and the frequency
deviation must be less than or equal to the maximum frequency for the selected
waveform generator function plus 100kHz.
The following screen shows an FM modulation of a 100kHz sine wave carrier
signal.
|  |
|---|
|  |

---
**[Page 339]**

20 Waveform Generator
340 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To set up Frequency-Shift Keying Modulation (FSK)
In the Waveform Generator Modulation Menu (under [Wave Gen] > Settings >
Modulation):
1 Press the Type softkey and turn the Entry knob to select Frequency-Shift Keying
Modulation (FSK).
2 Press the Hop Freq softkey and turn the Entry knob to specify the "hop
frequency".
The output frequency "shifts" between the original carrier frequency and this
"hop frequency".
3 Press the FSK Rate softkey and turn the Entry knob to specify the rate at which
the output frequency "shifts".
The FSK rate specifies a digital square wave modulating signal.
The following screen shows an FSK modulation of a 100kHz sine wave carrier
signal.
|  |
|---|
|  |

---
**[Page 340]**

Waveform Generator 20
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 341
To restore waveform generator defaults
1 If the Waveform Generator Menu is not currently displayed on the
oscilloscope's softkeys, press the [Wave Gen] key.
2 In the Waveform Generator Menu, press the Settings softkey.
3 In the Waveform Generator Settings Menu, press the Default Wave Gen softkey.
The waveform generator factory default settings (1kHz sine wave, 500mVpp,
0V offset, High-Z output load) are restored.
To set up dual channel tracking
You can set up one waveform generator output to track adjustments in the other
waveform generator output.
To set up dual channel tracking:
1 Press the [WaveGen1] or [WaveGen2] key for the waveform generator output
that you want to be tracked.
2 In the Waveform Generator Menu, press Settings.
3 In the Waveform Generator Settings Menu, press DualChan.
4 In the Waveform Generator: Dual-Channel Menu, you have these options:
• Tracking — frequency, amplitude, offset, and duty cycle adjustments to this
waveform generator output signal are tracked by the other waveform
generator output.
• Freq Tracking — frequency adjustments to this waveform generator output
signal are tracked by the other waveform generator output.
• Amp Tracking — amplitude and offset adjustments to this waveform generator
output signal are tracked by the other waveform generator output.
• Phase (°) — lets you adjust the phase of a frequency-tracked waveform
generator output.
Not all waveform shapes that can be frequency tracked can have their phase
adjusted.
• Copy Waveform to WaveGen2/1 — sets the other waveform generator output to
be identical to this waveform generator output (except that the shape of
either output may be inverted).

---
**[Page 341]**

20 Waveform Generator
342 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Not all waveform shapes can be frequency tracked. When Tracking or Freq Tracking
is enabled, the other generator's waveform selections will be limited dependent
upon this generator's waveform.
Also, when tracking is enabled, adjustments for tracked settings in the other
waveform generator become unavailable (ghosted).

---
**[Page 342]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
343
21 Save/Email/Recall
(Setups, Screens, Data)
Saving Setups, Screen Images, or Data / 343
Emailing Setups, Screen Images, or Data / 352
Recalling Setups, Masks, or Data / 353
Recalling Default Setups / 355
Performing a Secure Erase / 356
Oscilloscope setups, reference waveforms, and mask files can be saved to internal
oscilloscope memory or to a USB storage device and recalled later. You can also
recall default or factory default setups.
Oscilloscope screen images can be saved to a USB storage device in BMP or PNG
formats.
Acquired waveform data can be saved to a USB storage device in
comma-separated value (CSV), ASCII XY, and binary (BIN) formats.
Any file that can be saved to a USB storage device can also be e-mailed over the
network.
There is also a command to securely erase all the oscilloscope's non-volatile
internal memory.
Saving Setups, Screen Images, or Data
1 Press the [Save/Recall] key.
2 In the Save/Recall Menu, press Save.

---
**[Page 343]**

21 Save/Email/Recall (Setups, Screens, Data)
344 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 In the Save Trace and Setup Menu, press Format; then, turn the Entry knob to
select the type of file you want to save:
• Setup (*.scp) — The oscilloscope's horizontal timebase, vertical sensitivity,
trigger mode, trigger level, measurements, cursors, and math function
settings that tell the oscilloscope how to make a particular measurement.
See “To save setup files"on page345.
• 8-bit Bitmap image (*.bmp) — The complete screen image in a reduced color
(8-bit) bitmap format. See “To save BMP or PNG image files"on page346.
• 24-bit Bitmap image (*.bmp) — The complete screen image in a 24-bit color
bitmap format. See “To save BMP or PNG image files"on page346.
• 24-bit image (*.png) — The complete screen image in a 24-bit color PNG
format that uses lossless compression. Files are much smaller than the BMP
format. See “To save BMP or PNG image files"on page346.
• CSV data (*.csv) — This creates a file of comma-separated values of all
displayed channels and math waveforms. This format is suitable for
spreadsheet analysis. See “To save CSV, ASCII XY, or BIN data files"on
page346.
• ASCII XY data (*.csv) — This creates separate files of comma-separated values
for each displayed channel. This format is also suitable for spreadsheets. See
“To save CSV, ASCII XY, or BIN data files"on page346.
• Binary data (*.bin) — This creates a binary file, with a header, and data in the
form of time and voltage pairs. This file is much smaller than the ASCII XY
data file. See “To save CSV, ASCII XY, or BIN data files"on page346.
• Lister data (*.csv) — This is a CSV format file containing serial decode row
information with commas separating the columns. See “To save Lister data
files"on page349.
• Reference Waveform data (*.h5) — Saves waveform data in a format that can be
recalled to one of the oscilloscope's reference waveform locations. See “To
save reference waveform files to a USB storage device"on page350.
• Multi Channel Waveform data (*.h5) — Saves multiple channels of waveform
data in a format that can be opened by the N8900A Infiniium Offline
oscilloscope analysis software. You can recall the first Analog or Math
channel from a multi channel waveform data file.

---
**[Page 344]**

Save/Email/Recall (Setups, Screens, Data) 21
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 345
• Mask (*.msk) — This creates a mask file in a Keysight proprietary format that
can be read by Keysight InfiniiVision oscilloscopes. A mask data file includes
some oscilloscope setup information, but not all setup information. To save
all setup information including the mask data file, choose "Setup (*.scp)"
format instead. See “To save masks"on page350.
• Arbitrary Waveform data (*.csv) — This creates a file of comma-separated
values for the arbitrary waveform points' time and voltage values. See “To
save arbitrary waveforms"on page351.
• Power Harmonics data (*.csv) — When the DSOX6PWR power analysis
application is licensed, this creates a file of comma-separated values for the
current harmonics power analysis results. See the DSOX6PWR Power
Measurement Application User's Guide for more information.
• USB Signal Quality (*.html & *.bmp) — When the DSOX6USBSQ USB 2.0 signal
quality analysis application is licensed, this saves test results information
which includes waveform plot and eye diagram pictures. See the USBSQ
USB 2.0 Signal Quality Analysis Application Electrical Testing Notes manual
for more information.
• Analysis Results (*.csv) — A file of comma-separated values is saved for the
analysis types selected using the Analysis Select softkey.
You can also configure the [Quick Action] key to save setups, screen images, or
data. See “Configuring the [Quick Action] Key"on page381.
To save setup files
Setup files can be saved to one of 10 internal (\User Files) locations or to an
external USB storage device.
1 Press [Save/Recall] > Save > Format; then, turn the Entry knob to select Setup
(*.scp).
2 Press the softkey in the second position and use the Entry knob to navigate to
the save location. See “To navigate storage locations"on page351.
3 Finally, press the Press to Save softkey.
A message indicating whether the save was successful is displayed.
Setup files have the extension SCP. These extensions appear when using the File
Explorer (see “File Explorer"on page366), but they do not appear when using the
Recall Menu.

---
**[Page 345]**

21 Save/Email/Recall (Setups, Screens, Data)
346 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To save BMP or PNG image files
Image files can be saved to an external USB storage device.
1 Press [Save/Recall] > Save > Format; then, turn the Entry knob to select 8-bit
Bitmap image (*.bmp), 24-bit Bitmap image (*.bmp), or 24-bit image (*.png).
2 Press the softkey in the second position and use the Entry knob to navigate to
the save location. See “To navigate storage locations"on page351.
3 Press the Settings softkey.
In the File Settings Menu, you have these softkeys and options:
• Setup Info — setup information (vertical, horizontal, trigger, acquisition, math,
and display settings) is also saved in a separate file with a TXT extension.
• Invert Grat — the graticule in the image file has a white background instead of
the black background that appears on-screen.
• Palette — lets you choose between Color or Grayscale images.
4 Finally, press the Press to Save softkey.
A message indicating whether the save was successful is displayed.
When saving screen images, the oscilloscope uses the last menu visited before pressing the
NOTE
[Save/Recall] key. This lets you save any relevant information within the softkey menu area.
To save a screen image showing the Save/Recall Menu at the bottom, press the [Save/Recall]
key twice before saving the image.
You can also save the oscilloscope's display image using a web browser. See “Get
NOTE
Image"on page393 for details.
See Also • “To add an annotation"on page160
To save CSV, ASCII XY, or BIN data files
Data files can be saved to an external USB storage device.
1 Press [Save/Recall] > Save > Format; then, turn the Entry knob to select CSV data
(*.csv), ASCII XY data (*.csv), or Binary data (*.bin).
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |

---
**[Page 346]**

Save/Email/Recall (Setups, Screens, Data) 21
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 347
2 Press the softkey in the second position and use the Entry knob to navigate to
the save location. See “To navigate storage locations"on page351.
3 Press the Settings softkey.
In the File Settings Menu, you have these softkeys and options:
• Setup Info — when enabled, setup information (vertical, horizontal, trigger,
acquisition, math, and display settings) is also saved in a separate file with a
TXT extension.
• Length — sets the number of data points that will be output to the file. For
more information, see “Length Control"on page348.
• Save Seg — when data is acquired to segmented memory, you can specify
whether the currently displayed segment is saved or all acquired segments
are saved. (See also “Saving Data from Segmented Memory"on page234.)
4 Finally, press the Press to Save softkey.
A message indicating whether the save was successful is displayed.
CSV Data When the CSV data (*.csv) file format is selected, comma-separated values for
each displayed waveform and digital channel pod are saved as multiple columns
in a single file. Math FFT waveforms, whose values are in the frequency domain,
are appended at the bottom of the .csv file. Pod names (for example, D0-D7) or
waveform labels are used as column headers. This format is suitable for
spreadsheet analysis.
For CSV data, length "N" value-at-time measurements are performed across the
entire screen (using the measurement record data) for each active source.
Interpolation between measurement record data points is performed as needed.
ASCII XY Data When the ASCII XY data (*.csv) file format is selected, comma-separated value
files for each displayed waveform, digital channel pod, digital bus, and serial bus
are saved. For digital pods, an underscore (_) and the pod name (for example,
D0-D7) are appended to the specified file name; otherwise, an underscore and the
waveform's label are appended.
If the oscilloscope acquisition is stopped, data from the raw acquisition record
(which has more points than the measurement record) can be written. Press the
[Single] key to obtain maximum memory depth with current settings. If enabled,
serial decode data is saved.

---
**[Page 347]**

21 Save/Email/Recall (Setups, Screens, Data)
348 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
When you want to save less than the maximum number of data points, a 1-of-N
decimation is performed to produce an output whose length is less than or equal
to the requested length. For example, if there are 100k points of data, and you
specify a length of 2k, 1 of every 50 data points is saved.
See Also • “Binary Data (.bin) Format"on page409
• “CSV and ASCII XY files"on page416
• “Minimum and Maximum Values in CSV Files"on page417
Length Control
The Length control is available when saving data to CSV, ASCII XY, or BIN format
files. It sets the number of data points that will be output to the file. Only displayed
data points are saved.
When Max Length is enabled, the maximum number of waveform data points is
saved.
The maximum number of data points depends on these things:
• Whether acquisitions are running. When stopped, data comes from the raw
acquisition record. When running, data comes from the smaller measurement
record or the precision analysis record if enabled (see “Precision Measurements
and Math"on page275).
• Whether the oscilloscope was stopped using [Stop] or [Single]. Running
acquisitions split memory to provide fast waveform update rates. Single
acquisitions use full memory.
• Whether only one channel of a pair is turned on. (Channels 1 and 2 are one pair,
channels 3 and 4 are the other.) Acquisition memory is divided among the
channels in a pair.
• Whether reference waveforms are on. Displayed reference waveforms consume
acquisition memory.
• Whether digital channels are on. Displayed digital channels consume
acquisition memory.
• Whether segmented memory is on. Acquisition memory is divided by the
number of segments.
• The horizontal time/div (sweep speed) setting. At faster settings, fewer data
points appear on the display.

---
**[Page 348]**

Save/Email/Recall (Setups, Screens, Data) 21
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 349
Also, when the sample rate is above 2GSa/s (or 1GSa/s when two channels of
a pair are on), the maximum record length is 1M points. Acquisition memory is
still divided among the channels in a pair, but there is no difference between
using [Stop] or [Single].
• When saving to a CSV format file, the maximum number of data points is 64K.
When necessary, the Length control performs a "1 of n" decimation of the data .
For example: if the Length is set to 1000, and you are displaying a record that is
5000 data points in length, four of each five data points will be decimated,
creating an output file 1000 data points in length.
When saving waveform data, the save times depend on the chosen format:
Data File Format Save Times
BIN fastest
ASCII XY medium
CSV slowest
See Also • “Binary Data (.bin) Format"on page409
• “CSV and ASCII XY files"on page416
• “Minimum and Maximum Values in CSV Files"on page417
To save Lister data files
Lister data files can be saved to an external USB storage device.
1 Press [Save/Recall] > Save > Format; then, turn the Entry knob to select Lister data
file.
2 Press the softkey in the second position and use the Entry knob to navigate to
the save location. See “To navigate storage locations"on page351.
3 Press the Settings softkey.
In the File Settings Menu, you have these softkeys and options:
• Setup Info — when enabled, setup information (vertical, horizontal, trigger,
acquisition, math, and display settings) is also saved in a separate file with a
TXT extension.
4 Finally, press the Press to Save softkey.
| Data File Format | Save Times |
|---|---|
| BIN | fastest |
| ASCII XY | medium |
| CSV | slowest |

---
**[Page 349]**

21 Save/Email/Recall (Setups, Screens, Data)
350 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
A message indicating whether the save was successful is displayed.
To save reference waveform files to a USB storage device
1 Press the [Save/Recall] key.
2 In the Save/Recall Menu, press the Save softkey.
3 In the Save Menu, press the Format softkey and turn the Entry knob to select
Reference Waveform data (*.h5) .
4 Press the Source softkey and turn the Entry knob to select the source waveform.
5 Press the softkey in the second position and use the Entry knob to navigate to
the save location. See “To navigate storage locations"on page351.
6 Finally, press the Press to Save softkey.
A message indicating whether the save was successful is displayed.
To save masks
Mask files can be saved to one of four internal (\User Files) locations or to an
external USB storage device.
1 Press [Save/Recall] > Save > Format; then, turn the Entry knob to select Mask
(*.msk).
2 Press the softkey in the second position and use the Entry knob to navigate to
the save location. See “To navigate storage locations"on page351.
3 Finally, press the Press to Save softkey.
A message indicating whether the save was successful is displayed.
Mask files have the extension MSK.
Masks are also saved as part of setup files. See “To save setup files"on page345.
NOTE
See Also • Chapter18, “Mask Testing,” starting on page 303
| NOTE |
|---|
|  |

---
**[Page 350]**

Save/Email/Recall (Setups, Screens, Data) 21
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 351
To save arbitrary waveforms
Arbitrary waveform files can be saved to one of four internal (\User Files) locations
or to an external USB storage device.
1 Press [Save/Recall] > Save > Format; then, turn the Entry knob to select Arbitrary
Waveform data (*.csv).
2 Press the softkey in the second position and use the Entry knob to navigate to
the save location. See “To navigate storage locations"on page351.
3 Finally, press the Press to Save softkey.
A message indicating whether the save was successful is displayed.
See Also • “To edit arbitrary waveforms"on page327
To navigate storage locations
When saving or recalling files, the softkey in the second position of the Save Menu
or Recall Menu, along with the Entry knob, are used to navigate to storage
locations. The storage locations can be internal oscilloscope storage locations (for
setup files or mask files) or they can be external storage locations on a connected
USB storage device.
The softkey in the second position can have these labels:
• Press to go — when you can push the Entry knob to navigate to a new folder or
storage location.
• Location — when you have navigated to the current folder location (and are not
saving files).
• Save to — when you can save to the selected location.
• Load from — when you can recall from the selected file.
When saving files:
• The proposed file name is shown in the Save to file = line above the softkeys.
• To overwrite an existing file, browse to that file and select it. To create a new file
name, see “To enter file names"on page351.
To enter file names
To create new file names when saving files to a USB storage device:
1 In the Save Menu, press the File Name softkey.

---
**[Page 351]**

21 Save/Email/Recall (Setups, Screens, Data)
352 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You must have a USB storage device connected to the oscilloscope for this
softkey to be active.
2 In the File Name Menu, press the File Name softkey.
3 In the File Name keypad dialog, you can enter file names using:
• The touch screen (when the front panel [Touch] key is lit).
• The Entry knob. Turn the knob to select a key in the dialog; then, push
the Entry knob to enter it.
• A connected USB keyboard.
• A connected USB mouse — you can click anything on the screen that can be
touched.
4 When you are done entering the file name, select the dialog's Enter or OK key
or press the File Name softkey again.
The file name appears in the softkey.
5 When available, the Increment softkey can be used to enable or disable
automatically incremented file names. Auto increment adds a numeric suffix to
your file name and increments the number with each successive save. It will
truncate characters as necessary when the file name length is at maximum and
more digits are required for the numeric portion of the file name.
Emailing Setups, Screen Images, or Data
You can send oscilloscope files over the network via e-mail. You can e-mail any file
that can be saved.
To e-mail a setup, screen image, or data file:
1 Make sure the oscilloscope is connected to the local area network (see “To
establish a LAN connection"on page365).
2 Press the [Save/Recall] key.
3 In the Save/Recall Menu, press Email.
4 In the Email Menu, press Format; then, select the type of file you want to send.
You can select from the same formats that are available when saving files.
Settings for the selected format are also the same. See “Saving Setups, Screen
Images, or Data"on page343.

---
**[Page 352]**

Save/Email/Recall (Setups, Screens, Data) 21
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 353
5 Press the Attachment Name softkey and use the keypad dialog to enter the name
of the attachment file that will be sent.
6 In the e-mail configuration dialog box, touch the To, From, Server, and Subject
fields and use the keypad dialog to enter the appropriate strings.
You can also enter these strings by pressing the Config Email softkey and the To,
From, Server, and Subject softkeys in the Configure Email Menu.
You can specify multiple e-mail addresses by separating each address by a
semi-colon.
The Server name is the name of your mail server running the Simple Mail
Transfer Protocol (SMTP). If you do not know this name, ask your Network
Administrator.
7 Finally, press the Press to Send Email softkey.
You can also configure the [Quick Action] key to e-mail setups, screen images, or
data. See “Configuring the [Quick Action] Key"on page381.
Recalling Setups, Masks, or Data
1 Press the [Save/Recall] key.
2 In the Save/Recall Menu, press Recall.
3 In the Recall Menu, press Recall:, then, turn the Entry knob to select the type of
file you want to recall:
• Setup (*.scp) — See “To recall setup files"on page354.
• Mask (*.msk) — See “To recall mask files"on page354.
• Reference Waveform data (*.h5) — See “To recall reference waveform files from
a USB storage device"on page354.
• Arbitrary Waveform data (*.csv) — See “To recall arbitrary waveforms"on
page355.
• CAN Symbolic data (*.dbc) — See “Loading and Displaying CAN Symbolic
Data"on page422.
You can also recall setups and mask files by loading them using the File Explorer.
See “File Explorer"on page366.
You can also configure the [Quick Action] key to recall setups, masks, or reference
waveforms. See “Configuring the [Quick Action] Key"on page381.

---
**[Page 353]**

21 Save/Email/Recall (Setups, Screens, Data)
354 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To recall setup files
Setup files can be recalled from one of 10 internal (\User Files) locations or from
an external USB storage device.
1 Press [Save/Recall] > Recall > Recall:; then, turn the Entry knob to select Setup
(*.scp).
2 Press the softkey in the second position and use the Entry knob to navigate to
the file to recall. See “To navigate storage locations"on page351.
3 Press the Press to Recall softkey.
A message indicating whether the recall was successful is displayed.
4 If you would like to clear the display, press Clear Display.
To recall mask files
Mask files can be recalled from one of four internal (\User Files) locations or from
an external USB storage device.
1 Press [Save/Recall] > Recall > Recall:; then, turn the Entry knob to select Mask
(*.msk).
2 Press the softkey in the second position and use the Entry knob to navigate to
the file to recall. See “To navigate storage locations"on page351.
3 Press the Press to Recall softkey.
A message indicating whether the recall was successful is displayed.
4 If you would like to clear the display or clear the recalled mask, press Clear
Display or Clear Mask.
To recall reference waveform files from a USB storage device
1 Press the [Save/Recall] key.
2 In the Save/Recall Menu, press the Recall softkey.
3 In the Recall Menu, press the Recall softkey and turn the Entry knob to select
Reference Waveform data (*.h5) .
4 Press the To Ref: softkey and turn the Entry knob to select the desired reference
waveform location.
5 Press the softkey in the second position and use the Entry knob to navigate to
the file to recall. See “To navigate storage locations"on page351.
6 Press the Press to Recall softkey.

---
**[Page 354]**

Save/Email/Recall (Setups, Screens, Data) 21
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 355
A message indicating whether the recall was successful is displayed.
7 If you would like to clear the display of everything except the reference
waveform, press Clear Display.
To recall arbitrary waveforms
Arbitrary waveform files can be recalled from one of four internal (\User Files)
locations or from an external USB storage device.
When recalling arbitrary waveforms (from an external USB storage device) that
were not saved from the oscilloscope, be aware that:
• If the file contains two columns, the second column is automatically chosen.
• If the file contains more than two columns, you are prompted to select which
column to load. Up to five columns are parsed by the oscilloscope; columns
above the fifth are ignored.
• The oscilloscope uses a maximum of 8192 points for an arbitrary waveform. For
more efficient recalls, make sure your arbitrary waveforms are 8192 points or
less.
To recall an arbitrary waveform:
1 Press [Save/Recall] > Recall > Recall:; then, turn the Entry knob to select Arbitrary
Waveform data (*.csv).
2 Press the softkey in the second position and use the Entry knob to navigate to
the file to recall. See “To navigate storage locations"on page351.
3 Press the Press to Recall softkey.
A message indicating whether the recall was successful is displayed.
4 If you would like to clear the display, press Clear Display.
See Also • “To edit arbitrary waveforms"on page327
Recalling Default Setups
1 Press the [Save/Recall] key.
2 In the Save/Recall Menu, press Default/Erase.
3 In the Default Menu, press one of these softkeys:

---
**[Page 355]**

21 Save/Email/Recall (Setups, Screens, Data)
356 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Default Setup— recalls the oscilloscope's default setup. This is the same as
pressing the front panel [Default Setup] key. See “Recall the Default
Oscilloscope Setup"on page32.
Some user settings are not changed when recalling the default setup.
• Factory Default— recalls the oscilloscope's factory default settings.
You must confirm the recall because there are no user settings that are left
unchanged.
Performing a Secure Erase
1 Press the [Save/Recall] key.
2 In the Save/Recall Menu, press Default/Erase.
3 In the Default menu, press Secure Erase.
This performs a secure erase of all non-volatile memory in compliance with
National Industrial Security Program Operation Manual (NISPOM) Chapter 8
requirements.
You must confirm the secure erase, and the oscilloscope will reboot when
finished.

---
**[Page 356]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
357
22 Print (Screens)
To print the oscilloscope's display / 357
To set up network printer connections / 359
To specify the print options / 360
To specify the palette option / 361
You can print the complete display, including the status line and softkeys, to a
USB printer or a network printer when the LAN connection is used.
The Print Configuration Menu is displayed when you press the [Print] key. The print
option softkeys and the Press to Print softkey are ghosted (not available) until a
printer is connected.
To print the oscilloscope's display
1 Connect a printer. You can:
• Connect a USB printer to one of the the USB ports on the front panel or the
rectangular USB host port on the rear panel.
For the most up-to-date listing of printers that are compatible with the
InfiniiVision oscilloscopes, please visit
www.keysight.com/find/InfiniiVision-printers.
• Set up a network printer connection. See “To set up network printer
connections"on page359.
2 Press the [Print] key on the front panel.
3 In the Print Configuration Menu, press the Print to softkey; then, turn the Entry
knob to select the desired printer.
4 Press the Options softkey to select the print options.

---
**[Page 357]**

22 Print (Screens)
358 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
See “To specify the print options"on page360.
5 Press the Palette softkey to select the print palette. See “To specify the palette
option"on page361.
6 Press the Press to Print softkey.
You can stop printing by pressing the Cancel Print softkey.
The oscilloscope will print the last menu visited before you pressed the [Print] key. Therefore,
NOTE
if you have measurements (Amplitude, Frequency, etc.) showing on the display before you
press [Print], the measurements will be shown on the printout.
To print the display showing the Print Configuration Menu at the bottom, press the [Print] key
twice; then, press the Press to Print softkey.
You can also configure the [Quick Action] key to print the display. See “Configuring
the [Quick Action] Key"on page381.
See Also • “To add an annotation"on page160
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 358]**

Print (Screens) 22
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 359
To set up network printer connections
When the oscilloscope is connected to a LAN, you can set up network printer
connections.
A network printer is a printer attached to a computer or print server on the
network.
1 Press the [Print] key on the front panel.
2 In the Print Configuration Menu, press the Print to softkey; then, turn the Entry
knob to select the network printer you want to configure (either #0 or #1).
3 Press the Network Setup softkey.
4 In the Network Printer Setup Menu:
a Press the Address softkey.
b In the Address keypad dialog, you can enter text using:
• The touch screen (when the front panel [Touch] key is lit).
• The Entry knob. Turn the knob to select a key in the dialog; then,
push the Entry knob to enter it.
• A connected USB keyboard.
• A connected USB mouse — you can click anything on the screen that can
be touched.
The Address is the printer or print server's address in one of the following
formats:
• IP address of a network-enabled printer (for example: 192.168.1.100 or
192.168.1.100:650). Optionally, a non-standard port number can be
specified following a colon.
• IP address of a print server followed by the path to the printer (for
example: 192.168.1.100/printers/printer-name or
192.168.1.100:650/printers/printer-name).
• Path to a Windows network printer share (for example: \\server\share).
c When you are done entering text, select the dialog's Enter or OK key or press
the Address softkey again.

---
**[Page 359]**

22 Print (Screens)
360 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The address appears in the softkey.
d When the Address is a Windows network printer share, these softkeys appear
and let you enter additional settings:
• Domain — this is the Windows network domain name.
• Username — this is your login name for the Windows network domain.
• Password — this is your login password for the Windows network domain.
To clear an entered password, press the Clear key in the Password keypad
dialog.
e Press the Apply softkey to make the printer connection.
A message appears to tell you whether the connection was successful.
To specify the print options
In the Print Configuration Menu, press the Options softkey to change the following
options:
• Setup Information — Select this to print oscilloscope setup information on your
printout, including vertical, horizontal, trigger, acquisition, math, and display
settings.
• Invert Graticule Colors — Select this to reduce the amount of black ink it takes to
print oscilloscope images by changing the black background to white. Invert
Graticule Colors is the default mode.
• Form Feed — Select this to send a form feed command to the printer after the
waveform is printed and before the setup information is printed. Switch Form
Feed off if you want setup information printed on the same sheet of paper with
the waveform. This option only has an effect when the Setup Information option is
selected. Also, if the amount of setup information will not fit on the same page
with the waveform, it will be printed on a new page regardless of the Form Feed
setting.
• Landscape — Select this to print horizontally on the page instead of vertically
(portrait mode).

---
**[Page 360]**

Print (Screens) 22
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 361
To specify the palette option
In the Print Configuration Menu, press the Palette softkey to change the following
options.
• Color — Select this to print the screen in color.
• Grayscale — Select this to print the screen in shades of gray rather than in color.

---
**[Page 361]**

22 Print (Screens)
362 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 362]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
363
23 Utility Settings
I/O Interface Settings / 363
Setting up the Oscilloscope's LAN Connection / 364
File Explorer / 366
Setting Oscilloscope Preferences / 369
Setting the Oscilloscope's Clock / 373
Setting the Rear Panel TRIG OUT Source / 374
Setting the Reference Signal Mode / 375
Enabling Remote Command Logging / 377
Performing Service Tasks / 378
Configuring the [Quick Action] Key / 381
This chapter explains oscilloscope utility functions.
I/O Interface Settings
The oscilloscope can be accessed and/or controlled remotely via these I/O
interfaces:
• USB device port on the rear panel (square shaped USB port).
• LAN interface on the rear panel.
To configure the I/O interfaces:
1 On the oscilloscope's front panel, press [Utility].
2 In the Utility Menu, press I/O.
3 In the I/O Menu, press Configure.

---
**[Page 363]**

23 Utility Settings
364 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• LAN — When connected to a LAN, you can use the LAN Settings and LAN Reset
softkeys to configure the LAN interface. See “Setting up the Oscilloscope's
LAN Connection"on page364.
• There are no configuration settings for the USB interface.
When an I/O interface is installed, remote control over that interface is always
enabled. Also, the oscilloscope can be controlled via multiple I/O interfaces (for
example, USB and LAN) at the same time.
See Also • Chapter24, “Web Interface,” starting on page 383 (when the oscilloscope is
connected to a LAN).
• “Remote Programming via the Web Interface"on page389
• The oscilloscope's Programmer's Guide.
• “Remote Programming with Keysight IO Libraries"on page390
Setting up the Oscilloscope's LAN Connection
Using the rear panel LAN port, you can place the oscilloscope on the network and
set up its LAN connection. Once that is done, you can set up and use network
printers or use the oscilloscope's web interface or remotely control the
oscilloscope via the LAN interface.
The oscilloscope supports methods for automated LAN configuration or manual
LAN configuration (see “To establish a LAN connection"on page365). It is also
possible to set up a point-to-point LAN connection between a PC and the
oscilloscope (see “Stand-alone (Point-to-Point) Connection to a PC"on
page366).
Once the oscilloscope is set up on the network, you can use the oscilloscope's
web page to view or change its network configuration and access additional
settings (like the network password). See Chapter24, “Web Interface,” starting on
page 383.
When you connect the oscilloscope to a LAN it is a good practice to limit access to the
NOTE
oscilloscope by setting a password. By default, the oscilloscope is not password protected.
See “Setting a Password"on page397 to set a password.
| NOTE |
|---|
|  |

---
**[Page 364]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 365
Any time you modify the oscilloscope's hostname, it breaks the connection between the
NOTE
oscilloscope and the LAN. You need to re-establish communication to the oscilloscope using
the new hostname.
To establish a LAN connection
Automatic 1 Press [Utility] > I/O.
Configuration
2 Press the LAN Settings softkey.
3 Press the Config softkey; then, turn the Entry knob to select Automatic, and press
the softkey again to enable it.
If your network supports DHCP or AutoIP, enabling Automatic lets the
oscilloscope use those services to get its LAN configuration settings
4 If your network provides Dynamic DNS, you can enable the Dynamic DNS option
to let the oscilloscope register its hostname and use the DNS server for name
resolution.
5 You can enable the Multicast DNS option to let the oscilloscope use Multicast
DNS for name resolution on small networks without a conventional DNS server.
6 Connect the oscilloscope to the local area network (LAN) by inserting the LAN
cable into the "LAN" port on the rear panel of the oscilloscope.
In a few moments the oscilloscope will connect to the network automatically.
If the oscilloscope does not automatically connect to the network, press [Utility]
> I/O > LAN Reset. In a few moments the oscilloscope will connect to the
network.
Manual 1 Get the oscilloscope's network parameters (host name, IP address, subnet
Configuration mask, gateway IP, DNS IP, etc.) from your network administrator.
2 Press [Utility] > I/O.
3 Press the LAN Settings softkey.
4 Press the Config softkey; then, turn the Entry knob to select Automatic, and press
the softkey again to disable it.
If Automatic is not enabled, the oscilloscope's LAN configuration must be set
up manually using the Modify and Host name softkeys
| NOTE |
|---|
|  |

---
**[Page 365]**

23 Utility Settings
366 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
5 Configure the oscilloscope's LAN interface:
a Use the Modify softkey (and the other softkeys and keypad entry dialogs) to
enter the IP Address, Subnet Mask, Gateway IP, and DNS IP values.
b Press the Hostname softkey and use the keypad entry dialog to enter the
Host Name.
c Press the Apply softkey.
6 Connect the oscilloscope to the local area network (LAN) by inserting the LAN
cable into the "LAN" port on the rear panel of the oscilloscope.
Stand-alone (Point-to-Point) Connection to a PC
The following procedure describes how to establish a point-to-point (stand alone)
connection to the oscilloscope. This is useful if you want to control the
oscilloscope using a laptop computer or a stand-alone computer.
1 Press [Utility] > I/O.
2 Press the LAN Settings softkey.
3 Press the Config softkey; then, turn the Entry knob to select Automatic, and press
the softkey again to enable it.
If your network supports DHCP or AutoIP, enabling Automatic lets the
oscilloscope use those services to get its LAN configuration settings
4 Connect your PC to the oscilloscope using a cross-over LAN cable such as
Keysight part number 5061-0701, available on the web at
www.parts.keysight.com.
5 Cycle power on the oscilloscope. Wait until the LAN connection is configured:
• Press [Utility] > I/O and wait until the LAN status shows "configured".
This may take a few minutes.
Now, the instrument is connected, and the instrument's web interface or remote
control via LAN may be used.
File Explorer
The File Explorer lets you navigate the oscilloscope's internal file system and the
file systems of connected USB storage devices.
From the internal file system, you can load oscilloscope setup files or mask files.

---
**[Page 366]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 367
From a connected USB storage device, you can load setup files, mask files, license
files, firmware update (*.ksx) files, label files, etc. Also, you can delete files on a
connected USB storage device.
The USB port on the front panel, and the USB port on the rear panel labeled "HOST" are USB
NOTE
Series A receptacles. These are the receptacles to which you can connect USB mass storage
devices and printers.
The square receptacle on the rear panel labeled "DEVICE" is provided for controlling the
oscilloscope over USB. See the Programmer's Guide for more information.
The oscilloscope's internal file system, under "\User Files", consists of 10 locations
for oscilloscope setup files, four locations for mask files, and four locations for
waveform generator arbitrary waveform files.
To use the File Explorer:
1 Press [Utility] > File Explorer.
2 In the File Explorer Menu, press the softkey in the first position and use the
Entry knob to navigate.
| NOTE |
|---|
|  |

---
**[Page 367]**

23 Utility Settings
368 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The softkey in the first position can have these labels:
• Press to go — when you can push the Entry knob to navigate to a new folder
or storage location.
• Location — when pointing to a directory that is currently selected.
• Selected — when pointing to a file that can be loaded or deleted.
When this label appears, you can press the Load File or Delete File softkeys to
take the action.
Pushing the Entry knob is the same as pressing the Load File softkey.
A file that has been deleted from a USB storage device cannot be recovered
by the oscilloscope.
Use your PC to create directories on a USB storage device.
USB Storage Most USB mass storage devices are compatible with the oscilloscope. However,
Devices certain devices may be incompatible, and may not be able to be read or written to.
USB storage devices must be formatted with the FAT or FAT32 file system format.
|  |  |
|---|---|

---
**[Page 368]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 369
When the USB mass storage device is connected to the oscilloscope's front or rear
USB host port, a small four-color circle icon may be displayed briefly as the USB
device is read.
You do not need to "eject" the USB mass storage device before removing it. Simply
ensure that any file operation you've initiated is done, and remove the USB drive
from the oscilloscope's host port.
Do not connect USB devices that identify themselves as hardware type "CD"
because these devices are not compatible with the InfiniiVision X-Series
oscilloscopes.
If two USB mass storage devices are connected to the oscilloscope, the first one is
designated "\usb" and the second one is designated "\usb2".
See Also • Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on page 343
Setting Oscilloscope Preferences
The User Preferences Menu (under [Utility] > Options > Preferences) lets you specify
oscilloscope preferences.
• “To choose "expand about" center or ground"on page369
• “To disable/enable transparent backgrounds"on page370
• “To set voice recognition and speaker options"on page370
• “To set up the screen saver"on page371
• “To set Autoscale preferences"on page372
• “Jitter-Free Trigger"on page373
To choose "expand about" center or ground
When you change a channel's volts/division setting, the waveform display can be
set to expand (or compress) about the signal ground level or the center of the
display.
To set the waveform expansion reference point:
1 Press [Utility] > Options > Preferences > Expand and select:
• Ground— The displayed waveform will expand about the position of the
channel's ground. This is the default setting.

---
**[Page 369]**

23 Utility Settings
370 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The ground level of the signal is identified by the position of the ground level
( ) icon at the far-left side of the display.
The ground level will not move when you adjust the vertical sensitivity
(volts/division) control.
If the ground level is off screen, the waveform will expand about the top or
bottom edge of the screen based on where the ground is off screen.
• Center— The displayed waveform will expand about the center of the display.
To disable/enable transparent backgrounds
There is a preference setting for whether measurements, statistics, reference
waveform information, and other text displays have transparent or solid
backgrounds.
1 Press [Utility] > Options >Preferences.
2 Press Transparent to toggle between transparent and solid text display
backgrounds.
To set voice recognition and speaker options
The oscilloscope's voice recognition and speaker volume options can be set in the
user preferences.
1 Press [Utility] > Options >Preferences > Audio to display the Audio Menu.
You can also display the Audio Menu by touching the microphone icon on the
display — see “Learn the Voice Controls"on page58.
2 Press the Voice Recognition softkey to enable or disable the feature.
3 Press the Language (Voice) softkey; then, turn the Entry knob to select your
speaking language.
4 Press the Speaker Volume softkey; then, turn the Entry knob to change the
setting.
The speaker beeps during user calibration when you need to reconnect the
calibration cable.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 370]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 371
5 Press the Beep softkey to open the beep event selection menu, use the Entry
knob (or touch) to select the event, and then press the softkey again to
enable/disable beeps on the selected event.
The oscilloscope can beep on these events:
• On Single — when you perform a single run and the single trigger occurs.
• On Trig — in the Normal trigger mode, when the trigger status transitions
from "Trig'd?" (trigger not found) to "Trig'd" (trigger found).
• On Mask Failure — when relatively rare mask test failures occur.
• On DVM Limit — when the specified digital voltmeter reading limit occurs.
Press the Limits softkey to open a menu where you can specify the limits. See
“Digital Voltmeter"on page318.
• On Long Save — when saving a file takes longer than 20 seconds and the save
completes.
• On Calibration — when performing a user calibration and it is time to move the
calibration cable from one channel to the next.
To set up the screen saver
The oscilloscope can be configured to turn on a display screen saver when the
oscilloscope has been idle for a specified length of time.
1 Press [Utility] > Options >Preferences > ScreenSaver to display the Screen Saver
Menu.
2 Press the Screen Saver softkey to select the screen saver type.
The screen saver can be set to Off, to display any of the images shown in the
list, or can display a user-defined text string.
If User is selected:
|  |  |
|---|---|

---
**[Page 371]**

23 Utility Settings
372 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
a Press the Text softkey.
b In the Text keypad dialog, you can enter text using:
• The touch screen (when the front panel [Touch] key is lit).
• The Entry knob. Turn the knob to select a key in the dialog; then,
push the Entry knob to enter it.
• A connected USB keyboard.
• A connected USB mouse — you can click anything on the screen that can
be touched.
c When you are done entering text, select the dialog's Enter or OK key or press
the Text softkey again.
The user-defined screen saver text appears in the softkey.
3 Press the Wait softkey; then, turn the Entry knob to select the number of
minutes to wait before the selected screen saver activates.
When you turn the Entry knob, the number of minutes is displayed on the Wait
softkey. The default time is 180 minutes (3 hours).
4 Press the Preview softkey to preview the screen saver you have selected with the
Saver softkey.
5 To view the normal display after the screen saver has started, press any key or
turn any knob.
To set Autoscale preferences
1 Press [Utility] > Options > Preferences > Autoscale.
2 In the Autoscale Preferences Menu, you can:
• Press the Fast Debug softkey enable/disable this type of autoscale.
When fast debug is enabled, autoscale lets you make quick visual
comparisons to determine whether the signal being probed is a DC voltage,
ground, or an active AC signal.
Channel coupling is maintained to allow easy viewing of oscillating signals.
|  |  |
|---|---|

---
**[Page 372]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 373
• Press the Channels softkey and turn the Entry knob to specify the channels to
be autoscaled:
• All Channels — The next time you press [Auto Scale], all channels that meet
the requirements of Autoscale will be displayed.
• Only Displayed Channels — The next time you press [Auto Scale], only the
channels that are turned on will be examined for signal activity. This is
useful if you only want to view specific active channels after pressing [Auto
Scale].
• Press the Acq Mode softkey and turn the Entry knob to select whether the
acquisition mode should be preserved during autoscale:
• Normal — to make the oscilloscope switch to Normal acquisition mode
whenever the [Auto Scale] key is pressed. This is the default mode.
• Preserve — to make the oscilloscope remain in the acquisition mode you
have chosen when the [Auto Scale] key is pressed.
Jitter-Free Trigger
Oscilloscope trigger circuitry introduces a certain amount of noise and jitter that
result in horizontal error. To correct for this error, in certain trigger modes and at
certain timebase ranges, hardware Jitter-Free Trigger correction is used to
minimize trigger jitter at the trigger point.
The effect seen on the oscilloscope display is that all plotted acquisitions cross
through the same pixel location at the intersection of the trigger level and time=0.
Jitter-Free Trigger correction works well for fast digital edges, but you may want
to turn it off for some slow slew rate analog signals.
Setting the Oscilloscope's Clock
The Clock Menu lets you set the current date and time of day (24-hour format).
This time/date stamp will appear on hardcopy prints and directory information on
the USB mass storage device.
To set the date and time, or to view the current date and time:
1 Press [Utility] >Options > Clock.

---
**[Page 373]**

23 Utility Settings
374 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 Press the Year, Month, Day, Hour or Minute softkey; then, rotate the Entry knob to
set to the desired number.
The hours are shown in the 24-hour format. So 1:00 PM is hour 13.
The real-time clock only allows selection of valid dates. If a day is selected and the
month or year is changed so the day is invalid, the day is automatically adjusted.
Setting the Rear Panel TRIG OUT Source
You can choose the source of the TRIGOUT connector on the rear panel of the
oscilloscope:
1 Press [Utility] > Options > Rear Panel.
2 In the Rear Panel Menu, press Trig Out; then, turn the Entry knob to select from:
• Triggers— Each time the oscilloscope triggers, a rising edge occurs on
TRIGOUT. The rising edge is delayed 30ns from the oscilloscope's trigger
point. The output level is 0-5V into an open circuit, and 0-2.5V into 50Ω .
See Chapter10, “Triggers,” starting on page 171.
• Mask— The pass/fail status is evaluated periodically. When the evaluation of
the testing period results in a failure, the trigger output pulses high (+5V).
Otherwise, the trigger output remains at low (0V). See Chapter18, “Mask
Testing,” starting on page 303.
• Waveform Generator 1/2 Sync Pulse— All of the waveform generator output
functions (except DC, Noise, and Cardiac) have an associated Sync signal:
The Sync signal is a TTL positive pulse that occurs when the waveform rises
above zero volts (or the DC offset value).
See Chapter20, “Waveform Generator,” starting on page 323.
The TRIGOUT connector also provides the User Calibration signal. See “To
perform user calibration"on page378.
|  |  |
|---|---|

---
**[Page 374]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 375
Setting the Reference Signal Mode
The 10 MHz REF BNC connector on the rear panel is provided so you can:
• Supply a more accurate sample clock signal to the oscilloscope, or
• Synchronize the timebase of two or more instruments.
Sample clock and The oscilloscope's timebase uses a built-in reference that has an accuracy of
frequency counter 15ppm. This is sufficient for most uses. However, if you are looking at a window
accuracy that is very narrow compared to the selected delay (for example, looking at a 15ns
pulse with the delay set to 1ms), significant error can be introduced.
Using the built-in sample clock, the oscilloscope's hardware frequency counter is
a 5-digit counter.
See “To supply a sample clock to the oscilloscope"on page375.
Supplying an When you supply an external timebase reference, the hardware frequency counter
external timebase is automatically changed to an 8-digit counter. In this case, the frequency counter
reference ([Meas] > Select > Counter) is as accurate as the external clock.
See “To synchronize the timebase of two or more instruments"on page376.
For more information on the hardware frequency counter, see “Counter"on
page262.
To supply a sample clock to the oscilloscope
1 Connect a 10MHz square or sine wave to the BNC connector labeled 10MHz
REF. The amplitude must be from -5dBm to 17dBm (356mVpp to 4.48Vpp).
Maximum input voltage at 10 MHz REF connector
CAUTION
Do not apply more than 20dBm Max (6.32Vpp Max) at the 10MHz REF BNC connector
on the rear panel or damage to the instrument may occur.
2 Press [Utility] > Options > Rear Panel > 10MHz Ref Signal.
3 Use the Entry knob and the 10MHz Ref Signal softkey to select Input On.
A locked padlock icon appears at the top of the display.
| CAUTION |
|---|
|  |

---
**[Page 375]**

23 Utility Settings
376 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If the externally supplied sample clock signal is lost, a hard unlock will occur. The
lock symbol in the upper right part of the display will become an unlocked padlock
icon and the oscilloscope will stop acquiring data. The oscilloscope will resume
sampling when the externally supplied sample clock becomes stable again.
To synchronize the timebase of two or more instruments
The oscilloscope can output its 10MHz system clock for the purpose of
synchronization with other instruments.
1 Connect a BNC cable to the BNC connector labeled 10MHz REF on the rear
panel of the oscilloscope.
2 Connect the other end of the BNC cable to the instrument(s) that will accept
the 10MHz reference signal.
The amplitude of this 10MHz reference output signal is 5Vpp into a high
impedance or 2.5Vpp into 50Ohms. It is capable of driving into lower
impedances, but the output will be reduced because of the 50Ohm source
impedance.
|  |
|---|
|  |

---
**[Page 376]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 377
3 Press [Utility] > Options > Rear Panel > 10MHz Ref Signal.
4 Use the Entry knob and the 10MHz Ref Signal softkey to select Output On.
Enabling Remote Command Logging
When the RMT license is enabled (order DSOXSCPILOG), you can enable remote
command logging. When enabled, remote commands sent to the instrument (and
results returned by the instrument) can be logged to the screen, to a text file on a
USB storage device, or to both the screen and a text file.
To enable remote command logging:
1 Press [Utility] > Options > Remote Log to open the Remote Log Menu:
2 Press Enable to enable or disable the remote command logging feature.
When remote logging is enabled, additional debug information can be included
in the returned error string. If the error is detected by the SCPI command
parser, such as a header error or other syntax error, the extra debug
information is generated and included. But if the error is detected by the
oscilloscope system, such as when an out-of-range value is sent, then no extra
debug information is included.
3 Press Destination to select whether remote commands are logged to a text file
(on a connected USB storage device), logged to the screen, or both.
4 Press Write Mode to specify whether logged commands will be created in a new
list or appended to existing logged commands.
Your selection takes effect when remote command logging is enabled.
This option applies to both screen and file logging.
5 Press File Name to open the Remote Log Filename Menu where you can specify
the name of the file (on the USB storage device) to which remote commands
are logged.
6 Press Display On to enable or disable the screen display of logged remote
commands and their return values (if applicable).
|  |  |
|---|---|

---
**[Page 377]**

23 Utility Settings
378 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
7 Press Transparent to disable or enable a transparent background for the remote
command logging screen display.
Enable to make the background transparent. This lets you view underlying
waveforms.
Disable for a solid background which makes the logged remote commands
easier to read.
Performing Service Tasks
The Service Menu (under [Utility] > Service) lets you perform service-related tasks:
• “To perform user calibration"on page378
• “To perform hardware self test"on page379
• “To perform front panel self test"on page379
• “To display oscilloscope information"on page380
• “To display the user calibration status"on page380
For other information related to oscilloscope maintenance and service, see:
• “To clean the oscilloscope"on page380
• “To check warranty and extended services status"on page380
• “To contact Keysight"on page381
• “To return the instrument"on page381
To perform user calibration
Perform user-calibration:
• Every two years or after 4000 hours of operation.
• If the ambient temperature is >10°C from the calibration temperature.
• If you want to maximize the measurement accuracy.
|  |
|---|
|  |

---
**[Page 378]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 379
The amount of use, environmental conditions, and experience with other
instruments help determine if you need shorter User Calibration intervals.
User Calibration performs an internal self-alignment routine to optimize the signal
path in the oscilloscope. The routine uses internally generated signals to optimize
circuits that affect channel sensitivity, offset, and trigger parameters.
Performing User Calibration will invalidate your Certificate of Calibration. If NIST
(National Institute of Standards and Technology) traceability is required, perform
the "Performance Verification" procedure in the Keysight InfiniiVision
6000X-Series Oscilloscopes Service Guide using traceable sources.
To perform user calibration:
1 Disconnect all inputs from the front and rear panels, including the digital
channels cable on an MSO, and allow the oscilloscope to warm up before
performing this procedure.
2 Press the rear-panel CAL button to disable calibration protection.
3 Connect the included calibration BNC cable (54609-61609) from the TRIG OUT
connector on the rear panel to the channel 1 input.
4 Press the [Utility] key; then, press the Service softkey.
5 Begin the Self Calibration by pressing the Start User Calibration softkey.
To perform hardware self test
Pressing [Utility] > Service > Hardware Self Test performs a series of internal
procedures to verify that the oscilloscope is operating properly.
It is recommended you run Hardware Self Test:
• After experiencing abnormal operation.
• For additional information to better describe an oscilloscope failure.
• To verify proper operation after the oscilloscope has been repaired.
Successfully passing Hardware Self Test does not guarantee 100% of the
oscilloscope's functionality. Hardware Self Test is designed to provide an 80%
confidence level that the oscilloscope is operating properly.
To perform front panel self test
Pressing [Utility] > Service > Front Panel Self Test lets you test the front panel keys
and knobs as well as the oscilloscope display.

---
**[Page 379]**

23 Utility Settings
380 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Follow the on-screen instructions.
To display oscilloscope information
Press [Help] > About Oscilloscope to display information about your oscilloscope:
• Model number.
• Serial number.
• Bandwidth.
• Module installed.
• Software version.
• Installed licenses. See also “Loading Licenses and Displaying License
Information"on page406.
To display the user calibration status
Pressing [Utility] > Service > User Calibration Status displays the summary results of
the previous User Calibration, and the status of probe calibrations for probes that
can be calibrated. Note that passive probes do not need to be calibrated, but
InfiniiMax probes can be calibrated. For more information about calibrating probes
see “To calibrate a probe"on page89.
To clean the oscilloscope
1 Remove power from the instrument.
2 Clean the external surfaces of the oscilloscope with a soft cloth dampened with
a mixture of mild detergent and water.
3 Make sure that the instrument is completely dry before reconnecting it to a
power source.
To check warranty and extended services status
To learn the warranty status of your oscilloscope:
1 Point your web browser to: www.keysight.com/find/warrantystatus
2 Enter your product's model number and serial number. The system will search
for the warranty status of your product and display the results. If the system
cannot find your product's warranty status, select Contact Us and speak with a
Keysight Technologies representative.

---
**[Page 380]**

Utility Settings 23
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 381
To contact Keysight
Information on contacting Keysight Technologies can be found at:
www.keysight.com/find/contactus
To return the instrument
Before shipping the oscilloscope to Keysight Technologies, contact your nearest
Keysight Technologies sales or service office for additional details. Information on
contacting Keysight Technologies can be found at:
www.keysight.com/find/contactus
1 Write the following information on a tag and attach it to the oscilloscope.
• Name and address of owner.
• Model number.
• Serial number.
• Description of service required or failure indication.
2 Remove accessories from the oscilloscope.
Only return accessories to Keysight Technologies if they are associated with the
failure symptoms.
3 Package the oscilloscope.
You can use the original shipping container, or provide your own materials
sufficient to protect the instrument during shipping.
4 Seal the shipping container securely, and mark it FRAGILE.
Configuring the [Quick Action] Key
The [Quick Action] key lets you perform common, repetitive actions by pressing a
single key.
To configure the [Quick Action] key:
1 Press [Utility] > Quick Action > Action; then, select the action that should be
performed:
• Off — disables the [Quick Action] key.

---
**[Page 381]**

23 Utility Settings
382 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Quick Measure All — displays a popup containing a snapshot of all the single
waveform measurements. The Source softkey lets you select the waveform
source (which also becomes the source selection in the Measurement
Menu). See Chapter14, “Measurements,” starting on page 245.
• Quick Measure Statistics Reset — resets all measurement statistics and the
measurement count. See “Measurement Statistics"on page272.
• Quick Mask Statistics Reset — resets mask statistics and counters. See “Mask
Statistics"on page308.
• Quick Print — prints the current screen image. Press Settings to set up the
printing options. See Chapter22, “Print (Screens),” starting on page 357.
• Quick Save — saves the current image, waveform data, or setup. Press Settings
to set up the save options. See Chapter21, “Save/Email/Recall (Setups,
Screens, Data),” starting on page 343.
• Quick Email — e-mails the current setup, screen image, or data file. Press
Settings to set up the e-mail options. See “Emailing Setups, Screen Images,
or Data"on page352.
• Quick Recall — recalls a setup, mask, or reference waveform. Press Settings to
set up the recall options. See Chapter21, “Save/Email/Recall (Setups,
Screens, Data),” starting on page 343.
• Quick Freeze Display — freezes the display without stopping running
acquisitions or un-freezes the display if currently frozen. For more
information, see “To freeze the display"on page164.
• Quick Trigger Mode — toggles the trigger mode between Auto and Normal, see
“To select the Auto or Normal trigger mode"on page210.
• Quick Clear Display — clears the display, see “To clear the display"on
page159.
Once the [Quick Action] key is configured, you simply press it to perform the
selected action.

---
**[Page 382]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
383
24 Web Interface
Accessing the Web Interface / 384
Browser Web Control / 385
Save/Recall / 391
Get Image / 393
Identification Function / 394
Instrument Utilities / 394
Setting a Password / 397
When Keysight InfiniiVision 6000X-Series oscilloscopes are set up on the LAN,
you can access the oscilloscope's built-in web server using a Java-enabled web
browser. The oscilloscope's web interface lets you:
• View information about the oscilloscope like its model number, serial number,
host name, IP address, and VISA (address) connect string.
• Control the oscilloscope using the Remote Front Panel.
• Send SCPI (Standard Commands for Programmable Instrumentation) remote
programming commands via the SCPI Commands applet window.
• Save setups, screen images, waveform data, and mask files.
• Recall setup files, reference waveform data files, or mask files.
• Get screen images and save or print them from the browser.
• Activate the Identification function to identify a particular instrument by
causing a message to be displayed or a front panel light to blink.
• View installed options, view firmware versions and install firmware upgrade
files, and view calibration status (via the Instrument Utilities page).
• View and modify the oscilloscope's network configuration.

---
**[Page 383]**

24 Web Interface
384 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The web interface for InfiniiVision X-Series oscilloscopes also provides help for
each of its pages.
Microsoft Internet Explorer is the recommended Web browser for communication
and control of the oscilloscope. Other Web browsers may work but are not
guaranteed to work with the oscilloscope. The Web browser must be
Java-enabled.
Before you can use the web interface, you must place the oscilloscope on the
network and set up its LAN connection.
Accessing the Web Interface
To access the oscilloscope's web interface:
1 Connect the oscilloscope to your LAN (see “To establish a LAN connection"on
page365) or establish a point-to-point connection (see “Stand-alone
(Point-to-Point) Connection to a PC"on page366).
It is possible to use a point-to-point connection, but using a normal LAN
connection is the preferred method.
2 Type the oscilloscope's hostname or IP address in the web browser.
The oscilloscope's web interface Welcome Page is displayed.

---
**[Page 384]**

Web Interface 24
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 385
Browser Web Control
The web interface's Browser Web Control page gives you access to:
• The Full Scope Remote Front Panel (see “Full Scope Remote Front Panel"on
page386).
• The Screen Only Remote Front Panel (see “Screen Only Remote Front
Panel"on page387).
• The Tablet Remote Front Panel (see “Tablet Remote Front Panel"on page388).
• The SCPI Command window applet for Remote Programming (see “Remote
Programming via the Web Interface"on page389).
|  |  |
|---|---|

---
**[Page 385]**

24 Web Interface
386 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If Java is not installed on your PC, you will be prompted to install the Java Plug-in. This
NOTE
plug-in must be installed on the controlling PC for the web interface's Remote Front Panel or
Remote Programming operations.
The SCPI Command window is useful for testing commands or entering a few
commands interactively. When creating automated programs for controlling the
oscilloscope, you will typically use the Keysight IO Libraries from within a
programming environment like Microsoft Visual Studio (see “Remote
Programming with Keysight IO Libraries"on page390).
Full Scope Remote Front Panel
To operate the oscilloscope using the web interface's Full Scope Remote Front
Panel:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface is displayed, select BrowserWebControl,
then select FullScopeRemoteFrontPanel. After a few seconds the Remote Front
Panel appears.
3 Click keys or knobs that you would normally press on the oscilloscope's front
panel. Drag on edges of knobs to turn them.
| NOTE |
|---|
|  |

---
**[Page 386]**

Web Interface 24
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 387
Screen Only Remote Front Panel
To operate the oscilloscope using the web interface's Screen Only Remote Front
Panel:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface is displayed, select BrowserWebControl,
then select ScreenOnlyRemoteFrontPanel. After a few seconds the Remote Front
Panel appears.
3 Use the Main Menu and the Function Keys to control the oscilloscope. To view
Quick Help, right-click on a softkey.
|  |
|---|
|  |

---
**[Page 387]**

24 Web Interface
388 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Scrolling and When using a monitor resolution of 800x600 or less on the remote computer, you
Monitor need to scroll to access the full remote front panel. To display the remote front
Resolution panel without scroll bars, use a monitor resolution greater than 800x600 on your
computer's display.
Tablet Remote Front Panel
To operate the oscilloscope using the web interface's Tablet Remote Front Panel:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
|  |
|---|
|  |

---
**[Page 388]**

Web Interface 24
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 389
2 When the oscilloscope's web interface is displayed, select BrowserWebControl,
then select TabletRemoteFrontPanel. After a few seconds the Remote Front
Panel appears.
3 Click keys or knobs that you would normally press on the oscilloscope's front
panel. Buttons have been added for turning knobs.
Remote Programming via the Web Interface
To send remote programming commands to the oscilloscope via the SCPI
Commands applet window:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface is displayed, select BrowserWebControl,
then select RemoteProgramming.
The SCPI Commands applet appears within the browser web page.
|  |
|---|
|  |

---
**[Page 389]**

24 Web Interface
390 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Remote Programming with Keysight IO Libraries
While the SCPI Commands applet window lets you enter and remote
programming commands, remote programming for automated test and data
acquisition is typically done using the Keysight IO Libraries, which are separate
from the instrument's web interface.
The Keysight IO Libraries let a controller PC communicate with Keysight
InfiniiVision X-Series oscilloscopes via their USB, LAN, or GPIB interfaces (if
available).
The Keysight IO Libraries Suite connectivity software to enables communication
over these interfaces. You can download the Keysight IO Libraries Suite from
www.keysight.com/find/iolib.
|  |  |
|---|---|

---
**[Page 390]**

Web Interface 24
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 391
Information about controlling the oscilloscope through remote commands is
contained in the Programmer's Guide, which is included on the documentation CD
supplied with this oscilloscope. You can also access this document on the
Keysight web site.
For more information about connecting to the oscilloscope, refer to the Keysight
Technologies USB/LAN/GPIB Interfaces Connectivity Guide. For a printable
electronic copy of the Connectivity Guide, direct your Web browser to
www.keysight.com and search for "Connectivity Guide".
Save/Recall
You can save setup files, screen images, waveform data files, or mask files to your
PC via the oscilloscope's web interface (see “Saving Files via the Web
Interface"on page391).
You can recall setup files, reference waveform data files, or mask files from your PC
via the oscilloscope's web interface (see “Recalling Files via the Web
Interface"on page392).
Saving Files via the Web Interface
To save setup files, screen images, waveform data, Lister data, or mask files to
your PC via the oscilloscope's web interface:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface is displayed, select the Save/Recall tab
from the left side of the Welcome screen.
3 Click the Save link.
4 On the Save page:
a Enter the name of the file you are saving to.
b Select the format.

---
**[Page 391]**

24 Web Interface
392 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You can click Preview to view the oscilloscope's current screen image. When
previewing, you can use the New Acquisition check box to force a new
acquisition before the preview.
With some formats, you can click Save Setup Info to save setup information to
an ASCII .txt format file.
c Click Save.
The current acquisition is saved.
d In the File Download dialog, click Save.
e In the Save As dialog, navigate to the folder where you want to save the file;
then, click Save.
Recalling Files via the Web Interface
To recall setup files, reference waveform data files, mask files, or arbitrary
waveform files from your PC via the oscilloscope's web interface:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface is displayed, select the Save/Recall tab
from the left side of the Welcome screen.
|  |  |
|---|---|

---
**[Page 392]**

Web Interface 24
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 393
3 Click the Recall link.
4 On the Recall page:
a Click Browse....
b In the "Choose file" dialog, select the file you want to recall; then, click Open.
c When recalling reference waveform data files, select the To Reference
Waveform location.
d Click Recall.
Get Image
To save (or print) the oscilloscope's display from the web interface:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface is displayed, select the Get Image tab
from the left side of the Welcome screen. After a delay of several seconds, the
oscilloscope's screen image will be displayed.
3 Right-click on the image and select Save Picture As... (or Print Picture...).
4 Select a storage location for the image file and click Save.
|  |  |
|---|---|

---
**[Page 393]**

24 Web Interface
394 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Identification Function
The Identification web interface feature is useful when trying to locate a specific
instrument in a rack of equipment.
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface Welcome Page is displayed, select the
Identification on radio button.
An "Identify" message is displayed on the oscilloscope; you can either select
Identification off or press the OK softkey on the oscilloscope to continue.
Identification option
Instrument Utilities
The Instrument Utilities page of the web interface lets you:
| Identification option |
|---|
|  |

---
**[Page 394]**

Web Interface 24
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 395
• View installed options.
• View firmware versions.
• Install firmware upgrade files.
• View calibration status.
You can select these capabilities via a drop-down menu.

---
**[Page 395]**

24 Web Interface
396 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
|  |
|---|
|  |

---
**[Page 396]**

Web Interface 24
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 397
Setting a Password
Whenever you connect the oscilloscope to a LAN, it is good practice to set a
password. The password prevents someone from remotely accessing the
oscilloscope via a Web browser and changing parameters. Remote users can still
view the Welcome screen, view network status, etc., but they can't operate the
instrument or change its setup without the password.
To set a password:
1 Access the oscilloscope's web interface (see “Accessing the Web Interface"on
page384).
2 When the oscilloscope's web interface is displayed, select the Configure
Network tab from the instrument's Welcome page.
3 Click the Modify Configuration button.
Modify Configuration
Configure
Network
tab
4 Enter your desired password, and click Apply Changes.
| Modify Configuration
Configure
Network
tab | Modify Configuration
Configure
Network
tab |
|---|---|

---
**[Page 397]**

24 Web Interface
398 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Enter
password
When accessing the password protected oscilloscope, the user name is the IP
address of the oscilloscope.
To reset the Do one of these things to reset the password:
password
• Using the keys on the front panel of the oscilloscope, press [Utility] > I/O > LAN
Reset.
• Using the web browser select the Configure Network tab, select Modify
Configuration, erase the Password, and select Apply Changes.
| Enter
password | Enter
password |
|---|---|

---
**[Page 398]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
399
25 Reference
Specifications and Characteristics / 399
Measurement Category / 399
Environmental Conditions / 401
Probes and Accessories / 401
Loading Licenses and Displaying License Information / 406
Software and Firmware Updates / 409
Binary Data (.bin) Format / 409
CSV and ASCII XY files / 416
Acknowledgements / 418
Specifications and Characteristics
Please see the InfiniiVision oscilloscope data sheets for complete, up-to-date
specifications and characteristics. To download a data sheet, please visit:
www.keysight.com/find/6000X-Series
Then, select the Library tab, followed by Specifications.
Or, go to the Keysight home page at www.keysight.com and search for "6000
X-Series oscilloscopes data sheet".
To order a data sheet by phone, please contact your local Keysight office. The
complete list is available at: www.keysight.com/find/contactus.
Measurement Category
• “Oscilloscope Measurement Category"on page400
• “Measurement Category Definitions"on page400
• “Transient Withstand Capability"on page400

---
**[Page 399]**

25 Reference
400 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Oscilloscope Measurement Category
The InfiniiVision oscilloscopes are intended to be used for measurements in
Measurement Category I.
Use this instrument only for measurements within its specified measurement category.
WARNING
Measurement Category Definitions
Measurement category I is for measurements performed on circuits not directly
connected to MAINS. Examples are measurements on circuits not derived from
MAINS, and specially protected (internal) MAINS derived circuits. In the latter
case, transient stresses are variable; for that reason, the transient withstand
capability of the equipment is made known to the user.
Measurement category II is for measurements performed on circuits directly
connected to the low voltage installation. Examples are measurements on
household appliances, portable tools and similar equipment.
Measurement category III is for measurements performed in the building
installation. Examples are measurements on distribution boards, circuit-breakers,
wiring, including cables, bus-bars, junction boxes, switches, socket-outlets in the
fixed installation, and equipment for industrial use and some other equipment, for
example, stationary motors with permanent connection to the fixed installation.
Measurement category IV is for measurements performed at the source of the
low-voltage installation. Examples are electricity meters and measurements on
primary overcurrent protection devices and ripple control units.
Transient Withstand Capability
Maximum input voltage at analog inputs
CAUTION
300Vrms, 400Vpk; transient overvoltage 1.6kVpk
50Ω input: 5Vrms Input protection is enabled in 50Ω mode and the 50Ω load will
disconnect if greater than 5Vrms is detected. However the inputs could still be damaged,
depending on the time constant of the signal. The 50Ω input protection only functions
when the oscilloscope is powered on.
| WARNING |
|---|
|  |
| CAUTION |
|---|
|  |

---
**[Page 400]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 401
Maximum input voltage at digital channels
CAUTION
±40V peak; transient overvoltage 800Vpk
Environmental Conditions
Environment Indoor use only.
Ambient Operating 0°C to +50°C; non-operating –30°C to +70°C
temperature
Humidity Operating: 50% to 95% RH at 40°C for 5 days.
Non-operating: 90% RH at 65°C for 24 hr.
Altitude Maximum operating altitude: 4,000 m (13,123ft)
Overvoltage This product is intended to be powered by MAINS that comply to Overvoltage
Category Category II, which is typical of cord-and-plug connected equipment.
Pollution Degree The InfiniiVision 6000X-Series oscilloscopes may be operated in environments
of Pollution Degree 2 (or Pollution Degree 1).
Pollution Degree Pollution Degree 1: No pollution or only dry, non-conductive pollution occurs.
Definitions The pollution has no influence. Example: A clean room or climate controlled
office environment.
Pollution Degree 2. Normally only dry non-conductive pollution occurs.
Occasionally a temporary conductivity caused by condensation may occur.
Example: General indoor environment.
Pollution Degree 3: Conductive pollution occurs, or dry, non-conductive
pollution occurs which becomes conductive due to condensation which is
expected. Example: Sheltered outdoor environment.
Probes and Accessories
This section lists the probes and accessories that are compatible with the
6000X-Series oscilloscopes.
• “Passive Probes"on page402
• “Single-Ended Active Probes"on page403
• “Differential Probes"on page404
| CAUTION |
|---|
|  |
| Environment | Indoor use only. |
|---|---|
| Ambient
temperature | Operating 0°C to +50°C; non-operating –30°C to +70°C |
| Humidity | Operating: 50% to 95% RH at 40°C for 5 days.
Non-operating: 90% RH at 65°C for 24 hr. |
| Altitude | Maximum operating altitude: 4,000 m (13,123ft) |
| Overvoltage
Category | This product is intended to be powered by MAINS that comply to Overvoltage
Category II, which is typical of cord-and-plug connected equipment. |
| Pollution Degree | The InfiniiVision 6000X-Series oscilloscopes may be operated in environments
of Pollution Degree 2 (or Pollution Degree 1). |
| Pollution Degree
Definitions | Pollution Degree 1: No pollution or only dry, non-conductive pollution occurs.
The pollution has no influence. Example: A clean room or climate controlled
office environment.
Pollution Degree 2. Normally only dry non-conductive pollution occurs.
Occasionally a temporary conductivity caused by condensation may occur.
Example: General indoor environment.
Pollution Degree 3: Conductive pollution occurs, or dry, non-conductive
pollution occurs which becomes conductive due to condensation which is
expected. Example: Sheltered outdoor environment. |

---
**[Page 401]**

25 Reference
402 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• “Current Probes"on page405
• “Accessories Available"on page405
AutoProbe Most Keysight single-ended active, differential, and current probes are compatible
Interface with the AutoProbe interface. Active probes that do not have their own external
power supply require substantial power from the AutoProbe interface.
In the following tables, for AutoProbe interface compatible probes, "Quantity
Supported" indicates the maximum number of each type of active probe that can
be connected to the oscilloscope.
If too much current is drawn from the AutoProbe interface, an error message will
be displayed, indicating that you must momentarily disconnect all probes to reset
the AutoProbe interface, then connect only the supported quantity of active
probes.
See Also For more information on probes and accessories, see www.keysight.com for:
• Probes and Accessories Selection Guide (5989-6162EN)
• InfiniiVision Oscilloscope Probes and Accessories Selection Guide Data Sheet
(5968-8153EN)
Passive Probes
InfiniiVision 6000X-Series oscilloscopes recognize passive probes such as the
N2894A, 10070D, N2870A, etc. These probes have a pin on their connector that
connects to the ring around the oscilloscope's BNC connector. Therefore, the
oscilloscope will automatically set the attenuation factor for recognized Keysight
passive probes.
Passive probes that do not have a pin that connects to the ring around the BNC
connector will not be recognized by the oscilloscope, and you must set the probe
attenuation factor manually. See “To specify the probe attenuation"on page88.
The following passive probes can be used with the InfiniiVision 6000X-Series
oscilloscopes. Any combination of passive probes can be used.
Table 4 Passive Probes
Model Description
10076B High-voltage passive probe, 100:1, 4kV, 250MHz
N2771B High-voltage passive probe, 1000:1, 30kV, 50MHz
| Model | Description |
|---|---|
| 10076B | High-voltage passive probe, 100:1, 4kV, 250MHz |
| N2771B | High-voltage passive probe, 1000:1, 30kV, 50MHz |

---
**[Page 402]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 403
Table 4 Passive Probes (continued)
Model Description
N2874A Low impedance passive probe, 10:1, 1.5GHz, 500ohm input Z, 1.3m
N2876A Low impedance passive probe, 100:1, 1.5GHz, 5kohm input Z, 1.3m
N2894A Passive probe, 10:1, 700MHz, 1.3m
Single-Ended Active Probes
The following single-ended active probes can be used with the InfiniiVision
6000X-Series oscilloscopes.
Table 5 Active Probes
Model Description Quantity
Supported1
1130A 1.5GHz InfiniiMax amplifier (with single-ended probe 4
head)
1131A 3.5GHz InfiniiMax amplifier (with single-ended probe 4
head)
1132A 5GHz InfiniiMax amplifier (with single-ended probe head) 4
1134A 7GHz InfiniiMax amplifier (with single-ended probe head) 4
N2750A InfiniiMode active differential probe (in single-ended 4
modes), 1.5GHz, 30VDC + peak AC max with AutoProbe
interface
N2751A InfiniiMode active differential probe (in single-ended 4
modes), 3.5GHz, 30VDC + peak AC max with AutoProbe
interface
N2752A InfiniiMode active differential probe (in single-ended 4
modes), 6GHz, 30VDC + peak AC max with AutoProbe
interface
N2744A T2A probe interface adapter Unknown,
depends on
probes
connected
| Model | Description |
|---|---|
| N2874A | Low impedance passive probe, 10:1, 1.5GHz, 500ohm input Z, 1.3m |
| N2876A | Low impedance passive probe, 100:1, 1.5GHz, 5kohm input Z, 1.3m |
| N2894A | Passive probe, 10:1, 700MHz, 1.3m |
| Model | Description | Quantity
Supported1 |
|---|---|---|
| 1130A | 1.5GHz InfiniiMax amplifier (with single-ended probe
head) | 4 |
| 1131A | 3.5GHz InfiniiMax amplifier (with single-ended probe
head) | 4 |
| 1132A | 5GHz InfiniiMax amplifier (with single-ended probe head) | 4 |
| 1134A | 7GHz InfiniiMax amplifier (with single-ended probe head) | 4 |
| N2750A | InfiniiMode active differential probe (in single-ended
modes), 1.5GHz, 30VDC + peak AC max with AutoProbe
interface | 4 |
| N2751A | InfiniiMode active differential probe (in single-ended
modes), 3.5GHz, 30VDC + peak AC max with AutoProbe
interface | 4 |
| N2752A | InfiniiMode active differential probe (in single-ended
modes), 6GHz, 30VDC + peak AC max with AutoProbe
interface | 4 |
| N2744A | T2A probe interface adapter | Unknown,
depends on
probes
connected |

---
**[Page 403]**

25 Reference
404 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Table 5 Active Probes (continued)
Model Description Quantity
Supported1
N2795A Active probe, 1GHz with AutoProbe interface 4
N2796A Active probe, 2GHz with AutoProbe interface 4
1See “AutoProbe Interface"on page402.
Differential Probes
The following differential probes can be used with the InfiniiVision 6000X-Series
oscilloscopes.
Table 6 Differential Probes
Model Description Quantity
Supported1
1130A 1.5GHz InfiniiMax amplifier (with differential probe head) 4
1131A 3.5GHz InfiniiMax amplifier (with differential probe head) 4
1132A 5GHz InfiniiMax amplifier (with differential probe head) 4
1134A 7GHz InfiniiMax amplifier (with differential probe head) 4
N2750A InfiniiMode active differential probe, 1.5GHz, 30VDC + peak AC max with 4
AutoProbe interface
N2751A InfiniiMode active differential probe, 3.5GHz, 30VDC + peak AC max with 4
AutoProbe interface
N2752A InfiniiMode active differential probe, 6GHz, 30VDC + peak AC max with 4
AutoProbe interface
N2790A High-voltage differential probe, 50:1 or 500:1 (switchable), 100MHz with 4
AutoProbe interface
N2791A High-voltage differential probe, 25MHz, +/-700V, 1MOhm termination,
10:1 or 100:1 (switchable)
N2792A Differential probe, 200MHz 10:1, 50Ohm termination
N2793A Differential probe, 800MHz 10:1, +/-15V, 50Ohm termination
| Model | Description | Quantity
Supported1 |
|---|---|---|
| N2795A | Active probe, 1GHz with AutoProbe interface | 4 |
| N2796A | Active probe, 2GHz with AutoProbe interface | 4 |
| 1See “AutoProbe Interface"on page402. |  |  |
| Model | Description | Quantity
Supported1 |
|---|---|---|
| 1130A | 1.5GHz InfiniiMax amplifier (with differential probe head) | 4 |
| 1131A | 3.5GHz InfiniiMax amplifier (with differential probe head) | 4 |
| 1132A | 5GHz InfiniiMax amplifier (with differential probe head) | 4 |
| 1134A | 7GHz InfiniiMax amplifier (with differential probe head) | 4 |
| N2750A | InfiniiMode active differential probe, 1.5GHz, 30VDC + peak AC max with
AutoProbe interface | 4 |
| N2751A | InfiniiMode active differential probe, 3.5GHz, 30VDC + peak AC max with
AutoProbe interface | 4 |
| N2752A | InfiniiMode active differential probe, 6GHz, 30VDC + peak AC max with
AutoProbe interface | 4 |
| N2790A | High-voltage differential probe, 50:1 or 500:1 (switchable), 100MHz with
AutoProbe interface | 4 |
| N2791A | High-voltage differential probe, 25MHz, +/-700V, 1MOhm termination,
10:1 or 100:1 (switchable) |  |
| N2792A | Differential probe, 200MHz 10:1, 50Ohm termination |  |
| N2793A | Differential probe, 800MHz 10:1, +/-15V, 50Ohm termination |  |

---
**[Page 404]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 405
Table 6 Differential Probes (continued)
Model Description Quantity
Supported1
N2891A 70MHz, 7kV high-voltage differential probe
1See “AutoProbe Interface"on page402.
Current Probes
The following current probes can be used with the InfiniiVision 6000X-Series
oscilloscopes.
Table 7 Current Probes
Model Description Quantity
Supported1
1146B Current probe, 100kHz, 100A, AC/DC
1147B Current probe, 50MHz, 15A, AC/DC with AutoProbe interface 4
N2780B Current probe, 2MHz, 500A, AC/DC (use with N2779A power supply)
N2781B Current probe, 10MHz, 150A, AC/DC (use with N2779A power supply)
N2782B Current probe, 50MHz, 30A, AC/DC (use with N2779A power supply)
N2783B Current probe, 100MHz, 30A, AC/DC (use with N2779A power supply)
N2820A Current probe, 3MHz/50uA High Sensitivity AC/DC (2-ch) 2
N2821A Current probe, 3MHz/50uA High Sensitivity AC/DC (1-ch) 4
N2893A Current probe, 100MHz, 15A, AC/DC with AutoProbe interface 4
1See “AutoProbe Interface"on page402.
Accessories Available
In addition to passive proves (“Passive Probes"on page402), single-ended active
probes (“Single-Ended Active Probes"on page403), differential probes
(“Differential Probes"on page404), and current probes (“Current Probes"on
page405), the following accessories are available for the InfiniiVision
6000X-Series oscilloscopes.
| Model | Description | Quantity
Supported1 |
|---|---|---|
| N2891A | 70MHz, 7kV high-voltage differential probe |  |
| 1See “AutoProbe Interface"on page402. |  |  |
| Model | Description | Quantity
Supported1 |
|---|---|---|
| 1146B | Current probe, 100kHz, 100A, AC/DC |  |
| 1147B | Current probe, 50MHz, 15A, AC/DC with AutoProbe interface | 4 |
| N2780B | Current probe, 2MHz, 500A, AC/DC (use with N2779A power supply) |  |
| N2781B | Current probe, 10MHz, 150A, AC/DC (use with N2779A power supply) |  |
| N2782B | Current probe, 50MHz, 30A, AC/DC (use with N2779A power supply) |  |
| N2783B | Current probe, 100MHz, 30A, AC/DC (use with N2779A power supply) |  |
| N2820A | Current probe, 3MHz/50uA High Sensitivity AC/DC (2-ch) | 2 |
| N2821A | Current probe, 3MHz/50uA High Sensitivity AC/DC (1-ch) | 4 |
| N2893A | Current probe, 100MHz, 15A, AC/DC with AutoProbe interface | 4 |
| 1See “AutoProbe Interface"on page402. |  |  |

---
**[Page 405]**

25 Reference
406 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Table 8 Accessories Available for InfiniiVision 6000X-Series Oscilloscopes
Model/Part # Description
N2111A Rack mount kit
N2733B Soft carrying case
N2786A 2-leg probe positioner
N2787A 3D probe positioner
1180CZ Testmobile
N2112A Hardcopy user's guide
various Front panel overlays - see “Front Panel Overlays for Different
Languages"on page43.
N2756-60001 16-channel logic probe and accessory kit (standard with MSO models and with
MSO upgrade)
01650-61607 Logic cable and terminator (40 pin to 40 pin MSO cable)
You can find these items at www.keysight.com or at www.parts.keysight.com.
For information on more probes and accessories, see www.keysight.com for:
• Probes and Accessories Selection Guide (5989-6162EN)
• InfiniiVision Oscilloscope Probes and Accessories Selection Guide Data Sheet
(5968-8153EN)
Loading Licenses and Displaying License Information
License files are loaded from a USB storage device using the File Explorer (see
“File Explorer"on page366).
License information is displayed with other oscilloscope information (see “To
display oscilloscope information"on page380).
For more information about the licenses and other oscilloscope options available,
see:
• “Licensed Options Available"on page407
• “Other Options Available"on page408
| Model/Part # | Description |
|---|---|
| N2111A | Rack mount kit |
| N2733B | Soft carrying case |
| N2786A | 2-leg probe positioner |
| N2787A | 3D probe positioner |
| 1180CZ | Testmobile |
| N2112A | Hardcopy user's guide |
| various | Front panel overlays - see “Front Panel Overlays for Different
Languages"on page43. |
| N2756-60001 | 16-channel logic probe and accessory kit (standard with MSO models and with
MSO upgrade) |
| 01650-61607 | Logic cable and terminator (40 pin to 40 pin MSO cable) |

---
**[Page 406]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 407
• “Upgrading to an MSO"on page409
Licensed Options Available
The following licensed options can be easily installed without returning the
oscilloscope to a Service Center. See data sheets for details.
Table 9 Licensed Options Available
License Description After purchase model number, notes
AERO MIL-STD-1553 and ARINC 429 Serial Triggering and Analysis. Order DSOX6AERO.
AUDIO Audio Serial Triggering and Analysis (I2S). Order DSOX6AUDIO.
AUTO Automotive Serial Triggering and Analysis (CAN,LIN). Order DSOX6AUTO.
CANFD Automotive Serial Triggering and Analysis (CAN,LIN). Order DSOX6AUTO.
COMP Computer Serial Triggering and Analysis Order DSOX6COMP.
(RS232/422/485/UART).
Provides trigger and decode capability for many UART
(Universal Asynchronous Receiver/Transmitter) protocols
including RS232 (Recommended Standard 232).
DVMCTR Digital Voltmeter and Counter Order DSOXDVMCTR.
Provides provides 3-digit voltage and counter measurements
using any analog channel.
EDK Educator's Kit Order DSOXEDK.
Provides training signals on the oscilloscope's Demo
terminals and a lab guide/tutorial for education
environments.
EMBD Embedded Serial Triggering and Analysis (I2C, SPI). Order DSOX6EMBD.
FLEX FlexRay Triggering and Analysis. Order DSOX6FLEX.
JITTER Jitter Analysis. Order DSOX6JITTER.
MASK Mask Limit Test Order DSOX6MASK.
Lets you create a mask and test waveforms to determine
whether they comply to the mask.
mem4M Memory Upgrade. Order DSOX6MEMUP.
It shows the total memory depth (4Mpts interleaved).
| License | Description | After purchase model number, notes |
|---|---|---|
| AERO | MIL-STD-1553 and ARINC 429 Serial Triggering and Analysis. | Order DSOX6AERO. |
| AUDIO | Audio Serial Triggering and Analysis (I2S). | Order DSOX6AUDIO. |
| AUTO | Automotive Serial Triggering and Analysis (CAN,LIN). | Order DSOX6AUTO. |
| CANFD | Automotive Serial Triggering and Analysis (CAN,LIN). | Order DSOX6AUTO. |
| COMP | Computer Serial Triggering and Analysis
(RS232/422/485/UART).
Provides trigger and decode capability for many UART
(Universal Asynchronous Receiver/Transmitter) protocols
including RS232 (Recommended Standard 232). | Order DSOX6COMP. |
| DVMCTR | Digital Voltmeter and Counter
Provides provides 3-digit voltage and counter measurements
using any analog channel. | Order DSOXDVMCTR. |
| EDK | Educator's Kit
Provides training signals on the oscilloscope's Demo
terminals and a lab guide/tutorial for education
environments. | Order DSOXEDK. |
| EMBD | Embedded Serial Triggering and Analysis (I2C, SPI). | Order DSOX6EMBD. |
| FLEX | FlexRay Triggering and Analysis. | Order DSOX6FLEX. |
| JITTER | Jitter Analysis. | Order DSOX6JITTER. |
| MASK | Mask Limit Test
Lets you create a mask and test waveforms to determine
whether they comply to the mask. | Order DSOX6MASK. |
| mem4M | Memory Upgrade.
It shows the total memory depth (4Mpts interleaved). | Order DSOX6MEMUP. |

---
**[Page 407]**

25 Reference
408 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Table 9 Licensed Options Available (continued)
License Description After purchase model number, notes
MSO Mixed Signal Oscilloscope (MSO). Upgrade a DSO to an MSO. Order DSOX6MSO.
Adds 16 digital channels. You do not have to install any The digital probe cable kit is supplied with
hardware. the MSO license.
PWR Power Measurement and Analysis. Order DSOX6PWR.
You can find the DSOX6PWR Power
Measurement Application User's Guide at
www.keysight.com/find/6000X-Series
-manual or on the Documentation CD.
RML Remote command logging. Order DSOXSCPILOG.
SENSOR SENT (Single Edge Nibble Transmission) Triggering and Order DSOX6SENSOR.
Analysis.
U2H USB 2.0 High Speed Triggering and Decode. Order DSOX6USBH.
USF USB 2.0 Full/Low Speed Triggering and Decode. Order DSOX6USBFL.
USBSQ USB 2.0 Signal Quality Analysis. Order DSOX6USBSQ.
You can find the USBSQ USB 2.0 Signal
Quality Analysis Application Electrical
Testing Notes manual at
www.keysight.com/find/6000X-Series
-manual or on the Documentation CD.
VID Extended Video Triggering and Analysis. Order DSOX6VID.
WAVEGEN Waveform Generator. Order DSOX6WAVEGEN2.
Other Options Available
Table 10 Calibration Option
Option Order
A6J ANSI Z540 Compliant Calibration
| License | Description | After purchase model number, notes |
|---|---|---|
| MSO | Mixed Signal Oscilloscope (MSO). Upgrade a DSO to an MSO.
Adds 16 digital channels. You do not have to install any
hardware. | Order DSOX6MSO.
The digital probe cable kit is supplied with
the MSO license. |
| PWR | Power Measurement and Analysis. | Order DSOX6PWR.
You can find the DSOX6PWR Power
Measurement Application User's Guide at
www.keysight.com/find/6000X-Series
-manual or on the Documentation CD. |
| RML | Remote command logging. | Order DSOXSCPILOG. |
| SENSOR | SENT (Single Edge Nibble Transmission) Triggering and
Analysis. | Order DSOX6SENSOR. |
| U2H | USB 2.0 High Speed Triggering and Decode. | Order DSOX6USBH. |
| USF | USB 2.0 Full/Low Speed Triggering and Decode. | Order DSOX6USBFL. |
| USBSQ | USB 2.0 Signal Quality Analysis. | Order DSOX6USBSQ.
You can find the USBSQ USB 2.0 Signal
Quality Analysis Application Electrical
Testing Notes manual at
www.keysight.com/find/6000X-Series
-manual or on the Documentation CD. |
| VID | Extended Video Triggering and Analysis. | Order DSOX6VID. |
| WAVEGEN | Waveform Generator. | Order DSOX6WAVEGEN2. |
| Option | Order |
|---|---|
| A6J | ANSI Z540 Compliant Calibration |

---
**[Page 408]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 409
Upgrading to an MSO
A license can be installed to activate the digital channels of an oscilloscope that
was not originally ordered as a mixed-signal oscilloscope (MSO). A mixed signal
oscilloscope has analog channels plus 16 time-correlated digital timing channels.
For information about upgrading your oscilloscope through licensing, contact your
local Keysight Technologies representative or see
www.keysight.com/find/6000X-Series.
Software and Firmware Updates
From time to time Keysight Technologies releases software and firmware updates
for its products. To search for firmware updates for your oscilloscope, direct your
web browser to www.keysight.com/find/6000X-Series-sw.
To view the currently installed software and firmware press [Help] > About
Oscilloscope.
Once you have downloaded a firmware update file, you can place it on a USB
storage device and load the file using File Explorer (see “File Explorer"on
page366), or you can use the Instrument Utilities page of the oscilloscope's web
interface (see “Instrument Utilities"on page394).
Binary Data (.bin) Format
The binary data format stores waveform data in binary format and provides data
headers that describe that data.
Because the data is in binary format, the size of the file is approximately 5 times
smaller than the ASCII XY format.
If more than one source is on, all displayed sources will be saved, except math
functions.
When using segmented memory, each segment is treated as a separate
waveform. All segments for a channel are saved, then all segments of the next
(higher numbered) channel are saved. This continues until all displayed channels
are saved.

---
**[Page 409]**

25 Reference
410 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
When the oscilloscope is in the Peak Detect acquisition mode, the minimum and
maximum value waveform data points are saved to the file in separate waveform
buffers. The minimum value data points are saved first; then, the maximum value
data points are saved.
BIN data - using When saving all segments, each segment has its own waveform header (see
segmented “Binary Header Format"on page410).
memory
In BIN file format, data are presented as follows:
• Channel 1 data (all segments)
• Channel 2 data (all segments)
• Channel 3 data (all segments)
• Channel 4 data (all segments)
• Digital channel data (all segments)
• Math waveform data (all segments)
When not saving all segments, the number of waveforms is equivalent to the
number of active channels (including math and digital channels, with up to seven
waveforms for each digital pod). When saving all segments, the number of
waveforms is equal to the number of active channels multiplied by the number of
segments acquired.
Binary Data in MATLAB
Binary data from an InfiniiVision oscilloscope can be imported to The MathWorks
MATLAB®. You can download the appropriate MATLAB functions from the
Keysight Technologies web site at
www.keysight.com/find/6000X-Series-examples.
Keysight provides the.m files, which need to be copied into the work directory for
MATLAB. The default work directory is C:\MATLAB7\work.
Binary Header Format
File Header There is only one file header in a binary file. The file header consists of the
following information.
Cookie Two byte characters, AG, that indicate the file is in the Keysight Binary Data file
format.
| Cookie | Two byte characters, AG, that indicate the file is in the Keysight Binary Data file
format. |
|---|---|

---
**[Page 410]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 411
Version Two bytes that represent the file version.
File Size A 32-bit integer that is the number of bytes that are in the file.
Number of A 32-bit integer that is the number of waveforms that are stored in the file.
Waveforms
Waveform Header It is possible to store more than one waveform in the file, and each waveform
stored will have a waveform header. When using segmented memory, each
segment is treated as a separate waveform. The waveform header contains
information about the type of waveform data that is stored following the waveform
data header.
Header Size A 32-bit integer that is the number of bytes in the header.
Waveform Type A 32-bit integer that is the type of waveform stored in the file:
• 0 = Unknown.
• 1 = Normal.
• 2 = Peak Detect.
• 3 = Average.
• 4 = Not used in InfiniiVision oscilloscopes.
• 5 = Not used in InfiniiVision oscilloscopes.
• 6 = Logic.
Number of A 32-bit integer that is the number of waveform buffers required to read the
Waveform data.
Buffers
Points A 32-bit integer that is the number of waveform points in the data.
Count A 32-bit integer that is the number of hits at each time bucket in the waveform
record when the waveform was created using an acquisition mode like
averaging. For example, when averaging, a count of four would mean every
waveform data point in the waveform record has been averaged at least four
times. The default value is 0.
X Display Range A 32-bit float that is the X-axis duration of the waveform that is displayed. For
time domain waveforms, it is the duration of time across the display. If the value
is zero then no data has been acquired.
X Display Origin A 64-bit double that is the X-axis value at the left edge of the display. For time
domain waveforms, it is the time at the start of the display. This value is treated
as a double precision 64-bit floating point number. If the value is zero then no
data has been acquired.
| Version | Two bytes that represent the file version. |
|---|---|
| File Size | A 32-bit integer that is the number of bytes that are in the file. |
| Number of
Waveforms | A 32-bit integer that is the number of waveforms that are stored in the file. |
| Header Size | A 32-bit integer that is the number of bytes in the header. |
|---|---|
| Waveform Type | A 32-bit integer that is the type of waveform stored in the file:
• 0 = Unknown.
• 1 = Normal.
• 2 = Peak Detect.
• 3 = Average.
• 4 = Not used in InfiniiVision oscilloscopes.
• 5 = Not used in InfiniiVision oscilloscopes.
• 6 = Logic. |
| Number of
Waveform
Buffers | A 32-bit integer that is the number of waveform buffers required to read the
data. |
| Points | A 32-bit integer that is the number of waveform points in the data. |
| Count | A 32-bit integer that is the number of hits at each time bucket in the waveform
record when the waveform was created using an acquisition mode like
averaging. For example, when averaging, a count of four would mean every
waveform data point in the waveform record has been averaged at least four
times. The default value is 0. |
| X Display Range | A 32-bit float that is the X-axis duration of the waveform that is displayed. For
time domain waveforms, it is the duration of time across the display. If the value
is zero then no data has been acquired. |
| X Display Origin | A 64-bit double that is the X-axis value at the left edge of the display. For time
domain waveforms, it is the time at the start of the display. This value is treated
as a double precision 64-bit floating point number. If the value is zero then no
data has been acquired. |

---
**[Page 411]**

25 Reference
412 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
X Increment A 64-bit double that is the duration between data points on the X axis. For time
domain waveforms, this is the time between points. If the value is zero then no
data has been acquired.
X Origin A 64-bit double that is the X-axis value of the first data point in the data record.
For time domain waveforms, it is the time of the first point. This value is treated
as a double precision 64-bit floating point number. If the value is zero then no
data has been acquired.
X Units A 32-bit integer that identifies the unit of measure for X values in the acquired
data:
• 0 = Unknown.
• 1 = Volts.
• 2 = Seconds.
• 3 = Constant.
• 4 = Amps.
• 5 = dB.
• 6 = Hz.
Y Units A 32-bit integer that identifies the unit of measure for Y values in the acquired
data. The possible values are listed above under X Units.
Date A 16-byte character array, left blank in InfiniiVision oscilloscopes.
Time A 16-byte character array, left blank in the InfiniiVision oscilloscopes.
Frame A 24 byte character array that is the model number and serial number of the
oscilloscope in the format of: MODEL#:SERIAL#.
Waveform Label A 16 byte character array that contains the label assigned to the waveform.
Time Tags A 64-bit double, only used when saving multiple segments (requires segmented
memory option). This is the time (in seconds) since the first trigger.
Segment Index A 32-bit unsigned integer. This is the segment number. Only used when saving
multiple segments.
Waveform Data A waveform may have more than one data set. Each waveform data set will have a
Header waveform data header. The waveform data header consists of information about
the waveform data set. This header is stored immediately before the data set.
Waveform Data A 32-bit integer that is the size of the waveform data header.
Header Size
| X Increment | A 64-bit double that is the duration between data points on the X axis. For time
domain waveforms, this is the time between points. If the value is zero then no
data has been acquired. |
|---|---|
| X Origin | A 64-bit double that is the X-axis value of the first data point in the data record.
For time domain waveforms, it is the time of the first point. This value is treated
as a double precision 64-bit floating point number. If the value is zero then no
data has been acquired. |
| X Units | A 32-bit integer that identifies the unit of measure for X values in the acquired
data:
• 0 = Unknown.
• 1 = Volts.
• 2 = Seconds.
• 3 = Constant.
• 4 = Amps.
• 5 = dB.
• 6 = Hz. |
| Y Units | A 32-bit integer that identifies the unit of measure for Y values in the acquired
data. The possible values are listed above under X Units. |
| Date | A 16-byte character array, left blank in InfiniiVision oscilloscopes. |
| Time | A 16-byte character array, left blank in the InfiniiVision oscilloscopes. |
| Frame | A 24 byte character array that is the model number and serial number of the
oscilloscope in the format of: MODEL#:SERIAL#. |
| Waveform Label | A 16 byte character array that contains the label assigned to the waveform. |
| Time Tags | A 64-bit double, only used when saving multiple segments (requires segmented
memory option). This is the time (in seconds) since the first trigger. |
| Segment Index | A 32-bit unsigned integer. This is the segment number. Only used when saving
multiple segments. |
| Waveform Data
Header Size | A 32-bit integer that is the size of the waveform data header. |
|---|---|

---
**[Page 412]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 413
Buffer Type A 16-bit short that is the type of waveform data stored in the file:
• 0 = Unknown data.
• 1 = Normal 32-bit float data.
• 2 = Maximum float data.
• 3 = Minimum float data.
• 4 = Not used in InfiniiVision oscilloscopes.
• 5 = Not used in InfiniiVision oscilloscopes.
• 6 = Digital unsigned 8-bit char data (for digital channels).
Bytes Per Point A 16-bit short that is the number of bytes per data point.
Buffer Size A 32-bit integer that is the size of the buffer required to hold the data points.
Example Program for Reading Binary Data
To find an example program for reading binary data, direct your web browser to
www.keysight.com/find/6000X-Series-examples, and select "Example Program
for Reading Binary Data".
Examples of Binary Files
Single Acquisition The following picture shows a binary file of a single acquisition with multiple
Multiple Analog analog channels.
Channels
| Buffer Type | A 16-bit short that is the type of waveform data stored in the file:
• 0 = Unknown data.
• 1 = Normal 32-bit float data.
• 2 = Maximum float data.
• 3 = Minimum float data.
• 4 = Not used in InfiniiVision oscilloscopes.
• 5 = Not used in InfiniiVision oscilloscopes.
• 6 = Digital unsigned 8-bit char data (for digital channels). |
|---|---|
| Bytes Per Point | A 16-bit short that is the number of bytes per data point. |
| Buffer Size | A 32-bit integer that is the size of the buffer required to hold the data points. |

---
**[Page 413]**

25 Reference
414 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
File Header
Number of Waveforms = N
12 bytes
Waveform Header 1 Number of Waveform Buffers = 1
140 bytes
Waveform Data
Buffer Type = 1 (floating point)
Header 1
Bytes per Point = 4
12 bytes
Voltage Data 1
buffer size
Waveform Header 2 Number of Waveform Buffers = 1
140 bytes
Waveform Data
Buffer Type = 1 (floating point)
Header 2
Bytes per Point = 4
12 bytes
Voltage Data 2
buffer size
Waveform Header N Number of Waveform Buffers = 1
140 bytes
Waveform Data
Buffer Type = 1 (floating point)
Header N
Bytes per Point = 4
12 bytes
Voltage Data N
buffer size
Single Acquisition The following picture shows a binary file of a single acquisition with all pods for the
All Pods Logic logic channels saved.
Channels
| Voltage Data N
buffer size |
|---|
|  |

---
**[Page 414]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 415
File Header
Number of Waveforms = 2
12 bytes
Waveform Header 1 Number of Waveform Buffers = 1
140 bytes
Waveform Data
Buffer Type = 6 (unsigned char)
Header 1
Bytes per Point = 1
12 bytes
Pod 1 Timing Data
buffer size
Waveform Header 2 Number of Waveform Buffers = 1
140 bytes
Waveform Data
Buffer Type = 6 (unsigned char)
Header 2
Bytes per Point = 1
12 bytes
Pod 2 Timing Data
buffer size
Segmented The following picture shows a binary file of a segmented memory acquisition on
Memory one analog channel.
Acquisition on One
Analog Channel
| Pod 2 Timing Data
buffer size |
|---|
|  |

---
**[Page 415]**

25 Reference
416 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
File Header
Number of Waveforms = N = Number of Segments
12 bytes
Number of Waveform Buffers = 1
Waveform Header 1
Index = 1
140 bytes
Time Tag = 0.0
Waveform Data
Buffer Type = 1 (floating point)
Header 1
Bytes per Point = 4
12 bytes
Voltage Data 1
buffer size
Number of Waveform Buffers = 1
Waveform Header 2
Index = 2
140 bytes
Time Tag = time between segment 1 and 2
Waveform Data
Buffer Type = 1 (floating point)
Header 2
Bytes per Point = 4
12 bytes
Voltage Data 2
buffer size
Number of Waveform Buffers = 1
Waveform Header N
Index = N
140 bytes
Time Tag = time between segment 1 and N
Waveform Data
Buffer Type = 1 (floating point)
Header N
Bytes per Point = 4
12 bytes
Voltage Data N
buffer size
CSV and ASCII XY files
• “CSV and ASCII XY file structure"on page417
• “Minimum and Maximum Values in CSV Files"on page417
| Voltage Data N
buffer size |
|---|
|  |

---
**[Page 416]**

Reference 25
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 417
CSV and ASCII XY file structure
In CSV or ASCII XY format the Length control selects the number of points per
segment. All segments are contained in the CSV file or in each ASCII XY data file.
For example: If the Length control is set to 1000 points, there will be 1000 points
(rows in the spreadsheet) per segment. When saving all segments there are three
header rows, so the data for the first segment starts at row 4. The second
segment's data starts at row 1004. The time column shows the time since the
trigger on the first segment. The top row shows the selected number of points per
segment.
BIN files are a more efficient data transfer format than CSV or ASCIIXY. Use this
file format for fastest data transfer.
Minimum and Maximum Values in CSV Files
If you are running a Minimum or Maximum measurement, the minimum and
maximum values shown in the measurement display may not appear in the CSV
file.
Explanation: When the oscilloscope's sample rate is 4GSa/s, a sample will be taken every
250ps. If the horizontal scale is set to 10us/div, there will be 100us of data
displayed (because there are ten divisions across the screen). To find the total
number of samples the oscilloscope will take:
100us x 4GSa/s = 400Ksamples
The oscilloscope is required to display those 400K samples using 640 pixel
columns. The oscilloscope will decimate the 400K samples to 640 pixel columns,
and this decimation keeps track of the min and max values of all the points that
are represented by any given column. Those min and max values will be displayed
in that screen column.
A similar process is used to reduce the acquired data to produce a record usable
for various analysis needs such as measurements and CSV data. This analysis
record (or measurement record) is much larger than 640 and may in fact contain
up to 65536 points. Still, once the # of acquired points > 65536, some form of
decimation is required. The decimator used to produce a CSV record is configured
to provide a best-estimate of all the samples that each point in the record
represents. Therefore, the min and max values may not appear in the CSV file.

---
**[Page 417]**

25 Reference
418 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Acknowledgements
RealVNC RealVNC is licensed under the GNU General Public License. Copyright (C)
2002-2005 RealVNC Ltd. All Rights Reserved.
This is free software; you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.
This software is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.
This license is located on the Keysight InfiniiVision Oscilloscopes Documentation
CD-ROM.
RealVNC source code can be obtained from RealVNC or by contacting Keysight.
Keysight will charge for the cost of physically performing the source distribution.
HDF5 Reference Waveform data and Multi Channel Waveform data files use HDF5.
HDF5 was developed by The HDF Group and by the National Center for
Supercomputing Applications at the University of Illinois at Urbana-Champaign.
CUPS Network printing uses the CUPS (Common Unix Printing System) library.
The CUPS and CUPS Imaging libraries are developed by Apple Inc. and licensed
under the GNU Library General Public License ("LGPL"), Version 2.
This license is located on the Keysight InfiniiVision Oscilloscopes Documentation
CD-ROM.
mDNSResponder CUPS network printing uses the mDNSResponder library.
The mDNSResponder library is developed by Apple Inc. and licensed under the
Apache License, Version 2.0.
This license is located on the Keysight InfiniiVision Oscilloscopes Documentation
CD-ROM.

---
**[Page 418]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
419
26 CAN/LIN Triggering and
Serial Decode
Setup for CAN/CAN FD Signals / 419
Loading and Displaying CAN Symbolic Data / 422
CAN/CAN FD Triggering / 423
CAN/CAN FD Serial Decode / 426
Setup for LIN Signals / 432
Loading and Displaying LIN Symbolic Data / 433
LIN Triggering / 434
LIN Serial Decode / 436
CAN/LIN triggering and serial decode requires Option AUTO or the DSOX6AUTO
upgrade.
Setup for CAN/CAN FD Signals
Setup consists of connecting the oscilloscope to a CAN signal, using the Signals
Menu to specify the signal source, threshold voltage level, baud rate, and sample
point.
Connect the oscilloscope to a CAN signal that has a dominant-low polarity. If you
are connecting to the CAN signal using a differential probe, connect the probe's
positive lead to the dominant-low CAN signal and connect the negative lead to
the dominant-high CAN signal.
To set up the oscilloscope to capture CAN signals:
1 Press [Serial].

---
**[Page 419]**

26 CAN/LIN Triggering and Serial Decode
420 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 Press the Serial softkey, turn the Entry knob to select Serial1 or Serial2, and
press the softkey again to enable decode.
3 Press the Mode softkey; then, select CAN trigger type.
4 Press the Signals softkey to open the CAN Signals Menu.
5 Press Source; then, select the channel for the CAN signal.
The label for the CAN source channel is automatically set.
6 Press the Threshold softkey; then, turn the Entry knob to select the CAN signal
threshold voltage level.
The threshold voltage level is used in decoding, and it will become the trigger
level when the trigger type is set to the selected serial decode slot.
7 Press the Std. Rate Settings softkey to open the CAN Standard Rate Settings
Menu.
a Press the Baud softkey; then, turn the Entry knob to select the baud rate that
matches match your CAN bus signal.
The CAN baud rate can be set to predefined baud rates from 10kb/s up to
5Mb/s or a user-defined baud rate from 10.0kb/s to 4Mb/s in increments
of 100b/s. Fractional user-defined baud rates between 4Mb/s and 5Mb/s
are not allowed.
The default baud rate is 125kb/s
If none of the pre-defined selections match your CAN bus signal, select User
Defined; then, press the User Baud softkey and turn the Entry knob to enter
the baud rate.
b Press the Sample Point softkey; then, turn the Entry knob to select the point
between phase segments 1 and 2 where the state of the bus is measured.
This controls the point within the bit's time where the bit value is captured.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 420]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 421
One Bit
60%
70%
Sample Point
80%
c Press the Back Back/Up key to return to the CAN Signals Menu.
8 When decoding CAN FD, press the FD Rate Settings softkey to open the CAN FD
Rate Settings Menu.
For standard CAN, only the Standard Rate Settings must be set correctly. For CAN FD, both
NOTE
the Standard Rate Settings and the FD Rate Settings must be set correctly.
a Press the Baud softkey; then, turn the Entry knob to match the CAN FD baud
rate of the signal from your device under test.
If the desired baud rate is not shown in the list, select User Defined and use
the User Baud softkey to set the baud rate.
The CAN FD baud rate can be set to predefined baud rates from 1-10Mb/s
or a user-defined baud rate from 10.0kb/s to 10Mb/s in increments of
100b/s.
If the baud rate you select does not match the CAN FD baud rate, false
triggers and decoding may occur.
b Press the Sample Point softkey; then, turn the Entry knob to select the sample
point.
The sample point is the point during the bit time where the bit level is
sampled to determine whether it is dominant or recessive. The sample point
represents the percentage of time between the beginning of the bit time to
the end of the bit time.
| One Bit
60%
70%
Sample Point
80% | One Bit
60%
70%
Sample Point
80% |
|---|---|
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 421]**

26 CAN/LIN Triggering and Serial Decode
422 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
You may need to adjust the sample point to get a reliable trigger and
decode, depending on your CAN FD network topology and where the
oscilloscope probe is located in the network.
c Press the Standard softkey to select the standard that will be used when
decoding or triggering on FD frames, ISO, or non-ISO.
This setting has no effect on the processing of non-FD (classical) frames.
d Press the Back Back/Up key to return to the CAN Signals Menu.
9 Press the Signal softkey and select the type and polarity of the CAN signal. This
also automatically sets the channel label for the source channel.
• CAN_H — The actual CAN_H differential bus.
• Differential (H-L) — The CAN differential bus signals connected to an analog
source channel using a differential probe. Connect the probe's positive lead
to the dominant-high CAN signal (CAN_H) and connect the negative lead to
the dominant-low CAN signal (CAN_L).
Dominant low signals:
• Rx — The Receive signal from the CAN bus transceiver.
• Tx — The Transmit signal from the CAN bus transceiver.
• CAN_L — The actual CAN_L differential bus signal.
• Differential (L-H) — The CAN differential bus signals connected to an analog
source channel using a differential probe. Connect the probe's positive lead
to the dominant-low CAN signal (CAN_L) and connect the negative lead to
the dominant-high CAN signal (CAN_H).
Loading and Displaying CAN Symbolic Data
When you load (recall) a CAN DBC communication database (*.dbc) file into the
oscilloscope, its symbolic information can be:
• Displayed in the decode waveform and Lister window.
• Used when setting up CAN triggering.
• Used when searching for CAN data in the decode.
To recall a DBC file into the oscilloscope:
1 Press [Save/Recall] > Recall > Recall > CAN Symbolic data (*.dbc).

---
**[Page 422]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 423
2 Press Press to go and navigate to the DBC file on a USB storage device.
3 Press Load to: and select which serial decode (S1 or S2) the symbolic information
will be used with.
4 Press Press to Recall.
The DBC file remains in the oscilloscope until it is overwritten or a secure erase is
performed.
To display CAN symbolic data:
1 Press [Serial].
2 Press the Display softkey and select Symbolic (instead of Hexadecimal).
Your choice affects both the decode waveform and the Lister window.
For CAN FD frames, symbolic decoding is limited to the first eight bytes.
NOTE
CAN/CAN FD Triggering
To set up the oscilloscope to capture a CAN signal, see “Setup for CAN/CAN FD
Signals"on page419.
The Controller Area Network (CAN) trigger allows triggering on CAN version 2.0A,
2.0B, and CAN FD (Flexible Data-rate) signals.
A CAN message frame in CAN_L signal type is shown below:
Bus Arbitration Control Data CRC ACK
EOF Intermission
Idle Field Field Field Field Field
SOF edge
After setting up the oscilloscope to capture a CAN signal:
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger Type softkey; then, turn the Entry knob to
select Serial1 or Serial2 on which the CAN signal is being decoded.
| NOTE |
|---|
|  |
| Bus Arbitration Control Data CRC ACK
EOF Intermission
Idle Field Field Field Field Field
SOF edge |
|---|
|  |
|  | Arbitration
Field | Control
Field | Data
Field | CRC
Field | ACK
Field |
|---|---|---|---|---|---|

---
**[Page 423]**

26 CAN/LIN Triggering and Serial Decode
424 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Press the Trigger on: softkey; then, turn the Entry knob to select the trigger
condition:
• SOF - Start of Frame — triggers at the start bit for both data and overload
frames.
• EOF - End of Frame — triggers at the end of any frame. *
• Frame ID — triggers on any standard CAN (data or remote) or CAN FD frame
at the end of the 11- or 29-bit ID field.
• Data Frame ID (non-FD) — triggers on standard CAN data frames at the end of
the 11- or 29-bit ID field.
• Data Frame ID and Data (non-FD) — triggers on any standard CAN data frame at
the end of the last data byte defined in the trigger. The DLC of the packet
must must match the number of bytes specified.
• Data Frame ID and Data (FD) — triggers on CAN FD frames at the end of the last
data byte defined in the trigger. You can trigger on up to 8 bytes of data
anywhere within the CAN FD data, which can be up to 64 bytes long.
• Remote Frame ID — triggers on standard CAN remote frames at the end of the
11- or 29-bit ID field.
• Error Frame — triggers after 6 consecutive 0s while in a data frame, at the
EOF. *
• Acknowledge Error — triggers on the acknowledge bit if the polarity is
incorrect. *
• Form Error — triggers on reserved bit errors. *
• Stuff Error — triggers on 6 consecutive 1s or 6 consecutive 0s, while in a
non-error or non overload frame. *
• CRC Field Error — triggers when the calculated CRC does not match the
transmitted CRC. In addition, for FD frames, will also trigger if the Stuff
Count is in error. *
• Spec Error (Ack or Form or Stuff or CRC) — triggers on Ack, Form, Stuff, or CRC
errors. *
• All Errors — triggers on all Spec errors and error frames. *
• BRS Bit (FD) — triggers on the BRS bit of CAN FD frames. *
• CRC Delimiter Bit (FD) — triggers on the CRC delimiter bit in CAN FD frames. *
|  |  |
|---|---|

---
**[Page 424]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 425
• ESI Bit Active (FD) — triggers on the ESI bit if set active. *
• ESI Bit Passive (FD) — triggers on the ESI bit if set passive. *
• Overload Frame — triggers on an overload frame.
* You can optionally qualify the trigger for frames whose ID you specify.
When CAN symbolic data is loaded into the oscilloscope (see “Loading and
Displaying CAN Symbolic Data"on page422), you can trigger on:
• Message — a symbolic message.
• Message and Signal (non-FD) — a symbolic message and a signal value.
• Message and Signal (FD, first 8 bytes only) — a symbolic message and a signal
value, limited to the first 8 bytes of FD data.
Symbolic messages, signals, and values are defined in the DBC communication
database file.
A message is the symbolic name for a CAN frame ID, a signal is the symbolic
name for a bit or set of bits within the CAN data, and a value can be a symbolic
representation of the signal bit values or it can be a decimal number with units.
4 If you select a condition that lets you qualify by ID or trigger on ID or data
values, use the Filter by ID softkey, or the Bits softkey and the CAN Bits Menu,
and the remaining softkeys to specify those values.
For details about using the remaining softkeys to enter values, press and hold
the softkey in question to display the built-in help.
You can use the Zoom mode for easier navigation of the decoded data.
If the setup does not produce a stable trigger, the CAN signal may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
To display CAN serial decode, see “CAN/CAN FD Serial Decode"on page426.
NOTE
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |

---
**[Page 425]**

26 CAN/LIN Triggering and Serial Decode
426 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
CAN/CAN FD Serial Decode
To set up the oscilloscope to capture CAN signals, see “Setup for CAN/CAN FD
Signals"on page419.
For CAN triggering set up see “CAN/CAN FD Triggering"on page423.
NOTE
To set up CAN serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
3 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
If the setup does not produce a stable trigger, the CAN signal may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the decoded data.
See Also • “Interpreting CAN/CAN FD Decode"on page427
• “CAN Totalizer"on page428
• “Interpreting CAN Lister Data"on page430
• “Searching for CAN Data in the Lister"on page431
| NOTE |
|---|
|  |
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 426]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 427
Interpreting CAN/CAN FD Decode
The CAN decode display is color coded as follows:
• Blue angled waveforms show an active bus (inside a packet/frame).
• Blue mid-level lines show an idle bus.
• Frame ID — yellow.
• Data bytes — white hex digits.
• CAN frame type and Data Length Code (DLC) — blue for data frames, green for
remote frames. The DLC is always a decimal value. CAN frame types can be:
• FD — a CAN FD frame whose bit rate does not switch during the data phase.
• BRS — a CAN FD frame whose bit rate switches during the data phase.
• RMT — a standard CAN remote frame.
• Data — a standard CAN data frame.
|  |
|---|
|  |

---
**[Page 427]**

26 CAN/LIN Triggering and Serial Decode
428 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The status of the Error State Indicator (ESI) flag is shown in the "Type" column
of the Lister. If the ESI bit is recessive, indicating error passive, the background
of the "Type" column will be yellow. If the ESI bit indicates error active, the
"Type" column's background will be unshaded.
The DLC field will always be displayed in decimal, and will indicate the number
of bytes in the frame. So for example, for an FD frame that has the DLC code
0xF, which represents a packet with 64 bytes, "DLC=64" will be displayed on
the decode line, and "64" will be displayed in the DLC column of the Lister.
• Overload frame — blue with the text "OVRLD". An overload condition may occur
before an end of frame condition. If so, the frame is closed and opened with
blue brackets at the start of the overload condition.
• Stuff Count — green hex digit when valid, red when error detected. The hex digit
shows the gray-coded with parity bit stuff count.
• CRC — blue hex digits when valid, red when error detected.
• Red angled waveforms — Unknown or error condition.
• Flagged error frames — red with "ERR FRAME", "STUFF ERR", "FORM ERR",
"ACK ERR", "GLITCH ERR", or "?" (unknown).
• Pink vertical bars — Expand horizontal scale (and run again) to see decode.
• Red Dot — More information is available. Decoded text is truncated to fit.
Expand the horizontal scale to view the information.
CAN Totalizer
The CAN totalizer provides a direct measure of bus quality and efficiency. The CAN
totalizer measures total CAN frames, Specification error counter, flagged error
frames, and bus utilization.
The totalizer is always running (counting frames and calculating percentages) and
is displayed whenever CAN decode is displayed. The totalizer counts even when
the oscilloscope is stopped (not acquiring data). Pressing the [Run/Stop] key does
not affect the totalizer. When an overflow condition occurs, the counter displays
OVERFLOW. The counters can be reset to zero by pressing the Reset CAN Counters
softkey.
|  |
|---|
|  |

---
**[Page 428]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 429
Types of Frames • Active error frames are CAN frames in which a CAN node recognizes an error
condition during a data or remote frame and issues an active error flag.
• A partial frameoccurs when the oscilloscope detects any error condition during
a frame that is not followed by an active error flag. Partial frames are not
counted.
Counters • The FRAMES counter gives the total number of completed remote, data,
overload, and active error frames.
• The SPEC counter gives the total number of Specification errors. This counter
tracks the number of Acknowledge, Form, Stuff, and CRC errors. If a packet has
more than one type of error, that packet will increment the counter by the total
number of errors in the packet.
• The ERRFR counter gives the total number of completed active error frames
and their percentage of the total number of frames.
• The LOAD (bus load) indicator measures the percentage of time the bus is
active. The calculation is done on 330ms periods, approximately every 400ms.
Example: If a data frame contains an active error flag, both the FRAMES counter
and the ERRFR counter will be incremented. If a data frame contains an error that
is not an active error it is considered a partial frame and no counters are
incremented.

---
**[Page 429]**

26 CAN/LIN Triggering and Serial Decode
430 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Interpreting CAN Lister Data
In addition to the standard Time column, the CAN Lister contains these columns:
• ID — frame ID. Can be displayed as hex digits or symbolic information (see
“Loading and Displaying CAN Symbolic Data"on page422).
• Type — frame type (RMT remote frame or Data).
• DLC — data length code.
• Data — data bytes. Can be displayed as hex digits or symbolic information.
• CRC — cyclic redundancy check.
• Errors — highlighted in red. Errors can be Acknowledge (Ack, A), Form (Fo), or
Frame (Fr). Different kinds of errors can be combined like "Fo,Fr" in the above
example.
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
|  |
|---|
|  |

---
**[Page 430]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 431
Searching for CAN Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
CAN data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With CAN selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
Serial1 or Serial2 on which the CAN signal is being decoded.
3 Press Search for; then, select from these options:
• Frame ID — Finds remote or data frames matching the specified ID.
• Data Frame ID — Finds data frames matching the specified ID.
• Data Frame ID and Data — Finds data frames matching the specified ID and
data.
• Remote Frame ID — Finds remote frames with the specified ID.
• Error Frame — Finds CAN active error frames.
• Acknowledge Error — Finds the acknowledge bit if the polarity is incorrect.
• Form Error — Finds reserved bit errors.
• Stuff Error — Finds 6 consecutive 1s or 6 consecutive 0s, while in a non-error
or non overload frame.
• CRC Field Error — Finds when the calculated CRC does not match the
transmitted CRC.
• All Errors — Finds any form error or active error.
• Overload Frame — Finds CAN overload frames.
When CAN symbolic data is loaded into the oscilloscope (see “Loading and
Displaying CAN Symbolic Data"on page422), you can search for:
• Message — a symbolic message.
• Message and Signal — a symbolic message and a signal value.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 431]**

26 CAN/LIN Triggering and Serial Decode
432 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Setup for LIN Signals
LIN (Local Interconnect Network) signal setup consists of connecting the
oscilloscope to a serial LIN signal, specifying the signal source, threshold voltage
level, baud rate, sample point, and other LIN signal parameters.
To set up the oscilloscope to capture LIN signals:
1 Press [Serial].
2 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
3 Press the Mode softkey; then, select LIN trigger type.
4 Press the Signals softkey to open the LIN Signals Menu.
5 Press the Source softkey to select the channel connected to the LIN signal line.
The label for the LIN source channel is automatically set.
6 Press the Threshold softkey; then, turn the Entry knob to set the LIN signal
threshold voltage level to the middle of the LIN signal.
The threshold voltage level is used in decoding, and it will become the trigger
level when the trigger type is set to the selected serial decode slot.
7 Press the Baud Rate softkey to open the LIN Baud Rate Menu.
8 Press the Baud softkey; then, turn the Entry knob to select the baud rate that
matches match your LIN bus signal.
The default baud rate is 19.2kb/s.
If none of the pre-defined selections match your LIN bus signal, select User
Defined; then, press the User Baud softkey and turn the Entry knob to enter the
baud rate.
You can set the LIN baud rate from 2.4kb/s to 625kb/s in increments of
100b/s.
9 Press the Back Back/Up key to return to the LIN Signals Menu.
|  |  |
|---|---|

---
**[Page 432]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 433
10Press the Sample Point softkey; then, turn the Entry knob to select the sample
point at which the oscilloscope will sample the bit value.
One Bit
60%
70%
Sample Point
80%
11Press the Standard softkey; then, turn the Entry knob to select the LIN standard
you are measuring (LIN 1.3 or LIN 2.X).
For LIN 1.2 signals, use the LIN 1.3 setting. The LIN 1.3 setting assumes the
signal follows the "Table of Valid ID Values" as shown in section A.2 of the LIN
Specification dated December 12, 2002. If your signal does not comply with the
table, use the LIN 2.X setting.
12Press the Sync Break softkey and select the minimum number of clocks that
define a sync break in your LIN signal.
Loading and Displaying LIN Symbolic Data
When you load (recall) a LIN description file (*.ldf) into the oscilloscope, its
symbolic information can be:
• Displayed in the decode waveform and Lister window.
• Used when setting up LIN triggering.
• Used when searching for LIN data in the decode.
To recall a LIN description file into the oscilloscope:
1 Press [Save/Recall] > Recall > Recall > LIN Symbolic data (*.ldf).
2 Press Press to go and navigate to the LIN description file on a USB storage
device.
3 Press Load to: and select which serial decode (S1 or S2) the symbolic information
will be used with.
4 Press Press to Recall.
The LIN description file remains in the oscilloscope until it is overwritten or a
secure erase is performed.
| One Bit
60%
70%
Sample Point
80% | One Bit
60%
70%
Sample Point
80% |
|---|---|

---
**[Page 433]**

26 CAN/LIN Triggering and Serial Decode
434 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To display LIN symbolic data:
1 Press [Serial].
2 Press the Display softkey and select Symbolic (instead of Hexadecimal).
Your choice affects both the decode waveform and the Lister window.
LIN Triggering
To set up the oscilloscope to capture a LIN signal, see “Setup for LIN Signals"on
page432.
LIN triggering can trigger on the rising edge at the Sync Break exit of the LIN
single-wire bus signal (that marks the beginning of the message frame), the
FrameID, or the FrameID and Data.
A LIN signal message frame is shown below:
Sync Sync Identifier Data Checksum
Break Field Break Fields Field
Sync Break Exit
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger Type softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the CAN signal is being
decoded.
3 Press the Trigger on: softkey; then, turn the Entry knob to select the trigger
condition:
• Sync (Sync Break) — The oscilloscope triggers on the rising edge at the Sync
Break exit of the LIN single-wire bus signal that marks the beginning the
message frame.
| Sync Sync Identifier Data Checksum
Break Field Break Fields Field
Sync Break Exit |
|---|
|  |
| Sync
Break | Sync
Field | Identifier
Break | Data
Fields | Checksum
Field |
|---|---|---|---|---|
|  |  |
|---|---|

---
**[Page 434]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 435
• ID (FrameID) — The oscilloscope triggers when a frame with an ID equal to
the selected value is detected. Use the Entry knob to select the value for the
FrameID.
• ID&Data (FrameID and Data) — The oscilloscope triggers when a frame with
an ID and data equal to the selected values is detected. When triggering on
a frame ID and data:
• To select the frame ID value, press the FrameID softkey, and use the Entry
knob.
Note that you can enter a "don't care" value for the frameID and trigger
on data values only.
• To set up the number of data bytes and enter their values (in hexadecimal
or binary), use the remaining softkeys.
• Parity Error — The oscilloscope triggers on parity errors.
• Checksum Error — The oscilloscope triggers on checksum errors.
When a LIN description file (*.ldf) is loaded (recalled) into the oscilloscope (see
“Loading and Displaying LIN Symbolic Data"on page433), you can trigger on:
• Frame (Symbolic) — a symbolic frame value.
• Frame and Signal — a symbolic frame value and a signal value.
Symbolic frames, signals, and values are defined in the LIN description file.
A frame is the symbolic name for a LIN frame ID, a signal is the symbolic name
for a bit or set of bits within the LIN data, and a value can be a symbolic
representation of the signal bit values or it can be a decimal number with units.

---
**[Page 435]**

26 CAN/LIN Triggering and Serial Decode
436 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
For details about using the LIN Bits Menu softkeys, press and hold the softkey in question to
NOTE
display the built-in help.
For LIN decode information see “LIN Serial Decode"on page436.
NOTE
LIN Serial Decode
To set up the oscilloscope to capture LIN signals, see “Setup for LIN Signals"on
page432.
|  |  |
|---|---|
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |

---
**[Page 436]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 437
For LIN triggering setup see “LIN Triggering"on page434.
NOTE
To set up LIN serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 Choose whether to include the parity bits in the identifier field.
a If you want to mask the upper two parity bits, ensure that the box under the
Show Parity softkey is not selected.
b If you want to include the parity bits in the identifier field, ensure that the box
under the Show Parity softkey is selected.
3 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
4 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
If the setup does not produce a stable trigger, the LIN signal may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the decoded data.
See Also • “Interpreting LIN Decode"on page438
• “Interpreting LIN Lister Data"on page439
• “Searching for LIN Data in the Lister"on page440
| NOTE |
|---|
|  |
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 437]**

26 CAN/LIN Triggering and Serial Decode
438 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Interpreting LIN Decode
• Angled waveforms show an active bus (inside a packet/frame).
• Mid-level blue lines show an idle bus.
• The hexadecimal ID and parity bits (if enabled) appear in yellow. If a parity error
is detected the hexadecimal ID and parity bits (if enabled) appear in red.
• Decoded hexadecimal data values appear in white.
• The checksum appears in blue if correct, or red if incorrect.
• Decoded text is truncated at the end of the associated frame when there is
insufficient space within frame boundaries.
• Pink vertical bars indicate you need to expand the horizontal scale (and run
again) to see decode.
• Red dots in the decode line indicate that there is data that is not being
displayed. Scroll or expand the horizontal scale to view the information.
• Unknown bus values (undefined or error conditions) are drawn in red.
|  |
|---|
|  |

---
**[Page 438]**

CAN/LIN Triggering and Serial Decode 26
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 439
• If there is an error in the synch field, SYNC will appear in red.
• If the header exceeds the length specified in the standard, THM will appear red.
• If the total frame count exceeds the length specified in the standard, TFM will
appear red (LIN 1.3 only).
• For LIN 1.3 a wakeup signal is indicated by WAKE in blue. If the wakeup signal
is not followed by a valid wakeup delimiter a wakeup error is detected and
displayed as WUP in red.
Interpreting LIN Lister Data
In addition to the standard Time column, the LIN Lister contains these columns:
• ID — frame ID. Can be displayed as hex digits or symbolic information (see
“Loading and Displaying LIN Symbolic Data"on page433).
• Data — data bytes. Can be displayed as hex digits or symbolic information.
• Checksum.
• Errors — highlighted in red.
|  |
|---|
|  |

---
**[Page 439]**

26 CAN/LIN Triggering and Serial Decode
440 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
Searching for LIN Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
LIN data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With LIN selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the LIN signal is being decoded.
3 Press Search; then, select from these options:
• ID — Finds frames with the specified ID. Press the Frame ID softkey to select
the ID.
• ID & Data — Finds frames with the specified ID and data. Press the Frame ID
softkey to select the ID. Press the Bits softkey to enter the data value.
• Errors — Finds all errors.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 440]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
441
27 FlexRay Triggering and
Serial Decode
Setup for FlexRay Signals / 441
FlexRay Triggering / 442
FlexRay Serial Decode / 445
FlexRay triggering and serial decode requires Option FLEX or the DSOX6FLEX
upgrade.
Setup for FlexRay Signals
FlexRay signal setup consists of first connecting the oscilloscope to a differential
FlexRay signal using a differential active probe (the Keysight N2792A is
recommended), specifying the signal source, threshold voltage trigger level, baud
rate, and bus type.
To set up the oscilloscope to capture FlexRay signals:
1 Press [Label] to turn on labels.
2 Press [Serial].
3 Press the Serial softkey, turn the Entry knob to select the desired serial bus
(Serial1 or Serial2), and press the softkey again to enable decode.
4 Press the Mode softkey; then, select FlexRay mode.
5 Press the Signals softkey to open the FlexRay Signals Menu.

---
**[Page 441]**

27 FlexRay Triggering and Serial Decode
442 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
6 Press Source and select the analog channel that is probing the FlexRay signal.
7 Press Threshold; then, turn the Entry knob to set the threshold voltage level.
The threshold level should be set below the idle level.
The threshold voltage level is used in decoding and will become the trigger
level when the trigger type is set to the selected serial decode bus.
8 Press Baud and select the baud rate of the FlexRay signal being probed.
9 Press Bus and select the bus type of the FlexRay signal being probed.
It is important to specify the correct bus because this setting affects CRC error
detection.
10Press Auto Setup to perform the following actions:
• Sets the selected source channel's impedance to 50Ohms, assuming a
differential active probe that requires a 50ohm termination is being used .
• Sets the selected source channel's probe attenuation to 10:1.
• Sets the trigger level (on the selected source channel) to -300mV.
• Turns on trigger Noise Reject.
• Turns on Serial Decode.
• Sets the trigger type to FlexRay.
FlexRay Triggering
To set up the oscilloscope to capture a FlexRay signal, see “Setup for FlexRay
Signals"on page441.
After you have set up the oscilloscope to capture a FlexRay signal, you can then
set up triggers on frames (see page443), errors (see page444), or events (see
page444).
To display FlexRay serial decode, see “FlexRay Serial Decode"on page445.
NOTE
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 442]**

FlexRay Triggering and Serial Decode 27
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 443
Triggering on FlexRay Frames
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial bus (Serial1 or Serial2) on which the FlexRay signals are being
decoded.
3 Press the Trigger softkey; then, turn the Entry knob to select Frame.
4 Press the Frames softkey to open the FlexRay Frame Trigger Menu.
5 Press the FrameID softkey, and use the Entry knob to select the frame ID value
from All or 1 to 2047.
6 Press the Frame Type softkey to select the frame type:
• All Frames
• Startup Frames
• NULL Frames
• Sync Frames
• Normal Frames
• NOT Startup Frames
• NOT NULL Frames
• NOT Sync Frames
7 Press the Cyc Ct Rep softkey, and use the Entry knob to select the cycle count
repetition factor (2, 4, 8, 16, 32, or 64, or All).
8 Press the Cyc Ct Bas softkey, and use the Entry knob to select the cycle count
base factor from 0 through the Cyc Ct Rep factor minus 1.
For example, with a base factor of 1 and a repetition factor of 16, the
oscilloscope triggers on cycles 1, 17, 33, 49, and 65.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 443]**

27 FlexRay Triggering and Serial Decode
444 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
To trigger on a particular cycle, set the Cycle Repetition factor to 64 and use
the cycle base factor to choose a cycle.
To trigger all (any) cycles, set the Cycle Repetition factor to All. The scope will
trigger on any and all cycles.
Because specific FlexRay frames may occur infrequently, it may be helpful to press the
NOTE
[Mode/Coupling] key, then press the Mode softkey to set the trigger mode from Auto to
Normal. This prevents the oscilloscope from Auto triggering while waiting for a particular
frame and cycle combination.
Triggering on FlexRay Errors
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial bus (Serial1 or Serial2) on which the FlexRay signals are being
decoded.
3 Press the Trigger softkey; then, turn the Entry knob to select Error.
4 Press the Errors softkey; then, select the error type:
• All Errors
• Header CRC Error — cyclic redundancy check error in the header.
• Frame CRC Error — cyclic redundancy check error in the frame.
Because FlexRay errors occur infrequently it may be helpful to set the oscilloscope to press
NOTE
the [Mode/Coupling] key, then press the Mode softkey to set the trigger mode from Auto to
Normal. This prevents the oscilloscope from Auto triggering while waiting for an error to
occur. You may need to adjust trigger holdoff to see a particular error when multiple errors
exist.
Triggering on FlexRay Events
1 Press [Trigger].
| NOTE |
|---|
|  |
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 444]**

FlexRay Triggering and Serial Decode 27
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 445
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial bus (Serial1 or Serial2) on which the FlexRay signals are being
decoded.
3 Press the Trigger softkey; then, turn the Entry knob to select Event.
4 Press the Event softkey; then, select the event type:
• Wake-up
• TSS — Transmission Start Sequence.
• BSS — ByteStart Sequence.
• FES/DTS — Frame End or Dynamic Trailing Sequence.
5 Press Auto Setup for Event.
This automatically configures oscilloscope settings (as shown on the display)
for the selected event trigger.
FlexRay Serial Decode
To set up the oscilloscope to capture FlexRay signals, see “Setup for FlexRay
Signals"on page441.
For FlexRay triggering setup see “FlexRay Triggering"on page442.
NOTE
To set up FlexRay serial decode:
1 Press [Serial] to display the Serial Decode Menu.
|  |  |
|---|---|
| NOTE |
|---|
|  |
|  |  |
|---|---|

---
**[Page 445]**

27 FlexRay Triggering and Serial Decode
446 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
3 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
You can use the horizontal Zoom window for easier navigation of the acquired data.
See Also • “Interpreting FlexRay Decode"on page446
• “FlexRay Totalizer"on page447
• “Interpreting FlexRay Lister Data"on page448
• “Searching for FlexRay Data in the Lister"on page449
Interpreting FlexRay Decode
• Frame type (NORM, SYNC, SUP, NULL in blue).
• Frame ID (decimal digits in yellow).
• Payload-length (decimal number of words in green).
|  |
|---|
|  |

---
**[Page 446]**

FlexRay Triggering and Serial Decode 27
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 447
• Header CRC (hex digits in blue plus red HCRC error message if invalid).
• Cycle number (decimal digits in yellow).
• Data bytes (HEX digits in white).
• Frame CRC (hex digits in blue plus red FCRC error message if invalid).
• Frame/coding errors (specific error symbol in red).
FlexRay Totalizer
The FlexRay totalizer consists of counters that provide a direct measure of bus
quality and efficiency. The totalizer appears on screen whenever FlexRay Decode
is ON in the Serial Decode Menu.
• The FRAMES counter gives a real-time count of all captured frames.
• The NULL counter gives the number and percentage of null frames.
• The SYNC counter gives the number and percentage of sync frames.
The totalizer runs, counting frames and calculating percentages, even when the
oscilloscope is stopped (not acquiring data).
When an overflow condition occurs, the counter displays OVERFLOW.
The counters can be reset to zero by pressing the Reset FlexRay Counters softkey.
|  |
|---|
|  |

---
**[Page 447]**

27 FlexRay Triggering and Serial Decode
448 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Interpreting FlexRay Lister Data
In addition to the standard Time column, the FlexRay Lister contains these
columns:
• FID — frame ID.
• Len — payload length.
• HCRC — header CRC.
• CYC — cycle number.
• Data.
• FCRC — frame CRC.
• Frames with errors are highlighted in red.
|  |
|---|
|  |

---
**[Page 448]**

FlexRay Triggering and Serial Decode 27
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 449
Searching for FlexRay Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
FlexRay data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With FlexRay selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial bus (Serial1 or Serial2) on which the FlexRay signals are being
decoded.
3 In the Search Menu, press Search for; then, select from these options:
• Frame ID — Finds frames with the specified ID. Press the Frame ID softkey to
select the ID.
• Cycle number (+ Frame ID) — Finds frames with the specified cycle number and
ID. Press the Frame ID softkey to select the ID. Press the Cycle # softkey to
select the number.
• Data (+ Frame ID + Cycle number) — Finds frames with the specified data, cycle
number, and frame ID. Press the Frame ID softkey to select the ID. Press the
Cycle # softkey to select the number. Press the Data softkey to open a menu
where you can enter the data value.
• Header CRC Error — Finds cyclic redundancy check errors in headers.
• Frame CRC Error — Finds cyclic redundancy check errors in frames.
• Errors — finds all errors.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 449]**

27 FlexRay Triggering and Serial Decode
450 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 450]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
451
28 I2C/SPI Triggering and
Serial Decode
Setup for I2C Signals / 451
I2C Triggering / 452
I2C Serial Decode / 456
Setup for SPI Signals / 460
SPI Triggering / 464
SPI Serial Decode / 466
I2C/SPI triggering and serial decode requires Option EMBD or the DSOX6EMBD
upgrade.
Only one SPI serial bus can be decoded at a time.
NOTE
Setup for I2C Signals
I2C (Inter-IC bus) signals setup consists of connecting the oscilloscope to the
serial data (SDA) line and the serial clock (SCL) line and then specifying the input
signal threshold voltage levels.
To set up the oscilloscope to capture I2C signals, use the Signals softkey which
appears in the Serial Decode Menu:
1 Press [Serial].
| NOTE |
|---|
|  |

---
**[Page 451]**

28 I2C/SPI Triggering and Serial Decode
452 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
3 Press the Mode softkey; then, select I2C trigger type.
4 Press the Signals softkey to open the I2C Signals Menu.
5 For both the SCL (serial clock) and SDA (serial data) signals:
a Connect an oscilloscope channel to the signal in the device under test.
b Press the SCL or SDA softkey; then, turn the Entry knob to select the channel
for the signal.
c Press the corresponding Threshold softkey; then, turn the Entry knob to select
the signal threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
Data must be stable during the whole high clock cycle or it will be
interpreted as a start or stop condition (data transitioning while the clock is
high).
The SCL and SDA labels for the source channels are automatically set.
I2C Triggering
To set up the oscilloscope to capture I2C signals, see “Setup for I2C Signals"on
page451.
After the oscilloscope has been set up to capture I2C signals, you can trigger on a
stop/start condition, a restart, a missing acknowledge, an EEPROM data read, or
on a read/write frame with a specific device address and data value.
1 Press [Trigger]; then, select the I2C trigger type.
2 Press [Trigger].
3 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the I2C signals are being
decoded.
|  |  |
|---|---|

---
**[Page 452]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 453
4 Press the Trigger: softkey; then, turn the Entry knob to select the trigger
condition:
• Start Condition— triggers when SDA data transitions from high to low while
the SCL clock is high. For triggering purposes (including frame triggers), a
restart is treated as a start condition.
• Stop Condition— triggers when data (SDA) transitions from low to high while
the clock (SCL) is high.
SDA
SCL
Start Address R/ Ack Data Ack Stop
Condition Condition
• Restart— triggers when another start condition occurs before a stop
condition.
• Address — triggers on the selected address. The R/W bit is ignored.
• Address with no Ack— The oscilloscope triggers when the acknowledge of the
selected address field is false. The R/W bit is ignored.
• Write Data with no Ack— triggers if a write data byte is not acknowledged.
Note that this trigger mode will not trigger if the ack following the R/W bit is
missing, but will only trigger on missing acks following data bytes.
• Missing Acknowledge— triggers when SDA data is high during any Ack SCL
clock bit.
• EEPROM Data Read— The trigger looks for EEPROM control byte value 1010xxx
on the SDA line, followed by a Read bit and an Ack bit. It then looks for the
data value and qualifier set by the Data softkey and the Data is softkey. When
this event occurs, the oscilloscope will trigger on the clock edge for the Ack
bit after the data byte. This data byte does not need to occur directly after
the control byte.
|  |  |
|---|---|
| SDA
SCL
Start Address R/ Ack Data Ack Stop
Condition Condition | SDA
SCL
Start Address R/ Ack Data Ack Stop
Condition Condition |
|---|---|

---
**[Page 453]**

28 I2C/SPI Triggering and Serial Decode
454 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Read
SDA
SCL
Start or Control R/ Ack Data Ack
Restart byte Trigger point
Condition
• Frame (Start: Addr7: Read: Ack: Data) or Frame (Start: Addr7: Write: Ack: Data)— The
oscilloscope triggers on a read or write frame in 7-bit addressing mode on
the 17th clock edge if all bits in the pattern match. For triggering purposes,
a restart is treated as a start condition.
Read
Write
SDA
SCL
Start or Address R/ Ack Data Ack Stop
Restart Condition
Trigger point
Condition
17th clock edge
• Frame (Start: Addr7: Read: Ack: Data: Ack: Data2) or Frame (Start: Addr7: Write: Ack:
Data: Ack: Data2)— The oscilloscope triggers on a read or write frame in 7-bit
addressing mode on the 26th clock edge if all bits in the pattern match. For
triggering purposes, a restart is treated as a start condition.
Read
Write
Start Address R/W Ack Data Ack Data 2 Ack Stop
Condition Trigger point Condition
26th clock edge
• 10-bit Write — The oscilloscope triggers on a 10-bit write frame on the 26th
clock edge if all bits in the pattern match. The frame is in the format:
Frame (Start: Address byte 1: Write: Address byte 2: Ack: Data)
For triggering purposes, a restart is treated as a start condition.
| Read
Write
Start Address R/W Ack Data Ack Data 2 Ack Stop
Condition Trigger point Condition
26th clock edge | Read
Write
Start Address R/W Ack Data Ack Data 2 Ack Stop
Condition Trigger point Condition
26th clock edge |
|---|---|

---
**[Page 454]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 455
Write
SDA
SCL
Start or Address R/ Ack1 Address Ack2 Data Ack Stop
Restart 1st byte 2nd byte Trigger point Condition
Condition 26th clock edge
5 If you have set the oscilloscope to trigger on an EEPROM Data Read condition:
Press the Data is softkey to set the oscilloscope to trigger when data is =(equal
to), ≠(not equal to), <(less than), or >(greater than) the data value set in the
Data softkey.
The oscilloscope will trigger on the clock edge for the Ack bit after the trigger
event is found. This data byte does not need to occur directly after the control
byte. The oscilloscope will trigger on any data byte that meets the criteria
defined by the Data is and Data softkeys during a current address read or a
random read or a sequential read cycle.
6 If you have set the oscilloscope to trigger on a 7-bit address read or write frame
condition or a 10-bit write frame condition:
a Press the Address softkey and turn the Entry knob to select the 7-bit or
10-bit device address.
You can select from an address range of 0x00 to 0x7F (7-bit) or 0x3FF
(10-bit) hexadecimal. When triggering on a read/write frame, the
oscilloscope will trigger after the start, address, read/write, acknowledge,
and data events occur.
If don't care is selected (0xXX or 0xXXX) for the address, the address will be
ignored. The trigger will always occur on the 17th clock for 7-bit addressing
or 26th clock for 10-bit addressing.
b Press the Data value softkey and turn the Entry knob to select the 8-bit data
pattern on which to trigger.
You can select a data value in the range of 0x00 to 0xFF (hexadecimal). The
oscilloscope will trigger after the start, address, read/write, acknowledge,
and data events occur.
| Write
SDA
SCL
Start or Address R/ Ack1 Address Ack2 Data Ack Stop
Restart 1st byte 2nd byte Trigger point Condition
Condition 26th clock edge | Write
SDA
SCL
Start or Address R/ Ack1 Address Ack2 Data Ack Stop
Restart 1st byte 2nd byte Trigger point Condition
Condition 26th clock edge |
|---|---|

---
**[Page 455]**

28 I2C/SPI Triggering and Serial Decode
456 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If don't care (0xXX) is selected for data, the data will be ignored. The trigger
will always occur on the 17th clock for 7-bit addressing or 26th clock for
10-bit addressing.
c If you have selected a three-byte trigger, press the Data2 value softkey and
turn the Entry knob to select the 8-bit data pattern on which to trigger.
To display I2C serial decode, see “I2C Serial Decode"on page456.
NOTE
I2C Serial Decode
To set up the oscilloscope to capture I2C signals, see “Setup for I2C Signals"on
page451.
For I2C triggering setup see “I2C Triggering"on page452.
NOTE
To set up I2C serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 Choose 7-bit or 8-bit address size. Use 8-bit address size to include the R/W
bit as part of the address value, or choose 7-bit address size to exclude the
R/W bit from the address value.
3 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
4 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
|  |  |
|---|---|

---
**[Page 456]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 457
If the setup does not produce a stable trigger, the I2C signals may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the acquired data.
See Also • “Interpreting I2C Decode"on page457
• “Interpreting I2C Lister Data"on page459
• “Searching for I2C Data in the Lister"on page459
Interpreting I2C Decode
• Angled waveforms show an active bus (inside a packet/frame).
• Mid-level blue lines show an idle bus.
• In the decoded hexadecimal data:
• Address values appear at the start of a frame.
| NOTE |
|---|
|  |
|  |
|---|
|  |

---
**[Page 457]**

28 I2C/SPI Triggering and Serial Decode
458 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Write addresses appear in light-blue along with the "W" character.
• Read addresses appear in yellow along with the "R" character.
• Restart addresses appear in green along with the "S" character.
• Data values appear in white.
• "a" indicates Ack (low), "~a" indicates No Ack (high).
• Decoded text is truncated at the end of the associated frame when there is
insufficient space within frame boundaries.
• Pink vertical bars indicate you need to expand the horizontal scale (and run
again) to see decode.
• Red dots in the decode line indicate that more data can be displayed. Scroll or
expand the horizontal scale to view the data.
• Aliased bus values (undersampled or indeterminate) are drawn in pink.
• Unknown bus values (undefined or error conditions) are drawn in red.

---
**[Page 458]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 459
Interpreting I2C Lister Data
In addition to the standard Time column, the I2C Lister contains these columns:
• Restart — indicated with an "X".
• Address — colored blue for writes, yellow for reads.
• Data — data bytes.
• Missing Ack — indicated by an "X", highlighted in red if an error.
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
Searching for I2C Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
I2C data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With I2C selected as the serial decode mode, press [Search].
|  |
|---|
|  |

---
**[Page 459]**

28 I2C/SPI Triggering and Serial Decode
460 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the I2C signal is being decoded.
3 Press Search; then, select from these options:
• Restart — finds when another start condition occurs before a stop condition.
• Address — finds a packet with the specified address, ignoring the R/W bit.
• Address with no Ack — finds when the acknowledge of the selected address
field is false. The R/W bit is ignored.
• Missing Acknowledge — finds SDA data is high during any Ack SCL clock bit.
• EEPROM Data Read — finds EEPROM control byte value 1010xxx on the SDA
line, followed by a Read bit and an Ack bit. It then looks for the data value
and qualifier set by the Data is softkey and the Data softkeys.
• Frame(Start:Address7:Read:Ack:Data) — finds a read frame on the 17th clock
edge if all bits in the pattern match.
• Frame(Start:Address7:Write:Ack:Data) — finds a write frame on the 17th clock
edge if all bits in the pattern match.
• Frame(Start:Address7:Read:Ack:Data:Ack:Data2) — finds a read frame on the 26th
clock edge if all bits in the pattern match.
• Frame(Start:Address7:Write:Ack:Data:Ack:Data2) — finds a write frame on the
26th clock edge if all bits in the pattern match.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.
Setup for SPI Signals
Serial Peripheral Interface (SPI) signals setup consists of connecting the
oscilloscope to a clock, MOSI data, MISO data, and framing signal, then setting
the threshold voltage level for each input channel, and finally specifying any other
signal parameters.
To set up the oscilloscope to capture SPI signals, use the Signals softkey which
appears in the Serial Decode Menu:
1 Press [Serial].
2 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.

---
**[Page 460]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 461
3 Press the Mode softkey; then, select SPI trigger type.
4 Press the Signals softkey to open the SPI Signals Menu.
5 Press the Clock softkey to open the SPI Clock Menu.
In the SPI Clock Menu:
a Press the Clock softkey; then, turn the Entry knob to select the channel
connected to the SPI serial clock line.
The CLK label for the source channel is automatically set.
b Press the Threshold softkey; then, turn the Entry knob to select the clock
signal threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
c Press the slope softkey ( ) to select rising edge or falling edge for the
selected Clock source.
This determines which clock edge the oscilloscope will use to latch the serial
data. When Display Info is enabled, the graphic changes to show the current
state of the clock signal.
6 Press the MOSI softkey to open the SPI Master-Out Slave-In Menu.
|  |  |
|---|---|
|  |  |
|---|---|
|  |  |  |
|---|---|---|
|  |  |
|---|---|

---
**[Page 461]**

28 I2C/SPI Triggering and Serial Decode
462 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
In the SPI Master-Out Slave-In Menu:
a Press the MOSI Data softkey; then, turn the Entry knob to select the channel
that is connected to a SPI serial data line. (If the channel you selected is off,
switch it on.)
The MOSI label for the source channel is automatically set.
b Press the Threshold softkey; then, turn the Entry knob to select the MOSI
signal threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
7 (Optional) Press the MISO softkey to open the SPI Master-In Slave-Out Menu.
In the SPI Master-In Slave-Out Menu:
a Press the MISO Data softkey; then, turn the Entry knob to select the channel
that is connected to a second SPI serial data line. (If the channel you
selected is off, switch it on.)
The MISO label for the source channel is automatically set.
b Press the Threshold softkey; then, turn the Entry knob to select the MISO
signal threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
8 Press the CS softkey to open the SPI Chip Select Menu.
|  |  |
|---|---|

---
**[Page 462]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 463
In the SPI Chip Select Menu:
a Press the Frame by softkey to select a framing signal that the oscilloscope will
use for determining which clock edge is the first clock edge in the serial
stream.
You can set the oscilloscope to trigger during a high chip select (CS), a low
chip select (~CS), or after a Timeout period during which the clock signal has
been idle.
• If the framing signal is set to CS (or ~CS), the first clock edge as defined,
rising or falling, seen after the CS (or ~CS) signal transitions from low to
high (or high to low) is the first clock in the serial stream.
Chip Select — Press the CS or ~CS softkey; then, turn the Entry knob to
select the channel that is connected to the SPI frame line. The label (~CS
or CS) for the source channel is automatically set. The data pattern and
the clock transition must occur during the time when the framing signal is
valid. The framing signal must be valid for the entire data pattern.
|  |  |
|---|---|

---
**[Page 463]**

28 I2C/SPI Triggering and Serial Decode
464 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• If the framing signal is set to Timeout, the oscilloscope generates it's own
internal framing signal after it sees inactivity on the serial clock line.
Clock Timeout — Select Clock Timeout in the Frame by softkey, then select
the Timeout softkey and turn the Entry knob to set the minimum time that
the Clock signal must be idle (not transitioning) before the oscilloscope
will search for the Data pattern on which to trigger.
The Timeout value can be set anywhere from 100ns to 10s.
When you press the Frame by softkey, the Display Info graphic changes to
show timeout selection or the current state of the chip select signal.
b Press the Threshold softkey; then, turn the Entry knob to select the chip select
signal threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
When Display Info is enabled, information about the selected signal sources and
their threshold voltage levels, as well as a waveform diagram, appears on the
screen.
SPI Triggering
To set up the oscilloscope to capture SPI signals, see “Setup for SPI Signals"on
page460.
After the oscilloscope has been set up to capture SPI signals, you can then trigger
on a data pattern that occurs at the start of a frame. The serial data string can be
specified to be from 4 to 32 bits long.
When you select the SPI trigger type and Display Info is enabled, a graphic is
displayed showing the current state of the frame signal, clock slope, number of
data bits, and data bit values.
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger Type softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the SPI signals are being
decoded.

---
**[Page 464]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 465
3 Press the second Trigger Type softkey; then, turn the Entry knob to select the
trigger condition:
• Master-Out, Slave-In (MOSI) Data — for triggering on the MOSI data signal.
• Master-In, Slave-Out (MISO) Data — for triggering on the MISO data signal.
4 Press the #Bits softkey, and turn the Entry knob to set the number of bits (#Bits)
in the serial data string.
The number of bits in the string can be set anywhere from 4 bits to 64 bits. The
data values for the serial string are displayed in the MOSI/MISO Data string in
the waveform area.
5 Press the MOSI Data or MISO Data softkey and use the binary keypad dialog to
enter bit values of 0 (low), 1 (high), or X (don't care).
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 465]**

28 I2C/SPI Triggering and Serial Decode
466 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
The data value is left-justified in the frame when setting up the trigger. If the
base is Hex, the first digit represents the first 4 bits after the start of frame,
continuing with the remaining digits in the data value.
For SPI decode information see “SPI Serial Decode"on page466.
NOTE
SPI Serial Decode
To set up the oscilloscope to capture SPI signals, see “Setup for SPI Signals"on
page460.
For SPI triggering setup see “SPI Triggering"on page464.
NOTE
To set up SPI serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 Press the Word Size softkey; then, turn the Entry knob to select the number of
bits in a word.
3 Press the Bit Order softkey; then turn the Entry knob to select the bit order, most
significant bit first (MSB) or least significant bit first (LSB), used when
displaying data in the serial decode waveform and in the Lister.
4 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
5 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
|  |  |
|---|---|

---
**[Page 466]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 467
If the setup does not produce a stable trigger, the SPI signal may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the acquired data.
See Also • “Interpreting SPI Decode"on page467
• “Interpreting SPI Lister Data"on page468
• “Searching for SPI Data in the Lister"on page469
Interpreting SPI Decode
• Angled waveforms show an active bus (inside a packet/frame).
• Mid-level blue lines show an idle bus.
• The number of clocks in a frame appears in light-blue above the frame, to the
right.
| NOTE |
|---|
|  |
|  |
|---|
|  |

---
**[Page 467]**

28 I2C/SPI Triggering and Serial Decode
468 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Decoded hexadecimal data values appear in white.
• Decoded text is truncated at the end of the associated frame when there is
insufficient space within frame boundaries.
• Pink vertical bars indicate you need to expand the horizontal scale (and run
again) to see decode.
• Red dots in the decode line indicate that there is data that is not being
displayed. Scroll or expand the horizontal scale to view the information.
• Aliased bus values (undersampled or indeterminate) are drawn in pink.
• Unknown bus values (undefined or error conditions) are drawn in red.
Interpreting SPI Lister Data
In addition to the standard Time column, the SPI Lister contains these columns:
• Data — data bytes (MOSI and MISO).
|  |
|---|
|  |

---
**[Page 468]**

I2C/SPI Triggering and Serial Decode 28
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 469
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
Searching for SPI Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
SPI data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With SPI selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the SPI signals are being decoded.
3 Press Search for:; then, select from these options:
• Master-Out, Slave-In (MOSI) Data — for searching MOSI data.
• Master-In, Slave-Out (MISO) Data — for searching MISO data.
4 In the SPI Bits Search Menu, use the Words softkey to specify the number of
words in the data value; then, use the remaining softkeys to enter the hex digit
values.
5 Press the Data softkey and use the keypad dialog to enter the hexadecimal data
value.
The search pattern is always left-justified in the packet. If you want to search
for a value in the second or higher word, increase the Words count and enter
don't cares ('X's) for the earlier words.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate]key and controls, see “Navigating
the Time Base"on page77.

---
**[Page 469]**

28 I2C/SPI Triggering and Serial Decode
470 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 470]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
471
29 I2S Triggering and Serial
Decode
Setup for I2S Signals / 471
I2S Triggering / 474
I2S Serial Decode / 477
I2S triggering and serial decode requires Option AUDIO or the DSOX6AUDIO
upgrade.
Only one I2S serial bus can be decoded at a time.
NOTE
Setup for I2S Signals
I2S (Inter-IC Sound or Integrated Interchip Sound) signals setup consists of
connecting the oscilloscope to the serial clock, word select, and serial data lines
and then specifying the input signal threshold voltage levels.
To set up the oscilloscope to capture I2S signals:
1 Press [Label] to turn on labels.
2 Press [Serial].
3 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
4 Press the Mode softkey; then, select I2S trigger type.
| NOTE |
|---|
|  |

---
**[Page 471]**

29 I2S Triggering and Serial Decode
472 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
5 Press the Signals softkey to open the I2S Signals Menu.
6 For the SCLK (serial clock), WS (word select), and SDATA (serial data) signals:
a Connect an oscilloscope channel to the signal in the device under test.
b Press the SCLK, WS, or SDATA softkey; then, turn the Entry knob to select the
channel for the signal.
c Press the corresponding Threshold softkey; then, turn the Entry knob to select
the signal threshold voltage level.
Set the threshold levels for the SCLK, WS, and SDATA signals to the middle
of the signals.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
The SCLK, WS, and SDATA labels for the source channels are automatically set.
7 Press the Back Back/Up key to return to the Serial Decode Menu.
8 Press the Bus Config softkey to open the I2S Bus Configuration Menu and display
a diagram showing WS, SCLK, and SDATA signals for the currently specified
bus configuration.
9 Press the Word Size softkey. Turn the Entry knob to match the transmitter word
size of the device under test (from 4 to 32 bits).
10Press the Receiver softkey. Turn the Entry knob to match the receiver word size
of the device under test (from 4 to 32 bits).
11Press the Alignment softkey; then, turn the Entry knob to select the desired
alignment of the data signal (SDATA). The on-screen diagram changes with
your selection.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 472]**

I2S Triggering and Serial Decode 29
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 473
Standard Alignment — MSB of data for each sample is sent first, LSB is sent last.
The MSB appears on the SDATA line one bit clock after the edge of the WS
transition.
LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB
Left-Justified — Data transmission (MSB first) begins at the edge of the WS
transition (without the one-bit delay that Standard format employs).
LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB
Right-Justified — Data transmission (MSB first) is right-justified to the transition
of WS.
LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB
12Press the WSLow softkey; then, turn the Entry knob to select whether WSLow
indicates Left or Right channel data. The on-screen diagram changes with your
selection.
| LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB | LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB |
|---|---|
|  |  |
|---|---|
|  |  |
|  |  |
| LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB | LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB |
|---|---|
|  |
|---|
|  |
|  |
|---|
|  |
|  |
|---|
|  |
| LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB | LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB |
|---|---|
|  |
|---|
|  |
|  |
|---|
|  |

---
**[Page 473]**

29 I2S Triggering and Serial Decode
474 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
WSLow = Left Channel — Left-channel data corresponds to WS=low;
right-channel data corresponds to WS=high. WSLow=Left is the oscilloscope's
default WS setting.
LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB
WSLow = Right Channel — Right-channel data corresponds to WS=low;
left-channel data corresponds to WS=high.
LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB
13Press the SCLKSlope softkey; then, turn the Entry knob to select the SCLK edge
on which data is clocked in your device under test: either rising or falling. The
on-screen diagram changes with your selection.
I2S Triggering
To set up the oscilloscope to capture I2S signals, see “Setup for I2S Signals"on
page471.
After you have set up the oscilloscope to capture I2S signals, you can then trigger
on a data value.
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the I2S signals are being
decoded.
| LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB | LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB |
|---|---|
|  |  |
|---|---|
|  |  |
|  |  |
| LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB | LEFT CHANNEL RIGHT CHANNEL
WS
SCLK
ONE SCLK CYCLE
SDATA 0 1 2 n-2 n-1 0 1 2 n-2 n-1
MSB LSB MSB LSB |
|---|---|
|  |
|---|
|  |
|  |  |  |
|---|---|---|
|  |  |  |
|  |
|---|
|  |
|  |  |  |
|---|---|---|

---
**[Page 474]**

I2S Triggering and Serial Decode 29
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 475
3 Press the Trigger Setup softkey to open the I2S Trigger Setup Menu.
4 Press the Audio softkey; then, turn the Entry knob to choose to trigger on Left
channel events, Right channel events, or events that occur on Either channel.
5 Press the Trigger softkey and choose a qualifier:
• Equal — triggers on the specified audio channel's data word when it equals
the specified word.
• Not equal — triggers on any word other than the specified word.
• Less than — triggers when the channel's data word is less than the specified
value.
• Greater than — triggers when the channel's data word is greater than the
specified value.
• In Range — enter upper and lower values to specify the range in which to
trigger.
• Out of Range — enter upper and lower values to specify range in which trigger
will not occur.
• Increasing value — triggers when the data value is increasing over time and
the specified value is met or exceeded. Set Trigger>= to the data value that
must be reached. Set Armed<= to the value to which the data must fall
before the trigger circuit is re-armed (ready to trigger again). These settings
are made in the current menu when Base is Decimal or in the Bits submenu
when the Base is Binary. The Armed control reduces triggers due to noise.
This trigger condition is best understood when the digital data transferred
over the I2S bus is considered in terms of representing an analog waveform.
The figure below shows a plot of sample data transmitted over an I2S bus for
one channel. In this example, the oscilloscope will trigger at the 2 points
shown since there are two instances in which the data increases from a value
below (or at) the "Armed" value to a value greater than (or equal to) the
specified "Trigger" value.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 475]**

29 I2S Triggering and Serial Decode
476 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If you select an "Armed" value that is equal to or greater than the "Trigger"
value, the "Trigger" value will be increased so that it is always greater than
the "Armed" value.
Trigger Trigger No trigger
"Trigger" value
"Armed" value
• Decreasing value — similar to the description above except the trigger occurs
on a decreasing data word value, and the "Armed" value is the value to
which the data must rise in order to re-arm the trigger.
6 Press the Base softkey and select a number base for entering data values:
• Binary (2's complement).
When Binary is selected, the Bits softkey appears. This softkey opens the I2S
Bits Menu for entering data values.
When the trigger qualifier requires a pair of values (as with In Range, Out of
Range, Increasing value, or Decreasing value), the first softkey in the I2S Bits
Menu lets you select which value of the pair.
In the I2S Bits Menu, press the Bit softkey and rotate the Entry knob to select
each bit; then, use the 01X softkey to set each bit value to zero, one, or
don't care. You can use the Set all Bits softkey to set all bits to the value
chosen on the 01X softkey. Don't care values are only allowed with Equal or
Not Equal trigger qualifiers.
• Signed decimal.
When Decimal is selected, the softkey(s) to the right let you enter decimal
values with the Entry knob. These softkeys can be Data, <, >, or Threshold
depending on the selected trigger qualifier.
If the setup does not produce a stable trigger, the I2S signal may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
| Trigger Trigger No trigger
"Trigger" value
"Armed" value | Trigger Trigger No trigger
"Trigger" value
"Armed" value |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 476]**

I2S Triggering and Serial Decode 29
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 477
To display I2S serial decode, see “I2S Serial Decode"on page477.
NOTE
I2S Serial Decode
To set up the oscilloscope to capture I2S signals, see “Setup for I2S Signals"on
page471.
For I2S triggering setup see “I2S Triggering"on page474.
NOTE
To set up I2S serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 Press the Base softkey to select the number base in which to display decoded
data.
3 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
4 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
If the setup does not produce a stable trigger, the I2S signal may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the acquired data.
See Also • “Interpreting I2S Decode"on page478
• “Interpreting I2S Lister Data"on page479
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 477]**

29 I2S Triggering and Serial Decode
478 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• “Searching for I2S Data in the Lister"on page480
Interpreting I2S Decode
• Angled waveforms show an active bus (inside a packet/frame).
• Mid-level blue lines show an idle bus.
• In the decoded data:
• Right channel data values appear in green along with the "R:" characters.
• Left channel data values appear in white along with the "L:" characters.
• Decoded text is truncated at the end of the associated frame when there is
insufficient space within frame boundaries.
• Pink vertical bars indicate you need to expand the horizontal scale (and run
again) to see decode.
• Red dots in the decode line indicate that more data can be displayed. Scroll or
expand the horizontal scale to view the data.
• Aliased bus values (undersampled or indeterminate) are drawn in pink.
|  |
|---|
|  |

---
**[Page 478]**

I2S Triggering and Serial Decode 29
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 479
• Unknown bus values (undefined or error conditions) are drawn in red.
When the receiver word size is greater than the transmit word size, the decoder fills the least
NOTE
significant bits with zeros and the decoded value does not match the trigger value.
Interpreting I2S Lister Data
In addition to the standard Time column, the I2S Lister contains these columns:
• Left Channel — displays the left channel data.
• Right Channel — displays the right channel data.
• Errors — highlighted in red and marked with an "X".
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
| NOTE |
|---|
|  |
|  |
|---|
|  |

---
**[Page 479]**

29 I2S Triggering and Serial Decode
480 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Searching for I2S Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
I2S data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With I2S selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the I2S signals are being decoded.
3 In the Search Menu, press Search; then, select from these options:
• = (Equal) — finds the specified audio channel's data word when it equals the
specified word.
• != (Not Equal) — finds any word other than the specified word.
• < (Less than) — finds when the channel's data word is less than the specified
value.
• > (Greater than) — finds when the channel's data word is greater than the
specified value.
• >< (In Range) — enter upper and lower values to specify the range to find.
• <> (Out of Range) — enter upper and lower values to specify range not to find.
• Errors — finds all errors.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 480]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
481
30 MIL-STD-1553/ARINC 429
Triggering and Serial
Decode
Setup for MIL-STD-1553 Signals / 481
MIL-STD-1553 Triggering / 483
MIL-STD-1553 Serial Decode / 484
Setup for ARINC429 Signals / 488
ARINC429 Triggering / 489
ARINC429 Serial Decode / 491
MIL-STD-1553/ARINC429 triggering and serial decode requires Option AERO or
the DSOX6AERO upgrade.
The MIL-STD-1553 triggering and decode solution supports bi-phase
MIL-STD-1553 signaling by using dual threshold triggering. The solution supports
the standard 1553 Manchester II encoding, data rate of 1Mb/s, and word length
of 20 bits.
Setup for MIL-STD-1553 Signals
MIL-STD-1553 signal setup consists of first connecting the oscilloscope to a serial
MIL-STD-1553 signal using a differential active probe (the Keysight N2791A is
recommended), specifying the signal source, and specifying the high and low
trigger threshold voltage levels.
To set up the oscilloscope to capture MIL-STD-1553 signals:

---
**[Page 481]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
482 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
1 Press [Label] to turn on labels.
2 Press [Serial].
3 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
4 Press the Mode softkey; then, select MIL-STD-1553 decode mode.
5 Press the Signals softkey to open the MIL-STD-1553 Signals Menu.
6 Press the Source softkey to select the channel connected to the MIL-STD-1553
signal line.
The label for the MIL-STD-1553 source channel is automatically set.
7 Press the Back Back/Up key to return to the Serial Decode Menu.
8 Press the Auto Setup softkey which performs these actions:
• Sets the probe attenuation factor of the input Source channel to 10:1.
• Sets upper and lower thresholds to a voltage value equal to ±1/3 division
based on the current V/div setting.
• Turns off trigger noise reject.
• Turns on Serial Decode.
• Sets the trigger type to MIL-1553.
9 If the upper and lower thresholds are not set correctly by Auto Setup, press the
Signals softkey to return to the MIL-STD-1553 Signals Menu. Then:
• Press the High Threshold softkey; then, turn the Entry knob to set the high
trigger threshold voltage level.
• Press the Low Threshold softkey; then, turn the Entry knob to set the low
trigger threshold voltage level.
The threshold voltage levels are used in decoding and will become the trigger
levels when the trigger type is set to the selected serial decode slot.
|  |  |
|---|---|

---
**[Page 482]**

MIL-STD-1553/ARINC429 Triggering and Serial Decode 30
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 483
MIL-STD-1553 Triggering
To set up the oscilloscope to capture a MIL-STD-1553 signal, see “Setup for
MIL-STD-1553 Signals"on page481.
To set up a MIL-STD-1553 trigger:
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the MIL-STD-1553 signal is
being decoded.
3 Press the Trigger softkey; then, turn the Entry knob to select the trigger
condition:
• Data Word Start — triggers on the start of a Data word (at the end of a valid
Data Sync pulse).
• Data Word Stop — triggers on the end of a Data word.
• Command/Status Word Start — triggers on the start of Command/Status word
(at the end of a valid C/S Sync pulse).
• Command/Status Word Stop — triggers on the end of a Command/Status word.
• Remote Terminal Address — triggers if the RTA of the Command/Status word
matches the specified value.
When this option is selected, the RTA softkey becomes available and lets you
select the hex Remote Terminal Address value to trigger on. If you select
0xXX (don't cares), the oscilloscope will trigger on any RTA.
• Remote Terminal Address + 11 Bits — triggers if the RTA and the remaining 11
bits match the specified criteria.
When this option is selected, these softkeys become available:
• The RTA softkey lets you select the hex Remote Terminal Address value.
• The Bit Times softkey lets you specify the bit time position values using a
binary keypad dialog to enter bit values of 0 (low), 1 (high), or X (don't
care).
|  |  |
|---|---|

---
**[Page 483]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
484 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Parity Error — triggers if the (odd) parity bit is incorrect for the data in the
word.
• Sync Error — triggers if an invalid Sync pulse is found.
• Manchester Error — triggers if a Manchester encoding error is detected.
For MIL-STD-1553 decode information see “MIL-STD-1553 Serial Decode"on page484.
NOTE
MIL-STD-1553 Serial Decode
To set up the oscilloscope to capture MIL-STD-1553 signals, see “Setup for
MIL-STD-1553 Signals"on page481.
For MIL-STD-1553 triggering setup see “MIL-STD-1553 Triggering"on page483.
NOTE
To set up MIL-STD-1553 serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 Use the Base softkey to select between hexadecimal and binary display of the
decoded data.
The base setting is used for the display of the remote terminal address and the
data, in both the decode line and in the Lister.
3 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
4 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
You can use the horizontal Zoom window for easier navigation of the decoded data.
See Also • “Interpreting MIL-STD-1553 Decode"on page485
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
|  |  |
|---|---|

---
**[Page 484]**

MIL-STD-1553/ARINC429 Triggering and Serial Decode 30
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 485
• “Interpreting MIL-STD-1553 Lister Data"on page486
• “Searching for MIL-STD-1553 Data in the Lister"on page487
Interpreting MIL-STD-1553 Decode
To display serial decode information, you must press [Run] or [Single] after
switching on serial decode.
The MIL-STD-1553 decode display is color coded as follows:
• Command and Status decoded data is colored green, with the Remote Terminal
Address (5 bits of data) being displayed first, then the text "C/S:", followed by
the value of the remaining 11 bits of a Command/Status word.
• Data word decoded data is colored white, preceded by the text "D:".
• Command/Status or Data words with a Parity error have the decode text
displayed in red instead of green or white.
• SYNC errors are displayed with the word "SYNC" within red angle brackets.
|  |
|---|
|  |

---
**[Page 485]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
486 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Manchester encoding errors are displayed with the word "MANCH" within blue
angle brackets (blue instead of red because a valid Sync pulse started the
word).
Interpreting MIL-STD-1553 Lister Data
In addition to the standard Time column, the MIL-STD-1553 Lister contains these
columns:
• RTA — displays the Remote Terminal Address for Command/Status words,
nothing for Data words.
• Word Type — "Cmd/Status" for Command/Status words, "Data" for Data words.
For Command/Status words the background color is green to match the
decode text color.
• Data — the 11 bits after the RTA for Command/Status words, or the 16 bits of a
Data word.
• Errors — "Sync", "Parity", or "Manchester" errors as appropriate. The
background color is red to indicate an error.
|  |
|---|
|  |

---
**[Page 486]**

MIL-STD-1553/ARINC429 Triggering and Serial Decode 30
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 487
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
Searching for MIL-STD-1553 Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
MIL-STD-1553 data in the Lister. You can use the [Navigate] key and controls to
navigate through the marked rows.
1 With MIL-STD-1553 selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the MIL-STD-1553 signal is being
decoded.
3 Press Search; then, select from these options:
• Data Word Start — finds the start of a Data word (at the end of a valid Data
Sync pulse).
• Command/Status Word Start — finds the start of Command/Status word (at the
end of a valid C/S Sync pulse).
• Remote Terminal Address — finds the Command/Status word whose RTA
matches the specified value. The value is specified in hex.
When this option is selected, the RTA softkey becomes available and lets you
select the hex Remote Terminal Address value to find.
• Remote Terminal Address + 11 Bits — finds the RTA and the remaining 11 bits
that match the specified criteria.
When this option is selected, these softkeys become available:
• The RTA softkey lets you select the hex Remote Terminal Address value.
• The Bit Time softkey lets you select the bit time position.
• The 0 1 X softkey lets you set the bit time position value as a 1, 0, or X
(don't care).
• Parity Error — finds (odd) parity bits that are incorrect for the data in the word.
• Sync Error — finds invalid Sync pulses.
• Manchester Error — finds Manchester encoding errors.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 487]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
488 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Setup for ARINC 429 Signals
Setup consists of first connecting the oscilloscope to a ARINC429 signal using a
differential active probe (the Keysight N2791A is recommended), then using the
Signals Menu to specify the signal source, the high and low trigger threshold
voltage levels, the signal speed, and the signal type.
To set up the oscilloscope to capture ARINC429 signals:
1 Press [Serial].
2 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
3 Press the Mode softkey; then, select ARINC429 decode mode.
4 Press the Signals softkey to open the ARINC429 Signals Menu.
5 Press Source; then, select the channel for the ARINC429 signal.
The label for the ARINC429 source channel is automatically set.
6 Press the Speed softkey to open the ARINC429 Speed Menu.
7 In the ARINC429 Speed Menu, press the Speed softkey and specify the speed of
the ARINC 429 signal:
• High — 100kb/s.
• Low — 12.5kb/s.
• User Defined — press the User Baud softkey and enter the user-defined speed
value.
8 Press the Back Back/Up key to return to the ARINC429 Signals Menu.
9 Press the Signal Type softkey and specify the signal type of the ARINC 429
signal:
• Line A (non-inverted).
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 488]**

MIL-STD-1553/ARINC429 Triggering and Serial Decode 30
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 489
• Line B (inverted).
• Differential (A-B).
10Press the Auto Setup softkey to automatically set these options for decoding and
triggering on ARINC 429 signals:
• High Trigger Threshold: 3.0V.
• Low Trigger Threshold: -3.0V.
• Noise Reject: Off.
• Probe Attenuation: 10.0.
• Vertical Scale: 4V/div.
• Serial Decode: On.
• Base: Hex.
• Word Format: Label/SDI/Data/SSM.
• Trigger: currently active serial bus.
• Trigger Mode: Word Start.
11If the high and low thresholds are not set correctly by Auto Setup:
• Press the High Threshold softkey; then, turn the Entry knob to set the high
trigger threshold voltage level.
• Press the Low Threshold softkey; then, turn the Entry knob to set the low
trigger threshold voltage level.
The threshold voltage levels are used in decoding and will become the trigger
levels when the trigger type is set to the selected serial decode slot.
ARINC 429 Triggering
To set up the oscilloscope to capture a ARINC429 signal, see “Setup for
ARINC429 Signals"on page488.
After setting up the oscilloscope to capture a ARINC429 signal:
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the ARINC429 signal is
being decoded.

---
**[Page 489]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
490 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
3 Press the Trigger: softkey; then, turn the Entry knob to select the trigger
condition:
• Word Start — triggers on the start of a word.
• Word Stop — triggers at the end of a word.
• Label — triggers on the specified label value.
• Label + Bits — triggers on the label and the other word fields as specified.
• Label Range — triggers on a label following in a min/max range.
• Parity Error — triggers on words with a parity error.
• Word Error — triggers on an intra-word coding error.
• Gap Error — triggers on an inter-word gap error.
• Word or Gap Error — triggers on either a Word or Gap Error.
• All Errors — triggers on any of the above errors.
• All Bits (Eye) — triggers on any bit, which will therefore form an eye diagram.
• All 0 Bits — triggers on any bit with a value of zero.
• All 1 Bits — triggers on any bit with a value of one.
4 If you select the Label or Label + Bits condition, use the Label softkey to specify
the label value.
Label values are always displayed in octal.
5 If you select the Label + Bits condition, use the Bits softkey and submenu to
specify the bit values:
Press the Data, SSM, and/or SSM softkeys and use the binary keypad dialog to
enter the 0, 1, or X (don't care) values.
The SDI or SSM selections may not be available, depending on word format
selection in the Serial Decode Menu.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 490]**

MIL-STD-1553/ARINC429 Triggering and Serial Decode 30
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 491
6 If you select the Label Range condition, use the Label Min and Label Max softkeys
to specify the ends of the range.
Again, label values are always displayed in octal.
You can use the Zoom mode for easier navigation of the decoded data.
To display ARINC429 serial decode, see “ARINC429 Serial Decode"on page491.
NOTE
ARINC 429 Serial Decode
To set up the oscilloscope to capture ARINC429 signals, see “Setup for
ARINC429 Signals"on page488.
For ARINC429 triggering set up see “ARINC429 Triggering"on page489.
NOTE
To set up ARINC429 serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 In the submenu accessed by the Settings softkey, you can use the Base softkey
to select between hexadecimal and binary display of the decoded data.
The base setting is used for data display in both the decode line and in the
Lister.
Label values are always displayed in octal, and SSM and SDI values are always
displayed in binary.
3 Press the Word Format softkey and specify the word decode format:
• Label/SDI/Data/SSM:
• Label - 8 bits.
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
|  |  |
|---|---|

---
**[Page 491]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
492 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• SDI - 2 bits.
• Data - 19 bits.
• SSM - 2 bits.
• Label/Data/SSM:
• Label - 8 bits.
• Data - 21 bits.
• SSM - 2 bits.
• Label/Data:
• Label - 8 bits.
• Data - 23 bits.
4 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
5 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
If the setup does not produce a stable trigger, the ARINC429 signal may be slow enough that
NOTE
the oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode
softkey to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the decoded data.
See Also • “Interpreting ARINC429 Decode"on page493
• “ARINC429 Totalizer"on page494
• “Interpreting ARINC429 Lister Data"on page495
• “Searching for ARINC429 Data in the Lister"on page496
| NOTE |
|---|
|  |

---
**[Page 492]**

MIL-STD-1553/ARINC429 Triggering and Serial Decode 30
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 493
Interpreting ARINC 429 Decode
Depending on the selected word decode format, the ARINC429 decode display is
color coded as follows:
• When the decode format is Label/SDI/Data/SSM:
• Label (yellow) (8 bits) – displayed in octal.
• SDI (blue) (2 bits) – displayed in binary.
• Data (white, red if parity error) (19 bits) – displayed in the selected Base.
• SSM (green) (2 bits) – displayed in binary.
• When the decode format is Label/Data/SSM:
• Label (yellow) (8 bits) – displayed in octal.
• Data (white, red if parity error) (21 bits) – displayed in the selected Base.
• SSM (green) (2 bits) – displayed in binary.
• When the decode format is Label/Data:
• Label (yellow) (8 bits) – displayed in octal.
|  |
|---|
|  |

---
**[Page 493]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
494 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Data (white, red if parity error) (23 bits) – displayed in the selected Base.
The Label bits are displayed in the same order as they are received on the wire. For
the Data, SSM, and SDI bits, the fields are displayed in the order received;
however, the bits within those fields are displayed in reverse order. In other words,
the non-Label fields are displayed in the ARINC429 Word Format, while the bits
for those fields have the opposite transfer order on the wire.
ARINC 429 Totalizer
The ARINC429 totalizer measures the total ARINC429 words and errors.
The totalizer is always running, counting words and errors, and is displayed
whenever ARINC429 decode is displayed. The totalizer counts even when the
oscilloscope is stopped (not acquiring data).
Pressing the [Run/Stop] key does not affect the totalizer.
When an overflow condition occurs, the counter displays OVERFLOW.
The counters can be reset to zero by pressing the Reset ARINC429 Counters softkey
(in the decode Settings menu).
|  |
|---|
|  |

---
**[Page 494]**

MIL-STD-1553/ARINC429 Triggering and Serial Decode 30
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 495
Interpreting ARINC 429 Lister Data
In addition to the standard Time column, the ARINC429 Lister contains these
columns:
• Label — the 5-bit label value in octal format.
• SDI — the bit values (if included in the word decode format).
• Data — the data value in binary or hex, depending on the base setting.
• SSM — the bit values (if included in the word decode format).
• Errors — highlighted in red. Errors can be Parity, Word, or Gap.
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
|  |
|---|
|  |

---
**[Page 495]**

30 MIL-STD-1553/ARINC429 Triggering and Serial Decode
496 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Searching for ARINC 429 Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
ARINC429 data in the Lister. You can use the [Navigate] key and controls to
navigate through the marked rows.
1 With ARINC429 selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the ARINC429 signal is being
decoded.
3 Press Search; then, select from these options:
• Label — finds the specified label value.
Label values are always displayed in octal.
• Label + Bits — finds the label and the other word fields as specified.
• Parity Error — finds words with a parity error.
• Word Error — finds an intra-word coding error.
• Gap Error — finds an inter-word gap error.
• Word or Gap Error — finds either a Word or Gap Error.
• All Errors — finds any of the above errors.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 496]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
497
31 SENT Triggering and Serial
Decode
Setup for SENT Signals / 497
SENT Triggering / 502
SENT Serial Decode / 504
SENT (Single Edge Nibble Transmission) triggering and serial decode requires the
DSOX6SENSOR license.
Setup for SENT Signals
To set up the oscilloscope to capture SENT signals:
1 Connect an oscilloscope channel to the signal in the device under test.
Analog channels or digital channels can be used.
2 Press [Serial].
3 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
4 Press the Mode softkey; then, select SENT.
5 Press the Source softkey to open the SENT Source Menu.

---
**[Page 497]**

31 SENT Triggering and Serial Decode
498 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
a Press the Source softkey; then, turn the Entry knob to select the channel for
the signal.
b Press the Threshold softkey; then, turn the Entry knob to select the signal
threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode
(Serial1 or Serial2).
c Press the Back Back/Up key to return to the SENT Serial Decode Menu.
6 Press the Bus Config softkey to open the SENT Bus Configuration Menu.
a Press the Clock Period softkey; then, turn the Entry knob (or press the softkey
again and use a keypad dialog) to specify the nominal clock period (tick)
time.
b Press the Tolerance softkey; then, turn the Entry knob (or press the softkey
again and use a keypad dialog) to specify the percent tolerance for
determining whether the sync pulse is valid for decoding the data.
If the measured time of the sync pulse is within the percent tolerance of the
nominal clock period setting, the decode proceeds; otherwise, the sync
pulse is in error, and the data is not decoded.
c Press the # of Nibbles softkey; then, turn the Entry knob (or press the softkey
again and use a keypad dialog) to specify the number of nibbles in a Fast
Channel Message.
d Press the Idle State softkey to specify the idle state of the SENT signal.
e Press the CRC Format softkey to specify the CRC format that will be used in
calculating the correctness of the CRCs.
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 498]**

SENT Triggering and Serial Decode 31
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 499
Enhanced Serial Message CRCs are always calculated using the 2010
format, but for the Fast Channel Messages, and for Short Serial Message
CRCs, the chosen setting is used.
f Press the Pause Pulse softkey to specify whether there is a pause pulse
between Fast Channel Messages.
A SENT serial bus with no pause pulse is never idle. This means, during
normal operation, the fast channel decode line will show a continuous
stream of packets, with a new packet opening as soon as the previous one
has closed.
If there is a pause pulse (and Pause Pulse is on), idle time is shown between
messages.
g Press the Back Back/Up key to return to the SENT Serial Decode Menu.
7 Press the Settings softkey to open the SENT Settings Menu.
a Press the Message Format softkey to select the message decode/triggering
format:
• Fast Nibbles (All) — displays the raw transmitted nibble values.
• Fast Signals — displays Fast Channel Message Signals.
• Fast + Short Serial — displays both Fast and Slow Messages (Short format)
simultaneously.
• Fast + Enhanced Serial — displays both Fast and Slow Messages (Enhanced
format) simultaneously.
• Short Serial — displays Slow Channel Messages in Short format.
• Enhanced Serial — displays Slow Channel Messages in Enhanced format.
This selection affects both decoding and triggering. The decode is affected
both in how the system interprets the data, and what will be displayed. The
trigger is affected in that the trigger hardware needs to be configured to
trigger on serial messages correctly.
You can specify the nibble display order for Fast Channel Message Signals
(under the Fast Signals softkey). Raw transmitted nibble values are displayed
in the order received.
|  |  |
|---|---|

---
**[Page 499]**

31 SENT Triggering and Serial Decode
500 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
For the Slow Channel, the proper format, Short or Enhanced, must be chosen for proper
NOTE
decoding and triggering to occur.
Slow Channel Serial Messages are always displayed as defined by the SENT
specification.
b Press the Display softkey to select between hexadecimal, unsigned decimal,
or "transfer function" display of Fast Channel nibbles, signals, and CRC
values, as well as Slow Channel IDs, data, and CRC values. (The S&C value is
always displayed in binary.)
Your selection is used for both the Lister and the decode line displays.
When Transfer Function is selected (for message formats that include fast
signals), Fast Channel Signals display a calculated physical value based on
the specified Multiplier and Offset (under the Fast Signals softkey):
• PhysicalValue = (Multiplier * SignalValueAsUnsignedInteger) + Offset
When Transfer Function is selected, the CRC and Slow Channel information is
displayed in hex.
8 When a fast signals message decode/triggering is selected, press the Fast
Signals softkey to open the SENT Signals Menu where you can define and
specify the display of up to six Fast Signals.
| NOTE |
|---|
|  |

---
**[Page 500]**

SENT Triggering and Serial Decode 31
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 501
a Press the Fast Signals softkey and use the Entry knob to select the Fast Signal
to be defined.
Once a Fast Signal is selected, press the softkey again to enable or disable
decode for that signal.
b Press the Start Bit # (MSB) softkey to specify the starting bit for the selected
signal.
c Press the # of Bits softkey to specify the number of bits in the selected signal.
d Press the Nibble Order softkey to specify the nibble display order as either
most significant nibble (MSN) or least significant nibble (LSN) first.
e When the display mode setting is Transfer Function (see the SENT Settings
Menu), press the Multiplier or Offset softkeys; then, turn the Entry knob (or
press the softkey again and use a keypad dialog) to specify the value.
The multiplier and offset values are used in calculating a physical value
displayed for the Fast Signal:
• PhysicalValue = (Multiplier * SignalValueAsUnsignedInteger) + Offset
Here are some Fast Signal definition examples:
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 501]**

31 SENT Triggering and Serial Decode
502 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
SENT Triggering
To set up the oscilloscope to capture SENT signals, see “Setup for SENT
Signals"on page497.
To set up a SENT trigger condition:
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger Type softkey; then, turn the Entry knob to
select the serial decode (Serial1 or Serial2) of the SENT signal.
3 Press the Trigger on: softkey and use the Entry knob to select the SENT
trigger condition:
• Start of Fast Channel Message — triggers on the start of any Fast Channel
Message (after 56 Synchronization/Calibration ticks).
• Start of Slow Channel Message — trigger on the start of any Slow Channel
Message.
• Fast Channel SC & Data — triggers on a Fast Channel Message when the Status
& Communication nibble and the data nibbles match the values entered
using additional softkeys.
• Slow Channel Message ID — triggers when a Slow Channel Message ID
matches the value entered using additional softkeys.
• Slow Channel Message ID & Data — triggers when a Slow Channel Message ID
and Data field both match the values entered using additional softkeys.
• Tolerance Violation — triggers when the sync pulse width varies from the
nominal value by greater than the entered percentage.
• Fast Channel CRC Error — triggers on any Fast Channel Message CRC error.
• Slow Chanel CRC Error — triggers on any Slow Channel Message CRC error.
• All CRC Errors — triggers on any CRC error, Fast or Slow.
• Pulse Period Error — triggers if a nibble is either too wide or too narrow (for
example, data nibble < 12 (11.5) or > 27 (27.5) ticks wide). Sync, S&C, data,
or checksum pulse periods are checked.
|  |  |
|---|---|

---
**[Page 502]**

SENT Triggering and Serial Decode 31
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 503
• Successive Sync Pulses Error — triggers on a sync pulse whose width varies
from the previous sync pulse's width by greater than 1/64 (1.5625%, as
defined in the SENT specification).
4 If you choose the Fast Channel SC & Data trigger condition:
a Press the Base softkey to choose between Hex or Binary data value entry.
Use the Binary method if you need to enter "don't care" bits (X) within a
nibble. If all bits in a nibble are "don't care", the hex nibble is displayed as
"don't care" (X). When all bits in a nibble are 1s or 0s, the hex value is shown.
Hex nibbles that contain a mix of 0/1 bits and "don't care" bits are displayed
as "$".
b Press the SC & Data softkey and use the keypad dialog to enter the data
value.
The S&C nibble is the left most nibble entered in the string of numbers,
followed by the data nibbles.
5 If you choose the Slow Channel Message ID or Slow Channel Message ID & Data
trigger condition:
a Press the Configuration softkey to select the desired packet ID for the selected
packet type.
When an Enhanced Serial message format is specified (see “Setup for SENT
Signals"on page497), press this softkey to select which enhanced format
configuration is being used:
• 16-Bit Data, 4-Bit ID
• 12-Bit Data, 8-Bit ID
b Press the Slow Message ID softkey and use the Entry knob (or press the
softkey again and use a keypad dialog) to specify the Slow Message ID.
c If you choose the Slow Channel Message ID & Data trigger condition, press the
Slow Data softkey and use the Entry knob (or press the softkey again and use
a keypad dialog) to specify the Slow Message data.
6 If you choose the Tolerance Violation trigger condition, press the Tolerance
softkey and use the Entry knob (or press the softkey again and use a keypad
dialog) to specify the tolerance variation that is considered a violation.
The percentage entered must be less than the percent tolerance specified in
the decode bus configuration settings.

---
**[Page 503]**

31 SENT Triggering and Serial Decode
504 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
If the setup does not produce a stable trigger, the SENT signals may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
To display SENT serial decode, see “SENT Serial Decode"on page504.
NOTE
SENT Serial Decode
To set up the oscilloscope to capture SENT signals, see “Setup for SENT
Signals"on page497.
For SENT triggering setup see “SENT Triggering"on page502.
NOTE
To set up SENT serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
3 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
If the setup does not produce a stable trigger, the SENT signals may be slow enough that the
NOTE
oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode softkey
to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the acquired data.
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 504]**

SENT Triggering and Serial Decode 31
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 505
See Also • “Interpreting SENT Decode"on page505
• “Interpreting SENT Lister Data"on page507
• “Searching for SENT Data in the Lister"on page509
Interpreting SENT Decode
The fields of the Fast and Slow Channels are displayed as follows. Note that the
Slow Channel has three different variants. The colors noted below indicate the
color of the text:
• Fast Channel:
• Status & Communication (S&C) Nibble (green) (4 bits):
• 2 Application bits and 2 Serial Message bits will be displayed, in all
formats.
• Data Nibbles (white) (4 bits, but may be combined into Signals, based on
format):
|  |  |
|---|---|

---
**[Page 505]**

31 SENT Triggering and Serial Decode
506 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• "Fast Nibbles (All)" format — each nibble displayed as hex or decimal
number.
• "Fast Signals", "Fast + Short Serial", or "Fast + Enhanced Serial" formats — If
any fast signals are enabled, signals are displayed like:
• S1:<value>;S2:<value>.
• Unused nibbles are not displayed (example, when 6th nibble is an
inverted copy of the 1st nibble).
• CRC Nibble (blue when valid, red when error detected) (4 bits).
• Slow Channel – Short Serial Message:
• Message ID (yellow) (4 bits).
• Data Byte (white) (8 bits).
• CRC (blue when valid, red when error detected) (4 bits).
• Slow Channel – Enhanced Serial Message:
• CRC (blue when valid, orange if end of message is off screen, red when error
detected) (6 bits).
|  |  |
|---|---|

---
**[Page 506]**

SENT Triggering and Serial Decode 31
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 507
• Message ID (yellow) (4 or 8 bits).
• Data Field (white) (16 or 12 bits).
Enhanced Serial Message CRCs will be displayed in orange if the data to calculate
the CRC is off-screen to the right. Serial messages will also be shown with a
leading idle line in orange and an opening brace in orange if the starting location
cannot be precisely determined due to that data being off screen to the left.
The decode will also indicate errors where a nibble's pulse is too wide or too
narrow. This will be indicated by a ">" or "<" in red, as well as the rest of the
packet's outline and closing brace being in red, as well as an orange idle line until
the next valid sync. At the time of the valid sync, there will be an orange opening
brace.
Interpreting SENT Lister Data
|  |
|---|
|  |

---
**[Page 507]**

31 SENT Triggering and Serial Decode
508 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Each Fast or Slow Channel message is represented on its own row. The start time
of Slow Channel messages determines their order relative to the Fast Channel
messages. Therefore, a Slow Channel message appears before most of the Fast
Channel messages that it was built from. This is due to the "Time" column holding
the start time of a packet.
In addition to the standard Time column, the following columns are used to
support both the Fast Channel and the Slow Channel simultaneously, and these
columns are displayed for all Message Format modes except Fast Nibbles (All):
• S&C — (Fast Channel Only) (binary).
• ID — (Slow Channel Only) (Hex or Decimal).
• Data — (Hex or Decimal):
• Fast Channel:
• <value> (value in Hex or Decimal) (Raw Decode Format).
• S1:<value>;S2:<value> (values are in Hex or Decimal) (other formats).
• Slow Channel: Hex or Decimal display of a single value.
• CRC — (value in Hex or Decimal).
• Pause Ticks (ticks will be displayed in orange if the uncertainty of the
measurement is > 25%).
• Errors.
When the Message Format is set to Fast Nibbles (All), the following columns are
displayed:
• Sync Width.
• S&C — (Fast Channel Only) (binary).
• Data — (Hex or Decimal).
• CRC — (value in Hex or Decimal).
• Errors.
When the selected Message Format contains both Fast and Slow Channel
Messages, the S&C Lister field (populated for Fast Messages) has a green
background, and the ID Lister field (populated for Slow Messages) has a yellow
background.
Slow Channel CRC values that cannot be confirmed as valid or invalid due to data
used in the calculation being off screen to the right, will have an orange
background in the Lister.

---
**[Page 508]**

SENT Triggering and Serial Decode 31
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 509
Searching for SENT Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
SENT data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With SENT selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
Serial1 or Serial2, where the SENT signals is being decoded.
3 In the Search Menu, press Search for; then, select from these options:
• Fast Channel Data — finds Fast Channel data nibbles that match the values
entered using additional softkeys.
• Slow Channel Message ID — finds Slow Channel Message IDs that match the
value entered using additional softkeys.
• Slow Channel Message ID & Data — finds Slow Channel Message IDs and Data
that match the values entered using additional softkeys.
• All CRC Errors — finds any CRC error, Fast or Slow.
• Pulse Period Error — finds where a nibble is either too wide or too narrow (for
example, data nibble < 12 (11.5) or > 27 (27.5) ticks wide). Sync, S&C, data,
or checksum pulse periods are checked.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 509]**

31 SENT Triggering and Serial Decode
510 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 510]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
511
32 UART/RS232 Triggering
and Serial Decode
Setup for UART/RS232 Signals / 511
UART/RS232 Triggering / 513
UART/RS232 Serial Decode / 515
UART/RS232 triggering and serial decode requires Option COMP or the
DSOX6COMP upgrade.
Setup for UART/RS232 Signals
To set up the oscilloscope to capture UART/RS232 signals:
1 Press [Serial].
2 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
3 Press the Mode softkey; then, select UART/RS232 trigger type.
4 Press the Signals softkey to open the UART/RS232 Signals Menu.
|  |  |
|---|---|

---
**[Page 511]**

32 UART/RS232 Triggering and Serial Decode
512 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
5 For both the Rx and Tx signals:
a Connect an oscilloscope channel to the signal in the device under test.
b Press the Rx or Tx softkey; then, turn the Entry knob to select the channel for
the signal.
c Press the corresponding Threshold softkey; then, turn the Entry knob to select
the signal threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
The RX and TX labels for the source channels are automatically set.
6 Press the Back Back/Up key to return to the Serial Decode Menu.
7 Press the Bus Config softkey to open the UART/RS232 Bus Configuration Menu.
Set the following parameters.
a #Bits — Set the number of bits in the UART/RS232 words to match your
device under test (selectable from 5-9 bits).
b Parity — Choose odd, even, or none, based on your device under test.
c Baud — Press the Baud Rate softkey, then press the Baud softkey and select a
baud rate to match the signal in your device under test. If the desired baud
rate is not listed, select User Defined on the Baud softkey; then, select the
desired baud rate using the User Baud softkey.
You can set the UART baud rate from 1.2kb/s to 8.0000Mb/s in increments
of 100b/s.
d Polarity — Select idle low or idle high to match your device under test's state
when at idle. For RS232 select idle low.
e Bit Order — Select whether the most significant bit (MSB) or the least
significant bit (LSB) is presented after the start bit in the signal from your
device under test. For RS232 select LSB.
In the serial decode display, the most significant bit is always displayed on the left regardless
NOTE
of how Bit Order is set.
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 512]**

UART/RS232 Triggering and Serial Decode 32
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 513
UART/RS232 Triggering
To set up the oscilloscope to capture UART/RS-232 signals, see “Setup for
UART/RS232 Signals"on page511.
To trigger on a UART (Universal Asynchronous Receiver/Transmitter) signal
connect the oscilloscope to the Rx and Tx lines and set up a trigger condition.
RS232 (Recommended Standard 232) is one example of a UART protocol.
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the UART/RS232 signals are
being decoded.
3 Press the Trigger Setup softkey to open the UART/RS232 Trigger Setup Menu.
4 Press the Base softkey to select Hex or ASCII as the base displayed on the Data
softkey in the UART/RS232 Trigger Setup Menu.
Note that the setting of this softkey does not affect the selected base of the
decode display.
5 Press the Trigger softkey and set up the desired trigger condition:
• Rx Start Bit — The oscilloscope triggers when a start bit occurs on Rx.
• Rx Stop Bit — Triggers when a stop bit occurs on Rx. The trigger will occur on
the first stop bit. This is done automatically whether the device under test
uses 1, 1.5, or 2 stop bits. You do not need to specify the number of stop bits
used by the device Under test.
• Rx Data — Triggers on a data byte that you specify. For use when the device
under test data words are from 5 to 8 bits in length (no 9th (alert) bit).
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 513]**

32 UART/RS232 Triggering and Serial Decode
514 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Rx 1:Data — For use when the device under test data words are 9 bits in
length including the alert bit (the 9th bit). Triggers only when the 9th (alert)
bit is 1. The specified data byte applies to the least significant 8 bits
(excludes the 9th (alert) bit).
• Rx 0:Data — For use when the device under test data words are 9 bits in
length including the alert bit (the 9th bit). Triggers only when the 9th (alert)
bit is 0. The specified data byte applies to the least significant 8 bits
(excludes the 9th (alert) bit).
• Rx X:Data — For use when the device under test data words are 9 bits in
length including the alert bit (the 9th bit). Triggers on a data byte that you
specify regardless of the value of the 9th (alert) bit. The specified data byte
applies to the least significant 8 bits (excludes the 9th (alert) bit).
• Similar choices are available for Tx.
• Rx or Tx Parity Error — Triggers on a parity error based on the parity you have
set in the Bus Configuration Menu.
6 If you choose a trigger condition that includes "Data" in its description (for
example: Rx Data), then press the Data is softkey, and choose an equality
qualifier. You can choose equal to, not equal to, less than, or greater than a
specific data value.
7 Use the Data softkey to choose the data value for your trigger comparison. This
works in conjunction with the Data is softkey.
8 Optional: The Burst softkey lets you trigger on the Nth frame (1-4096) after an
idle time you select. All trigger conditions must be met for the trigger to occur.
9 If Burst is selected, an idle time (1µs to 10s) can be specified so that the
oscilloscope will look for a trigger condition only after the idle time has past.
Press the Idle softkey and rotate the Entry knob to set an idle time.
If the setup does not produce a stable trigger, the UART/RS232 signals may be slow enough
NOTE
that the oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode
softkey to set the trigger mode from Auto to Normal.
To display UART/RS232 serial decode, see “UART/RS232 Serial Decode"on page515.
NOTE
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |

---
**[Page 514]**

UART/RS232 Triggering and Serial Decode 32
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 515
UART/RS232 Serial Decode
To set up the oscilloscope to capture UART/RS232 signals, see “Setup for
UART/RS232 Signals"on page511.
For UART/RS232 triggering setup see “UART/RS232 Triggering"on page513.
NOTE
To set up UART/RS232 serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 Press Settings.
3 In the UART/RS232 Settings Menu, press the Base softkey to select the base
(hex, binary, or ASCII) in which decoded words are displayed.
• When displaying words in ASCII, the 7-bit ASCII format is used. Valid ASCII
characters are between 0x00 and 0x7F. To display in ASCII you must select
at least 7 bits in the Bus Configuration. If ASCII is selected and the data
exceeds 0x7F, the data is displayed in hex.
• When #Bits is set to 9 in the UART/RS232 Bus Configuration Menu, the 9th
(alert) bit is displayed directly to the left of the ASCII value (which is derived
from the lower 8 bits).
4 Optional: Press the Framing softkey and select a value. In the decode display,
the chosen value will be displayed in light blue. However, if a parity error occurs
the data will be displayed in red.
5 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
| NOTE |
|---|
|  |
|  |  |
|---|---|
|  |  |
|---|---|

---
**[Page 515]**

32 UART/RS232 Triggering and Serial Decode
516 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
6 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
If the setup does not produce a stable trigger, the UART/RS232 signals may be slow enough
NOTE
that the oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode
softkey to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the acquired data.
See Also • “Interpreting UART/RS232 Decode"on page516
• “UART/RS232 Totalizer"on page517
• “Interpreting UART/RS232 Lister Data"on page518
• “Searching for UART/RS232 Data in the Lister"on page518
Interpreting UART/RS232 Decode
| NOTE |
|---|
|  |
|  |
|---|
|  |

---
**[Page 516]**

UART/RS232 Triggering and Serial Decode 32
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 517
• Angled waveforms show an active bus (inside a packet/frame).
• Mid-level blue lines show an idle bus.
• When using 5-8 bit formats, the decoded data is displayed in white (in binary,
hex, or ASCII).
• When using the 9 bit format, all data words are displayed in green, including
the 9th bit. The 9th bit is displayed on the left.
• When a data word value is selected for framing, it is displayed in light blue.
When using 9-bit data words, the 9th bit will also be displayed in light blue.
• Decoded text is truncated at the end of the associated frame when there is
insufficient space within frame boundaries.
• Pink vertical bars indicate you need to expand the horizontal scale (and run
again) to see decode.
• When the horizontal scale setting does not permit the display of all available
decoded data, red dots will appear in the decoded bus to mark the location of
hidden data. Expand the horizontal scale to allow the data to display.
• An unknown (undefined) bus is shown in red.
• A parity error will cause the associated data word to be shown in red, which
includes the 5-8 data bits and the optional 9th bit.
UART/RS232 Totalizer
The UART/RS232 totalizer consists of counters that provide a direct measure of
bus quality and efficiency. The totalizer appears on screen whenever UART/RS232
Decode is ON in the Serial Decode Menu.
The totalizer is running, counting frames and calculating the percentage of error
frames, even when the oscilloscope is stopped (not acquiring data).
The ERR (error) counter is a count of Rx and Tx frames with parity errors. The TX
FRAMES and RX FRAMES counts include both normal frames and frames with
parity errors. When an overflow condition occurs, the counter displays OVERFLOW.
The counters can be reset to zero by pressing the Reset UART Counters softkey in
the UART/RS232 Settings Menu.
|  |
|---|
|  |

---
**[Page 517]**

32 UART/RS232 Triggering and Serial Decode
518 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Interpreting UART/RS232 Lister Data
In addition to the standard Time column, the UART/RS232 Lister contains these
columns:
• Rx — receive data.
• Tx — transmit data.
• Errors — highlighted in red, Parity Error or Unknown Error.
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
Searching for UART/RS232 Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
UART/RS232 data in the Lister. You can use the [Navigate] key and controls to
navigate through the marked rows.
1 With UART/RS232 selected as the serial decode mode, press [Search].
|  |
|---|
|  |

---
**[Page 518]**

UART/RS232 Triggering and Serial Decode 32
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 519
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the UART/RS232 signals are being
decoded.
3 In the Search Menu, press Search; then, select from these options:
• Rx Data — Finds a data byte that you specify. For use when the DUT data
words are from 5 to 8 bits in length (no 9th (alert) bit).
• Rx 1:Data — For use when the DUT data words are 9 bits in length including
the alert bit (the 9th bit). Finds only when the 9th (alert) bit is 1. The
specified data byte applies to the least significant 8 bits (excludes the 9th
(alert) bit)
• Rx 0:Data — For use when the DUT data words are 9 bits in length including
the alert bit (the 9th bit). Finds only when the 9th (alert) bit is 0. The
specified data byte applies to the least significant 8 bits (excludes the 9th
(alert) bit).
• Rx X:Data — For use when the DUT data words are 9 bits in length including
the alert bit (the 9th bit). Finds a data byte that you specify regardless of the
value of the 9th (alert) bit. The specified data byte applies to the least
significant 8 bits (excludes the 9th (alert) bit).
• Similar choices are available for Tx.
• Rx or Tx Parity Error — Finds a parity error based on the parity you have set in
the Bus Configuration Menu.
• Rx or Tx Any Error — Finds any error.
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 519]**

32 UART/RS232 Triggering and Serial Decode
520 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 520]**

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
521
33 USB 2.0 Triggering and
Serial Decode
Setup for USB 2.0 Signals / 521
USB 2.0 Triggering / 523
USB 2.0 Serial Decode / 525
USB 2.0 triggering and serial decode requires:
• Option USF or the DSOX6USBFL upgrade for full/low speed decode.
• Option U2H or the DSOX6USBH upgrade for high speed decode.
Setup for USB 2.0 Signals
To set up the oscilloscope to capture USB 2.0 signals:
1 Press [Serial].
2 Press the Serial softkey, turn the Entry knob to select the desired slot (Serial1 or
Serial2), and press the softkey again to enable decode.
3 Press the Mode softkey; then, select USB trigger type.
4 Press the Speed softkey and specify the speed of the USB signal:
• Low (1.5Mb/s) — requires two single-ended probes.
• Full (12Mb/s) — requires two single-ended probes.
• High (480Mb/s) — requires a differential probe.
Analog channels can be used for any of these speeds. Digital channels can be
used for Low and Full speed only.

---
**[Page 521]**

33 USB 2.0 Triggering and Serial Decode
522 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
5 Press the Signals softkey to open the USB Signals Menu.
6 For both the D+ and D- signals (for low or full speed, similar steps for the single
Source for high speed):
a Connect an oscilloscope channel to the signal in the device under test.
b Press the D+ Source or D- Source softkey; then, turn the Entry knob to select
the channel for the signal.
c Press the corresponding Threshold softkey; then, turn the Entry knob to select
the signal threshold voltage level.
The threshold voltage level is used in decoding, and it will become the
trigger level when the trigger type is set to the selected serial decode slot.
7 Press Auto Setup to automatically set these options for decoding and triggering
on USB signals:
• Low-speed:
• D+/- Source thresholds: 1.4V
• D+/- Source vertical scale: 1.0V/div
• D+/- Source vertical offset: 0.0V
• Horizontal scale: 5µs/div
• Full-speed:
• D+/- Source thresholds: 1.4V
• D+/- Source vertical scale: 1.0V/div
• D+/- Source vertical offset: 0.0V
• Horizontal scale: 500ns/div
• High-speed:
• D+/- Source thresholds: 0.0V
• D+/- Source vertical scale: 200mV/div
• D+/- Source vertical offset: 0.0V
• Horizontal scale: 20ns/div
• Serial Decode: On
|  |  |
|---|---|

---
**[Page 522]**

USB 2.0 Triggering and Serial Decode 33
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 523
• Trigger Mode: currently active serial bus
• USB Trigger Mode: Start of Packet
USB 2.0 Triggering
To set up the oscilloscope to capture USB 2.0 signals, see “Setup for USB 2.0
Signals"on page521.
To trigger on a USB 2.0 signal, connect the oscilloscope to the D+ and D- lines
and set up a trigger condition.
1 Press [Trigger].
2 In the Trigger Menu, press the Trigger softkey; then, turn the Entry knob to
select the serial slot (Serial1 or Serial2) on which the USB 2.0 signals are
being decoded.
3 Press the Trigger softkey and use the Entry knob to select the USB packet,
error, or event to trigger on:
• SOP - Start of Packet — triggers on the sync bit at the beginning of the packet
(low and full speed only).
• EOP - End of Packet — triggers at the end of the SE0 portion of the EOP (low
and full speed only).
• Suspend — triggers when the bus is idle for > 3ms (low and full speed only).
• Resume — triggers when exiting an idle state > 10ms (low and full speed
only).
• Reset — triggers when SE0 is > 10ms (low and full speed only).
• Token Packet — triggers when a token packet with the specified content is
detected.
• Data Packet — triggers when a data packet with the specified content is
detected.
• Handshake Packet — triggers when a handshake packet with the specified
content is detected.
|  |  |
|---|---|

---
**[Page 523]**

33 USB 2.0 Triggering and Serial Decode
524 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• Special Packet — triggers when a special packet with the specified content is
detected.
• All Errors — triggers when any of the following errors are detected.
• PID Error — triggers when the packet type field does not match the check
field.
• CRC5 Error — triggers when a 5 bit CRC error is detected.
• CRC16 Error — triggers when a 16 bit CRC error is detected.
• Glitch Error — triggers when two transitions occur in half a bit time.
• Bit Stuff Error — triggers when > 6 consecutive ones are detected (low and full
speed only).
• SE1 Error — triggers if SE1 > 1 bit time (low and full speed only).
4 If you choose the Token Packet, Data Packet, Handshake Packet, or Special Packet
trigger condition:
a Press the PID softkey to select the desired packet ID for the selected packet
type.
b Press the Base softkey to select the Hex or Binary number base when
displaying or entering USB packet trigger values.
Note that the setting of this softkey does not affect the selected base of the
decode display.
c Press the Bits softkey.
d In the USB Bits Menu, press the Define softkey to select the trigger value to
specify.
e Use the remaining softkeys to specify the value.
For details about using the USB Bits Menu softkeys, press and hold the
softkey in question to display the built-in help.
If the setup does not produce a stable trigger, the USB 2.0 signals may be slow enough that
NOTE
the oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode
softkey to set the trigger mode from Auto to Normal.
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 524]**

USB 2.0 Triggering and Serial Decode 33
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 525
To display USB 2.0 serial decode, see “USB 2.0 Serial Decode"on page525.
NOTE
USB 2.0 Serial Decode
To set up the oscilloscope to capture USB 2.0 signals, see “Setup for USB 2.0
Signals"on page521.
For USB 2.0 triggering setup see “USB 2.0 Triggering"on page523.
NOTE
To set up USB 2.0 serial decode:
1 Press [Serial] to display the Serial Decode Menu.
2 Press the Base for Data softkey to select the base (hex, binary, ASCII, or decimal)
in which decoded data is displayed.
3 If the decode line does not appear on the display, press the [Serial] key to turn it
on.
4 If the oscilloscope is stopped, press the [Run/Stop] key to acquire and decode
data.
If the setup does not produce a stable trigger, the USB 2.0 signals may be slow enough that
NOTE
the oscilloscope is AutoTriggering. Press the [Mode/Coupling] key, then press the Mode
softkey to set the trigger mode from Auto to Normal.
You can use the horizontal Zoom window for easier navigation of the acquired data.
See Also • “Interpreting USB 2.0 Decode"on page526
• “Interpreting USB 2.0 Lister Data"on page528
| NOTE |
|---|
|  |
| NOTE |
|---|
|  |
|  |  |
|---|---|
| NOTE |
|---|
|  |

---
**[Page 525]**

33 USB 2.0 Triggering and Serial Decode
526 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
• “Searching for USB 2.0 Data in the Lister"on page529
Interpreting USB 2.0 Decode
The USB decode display is color coded as follows:
• For Token Packets (all but SOF):
• PID (yellow, "OUT", "IN", "SETUP", "PING")
• PID Check (yellow when valid, red when error detected)
• Address (blue)
• Endpoint (green)
• CRC (blue when valid, red when error detected)
• For Token Packets (SOF):
• PID (yellow, "SOF")
• PID Check (yellow when valid, red when error detected)
• Frame (green) – the frame number
|  |
|---|
|  |

---
**[Page 526]**

USB 2.0 Triggering and Serial Decode 33
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 527
• CRC (blue when valid, red when error detected)
• For Data Packets:
• PID (yellow, "DATA0", "DATA1", "DATA2", "MDATA")
• PID Check (yellow when valid, red when error detected)
• Data (white)
• CRC (blue when valid, red when error detected)
• For Handshake Packets:
• PID (yellow, "ACK", "NAK", "STALL", "NYET", "PRE", "ERR")
• PID Check (yellow when valid, red when error detected)
• For Split Transaction Token Packets:
• PID (yellow, "SPLIT")
• PID Check (yellow when valid, red when error detected)
• Hub Addr (green)
• SC (blue)
• Port (green)
• S & E|U (blue)
• ET (green)
• CRC (blue when valid, red when error detected)
If the packet type is unknown because the PID is off screen, all bytes will be
displayed in orange.

---
**[Page 527]**

33 USB 2.0 Triggering and Serial Decode
528 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide
Interpreting USB 2.0 Lister Data
In addition to the standard Time column, the USB 2.0 Lister contains these
columns:
• PID — PID is displayed as red text if the PID check value does not match.
• Addr — Address.
• Endp — Endpoint.
• Data — either the Data of a Data Packet, or the various fields of a SPLIT packet.
• Fr — Frame – frame number of a SOF packet.
• CRC.
• Errors — "PID", "CRC5", "CRC16", "Glitch", "Stuff" , or "SE1" errors as
appropriate. The background color is red to indicate an error.
Aliased data is highlighted in pink. When this happens, decrease the horizontal
time/div setting and run again.
|  |
|---|
|  |

---
**[Page 528]**

USB 2.0 Triggering and Serial Decode 33
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 529
If the packet type is unknown because the PID is off screen, the Lister text will
have an orange background.
Searching for USB 2.0 Data in the Lister
The oscilloscope's search capability lets you search for (and mark) certain types of
USB 2.0 data in the Lister. You can use the [Navigate] key and controls to navigate
through the marked rows.
1 With USB 2.0 selected as the serial decode mode, press [Search].
2 In the Search Menu, press the Search softkey; then, turn the Entry knob to select
the serial slot (Serial1 or Serial2) on which the USB 2.0 signals are being
decoded.
3 In the Search Menu, press Search for; then, select from these options:
• Token Packet — finds token packets with the specified content.
• Data Packet — finds data packets with the specified content.
• Handshake Packet — finds handshake packets with the specified content.
• Special Packet — finds special packets with the specified content.
• All Errors — finds any of the following errors.
• PID Error — finds packet type fields that do not match the check field.
• CRC5 Error — finds 5 bit CRC errors.
• CRC16 Error — finds 16 bit CRC errors.
• Glitch Error — finds two transitions that occur in half a bit time.
• Bit Stuff Error — finds > 6 consecutive ones (low and full speed only).
• SE1 Error — finds when SE1 > 1 bit time (low and full speed only).
For more information on searching data, see “Searching Lister Data"on page153.
For more information on using the [Navigate] key and controls, see “Navigating the
Time Base"on page77.

---
**[Page 529]**

33 USB 2.0 Triggering and Serial Decode
530 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 530]**

Index
Symbols address with no ack condition, I2C attenuation, probe, 88
trigger, 453 attenuation, probe, external
(-) Width measurement, 263 address, I2C trigger, 453 trigger, 215
(+) Width measurement, 263 AERO license, 407 attenuators, 89
+Width to +Width jitter aliasing, 219 AUDIO license, 407
measurement, 298 aliasing, FFT, 107 Auto Increment, 352
all edges, measure, 293 AUTO Option, 407
Numerics alternating edge trigger, 175 Auto Scale key, 40
AM (amplitude modulation), waveform Auto Setup, FFT, 103
1 M ohm input impedance, 85 generator output, 337 Auto trigger mode, 210
10 MHz REF connector, 60, 375 Amplitude measurement, 253 Auto? trigger indicator, 211
50 ohm input impedance, 85 amplitude modulation (AM), waveform AutoIP, 365, 366
generator output, 337 automatic measurements, 245, 248
A analog channel inputs, 42 automatic setup, 135
analog channel, probe attenuation, 88 AutoProbe interface, 42, 85
About Oscilloscope, 380 analog channel, setup, 81 Autoscale preferences, 372
absolute value math function, 111 analog filters, adjusting, 101 Autoscale, digital channels, 135
AC channel coupling, 84 analysis results, saving, 345 Autoscale, undo, 34
AC RMS - Full Screen Analyze key, 38 Average - Full Screen
measurement, 258 Analyze Segments, 232, 233, 274 measurement, 257
AC RMS - N Cycles measurement, 258 annotation, adding, 160 Average - N Cycles measurement, 257
accessories, 28, 401, 402, 405, 406 antialiasing, disabling/enabling, 163 average measurement trend, 118
acquire, 217, 227 arbitrary generated waveforms, averaged value math function, 115
Acquire key, 38 editing, 327 averaging acquire mode, 223, 227
acquisition memory, 172 arbitrary waveform generator Ax + B math function, 109
acquisition memory, saving, 348 output, 324
acquisition mode, 223 arbitrary waveforms, copying from other B
acquisition mode, averaging, 227 sources, 333
acquisition mode, high resolution, 229 arbitrary waveforms, creating new, 328 Back Up key, 37
acquisition mode, normal, 224 arbitrary waveforms, editing bandwidth, 380
acquisition mode, peak detect, 224 existing, 329 bandwidth limit, 85
acquisition mode, preserve during Area - Full Screen measurement, 270 bandwidth required, oscilloscope, 222
Autoscale, 373 Area - N Cycles measurement, 270 bandwidth, oscilloscope, 219
acquisition modes, 217 ARINC 429 serial decode, 491 bandwidth, realtime sampling, 231
active probes, 87 ARINC 429 totalizer, 494 base 10 exponential math
active serial bus, 438, 457, 467, 478, ARINC 429 trigger, 489 function, 113
517 ARINC 429 words/errors counter, 494 Base measurement, 255
activity indicator, 137 ARINC429 decode, signal speed, 488 beep on events, 371
actual sample rate, 223 ARINC429 decode, signal type, 488 BIN file format, 344
adding digital channels license, 409 ARINC429 decode, word format, 491 binary data (.bin), 409
addition math function, 94 ASCII file format, 344 binary data file examples, 413
ASCII XY data, 347 binary data in MATLAB, 410
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 531

---
**[Page 531]**

Index
binary data, example program for channel, skew, 89 Cursors knob, 41
reading, 413 channel, vertical sensitivity, 83 cursors, binary, 237
binary mode cursors, 237 characteristics, 399 cursors, hex, 237
bit rate measurement, 264 chart logic bus state math cursors, manual, 236
bits, SPI trigger, 465 function, 120 cursors, measure mode, 236
Blackman Harris FFT window, 103 chart logic bus timing math cursors, track waveform, 236
blanking, 72 function, 119
BMP file format, 344 choosing values, 38 D
brick-wall frequency response, 220 cleaning, 380
brightness of waveforms, 37 clear display, 159, 226 D*, 40, 140
Browser Web Control, 385, 386, 387, Clear Display key, 38 d/dt math function, 97
389 clear display, Quick Clear Display, 382 damage, shipping, 27
built-in help, 62 clear persistence, 158 damping factor (second-order PLL),
bursors, gated measurement clock, 373 clock recovery, 123
window, 272 clock recovery, 122 data acquisition mode, 230
burst width measurements, 263 Clock TIE jitter measurement, 296 data sheet, 399
burst, capture signal bursts, 232 CMOS threshold, 139 Data TIE jitter measurement, 295
bus display mode, 140 color grade themes, 290 DC channel coupling, 84
buttons (keys), front panel, 36 color grade waveform, 287 DC offset correction for integrate
BW Limit? in DVM display, 319 color grade waveform, enabling, 288 waveform, 99
common logarithm math function, 111 DC RMS - Full Screen
C COMP license, 407 measurement, 257
compensate passive probes, 35, 42 DC RMS - N Cycles measurement, 258
calibrate probe, 89 Config softkey, 365, 366 DC signals, checking, 211
calibration, 378 connect probes, digital, 131 DC waveform generator output, 325
calibration protect switch, 59, 60 connection, to a PC, 366 dead time (re-arm), 234
calibration status, 395 connectors, rear panel, 59 decaying average approximation, 115
calibration, beep on, 371 constant frequency clock decibels, FFT vertical units, 103
CAN decode, source channels, 420 recovery, 123 decimating samples, 223
CAN FD standard, 422 control, remote, 363 decimation, for measurement
CAN frame counter, 428 controls, front panel, 36 record, 417
CAN serial decode, 426 copyright, 2 decimation, for screen, 417
CAN symbolic data, 422 counter, 320 default configuration, 32
CAN totalizer, 428 Counter measurement, 262 default setup, 32, 356
CAN trigger, 423 counter, ARINC 429 words/errors, 494 Default Setup key, 39
CANFD license, 407 counter, CAN frame, 428 defaults, waveform generator, 341
capture signal bursts, 232 counter, FlexRay frame, 447 delay knob, 67
cardiac waveform generator counter, UART/RS232 frame, 517 Delay measurement, 249, 264
output, 326 coupling, channel, 84 delay time indicator, 75
Center, FFT, 102 coupling, trigger, 211 delayed sweep, 73
channel labels, 165 crosstalk problems, 101 delete file, 366
channel, analog, 81 CSV data, 347 Demo 1 terminal, 42
channel, bandwidth limit, 85 CSV file format, 344 Demo 2 terminal, 42
channel, coupling, 84 CSV files, minimum and maximum depth, AM modulation, 337
channel, fine adjustment, 86 values, 417 deviation, FM modulation, 339
channel, invert, 87 current probes, 405 DHCP, 365, 366
channel, on/off keys, 42 cursor measurements, 235 differential probes, 404
channel, position, 83 cursor units, 238 differentiate math function, 97
channel, probe units, 88 Cursors key, 41 digital bus mode, 140
532 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 532]**

Index
digital channel controls, 40 EEPROM data read, I2C trigger, 453 FFT resolution, 106
digital channel inputs, 60 either edge trigger, 175 FFT spectral leakage, 108
digital channel menu, 138 e-mail setups, images, or data, 352 FFT units, 107
digital channels, 138 e-mail, Quick Email, 382 FFT vertical units, 103
digital channels, Autoscale, 135 EMBD license, 407 FFT window, 102
digital channels, enabling, 409 energy of a pulse, 98 file explorer, 366
digital channels, logic threshold, 139 Entry knob, 38 file format, ASCII, 344
digital channels, probing, 143 Entry knob, push to select, 38 file format, BIN, 344
digital channels, size, 137 envelope math function, 116 file format, BMP, 344
digital display, interpreting, 136 envelope, max/min, 117 file format, CSV, 344
Digital key, 40 equivalent time sampling, 231 file format, PNG, 344
digital probes, 131, 143 erase, secure, 356 File keys, 41
digital probes, impedance, 143 event table, 151 file name, new, 351
digital voltmeter (DVM), 318 expand about, 83, 369 file, save, recall, load, 366
digits, counter resolution, 321 expand about center, 370 filter math function, averaged
Display key, 38 expand about ground, 369 value, 115
display multiple acquisitions, 218 explicit clock recovery, 123 filter math function, envelope, 116
display, area, 61 exponential fall waveform generator filter math function, high pass and low
display, clear, 159 output, 325 pass, 114
display, interpreting, 60 exponential math function, 112 filter math function, smoothing, 115
display, persistence, 157 exponential rise waveform generator filters, math, 113
display, signal detail, 155 output, 325 fine adjustment, channel, 86
display, softkey labels, 62 exporting waveform, 343 fine adjustment, horizontal scale, 74
display, status line, 61 EXT TRIG IN as Z-axis input, 72 firmware updates, 409
displayed channels Autoscale, 373 EXT TRIG IN connector, 43 firmware upgrade files, 395
distortion problems, 101 external memory device, 43 firmware version information, 383
Divide math function, 95 external trigger, 214 firmware versions, 395
DNS IP, 365 external trigger, input impedance, 215 first-order PLL clock recovery, 123
dots or vectors, waveform display, 162 external trigger, input signal flash drive, 43
drag touch gesture, 47 range, 215 Flat top FFT window, 103
dual channel tracking, waveform external trigger, probe FLEX license, 407
generator, 341 attenuation, 215 FlexRay frame counter, 447
dual-channel (N2820A probe) external trigger, probe units, 215 FlexRay serial decode, 445
measurements, 250 FlexRay totalizer, 447
Duty cycle measurement, 263 F FlexRay trigger, 442
duty cycle measurement trend, 119 flick touch gesture, 47
DVM (digital voltmeter), 318 factory default settings, 356 FM (frequency modulation), waveform
DVM limit, beep on, 319, 371 Fall time measurement, 264 generator output, 338
DVMCTR license, 407 fall time measurement trend, 119 folding frequency, 219
Dynamic DNS, 365 falling edges count forcing a trigger, 173
measurements, 269 frame trigger, I2C, 454
E fast debug Autoscale, 372 frame, LIN symbolic, 435
FAT file system format, 368 freeze display, 382
ECL threshold, 139 FAT32 file system format, 368 freeze display, Quick Freeze
edge speeds, 222 FFT aliasing, 107 Display, 382
edge then edge triggering, 176 FFT DC value, 107 French front panel overlays, 45
edge triggering, 174 FFT math function, 101 frequency counter, 321
edges, measure all, 293 FFT measurement hints, 105 frequency deviation, FM
EDK license, 407 FFT peaks, searching, 105 modulation, 339
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 533

---
**[Page 533]**

Index
Frequency measurement, 261 Help key, 41 instantaneous slope of a waveform, 97
frequency measurement trend, 118 help, built-in, 62 Instrument Utilities web page, 394
frequency modulation (FM), waveform hex bus trigger, 183 Integrate math function, 98
generator output, 338 hex mode cursors, 237 intensity color grade scheme, 290
frequency peaks, searching, 105 HF Reject, 213 intensity control, 155
frequency requirements, power high pass filter math function, 114 Intensity key, 37
source, 30 high-frequency noise rejection, 213 interpolate, arbitrary waveform
frequency, Nyquist, 219 high-resolution mode, 223, 229 option, 328
frequency-shift keying modulation histogram, 277 invert graticule colors, 346
(FSK), waveform generator histogram graph, 283 invert waveform, 87
output, 340 histogram statistics, 284 IP address, 365, 383
front panel controls and connectors, 36 histogram, measurement, 278, 282 Italian front panel overlays, 45
front panel self test, 379 holdoff, 214
front panel, full scope remote, 386 hop frequency, FSK modulation, 340 J
front panel, language overlay, 43 Horiz key, 39, 65, 70, 73, 227
front panel, screen only remote, 387 Horizontal controls, 39, 69 Japanese front panel overlays, 45
front panel, tablet remote, 388 horizontal Navigate key, 39 jitter analysis, 291
FSK (frequency-shift keying horizontal position control, 39 Jitter analysis measurements, 250
modulation), waveform generator horizontal position knob, 67 jitter analysis, setting up, 292
output, 340 horizontal scale fine adjustment, 74 Jitter key, 38
Full Scope Remote Front Panel, 386 horizontal Search key, 39 JITTER license, 407
horizontal sweep speed control, 39 jitter measurements, 295
G horizontal time/div control, 39 Jitter-Free Trigger, 373
horizontal Zoom key, 39
gated by cursors measurement host name, 365, 383 K
window, 272 Host name softkey, 366
gateway IP, 365 keys, front panel, 36
Gaussian frequency response, 220 I Keysight IO Libraries Suite, 390
Gaussian pulse waveform generator knobs, front panel, 36
output, 326 I/O interface settings, 363 Korean front panel overlays, 45
Generic video trigger, 197 I2C serial decode, 456 ksx files, 367
German front panel overlays, 45 I2C trigger, 452
glitch capture, 225 I2S serial decode, 477 L
glitch trigger, 178 I2S trigger, 474
golden waveform test, 303 identification function, web Label key, 42
grabber, 133 interface, 394 label list, 169
graph, histogram, 283 idle serial bus, 438, 457, 467, 478, label list, loading from text file, 168
graphical user interface language, 63 517 labels, 165
graticule intensity, 159 Imped softkey, 85 labels, auto-increment, 168
graticule type, 159 impedance, digital probes, 143 labels, reset library, 169
grid intensity, 159 increment statistics, 274 LAN connection, 365
grid type, 159 indeterminate state, 237 LAN interface, remote control, 363
ground level, 82 InfiniiMax probes, 87 LAN port, 60
Ground terminal, 42 infinite persistence, 158, 218, 225 LAN Settings softkey, 365, 366
information area, 62 landscape mode, 360
H input impedance, analog channel language, user interface and Quick
input, 85 Help, 63
Hanning FFT window, 103 installed licenses, 380 length control, 348
hardware self test, 379 installed options, 395 length softkey, 347
534 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 534]**

Index
level, trigger, 172 math, offset, 93 Modify softkey, 366
LF Reject, 212 math, scale, 93 modulation, waveform generator
library, labels, 167 math, subtract, 94 output, 336
licenses, 407, 409 math, units, 93 module installed, 380
LIN serial decode, 436 math, using waveform math, 91 MSO, 4
LIN symbolic data, 433 MATLAB binary data, 410 MSO feature upgrade, 409
LIN trigger, 434 max envelope, 117 MSO license, 408
line voltage, 30 max hold math function, 117 Multicast DNS, 365
Lister, 151 Maximum measurement, 253 multiplexed position knob, 40
load file, 366 maximum sample rate, 223 multiplexed scale knob, 40
Load from, 351 Meas key, 41, 245 Multiply math function, 95
localized front panel overlay, 43 measure all edges, 293
Location, 351 Measure controls, 41 N
Location, File Explorer softkey measure mode cursors, 236
label, 368 measure statistics, quick reset, 382 N2820A high-sensitivity current
logging remote commands, 377 measure, Quick Measure All, 382 probe, 250
logic presets, waveform generator, 335 measurement category, N8900A Infiniium Offline oscilloscope
logic threshold, 139 definitions, 400 analysis software, 344
long save, beep on, 371 measurement definitions, 248 natural logarithm math function, 112
loop bandwidth (PLL), clock measurement histogram, 278, 282 navigate files, 366
recovery, 123 measurement record, 348 Navigate key, 39
low pass filter math function, 114 measurement statistics, 272 navigating the time base, 77
low-frequency noise rejection, 212 measurement thresholds, 270 negative pulse width measurement
measurement trend math function, 118 trend, 119
M measurement window, 272 network configuration parameters, 383
measurements, 248 network printer connection, 359
magnify math function, 116 measurements, automatic, 245 network, connecting to, 365
mask failure, beep on, 371 measurements, delay, 249 new label, 167
mask files, recall, 354 measurements, jitter, 295 noise rejection, 213
MASK license, 407 measurements, overshoot, 249 noise waveform generator output, 325
mask statistics, quick reset, 382 measurements, phase, 249 noise, adding to waveform generator
mask test, trigger output, 307, 374 measurements, preshoot, 249 output, 335
mask testing, 303 measurements, time, 259 noise, high-frequency, 213
mask, TRIG OUT signal, 374 measurements, voltage, 252 noise, low-frequency, 212
math filters, 113 MegaZoom IV, 4 noisy signals, 209
math functions, cascaded, 92 mem4M, 407 nominal data rate, clock recovery, 123
Math key, 40 memory depth and sample rate, 223 non-volatile memory, secure
math operators, 94 memory, segmented, 232 erase, 356
math transforms, 96 menu line, 62 normal acquire mode, 224
math visualizations, 116 message, CAN symbolic, 425 normal mode, 223, 224
math, 1*2, 95 MIL-STD-1553 serial decode, 484 Normal trigger mode, 210
math, 1/2, 95 MIL-STD-1553 trigger, 483 notices, 2
math, addition, 94 min envelope, 117 N-Period jitter measurement, 296
math, differentiate, 97 min hold math function, 117 Nth edge burst trigger, 187
math, divide, 95 Minimum measurement, 253 Nth edge burst triggering, 187
math, FFT, 101 missing acknowledge condition, I2C number of negative pulses
math, functions, 91 trigger, 453 measurements, 268
math, integrate, 98 Mode/Coupling key, trigger, 209 number of positive pulses
math, multiply, 95 model number, 380, 383 measurements, 268
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 535

---
**[Page 535]**

Index
Nyquist frequency, 107 pollution degree, definitions, 401 probes, passive, compensating, 35
Nyquist sampling theory, 219 Portuguese front panel overlays, 45 probes, single-ended active, 403
position digital channels, 139 programmer's guide, 391
O position knob, 139 pulse polarity, 179
position, analog, 83 pulse waveform generator output, 325
offset (DC) correction for integrate positive pulse width measurement pulse width trigger, 178
waveform, 99 trend, 119 PWR license, 408
operators, math, 94 post-processing, 246
options, print, 360 post-trigger information, 68 Q
OR trigger, 184 Power App measurements, 250
oscilloscope bandwidth, 219 power consumption, 30 qualifier, pulse width, 180
oscilloscope bandwidth required, 222 power cord connector, 59 Quick Action key, 41, 381
oscilloscope rise time, 221 power requirements, 30 Quick Clear Display, 382
oscilloscope sample rate, 221 power supply, 59 Quick Email, 382
output load expected, waveform power switch, 31, 37 Quick Freeze Display, 382
generator, 334 power-on, 30 Quick Help, 62
output, trigger, 374 precision analysis record, 348 Quick Help language, 63
overlay, localized, 43 precision measurements and Quick Mask Statistics Reset, 382
Overshoot measurement, 249, 255 math, 275 Quick Measure All, 382
overvoltage category, 401 precision measurements, jitter analysis Quick Measure Statistics Reset, 382
and, 292 Quick Print, 382
P predefined labels, 166 Quick Recall, 382
Preshoot measurement, 249, 256 Quick Save, 382
palette, 346 Press to go, 351 Quick Trigger Mode, 382
pan and zoom, 66 Press to go, File Explorer softkey
passive probes, 87, 402 label, 368 R
passive probes, compensating, 35 pre-trigger information, 68
password (network), reset, 398 print, 382 ramp waveform generator output, 325
password (network), setting, 397 Print key, 41 random noise, 209
pattern trigger, 181 print options, 360 range, external trigger input, 215
pattern, SPI trigger, 465 print screen, 357 ratio measurement, 259
PC connection, 366 print, landscape, 360 ratio measurement trend, 118
peak detect mode, 223, 224, 225 print, Quick Print, 382 ratio X cursor units, 238
Peak-peak measurement, 253 printer, USB, 43, 357 ratio Y cursor units, 238
period counter, 321 printing the display, 357 raw acquisition record, 348
Period measurement, 260 probe attenuation, 88 real-time eye analysis, 299
period measurement trend, 118 probe attenuation, external Real-Time Eye analysis
Period-Period jitter measurement, 297 trigger, 215 measurements, 250
persistence, 157 probe compensation, 42 realtime sampling and oscilloscope
persistence, clearing, 158 probe head, 89 bandwidth, 231
persistence, infinite, 218 probe units, 88 realtime sampling option, 230
Phase measurement, 249, 265 probe, AutoProbe interface, 42 rear panel connectors, 59
phase of frequency-tracked waveform probe, calibrate, 89 re-arm time, 234
generator output, 341 probes, 401, 402, 405, 406 recall, 382
phase X cursor units, 238 probes, connecting to oscilloscope, 31 recall files via web interface, 392
pinch touch gesture, 47 probes, current, 405 recall mask files, 354
PNG file format, 344 probes, differential, 404 recall setups, 354
point-to-point connection, 366 probes, digital, 131 recall, Quick Recall, 382
pollution degree, 401 probes, passive, 402 recovery, clock, 122
536 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 536]**

Index
rectangle draw mode, 46 Save to, 351 setup, default, 32
Rectangular FFT window, 103 save, Quick Save, 382 setups, recall, 354
Ref key, 40, 127 save/recall from web interface, 391 shipping damage, 27
reference point, waveform, 369 Save/Recall key, 41 shipping precautions, 381
reference signal mode, 375 saver, screen, 371 sidebar, 49
reference waveforms, 127 saving data, 343 Sigma, minimum, 306
remote commands, logging, 377 SCL, I2C trigger, 452 signal, CAN symbolic, 425
remote control, 363 SCLK, I2S trigger, 472 signal, LIN symbolic, 435
Remote Front Panel, 389 SCPI Commands window, 389 Simplified Chinese front panel
remote programming, Keysight IO screen image via web interface, 393 overlays, 45
Libraries, 390 Screen Only Remote Front Panel, 387 sinc waveform generator output, 325
remote programming, web screen saver, 371 sine waveform generator output, 325
interface, 389 SDA, 451 single acquisition, 39
required oscilloscope bandwidth, 222 SDA, I2C trigger, 452 Single key, 217
reset label library, 169 Search key, 39 single, beep on, 371
reset network password, 398 second-order PLL clock recovery, 123 single-ended active probes, 403
restart condition, I2C trigger, 453 secure erase, 356 single-shot acquisitions, 211
return instrument for service, 381 segmented memory, 232 single-shot events, 218
Rise time measurement, 264 segmented memory, re-arm time, 234 size, 137
rise time measurement trend, 119 segmented memory, saving skew, analog channel, 89
rise time, oscilloscope, 221 segments, 347 slope trigger, 174
rise time, signal, 222 segmented memory, statistical smoothing math function, 115
rise/fall time triggering, 185 data, 233 Snapshot All measurements, 251
rising edge count measurements, 269 select digital channels, 139 snapshot all, quick action, 382
RML license, 408 select knob, 139 softkey labels, 62
RMS - AC measurement trend, 118 Selected, File Explorer softkey softkeys, 7, 37
roll mode, 69 label, 368 software updates, 409
RS232 trigger, 513 selecting, values, 38 software version, 380
Run Control keys, 39 self test, front panel, 379 Span, FFT, 102
runt pulses, 260 self test, hardware, 379 Spanish front panel overlays, 45
runt triggering, 188 SENSOR license, 408 speaker options, 370
Russian front panel overlays, 45 SENT data, searching, 509 specifications, 399
SENT decode, interpreting, 505 spectral leakage, FFT, 108
S SENT decode, signal setup, 497 SPI serial decode, 466
SENT fast signals definition, 500 SPI trigger, 464
safety warning, 32 SENT Lister data, 507 square math function, 110
sample rate, 3 SENT serial decode, 504 square root, 109
sample rate and memory depth, 223 SENT trigger, 502 square waveform generator
sample rate, current rate displayed, 66 serial clock, I2C trigger, 452 output, 325
sample rate, oscilloscope, 220, 221 serial clock, I2S trigger, 472 square waves, 220
sampling theory, 219 serial data, 451 stand-alone connection, 366
sampling, overview, 218 serial data, I2C trigger, 452 start acquisition, 39
saturated color grade, 288 serial decode controls, 40 start condition, I2C, 453
save, 382 Serial key, 40 Start Freq, FFT, 102
save file, 366 serial number, 380, 383 state logic bus chart, 120
save files via web interface, 391 service functions, 378 statistics, histogram, 284
save segment, 347 setup and hold triggering, 191 statistics, increment, 274
save setup files, 345 setup files, saving, 345 statistics, mask test, 308
save times, data, 349 setup, automatic, 135 statistics, measurement, 272
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 537

---
**[Page 537]**

Index
statistics, using segmented TRIG OUT connector, 59, 374 trigger, mode/coupling, 209
memory, 233 TRIG OUT signal and zone qualified trigger, source, 174
status line, 61 trigger, 208 trigger, zone qualified, 206
status, User Cal, 380 Trig'd trigger indicator, 211 triggers, TRIG OUT signal, 374
Std Deviation measurement, 258 Trig'd? trigger indicator, 211 TTL threshold, 139
stop acquisition, 39 Trigger controls, 39 turn channel on, 42
stop condition, I2C, 453 trigger coupling, 211
Stop Freq, FFT, 102 trigger indicator, Auto?, 211 U
storage locations, navigate, 351 trigger indicator, Trig'd, 211
subnet mask, 365 trigger indicator, Trig'd?, 211 U2H license, 408
subtract math function, 94 trigger level, 172 UART totalizer, 517
symbolic data, CAN, 422 trigger mode, auto or normal, 210 UART trigger, 513
symbolic data, LIN, 433 trigger mode, Quick Trigger Mode, 382 UART/RS232 frame counter, 517
sync pulse, waveform generator, 334 trigger output, 374 UART/RS232 license, 407
trigger output, mask test, 307, 374 UART/RS232 serial decode, 515
T trigger qualified event signal, under-sampled signals, 219
counting, 321 units, cursor, 238
Tablet Remote Front Panel, 388 trigger type, ARINC 429, 489 units, external trigger probe, 215
temperature color grade scheme, 290 trigger type, CAN, 423 units, math, 93
template, front panel, 43 trigger type, edge, 174 units, probe, 88
test, mask, 303 trigger type, edge then edge, 176 updating software and firmware, 409
themes, color grade, 290 trigger type, FlexRay, 442 upgrade files, 395
theory, sampling, 219 trigger type, glitch, 178 upgrade options, 407
threshold, analog channel trigger type, hex bus, 183 upgrading the oscilloscope, 409
measurements, 270 trigger type, I2C, 452 upload new firmware, 383
threshold, digital channels, 139 trigger type, I2S, 474 usb, 369
thumb drive, 43 trigger type, LIN, 434 USB 2.0 serial decode, 525
tilt for viewing, 30 trigger type, MIL-STD-1553, 483 USB 2.0 trigger, 523
time measurements, 259 trigger type, Nth edge burst, 187 USB decode, signal speed, 521
time reference indicator, 75 trigger type, OR, 184 USB device port, 60
time, re-arm, 234 trigger type, pattern, 181 USB device port, remote control, 363
timebase, 69 trigger type, pulse width, 178 USB host port, 60, 357
times for saving data, 349 trigger type, rise/fall time, 185 USB host ports, 43
timing logic bus chart, 119 trigger type, RS232, 513 USB printer, 357
Tools keys, 41 trigger type, runt, 188 USB printers, supported, 357
Top measurement, 254 trigger type, SENT, 502 USB storage device, 43
totalize counter, 321 trigger type, setup and hold, 191 USB, CD device, 369
totalizer, ARINC 429, 494 trigger type, slope, 174 USB, eject device, 43
totalizer, CAN, 428 trigger type, SPI, 464 USB, storage device numbering, 369
totalizer, FlexRay, 447 trigger type, UART, 513 usb2, 369
totalizer, UART/rs232, 517 trigger type, USB 2.0, 523 USBSQ license, 408
Touch key, 42, 45 trigger type, video, 192 user cal, 378
touchscreen controls, 45 trigger types, 171 user calibration, 378
tracking cursors, 236 trigger, beep on, 371 user interface language, 63
Traditional Chinese front panel trigger, definition, 172 User-defined threshold, 139
overlays, 45 trigger, external, 214 USF license, 408
transforms, math, 96 trigger, forcing a, 173 utilities, 363
transient withstand capability, 400 trigger, general information, 172 Utility key, 41
Transparent backgrounds, 370 trigger, holdoff, 214
538 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 538]**

Index
V waveform, cursor tracking, 236
waveform, intensity, 155
V RMS, FFT vertical units, 103 waveform, printing, 357
values, choosing, 38 waveform, reference point, 369
variable persistence, 158 waveform, saving/exporting, 343
vectors or dots, waveform display, 162 WAVEGEN license, 408
ventilation requirements, 30 web interface, 383
Vertical controls, 42 web interface, accessing, 384
vertical expansion, 83 white noise, adding to waveform
vertical offset, 83 generator output, 335
vertical position, 83 Width - measurement, 263
vertical position knobs, 42 Width + measurement, 263
vertical scale knobs, 42 -Width to -Width jitter
vertical sensitivity, 42, 83 measurement, 298
Vertical Units, FFT, 103 Window, FFT, 102
VGA video output, 60 write data with no ack condition, I2C
VID license, 408 trigger, 453
video trigger, 192
video trigger, custom Generic, 197
X
viewing, tilt the instrument, 30
VISA connect string, 383 X at Max Y measurement, 267
visualizations, math, 116 X at Max Y on FFT, 250
voice control, 370 X at Min Y measurement, 267
voice recognition, 58 X at Min Y on FFT, 250
voltage measurements, 252 XY mode, 69, 70
W Z
warranted specifications, 399 Z-axis blanking, 72
warranty, 2, 380 zone qualified trigger, 206
Wave Gen1/2 keys, 41, 43 zoom and pan, 66
waveform generator, 323 zoom display measurement
waveform generator defaults, window, 272
restoring, 341 Zoom key, 39
waveform generator dual channel
tracking, 341
waveform generator expected output
load, 334
waveform generator logic presets, 335
waveform generator sync pulse, 334
waveform generator sync pulse, TRIG
OUT signal, 374
waveform generator, arbitrary
waveforms, 327
waveform generator, waveform
type, 323
Waveform keys, 38
waveform type, waveform
generator, 323
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 539

---
**[Page 539]**

Index
540 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

---
**[Page 540]**
