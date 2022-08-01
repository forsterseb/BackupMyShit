# BackupMyShit

Tired of Games overwriting a savegame all the time and not having backups?  
The solution is this python script, which creates backups of your savegame every x minutes.

## Usage
```shell
python backup.py -f Filename [-p Path] [-t Interval]
python backup.py -h #Help page with explanation of parameters
```
Filename: The file or folder to backup.  
Path: The directory where to store your backups. By default the parent directory of the original file/folder.  
Interval: The time interval in minutes in which the backups should be created. By default 5 minutes.  

In the target directory the 'Backups_dir' is created and contains all the backups.

To stop the script use `ctrl + c`.

## Future Ideas
- [x] Allow backup of whole directories
- [ ] Windows notification for each created backup

### Credit
Credit for the repo name goes to [@EzErenEz](https://github.com/EzErenEz).