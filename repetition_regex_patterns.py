import re

# Match zero or one pattern ?
message = 'The Adventures of Batman'

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search(message)
print(mo.group())

message = 'The Adventures of Batwoman'
mo = batRegex.search(message)
print(mo.group(), '\n')

string1 = 'My phone number is 415-555-1234. Call me tomorrow'
string2 = 'My phone number is 555-1234. Call me tomorrow'

phoneNumRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneNumRegex.search(string1)
mo2 = phoneNumRegex.search(string2)
print(mo1.group())
print(mo2.group(), '\n')

string = 'dinner?'

dinnerRegex = re.compile(r'dinner\?')
mo = dinnerRegex.search(string)
print(mo.group(), '\n')

# Match zero or more patterns *
message = 'The Adventures of Batwowowoman'

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search(message)
print(mo.group(), '\n')

# Match one or more patterns +
message1 = 'The Adventures of Batman'
message2 = 'The Adventures of Batwoman'

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search(message1)
mo2 = batRegex.search(message2)
print(mo1)
print(mo2.group(), '\n')

# Escaping ?, * and +
string = 'I learned about +*? regex syntax'

regex = re.compile(r'\+\*\?')
mo = regex.search(string)
print(mo.group())

string = 'I learned about +*?+*?+*? regex syntax'

regex = re.compile(r'(\+\*\?)+')
mo = regex.search(string)
print(mo.group(), '\n')

# Match n times {x}
message = 'He said "HaHaHa"'

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search(message)
print(mo.group(), '\n')

message = 'My phone numbers are 415-555-1234,555-4242,212-555-0000'

phoneNumRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneNumRegex.search(message)
print(mo.group(), '\n')

# Match n times {x, y} (at least x times, at most y times)
message1 = 'He said "HaHaHa"'
message2 = 'He said "HaHaHaHaHa"'

haRegex = re.compile(r'(Ha){3,5}')
mo1 = haRegex.search(message1)
mo2 = haRegex.search(message2)
print(mo1.group())
print(mo2.group(), '\n')

message = 'He said "HaHaHaHaHaHaHa"'

haRegex = re.compile(r'(Ha){3,}') # more than three
mo = haRegex.search(message)
print(mo.group(), '\n')

# Greedy matching match the longest string possible, nongreedy matching match the shortest string possible
numbers = '1234567890'

digitRegex = re.compile(r'(\d){3,5}') # Greedy matching
mo = digitRegex.search(numbers)
print(mo.group())

# Putting a question mark after the curly braces makes it do a nongreedy match
digitRegex = re.compile(r'(\d){3,5}?') # Nongreedy matching
mo = digitRegex.search(numbers)
print(mo.group())