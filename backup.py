import os
import time
import shutil
import argparse
import datetime

DEFAULT_INTERVAL = 5
BACKUP_DEFAULT_DIR = "Backups_dir"

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-f', '--file', required=True, metavar='Filename', dest='file_path',
                    help='The path to the file to be backed up')
parser.add_argument('-p', '--path', required=False, metavar='Path', dest='backup_path',
                    help='The path where you want the backup to be stored')
parser.add_argument('-t', '--time', default=5, type=int, metavar="Interval", dest='interval',
                    help='The timeintervall in minutes in which the file should be backed up')

args = parser.parse_args()

if args.file_path is None:
    raise argparse.ArgumentError('Filepath must not be none')
file_path: str = args.file_path
file_parts = file_path.split('\\')[-1].split('.')

if args.interval is None:
    args.interval = DEFAULT_INTERVAL
interval: int = args.interval

if args.backup_path is None:
    path_parts = file_path.rsplit('\\',  maxsplit=1)
    # if only one argument -> only filename was given -> dir = .
    args.backup_path = f'./{BACKUP_DEFAULT_DIR}' if len(path_parts)==1 else f"{path_parts[0]}/{BACKUP_DEFAULT_DIR}" #save in dir of original file
backup_path: str = args.backup_path

file_name = file_parts[0]
file_ending = file_parts[1]

os.makedirs(backup_path, exist_ok=True)

while True:
    timestring = datetime.datetime.now().strftime('_%d.%m.%y_%H.%M.%S')
    new_filepath = f"{backup_path}\\{file_name}{timestring}.{file_ending}"
    shutil.copy2(file_path, new_filepath)
    print(f"Stored new Backup {new_filepath}")
    time.sleep(interval*60)