from fastapi import APIRouter, UploadFile, File
from app.schemas import QuestionRequest
from app.services import pdf_loader, chunker
from app.services.embedder import Embedder
from app.services.vector_store import VectorStore
from app.services.retriever import retrieve
from app.services.generator import generate_answer

router = APIRouter()

embedder = Embedder()
vector_store = None
chunks_cache = []

@router.get("/")
def root():
    return {"message": "Document Q&A RAG System", "endpoints": {"upload": "POST /upload", "ask": "POST /ask"}}

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    global vector_store, chunks_cache

    path = f"temp_{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())

    text = pdf_loader.load_pdf(path)
    chunks = chunker.chunk_text(text)
    embeddings = embedder.embed(chunks)

    vector_store = VectorStore(embeddings.shape[1])
    vector_store.add(embeddings)

    chunks_cache = chunks
    return {"message": "PDF processed successfully"}

@router.post("/ask")
def ask_question(req: QuestionRequest):
    query_embedding = embedder.embed([req.question])[0]
    indices = retrieve(query_embedding, vector_store)
    context = [chunks_cache[i] for i in indices]
    answer = generate_answer(context, req.question)
    return {"answer": answer}
