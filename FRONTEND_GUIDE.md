# Frontend Integration Guide

## Running the Application

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the FastAPI server:**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

3. **Access the frontend:**
- Open your browser and go to `http://localhost:8000`

## API Endpoints

### Frontend Routes
- `GET /` - Serves the main HTML frontend interface

### API Routes (Backend)
- `GET /api/` - Health check and API info
- `POST /api/upload` - Upload and process PDF file
- `POST /api/ask` - Ask questions about the uploaded document

## Frontend Features

### Upload Section
- **Drag & Drop**: Drag PDF files directly into the upload area
- **Click to Upload**: Click to select a PDF file
- **File Validation**: Only accepts PDF files up to 50MB
- **Status Tracking**: Shows uploaded files and their processing status
- **Statistics**: Displays number of files uploaded and chunks created

### Q&A Section
- **Question Input**: Type your question in natural language
- **Answer Display**: Get AI-generated answers based on document content
- **Loading State**: Visual feedback while processing questions
- **Clear Function**: Clear questions and results

## API Request/Response Format

### Upload PDF
**Request:**
```
POST /api/upload
Content-Type: multipart/form-data

file: <PDF_FILE>
```

**Response:**
```json
{
  "message": "PDF processed successfully",
  "filename": "document.pdf",
  "chunks_count": 42,
  "text_length": 15234
}
```

### Ask Question
**Request:**
```
POST /api/ask
Content-Type: application/json

{
  "question": "What is the main topic of this document?"
}
```

**Response:**
```json
{
  "answer": "The document discusses..."
}
```

## Frontend Architecture

- **HTML Structure**: Clean, semantic HTML5
- **Styling**: Modern CSS with gradients and shadows
- **JavaScript**: Vanilla JS (no dependencies)
- **Features**:
  - File upload with drag & drop
  - Real-time form validation
  - Loading states and spinners
  - Error handling and alerts
  - Responsive design (mobile-friendly)
  - CORS-enabled backend

## Browser Compatibility

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Troubleshooting

**Issue: CORS errors in console**
- The backend includes CORS middleware, so this should work

**Issue: File upload fails**
- Check file size (max 50MB)
- Ensure file is a valid PDF
- Check browser console for detailed errors

**Issue: "Please upload a PDF first" when asking questions**
- Make sure the PDF upload completed successfully
- Look for the success message and file status

**Issue: API endpoints returning 404**
- Ensure the server is running
- Check that routes are prefixed with `/api/`
