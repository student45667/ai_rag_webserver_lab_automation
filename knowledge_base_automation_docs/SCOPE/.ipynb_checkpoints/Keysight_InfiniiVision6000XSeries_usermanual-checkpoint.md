# Keysight_InfiniiVision6000XSeries_usermanual

**Source PDF:** `Keysight_InfiniiVision6000XSeries_usermanual.pdf`

**Extracted:** 1779774186.1557028

---

## Page 1

Keysight InfiniiVision

### 6000 X-Series Oscilloscopes

User's Guide

## Page 2


### 2 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide

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

### 2.101, pursuant to FAR 12.211 and 27.404.2

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

### 227.7202, the U.S. government acquires A CAUTION notice denotes a hazard.

Printed in Malaysia commercial computer software under the
It calls attention to an operating
Published by: same terms by which the software is
procedure, practice, or the like that,
Keysight Technologies, Inc. customarily provided to the public.

### 1900 Garden of the Gods Road Accordingly, Keysight provides the Software if not correctly performed or

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

### WARNING

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

### connection with the furnishing, use, or commercial computer software

### performance of this document or of any documentation. No additional government notice until the indicated

information contained herein. Should requirements beyond those set forth in the conditions are fully understood and
Keysight and the user have a separate EULA shall apply, except to the extent that met.
written agreement with warranty terms those terms, rights, or licenses are explicitly
covering the material in this document that required from all providers of commercial
conflict with these terms, the warranty computer software pursuant to the FAR and

### Tables on this Page

## Page 3

Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide 3
InfiniiVision 6000 X-Series Oscilloscopes—At a Glance

### Table 1 6000 X-Series Model Numbers, Bandwidths, Sample Rates

Model Analog Digital Bandwidth Options Sample Rate (interleaved,
Channels Channels non-interleaved)
DSO-X 6002A 2 • (none) = 1 GHz 20 GSa/s, 10 GSa/s
• BW250 = 2.5 GHz

### DSO-X 6004A 4

• BW400 = 4 GHz
MSO-X 6002A 2 16 • BW600 = 6 GHz

### MSO-X 6004A 4 16

The Keysight InfiniiVision 6000 X-Series oscilloscopes deliver these features:
• 1 GHz, 2.5 GHz, 4 GHz, and 6 GHz bandwidth options.

### Tables on this Page

| Model | Analog Channels | Digital Channels | Bandwidth Options | Sample Rate (interleaved, non-interleaved) |
|---|---|---|---|---|
| DSO-X 6002A | 2 |  | • (none) = 1 GHz • BW250 = 2.5 GHz • BW400 = 4 GHz • BW600 = 6 GHz | 20 GSa/s, 10 GSa/s |
| DSO-X 6004A | 4 |  |  |  |
| MSO-X 6002A | 2 | 16 |  |  |
| MSO-X 6004A | 4 | 16 |  |  |

## Page 4


### 4 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide

• 2- and 4-channel digital storage oscilloscope (DSO) models.
• 2+16-channel and 4+16-channel mixed-signal oscilloscope (MSO) models.
An MSO lets you debug your mixed-signal designs using analog signals and
tightly correlated digital signals simultaneously. The 16 digital channels have a

### 1 GSa/s sample rate, with a 250 MHz toggle rate.

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

### example, to view cursor values and measurements at the same time.

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

## Page 5

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

## Page 6


### 6 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide

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

### Tables on this Page

| When unpacking and using the oscilloscope for the first time, see: | • Chapter 1, “Getting Started,” starting on page 27 |
|---|---|
| When displaying waveforms and acquired data, see: | • Chapter 2, “Horizontal Controls,” starting on page 65 • Chapter 3, “Vertical Controls,” starting on page 81 • Chapter 4, “Math Waveforms,” starting on page 91 • Chapter 5, “Reference Waveforms,” starting on page 127 • Chapter 6, “Digital Channels,” starting on page 131 • Chapter 7, “Serial Decode,” starting on page 149 • Chapter 8, “Display Settings,” starting on page 155 • Chapter 9, “Labels,” starting on page 165 |
| When setting up triggers or changing how data is acquired, see: | • Chapter 10, “Triggers,” starting on page 171 • Chapter 11, “Trigger Mode/Coupling,” starting on page 209 • Chapter 12, “Acquisition Control,” starting on page 217 |
| Making measurements and analyzing data: | • Chapter 13, “Cursors,” starting on page 235 • Chapter 14, “Measurements,” starting on page 245 • Chapter 15, “Histogram,” starting on page 277 • Chapter 16, “Color Grade Waveform,” starting on page 287 • Chapter 17, “Jitter and Real-Time Eye Analysis,” starting on page 291 • Chapter 18, “Mask Testing,” starting on page 303 • Chapter 19, “Digital Voltmeter and Counter,” starting on page 317 |
| When using the built-in license enabled waveform generator, see: | • Chapter 20, “Waveform Generator,” starting on page 323 |
| When saving, recalling, or printing, see: | • Chapter 21, “Save/Email/Recall (Setups, Screens, Data),” starting on page 343 • Chapter 22, “Print (Screens),” starting on page 357 |
| When using the oscilloscope's utility functions or web interface, see: | • Chapter 23, “Utility Settings,” starting on page 363 • Chapter 24, “Web Interface,” starting on page 383 |

## Page 7

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

### NOTE

Instructions for pressing a series of keys are written in an abbreviated manner. Instructions for
pressing [Key1], then pressing Softkey2, then pressing Softkey3 are abbreviated as follows:
Press [Key1] > Softkey2 > Softkey3.
The keys may be a front panel [Key] or a Softkey. Softkeys are the six keys located directly
below the oscilloscope display.

### Tables on this Page

