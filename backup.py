import os
import time
import shutil
import argparse
import datetime
from pathlib import Path

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

if args.interval is None:
    args.interval = DEFAULT_INTERVAL
interval: int = args.interval

if args.file_path is None:
    raise ValueError('Filepath must not be none')
file_path: str = args.file_path

if os.path.isfile(file_path):
    ## backup a file
    file_parts = file_path.split('\\')[-1].split('.')

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


if os.path.isdir(file_path): ## backup a directory
    path = Path(os.path.abspath(file_path))
    dir_name = path.name
    if args.backup_path is None:
        ## store in parent directory of backup dir
        parent_dir = path.parents[0]
        print(parent_dir)
        print(path.name)
        # if only one argument -> only filename was given -> dir = .
        args.backup_path = f"{parent_dir}/{BACKUP_DEFAULT_DIR}" #save in dir of original file
        #os.makedirs(args.backup_path, exist_ok=True)
    backup_path: str = args.backup_path

    while True:
        timestring = datetime.datetime.now().strftime('_%d.%m.%y_%H.%M.%S')
        new_filepath = f"{backup_path}\\{dir_name}{timestring}"
        shutil.copytree(file_path, new_filepath)
        print(f"Stored new Backup {new_filepath}")
        time.sleep(interval)