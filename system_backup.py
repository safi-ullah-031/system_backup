import os
import datetime
import sys
import ctypes

# Ensure script is run as Administrator
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Restarting script with Administrator privileges...")
    script = os.path.abspath(sys.argv[0])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "powershell.exe", f'python "{script}"', None, 1)
    sys.exit()

# Define backup location
backup_location = "D:\\SystemBackup"

# Ensure the directory exists
if not os.path.exists(backup_location):
    os.makedirs(backup_location)

# Generate a timestamped folder
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(backup_location, f"Backup_{timestamp}")

# PowerShell command to run wbAdmin with elevated privileges
command = f'''
Start-Process -Verb runAs -FilePath "wbAdmin" -ArgumentList 'start backup -backupTarget:{backup_folder} -include:C: -allCritical -quiet'
'''

print(f"Starting Windows system backup to {backup_folder}...\n")
os.system(f'powershell -Command "{command}"')
print("\nBackup process started!")
