import os

for folderName, subfolders, filenames in os.walk('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff'):
    print('The folder is: ' + folderName)
    print('The subfolders in: ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in: ' + folderName + ' are: ' + str(filenames), '\n')