# Minecraft-Bedrock-Dedicated-Server-Auto-Backuper
This only works for windows
Please note this is my first python program that manages files and there are probably better ways to do this.

You must have python installed for this to run
You also need pynput,pygame,shutil,time,datetime installed for this to work.

1. put the autobackup.pyw in the same folder as the server.exe file
2. open the python file with the idle 
3. edit the backup interval to change how often it backups 
4. change the world name to the same thing in the server.properties file
5. run the python file
6. use f1 to pause when you click on the window with a circle and f2 to unpause
7. to stop it go to the controll window and press f3 then click on the command prompt

When it is running you can't do anything else on the computer or else it will not backup.
You can pause it to do other things on your computer.
If the python window closes type stop in the command window and press enter.
This will boot everyone from the server while saving, but will come right back up.
The backups are stored in the backup folder in the server folder labeld day, month, year, hour, minute, second.
To replace world with a backup rename the world file and copy it to the worlds folder.
