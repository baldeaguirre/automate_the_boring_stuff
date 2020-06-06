import os
import shutil
import send2trash

# Delete a file from current directory
os.unlink('bacon.txt')

# Delete empty folders
os.rmdir()

# Delete folder and its content
shutil.rmtree()

for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print(filename)

# Send files / folders to the trash bin
send2trash.send2trash()