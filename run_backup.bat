@echo off
:: Run script silently with admin privileges
powershell -Command "Start-Process python -ArgumentList 'D:\system_backup\system_backup.py' -WindowStyle Hidden -Verb RunAs"
