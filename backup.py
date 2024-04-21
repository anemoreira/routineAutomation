
import shutil
import os
import datetime

def backup_files(source_dir, dest_dir):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(dest_dir, f"backup_{timestamp}")
    os.makedirs(backup_dir)
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(backup_dir, os.path.relpath(source_file, source_dir))
            shutil.copy2(source_file, dest_file)
