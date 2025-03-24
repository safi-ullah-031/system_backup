import os
import datetime
import shutil
import ctypes
import sys
import time

# Ensure script is running as Admin
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Restarting script with Administrator privileges...")
    script = os.path.abspath(sys.argv[0])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, script, None, 1)
    sys.exit()

# Define backup storage location
backup_location = "D:\\SystemBackup"

# Ensure backup directory exists
if not os.path.exists(backup_location):
    os.makedirs(backup_location)

# Generate a timestamped folder for each backup
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(backup_location, f"Backup_{timestamp}")

# Run Windows Backup Command with Elevated Permissions
backup_command = f'''
wbAdmin start backup -backupTarget:{backup_folder} -include:C: -allCritical -quiet
'''

print(f"Starting Windows system backup to {backup_folder}...\n")
os.system(backup_command)
print("\nBackup completed successfully!")

# Delete old backups (older than 7 days)
retention_days = 7
for folder in os.listdir(backup_location):
    folder_path = os.path.join(backup_location, folder)
    if os.path.isdir(folder_path):
        creation_time = os.path.getctime(folder_path)
        if (time.time() - creation_time) > (retention_days * 24 * 60 * 60):
            shutil.rmtree(folder_path)
            print(f"Deleted old backup: {folder_path}")
