#!/bin/bash

# Document Q&A RAG System - Startup Script for Linux/macOS

echo ""
echo "========================================"
echo "  Document Q&A - RAG System"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if requirements are installed
pip show fastapi >>/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

echo ""
echo "Starting FastAPI server..."
echo ""
echo "========================================"
echo "Frontend:  http://localhost:8000"
echo "API Docs:  http://localhost:8000/docs"
echo "ReDoc:     http://localhost:8000/redoc"
echo "========================================"
echo ""
echo "Press CTRL+C to stop the server"
echo ""

# Start the FastAPI server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
