@echo off
REM Document Q&A RAG System - Startup Script for Windows

echo.
echo ========================================
echo  Document Q&A - RAG System
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check if requirements are installed
pip show fastapi >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Installing dependencies...
    pip install -r requirements.txt
)

echo.
echo Starting FastAPI server...
echo.
echo ========================================
echo Frontend:  http://localhost:8000
echo API Docs:  http://localhost:8000/docs
echo ReDoc:     http://localhost:8000/redoc
echo ========================================
echo.
echo Press CTRL+C to stop the server
echo.

REM Start the FastAPI server
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause
