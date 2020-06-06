spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))
print(spam.index('heyas'), '\n')

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam, '\n')
spam.remove('moose')
print(spam, '\n')

spam.insert(1, 'chicken')
print(spam, '\n')

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam, '\n')

spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)
spam.sort(reverse=True)
print(spam, '\n')

spam = ['Z', 'A', 'z', 'a']
spam.sort(key=str.lower)
print(spam)