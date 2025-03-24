import os
import datetime
import ctypes
import sys
import time
import subprocess

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
backup_drive = "D:"
backup_folder = os.path.join(backup_drive, "SystemBackup")

# Ensure backup directory exists
if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

# Generate a timestamped backup directory
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_target = os.path.join(backup_folder, f"Backup_{timestamp}")

# Corrected Windows Backup Command
backup_command = [
    "wbAdmin", "start", "backup",
    "-backupTarget:D:",    # Backup drive
    "-include:C:",         # System drive
    "-allCritical",        # Ensure system files are included
    "-quiet"               # Run without asking for confirmation
]

print(f"Starting system backup to {backup_target}...\n")

# Run the backup command and capture output
process = subprocess.run(backup_command, shell=True, capture_output=True, text=True)

# Check for errors
if process.returncode == 0:
    print("\nBackup completed successfully!")
else:
    print("\nBackup failed. Error:")
    print(process.stderr)

# Delete old backups (older than 7 days)
retention_days = 7
for folder in os.listdir(backup_folder):
    folder_path = os.path.join(backup_folder, folder)
    if os.path.isdir(folder_path):
        creation_time = os.path.getctime(folder_path)
        if (time.time() - creation_time) > (retention_days * 24 * 60 * 60):
            os.rmdir(folder_path)  # Use os.rmdir() instead of shutil.rmtree()
            print(f"Deleted old backup: {folder_path}")
