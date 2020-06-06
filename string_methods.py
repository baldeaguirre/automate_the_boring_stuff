import pyperclip

spam = 'Hello world!'

spam = spam.upper()
print(spam, '\n')

spam = spam.lower()
print(spam, '\n')

# print('Do you wanna play again?')
# answer = input()
# answer = answer.lower()
#
# if answer == 'yes':
#     print('Playing again!', '\n')
# else:
#     print('See you next time!', '\n')

print(' '.join(['cats', 'rats', 'bats']), '\n')
print('\n'.join(['cats', 'rats', 'bats']), '\n')

print('My names is Balde'.split(), '\n')

spam = 'Hello'.rjust(100)
spam = spam.strip()
print(spam, '\n')

name = 'Balde'.center(100, '=')
print(name)
# name = name.lstrip('=')
# name = name.rstrip('=')
name = name.strip('=')
print(name, '\n')

name = 'Baldemar Aguirre Fraire'
name = name.replace('B', 'b')
name = name.replace('A', 'a')
name = name.replace('F', 'f')
print(name, '\n')

pyperclip.copy('Hello')
print(pyperclip.paste())