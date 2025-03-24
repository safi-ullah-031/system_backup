@echo off
:: Check if running as admin
net session >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Requesting admin privileges...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~s0' -Verb runAs"
    exit /b
)

:: Run Python backup script
python D:\system_backup\system_backup.py
