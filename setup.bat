@echo off
setlocal

echo ======================================
echo 🚀 Full Project Setup + Run (Windows)
echo ======================================

REM Step 1 — Check Python
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python not found. Install Python first.
    pause
    exit /b
)

REM Step 2 — Create venv if not exists
IF NOT EXIST venv (
    echo 📦 Creating virtual environment...
    python -m venv venv
) ELSE (
    echo ✅ Virtual environment exists
)

REM Step 3 — Activate venv
call venv\Scripts\activate

REM Step 4 — Upgrade pip
python -m pip install --upgrade pip

REM Step 5 — Create requirements.txt if missing
IF NOT EXIST requirements.txt (
    echo 📄 Creating requirements.txt...
    (
        echo fastapi
        echo uvicorn[standard]
        echo sqlalchemy
        echo psycopg2-binary
        echo python-dotenv
        echo httpx
        echo pydantic
        echo gradio
    ) > requirements.txt
)

REM Step 6 — Install dependencies
pip install -r requirements.txt

REM Step 7 — Create .env if missing
IF NOT EXIST .env (
    echo 🔐 Creating .env file...
    (
        echo API_TOKEN=mysupersecrettoken123
        echo DATABASE_URL=postgresql://user:password@localhost:5432/agentdb
        echo GROQ_API_KEY=your_groq_api_key_here
    ) > .env
)

REM Step 8 — Check files
IF NOT EXIST src/main.py (
    echo ❌ main.py not found!
    pause
    exit /b
)

IF NOT EXIST src/app.py (
    echo ❌ app.py not found!
    pause
    exit /b
)

REM Step 9 — Start FastAPI in new window
echo 🌐 Starting FastAPI backend...
start cmd /k "call venv\Scripts\activate && cd src  && uvicorn main:app --reload"

REM Step 10 — Start Gradio in new window
echo 🎨 Starting Gradio UI...
start cmd /k "call venv\Scripts\activate && cd src  && python app.py"

echo ======================================
echo ✅ Both services started!
echo FastAPI → http://localhost:8000
echo Gradio → http://127.0.0.1:7860
echo ======================================

pause
endlocal