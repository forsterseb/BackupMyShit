import pathlib
from winotify import Notification, audio

par_dir = pathlib.Path(__file__).parent.resolve()
icon_file = f"{par_dir}/icon.png"

def showBackupFinishedToast(backupname, backupdir):
    toast = Notification(app_id="BackupMyShit", title=f"Backup {backupname} has been created.", icon=icon_file)
    toast.set_audio(audio.Default, loop=False)
    toast.add_actions(label="Show Backup", launch=f"file:///{backupdir}")
    toast.show()