| For reference information, see: | • Chapter 25, “Reference,” starting on page 399 |
|---|---|
| When using licensed serial bus triggering and decode features, see: | • Chapter 26, “CAN/LIN Triggering and Serial Decode,” starting on page 419 • Chapter 27, “FlexRay Triggering and Serial Decode,” starting on page 441 • Chapter 28, “I2C/SPI Triggering and Serial Decode,” starting on page 451 • Chapter 29, “I2S Triggering and Serial Decode,” starting on page 471 • Chapter 30, “MIL-STD-1553/ARINC 429 Triggering and Serial Decode,” starting on page 481 • Chapter 31, “SENT Triggering and Serial Decode,” starting on page 497 • Chapter 32, “UART/RS232 Triggering and Serial Decode,” starting on page 511 • Chapter 33, “USB 2.0 Triggering and Serial Decode,” starting on page 521 |

| NOTE |
|---|
|  |

## Page 8


### 8 Keysight InfiniiVision 6000 X-Series Oscilloscopes User's Guide


## Page 9

Contents
InfiniiVision 6000X-Series Oscilloscopes—At a Glance / 3
In This Guide / 6

### 1 Getting Started

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

### Tables on this Page

## Page 10

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

### 2 Horizontal Controls

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

### 10 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 11

To copy search setups / 76
Navigating the Time Base / 77
To navigate time / 77
To navigate search events / 78
To navigate segments / 78

### 3 Vertical Controls

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

### 4 Math Waveforms

To display math waveforms / 91
To adjust the math waveform scale and offset / 93
Units for Math Waveforms / 93
Math Operators / 94
Add or Subtract / 94
Multiply or Divide / 95
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 11

## Page 12

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

### Measurement Trend / 118

Chart Logic Bus Timing / 119
Chart Logic Bus State / 120
Clock Recovery / 122
The Measurement Record and Waveform Math / 123

### 5 Reference Waveforms

To save a waveform to a reference waveform location / 127
To display a reference waveform / 128
To scale and position reference waveforms / 129
To adjust reference waveform skew / 130

### 12 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 13

To display reference waveform information / 130
To save/recall reference waveform files to/from a USB storage
device / 130

### 6 Digital Channels

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

### 7 Serial Decode

Serial Decode Options / 149
Lister / 151
Searching Lister Data / 153
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 13

### Tables on this Page

## Page 14


### 8 Display Settings

To adjust waveform intensity / 155
To set or clear persistence / 157
To clear the display / 159
To select the grid type / 159
To adjust the grid intensity / 159
To add an annotation / 160
To display waveforms as vectors or dots / 162
To disable/enable antialiasing / 163
To freeze the display / 164

### 9 Labels

To turn the label display on or off / 165
To assign a predefined label to a channel / 166
To define a new label / 167
To load a list of labels from a text file you create / 168
To reset the label library to the factory default / 169

### 10 Triggers

Adjusting the Trigger Level / 172
Forcing a Trigger / 173
Edge Trigger / 174
Edge then Edge Trigger / 176
Pulse Width Trigger / 178
Pattern Trigger / 181
Hex Bus Pattern Trigger / 183

### 14 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 15

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

### 11 Trigger Mode/Coupling

To select the Auto or Normal trigger mode / 210
To select the trigger coupling / 211
To enable or disable trigger noise rejection / 213
To enable or disable trigger HF Reject / 213
To set the trigger holdoff / 214
External Trigger Input / 214
Maximum voltage at oscilloscope external trigger input / 215

### 12 Acquisition Control

Running, Stopping, and Making Single Acquisitions (Run
Control) / 217
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 15

### Tables on this Page

## Page 16

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

### Measurements, Statistics, and Infinite Persistence with

Segmented Memory / 233
Segmented Memory Re-Arm Time / 234
Saving Data from Segmented Memory / 234

### 13 Cursors

To make cursor measurements / 236
Cursor Examples / 239

### 14 Measurements

To make automatic measurements / 246

### Measurements Summary / 248

Snapshot All / 251
Voltage Measurements / 252

### 16 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 17

Peak-Peak / 253
Maximum / 253
Minimum / 253
Amplitude / 253
Top / 254
Base / 255
Overshoot / 255
Preshoot / 256
Average / 257

### DC RMS / 257

### AC RMS / 258

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

## Page 18

Mixed Measurements / 269
Area / 269

### Measurement Thresholds / 270

### Measurement Window / 272

### Measurement Statistics / 272

Precision Measurements and Math / 275

### 15 Histogram

Waveform Histogram Set Up / 278
Defining the Histogram Limits Window / 280

### Measurement Histogram Set Up / 282

Histogram Data Graph / 283
Histogram Data Statistics / 284

### 16 Color Grade Waveform

Enabling a Color Grade Waveform / 288
Color Grade Themes / 290

### 17 Jitter and Real-Time Eye Analysis

Setting Up Jitter Analysis / 292
Jitter Measurements / 295
Data TIE / 295
Clock TIE / 296
N-Period / 296
Period-Period / 297
+Width to +Width / 298
-Width to -Width / 298
Real-Time Eye Analysis / 299

### 18 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 19


### 18 Mask Testing

To create a mask from a "golden" waveform (Automask) / 303
Mask Test Setup Options / 305
Mask Statistics / 308
To manually modify a mask file / 309
Building a Mask File / 312
How is mask testing done? / 315

### 19 Digital Voltmeter and Counter

Digital Voltmeter / 318
Counter / 320

### 20 Waveform Generator

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

## Page 20


### 21 Save/Email/Recall (Setups, Screens, Data)

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

### 22 Print (Screens)

To print the oscilloscope's display / 357
To set up network printer connections / 359
To specify the print options / 360
To specify the palette option / 361

