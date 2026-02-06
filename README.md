# Document Q&A - RAG System

This repository is a small Retrieval-Augmented Generation (RAG) web service that
lets you upload a PDF, embeds document chunks, stores them in a local vector
store and answers user questions using a language model.

This README explains how to set up the project, run it locally, choose between
local models (Ollama) or cloud models (OpenAI), and use the API endpoints.

---

## Features
- Upload a PDF and split it into chunks
- Create embeddings for chunks and store them in a vector index
- Retrieve relevant chunks for a question and generate an answer via an LLM

---

## Repo layout
- `app/` — FastAPI application and endpoints (`app/main.py`, `app/routes.py`)
- `app/services/` — service modules: `pdf_loader`, `chunker`, `embedder`,
  `vector_store`, `retriever`, `generator`
- `storage/faiss_index/` — persisted vector index (if used)
- `requirements.txt` — Python dependencies

Files to check:
- `app/main.py` ([app/main.py](app/main.py))
- `app/routes.py` ([app/routes.py](app/routes.py))
- `app/services/generator.py` ([app/services/generator.py](app/services/generator.py))

---

## Prerequisites
- Python 3.10+ (3.11/3.12 recommended)
- Git
- Optional: Ollama (for running local LLMs) — Windows/Mac/Linux installers at https://ollama.ai
- Optional: OpenAI API key (if you prefer the cloud LLM path)

Disk/Memory notes
- Local LLMs can require several GBs of RAM. If your machine has limited RAM,
  consider using a smaller model or using OpenAI to avoid local memory constraints.

---

## Setup (quick)
1. Clone the repo and enter the project folder:

```bash
git clone <repo-url>
cd "Document Q&A RAG"
```

2. Create and activate a virtual environment (Windows):

```powershell
python -m venv venv
venv\Scripts\activate
```

On macOS / Linux:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

4. (Optional) If you plan to use Ollama (local LLM), install Ollama and pull a small model:

```cmd
"C:\Users\<you>\AppData\Local\Programs\Ollama\ollama" pull phi
```

Note: replace the command path if Ollama is installed elsewhere. Use a smaller
model than `mistral` if your machine has limited RAM.

---

## Configuration options

1. Local Ollama (recommended for offline testing)
   - Ensure Ollama is running: it listens on `http://localhost:11434`
   - `app/services/generator.py` uses `langchain-ollama` by default in this project.

2. OpenAI (cloud)
   - Set `OPENAI_API_KEY` environment variable in your shell or system settings
   - Modify `app/services/generator.py` to use OpenAILLM (LangChain) if desired.

---

## Run the API locally

Start the FastAPI app (from project root, with venv active):

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Endpoints
- `GET /` — welcome message and available endpoints
- `POST /upload` — upload a PDF
  - Body: `form-data` with key `file` (type: File)
- `POST /ask` — ask a question
  - Body: JSON `{ "question": "..." }`

Example using `curl`:

Upload:
```bash
curl -F "file=@/path/to/document.pdf" http://127.0.0.1:8000/upload
```

Ask:
```bash
curl -H "Content-Type: application/json" -d '{"question":"What is this document about?"}' http://127.0.0.1:8000/ask
```

---

## Troubleshooting

- 422 Unprocessable Content when uploading: ensure you use `form-data` and the key is `file`.
- `ModuleNotFoundError: No module named 'langchain.text_splitter'`: install `langchain-text-splitters` (already in `requirements.txt`).
- Ollama model memory errors (`model requires more system memory`):
  - Increase pagefile (virtual memory) or use a smaller model (recommended).
  - To move models to another drive, stop Ollama, move `C:\Users\<you>\.ollama` to the new drive,
    and create a junction: `mklink /J "C:\Users\<you>\.ollama" "D:\ollama"` (admin required).

---

## Development notes
- `app/services/generator.py` currently uses `langchain_ollama.OllamaLLM`.
- Retrieval is performed in `app/services/retriever.py` and embeddings by `app/services/embedder.py`.
- You can swap the LLM backend by editing `generator.py` and restarting the API.

---

## Next improvements
- Add authentication for endpoints
- Persist the vector store to disk automatically
- Add batching and streaming responses for long LLM calls

---
