print('What is your name?')
name = input()
if name == 'Alice':
    print('Hi Alice', '\n')
else:
    print('Hi ' + name, '\n')
print('Done!', '\n')

print('Write your password:')
password = input()
if password == 'swordfish':
    print('Access granted', '\n')
else:
    print('Wrong password', '\n')
print('Done!')

print('What is your name?')
name = input()
if name != '':
    print('Hello ' + str(name)) # True
else:
    print('You did not enter a name') # False