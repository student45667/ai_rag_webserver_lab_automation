from pathlib import Path
from llama_cpp import Llama
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import uvicorn

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
# ADDED — ChromaDB RAG imports
import chromadb
from sentence_transformers import SentenceTransformer


# =============================================================================
# CONFIG
# =============================================================================

#MODEL_PATH = Path.home() / "hugging_face_rag/models/qwen2.5-coder-7b-q4/qwen2.5-coder-7b-instruct-q4_k_m.gguf"
MODEL_PATH = Path.home() / "hugging_face_rag/models/qwen3.5-9b-q4/Qwen3.5-9B-Q4_K_M.gguf"
CONTEXT_LEN  = 16384
N_THREADS    = 16
N_GPU_LAYERS = -1
MAX_TOKENS = 4096 #1024


# ChromaDB settings
CHROMA_PATH = "./chroma_db_lab_automation"
COLLECTION_NAME = "lab_automation"


EMBED_MODEL_NAME = "nomic-ai/nomic-embed-text-v1.5"

RECENCY_BUFFER = 3
MAX_SESSIONS = 10

# ChatML tokens
S = "<|im_start|>"
E = "<|im_end|>\n"

# =============================================================================
# SYSTEM PROMPT 
# =============================================================================





SYSTEM_PROMPT = """ /no_think
You are a lab automation engineer assistant specializing in test instruments and SCPI control via VISA/TCP sockets.

## Core Responsibilities
1. Write minimal, clean Python code using pyvisa or raw sockets
2. Follow SCPI handshake: *IDN? → *RST → *CLS → *OPC?
3. Use write_termination='\n' and read_termination='\n' explicitly
4. Never use query() on write-only commands (*RST, *CLS, OUTP ON)
5. Mark unknown instrument-specific commands with # VERIFY: check Programming Guide

## Code Style Rules
- No logging, no fancy error handling, no classes
- Straight SCPI commands via pyvisa
- Include response output after each command when useful
- Use TCPIP0::<host>::port::SOCKET resource strings (not ::INSTR)

## Response Format Preferences
1. For setup/connection questions: Step-by-step with diagrams and safety notes
2. For code requests: Minimal working examples first, improvements later
3. Always reference retrieved documentation when available
4. Explain WHY before showing HOW for technical concepts

## Safety First
- Power OFF before physical connections
- Match voltage/current limits to instrument capabilities
- Verify ground connections are secure
- Include measurement verification commands (MEAS:VOLT?, MEAS:CURR?)

## When in Doubt
- Ask clarifying questions about PSU model/channel count
- Check if multi-channel selection is needed (INST:SEL)
- Reference Keysight manuals or Command Expert tool for unknown commands

Retrieved documents:
{{RAG_CONTEXT}}



"""










SYSTEM_PROMPT_not_active = """ /no_think

You are a lab automation engineer assistant. You write clean Python code to control test instruments over VISA or raw TCP sockets using SCPI commands.

When generating code, always follow this sequence:
1. Handshake: connect, send *IDN?, then *CLS and *RST, verify with *OPC?
2. Configuration: apply settings from a config dict, one SCPI command per key
3. Measurement: loop over test points, read results, parse to float
4. Storage: write timestamped rows to CSV as you go, close in finally block
5. Display: plot results with matplotlib in a separate function

Communication rules:
- VISA (pyvisa): set write_termination='\n' and read_termination='\n' explicitly
- Raw socket fallback: port 5025, loop recv until '\n' found, set TCP_NODELAY=1
- pyvisa-py socket resource string: TCPIP0::<host>::5025::SOCKET (not ::INSTR)
- Use write() for *RST, *CLS, OUTP ON — never query() on write-only commands

SCPI commands are instrument-specific. If retrieved documents contain the instrument's Programming Guide or command reference, use those exact command strings. If not, use generic placeholders and mark every instrument-specific command with: # VERIFY: check instrument Programming Guide

Code writing:
Write minimal code [instrument] setup, no bells and whistles just it. 
No logging, no fancy error handling, no classes. Just straight SCPI commands via pyvisa.
Only offer improvements after showing the basic version.

Retrieved documents:
{{RAG_CONTEXT}}


"""





# =============================================================================
# LOAD MODEL
# =============================================================================

print(f"Loading model from {MODEL_PATH}...")
llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=CONTEXT_LEN,
    n_threads=N_THREADS,
    n_gpu_layers=N_GPU_LAYERS,
    verbose=False
)
print("Model loaded.\n")

# Setup ChromaDB RAG
print(f"⚙️  Setting up ChromaDB RAG...")
print(f"  Loading embeddings: {EMBED_MODEL_NAME}...")
embed_model = SentenceTransformer(EMBED_MODEL_NAME)
print("  ✓ Embedding model loaded")

