# Keysight Power Supply SCPI / VISA API Reference

## Official Documentation & Links

### E36300 Series (Most Common - what we found)
- **Programming Guide**: https://www.keysight.com/us/en/assets/9018-04577/programming-guides/9018-04577.pdf
- **User's Guide**: https://www.mouser.com/pdfDocs/E36311-90001.pdf
- **Models**: E36311A (USB), E36312A (USB/LAN/GPIB), E36313A (USB/LAN/GPIB, 160W)
- **Key specs**:
  - 3 outputs: P6V (0–6V, 0–5.15A), P25V (0–25V, 0–1.03A), N25V (0–25V, 0–1.03A)
  - SCPI over GPIB, USB, or LAN (port 5025 for socket)
  - Python / VISA compatible

### E3631A / E3632A (Legacy, still in use)
- **Programming Guide**: http://ece-research.unm.edu/jimp/650/instr_docs/AgilentE3631A.pdf
- **Models**: E3631A (triple output), E3632A (dual output)
- **Similar command set to E36300 but slightly different subsystem paths**

### Older 664xA–669xA Series (GPIB era)
- **Programming Guide**: https://www.testunlimited.com/pdf/keysight_6680A_6680A-J04_6681A_6682A_6683A_6684A_6690A_6691A_ConfigurationGuide.pdf
- Models: 6640A, 6648A, 6650A, 6680A, etc.
- GPIB only, still widely used in labs

### Keysight General Python Automation
- **Getting Started (Keysight Instruments + Python)**: https://docs.keysight.com/kkbopen/getting-started-automate-keysight-instruments-using-python-3-9-845872587.html
- **Instrument Automation with Python (white paper)**: https://www.keysight.com/us/en/assets/7018-06894/white-papers/5992-4268.pdf
- **System Power Supply Programming with Python & Sockets**: https://www.keysight.com/us/en/assets/7018-06563/white-papers/5992-3827.pdf
- **System Power Supply Programming (voltage ramping)**: https://www.keysight.com/us/en/assets/7018-06572/white-papers/5992-3841.pdf

### VISA & PyVISA Setup
- **PyVISA docs**: https://pyvisa.readthedocs.io/
- **Keysight IO Libraries Suite (required for VISA on Windows)**: https://www.keysight.com/find/iolibs
- **National Instruments NI-VISA (alternative)**: https://www.ni.com/en/support/documentation/supplemental/06/ni-virtual-instrument-software-architecture.html

---

## E36300 Core SCPI Commands (from Programming Guide)

### Connection & Handshake
```scpi
*IDN?                          # ID: returns "KEYSIGHT,E3631[1|2|3]A,SN...,FW..."
*RST                           # Reset to defaults
*CLS                           # Clear status registers
*OPC?                          # Operation complete (returns 1)
SYST:ERR?                      # Read error queue, e.g. "0,\"No error\""
```

### Output Selection (multi-channel)
```scpi
INST:SEL P6V | P25V | N25V     # Select output (or CH1, CH2, CH3)
INST:SEL?                      # Query current selection
```

### Voltage Control
```scpi
[SOUR:]VOLT 5.0 (@1)           # Set voltage on channel 1 (or selected)
[SOUR:]VOLT? (@1)              # Query voltage setting
[SOUR:]VOLT:PROT 6.0 (@1)      # Set voltage protection limit
[SOUR:]VOLT:PROT? (@1)         # Query protection limit
```

### Current Control  
```scpi
[SOUR:]CURR 2.0 (@1)           # Set current limit on channel 1
[SOUR:]CURR? (@1)              # Query current limit
[SOUR:]CURR:PROT:STAT ON (@1)  # Enable current protection
```

### Output On/Off
```scpi
OUTP ON, (@1)                  # Turn on output 1
OUTP OFF, (@1)                 # Turn off output 1
OUTP? (@1)                     # Query state: 1 or 0
```

### Measurement (Sense)
```scpi
MEAS:VOLT:DC? (@1)             # Measure actual voltage on output 1
MEAS:CURR:DC? (@1)             # Measure actual current on output 1
```

### Triggering & Status
```scpi
*TRG                           # Software trigger (if in triggered mode)
INIT:CONT ON, (@1)             # Continuous triggering (default)
INIT:CONT OFF, (@1)            # Single-shot mode
```

---

## Python Working Examples

