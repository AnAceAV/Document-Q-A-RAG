# Quick Start Guide - Document Q&A RAG with Frontend

## 🚀 Getting Started (60 seconds)

### Windows Users
```bash
# Just run this file:
run.bat
```

### macOS/Linux Users
```bash
# Just run these commands:
chmod +x run.sh
./run.sh
```

### Or Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start the server
python -m uvicorn app.main:app --reload
```

## 📱 Access Your Application

Once running, open your browser and go to:
- **Frontend:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs (interactive API testing)
- **ReDoc:** http://localhost:8000/redoc (API documentation)

## 🎯 Using the Frontend

### Step 1: Upload a PDF
1. Click on the upload area or drag a PDF onto it
2. Wait for the file to process (you'll see a success message)
3. Check the uploaded file count and chunks created

### Step 2: Ask Questions
1. Type your question in the "Ask a Question" box
2. Click "Ask Question"
3. Wait for the answer to appear below

### Step 3: Get Results
- Answers appear in the "Answer" section with full context
- Use "Clear" to reset and ask another question
- Upload new PDFs anytime

## 📝 File Structure

```
app/
├── main.py              ← FastAPI app with frontend serving
├── routes.py            ← API endpoints
├── schemas.py           ← Data models
├── templates/
│   └── index.html       ← Frontend UI (this is what you see!)
├── static/              ← Additional assets go here
└── services/
    ├── pdf_loader.py
    ├── chunker.py
    ├── embedder.py
    ├── vector_store.py
    ├── retriever.py
    └── generator.py
```

## 🔌 API Endpoints

### For Frontend (Built-in)
- `GET /` → Loads the web interface
- `POST /api/upload` → Upload PDF files
- `POST /api/ask` → Ask questions

### Using curl/Postman

**Upload a PDF:**
```bash
curl -F "file=@document.pdf" http://localhost:8000/api/upload
```

**Ask a question:**
```bash
curl -X POST http://localhost:8000/api/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"What is the main topic?"}'
```

## ⚙️ Configuration

### Change LLM (in app/services/generator.py)
- Currently uses: Ollama (local, free, offline)
- To use OpenAI: Uncomment OpenAI sections and add OPENAI_API_KEY

### Change Model (in generator.py or config)
- Default: `phi` (Ollama)
- Other options: `mistral`, `neural-chat`, `llama2`

### Adjust File Size Limit
In `app/templates/index.html`, find this line and change the size:
```javascript
if (file.size > 50 * 1024 * 1024) { // Change 50 to your limit (MB)
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| "Address already in use" | Change port: `--port 8001` or kill existing process |
| File upload fails | Ensure file is PDF and under 50MB |
| "Please upload PDF first" | Upload succeeded but backend not ready - try again |
| No answers showing | Check that Ollama is running (if using local model) |
| 404 errors on upload | Endpoints use `/api/` prefix now |
| CORS errors | Background request - frontend already handles this |

## 📊 Frontend Features

✅ Drag-and-drop upload  
✅ Real-time processing  
✅ Error handling  
✅ Statistics tracking  
✅ Beautiful UI  
✅ Mobile responsive  
✅ No external dependencies  
✅ Auto-linking to backend  

## 🔒 Security Notes

- File upload: 50MB max, PDF only
- No authentication yet (add if needed)
- Backend accepts connections from any origin (restrict if public)
- Files stored as temp files (clean up periodically)

## 💡 Tips

1. **First time?** Keep the default Ollama model running
2. **Slow processing?** Your LLM might be running on CPU (get more RAM or use OpenAI)
3. **Multiple PDFs?** Upload replaces the previous one (by design)
4. **API only?** Use the `/api/*` endpoints directly with `curl` or Postman
5. **Customize UI?** Edit `app/templates/index.html`

## 📚 More Information

- See `FRONTEND_GUIDE.md` for detailed API documentation
- See `IMPLEMENTATION_SUMMARY.md` for what was added
- See `README.md` for project overview

## 🎉 You're All Set!

Your Document Q&A system is ready to use. Upload a PDF and start asking questions!

Questions? Check the troubleshooting section above. 👆