### 23 Utility Settings

I/O Interface Settings / 363

### 20 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 21

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

### Tables on this Page

## Page 22


### 24 Web Interface

Accessing the Web Interface / 384
Browser Web Control / 385
Full Scope Remote Front Panel / 386
Screen Only Remote Front Panel / 387

### Tablet Remote Front Panel / 388

Remote Programming via the Web Interface / 389
Remote Programming with Keysight IO Libraries / 390
Save/Recall / 391
Saving Files via the Web Interface / 391
Recalling Files via the Web Interface / 392
Get Image / 393
Identification Function / 394
Instrument Utilities / 394
Setting a Password / 397

### 25 Reference

### Specifications and Characteristics / 399

### Measurement Category / 399

Oscilloscope Measurement Category / 400

### Measurement Category Definitions / 400

Transient Withstand Capability / 400
Maximum input voltage at analog inputs / 400
Maximum input voltage at digital channels / 401
Environmental Conditions / 401
Probes and Accessories / 401
Passive Probes / 402

### 22 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


### Tables on this Page

## Page 23

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

### Example Program for Reading Binary Data / 413

### Examples of Binary Files / 413

CSV and ASCII XY files / 416
CSV and ASCII XY file structure / 417
Minimum and Maximum Values in CSV Files / 417
Acknowledgements / 418

### 26 CAN/LIN Triggering and Serial Decode

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

## Page 24

Loading and Displaying LIN Symbolic Data / 433
LIN Triggering / 434
LIN Serial Decode / 436
Interpreting LIN Decode / 438
Interpreting LIN Lister Data / 439
Searching for LIN Data in the Lister / 440

### 27 FlexRay Triggering and Serial Decode

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

### 28 I2C/SPI Triggering and Serial Decode

Setup for I2C Signals / 451
I2C Triggering / 452
I2C Serial Decode / 456
Interpreting I2C Decode / 457
Interpreting I2C Lister Data / 459
Searching for I2C Data in the Lister / 459
Setup for SPI Signals / 460
SPI Triggering / 464
SPI Serial Decode / 466

### 24 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 25

Interpreting SPI Decode / 467
Interpreting SPI Lister Data / 468
Searching for SPI Data in the Lister / 469

### 29 I2S Triggering and Serial Decode

Setup for I2S Signals / 471
I2S Triggering / 474
I2S Serial Decode / 477
Interpreting I2S Decode / 478
Interpreting I2S Lister Data / 479
Searching for I2S Data in the Lister / 480

### 30 MIL-STD-1553/ARINC429 Triggering and Serial Decode

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

### 31 SENT Triggering and Serial Decode

Setup for SENT Signals / 497
SENT Triggering / 502
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 25

## Page 26

SENT Serial Decode / 504
Interpreting SENT Decode / 505
Interpreting SENT Lister Data / 507
Searching for SENT Data in the Lister / 509

### 32 UART/RS232 Triggering and Serial Decode

Setup for UART/RS232 Signals / 511
UART/RS232 Triggering / 513
UART/RS232 Serial Decode / 515
Interpreting UART/RS232 Decode / 516
UART/RS232 Totalizer / 517
Interpreting UART/RS232 Lister Data / 518
Searching for UART/RS232 Data in the Lister / 518

### 33 USB 2.0 Triggering and Serial Decode

Setup for USB 2.0 Signals / 521
USB 2.0 Triggering / 523
USB 2.0 Serial Decode / 525
Interpreting USB 2.0 Decode / 526
Interpreting USB 2.0 Lister Data / 528
Searching for USB 2.0 Data in the Lister / 529
Index

### 26 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide


## Page 27

Keysight InfiniiVision 6000X-Series Oscilloscopes
User's Guide
27

### 1 Getting Started

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

## Page 28


### 1 Getting Started

### 28 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

• Verify that you received the following items and any optional accessories you
may have ordered:
• InfiniiVision 6000X-Series oscilloscope.
• Power cord (country of origin determines specific type).
• Oscilloscope probes:
• Two probes for 2-channel models.
• Four probes for 4-channel models.
• Digital probe kit (MSO models only).
• Documentation CD-ROM.

## Page 29

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 29
InfiniiVision 6000 X-Series oscilloscope
N2894A probes
(Qty 2 or 4)
Documentation CD
Power cord
(Based on country
of origin)

### N2756-60001

Digital Probe Kit
(MSO models only)
See Also • “Accessories Available"on page405

### Tables on this Page

| InfiniiVision 6000 X-Series oscilloscope N2894A probes (Qty 2 or 4) Documentation CD Power cord (Based on country of origin) N2756-60001 Digital Probe Kit (MSO models only) |
|---|
|  |

## Page 30


### 1 Getting Started

### 30 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

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

## Page 31

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 31
When using the oscilloscope in a bench-top setting, provide at least 2" clearance
at the sides and 4" (100mm) clearance above and behind the oscilloscope for
proper cooling.
To power-on the 1 Connect the power cord to the rear of the oscilloscope, then to a suitable AC
oscilloscope voltage source. Route the power cord so the oscilloscope's feet and legs do not
pinch the cord.

### 2 The oscilloscope automatically adjusts for input line voltages in the range 100

to 240 VAC. The line cord provided is matched to the country of origin.
Always use a grounded power cord. Do not defeat the power cord ground.

### WARNING

### 3 Press the power switch.

The power switch is located on the lower left corner of the front panel. The
oscilloscope will perform a self-test and will be operational in a few seconds.
Connect Probes to the Oscilloscope

### 1 Connect the oscilloscope probe to an oscilloscope channel BNC connector.

### 2 Connect the probe's retractable hook tip to the point of interest on the circuit or

