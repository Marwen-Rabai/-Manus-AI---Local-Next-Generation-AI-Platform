@echo off
echo Starting Manus AI...
echo.
echo This will:
echo 1. Install dependencies (if needed)
echo 2. Start the web server
echo 3. Open the interface in your browser
echo.
echo Press any key to continue...
pause >nul

powershell -ExecutionPolicy Bypass -File "run.ps1" serve

echo.
echo Server stopped. Press any key to exit...
pause >nul
