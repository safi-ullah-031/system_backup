import os

# Define the backup script location (Change this to the actual path)
backup_script = r"D:\system_backup\system_backup.py"

# Define task name
task_name = "Automated System Backup"

# Define task creation command
command = f'''
SCHTASKS /Create /TN "{task_name}" /TR "python {backup_script}" /SC DAILY /ST 02:00 /RL HIGHEST /F
'''

print("Creating scheduled task for system backup...")
os.system(command)
print("Scheduled task created successfully!")