device under test. Be sure to connect the probe ground lead to a ground point
on the circuit.
Maximum input voltage at analog inputs

### CAUTION

300Vrms, 400Vpk; transient overvoltage 1.6kVpk
50Ω input: 5Vrms Input protection is enabled in 50Ω mode and the 50Ω load will
disconnect if greater than 5Vrms is detected. However the inputs could still be damaged,
depending on the time constant of the signal. The 50Ω input protection only functions
when the oscilloscope is powered on.

### Tables on this Page

| WARNING |
|---|
|  |

| CAUTION |
|---|
|  |

## Page 32


### 1 Getting Started

### 32 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

Do not float the oscilloscope chassis

### CAUTION

Defeating the ground connection and "floating" the oscilloscope chassis will probably
result in inaccurate measurements and may also cause equipment damage. The probe
ground lead is connected to the oscilloscope chassis and the ground wire in the power
cord. If you need to measure between two live points, use a differential probe with
sufficient dynamic range.
Do not negate the protective action of the ground connection to the oscilloscope. The

### WARNING

oscilloscope must remain grounded through its power cord. Defeating the ground
creates an electric shock hazard.
Input a Waveform
The first signal to input to the oscilloscope is the Demo2, Probe Comp signal. This
signal is used for compensating probes.

### 1 Connect an oscilloscope probe from channel 1 to the Demo 2 (Probe Comp)

terminal on the front panel.

### 2 Connect the probe's ground lead to the ground terminal (next to the Demo 2

terminal).
Recall the Default Oscilloscope Setup
To recall the default oscilloscope setup:

### 1 Press [Default Setup].

The default setup restores the oscilloscope's default settings. This places the
oscilloscope in a known operating condition. The major default settings are:

### Tables on this Page

| CAUTION |
|---|
|  |

| WARNING |
|---|
|  |

## Page 33

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 33

### Table 2 Default Configuration Settings

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

### 1 Press [Auto Scale].

You should see a waveform on the oscilloscope's display similar to this:

### Tables on this Page

| Horizontal | Normal mode, 100µs/div scale, 0s delay, center time reference. |
|---|---|
| Vertical (Analog) | Ω Channel 1 on, 5V/div scale, DC coupling, 0V position, 1M impedance. |
| Trigger | Edge trigger, Auto trigger mode, 0V level, channel 1 source, DC coupling, rising edge slope, 40ns holdoff time. |
| Display | Persistence off, 20% grid intensity, 50% waveform intensity. |
| Other | Acquire mode normal, [Run/Stop] to Run, cursors and measurements off. |
| Labels | All custom labels that you have created in the Label Library are preserved (not erased), but all channel labels will be set to their original names. |

## Page 34


### 1 Getting Started

### 34 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

### 2 If you want to return to the oscilloscope settings that existed before, press Undo

Autoscale.

### 3 If you want to enable "fast debug" autoscaling, change the channels

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

### Tables on this Page

## Page 35

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

### 1 Input the Probe Comp signal (see “Input a Waveform"on page32).

### 2 Press [Default Setup] to recall the default oscilloscope setup (see “Recall the

Default Oscilloscope Setup"on page32).

### 3 Press [Auto Scale] to automatically configure the oscilloscope for the Probe

Comp signal (see “Use Autoscale"on page33).

### 4 Press the channel key to which the probe is connected ([1], [2], etc.).

### 5 In the Channel Menu, press Probe.

### 6 In the Channel Probe Menu, press Probe Check; then, follow the instructions

on-screen.
If necessary, use a nonmetallic tool (supplied with the probe) to adjust the
trimmer capacitor on the probe for the flattest pulse possible.
On N2894A probes, the trimmer capacitor is located on the probe BNC
connector.

## Page 36


### 1 Getting Started

### 36 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

Perfectly compensated
Over compensated
Under compensated

### 7 Connect probes to all other oscilloscope channels (channel 2 of a 2-channel

oscilloscope, or channels 2, 3, and 4 of a 4-channel oscilloscope).

### 8 Repeat the procedure for each channel.

Learn the Front Panel Controls and Connectors
On the front panel, key refers to any key (button) you can press.
Softkey specifically refers to the six keys that are directly below the display. The
legend for these keys is directly above them, on the display. Their functions
change as you navigate through the oscilloscope's menus.
For the following figure, refer to the numbered descriptions in the table that
follows.

### Tables on this Page

| Perfectly compensated Over compensated Under compensated | Perfectly compensated Over compensated Under compensated |  |
|---|---|---|

## Page 37

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 37

### 5. Waveform keys 6. Trigger controls 7. Horizontal controls 8. Run Control keys

### 9. [Default Setup] key

### 10. [Auto Scale] key

### 11. Additional

### 4. Entry knob

waveform controls

### 3. [Intensity] key

### 12. Measure controls

### 13. File keys

### 14. Tools keys

### 2. Softkeys 15. [Help] key

### 1. Power switch 16. Vertical controls

### 21. Waveform 20. EXT TRIG IN 19. USB 18. Demo 2, Ground, 17. Analog

generator connector Host and Demo 1 channel
outputs ports terminals inputs

### 1. Power switch Press once to switch power on; press again to switch power off. See

“Power-On the Oscilloscope"on page30.

### 2. Softkeys The functions of these keys change based upon the menus shown on the

display directly above the keys.
The Back Back/Up key moves up in the softkey menu hierarchy. At the top
of the hierarchy, the Back Back/Up key turns the menus off, and
oscilloscope information is shown instead.

### 3. [Intensity] key Press the key to illuminate it. When illuminated, turn the Entry knob to

adjust waveform intensity.
You can vary the intensity control to bring out signal detail, much like an
analog oscilloscope.
Digital channel waveform intensity is not adjustable.
More details about using the Intensity control to view signal detail are on
“To adjust waveform intensity"on page155.

