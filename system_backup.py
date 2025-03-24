import os
import datetime

# Define backup destination (Change 'D:\\SystemBackup' to your preferred location)
backup_location = "D:\\SystemBackup"

# Ensure the backup directory exists
if not os.path.exists(backup_location):
    os.makedirs(backup_location)

# Generate timestamp for unique backups
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_folder = os.path.join(backup_location, f"Backup_{timestamp}")

# Windows Backup Command
command = f'wbAdmin start backup -backupTarget:{backup_folder} -include:C: -allCritical -quiet'

print(f"Starting Windows system backup to {backup_folder}...\n")
os.system(command)
print("\nBackup completed successfully!")
