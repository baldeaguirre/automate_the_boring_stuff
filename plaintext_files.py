# Open Mode
helloFile = open('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff\\hello.txt')
content = helloFile.read()
print(content, '\n')
helloFile.close()

helloFile = open('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff\\hello.txt')
print(helloFile.readlines(), '\n')
helloFile.close()

# Write Mode
helloFile = open('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff\\hello2.txt', 'w')
helloFile.write('Hello!!!\n')
helloFile.close()

# Append Mode
# Appends text to the end of the file
helloFile = open('C:\\Users\\balde\\PycharmProjects\\projects\\automate the boring stuff\\hello2.txt', 'a')
helloFile.write('How are you?')
helloFile.close()

# Shelve Mode
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail']
shelfFile.close()

shelfFile = shelve.open('mydata')
print(shelfFile['cats'], '\n')
shelfFile.close()

# Keys / values methods
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()