### Tables on this Page

| 5. Waveform keys 6. Trigger controls 7. Horizontal controls 8. Run Control keys 9. [Default Setup] key 10. [Auto Scale] key 11. Additional 4. Entry knob waveform controls 3. [Intensity] key 12. Measure controls 13. File keys 14. Tools keys 2. Softkeys 15. [Help] key 1. Power switch 16. Vertical controls 21. Waveform 20. EXT TRIG IN 19. USB 18. Demo 2, Ground, 17. Analog generator connector Host and Demo 1 channel outputs ports terminals inputs |
|---|
|  |

| 1. | Power switch | Press once to switch power on; press again to switch power off. See “Power-On the Oscilloscope"on page30. |
|---|---|---|
| 2. | Softkeys | The functions of these keys change based upon the menus shown on the display directly above the keys. The Back Back/Up key moves up in the softkey menu hierarchy. At the top of the hierarchy, the Back Back/Up key turns the menus off, and oscilloscope information is shown instead. |
| 3. | [Intensity] key | Press the key to illuminate it. When illuminated, turn the Entry knob to adjust waveform intensity. You can vary the intensity control to bring out signal detail, much like an analog oscilloscope. Digital channel waveform intensity is not adjustable. More details about using the Intensity control to view signal detail are on “To adjust waveform intensity"on page155. |

## Page 38


### 1 Getting Started

### 38 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

### 4. Entry knob The Entry knob is used to select items from menus and to change values.

The function of the Entry knob changes based upon the current menu and
softkey selections.
Note that the curved arrow symbol above the entry knob illuminates
whenever the entry knob can be used to select a value. Also, note that
when the Entry knob symbol appears on a softkey, you can use the
Entry knob, to select values.
Often, rotating the Entry knob is enough to make a selection. Sometimes,
you can push the Entry knob to enable or disable a selection. Pushing the
Entry knob also makes popup menus disappear.

### 5. Waveform keys [Analyze] key — Press this key to access analysis features like:

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

### Measurements and Math"on page275).

