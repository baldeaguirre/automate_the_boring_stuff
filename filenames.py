import os
os.getcwd() # Get current working directory
os.chdir # Change working directory

# Get size of files
os.path.getsize('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff\\phoneAndEmail.py')

# List files of a directory
os.listdir('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff')

totalSize = 0
for filename in os.listdir('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff'):
    if not os.path.isfile(os.path.join('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff', filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff', filename))

print(totalSize, '\n')

# Create folders
os.makedirs('C:\\delicious\\walnut\\waffles')