import os
import sys
import ctypes

# Check if running as admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    # Relaunch script as Administrator
    print("Requesting Administrator Privileges...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

# Define the backup script location
backup_script = r"D:\system_backup\system_backup.py"
task_name = "Automated System Backup"

# Task Scheduler command
command = f'''
SCHTASKS /Create /TN "{task_name}" /TR "python {backup_script}" /SC DAILY /ST 02:00 /RL HIGHEST /F
'''

print("Creating scheduled task for system backup...")
os.system(command)
print("Scheduled task created successfully!")