• Real-time eye analysis (included with the DSOX6JITTER jitter analysis

### application, see “Real-Time Eye Analysis"on page299).

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

### Tables on this Page

| 4. | Entry knob | The Entry knob is used to select items from menus and to change values. The function of the Entry knob changes based upon the current menu and softkey selections. Note that the curved arrow symbol above the entry knob illuminates whenever the entry knob can be used to select a value. Also, note that when the Entry knob symbol appears on a softkey, you can use the Entry knob, to select values. Often, rotating the Entry knob is enough to make a selection. Sometimes, you can push the Entry knob to enable or disable a selection. Pushing the Entry knob also makes popup menus disappear. |
|---|---|---|
| 5. | Waveform keys | [Analyze] key — Press this key to access analysis features like: • Trigger level setting. • Measurement threshold setting. • The DSOX6USBSQ USB 2.0 signal quality analysis application. • Video trigger automatic set up and display. • Color grade waveform display (see Chapter16, “Color Grade Waveform,” starting on page 287). • Counter (DVMCTR) (see “Counter"on page320). • Digital voltmeter (DVMCTR) (see “Digital Voltmeter"on page318). • Histogram of waveforms or measurements (see Chapter15, “Histogram,” starting on page 277). • Mask testing (see Chapter18, “Mask Testing,” starting on page 303). • The DSOX6PWR power measurement and analysis application. • Precision measurements and math functions (see “Precision Measurements and Math"on page275). • Real-time eye analysis (included with the DSOX6JITTER jitter analysis application, see “Real-Time Eye Analysis"on page299). The [Acquire] key lets you select Normal, Peak Detect, Averaging, or High Resolution acquisition modes (see “Selecting the Acquisition Mode"on page223) and use segmented memory (see “Acquiring to Segmented Memory"on page232). The [Jitter] key lets you set up jitter analysis (see Chapter17, “Jitter and Real-Time Eye Analysis,” starting on page 291). [Clear Display] key — Press this key to clear acquisition data from the oscilloscope display. The [Display] key lets you access the menu where you can enable persistence (see “To set or clear persistence"on page157), clear the display, and adjust the display grid (graticule) intensity (see “To adjust the grid intensity"on page159). |

## Page 39

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 39

### 6. Trigger controls These controls determine how the oscilloscope triggers to capture data.

See Chapter10, “Triggers,” starting on page 171 and Chapter11,
“Trigger Mode/Coupling,” starting on page 209.

### 7. Horizontal The Horizontal controls consist of:

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

### 8. Run Control When the [Run/Stop] key is green, the oscilloscope is running, that is,

keys acquiring data when trigger conditions are met. To stop acquiring data,
press [Run/Stop].
When the [Run/Stop] key is red, data acquisition is stopped. To start
acquiring data, press [Run/Stop].
To capture and display a single acquisition (whether the oscilloscope is
running or stopped), press [Single]. The [Single] key is yellow until the
oscilloscope triggers.
For more information, see “Running, Stopping, and Making Single
Acquisitions (Run Control)"on page217.

### 9. [Default Setup] Press this key to restore the oscilloscope's default settings (details on

key “Recall the Default Oscilloscope Setup"on page32).

### Tables on this Page

| 6. | Trigger controls | These controls determine how the oscilloscope triggers to capture data. See Chapter10, “Triggers,” starting on page 171 and Chapter11, “Trigger Mode/Coupling,” starting on page 209. |
|---|---|---|
| 7. | Horizontal controls | The Horizontal controls consist of: • Horizontal scale knob — Turn the knob in the Horizontal section that is marked to adjust the time/div (sweep speed) setting. The symbols under the knob indicate that this control has the effect of spreading out or zooming in on the waveform using the horizontal scale. • Horizontal position knob — Turn the knob marked to pan through the waveform data horizontally. You can see the captured waveform before the trigger (turn the knob clockwise) or after the trigger (turn the knob counterclockwise). If you pan through the waveform when the oscilloscope is stopped (not in Run mode) then you are looking at the waveform data from the last acquisition taken. • [Horiz] key — Press this key to open the Horizontal Menu where you can select XY and Roll modes, enable or disable Zoom, enable or disable horizontal time/division fine adjustment, and select the trigger time reference point. • Zoom key — Press the zoom key to split the oscilloscope display into Normal and Zoom sections without opening the Horizontal Menu. • [Search] key — Lets you search for events in the acquired data. • [Navigate] keys — Press these keys to navigate through captured data via time, search events, or segmented memory acquisition. See “Navigating the Time Base"on page77. For more information see Chapter2, “Horizontal Controls,” starting on page 65. |
| 8. | Run Control keys | When the [Run/Stop] key is green, the oscilloscope is running, that is, acquiring data when trigger conditions are met. To stop acquiring data, press [Run/Stop]. When the [Run/Stop] key is red, data acquisition is stopped. To start acquiring data, press [Run/Stop]. To capture and display a single acquisition (whether the oscilloscope is running or stopped), press [Single]. The [Single] key is yellow until the oscilloscope triggers. For more information, see “Running, Stopping, and Making Single Acquisitions (Run Control)"on page217. |
| 9. | [Default Setup] key | Press this key to restore the oscilloscope's default settings (details on “Recall the Default Oscilloscope Setup"on page32). |

## Page 40


### 1 Getting Started

### 40 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

### 10. [Auto Scale] When you press the [Auto Scale] key, the oscilloscope will quickly

key determine which channels have activity, and it will turn these channels on
and scale them to display the input signals. See “Use Autoscale"on
page33.

### 11. Additional The additional waveform controls consist of:

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

### Tables on this Page

| 10. | [Auto Scale] key | When you press the [Auto Scale] key, the oscilloscope will quickly determine which channels have activity, and it will turn these channels on and scale them to display the input signals. See “Use Autoscale"on page33. |
|---|---|---|
| 11. | Additional waveform controls | The additional waveform controls consist of: • [Math] key — provides access to math (add, subtract, etc.) waveform functions. See Chapter4, “Math Waveforms,” starting on page 91. • [Ref] key — provides access to reference waveform functions. Reference waveforms are saved waveforms that can be displayed and compared against other analog channel or math waveforms. Also, measurements can be made on reference waveforms. See Chapter5, “Reference Waveforms,” starting on page 127. • [Digital] key — Press this key to turn the digital channels on or off (the arrow to the left will illuminate). When the arrow to the left of the [Digital] key is illuminated, the upper multiplexed knob selects (and highlights in red) individual digital channels, and the lower multiplexed knob positions the selected digital channel. If a trace is repositioned over an existing trace the indicator at the left edge of the trace will change from Dnndesignation (where nn is a one or two digit channel number from 0 to 15) to D*. The "*" indicates that two or more channels are overlaid. You can rotate the upper knob to select an overlaid channel, then rotate the lower knob to position it just as you would any other channel. For more information on digital channels see Chapter6, “Digital Channels,” starting on page 131. • [Serial] key — This key is used to enable serial decode. The multiplexed scale and position knobs are not used with serial decode. For more information on serial decode, see Chapter7, “Serial Decode,” starting on page 149. • Multiplexed scale knob — This scale knob is used with Math, Ref, or Digital waveforms, whichever has the illuminated arrow to the left. For math and reference waveforms, the scale knob acts like an analog channel vertical scale knob. • Multiplexed position knob — This position knob is used with Math, Ref, or Digital waveforms, whichever has the illuminated arrow to the left. For math and reference waveforms, the position knob acts like an analog channel vertical position knob. |

## Page 41

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 41

### 12. Measure The measure controls consist of:

controls • Cursors knob — Push this knob to select cursors from a popup menu.
Then, after the popup menu closes (either by timeout or by pushing the
knob again), rotate the knob to adjust the selected cursor position.
• [Cursors] key — Press this key to open a menu that lets you select the
cursors mode and source.
• [Meas] key — Press this key to access a set of predefined

### measurements. See Chapter14, “Measurements,” starting on page

### 245.

### 13. File keys Press the [Save/Recall] key to save or recall a waveform or setup. See

Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on
page 343.
The [Print] key opens the Print Configuration Menu so you can print the
displayed waveforms. See Chapter22, “Print (Screens),” starting on page

### 357.

### 14. Tools keys The Tools keys consist of:

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

### 15. [Help] key Opens the Help Menu where you can display overview help topics and

select the Language. See also “Access the Built-In Quick Help"on
page62.

### Tables on this Page

| 12. | Measure controls | The measure controls consist of: • Cursors knob — Push this knob to select cursors from a popup menu. Then, after the popup menu closes (either by timeout or by pushing the knob again), rotate the knob to adjust the selected cursor position. • [Cursors] key — Press this key to open a menu that lets you select the cursors mode and source. • [Meas] key — Press this key to access a set of predefined measurements. See Chapter14, “Measurements,” starting on page 245. |
|---|---|---|
| 13. | File keys | Press the [Save/Recall] key to save or recall a waveform or setup. See Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on page 343. The [Print] key opens the Print Configuration Menu so you can print the displayed waveforms. See Chapter22, “Print (Screens),” starting on page 357. |
| 14. | Tools keys | The Tools keys consist of: • [Utility] key — Press this key to access the Utility Menu, which lets you configure the oscilloscope's I/O settings, use the file explorer, set preferences, access the service menu, and choose other options. See Chapter23, “Utility Settings,” starting on page 363. • [Quick Action] key — Press this key to perform the selected quick action: measure all snapshot, print, save, recall, freeze display, and more. See “Configuring the [Quick Action] Key"on page381. • [Wave Gen1], [Wave Gen2] keys — Press these keys to access waveform generator functions. See Chapter20, “Waveform Generator,” starting on page 323. |
| 15. | [Help] key | Opens the Help Menu where you can display overview help topics and select the Language. See also “Access the Built-In Quick Help"on page62. |

## Page 42


### 1 Getting Started

### 42 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

### 16. Vertical The Vertical controls consist of:

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

### 81.

### 17. Analog channel Attach oscilloscope probes or BNC cables to these BNC connectors.

inputs With the InfiniiVision 6000X-Series oscilloscopes, you can set the input
Ω Ω
impedance of the analog channels to either 50 or 1M . See “To
specify channel input impedance"on page85.
The InfiniiVision 6000X-Series oscilloscopes also provide the AutoProbe

### interface. The AutoProbe interface uses a series of contacts directly below

the channel's BNC connector to transfer information between the
oscilloscope and the probe. When you connect a compatible probe to the
oscilloscope, the AutoProbe interface determines the type of probe and
sets the oscilloscope's parameters (units, offset, attenuation, coupling, and
impedance) accordingly.