print(f"  Connecting to ChromaDB: {CHROMA_PATH}")
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
chroma_collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME,
    metadata={"hnsw:space": "cosine"}
)
print(f"  ✓ ChromaDB ready ({chroma_collection.count()} chunks)")
print()

# =============================================================================
# RAG RETRIEVAL
# =============================================================================

def retrieve_context(query: str, top_k: int = 5) -> str:
    """Retrieve relevant context from ChromaDB."""
    try:
        query_embedding = embed_model.encode([query])[0].tolist()
        
        results = chroma_collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
            include=["documents", "metadatas"]
        )
        
        if not results["documents"] or not results["documents"][0]:
            return "[No matching documents in RAG]"
        
        context_parts = []
        for i, (doc, meta) in enumerate(zip(results["documents"][0], results["metadatas"][0])):
            source = meta.get("rel_path", "unknown")
            context_parts.append(f"[{source}]\n{doc}")
        
        return "\n\n".join(context_parts)
    
    except Exception as e:
        print(f"RAG retrieval error: {e}", flush=True)
        return "[RAG error]"

# =============================================================================
# SESSION STORE
# =============================================================================

sessions: dict[str, dict] = {}

def get_or_create_session(session_id: str) -> dict:
    """Return existing session or create new one."""
    if session_id not in sessions:
        if len(sessions) >= MAX_SESSIONS:
            sessions.pop(next(iter(sessions)))
        sessions[session_id] = {
            "history": [],
            "system": SYSTEM_PROMPT,
        }
    return sessions[session_id]

# =============================================================================
# TOKEN COUNTER
# =============================================================================

def count_tokens(text: str) -> int:
    return len(llm.tokenize(text.encode()))

# =============================================================================
# PROMPT BUILDER
# =============================================================================

def build_prompt(history: list, user_input: str, rag_context: str) -> str:
    system_block = f"{S}system\n{SYSTEM_PROMPT}{E}"
    rag_block = f"{S}user\n[RAG Context]\n{rag_context}{E}"
    user_block = f"{S}user\n{user_input}{E}{S}assistant\n"

    budget = CONTEXT_LEN - MAX_TOKENS - count_tokens(system_block + rag_block + user_block) - 64

    trimmed = list(history)
    while trimmed:
        hist_text = "".join(
            f"{S}user\n{t['user']}{E}{S}assistant\n{t['bot']}{E}"
            for t in trimmed
        )
        if count_tokens(hist_text) <= budget:
            break
        trimmed.pop(0)

    prompt = system_block + rag_block
    for t in trimmed:
        prompt += f"{S}user\n{t['user']}{E}{S}assistant\n{t['bot']}{E}"
    prompt += user_block

    return prompt

# =============================================================================
# STREAMING INFERENCE
# =============================================================================

def stream_chat(session_id: str, user_input: str):
    sess = get_or_create_session(session_id)
    
    # Retrieve RAG context
    rag_context = retrieve_context(user_input, top_k=5)
    
    # Build prompt with RAG context
    prompt = build_prompt(sess["history"], user_input, rag_context)

    full_reply = []
    token_count = 0

    for chunk in llm(
        prompt,
        max_tokens=MAX_TOKENS,
        temperature=0.2,
        top_p=0.95,
        top_k=40,
        repeat_penalty=1.1,
        stop=[E, S],
        echo=False,
        stream=True
    ):
        token = chunk["choices"][0]["text"]
        full_reply.append(token)
        token_count += 1
        yield token

    reply = "".join(full_reply).strip()
    print(f"[{session_id}] generated: {token_count} tokens", flush=True)
    
    sess["history"].append({"user": user_input, "bot": reply})

# =============================================================================
# FASTAPI
# =============================================================================

app = FastAPI(title="RAG Assistant")

class ChatRequest(BaseModel):
    session_id: str = "default"
    message: str = ""

@app.post("/stream")
def stream_endpoint(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(status_code=400, detail="Empty message")
    return StreamingResponse(
        stream_chat(req.session_id, req.message),
        media_type="text/plain"
    )

@app.post("/clear")
def clear_endpoint(req: ChatRequest):
    sessions.pop(req.session_id, None)
    return {"status": "cleared"}




# In the FastAPI section, change:
@app.get("/")
def root():
    return FileResponse("WEBRAG_simple.html")

# Or mount the file:
# app = FastAPI(title="RAG Assistant")
# app.mount("/", StaticFiles(directory=".", html=True), name="static")


# =============================================================================
# RUN
# =============================================================================

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)