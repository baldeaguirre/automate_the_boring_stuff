import shutil
shutil.copy('hello.txt', 'C:\\Users\\balde\\Documents')
shutil.copy('hello.txt', 'C:\\Users\\balde\\Documents\\hello_copy.txt') # rename copied file

# Copying folders
shutil.copytree('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff',
                'C:\\Users\\balde\\Documents\\automate the boring stuff_BACKUP')

# Moving files
shutil.move()

# Renaming files
shutil.move('hello2.txt', 'rename_hello2.txt')