### 18. Demo 2, • Demo 2 terminal — This terminal outputs the Probe Comp signal which

Ground, and helps you match a probe's input capacitance to the oscilloscope
Demo 1 channel to which it is connected. See “Compensate Passive
terminals Probes"on page35. With certain licensed features, the oscilloscope
can also output demo or training signals on this terminal.
• Ground terminal — Use the ground terminal for oscilloscope probes
connected to the Demo 1 or Demo 2 terminals.
• Demo 1 terminal — With certain licensed features, the oscilloscope can
output demo or training signals on this terminal.

### Tables on this Page

| 16. | Vertical controls | The Vertical controls consist of: • Analog channel on/off keys — Use these keys to switch a channel on or off, or to access a channel's menu in the softkeys. There is one channel on/off key for each analog channel. • Vertical scale knob — There are knobs marked for each channel. Use these knobs to change the vertical sensitivity (gain) of each analog channel. • Vertical position knobs — Use these knobs to change a channel's vertical position on the display. There is one Vertical Position control for each analog channel. • [Label] key — Press this key to access the Label Menu, which lets you enter labels to identify each trace on the oscilloscope display. See Chapter9, “Labels,” starting on page 165. • [Touch] key — Press this key to disable/enable the touchscreen. For more information, see Chapter3, “Vertical Controls,” starting on page 81. |
|---|---|---|
| 17. | Analog channel inputs | Attach oscilloscope probes or BNC cables to these BNC connectors. With the InfiniiVision 6000X-Series oscilloscopes, you can set the input Ω Ω impedance of the analog channels to either 50 or 1M . See “To specify channel input impedance"on page85. The InfiniiVision 6000X-Series oscilloscopes also provide the AutoProbe interface. The AutoProbe interface uses a series of contacts directly below the channel's BNC connector to transfer information between the oscilloscope and the probe. When you connect a compatible probe to the oscilloscope, the AutoProbe interface determines the type of probe and sets the oscilloscope's parameters (units, offset, attenuation, coupling, and impedance) accordingly. |
| 18. | Demo 2, Ground, and Demo 1 terminals | • Demo 2 terminal — This terminal outputs the Probe Comp signal which helps you match a probe's input capacitance to the oscilloscope channel to which it is connected. See “Compensate Passive Probes"on page35. With certain licensed features, the oscilloscope can also output demo or training signals on this terminal. • Ground terminal — Use the ground terminal for oscilloscope probes connected to the Demo 1 or Demo 2 terminals. • Demo 1 terminal — With certain licensed features, the oscilloscope can output demo or training signals on this terminal. |

## Page 43

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 43

### 19. USB Host ports These ports are for connecting a USB mass storage device, printer, mouse,

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

### 20. EXT TRIG IN External trigger input BNC connector. See “External Trigger Input"on

connector page214 for an explanation of this feature.

### 21. Waveform Built-in, license-enabled 2-channel waveform generator can output

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

### 1 Gently pull on the front panel knobs to remove them.

### 2 Insert the overlay's side tabs into the slots on the front panel.


### Tables on this Page

| 19. | USB Host ports | These ports are for connecting a USB mass storage device, printer, mouse, or keyboard to the oscilloscope. Connect a USB compliant mass storage device (flash drive, disk drive, etc.) to save or recall oscilloscope setup files and reference waveforms or to save data and screen images. See Chapter21, “Save/Email/Recall (Setups, Screens, Data),” starting on page 343. To print, connect a USB compliant printer. For more information about printing see Chapter22, “Print (Screens),” starting on page 357. You can also use the USB port to update the oscilloscope's system software when updates are available. You do not need to take special precautions before removing the USB mass storage device from the oscilloscope (you do not need to "eject" it). Simply unplug the USB mass storage device from the oscilloscope when the file operation is complete. CAUTION: Do not connect a host computer to the oscilloscope's USB host port. Use the device port. A host computer sees the oscilloscope as a device, so connect the host computer to the oscilloscope's device port (on the rear panel). See “I/O Interface Settings"on page363. There is a third USB host port on the back panel. |
|---|---|---|
| 20. | EXT TRIG IN connector | External trigger input BNC connector. See “External Trigger Input"on page214 for an explanation of this feature. |
| 21. | Waveform generator outputs | Built-in, license-enabled 2-channel waveform generator can output arbitrary, sine, square, ramp, pulse, DC, noise, sine cardinal, exponential rise, exponential fall, cardiac, or Gaussian pulse waveforms on the GenOut1 or GenOut2 BNC connectors. Modulated waveforms are available on WaveGen1 except for arbitrary, pulse, DC, and noise waveforms. Press the [Wave Gen1] or [Wave Gen2] keys to set up the waveform generator. See Chapter20, “Waveform Generator,” starting on page 323. |

