# Lab Automation RAG Assistant Manual

**Complete Guide to Building & Operating a Local AI Assistant for Test Instrument Control**

---

## Table of Contents

1. [Overview](#overview)
2. [What It Does](#what-it-does)
3. [Project Structure](#project-structure)
4. [Requirements](#requirements)
5. [Installation & Setup](#installation--setup)
6. [Step 1: Prepare Knowledge Base](#step-1-prepare-knowledge-base)
7. [Step 2: Ingest Documentation](#step-2-ingest-documentation)
8. [Step 3: Start the Server](#step-3-start-the-server)
9. [Step 4: Use the Assistant](#step-4-use-the-assistant)
10. [How RAG Works](#how-rag-works)
11. [Configuration & Tuning](#configuration--tuning)
12. [Example Workflows](#example-workflows)
13. [Troubleshooting](#troubleshooting)


![Screenshot](images/Screenshot%202026-05-26%20at%2010.12.28.png)

[RAG Conversation - Copper Mountain VNA on Raspberry Pi](RAG%20Conversation%20-%20Copper%20Mountain%20VNA%20on%20Raspberry%20Pi.pdf)

[RAG Conversation - E36300 PSU Voltage Sequencing](RAG%20Conversation%20-%20E36300%20PSU%20Voltage%20Sequencing.pdf)

[RAG Conversation - Eye Diagram 2 Gbps Signal](RAG%20Conversation%20-%20Eye%20Diagram%202%20Gbps%20Signal.pdf)


### Knowledge Base: Lab Instrument Automation & Integration

The RAG automation knowledge base enables programmatic control of laboratory instruments through SCPI/VISA protocols, supporting full test automation from measurement acquisition to data analysis:

**Copper Mountain VNA (Vector Network Analyzer):**
- SCPI command reference and programming manual
- One-port and two-port S-parameter calibration automation
- Power sweep and frequency sweep procedures
- Binary data transfer (HiSLIP and socket protocols)
- Multi-VNA orchestration and synchronization
- External trigger integration and cycle-time optimization
- Python and C/C++ implementation examples
- Linux installation and connectivity guides

**Keysight Power Supply (PSU):**
- Voltage sequencing and multi-output coordination
- API reference and command set documentation
- Parameter sweep automation
- Real-time monitoring and data logging
- Integration with test workflows

**Keysight Oscilloscope (Scope):**
- Signal acquisition and waveform capture
- Triggering modes and external sync
- Data transfer protocols (Socket, Serial, PXI)
- Measurement automation (eye diagrams, jitter, rise time)
- Python and C/C++ example code
- User manuals and API documentation

**Implementation Examples:**
- Socket and HiSLIP binary protocols for high-speed data transfer
- Error handling and device discovery patterns
- Multi-instrument coordination and synchronization
- External trigger-based pass/fail signaling
- Periodic data archival and real-time analysis

This knowledge base transforms ad-hoc manual measurements into fully automated test sequences, enabling unattended characterization, yield analysis, and compliance verification.
---

## Overview

The **Lab Automation RAG Assistant** is a fully local, offline AI system for controlling test instruments via SCPI/VISA commands. It combines:

- **LLM (Qwen 3.5-9B Q4)** — Generates Python code and technical advice
- **RAG (ChromaDB + embeddings)** — Retrieves relevant documentation in real-time
- **FastAPI Web Server** — Serves a responsive chat interface
- **Instrument Knowledge Base** — Your manuals, programming guides, SCPI references

No cloud. No API keys. All processing happens on your machine with full privacy and offline capability.

### Why RAG for Lab Automation?

**Traditional approach:** Write SCPI commands from memory or flip through PDF manuals
- ❌ Slow — find page 1732 of the Programmer's Guide
- ❌ Error-prone — syntax mistakes, wrong channel numbers
- ❌ Repetitive — same setup boilerplate for every test

**RAG approach:** Ask the AI assistant
- ✓ Fast — retrieve relevant SCPI commands in milliseconds
- ✓ Accurate — grounded in actual documentation, not hallucination
- ✓ Intelligent — cross-references data sheets, knows dependencies
- ✓ Reproducible — generates consistent code following your patterns

---

## What It Does

### Core Capabilities

#### 1. **SCPI Code Generation**
Ask for setup code, get working Python + VISA automation:

```
User: "Connect to E36300 PSU on 192.168.1.50, set CH1 to 3.3V @ 0.5A max current"Assistant: 
import pyvisa as visa
import time

RESOURCE_STRING = "TCPIP0::192.168.1.50::5000::SOCKET"

rm = visa.ResourceManager()
inst = rm.open_resource(RESOURCE_STRING, write_termination='\n', read_termination='\n')

try:
    print(inst.query('*IDN?'))
    inst.write('*RST')
    inst.write(':SOURCE:VOLTAGE 3.3')
    inst.write(':SOURCE:CURRENT 0.5')
    inst.write(':OUTPUT ON')
    print("✓ PSU configured: 3.3V @ 0.5A max")
except Exception as e:
    print(f"Error: {e}")
finally:
    inst.close()
```

#### 2. **Documentation Retrieval**
Instantly search your knowledge base:

```
User: "What SCPI commands does the Keysight 6000X use for real-time eye analysis?"
Assistant: Retrieves sections from InfiniiVision 6000X Programmer's Guide + examples
```

#### 3. **Cross-File Dependencies**
Understands instrument interconnections:

```
User: "What voltage range does the P6V channel support?"
Assistant: Knows P6V specs, typical usage patterns, power budget constraints
```

#### 4. **Best Practice Guidance**
Follows test engineering patterns:

```
User: "How do I safely switch a PSU from 3V to 5V?"
Assistant: Safety checks, settle time, measurement verification, error handling
```

---

## Project Structure

```
lab_automation/
│
├── WEBRAG_simple.py              ← Web server (FastAPI + inference)
├── WEBRAG_simple.html            ← Chat UI (loads at http://ai.local:8000)
├── WEBRAG_INGEST.py              ← Ingestion script
│
├── knowledge_base/               ← Your documentation (populate this)
│   ├── psu/
│   │   ├── E36300_UserGuide.pdf
│   │   ├── E36300_Programming.pdf
│   │   └── E36300_SCPI_Reference.txt
│   ├── scope/
│   │   ├── InfiniiVision_6000X_UserGuide.md
│   │   └── InfiniiVision_6000X_Programming.md
│   ├── vna/
│   │   ├── CMT_S4VNA_Manual.md
│   │   └── CMT_SCPI_Commands.txt
│   ├── code_examples/
│   │   ├── psu_setup.py
│   │   ├── scope_eye_measurement.py
│   │   └── vna_s2p_sweep.py
│   └── notes/
│       ├── lab_safety.md
│       └── best_practices.md
│
└── chroma_db/                    ← Vector database (auto-created)
    └── (contains embedded documentation)
```

**Key folders:**
- **knowledge_base/** — Put all your instrument manuals and code examples here
- **chroma_db/** — Created automatically, do not edit manually

---

## Requirements

### Hardware

| Spec | Minimum | Recommended |
|------|---------|-------------|
| GPU VRAM | 6 GB | 8 GB+ (RTX 3070 or better) |
| System RAM | 8 GB | 16 GB+ |
| Storage | 15 GB free | 30 GB free |
| CPU | Quad-core | Ryzen 7 / i7 or better |

### OS & Python

- **OS:** Linux (Ubuntu 22+), Windows 11 (WSL2), macOS 13+
- **Python:** 3.10 or later
- **GPU:** NVIDIA CUDA 11.8+ (recommended) or CPU-only mode

### Python Libraries

Install with one command:

```bash
pip install llama-cpp-python fastapi uvicorn pydantic chromadb sentence-transformers --break-system-packages
```

| Library | Purpose | Notes |
|---------|---------|-------|
| `llama-cpp-python` | LLM inference | Runs GGUF models on GPU/CPU |
| `fastapi` | Web framework | HTTP routing & streaming |
| `uvicorn` | ASGI server | Runs FastAPI app |
| `chromadb` | Vector DB | Stores & retrieves embeddings |
| `sentence-transformers` | Embeddings | Converts text to vectors for RAG |

### Model Files

**LLM Model** (~7GB download):

```bash
# Qwen 3.5-9B Q4 quantized (recommended)
# Download from: https://huggingface.co/Qwen/Qwen3.5-9B-GGUF
# Save to: ~/hugging_face_rag/models/qwen3.5-9b-q4/Qwen3.5-9B-Q4_K_M.gguf
```

**Embedding Model** (~270MB, auto-downloaded on first run):

```bash
# nomic-ai/nomic-embed-text-v1.5
# Downloads automatically via sentence-transformers
```

---

## Installation & Setup

### Step 1: Clone or Download

Get the Lab Automation RAG files:

```bash
# Create project directory
mkdir ~/lab_automation
cd ~/lab_automation

# Copy files (or clone if using git)
# - WEBRAG_simple.py
# - WEBRAG_simple.html
# - WEBRAG_INGEST.py
```

### Step 2: Install Dependencies

```bash
pip install llama-cpp-python fastapi uvicorn pydantic chromadb sentence-transformers --break-system-packages
```

Verify installation:

```bash
python3 -c "import llama_cpp; import chromadb; import sentence_transformers; print('✓ All dependencies installed')"
```

### Step 3: Download LLM Model

```bash
# Create model directory
mkdir -p ~/hugging_face_rag/models/qwen3.5-9b-q4

# Download Qwen 3.5-9B Q4 from Hugging Face
# https://huggingface.co/Qwen/Qwen3.5-9B-GGUF/blob/main/Qwen3.5-9B-Q4_K_M.gguf
# Save to: ~/hugging_face_rag/models/qwen3.5-9b-q4/Qwen3.5-9B-Q4_K_M.gguf
```

Or use `huggingface-cli`:

```bash
huggingface-cli download Qwen/Qwen3.5-9B-GGUF Qwen3.5-9B-Q4_K_M.gguf \
  --local-dir ~/hugging_face_rag/models/qwen3.5-9b-q4
```

### Step 4: Create Knowledge Base Folder

```bash
mkdir -p ~/lab_automation/knowledge_base/{psu,scope,vna,code_examples,notes}
```

---

## Step 1: Prepare Knowledge Base

Add all your documentation to the `knowledge_base/` folder. The system will automatically process these file types:

### Supported Formats

| Type | Extensions | Examples |
|------|-----------|----------|
| PDFs | `.pdf` | Keysight programming guides, user manuals |
| Markdown | `.md` | Notes, reference cards, checklists |
| Text | `.txt` | SCPI command lists, specifications |
| Code | `.py`, `.c`, `.cpp`, `.h` | Test scripts, measurement examples |
| Config | `.json`, `.xml` | Setup templates, device configs |

### Organize Your Knowledge Base

**Example structure:**

```
knowledge_base/
├── psu/
│   ├── E36300_UserGuide.pdf
│   ├── E36300_SCPI_Reference.txt
│   └── E36300_Command_Examples.md
├── scope/
│   ├── InfiniiVision_6000X_Programmer.pdf
│   ├── eye_diagram_setup.md
│   └── s11_measurement.py
├── vna/
│   ├── CMT_S4VNA_Manual.pdf
│   └── s2p_measurement_example.py
├── code_examples/
│   ├── psu_voltage_sweep.py
│   ├── scope_capture_waveform.py
│   └── vna_network_analysis.py
└── notes/
    ├── lab_setup.md
    ├── safety_checklist.md
    └── troubleshooting.md
```

### Adding PDFs to Knowledge Base

For PDF files, it's helpful to extract them to Markdown first for better retrieval:

```bash
# Use the included pdf2md.py script
python3 pdf2md.py E36300_UserGuide.pdf E36300_UserGuide.md
python3 pdf2md.py InfiniiVision_6000X_Programmer.pdf scope_prog.md

# Move converted files to knowledge_base
mv *.md knowledge_base/
```

### What to Include

**Minimum knowledge base** (for any instrument):
- User's Guide / Hardware Manual
- SCPI/Programming Reference
- Quick reference command list
- 2-3 working code examples

**Complete knowledge base** (recommended):
- All above plus:
  - Device specifications sheet
  - Hardware block diagram
  - Connection/cabling guide
  - Safety guidelines
  - Troubleshooting guide
  - 5+ working code examples

---

## Step 2: Ingest Documentation

The ingestion process reads your documentation, splits it into chunks, converts each to a vector using the embedding model, and stores them in ChromaDB.

### Run Ingestion

```bash
cd ~/lab_automation
python3 WEBRAG_INGEST.py ./knowledge_base/
```

Expected output:

```
⚙️  Setting up embeddings...
  Loading embeddings: nomic-ai/nomic-embed-text-v1.5...
  ✓ Embedding model loaded
✓ Ready for ingestion

📦 Setting up vector database at: ./chroma_db
✓ Vector database ready (collection: lab_automation)

📁 Scanning: ./knowledge_base/
──────────────────────────────────────────────────────────

📊 Found 12 file(s) to process:

[1/12]
   📄 knowledge_base/psu/E36300_UserGuide.pdf
      Size: 2,451,823 bytes | Type: .pdf
      Content: 1,842,456 characters
      Chunks: 156
      ⏳ Embedding and storing...
      ✅ Stored 156 chunks!

[2/12]
   📄 knowledge_base/psu/E36300_SCPI_Reference.txt
...

══════════════════════════════════════════════════════════════════════
✅ DONE!
   Files processed:  12
   Files failed:     0
   Total chunks:     847
   Database:         ./chroma_db
   Collection:       lab_automation
══════════════════════════════════════════════════════════════════════
```

### Re-ingesting After Updates

If you add new documents to `knowledge_base/`, delete the old database and re-ingest:

```bash
rm -rf chroma_db/
python3 WEBRAG_INGEST.py ./knowledge_base/
```

---

## Step 3: Start the Server

```bash
cd ~/lab_automation
python3 WEBRAG_simple.py
```

Expected output:

```
Loading model from /home/user/hugging_face_rag/models/qwen3.5-9b-q4/Qwen3.5-9B-Q4_K_M.gguf...
llama_context: n_ctx_seq (16384) < n_ctx_train (262144) -- the full capacity 
of the model will not be utilized
Model loaded.

⚙️  Setting up ChromaDB RAG...
  Loading embeddings: nomic-ai/nomic-embed-text-v1.5...
  ✓ Embedding model loaded
  Connecting to ChromaDB: ./chroma_db
  ✓ ChromaDB ready (847 chunks)

INFO:     Started server process [12345]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

Server is ready when you see: **`Uvicorn running on http://0.0.0.0:8000`**

---

## Step 4: Use the Assistant

### Open the Web UI

In any browser on your network, visit:

```
http://ai.local:8000
```

**If `ai.local` doesn't resolve**, find your server IP:

```bash
hostname -I
# or
ip addr show | grep "inet " | grep -v 127
```

Then visit: `http://<server-ip>:8000`

### Chat Interface

The interface has three areas:

1. **Chat history** (top, scrollable) — Shows previous questions & answers
2. **Input box** (bottom) — Type your question here
3. **Buttons** (right):
   - **Send** — Submit your message (or press Enter)
   - **Clear** — Reset conversation history

### Example Queries

#### PSU Setup
```
"Give me Python code to connect to a Keysight E36300 PSU at 192.168.1.100, 
set channel 1 to 5V with 0.5A current limit, then measure the actual voltage"
```

#### Oscilloscope Measurement
```
"How do I capture an eye diagram on a 2 Gbps signal using the InfiniiVision 6000X? 
Include Python code with VISA connection, setup, and data retrieval."
```

#### VNA S-Parameter Sweep
```
"Create Python code to measure S2P from 1 MHz to 2 GHz with 10 points per decade 
using the Copper Mountain CMT S4VNA. Save results in Touchstone format."
```

#### Troubleshooting
```
"My oscilloscope triggering is unstable. What's the procedure to verify trigger 
settings and lock onto a 2 GHz signal?"
```

#### Cross-Device Setup
```
"I need to simultaneously sweep the E36300 PSU from 3V to 5V while the InfiniiVision 
captures oscilloscope traces at each step. Show me the Python structure to coordinate both."
```

---

## How RAG Works

RAG = **Retrieval Augmented Generation**

When you ask a question, the system does:

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. USER QUESTION                                               │
│    "How do I set voltage on the E36300 PSU?"                   │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│ 2. RAG RETRIEVAL                                               │
│    • Convert question to vector (embedding)                    │
│    • Search ChromaDB for similar chunks                        │
│    • Retrieve top 5 relevant sections                          │
│    Result: SCPI commands, examples, safe procedures from docs │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│ 3. PROMPT ASSEMBLY                                             │
│    • System instructions (how to write SCPI code)             │
│    • Retrieved documentation (from RAG)                        │
│    • Conversation history (previous exchanges)                │
│    • Your question                                            │
│    Total: ~8KB of context                                     │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│ 4. INFERENCE                                                   │
│    Qwen 3.5-9B reads assembled context                        │
│    Generates reply token-by-token                             │
│    Streams to browser in real-time                            │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│ 5. RESPONSE                                                    │
│    Python code grounded in your actual documentation          │
│    Not hallucinated — based on what's in your knowledge base  │
└─────────────────────────────────────────────────────────────────┘
```

**Why this works:**
- Model sees only relevant chunks (not entire 2000-page PDF)
- Answers are grounded in your actual documentation
- No hallucination of commands that don't exist
- Consistent with your instrument's behavior

---

## Configuration & Tuning

### Server Settings (WEBRAG_simple.py)

Edit these values at the top of the file to customize behavior:

```python
# Model path
MODEL_PATH = Path.home() / "hugging_face_rag/models/qwen3.5-9b-q4/Qwen3.5-9B-Q4_K_M.gguf"

# Context window (tokens) — reduce if running out of VRAM
CONTEXT_LEN = 16384

# Max tokens per reply
MAX_TOKENS = 4096

# GPU/CPU usage: -1 = all layers on GPU, 0 = CPU only, 32 = first 32 layers on GPU
N_GPU_LAYERS = -1

# Number of CPU threads for inference
N_THREADS = 16

# ChromaDB settings
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "lab_automation"

# Model parameters (affects response style)
temperature = 0.2        # Lower = more deterministic, Higher = more creative
top_p = 0.95            # Nucleus sampling
top_k = 40              # Top-k sampling
repeat_penalty = 1.1    # Penalizes repeated tokens
```

### Ingestion Settings (WEBRAG_INGEST.py)

```python
# How many tokens per chunk
CHUNK_SIZE = 256

# Overlap between chunks (prevents cutting mid-sentence)
CHUNK_OVERLAP = 50

# Same paths as server (must match!)
CHROMA_PATH = "./chroma_db"
COLLECTION_NAME = "lab_automation"
```

### Performance Tuning

**If running out of VRAM (Out of Memory errors):**

1. Reduce context window:
```python
CONTEXT_LEN = 8192  # down from 16384
```

2. Use fewer GPU layers:
```python
N_GPU_LAYERS = 32  # instead of -1 (all)
```

3. Reduce batch size in ingestion:
```python
CHUNK_SIZE = 128  # smaller chunks
```

**If responses are too slow:**

1. Reduce context:
```python
CONTEXT_LEN = 8192
MAX_TOKENS = 2048  # shorter replies
```

2. Reduce threads:
```python
N_THREADS = 8
```

**If responses are too generic or repetitive:**

1. Increase creativity:
```python
temperature = 0.5  # from 0.2
top_p = 0.9       # from 0.95
```

2. Add more diverse examples to knowledge base

---

## Example Workflows

### Workflow 1: Set Up and Measure PSU

**Scenario:** Need to verify E36300 PSU output voltage

```
User: "I have a Keysight E36300 PSU at 192.168.1.100 on TCP port 5000.
       Write code to set CH1 to 5V @ 0.5A max, measure actual voltage and current,
       then switch to 3.3V @ 1A after 2 seconds."
```

**Assistant retrieves:** E36300 SCPI reference, examples, safety procedures

**Generates:** Complete Python code with VISA connection, error handling, measurements

**Code includes:**
- pyvisa connection setup
- SCPI handshake (*IDN?, *RST, *CLS)
- Voltage/current set
- 2-second wait
- Voltage change
- Measurement queries
- Error handling

---

### Workflow 2: Multi-Instrument Coordination

**Scenario:** Simultaneous PSU + Oscilloscope sweep

```
User: "I need to sweep the E36300 PSU from 3V to 5V in 0.5V steps while 
       the InfiniiVision 6000X captures oscilloscope traces at each step.
       Give me the Python code structure to coordinate both instruments."
```

**Assistant retrieves:**
- E36300 voltage setting commands
- InfiniiVision waveform capture commands
- Timing/synchronization examples

**Generates:** Structured code with:
- Connection to both instruments
- Loop over voltage points
- PSU set → wait for settle → oscilloscope capture → data log
- Cleanup

---

### Workflow 3: Troubleshooting

**Scenario:** Instrument not responding

```
User: "My oscilloscope at 192.168.1.50 isn't responding to VISA commands. 
       What's the step-by-step debugging procedure?"
```

**Assistant retrieves:** Connection troubleshooting sections from manuals

**Generates:** Diagnostic checklist:
1. Verify IP connectivity (ping)
2. Check VISA resource discovery
3. Test *IDN? handshake
4. Verify write/read termination
5. Check USB/network cabling

---

## Troubleshooting

### Issue: "Failed to fetch" in Browser

**Symptoms:** Clicking "Send" produces an error message

**Solutions:**

1. Check server is running:
```bash
# Terminal shows "Uvicorn running on http://0.0.0.0:8000"?
```

2. Try IP address instead of `ai.local`:
```
http://192.168.1.100:8000  # replace with your server IP
```

3. Check firewall allows port 8000:
```bash
sudo ufw allow 8000
```

4. Restart server:
```bash
# Ctrl+C in server terminal, then
python3 WEBRAG_simple.py
```

---

### Issue: ChromaDB Empty (0 chunks)

**Symptoms:** Server starts but responses say "[No matching documents in RAG]"

**Solutions:**

1. Verify knowledge base has files:
```bash
ls -la knowledge_base/
# Should show .pdf, .md, .txt files
```

2. Run ingestion:
```bash
python3 WEBRAG_INGEST.py ./knowledge_base/
# Should show "✅ DONE!" with chunk count
```

3. Verify ChromaDB was created:
```bash
ls -la chroma_db/
# Should show database files
```

---

### Issue: Out of Memory (CUDA OOM)

**Symptoms:** Error like "cuda out of memory"

**Solutions:**

1. Reduce context window in `WEBRAG_simple.py`:
```python
CONTEXT_LEN = 8192  # down from 16384
```

2. Use fewer GPU layers:
```python
N_GPU_LAYERS = 32  # instead of -1
```

3. Restart server and try again

---

### Issue: Model Not Found

**Symptoms:** "FileNotFoundError: ~/hugging_face_rag/models/..."

**Solutions:**

1. Download Qwen 3.5-9B Q4 model:
```bash
# Download from https://huggingface.co/Qwen/Qwen3.5-9B-GGUF
# Save to ~/hugging_face_rag/models/qwen3.5-9b-q4/
```

2. Verify path matches in `WEBRAG_simple.py`:
```python
MODEL_PATH = Path.home() / "hugging_face_rag/models/qwen3.5-9b-q4/Qwen3.5-9B-Q4_K_M.gguf"
```

---

### Issue: Slow Response Time

**Symptoms:** 10+ seconds to get any reply

**Solutions:**

1. Check GPU is being used:
```bash
nvidia-smi  # should show VRAM usage
```

2. Reduce response length:
```python
MAX_TOKENS = 2048  # down from 4096
```

3. Use CPU for embeddings only (faster ingestion):
```python
N_GPU_LAYERS = 0  # run LLM on CPU
```

---

## Best Practices

### Knowledge Base Organization

1. **Organize by instrument type:**
```
psu/     → power supplies
scope/   → oscilloscopes
vna/     → network analyzers
dpm/     → digital multimeters
```

2. **Include working examples:**
Each instrument folder should have 2-3 complete, tested code examples

3. **Keep PDFs extracted as Markdown:**
Markdown files are easier to retrieve and more reliable than raw PDFs

4. **Tag documents with keywords:**
Add notes like:
```
# Keysight E36300 Power Supply
Keywords: PSU, voltage, current, SCPI, E36300
```

### Query Tips

1. **Be specific about instruments:**
"E36300 PSU" not just "power supply"

2. **Include network details when asking for connection code:**
"IP: 192.168.1.100, Port: 5000"

3. **Ask for complete workflows:**
"Give me code from connection through cleanup" not just one step

4. **Reference previous context:**
"Now add error handling to the code you just showed me"

### Document Updates

1. **After adding new instruments:**
```bash
rm -rf chroma_db/
python3 WEBRAG_INGEST.py ./knowledge_base/
```

2. **After correcting manuals:**
Same as above — re-ingest everything

3. **Keep a changelog:**
Document what each instrument type is and when it was added

---

## Summary Checklist

### Initial Setup
- [ ] Install Python 3.10+
- [ ] Install dependencies: `pip install llama-cpp-python fastapi uvicorn chromadb sentence-transformers`
- [ ] Download Qwen 3.5-9B Q4 model
- [ ] Create `knowledge_base/` folder
- [ ] Download instrument manuals and save to `knowledge_base/`

### Before First Use
- [ ] Run ingestion: `python3 WEBRAG_INGEST.py ./knowledge_base/`
- [ ] Verify ChromaDB created: `ls -la chroma_db/`
- [ ] Check chunk count in ingestion output

### Operation
- [ ] Start server: `python3 WEBRAG_simple.py`
- [ ] Wait for "Uvicorn running on..." message
- [ ] Open browser: `http://ai.local:8000`
- [ ] Type question and press Send

### Maintenance
- [ ] Keep knowledge base updated with new manuals
- [ ] Re-ingest after adding documents
- [ ] Monitor server terminal for errors
- [ ] Back up `chroma_db/` periodically

---

**Lab Automation RAG Manual — Complete**

For questions or updates, refer to the included `README.md` file and the source code documentation in `WEBRAG_simple.py` and `WEBRAG_INGEST.py`.