### Example 1: VISA Connection (Keysight IO Libs or NI-VISA)
```python
import pyvisa
import time

# Connect via VISA
rm = pyvisa.ResourceManager()  # Uses installed VISA backend
psu = rm.open_resource('GPIB0::5::INSTR')  # GPIB address 5
# OR for LAN: 'TCPIP0::192.168.1.100::inst0::INSTR'
# OR for USB: 'USB0::0x0957::0x0588::MY1234::INSTR'

# Set termination (important!)
psu.write_termination = '\n'
psu.read_termination  = '\n'
psu.timeout = 5000

# Handshake
idn = psu.query('*IDN?')
print(f"[INFO] Connected: {idn}")
psu.write('*RST')
psu.write('*CLS')
psu.query('*OPC?')

# Check for errors
err = psu.query('SYST:ERR?')
print(f"[INFO] Post-reset error: {err}")

# Set voltage on P6V (CH1)
psu.write('INST:SEL P6V')        # Select P6V
psu.write('VOLT 3.3')            # Set 3.3V
psu.write('CURR 2.0')            # Limit to 2A
time.sleep(0.1)                  # Let it settle
psu.write('OUTP ON')             # Turn on

# Measure
v = float(psu.query('MEAS:VOLT:DC?'))
i = float(psu.query('MEAS:CURR:DC?'))
print(f"[INFO] P6V output: {v:.3f}V, {i:.3f}A")

psu.write('OUTP OFF')
psu.close()
```

### Example 2: Raw Socket (no VISA backend needed)
```python
import socket
import time

def socket_query(s, cmd):
    """Send SCPI command, return response."""
    s.sendall((cmd.strip() + '\n').encode())
    buf = ''
    while '\n' not in buf:
        buf += s.recv(4096).decode()
    return buf.split('\n', 1)[0].strip()

def socket_write(s, cmd):
    """Send SCPI command (no response expected)."""
    s.sendall((cmd.strip() + '\n').encode())

# Connect
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
s.settimeout(5.0)
s.connect(('192.168.1.100', 5025))  # PSU IP, port 5025

# Handshake
idn = socket_query(s, '*IDN?')
print(f"[INFO] Connected: {idn}")
socket_write(s, '*RST')
socket_write(s, '*CLS')
socket_query(s, '*OPC?')

# Configure
socket_write(s, 'INST:SEL P6V')
socket_write(s, 'VOLT 3.3')
socket_write(s, 'CURR 2.0')
time.sleep(0.1)
socket_write(s, 'OUTP ON')

# Measure
v = float(socket_query(s, 'MEAS:VOLT:DC?'))
i = float(socket_query(s, 'MEAS:CURR:DC?'))
print(f"[INFO] P6V output: {v:.3f}V, {i:.3f}A")

socket_write(s, 'OUTP OFF')
s.close()
```

### Example 3: Multi-Channel Sweep to CSV
```python
import pyvisa
import csv
from datetime import datetime
import time

rm = pyvisa.ResourceManager()
psu = rm.open_resource('TCPIP0::192.168.1.100::5025::SOCKET')
psu.write_termination = '\n'
psu.read_termination = '\n'
psu.timeout = 5000

# Handshake
psu.query('*IDN?')
psu.write('*RST')
psu.query('*OPC?')

# Sweep P6V from 0V to 6V in 0.5V steps, measure at each
config = {
    'channel': 'P6V',
    'current_limit': 2.0,
    'volts': [0.0, 0.5, 1.0, 1.5, 2.0, 3.3, 5.0, 6.0],
}

filename = f"psu_sweep_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['timestamp', 'channel', 'voltage_set', 'voltage_meas', 'current_meas'])
    writer.writeheader()
    
    psu.write(f'INST:SEL {config["channel"]}')
    psu.write(f'CURR {config["current_limit"]}')
    
    for v_set in config['volts']:
        psu.write(f'VOLT {v_set}')
        psu.write('OUTP ON')
        time.sleep(0.2)  # Settle
        
        v_meas = float(psu.query('MEAS:VOLT:DC?'))
        i_meas = float(psu.query('MEAS:CURR:DC?'))
        
        writer.writerow({
            'timestamp': datetime.now().isoformat(),
            'channel': config['channel'],
            'voltage_set': v_set,
            'voltage_meas': v_meas,
            'current_meas': i_meas,
        })
        print(f"[WRITE] {v_set:.1f}V set → {v_meas:.3f}V, {i_meas:.3f}A")

psu.write('OUTP OFF')
psu.close()
print(f"[DONE] Results saved to {filename}")
```

