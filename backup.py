import os
import time
import shutil
import argparse
import datetime
from pathlib import Path

DEFAULT_INTERVAL = 5
BACKUP_DEFAULT_DIR = "Backups_dir"

# ArgumentParser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--file', required=True, metavar='Filename', dest='file_path',
                    help='The path to the file to be backed up')
parser.add_argument('-p', '--path', required=False, metavar='Path', dest='backup_path',
                    help='The path where you want the backup to be stored')
parser.add_argument('-t', '--time', default=5, type=int, metavar="Interval", dest='interval',
                    help='The timeintervall in minutes in which the file should be backed up')
parser.add_argument('-n', '--notification', action='store_true',
                    help="Use this argument to get a windows notification after each backup")

# read args or set default values
args = parser.parse_args()
print(args.notification)
if args.interval is None:
    args.interval = DEFAULT_INTERVAL
interval: int = args.interval

if args.file_path is None:
    raise ValueError('Filepath must not be none')
file_path: str = args.file_path
path = Path(os.path.abspath(file_path))

if args.backup_path is None:
    # save in dir of parent directory
    parent_dir = path.parent
    args.backup_path = parent_dir
backup_path: str = f"{os.path.abspath(args.backup_path)}\\{BACKUP_DEFAULT_DIR}"
os.makedirs(backup_path, exist_ok=True)

isFilepathFile = os.path.isfile(file_path)
isFilepathDir = os.path.isdir(file_path)

if (args.notification):
    from toaster import showBackupFinishedToast

# create backup-names
if isFilepathFile:
    file_parts = file_path.split('\\')[-1].split('.')
    file_name = file_parts[0]
    file_ending = file_parts[1]
if isFilepathDir:
    dir_name = path.name

# backup-loop
while True:
    timestring = datetime.datetime.now().strftime('_%d.%m.%y_%H.%M.%S')
    if isFilepathFile:
        new_filepath = f"{backup_path}\\{file_name}{timestring}.{file_ending}"
        shutil.copy2(file_path, new_filepath)
    if isFilepathDir:
        new_filepath = f"{backup_path}\\{dir_name}{timestring}"
        shutil.copytree(file_path, new_filepath)

    print(f"Stored new Backup {new_filepath}")
    if (args.notification):
        showBackupFinishedToast(new_filepath.rsplit('\\', maxsplit=1)[-1], backup_path)
    time.sleep(interval*60)