## Page 44


### 1 Getting Started

### 44 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

### 3 Reinstall the front panel knobs.

Front panel overlays may be ordered from www.parts.keysight.com using the
following part numbers:

### Tables on this Page

## Page 45

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

### Tables on this Page

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

## Page 46


### 1 Getting Started

### 46 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

• “Access the Trigger Menu, Change the Trigger Mode, and Open the Trigger
Level Dialog"on page57
• “Use a USB Mouse and/or Keyboard for Touchscreen Controls"on page58
Draw Rectangles for Waveform Zoom or Zone Trigger Set Up

### 1 Touch the upper-right corner to select the rectangle draw mode.

### 2 Drag your finger across the screen to draw a rectangle.

### 3 Take your finger off the screen.

### 4 Touch the desired option from the popup menu.


### Tables on this Page

## Page 47

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 47
Pinch, Flick, or Drag to Scale, Position, and Change Offset

### 1 Touch the upper-right corner to select the waveform drag mode.

### 2 When the waveform drag mode is selected, you can use these touch gestures:


### Tables on this Page

## Page 48


### 1 Getting Started

### 48 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

• Pinch — used to zoom in on a waveform of interest. A horizontal pinch
adjusts the oscilloscope's time/div and delay settings at once — for "off
center zooming", this is more efficient than using knobs. A vertical pinch
adjusts a waveform's V/div and offset settings at once.
To select waveforms, tap them. The waveform closest horizontally to the tap
location is selected. The selected waveform is indicated by the ground
marker with the filled background (channel 1 in the following example).

### Tables on this Page

## Page 49

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 49
• Flick — allows very fast browsing of waveforms. It is similar to browsing on

### tablets and smartphones. It is much easier to flick than to continually turn a

knob.
• Drag — drag your finger across the screen to change the horizontal delay.
Select Sidebar Information or Controls

### 1 Touch the blue menu icon in the sidebar.

### 2 In the popup menu, touch the type of information or controls you want to see in

the sidebar.

### Tables on this Page

## Page 50


### 1 Getting Started

### 50 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

Undock Sidebar Dialogs by Dragging
Sidebar dialogs can be undocked and placed anywhere on the screen.

### 1 Drag the sidebar dialog title wherever you like.

This lets you view multiple types of information or controls at the same time.

### Tables on this Page

## Page 51

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

### Tables on this Page

## Page 52


### 1 Getting Started

### 52 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

• When softkeys provide menus, double-touch to select a menu item.
This may be an easier than selecting a menu item via the Entry knob.
Enter Names Using Alpha-Numeric Keypad Dialogs
Some softkeys open alpha-numeric dialogs that let you touch to enter names.

### Tables on this Page

## Page 53

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 53
Change Waveform Offsets By Dragging Ground Reference Icons
When the waveform drag mode is selected, you can drag waveforms up or down
to change the vertical offset.
You can always change waveform vertical offsets by dragging ground markers and
labels, even when in the rectangle draw mode.

### Tables on this Page

## Page 54


### 1 Getting Started

### 54 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

Access Controls and Menus Using the Spark Icon

### 1 Touch the upper-left spark icon to open the main menu.

### 2 Touch left side controls to perform oscilloscope operations.


### Tables on this Page

## Page 55

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 55

### 3 Touch menu items and submenu items to access menus and additional

controls.

### Tables on this Page

## Page 56


### 1 Getting Started

### 56 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

Turn Channels On/Off and Open Scale/Offset Dialogs
• Touch channel numbers to turn them on or off.
• When channels are on, touch the scale and offset values to access a dialog for
changing them.
Access the Horizontal Menu and Open the Scale/Delay Dialog
• Touch "H" to access the Horizontal Menu.
• Touch the horizontal scale and delay values to access a dialog for changing
them.

### Tables on this Page

## Page 57

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 57
Access the Trigger Menu, Change the Trigger Mode, and Open the
Trigger Level Dialog
• Touch "T" to access the Trigger Menu.
• Touch the trigger level value(s) to access a dialog for changing the level(s).
• Touch "Auto" or "Trig'd" to quickly toggle the trigger mode.

### Tables on this Page

## Page 58


### 1 Getting Started

### 58 Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide

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

### command.

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

## Page 59

Getting Started 1
Keysight InfiniiVision 6000X-Series Oscilloscopes User's Guide 59
The recognition is best when using the accent of the selected language. See “To
select the language"on page63.
Learn the Rear Panel Connectors
For the following figure, refer to the numbered descriptions in the table that
follows.

### 3. TRIG OUT connector

### 6. Digital channel inputs 4. 10 MHz REF connector 5. Calibration protect switch

### 8. USB Host port

### 9. USB Device port

### 10. LAN port

### 7. VGA Video Out

### 2. Kensington lock hole 1. Power cord connector

### 1. Power cord Attach the power cord here.

connector

### 2. Kensington lock This is where you can attach a Kensington lock for securing the instrument.

hole

### 3. TRIG OUT Trigger output BNC connector. See “Setting the Rear Panel TRIG OUT

connector Source"on page374.

### Tables on this Page

| 3. TRIG OUT connector 6. Digital channel inputs 4. 10 MHz REF connector 5. Calibration protect switch 8. USB Host port 9. USB Device port 10. LAN port 7. VGA Video Out 2. Kensington lock hole 1. Power cord connector |
|---|
|  |

