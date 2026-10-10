@echo off
title TCM Acupuncture Study Suite
cd /d "%~dp0"

echo ========================================================
echo        TCM Acupuncture Study Suite Launcher
echo ========================================================
echo.

:: Check if server is already running on port 8501
netstat -ano | findstr ":8501 " | findstr "LISTENING" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [INFO] TCM Acupuncture Study Suite is already running!
    echo [INFO] Opening application in your browser...
    start "" "http://localhost:8501"
    exit /b 0
)

echo Starting Streamlit server...
echo Access locally at:  http://localhost:8501
echo Access on mobile at: http://0.0.0.0:8501
echo.

:: Streamlit automatically opens the browser ONCE when server is ready
".\venv\Scripts\streamlit.exe" run app.py --server.address 0.0.0.0 --server.headless false

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Server encountered an error. Press any key to exit.
    pause
)