### Example 4: Emulator (for local testing without hardware)
```python
#!/usr/bin/env python3
import socket
import threading

def handle_psu(conn, addr):
    """Emulate E36311A power supply on port 5025."""
    conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    buf = ''
    state = {
        'inst_sel': 'P6V',
        'p6v_volt': 0.0,
        'p6v_curr': 2.0,
        'p25v_volt': 0.0,
        'p25v_curr': 1.0,
        'n25v_volt': 0.0,
        'n25v_curr': 1.0,
        'outp': 0,
    }
    
    def dispatch(cmd):
        cmd = cmd.upper().strip()
        if cmd == '*IDN?':
            return 'KEYSIGHT,E36311A,SN12345678,1.0.1'
        elif cmd == '*RST':
            state.update({'p6v_volt': 0, 'p25v_volt': 0, 'n25v_volt': 0, 'outp': 0})
            return ''
        elif cmd == '*CLS':
            return ''
        elif cmd == '*OPC?':
            return '1'
        elif cmd == 'SYST:ERR?':
            return '0,"No error"'
        elif cmd.startswith('INST:SEL'):
            state['inst_sel'] = cmd.split()[-1]
            return ''
        elif cmd.startswith('VOLT'):
            try:
                v = float(cmd.split()[-1])
                state[f"{state['inst_sel'].lower()}_volt"] = v
            except:
                pass
            return ''
        elif cmd == 'MEAS:VOLT:DC?':
            ch = state['inst_sel'].lower()
            return str(state.get(f'{ch}_volt', 0.0))
        elif cmd == 'MEAS:CURR:DC?':
            ch = state['inst_sel'].lower()
            return str(state.get(f'{ch}_curr', 0.0))
        elif cmd.startswith('OUTP'):
            if 'ON' in cmd or '1' in cmd:
                state['outp'] = 1
            elif 'OFF' in cmd or '0' in cmd:
                state['outp'] = 0
            return ''
        else:
            return 'ERROR'
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            buf += data.decode()
            while '\n' in buf:
                cmd, buf = buf.split('\n', 1)
                if cmd.strip():
                    resp = dispatch(cmd.strip())
                    if resp is not None:
                        conn.sendall((resp + '\n').encode())
    except:
        pass
    finally:
        conn.close()

if __name__ == '__main__':
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('0.0.0.0', 5025))
    srv.listen(5)
    print("[EMULATOR] PSU emulator running on 0.0.0.0:5025")
    try:
        while True:
            conn, addr = srv.accept()
            threading.Thread(target=handle_psu, args=(conn, addr), daemon=True).start()
    except KeyboardInterrupt:
        print("[EMULATOR] Stopped")
```

**Run the emulator:**
```bash
python psu_emulator.py &
```

**Test against it:**
```bash
python -c "
import socket
s = socket.socket()
s.connect(('localhost', 5025))
s.sendall(b'*IDN?\n')
print(s.recv(256).decode())
s.close()
"
```

---

## GitHub Examples (Community)

- **Keysight E3631A Python wrapper**: https://github.com/psmd-iberutaru/Keysight-E3631A-Python
- **Lab instrument control (multi-tool)**: https://github.com/topics/pyvisa
- **Oscilloscope SCPI (Keysight)**: https://github.com/sgoadhouse/oscope-scpi

---

## Quick Reference: VISA Resource Strings

| Interface | Format | Example |
|-----------|--------|---------|
| GPIB | `GPIB<board>::<address>::INSTR` | `GPIB0::5::INSTR` |
| USB | `USB0::<vendor>::<product>::<serial>::INSTR` | `USB0::0x0957::0x0588::12345::INSTR` |
| LAN (VXI-11) | `TCPIP0::<IP>::inst0::INSTR` | `TCPIP0::192.168.1.100::inst0::INSTR` |
| LAN (raw socket) | `TCPIP0::<IP>::5025::SOCKET` | `TCPIP0::192.168.1.100::5025::SOCKET` |
| Serial | `ASRL<COM>::INSTR` | `ASRL1::INSTR` |

> **Note**: For raw socket, always use `::SOCKET` suffix. If you omit it, pyvisa will try VXI-11 protocol which won't work on a basic emulator.

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `VisaIOError: (timeout)` on LAN | Check IP is correct, firewall allows port 5025, PSU has LAN enabled |
| `VisaIOError: (connection refused)` | PSU may not be listening on 5025; try GPIB or USB instead |
| Response hangs forever | Set `timeout` explicitly: `psu.timeout = 5000` (ms) |
| Empty string response | Command may be write-only (e.g. `*RST`); use `write()` not `query()` |
| "resource not found" | Run `rm.list_resources()` to see available instruments |
| pyvisa-py not working | Install: `pip install pyvisa pyvisa-py` (pure Python, no VISA backend needed) |

